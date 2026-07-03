from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class RawModel:

    symbols: list

    imports: list

    calls: list

    contains: list

@dataclass
class ResolvedModel:

    symbols: list

    imports: list

    calls: list

    contains: list

class SymbolTable:

    def __init__(self):

        self.table: Dict[str, str] = {}

    def register(
        self,
        name: str,
        fqdn: str
    ):

        self.table[name] = fqdn

    def resolve(
        self,
        name: str
    ) -> Optional[str]:

        return self.table.get(name)

class SymbolResolver:

    def __init__(self):

        self.symbol_table = SymbolTable()

    def resolve(
        self,
        model: RawModel
    ) -> ResolvedModel:
        self._index_symbols(model)

        return ResolvedModel(
            symbols=self._resolve_symbols(model),
            imports=self._resolve_imports(model),
            calls=self._resolve_calls(model),
            contains=self._resolve_contains(model)
        )
        
    def _index_symbols(self, model: RawModel):

        for symbol in model.symbols:

            self.symbol_table.register(
                symbol.name,
                symbol.fqdn
            )

    def _resolve_symbols(self, model: RawModel):

        resolved = []

        for s in model.symbols:

            resolved.append({
                "name": s.name,
                "fqdn": s.fqdn,
                "type": s.type,
                "file": s.file,
                "line": s.line,
                "resolved": True
            })

        return resolved

    def _resolve_imports(self, model: RawModel):

        resolved = []

        for imp in model.imports:

            target = self.symbol_table.resolve(imp.target)

            resolved.append({
                "source": imp.source,
                "target": target or imp.target,
                "confidence": 1.0 if target else 0.3
            })

        return resolved

    def _resolve_calls(self, model: RawModel):

        resolved = []

        for call in model.calls:

            caller = self.symbol_table.resolve(call.caller)
            callee = self.symbol_table.resolve(call.callee)

            if caller and callee:
                confidence = 1.0 # FULL

            elif callee:
                confidence = 0.7 # PARTIAL

            else:
                confidence = 0.2 # WEAK

            resolved.append({
                "caller": caller or call.caller,
                "callee": callee or call.callee,
                "confidence": confidence
            })

        return resolved

    def _resolve_contains(self, model: RawModel):

        resolved = []

        for rel in model.contains:

            parent = self.symbol_table.resolve(rel.parent)
            child = self.symbol_table.resolve(rel.child)

            resolved.append({
                "parent": parent or rel.parent,
                "child": child or rel.child,
                "confidence": 1.0
            })

        return resolved