# LZW Compressor 📚

## Compress 
`python main.py -input_file "input/corpus16MB.txt" -bits_number "9" -operation "compress"`
<br>
## Decompress
`python main.py -input_file "output/02.mp4.lzw" -bits_number "9" -operation "decompress"`
<br>
## Obs 🔎
In compression, the `bits_number` parameter is optional, if not used, a range of 9 to 16 will be used for compression. 