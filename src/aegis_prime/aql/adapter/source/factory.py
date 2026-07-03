from .json_source import JsonStdinSource
from .csv_source import CsvSource
from .log_stdin import LogStdinSource
from .xml_source import XmlSource
from .yml_source import YamlSource

class StdinSourceFactory:
    @staticmethod
    def from_raw(raw: str):
        raw = raw.strip()

        # JSON (fast path)
        if raw.startswith("{") or raw.startswith("["):
            return JsonStdinSource(raw)

        # CSV (simple heuristic)
        if "," in raw and "\n" in raw:
            return CsvSource(raw)

        # YAML
        if raw.endswith(":\n"):
            try:
                import yaml
                yaml.safe_load(raw)
                return YamlSource(raw)
            except Exception:
                pass

        # XML
        if raw.startswith("<"):
            return XmlSource(raw)

        # fallback
        return LogStdinSource(raw)