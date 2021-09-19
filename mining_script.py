from hashlib import sha256

max_nonce = 2000000 


def to_hash(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(height, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for nonce in range(max_nonce): 
        text = str(height) + transactions + previous_hash + str(nonce)
        new_hash = to_hash(text)
        if new_hash.startswith(prefix_str):
            print(f"Attempt number: {nonce}") 
            return new_hash

    raise BaseException


# Testing
if __name__ == "__main__":
    print(mine(1,
               "Some test transaction",
               "4e1c44e5ca9dafd36dd53a31347f220c51b16384cfaed8de78ad2e709b590dff",
               5))
