"""
SQL Parser Module

Provides SQL parsing functionality.
"""

import sqlparse
from typing import Dict, List


class SQLParser:
    """
    Parser for SQL queries.
    
    Provides methods to parse and analyze SQL query structure.
    """
    
    def __init__(self):
        """Initialize the SQL Parser."""
        pass
    
    def parse(self, query: str) -> Dict:
        """
        Parse a SQL query and extract structural information.
        
        Args:
            query: SQL query string
            
        Returns:
            Dictionary containing parsed query information
        """
        parsed = sqlparse.parse(query)
        
        if not parsed:
            return {"error": "Unable to parse query"}
        
        statement = parsed[0]
        
        return {
            "tokens": self._extract_tokens(statement),
            "type": self._get_query_type(statement),
            "tables": self._extract_tables(statement),
            "keywords": self._extract_keywords(statement)
        }
    
    def _extract_tokens(self, statement) -> List[Dict]:
        """
        Extract tokens from the statement.
        
        Args:
            statement: Parsed SQL statement
            
        Returns:
            List of token dictionaries
        """
        tokens = []
        for token in statement.tokens:
            if not token.is_whitespace:
                tokens.append({
                    "value": str(token),
                    "type": str(token.ttype) if token.ttype else "Unknown"
                })
        return tokens
    
    def _get_query_type(self, statement) -> str:
        """
        Determine the type of SQL query.
        
        Args:
            statement: Parsed SQL statement
            
        Returns:
            Query type string (SELECT, INSERT, UPDATE, DELETE, etc.)
        """
        for token in statement.tokens:
            if token.ttype is sqlparse.tokens.Keyword.DML:
                return token.value.upper()
        return "UNKNOWN"
    
    def _extract_tables(self, statement) -> List[str]:
        """
        Extract table names from the statement.
        
        Args:
            statement: Parsed SQL statement
            
        Returns:
            List of table names
        """
        tables = []
        for token in statement.tokens:
            if hasattr(token, 'get_name') and token.get_name():
                tables.append(token.get_name())
        return tables
    
    def _extract_keywords(self, statement) -> List[str]:
        """
        Extract SQL keywords from the statement.
        
        Args:
            statement: Parsed SQL statement
            
        Returns:
            List of keywords
        """
        keywords = []
        for token in statement.tokens:
            if token.ttype in sqlparse.tokens.Keyword:
                keywords.append(token.value.upper())
        return keywords
