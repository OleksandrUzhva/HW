import os
import threading
import time
from multiprocessing import Process

import requests
from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("exaple.key", "wb") as filekey:
        filekey.write(key)


def load_key():
    with open("exaple.key", "rb") as filekey:
        key = filekey.read()
    return key


def encrypt_file(file_path, key):
    print(f"Encrypting file from {file_path} in process {os.getpid()}")
    with open("rockyou.txt", "rb") as file:
        original = file.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(original)
    with open("rockyou.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    _ = [i for i in range(100_000_000)]


def download_image(image_url):
    print(
        f"Downloading image from {image_url} in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


def encryption_task(path, key):
    start_time = time.perf_counter()
    encrypt_file(path, key)
    end_time = time.perf_counter()
    print(f"Time taken for encryption task: {end_time - start_time} seconds")


def download_task(image_url):
    start_time = time.perf_counter()
    download_image(image_url)
    end_time = time.perf_counter()
    print(f"Time taken for download task: {end_time - start_time} seconds")


if __name__ == "__main__":
    try:
        generate_key()
        key = load_key()
        path = "rockyou.txt"
        image_url = "https://picsum.photos/1000/1000"
    except Exception as e:
        print(f"Error occurred: {e}")

    thread_encryption = threading.Thread(target=encryption_task, args=(path, key))
    thread_download = threading.Thread(target=download_task, args=(image_url,))

    thread_encryption.start()
    thread_download.start()

    thread_encryption.join()
    thread_download.join()

    process_encryption = Process(target=encryption_task, args=(path, key))
    process_download = Process(target=download_task, args=(image_url,))

    process_encryption.start()
    process_download.start()

    process_encryption.join()
    process_download.join()
