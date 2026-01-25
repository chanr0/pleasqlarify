"""
Tests for the SQL Clarifier
"""

import pytest
from pleasqlarify import SQLClarifier


class TestSQLClarifier:
    """Test cases for SQLClarifier class."""
    
    def test_init(self):
        """Test clarifier initialization."""
        clarifier = SQLClarifier()
        assert clarifier is not None
        assert clarifier.config == {}
    
    def test_init_with_config(self):
        """Test clarifier initialization with config."""
        config = {"option": "value"}
        clarifier = SQLClarifier(config=config)
        assert clarifier.config == config
    
    def test_clarify_simple_select(self):
        """Test clarifying a simple SELECT query."""
        clarifier = SQLClarifier()
        query = "SELECT * FROM users WHERE age > 25"
        result = clarifier.clarify(query)
        
        assert "query" in result
        assert "formatted" in result
        assert "explanation" in result
        assert "components" in result
        assert result["query"] == query
    
    def test_clarify_empty_query(self):
        """Test clarifying an empty query."""
        clarifier = SQLClarifier()
        result = clarifier.clarify("")
        
        assert "error" in result or "query" in result
    
    def test_clarify_invalid_query(self):
        """Test clarifying an invalid query."""
        clarifier = SQLClarifier()
        query = "INVALID SQL QUERY"
        result = clarifier.clarify(query)
        
        # Should still return some result structure
        assert result is not None
        assert isinstance(result, dict)
    
    def test_formatted_query(self):
        """Test that formatted query is properly formatted."""
        clarifier = SQLClarifier()
        query = "select * from users where age>25"
        result = clarifier.clarify(query)
        
        assert "formatted" in result
        # Formatted should have uppercase keywords
        assert "SELECT" in result["formatted"]
        assert "FROM" in result["formatted"]
        assert "WHERE" in result["formatted"]
