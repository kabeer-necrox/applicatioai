def is_palindrome(num):
    # Convert the integer to a string for easy comparison
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    if num_str == num_str[::-1]:
        return True
    else:
        return False

def main():
    # Input a five-digit integer
    num = input("Enter a five-digit integer: ")
    
    # Check if the input is a valid five-digit integer
    if len(num) != 5 or not num.isdigit():
        print("Invalid input. Please enter a five-digit integer.")
        return
    
    # Convert the input to an integer
    num = int(num)
    
    # Check if the integer is a palindrome
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")

if __name__ == "__main__":
    main()
