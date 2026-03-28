import hashlib

with open("md.txt", "w") as f:
    for i in range(3000, 3036):
        num_str = str(i)
        md5_hash = hashlib.md5(num_str.encode()).hexdigest()
        f.write(f"{md5_hash}\n")

print("MD5 hashes saved to md.txt")
