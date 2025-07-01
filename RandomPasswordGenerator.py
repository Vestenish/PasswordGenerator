import random, string

while True:
    input_message = input("Which type of password would you like to set? Options: Letter, Letter_Number, All --> ").strip().capitalize()
    if input_message in ["Letter", "Letter_number", "All"]:
        break
    else:
        print("Please select one of the options.")

password_length = int(input("Enter the desired password length --> "))

Letter = string.ascii_uppercase + string.ascii_lowercase
Letter_Number = string.digits + string.ascii_letters
All = string.ascii_letters + string.digits + string.punctuation

if input_message == "Letter":
    Character_Pool = Letter
elif input_message == "Letter_number":
    Character_Pool = Letter_Number
else:
    Character_Pool = All

new_password = ''.join(random.choices(Character_Pool, k=password_length))
print("Your new password -->", new_password)