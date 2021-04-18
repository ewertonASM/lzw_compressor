from util import lzwcompress
import fire


def process(**kwargs):
    
    try:
        option = kwargs.get('operation')

    except print(0):
        return

    if option == 'compress':

        file_dir = kwargs.get('input_file')
        bits_number = kwargs.get('bits_number')
        dictionary_size = kwargs.get('dictionary_size')

        compress = lzwcompress.LzwCompress(file_dir, bits_number, dictionary_size)
        compress.start_compress()

    elif option == 'descompress':
        pass
    


if __name__ == '__main__':
    fire.Fire(process)