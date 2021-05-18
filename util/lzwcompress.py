from pathlib import Path
from struct import pack
from tqdm import tqdm
import re

encoding = 'latin-1'

class LzwCompress():

    def __init__(self, file_dir=str, bits_number=int):

        self._file_dir = file_dir
        self._table_edge = pow(2, bits_number)
        self.bytes_dictionary_size = 256
        self._dictionary = {i.to_bytes(1, 'big'):i for i in range(
            self.bytes_dictionary_size)}


    def open_file(self):

        data = []
        with open(self._file_dir, 'rb') as f:
            while True:
                rec = f.read(1)
                if len(rec) != 1:
                    break
                data.append(rec)
        return data

    def write_compress_file(self, compressed_data=list):

        Path("output").mkdir(parents=True, exist_ok=True)
        output_dir = re.search(r'[^/]+(?=$)', self._file_dir).group(0)+".lzw"
        print(output_dir)

        with open(f'./output/{output_dir}', 'wb') as output:

            for data in compressed_data:

                 output.write(pack('>I', data))

    def start_compress(self):

        data = self.open_file()

        string = ""
        compressed_data = []

        for character in tqdm(data):

            symbol = string + character.decode(encoding) 

            if symbol.encode(encoding) in self._dictionary:

                string = symbol

            else:

                encoded_chr = string.encode(encoding)
                compressed_data.append(self._dictionary[encoded_chr])

                if(len(self._dictionary) <= self._table_edge):

                    self._dictionary[symbol.encode(encoding)] = self.bytes_dictionary_size
                    self.bytes_dictionary_size += 1

                string = character.decode(encoding)

        if string.encode(encoding) in self._dictionary:

            compressed_data.append(self._dictionary[string.encode(encoding)])

        self.write_compress_file(compressed_data)
