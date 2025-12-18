"""
Custom CSV Writer implementation.
"""


class CustomCsvWriter:
    """
    A custom CSV writer that formats and writes data to CSV files.
    """

    def __init__(self, file_path):
        """
        Initialize the CSV writer.
        """
        self.file_path = file_path

    def _format_field(self, field: str) -> str:
        """
        Format a field for CSV output.
        """
        if not isinstance(field, str):
            field = str(field)

        if "," in field or '"' in field or "\n" in field:
            field = field.replace('"', '""')
            return f'"{field}"'

        return field

    def write(self, data):
        """
        Write data to CSV file.
        """
        with open(self.file_path, "w", newline="") as file:
            for row in data:
                formatted_fields = [
                    self._format_field(field) for field in row
                ]
                line = ",".join(formatted_fields)
                file.write(line + "\n")