# core/exchange/chunking.py

def chunk_bytes(data: bytes, chunk_size: int = 800):
    """
    Split bytes into fixed-size chunks.
    """
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]