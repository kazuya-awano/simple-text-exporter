from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.mimetype import MimeType

class SimpleTextExporterTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        text = tool_parameters.get("text")
        output_filename = tool_parameters.get("output_filename")
        result_file_bytes = text.encode("utf-8")

        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={
                "mime_type": MimeType.guess_mime_type(output_filename),
                "filename": output_filename,
            }
        )
        return
