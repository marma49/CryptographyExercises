import hashlib
import timeit


text = input("Enter text: ")
text = text.encode()


def hashSomething(text: str, hashMethod: str):
    """Function to hash text with different methods

    Args:
        text (str): Text to hash
        hashMethod (str): Function which is used to hash the text
    """
    start = timeit.default_timer()
    
    match hashMethod:
        case "sha1":
            hash = hashlib.sha1()
        case "sha3_224":
            hash = hashlib.sha3_224()
        case "shake_256":
            hash = hashlib.shake_256()
        case "sha256":
            hash = hashlib.sha256()
        case "blake2b":
            hash = hashlib.blake2b()
        case "shake_128":
            hash = hashlib.shake_128()
        case "sha512":
            hash = hashlib.sha512()
        case "sha3_256":
            hash = hashlib.sha3_256()
        case "sha3_384":
            hash = hashlib.sha3_384()
        case "md5":
            hash = hashlib.md5()
        case "sha384":
            hash = hashlib.sha384()
        case "blake2s":
            hash = hashlib.blake2s() 
        case "sha224":
            hash = hashlib.sha224()
        case "sha3_512":
            hash = hashlib.sha3_512()
        case _:
            print("No such method available")
            exit()

    hash.update(text)
    stop = timeit.default_timer()
    timeInMiliseconds = str((stop - start) * 1000)[:7]
    print(f"Hashing with {hashMethod} method took: {timeInMiliseconds} miliseconds")

    if (hashMethod in ["shake_128", "shake_256"]):
        print(f"Hash: {hash.hexdigest(10)}\n")
    else:
        print(f"Hash: {hash.hexdigest()}\n")

hashSomething(text, "sha1")
hashSomething(text, "sha3_224")
hashSomething(text, "shake_256")
hashSomething(text, "sha256")
hashSomething(text, "blake2b")
hashSomething(text, "shake_128")
hashSomething(text, "sha512")
hashSomething(text, "sha3_256")
hashSomething(text, "sha3_384")
hashSomething(text, "md5")
hashSomething(text, "sha384")
hashSomething(text, "blake2s")
hashSomething(text, "sha224")
hashSomething(text, "sha3_512")

