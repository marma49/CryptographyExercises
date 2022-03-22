import hashlib

def hashFile(fileName: str) -> str:
    """Function to get a hash of a file

    Args:
        fileName (str): Name of a file

    Returns:
        str: Hash of a file
    """

    text = open(fileName, "rb").read()
    hash = hashlib.sha256()
    hash.update(text)
    return hash.hexdigest()

hash = hashFile("ubuntu-21.10-desktop-amd64.iso")
print(hash)

"""
Hash is the same as there:
http://releases.ubuntu.com/21.10/SHA256SUMS
"""