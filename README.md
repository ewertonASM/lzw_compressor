# LZW Compressor 📚

## Sumário:

1. Equipe
2. Metodologia
3. Análise de Resultados
4. Equipe


## 1. Equipe 

[Ewerton Moura](https://github.com/ewertonASM),
[Renan](https://github.com/Renan-Goes)


## 2. Metodologia ⚙️

Para o desenvolvimento do projeto foi necessário instalar algumas bibliotecas não-nativas do python para 
realizar os objetivos.

O dicionário do LZW foi criado utilizando a estrutura de dados de dicionário do próprio python, com variáveis 
em formato de byte e inteiro (para o byte e o índice).

Na leitura e escrita de arquivos foi utilizada a biblioteca "struct", que utiliza as funções "pack" e 
"unpack", "pack" serve para colocar as variáveis (inteiros que representam os índices) em formato de bytes 
(a quantidade de bytes utilizados para o armazenamento é determinada na chamada da função), enquanto "unpack" 
lê exatamente a quantidade de bytes que foi determinada e armazena em uma variável.

Outras bibliotecas utilizadas foram o "matplotlib" (versão 3.3.2), para geração dos gráficos, a "fire" 
(versão 0.4.0), para a linha de execução do código e passagem dos argumentos, o "tqdm" (versão 4.50.2) para 
a visualização do progresso da compressão ou descompressão e por último a "colr" (versão 0.9.1) em conjunto 
com o "tqdm" para colorir a barra de progresso.

Por fim, para verificar os resultados foram gerados gráficos de:
* Tempo de compressão por número "k" de bits
* Número de índices utilizados no dicionário por número "k" de bits
* Razão de compressão por número "k" de bits

Os arquivos utilizados para teste foram os pedidos na escecificação ("02.mp4" e "corpus16MB.txt").

## 3. Análise de resultados 🔎

### 3.1 Arquivo de texto 📝

*Corpus 16 MB*

<p align="center">
  <img width="600px" src="./results/graphs/graph_Compression_time_corpus.png">
  <img width="600px" src="./results/graphs/graph_indexes_corpus.png">
  <img width="600px" src="./results/graphs/graph_RC_corpus.png">
</p>

### 3.2 Arquivo de vídeo 🎞️

*Video MP4 2,01 MB*

<p align="center">
  <img width="600px" src="./results/graphs/graph_Compression_time_video.png">
  <img width="600px" src="./results/graphs/graph_indexes_video.png">
  <img width="600px" src="./results/graphs/graph_RC_video.png">
</p>

# 4. Rodando a aplicação 🏃‍♂️

## 4.1. Requisitos:

Antes de rodar a aplicação, é necessário instalar as depêndencias com os seguintes comandos:
<br>
<br>
`pip install -r requirements.txt`

## 4.2. Compress 
`python main.py -input_file "input/corpus16MB.txt" -bits_number "9" -operation "compress"`
<br>
## 4.3. Decompress
`python main.py -input_file "output/02.mp4.lzw" -bits_number "9" -operation "decompress"`
<br>
## 4.4. Obs 🔎
Na compressão, o parâmetro `bits_number` é opcional, se não for usado, o intervalo entre 9 e 16 será usado. 