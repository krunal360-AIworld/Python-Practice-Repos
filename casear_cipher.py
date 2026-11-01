alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encryption(text,shift):


def decryption(text,shift):

w = input("Type 'encrypt' for Encription and 'decrypt' for Decryption :" )
text = input("Type Your Text :")
shift=input("Enter shift key :")

if w == "encrypt":
    encryption(text,shift)
elif w == "decrypt":
    decryption(text,shift)