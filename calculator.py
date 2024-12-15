class Calculator:
    def __init__(self, session):
        self.session = session

    def add(self, a, b):
        result = a + b
        self._save_operation('add', result)
        return result

    # Implement other operations: subtract, multiply, divide, power, root
    # Example for subtraction:
    def subtract(self, a, b):
        result = a - b
        self._save_operation('subtract', result)
        return result

    def _save_operation(self, operation, result):
        new_operation = Operation(operation=operation, result=result)
        self.session.add(new_operation)
        self.session.commit()
