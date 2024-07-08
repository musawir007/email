import requests
import pyfiglet
pyfiglet.print_figlet("musawir",colors="")
import pyfiglet
from termcolor import colored
import sys
import time
import os
os.system("pip install pyfiglet")

# Generate ASCII art
ascii_art = pyfiglet.figlet_format("musawir")

# Color the ASCII art (green in this case)
colored_ascii_art = colored(ascii_art, 'green')

# Print the colored ASCII art
print(colored_ascii_art)



def slow_print(text, delay=0.1, color='\033[92m'):
    # \033[92m is the ANSI escape code for green text
    reset = '\033[0m'  # ANSI escape code to reset color
    for char in text:
        sys.stdout.write(f"{color}{char}{reset}")
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

# Example usage
slow_print("______________________________________________________", delay=0.05)
print("\033[92m")

slow_print("<<<<<<<<<<<<<<<<<<<< GENERATE EMAIL >>>>>>>>>>>>>>>>>>>", delay=0.05)

print("\033[92m")
slow_print("______________________________________________________", delay=0.05)
print("\033[92m")







url = "https://temp-mail-temporary-email.p.rapidapi.com/domain"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"count\"\r\n\r\n1\r\n-----011000010111000001101001--\r\n\r\n"
headers = {
	"x-rapidapi-key": "d97ad460d8msh47ea613332686f8p10fe95jsn7de0ccd346bb",
	"x-rapidapi-host": "temp-mail-temporary-email.p.rapidapi.com",
	"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
}

response = requests.post(url, data=payload, headers=headers)

slow_print("*******************************************************", delay=0.05)
print("\033[92m")
print(f"email: {response.json()[0]}")
print("\033[92m")
slow_print("*******************************************************", delay=0.05)