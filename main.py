# main.py

import sys
from ai_helper import interpret_query
from db_helper import save_calculation, load_history

def start_calculator():
     
    print("*********************************************")
    print("      Welcome to the Enhanced Calculator!   ")
    print("*********************************************")
    print("       I'm here to help you with:")
    print("              ➕ Addition")
    print("              ➖ Subtraction")
    print("              ✖️  Multiplication")
    print("              ➗ Division")
    print("              🔼 Power")
    print("              🔽 Square Root")
    print("              ❓ History")
    print("              🛑 Exit")      
    print("")

    print("Simply type your query and I'll compute the result for you. 😊")
    print("For example:")
    print("   'Add 5 and 3' ➡ 8")
    print("   'What is the square root of 16?' ➡ 4")
    print("")

    print("Let's get started! Type 'exit' anytime to quit. 👋")
    print("")
    print("*********************************************")





    while True:
        user_input = input("\nType here: ")
        
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        
        # Interpreting the query and getting the result
        result = interpret_query(user_input)
        
        # Show the result to the user
        print(f"Result: {result}")
        
        # Optionally save the result in the database
        save_calculation(user_input, result)
        
        # If the user asks for history
        if "history" in user_input.lower():
            history = load_history()
            print("Calculation History:")
            for entry in history:
                print(f"{entry[0]} = {entry[1]}")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                break
            
            result = interpret_query(user_input)  # Assuming interpret_query returns the result
            print(f"Result: {result}")
            
            # Save the calculation to the database
            save_calculation(user_input, result)

            # Optionally, load and display the calculation history
            history = load_history()
            print("\nCalculation History:")
            for entry in history:
                print(entry)
        
        except Exception as e:
            print(f"An error occurred: {e}")
           


if __name__ == "__main__":
    start_calculator()
