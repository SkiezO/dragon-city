from app.main.src.DataLoader.ChunkProcessors import ChunkProcessor


class LinePrinterProcessor(ChunkProcessor):

    def process_chunk(self, line_iterator: iter):
        for line in line_iterator:
            print(line)
