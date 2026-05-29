import sys
from aegis_prime.aql.adapter.dataset import Dataset
from aegis_prime.aql.link.registry import FUNCTION_CALL_REGISTRY
from aegis_prime.aql.link import fn_call
from aegis_prime.aql.language.ast.function_call import TableFunctionCall
from aegis_prime.aql.language.ast.identifier import Identifier
from aegis_prime.aql.language.ast.expressions.literals import Literal

class SourceResolver:
    def __init__(self, data_sources):
        self.data_sources = data_sources

    def resolve(self, ast_node, include_schema: bool = False):
        if(isinstance(ast_node, str)):
            return self.resolve_identifier(ast_node, include_schema)
        elif(isinstance(ast_node, Identifier)):
            return self.resolve_identifier(ast_node.name, include_schema)
        elif(isinstance(ast_node, TableFunctionCall)):
            return self.resolve_tbl_function(ast_node)
    
    def resolve_tbl_function(self, fn_type):
        raw = fn_type.arg

        if isinstance(raw, Literal):
            raw = raw.value

        fn_cls = FUNCTION_CALL_REGISTRY.get(fn_type.name)

        if not fn_cls:
            raise Exception(f"Unknown table function: {fn_type.name}")

        fn = fn_cls()

        source = fn.execute(raw)

        return source.as_rows() #, dataset.schema()
            
    
    def resolve_identifier(self, source_name, include_schema: bool):
        factory = self.data_sources.get(source_name)

        if factory is None:
            raise ValueError(f"Unknown source: {source_name}")

        # ✅ stdin case
        if source_name == "stdin":
            raw = sys.stdin.read()
            source = factory.from_raw(raw)

            dataset = source.to_dataset()   # 👈 normalize here
            return dataset.as_rows(), dataset.schema()

        # ✅ normal sources
        source = factory  # or factory.build()

        dataset = source.to_dataset()       # 👈 REQUIRED
        
        if include_schema == False:
            return dataset.as_rows()
        
        return dataset.as_rows(), dataset.schema()