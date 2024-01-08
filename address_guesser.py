import os, random, requests

print("\nThis script uses random number generation to test URLs matching an otherwise known pattern, saves any valid URLs to a file in the same directory as the script file, then stops after it has successfully figured out a desired number of valid URLs.")
print("\nYou may quit at any time with Control + C.")

not_int = "\nInvalid input; only integers (e.g. \"1\" or \"2\", not \"one\", \"1.4\", etc.) are accepted."

while True:
    enough = input(f"\nHow many valid URLs do you want to generate?: ")
    try:
        enough = int(enough)
        break
    except ValueError:
        print(not_int)

plurality = "s"
is_or_are = "are"
if enough == 1:
    plurality = ""
    is_or_are = "is"

print(f"\nGot it. Execution will stop once {enough} valid URL{plurality} {is_or_are} determined.")

print("\nPlease specify the range of random numbers that you wish to generate.")
while True:
    lo = input(f"\nPlease specify the lowest number in range: ")
    try:
        lo = int(lo)
        break
    except ValueError:
        print(not_int)
while True:
    hi = input(f"\nPlease specify the highest number in range: ")
    try:
        hi = int(hi)
        if hi > lo:
            break
        else:
            print("\nYou entered a number that is lower than the one you previously specified as the bottom of your range.")
            print(f"\nPlease enter a number larger than {lo} or press Control + C to quit.")
    except ValueError:
        print(not_int)

print("\nAn URL pattern must be specified. If you haven't done so already, please save this in a one-line plaintext (.txt) file, inserting \"{random}\" (without the quotation marks) in the spot where you want the randomised numbers to be injected.")
while True:
    url_pattern_path = input("\nPlease specify a file from which to load the desired URL pattern (excluding the file extension): ")
    url_pattern_path += ".txt"
    try:
        with open(url_pattern_path, "r") as file:
            url_pattern = file.read().strip()
        break
    except FileNotFoundError:
        print(f"Error: {url_pattern_path} not found. Please check file path and try again.")

tested_urls = []
all_tested_urls = "tested_urls.txt"
if os.path.exists(all_tested_urls):
    with open(all_tested_urls, "r") as file:
        for line in file:
            tested_urls.append(line.strip())
else:
    print(f"No {all_tested_urls} file found, so one will be created.")

filename = "valid_urls.txt"
print(f"\nIf any valid URLs are identified, they will be saved to {filename}. If the file already exists, any existing contents will not be overwritten, new URLs will just be appended to the end of the file instead.")
print("\nIf the URL pattern is incorrect, the operation might find no valid URLs, in which case the script will run until interrupted (e.g. with Control + C).")

input("\nPress Return or Enter to begin.\n")

working_urls = []

while len(working_urls) < enough:
    random_number = random.randint(lo, hi)
    url = url_pattern.format(random=random_number)

    if url in tested_urls:
        continue

    response = requests.get(url)
    tested_urls.append(url)
    with open(all_tested_urls, "w") as file:
        for url in tested_urls:
            file.write(url + "\n")

    if response.status_code == 200:
        working_urls.append(url)
        with open(filename, "a") as file:
            file.write(url + "\n")
        print(f"{url} is valid ({response.status_code})! Saved to {filename}")
    else:
        print(f"{url} is invalid ({response.status_code})")

print(f"\nExecution completed. Valid URL{plurality} identified during this session:")
for url in working_urls:
    print(url)
