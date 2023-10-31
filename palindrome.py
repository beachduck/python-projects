# Online Python compiler (interpreter) to run Python online.
from mpmath import mp
import time

def get_pi_digits(n):
    mp.dps = n + 2  # Set decimal places to desired number of digits + 2
    pi_str = str(mp.pi)
    pi_digits = pi_str[2:n + 2]  # Exclude the "3." and get the first n digits
    return pi_digits

def find_palindromes(s):
    n = len(s)
    palindromes = []
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1]:
                palindromes.append(sub_str)
                
    return palindromes

def find_longest_palindrome(palindromes):
    longest_palindrome = max(palindromes, key=len, default=None)
    return longest_palindrome

def save_cache(n, palindromes):
    with open("pi_cache.txt", "a") as file:
        file.write(f"{n}:{'|'.join(palindromes)}\n")

def load_cache(n):
    cache = {}
    try:
        with open("pi_cache.txt", "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                parts = line.split(":")
                if len(parts) == 2:
                    cache[int(parts[0])] = parts[1]
    except FileNotFoundError:
        pass
    return cache

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of digits to search in Pi: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue

            cache = load_cache(n)
            if n in cache:
                print("Using cached result.")
                cached_result = cache[n].split('|')
                palindromes = cached_result
                duration = 0  # Initialize duration when using cached result
            else:
                start_time = time.time()
                pi_digits = get_pi_digits(n)
                palindromes = find_palindromes(pi_digits)
                save_cache(n, palindromes)
                end_time = time.time()
                duration = end_time - start_time

            if palindromes:
                total_palindromes = len(palindromes)
                longest_palindrome = find_longest_palindrome(palindromes)
                print(f"Total palindromes found in Pi up to {n} digits: {total_palindromes}")
                print(f"Longest palindrome: {longest_palindrome}")
                print(f"It contains {len(longest_palindrome)} digits.")
                print(f"Computation took {duration:.6f} seconds.")
            else:
                print(f"No palindromes found in the first {n} digits of Pi.")
                print(f"Computation took {duration:.6f} seconds.")

            search_again = input("Do you want to search for palindromes in Pi again? (yes/no): ")
            if search_again.lower() != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")





