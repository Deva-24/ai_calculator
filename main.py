from calculator import Calculator
from ai_helper import interpret_query

def main():
    calc = Calculator()

    print("Welcome to the Groq Function Chat!")
    print("You can ask the system to perform addition, subtraction, multiplication, or division.\n")

    while True:
        query = input("You: ")

        if query.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break

        # Use Groq AI to interpret the query
        ai_response = interpret_query(query)
        print(f"AI Interpretation: {ai_response}")

        # Assuming the response is something like 'add 5 and 10' or 'divide 20 by 4'
        parts = ai_response.split()
        if len(parts) >= 3:
            operation = parts[0].lower()
            try:
                a = float(parts[1])
                b = float(parts[3])

                if operation == 'add':
                    result = calc.add(a, b)
                elif operation == 'subtract':
                    result = calc.subtract(a, b)
                elif operation == 'multiply':
                    result = calc.multiply(a, b)
                elif operation == 'divide':
                    result = calc.divide(a, b)
                else:
                    result = "Unrecognized operation"
            except Exception as e:
                result = f"Error: {e}"
        else:
            result = "Could not understand the query. Please try again."

        print(f"Result: {result}\n")
        
if __name__ == "__main__":
    main()
