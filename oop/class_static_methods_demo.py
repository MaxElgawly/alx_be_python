class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that adds two numbers.
        Does not require access to class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that multiplies two numbers.
        Accesses the class attribute calculation_type.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
