from pathlib import Path
from struct import pack
from tqdm import tqdm
import fire
import re


class LzwCompress():

    def __init__(self, file_dir=str, bits_number=int):

        self._file_dir = file_dir
        self._table_edge = pow(2, bits_number)
        self.bytes_dictionary_size = 256
        self._dictionary = {chr(i): i for i in range(
            self.bytes_dictionary_size)}

    def open_file(self):

        bytes_data = []
        with open(self._file_dir, mode='rb') as f:

            while (byte := f.read(1)):
                bytes_data.append(byte)
                # print(byte)
                # print(type(bytes_data[0]))
            # data = f.read()

        # with open("myfile", "rb") as f:

        # for byte in bytes_data:
        #     a = b''+byte

        # print(bytes_data)
        # exit()
        return bytes_data

    def write_compress_file(self, compressed_data=list):

        Path("output").mkdir(parents=True, exist_ok=True)
        output_dir = re.search(r'[^/]+(?=\.)', self._file_dir).group(0)+".lzw"
        print(output_dir)

        with open(f'./output/{output_dir}', 'wb') as output:

            for data in compressed_data:
                output.write(pack('>H', int(data)))

    def start_compress(self):

        data = self.open_file()

        string = b""
        compressed_data = []

        for character in tqdm(data):

            symbol = string + character

            print(symbol)
            # exit()

            if symbol in self._dictionary:
                string = symbol

            else:

                if string:
                    # pass
                    compressed_data.append(self._dictionary[string])

                if(len(self._dictionary) <= self._table_edge):

                    self._dictionary[symbol] = self.bytes_dictionary_size
                    self.bytes_dictionary_size += 1

                string = character

        if string in self._dictionary:
            print()
            compressed_data.append(self._dictionary[string])
        exit
        self.write_compress_file(compressed_data)
