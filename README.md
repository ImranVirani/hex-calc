# Hex Calculator

This application was created using aid from AI

A simple command-line hexadecimal calculator that performs basic arithmetic operations.

## Features

- Addition, subtraction, multiplication, and division of hexadecimal numbers
- Input validation and error handling
- Simple and intuitive interface
- Results displayed in both hexadecimal (with 0x prefix) and decimal format
- Support for negative numbers

## Usage

1. Make the script executable:
   ```bash
   chmod +x hex_calc.py
   ```

2. Run the calculator:
   ```bash
   ./hex_calc.py
   ```

3. Enter calculations in the format: `<hex1> <operation> <hex2>`
   - Example: `FF + 1A`
   - Example: `2A * 3`
   - Example: `100 / 2`
   - Example: `-FF + 1A`

4. Available operations:
   - `+` : Addition
   - `-` : Subtraction
   - `*` : Multiplication
   - `/` : Division (integer division)

5. Enter `q` to quit the calculator

## Examples

```
Enter calculation: FF + 1A
Result: 0x119 (hex)
Decimal: 281

Enter calculation: 2A * 3
Result: 0x7E (hex)
Decimal: 126

Enter calculation: -FF + 1A
Result: -0xE5 (hex)
Decimal: -229
```

## Requirements

- Python 3.x
