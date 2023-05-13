import csv

# Read phone numbers from text file
with open("phone_numbers.txt", "r") as f:
    phone_numbers = f.read().splitlines()
print(phone_numbers)

# Write phone numbers to CSV file
with open("phone_numbers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for phone_number in phone_numbers:
        writer.writerow([phone_number])






