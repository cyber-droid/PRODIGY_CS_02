import cv2
import numpy as np
import secrets

def encrypt_image(input_path, output_path, key):
    image = cv2.imread(input_path)
    if image is None:
        raise ValueError("Image not found or invalid format.")
    
    key = np.frombuffer(key.encode(), dtype=np.uint8)  # Convert key to byte array
    key = np.resize(key, image.shape)  # Resize key to match image shape
    
    encrypted_image = cv2.bitwise_xor(image, key)  # XOR pixel values
    cv2.imwrite(output_path, encrypted_image)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    encrypt_image(input_path, output_path, key)  # XOR operation is reversible
    print(f"Decrypted image saved as {output_path}")

if __name__ == "__main__":
    key = secrets.token_hex(16)  # Generates a 32-character secure key
    print("Your encryption key:", key)
    
    encrypt_image("input.jpg", "encrypted.png", key)
    decrypt_image("encrypted.png", "decrypted.jpg", key)

