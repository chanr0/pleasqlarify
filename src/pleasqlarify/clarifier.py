"""
SQL Query Clarifier

Main module for clarifying SQL queries.
"""

from typing import Dict, List, Optional
import sqlparse


class SQLClarifier:
    """
    Main class for clarifying SQL queries.
    
    This class provides methods to analyze and explain SQL queries
    in a user-friendly manner.
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize the SQL Clarifier.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        
    def clarify(self, query: str) -> Dict:
        """
        Clarify a SQL query by providing explanations and insights.
        
        Args:
            query: SQL query string to clarify
            
        Returns:
            Dictionary containing clarification information
        """
        parsed = sqlparse.parse(query)
        
        if not parsed:
            return {
                "error": "Unable to parse query",
                "query": query
            }
        
        statement = parsed[0]
        
        return {
            "query": query,
            "formatted": sqlparse.format(
                query,
                reindent=True,
                keyword_case='upper'
            ),
            "explanation": self._generate_explanation(statement),
            "components": self._extract_components(statement)
        }
    
    def _generate_explanation(self, statement) -> str:
        """
        Generate a natural language explanation of the query.
        
        Args:
            statement: Parsed SQL statement
            
        Returns:
            Natural language explanation string
        """
        # Basic explanation generation
        explanation_parts = []
        
        tokens = [token for token in statement.tokens if not token.is_whitespace]
        
        for token in tokens:
            if token.ttype is sqlparse.tokens.Keyword.DML:
                if token.value.upper() == 'SELECT':
                    explanation_parts.append("Retrieve data")
            elif token.ttype is sqlparse.tokens.Keyword:
                if token.value.upper() == 'FROM':
                    explanation_parts.append("from the specified table(s)")
                elif token.value.upper() == 'WHERE':
                    explanation_parts.append("filtering by conditions")
        
        return " ".join(explanation_parts) if explanation_parts else "SQL query"
    
    def _extract_components(self, statement) -> Dict:
        """
        Extract key components from the SQL statement.
        
        Args:
            statement: Parsed SQL statement
            
        Returns:
            Dictionary of query components
        """
        components = {
            "tables": [],
            "columns": [],
            "conditions": [],
            "operations": []
        }
        
        # Extract components from the parsed statement
        for token in statement.tokens:
            if hasattr(token, 'get_name') and token.get_name():
                components["tables"].append(token.get_name())
        
        return components
