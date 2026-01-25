"""
Tests for the Query Visualizer
"""

import pytest
from pleasqlarify import QueryVisualizer


class TestQueryVisualizer:
    """Test cases for QueryVisualizer class."""
    
    def test_init(self):
        """Test visualizer initialization."""
        visualizer = QueryVisualizer()
        assert visualizer is not None
        assert visualizer.style == "default"
    
    def test_init_with_style(self):
        """Test visualizer initialization with custom style."""
        visualizer = QueryVisualizer(style="minimal")
        assert visualizer.style == "minimal"
    
    def test_text_visualization(self):
        """Test text visualization."""
        visualizer = QueryVisualizer()
        query = "SELECT * FROM users"
        result = visualizer.visualize(query, output_format="text")
        
        assert isinstance(result, str)
        assert len(result) > 0
        assert "SELECT" in result
    
    def test_html_visualization(self):
        """Test HTML visualization."""
        visualizer = QueryVisualizer()
        query = "SELECT * FROM users"
        result = visualizer.visualize(query, output_format="html")
        
        assert isinstance(result, str)
        assert "<div" in result or "<pre" in result
        assert "SELECT" in result
    
    def test_json_visualization(self):
        """Test JSON visualization."""
        visualizer = QueryVisualizer()
        query = "SELECT * FROM users"
        result = visualizer.visualize(query, output_format="json")
        
        assert isinstance(result, str)
        # Should be valid JSON
        import json
        data = json.loads(result)
        assert "query" in data
    
    def test_invalid_output_format(self):
        """Test with invalid output format."""
        visualizer = QueryVisualizer()
        query = "SELECT * FROM users"
        
        with pytest.raises(ValueError):
            visualizer.visualize(query, output_format="invalid")
    
    def test_create_flow_diagram(self):
        """Test flow diagram creation."""
        visualizer = QueryVisualizer()
        query = "SELECT * FROM users"
        result = visualizer.create_flow_diagram(query)
        
        assert isinstance(result, dict)
        assert "nodes" in result
        assert "edges" in result
        assert "query" in result
