#!/usr/bin/env python3

def hex_to_decimal(hex_str):
    """Convert a hexadecimal string to decimal."""
    try:
        # Handle negative numbers
        if hex_str.startswith('-'):
            return -int(hex_str[1:], 16)
        return int(hex_str, 16)
    except ValueError:
        raise ValueError(f"Invalid hexadecimal number: {hex_str}")

def decimal_to_hex(decimal):
    """Convert a decimal number to hexadecimal string."""
    if decimal < 0:
        return '-0x' + hex(abs(decimal))[2:].upper()
    return '0x' + hex(decimal)[2:].upper()

def calculate(operation, num1, num2):
    """Perform the specified operation on two hexadecimal numbers."""
    # Convert hex strings to decimal
    n1 = hex_to_decimal(num1)
    n2 = hex_to_decimal(num2)
    
    # Perform the operation
    if operation == '+':
        result = n1 + n2
    elif operation == '-':
        result = n1 - n2
    elif operation == '*':
        result = n1 * n2
    elif operation == '/':
        if n2 == 0:
            raise ValueError("Division by zero")
        result = n1 // n2  # Integer division
    else:
        raise ValueError(f"Invalid operation: {operation}")
    
    return decimal_to_hex(result)

def main():
    print("Hex Calculator")
    print("Enter 'q' to quit")
    print("Operations: +, -, *, /")
    print("Example: FF + 1A")
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter calculation: ").strip()
            
            # Check for quit command
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
            
            # Parse input
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input format. Use: <hex1> <operation> <hex2>")
                continue
            
            num1, operation, num2 = parts
            
            # Perform calculation
            result = calculate(operation, num1, num2)
            
            # Display result
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main() 
