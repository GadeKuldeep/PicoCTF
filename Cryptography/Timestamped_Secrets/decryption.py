from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import sha256

cipher_hex = "dcc2a6a4cf3dbc69a929aa7c4e3c33e7558eef1f2244bde76e450b065188db38"

def decrypt(ciphertext_hex, timestamp):
    key = sha256(str(timestamp).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted = cipher.decrypt(ciphertext)
    
    try:
        plaintext = unpad(decrypted, AES.block_size)
        return plaintext.decode()
    except:
        return None

base_time = 1770242624

for t in range(base_time - 2000, base_time + 2000):
    result = decrypt(cipher_hex, t)
    if result:
        print(f"[+] Found! Timestamp: {t}")
        print(f"[+] Plaintext: {result}")
        break

# flag found is =>picoCTF{sa3S_sEc9t_5e67da97}
