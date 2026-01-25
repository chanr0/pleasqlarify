"""
Command Line Interface for PleasQLarify
"""

import argparse
import sys
from .clarifier import SQLClarifier
from .visualizer import QueryVisualizer


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="PleasQLarify - SQL Query Clarification Tool"
    )
    
    parser.add_argument(
        "--query",
        type=str,
        help="SQL query to clarify"
    )
    
    parser.add_argument(
        "--file",
        type=str,
        help="Path to file containing SQL query"
    )
    
    parser.add_argument(
        "--format",
        type=str,
        choices=["text", "html", "json"],
        default="text",
        help="Output format"
    )
    
    parser.add_argument(
        "--visualize",
        action="store_true",
        help="Generate visualization"
    )
    
    args = parser.parse_args()
    
    # Get query from command line or file
    if args.query:
        query = args.query
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                query = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)
    
    # Clarify the query
    clarifier = SQLClarifier()
    result = clarifier.clarify(query)
    
    if "error" in result:
        print(f"Error: {result['error']}", file=sys.stderr)
        sys.exit(1)
    
    # Output results
    if args.visualize:
        visualizer = QueryVisualizer()
        print(visualizer.visualize(query, args.format))
    else:
        if args.format == "json":
            import json
            print(json.dumps(result, indent=2))
        else:
            print("Query:", result["query"])
            print("\nFormatted:")
            print(result["formatted"])
            print("\nExplanation:", result["explanation"])


if __name__ == "__main__":
    main()
