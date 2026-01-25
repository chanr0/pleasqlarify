"""
Basic SQL Query Clarification Example

This example demonstrates basic usage of the PleasQLarify system.
"""

from pleasqlarify import SQLClarifier


def main():
    """Run basic clarification examples."""
    # Initialize the clarifier
    clarifier = SQLClarifier()
    
    # Example 1: Simple SELECT query
    print("=" * 60)
    print("Example 1: Simple SELECT Query")
    print("=" * 60)
    
    query1 = "SELECT * FROM users WHERE age > 25"
    result1 = clarifier.clarify(query1)
    
    print(f"\nOriginal Query:\n{result1['query']}")
    print(f"\nFormatted Query:\n{result1['formatted']}")
    print(f"\nExplanation: {result1['explanation']}")
    
    # Example 2: Query with JOIN
    print("\n" + "=" * 60)
    print("Example 2: Query with JOIN")
    print("=" * 60)
    
    query2 = """
    SELECT u.name, o.order_date, o.total
    FROM users u
    JOIN orders o ON u.id = o.user_id
    WHERE o.total > 100
    """
    result2 = clarifier.clarify(query2)
    
    print(f"\nOriginal Query:\n{result2['query']}")
    print(f"\nFormatted Query:\n{result2['formatted']}")
    print(f"\nExplanation: {result2['explanation']}")
    
    # Example 3: Aggregation query
    print("\n" + "=" * 60)
    print("Example 3: Aggregation Query")
    print("=" * 60)
    
    query3 = """
    SELECT department, COUNT(*) as employee_count, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department
    HAVING COUNT(*) > 5
    ORDER BY avg_salary DESC
    """
    result3 = clarifier.clarify(query3)
    
    print(f"\nOriginal Query:\n{result3['query']}")
    print(f"\nFormatted Query:\n{result3['formatted']}")
    print(f"\nExplanation: {result3['explanation']}")


if __name__ == "__main__":
    main()
