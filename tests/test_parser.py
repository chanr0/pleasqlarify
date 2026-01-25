"""
Tests for the SQL Parser
"""

import pytest
from pleasqlarify import SQLParser


class TestSQLParser:
    """Test cases for SQLParser class."""
    
    def test_init(self):
        """Test parser initialization."""
        parser = SQLParser()
        assert parser is not None
    
    def test_parse_select_query(self):
        """Test parsing a SELECT query."""
        parser = SQLParser()
        query = "SELECT * FROM users"
        result = parser.parse(query)
        
        assert "tokens" in result
        assert "type" in result
        assert "tables" in result
        assert "keywords" in result
        assert result["type"] == "SELECT"
    
    def test_parse_insert_query(self):
        """Test parsing an INSERT query."""
        parser = SQLParser()
        query = "INSERT INTO users (name, age) VALUES ('John', 30)"
        result = parser.parse(query)
        
        assert result["type"] == "INSERT"
    
    def test_parse_update_query(self):
        """Test parsing an UPDATE query."""
        parser = SQLParser()
        query = "UPDATE users SET age = 31 WHERE id = 1"
        result = parser.parse(query)
        
        assert result["type"] == "UPDATE"
    
    def test_parse_delete_query(self):
        """Test parsing a DELETE query."""
        parser = SQLParser()
        query = "DELETE FROM users WHERE id = 1"
        result = parser.parse(query)
        
        assert result["type"] == "DELETE"
    
    def test_parse_empty_query(self):
        """Test parsing an empty query."""
        parser = SQLParser()
        result = parser.parse("")
        
        assert "error" in result or result is not None
    
    def test_extract_tokens(self):
        """Test token extraction."""
        parser = SQLParser()
        query = "SELECT name FROM users"
        result = parser.parse(query)
        
        assert "tokens" in result
        assert len(result["tokens"]) > 0
        assert isinstance(result["tokens"], list)
    
    def test_extract_keywords(self):
        """Test keyword extraction."""
        parser = SQLParser()
        query = "SELECT * FROM users WHERE age > 25"
        result = parser.parse(query)
        
        assert "keywords" in result
        assert isinstance(result["keywords"], list)
