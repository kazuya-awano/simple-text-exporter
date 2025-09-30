import os
from enum import StrEnum

class MimeType(StrEnum):
    CSS = "text/css"
    CSV = "text/csv"
    HTML = "text/html"
    JS = "text/javascript"
    JAVA = "text/x-java-source"
    JSON = "application/json"
    LATEX = "application/x-tex"
    MD = "text/markdown"
    PHP = "application/x-httpd-php"
    PY = "text/x-python"
    RST = "text/prs.fallenstein.rst"
    RUBY = "text/x-ruby"
    TXT = "text/plain"
    SH = "application/x-sh"
    XML = "text/xml"
    YAML = "text/yaml"

    @classmethod
    def guess_mime_type(cls, filename: str) -> "MimeType":
        _, ext = os.path.splitext(filename.lower())
        ext_map = {
            ".css": cls.CSS,
            ".csv": cls.CSV,
            ".html": cls.HTML,
            ".htm": cls.HTML,
            ".js": cls.JS,
            ".java": cls.JAVA,
            ".json": cls.JSON,
            ".tex": cls.LATEX,
            ".md": cls.MD,
            ".php": cls.PHP,
            ".py": cls.PY,
            ".rst": cls.RST,
            ".rb": cls.RUBY,
            ".txt": cls.TXT,
            ".sh": cls.SH,
            ".xml": cls.XML,
            ".yaml": cls.YAML,
            ".yml": cls.YAML,
        }
        return ext_map.get(ext, cls.TXT)
