from struct import unpack, calcsize
import fire
import re
from pathlib import Path
from tqdm import tqdm

class LzwDecompress():

    def __init__(self, file_dir=str, bits_number=int):
        
        self._file_dir = file_dir
        self._table_edge = pow(2,bits_number)
        self._dictionary_size = 256                  
        self._dictionary = {i: chr(i) for i in range(self._dictionary_size)}
        self._compressed_data = []


    def open_file(self):

        with open(self._file_dir, 'rb') as f:

            while True:
                byte = f.read(4)
                if len(byte) != 4:
                    break
                (byte,) = unpack('>I', byte)
                self._compressed_data.append(byte)
                print(byte)
        exit()

    def write_decompressed_file(self, decompressed_data=list):

        Path("results").mkdir(parents=True, exist_ok=True)
        result_dir = re.search(r'[^/]+(?=\.)', self._file_dir).group(0)+".txt"
        print(result_dir)

        with open(f'./results/{result_dir}', 'w') as result:
            result.write(decompressed_data)

    def start_decompression(self):

        self.open_file()

        string = ""   

        decompressed_data = ""

        for byte in tqdm(self._compressed_data):  

            if byte in self._dictionary:
                decompressed_data += self._dictionary[byte]

            else:
                self._dictionary[self._dictionary_size] = string + self._dictionary[byte][0]
                self._dictionary_size += 1

            string = self._dictionary[byte]
        
        print(self._dictionary)

        self.write_decompressed_file(decompressed_data)