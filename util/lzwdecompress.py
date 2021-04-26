from struct import unpack, calcsize
import fire
import re
from pathlib import Path

class LzwDecompress():

    def __init__(self, file_dir=str, bits_number=int, dictionary_size=int):
        
        self._file_dir = file_dir
        self._table_edge = pow(2,bits_number)
        self._dictionary_size = dictionary_size                  
        self._dictionary = {i: chr(i) for i in range(dictionary_size)}
        self._compressed_data = [0]

    def open_file(self):

        with open('1.lzw', 'rb') as f:

            while True:

                data = f.read(2)
                if len(data) != 2:
                    break
                (data, ) = unpack('>H', data)

                self._compressed_data.append(data)

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

        for byte in self._compressed_data:  

            if byte in self._dictionary:
                decompressed_data += self._dictionary[byte]

            else:
                self._dictionary[self._dictionary_size] = string + self._dictionary[byte][0]
                self._dictionary_size += 1

            string = self._dictionary[byte]
        
        print(self._dictionary)

        self.write_decompressed_file(decompressed_data)
