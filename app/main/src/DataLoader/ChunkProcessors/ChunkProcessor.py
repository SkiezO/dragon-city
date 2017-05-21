import os
from abc import abstractmethod
from types import GeneratorType


class ChunkProcessor(object):
    @staticmethod
    def read_lines_in_chunk(file: str, chunk_start: int, chunk_size: int) -> iter:
        with open(file) as f:
            f.seek(chunk_start)
            return {
                'chunk_size': chunk_size,
                'lines': f.read(chunk_size).splitlines()
            }

    @staticmethod
    def chunkify(file_name: str, size: int = 1024) -> GeneratorType:
        file_end = os.path.getsize(file_name)
        with open(file_name, 'rb') as f:
            chunk_end = f.tell()
            while True:
                chunk_start = chunk_end
                f.seek(size, 1)
                f.readline()
                chunk_end = f.tell()
                yield chunk_start, chunk_end - chunk_start
                if chunk_end > file_end:
                    break

    @abstractmethod
    def process_chunk(self, line_list): raise NotImplementedError
