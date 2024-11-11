from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

repeate = True

while repeate:
  encrypt_or_decrypt = input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
  text_message = input("Type your message:").lower()
  shift_nmber = int(input("Type the shift number:"))

  def encrypt(original_text, shift_amount):
    if encrypt_or_decrypt == "decode":
      shift_amount *= -1

    new_text = ""
    for letters in original_text:
      if letters in alphabet:
        letter_index = alphabet.index(letters)
        total_shift = letter_index + shift_amount
        total_shift %= len(alphabet)
        new_text += alphabet[total_shift]
      else:
        new_text += letters
    
    
    print(f"here is your {encrypt_or_decrypt} result : {new_text}")
  encrypt(text_message, shift_nmber)
  repeat_message = input("Type 'yes' if you want to go again. Otherwise, type 'no':").lower()
  if repeat_message == "no":
    repeate = False
    print("Thank You")
    
