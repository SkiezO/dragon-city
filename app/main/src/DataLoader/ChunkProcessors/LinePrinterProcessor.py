from app.main.src.DataLoader.ChunkProcessors import ChunkProcessor


class LinePrinterProcessor(ChunkProcessor):

    def process_chunk(self, line_list):
        for line in line_list:
            print(line)