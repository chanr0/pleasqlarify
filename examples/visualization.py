"""
Visualization Example

This example demonstrates how to use the visualization features.
"""

from pleasqlarify import QueryVisualizer


def main():
    """Run visualization examples."""
    visualizer = QueryVisualizer()
    
    query = """
    SELECT u.name, COUNT(o.id) as order_count
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    WHERE u.active = true
    GROUP BY u.name
    HAVING COUNT(o.id) > 0
    ORDER BY order_count DESC
    """
    
    # Text visualization
    print("Text Visualization:")
    print(visualizer.visualize(query, output_format="text"))
    
    print("\n" + "=" * 60 + "\n")
    
    # HTML visualization
    print("HTML Visualization:")
    print(visualizer.visualize(query, output_format="html"))
    
    print("\n" + "=" * 60 + "\n")
    
    # JSON visualization
    print("JSON Visualization:")
    print(visualizer.visualize(query, output_format="json"))


if __name__ == "__main__":
    main()
