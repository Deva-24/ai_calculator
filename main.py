from database import Session
from calculator import Calculator
from ai_helper import interpret_query

def main():
    session = Session()
    calc = Calculator(session)

    print("Welcome to AI Calculator!")
    while True:
        query = input("Enter a query (or 'exit' to quit): ")
        if query.lower() == "exit":
            break

        ai_response = interpret_query(query)
        print(f"AI Interpretation: {ai_response}")

        # Parse AI response and call relevant Calculator methods (example for addition)
        if "add" in ai_response:
            a, b = map(float, ai_response.split()[1:3])
            print(f"Result: {calc.add(a, b)}")

if __name__ == "__main__":
    main()
