"""
Unit tests for SystemFileHandler.

Run with: pytest tests/test_file_handler.py -v
"""

import pytest
import tempfile
import shutil
from pathlib import Path
from bmm.tools_py.core.file_handler import SystemFileHandler


class TestSystemFileHandler:
    """Test suite for SystemFileHandler."""

    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for tests."""
        temp_path = tempfile.mkdtemp()
        yield temp_path
        shutil.rmtree(temp_path)

    @pytest.fixture
    def handler(self, temp_dir):
        """Create handler instance with temp directory."""
        return SystemFileHandler(base_path=temp_dir)

    def test_write_file_creates_file(self, handler, temp_dir):
        """Test that write_file creates a file successfully."""
        result = handler.write_file("test.txt", "Hello World")

        assert result["success"] is True
        assert "written to" in result["message"]
        assert result["bytes_written"] > 0
        assert Path(temp_dir, "test.txt").exists()

    def test_write_file_creates_directories(self, handler, temp_dir):
        """Test that write_file creates parent directories."""
        result = handler.write_file("subdir/test.txt", "Content")

        assert result["success"] is True
        assert Path(temp_dir, "subdir", "test.txt").exists()

    def test_write_file_overwrite_mode(self, handler, temp_dir):
        """Test overwrite mode replaces content."""
        handler.write_file("test.txt", "First")
        result = handler.write_file("test.txt", "Second", mode="overwrite")

        assert result["success"] is True

        content = Path(temp_dir, "test.txt").read_text()
        assert content == "Second"

    def test_write_file_append_mode(self, handler, temp_dir):
        """Test append mode adds to existing content."""
        handler.write_file("test.txt", "First\n")
        result = handler.write_file("test.txt", "Second\n", mode="append")

        assert result["success"] is True

        content = Path(temp_dir, "test.txt").read_text()
        assert "First" in content
        assert "Second" in content

    def test_read_file_success(self, handler, temp_dir):
        """Test reading existing file."""
        test_content = "Test content here"
        handler.write_file("test.txt", test_content)

        result = handler.read_file("test.txt")

        assert result["success"] is True
        assert result["content"] == test_content
        assert result["error"] is None

    def test_read_file_not_found(self, handler):
        """Test reading non-existent file."""
        result = handler.read_file("nonexistent.txt")

        assert result["success"] is False
        assert "not found" in result["error"].lower()

    def test_read_file_is_directory(self, handler, temp_dir):
        """Test reading a directory instead of file."""
        Path(temp_dir, "testdir").mkdir()

        result = handler.read_file("testdir")

        assert result["success"] is False
        assert "not a file" in result["error"].lower()

    def test_list_directory_empty(self, handler):
        """Test listing empty directory."""
        result = handler.list_directory(".")

        assert result["success"] is True
        assert result["files"] == []
        assert result["count"] == 0

    def test_list_directory_with_files(self, handler, temp_dir):
        """Test listing directory with files."""
        # Create test files
        Path(temp_dir, "file1.txt").touch()
        Path(temp_dir, "file2.txt").touch()
        Path(temp_dir, "file3.md").touch()

        result = handler.list_directory(".")

        assert result["success"] is True
        assert result["count"] == 3
        assert len(result["files"]) == 3

    def test_list_directory_with_pattern(self, handler, temp_dir):
        """Test listing with glob pattern."""
        # Create test files
        Path(temp_dir, "file1.txt").touch()
        Path(temp_dir, "file2.txt").touch()
        Path(temp_dir, "file3.md").touch()

        result = handler.list_directory(".", pattern="*.txt")

        assert result["success"] is True
        assert result["count"] == 2
        assert all(f.endswith(".txt") for f in result["files"])

    def test_list_directory_recursive(self, handler, temp_dir):
        """Test recursive directory listing."""
        # Create nested structure
        Path(temp_dir, "subdir").mkdir()
        Path(temp_dir, "file1.txt").touch()
        Path(temp_dir, "subdir", "file2.txt").touch()

        result = handler.list_directory(".", pattern="*.txt", recursive=True)

        assert result["success"] is True
        assert result["count"] == 2

    def test_list_directory_not_found(self, handler):
        """Test listing non-existent directory."""
        result = handler.list_directory("nonexistent")

        assert result["success"] is False
        assert "not found" in result["error"].lower()

    def test_file_exists_true(self, handler, temp_dir):
        """Test file_exists for existing file."""
        Path(temp_dir, "test.txt").touch()

        result = handler.file_exists("test.txt")

        assert result["success"] is True
        assert result["exists"] is True
        assert result["is_file"] is True

    def test_file_exists_false(self, handler):
        """Test file_exists for non-existent file."""
        result = handler.file_exists("nonexistent.txt")

        assert result["success"] is True
        assert result["exists"] is False

    def test_get_file_info(self, handler, temp_dir):
        """Test getting file metadata."""
        test_content = "Test content"
        handler.write_file("test.txt", test_content)

        result = handler.get_file_info("test.txt")

        assert result["success"] is True
        assert result["size_bytes"] > 0
        assert result["extension"] == ".txt"

    def test_encoding_utf8(self, handler):
        """Test UTF-8 encoding."""
        content = "Testing UTF-8: café, naïve, 日本語"
        handler.write_file("test.txt", content, encoding="utf-8")

        result = handler.read_file("test.txt", encoding="utf-8")

        assert result["success"] is True
        assert result["content"] == content

    def test_large_file(self, handler):
        """Test handling large file content."""
        large_content = "A" * 1000000  # 1MB of data

        write_result = handler.write_file("large.txt", large_content)
        read_result = handler.read_file("large.txt")

        assert write_result["success"] is True
        assert read_result["success"] is True
        assert len(read_result["content"]) == 1000000


class TestConvenienceFunctions:
    """Test convenience functions."""

    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for tests."""
        temp_path = tempfile.mkdtemp()
        yield temp_path
        shutil.rmtree(temp_path)

    def test_quick_write_file(self, temp_dir):
        """Test quick write_file function."""
        from bmm.tools_py.core.file_handler import write_file

        result = write_file("test.txt", "Content", base_path=temp_dir)

        assert result["success"] is True
        assert Path(temp_dir, "test.txt").exists()

    def test_quick_read_file(self, temp_dir):
        """Test quick read_file function."""
        from bmm.tools_py.core.file_handler import read_file, write_file

        write_file("test.txt", "Content", base_path=temp_dir)
        result = read_file("test.txt", base_path=temp_dir)

        assert result["success"] is True
        assert result["content"] == "Content"

    def test_quick_list_directory(self, temp_dir):
        """Test quick list_directory function."""
        from bmm.tools_py.core.file_handler import list_directory

        Path(temp_dir, "file1.txt").touch()
        Path(temp_dir, "file2.txt").touch()

        result = list_directory(".", base_path=temp_dir)

        assert result["success"] is True
        assert result["count"] == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
