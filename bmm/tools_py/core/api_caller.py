"""
APICaller - HTTP API caller for agents.

NOTA: Implementação completa será feita no Dia 2.
Este é um stub temporário para não quebrar imports.
"""

import requests
from typing import Optional, Dict, Any, Literal


class APICaller:
    """
    Generic HTTP API caller for agents.

    Supports GET, POST, PUT, DELETE with headers and auth.

    TODO (Dia 2): Implementar todos os métodos completamente.
    """

    def __init__(
        self,
        base_url: Optional[str] = None,
        default_headers: Optional[Dict[str, str]] = None
    ):
        """
        Initialize API caller.

        Args:
            base_url: Base URL for API (optional)
            default_headers: Default headers for all requests (optional)
        """
        self.base_url = base_url
        self.default_headers = default_headers or {}
        self.timeout = 30  # seconds

    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[tuple] = None
    ) -> Dict[str, Any]:
        """
        Make GET request.

        TODO (Dia 2): Implementar completamente.
        """
        return {
            "success": False,
            "status_code": None,
            "data": None,
            "error": "APICaller não implementado ainda (Dia 2)"
        }

    def post(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[tuple] = None
    ) -> Dict[str, Any]:
        """
        Make POST request.

        TODO (Dia 2): Implementar completamente.
        """
        return {
            "success": False,
            "status_code": None,
            "data": None,
            "error": "APICaller não implementado ainda (Dia 2)"
        }

    def put(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[tuple] = None
    ) -> Dict[str, Any]:
        """Make PUT request. TODO (Dia 2)."""
        return {
            "success": False,
            "status_code": None,
            "data": None,
            "error": "APICaller não implementado ainda (Dia 2)"
        }

    def delete(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[tuple] = None
    ) -> Dict[str, Any]:
        """Make DELETE request. TODO (Dia 2)."""
        return {
            "success": False,
            "status_code": None,
            "data": None,
            "error": "APICaller não implementado ainda (Dia 2)"
        }
