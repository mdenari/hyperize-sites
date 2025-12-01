"""
SystemFileHandler - File operations for agents.

Permite que agents leiam, escrevam e listem arquivos no sistema.
Essencial para gerar outputs tangíveis (relatórios, templates, configs).

Usage:
    handler = SystemFileHandler()

    # Read file
    result = handler.read_file("reports/analysis.md")
    if result["success"]:
        print(result["content"])

    # Write file
    result = handler.write_file("output.txt", "Content here")

    # List directory
    result = handler.list_directory("reports", pattern="*.md")
    print(result["files"])
"""

from pathlib import Path
from typing import Optional, List, Literal, Dict, Any


class SystemFileHandler:
    """
    File operations for agents (read, write, list).

    Security: Restricts operations to project directory by default.
    All methods return dict with success/error pattern for agent parsing.
    """

    def __init__(self, base_path: str = "."):
        """
        Initialize handler with base path.

        Args:
            base_path: Root directory for file operations (default: current dir)
        """
        self.base_path = Path(base_path).resolve()

    def read_file(
        self,
        file_path: str,
        encoding: str = "utf-8"
    ) -> Dict[str, Any]:
        """
        Read file contents.

        Args:
            file_path: Relative or absolute path to file
            encoding: File encoding (default: utf-8)

        Returns:
            {
                "success": bool,
                "content": str | None,
                "file_path": str,
                "error": str | None
            }

        Example:
            >>> handler = SystemFileHandler()
            >>> result = handler.read_file("reports/analysis.md")
            >>> if result["success"]:
            >>>     print(result["content"])
            >>> else:
            >>>     print(f"Error: {result['error']}")
        """
        try:
            path = self._resolve_path(file_path)

            if not path.exists():
                return {
                    "success": False,
                    "content": None,
                    "file_path": file_path,
                    "error": f"File not found: {file_path}"
                }

            if not path.is_file():
                return {
                    "success": False,
                    "content": None,
                    "file_path": file_path,
                    "error": f"Path is not a file: {file_path}"
                }

            content = path.read_text(encoding=encoding)

            return {
                "success": True,
                "content": content,
                "file_path": str(path.relative_to(self.base_path)),
                "error": None
            }

        except UnicodeDecodeError as e:
            return {
                "success": False,
                "content": None,
                "file_path": file_path,
                "error": f"Encoding error (try different encoding): {str(e)}"
            }
        except PermissionError:
            return {
                "success": False,
                "content": None,
                "file_path": file_path,
                "error": f"Permission denied: {file_path}"
            }
        except Exception as e:
            return {
                "success": False,
                "content": None,
                "file_path": file_path,
                "error": f"Read error: {str(e)}"
            }

    def write_file(
        self,
        file_path: str,
        content: str,
        mode: Literal["overwrite", "append"] = "overwrite",
        encoding: str = "utf-8",
        create_dirs: bool = True
    ) -> Dict[str, Any]:
        """
        Write content to file.

        Args:
            file_path: Relative or absolute path to file
            content: Content to write
            mode: "overwrite" (default) or "append"
            encoding: File encoding (default: utf-8)
            create_dirs: Create parent directories if needed (default: True)

        Returns:
            {
                "success": bool,
                "message": str | None,
                "file_path": str,
                "bytes_written": int,
                "error": str | None
            }

        Example:
            >>> handler = SystemFileHandler()
            >>> result = handler.write_file(
            >>>     "reports/summary.md",
            >>>     "# Summary\n\nContent here..."
            >>> )
            >>> print(result["message"])
        """
        try:
            path = self._resolve_path(file_path)

            # Create parent directories if needed
            if create_dirs:
                path.parent.mkdir(parents=True, exist_ok=True)

            if mode == "append":
                with open(path, 'a', encoding=encoding) as f:
                    f.write(content)
                action = "appended to"
            else:
                path.write_text(content, encoding=encoding)
                action = "written to"

            bytes_written = len(content.encode(encoding))

            return {
                "success": True,
                "message": f"Content {action}: {file_path}",
                "file_path": str(path.relative_to(self.base_path)),
                "bytes_written": bytes_written,
                "error": None
            }

        except PermissionError:
            return {
                "success": False,
                "message": None,
                "file_path": file_path,
                "bytes_written": 0,
                "error": f"Permission denied: {file_path}"
            }
        except OSError as e:
            return {
                "success": False,
                "message": None,
                "file_path": file_path,
                "bytes_written": 0,
                "error": f"OS error: {str(e)}"
            }
        except Exception as e:
            return {
                "success": False,
                "message": None,
                "file_path": file_path,
                "bytes_written": 0,
                "error": f"Write error: {str(e)}"
            }

    def list_directory(
        self,
        directory_path: str = ".",
        pattern: Optional[str] = None,
        recursive: bool = False,
        files_only: bool = True
    ) -> Dict[str, Any]:
        """
        List files in directory.

        Args:
            directory_path: Directory to list (default: current)
            pattern: Glob pattern (e.g., "*.py", "**/*.md")
            recursive: Search recursively (default: False)
            files_only: Return only files, not directories (default: True)

        Returns:
            {
                "success": bool,
                "files": List[str] | None,
                "count": int,
                "directory": str,
                "error": str | None
            }

        Example:
            >>> handler = SystemFileHandler()
            >>> result = handler.list_directory("reports", pattern="*.md")
            >>> print(f"Found {result['count']} markdown files:")
            >>> for file in result["files"]:
            >>>     print(f"  - {file}")
        """
        try:
            path = self._resolve_path(directory_path)

            if not path.exists():
                return {
                    "success": False,
                    "files": None,
                    "count": 0,
                    "directory": directory_path,
                    "error": f"Directory not found: {directory_path}"
                }

            if not path.is_dir():
                return {
                    "success": False,
                    "files": None,
                    "count": 0,
                    "directory": directory_path,
                    "error": f"Path is not a directory: {directory_path}"
                }

            # List files
            if pattern:
                if recursive:
                    items = list(path.rglob(pattern))
                else:
                    items = list(path.glob(pattern))
            else:
                items = list(path.iterdir())

            # Filter files only if requested
            if files_only:
                items = [item for item in items if item.is_file()]

            # Convert to relative paths (strings)
            file_paths = [str(item.relative_to(self.base_path)) for item in items]

            return {
                "success": True,
                "files": sorted(file_paths),
                "count": len(file_paths),
                "directory": str(path.relative_to(self.base_path)),
                "error": None
            }

        except PermissionError:
            return {
                "success": False,
                "files": None,
                "count": 0,
                "directory": directory_path,
                "error": f"Permission denied: {directory_path}"
            }
        except Exception as e:
            return {
                "success": False,
                "files": None,
                "count": 0,
                "directory": directory_path,
                "error": f"List error: {str(e)}"
            }

    def file_exists(self, file_path: str) -> Dict[str, Any]:
        """
        Check if file exists.

        Args:
            file_path: Path to check

        Returns:
            {
                "success": bool,
                "exists": bool,
                "is_file": bool,
                "is_dir": bool,
                "file_path": str
            }
        """
        try:
            path = self._resolve_path(file_path)

            return {
                "success": True,
                "exists": path.exists(),
                "is_file": path.is_file() if path.exists() else False,
                "is_dir": path.is_dir() if path.exists() else False,
                "file_path": file_path
            }
        except Exception as e:
            return {
                "success": False,
                "exists": False,
                "is_file": False,
                "is_dir": False,
                "file_path": file_path,
                "error": str(e)
            }

    def _resolve_path(self, file_path: str) -> Path:
        """
        Resolve path relative to base_path.

        Internal method - converts relative paths to absolute.
        """
        path = Path(file_path)
        if not path.is_absolute():
            path = self.base_path / path
        return path.resolve()

    def get_file_info(self, file_path: str) -> Dict[str, Any]:
        """
        Get file metadata.

        Args:
            file_path: Path to file

        Returns:
            {
                "success": bool,
                "size_bytes": int,
                "created": str,
                "modified": str,
                "extension": str,
                "error": str | None
            }
        """
        try:
            path = self._resolve_path(file_path)

            if not path.exists():
                return {
                    "success": False,
                    "error": f"File not found: {file_path}"
                }

            stat = path.stat()

            return {
                "success": True,
                "size_bytes": stat.st_size,
                "created": str(stat.st_ctime),
                "modified": str(stat.st_mtime),
                "extension": path.suffix,
                "error": None
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Info error: {str(e)}"
            }


# Convenience functions for quick access
def read_file(file_path: str, base_path: str = ".") -> Dict[str, Any]:
    """Quick read file without creating handler instance."""
    handler = SystemFileHandler(base_path)
    return handler.read_file(file_path)


def write_file(
    file_path: str,
    content: str,
    mode: Literal["overwrite", "append"] = "overwrite",
    base_path: str = "."
) -> Dict[str, Any]:
    """Quick write file without creating handler instance."""
    handler = SystemFileHandler(base_path)
    return handler.write_file(file_path, content, mode)


def list_directory(
    directory_path: str = ".",
    pattern: Optional[str] = None,
    base_path: str = "."
) -> Dict[str, Any]:
    """Quick list directory without creating handler instance."""
    handler = SystemFileHandler(base_path)
    return handler.list_directory(directory_path, pattern)
