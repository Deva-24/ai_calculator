from database import Session
from calculator import Calculator
from ai_helper import interpret_query

def main():
    session = Session()
    calc = Calculator(session)

    print("Welcome to Groq AI Calculator!")
    while True:
        query = input("Enter a query (or 'exit' to quit): ")
        if query.lower() == "exit":
            break

        # Use Groq AI to interpret the query
        ai_response = interpret_query(query)
        print(f"AI Interpretation: {ai_response}")

        # Parse the AI response to trigger the correct calculator operation
        if "add" in ai_response:
            # Extract operands from the response
            operands = ai_response.split()[1:]
            a, b = map(float, operands)
            print(f"Result: {calc.add(a, b)}")
        elif "subtract" in ai_response:
            operands = ai_response.split()[1:]
            a, b = map(float, operands)
            print(f"Result: {calc.subtract(a, b)}")
        # Repeat for other operations as needed
        else:
            print("Unrecognized query format.")
  
if __name__ == "__main__":
    main()
