"""
Custom CSV Reader implementation.
"""


class CustomCsvReader:
    """
    A custom CSV reader that parses CSV files.
    """
    def __init__(self, file_path):
        self.file = open(file_path, "r", newline="")
        self.inside_quotes = False
        self.current_field = []
        self.current_row = []
        self.eof = False
        self.buffer = ""
        self.buffer_pos = 0
        # Read in larger chunks for better I/O performance
        self.buffer_size = 8192

    def _read_char(self):
        """
        Read a single character with buffering to reduce I/O calls.
        """
        if self.buffer_pos >= len(self.buffer):
            self.buffer = self.file.read(self.buffer_size)
            self.buffer_pos = 0
            if not self.buffer:
                return ""

        char = self.buffer[self.buffer_pos]
        self.buffer_pos += 1
        return char

    def _peek_char(self):
        """
        Peek at the next character without consuming it.
        """
        if self.buffer_pos >= len(self.buffer):
            self.buffer = self.file.read(self.buffer_size)
            self.buffer_pos = 0
            if not self.buffer:
                return ""

        return self.buffer[self.buffer_pos]

    def _finalize_row(self):
        """
        Finalize and return the current row.
        """
        # Add the current field to the row
        self.current_row.append("".join(self.current_field))
        row = self.current_row

        # Reset state
        self.current_field = []
        self.current_row = []

        # Handle empty lines: if row is [''], it represents a blank line,
        # return []
        if row == ['']:
            return []

        return row

    def __iter__(self):
        return self

    def __next__(self):
        if self.eof:
            self.file.close()
            raise StopIteration

        while True:
            char = self._read_char()

            # Handle EOF
            if char == "":
                self.eof = True
                # Only return a row if we have accumulated any data
                # Don't return empty row if both current_field and
                # current_row are empty
                if self.current_field or self.current_row:
                    return self._finalize_row()
                self.file.close()
                raise StopIteration

            # Handle quoted fields
            if char == '"':
                if self.inside_quotes:
                    next_char = self._peek_char()
                    if next_char == '"':
                        self._read_char()  # Consume the peeked quote
                        self.current_field.append('"')
                    else:
                        self.inside_quotes = False
                else:
                    self.inside_quotes = True

            # Handle field delimiter
            elif char == "," and not self.inside_quotes:
                self.current_row.append("".join(self.current_field))
                self.current_field = []

            # Handle line breaks
            elif char == "\n" and not self.inside_quotes:
                return self._finalize_row()

            elif char == "\r":
                next_char = self._peek_char()

                # Consume \n if it's part of CRLF
                if next_char == "\n":
                    self._read_char()

                if not self.inside_quotes:
                    return self._finalize_row()
                else:
                    # Preserve line breaks inside quoted fields
                    self.current_field.append("\r")
                    if next_char == "\n":
                        self.current_field.append("\n")

            # Handle regular characters
            else:
                self.current_field.append(char)

    def __enter__(self):
        """
        Support context manager protocol.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Ensure file is closed when used as context manager.
        """
        if hasattr(self, 'file') and self.file:
            self.file.close()
        return False