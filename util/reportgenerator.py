import plotly.graph_objects as go
from os import stat

class Report_Generator:

    def __init__(self, compressed_times, num_of_indexes, input_file, compressed_sizes, num_bits):

        self._compressed_times = compressed_times
        self._num_of_indexes = num_of_indexes
        self._input_file = input_file
        self._compressed_sizes = compressed_sizes
        self._num_bits = num_bits
        
        rc = self.calculate_size()
        print(f'Compression ratio: {rc}\nElapsed times: {self._compressed_times}\nNum of indexes: {self._num_of_indexes}\n' + '_'*50 + '\n')
        self.graph_generator(rc)


    def calculate_size(self):

        input_size = stat(self._input_file).st_size
        
        compressed_ratios = []

        for output_size in self._compressed_sizes:
            compressed_ratios.append((input_size*8)/(output_size*self._num_bits)) 

        return compressed_ratios
        

    def graph_generator(self, compress_ratio):

        compression_ratio_fig = go.Figure(
            data=[go.Scatter(x=[i for i in range(9, 17)],
                            y=compress_ratio)],
            layout=go.Layout(title="Compression ratio by K",
                            xaxis_title="K",
                            yaxis_title="Compression ratio"),
        )
        compression_ratio_fig.write_image("../results/compression_rate_x_k.png")

        time_fig = go.Figure(
            data=[go.Scatter(x=[i for i in range(9, 17)], y=self._compressed_times)],
            layout=go.Layout(title="Processing time by K",
                            xaxis=dict(
                                title="K"
                            ),
                            yaxis_title="Time in s")
        )

        time_fig.write_image("../results/time_x_k.png")

        indices_fig = go.Figure(
            data=[go.Scatter(x=[i for i in range(9, 17)], y=self._num_of_indexes)],
            layout=go.Layout(title="Indexes by K",
                            xaxis=dict(
                                title="K",
                                tickmode='linear'
                            ),
                            yaxis_title="Number of indexes")
        )

        indices_fig.write_image("../results/indices_x_k.png")