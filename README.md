How to use it.

```markdown
# Ai enhanced Chat Calculator

Welcome to the **Groq Function Chat Calculator**! This project is a Python-based calculator bot that uses natural language processing (NLP) to interact with users. The bot allows users to perform basic arithmetic operations like addition, subtraction, multiplication, and division. Additionally, it stores the history of calculations in a PostgreSQL database using **SQLAlchemy** and supports features like undo, redo, and history clearing.

The calculator bot uses **spaCy** for natural language processing to interpret user queries, and it stores the history of operations in a PostgreSQL database. You can ask the bot to perform calculations using conversational commands like "Add 5 and 10" or "Divide 20 by 4". It then returns the result and saves the operation to the history.

## Features

- **Basic Operations**: 
  - Addition (`add`)
  - Subtraction (`subtract`)
  - Multiplication (`multiply`)
  - Division (`divide`)

- **Advanced Operations**: 
  - Power
  - Root

- **History Tracking**:
  - View past calculations
  - Clear history
  - Undo the last operation
  - Redo the last undone operation

- **Database**:
  - Operations are stored in a PostgreSQL database using **SQLAlchemy**.
  - History can be managed through the database (view, clear, undo, redo).

- **Configuration**:
  - The bot uses environment variables for customizable precision, history size, and maximum input values.

## File Structure

```
/ai_calculator
│
├── /calculator
│   ├── __init__.py               # Initializes the calculator package
│   ├── calculator.py             # Contains the Calculator class and related methods
│   ├── ai_helper.py              # Contains NLP processing using spaCy
│   └── database.py               # Contains database-related functionality using SQLAlchemy
│
├── /tests
│   ├── test_calculator.py        # Unit tests for calculator operations
│   ├── test_history.py           # Unit tests for history functionality
│   └── test_db.py                # Unit tests for database interactions
│
├── /migrations                   # Database migrations (if using Alembic)
│
├── .gitignore                    # Git ignore file
├── config.py                     # Configuration file for environment variables
├── requirements.txt              # Python dependencies for the project
├── README.md                     # Project documentation (this file)
└── main.py                        # Main entry point for the calculator bot
```

## Installation

To get started with this project, follow the steps below:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/ai_calculator.git
cd ai_calculator
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment for managing dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the necessary Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database

Make sure you have **PostgreSQL** installed and running on your machine. Create a new database for the project:

```bash
# In PostgreSQL
CREATE DATABASE testdb;
```

Update the database connection details in `config.py`:

```python
# config.py

DATABASE_URL = 'postgresql://username:password@localhost:5432/testdb'
```

### 5. Set Environment Variables

Configure any environment variables for the project. For example, you can set the precision and history size using a `.env` file or export variables in your shell:

```bash
export CALCULATOR_PRECISION=2
export HISTORY_SIZE=50
export MAX_INPUT_VALUE=1000
```

### 6. Run Migrations (if applicable)

If using **Alembic** for database migrations, you can run the migrations to set up the schema:

```bash
alembic upgrade head
```

### 7. Run the Application

To start the calculator bot, simply run the following command:

```bash
python3 main.py
```

This will start the bot, and you can begin interacting with it in the terminal.

## Usage

Once the program is running, you can interact with the bot by typing your queries. Here are some examples:

```
Welcome to the Groq Function Chat!
You can ask the system to perform addition, subtraction, multiplication, or division.

You: Add 5 and 10
Result: 15

You: Divide 20 by 4
Result: 5.0

You: Quit
Goodbye!
```

The bot will process your request, perform the operation, and display the result. It will also save your operation to the history in the database.

### Available Commands

- **Basic Operations**:
  - `add <x> and <y>`
  - `subtract <x> from <y>`
  - `multiply <x> and <y>`
  - `divide <x> by <y>`
  
- **Advanced Operations**:
  - `power <x> to the <y>`
  - `root <x> of <y>`
  
- **History Commands**:
  - `history` – Shows all past calculations.
  - `clear` – Clears the calculation history.
  - `undo` – Undo the last operation.
  - `redo` – Redo the last undone operation.
  
- **Exit**:
  - `quit` – Exits the calculator program.

## Tests

This project uses **pytest** for unit testing. To run the tests, use the following command:

```bash
pytest
```

This will run all the test cases for the calculator, including tests for basic operations, history functionality, and database interactions.

### Test Coverage

- **test_calculator.py**: Tests the basic calculator operations (addition, subtraction, multiplication, division).
- **test_history.py**: Tests history-related functions such as saving, clearing, undoing, and redoing operations.
- **test_db.py**: Tests the database interactions, ensuring records are stored and retrieved correctly.

## Contributing

Feel free to fork this repository and contribute! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and add tests if necessary.
4. Commit your changes and push to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

**Note**: Remember to replace any placeholder values like `username`, `password`, etc., with your actual credentials or environment variables.

## Conclusion

This project is a powerful yet simple calculator bot that integrates **spaCy** for natural language processing and **PostgreSQL** for persistent storage of history. You can perform arithmetic operations, view your history, undo and redo calculations, and store the history in the database for future reference.
