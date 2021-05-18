from util import lzwcompress, lzwdecompress
import fire


def process(**kwargs):

    try:
        option = kwargs.get('operation')

    except print(0):
        return

    if option == 'compress':

        file_dir = kwargs.get('input_file')
        bits_number = kwargs.get('bits_number')

        compress = lzwcompress.LzwCompress(file_dir, bits_number)

        print(f'K={bits_number}, Dictionary_size={pow(2,bits_number)}')
        print('COMPRESSING...')

        compress.start_compress()

    elif option == 'decompress':

        file_dir = kwargs.get('input_file')
        bits_number = kwargs.get('bits_number')

        decompress = lzwdecompress.LzwDecompress(file_dir, bits_number)

        print(f'K={bits_number}, Dictionary_size={pow(2,bits_number)}')
        print('DECOMPRESSING...')

        decompress.start_decompression()


if __name__ == '__main__':
    fire.Fire(process)

