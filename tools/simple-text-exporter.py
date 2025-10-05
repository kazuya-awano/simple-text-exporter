from collections.abc import Generator
from typing import Any
from datetime import datetime, timezone

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.utils.mimetype import MimeType

class SimpleTextExporterTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        text = tool_parameters.get("text")
        output_filename = tool_parameters.get("output_filename")
        add_timestamp = tool_parameters.get("add_timestamp", False)
        result_file_bytes = text.encode("utf-8")

        # add timestamp (UTC)
        if add_timestamp:
            name_parts = output_filename.split(".", 1)
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
            if len(name_parts) == 2:
                base, ext = name_parts
                output_filename = f"{base}_{timestamp}_UTC.{ext}"
            else:
                output_filename = f"{output_filename}_{timestamp}_UTC"

        yield self.create_blob_message(
            blob=result_file_bytes,
            meta={
                "mime_type": MimeType.guess_mime_type(output_filename),
                "filename": output_filename,
            }
        )
        return
