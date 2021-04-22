from pathlib import Path
from struct import pack
from tqdm import tqdm
import fire
import re


class LzwCompress():

    def __init__(self, file_dir=str, bits_number=int):

        self._file_dir = file_dir
        self._table_edge = pow(2, bits_number)
        self.aux_dictionary_size = 256
        self._dictionary = {chr(i): i for i in range(self.aux_dictionary_size)}

    def open_file(self):

        with open(self._file_dir, encoding='latin-1') as f:
            data = f.read()

        return data

    def write_compress_file(self, compressed_data=list):

        Path("output").mkdir(parents=True, exist_ok=True)
        output_dir = re.search(r'[^/]+(?=\.)', self._file_dir).group(0)+".lzw"
        print(output_dir)

        with open(f'./output/{output_dir}', 'wb') as output:

            for data in compressed_data:
                output.write(pack('>H', int(data)))

    def start_compress(self):

        data = self.open_file()

        string = ""
        compressed_data = []

        for character in tqdm(data):

            symbol = string + character

            if symbol in self._dictionary:
                string = symbol

            else:

                compressed_data.append(self._dictionary[string])

                if(len(self._dictionary) <= self._table_edge):

                    self._dictionary[symbol] = self.aux_dictionary_size
                    self.aux_dictionary_size += 1

                string = character

        if string in self._dictionary:

            compressed_data.append(self._dictionary[string])

        self.write_compress_file(compressed_data)
