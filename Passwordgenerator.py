import random,string
def Passwordgenerator(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = '!@#$%&*()_+[]{}|;:,.<>?'

    all_characters= lowercase + uppercase + digits + special

    password = ''.join(random.choice(all_characters)for _ in range (length))
    return password

def main():
    password_length =12
    password = Passwordgenerator(password_length)
    print("Your generated password is: ", password )
if __name__ == "__main__":
    main()    
