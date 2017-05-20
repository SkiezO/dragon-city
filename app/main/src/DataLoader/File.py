import multiprocessing

from app.main.src.DataLoader.ChunkProcessors import ChunkProcessor


class File:
    @staticmethod
    def read(file: str, chunk_processor: ChunkProcessor):
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        jobs = []
        for chunkStart, chunkSize in ChunkProcessor.chunkify(file):
            jobs.append(pool.apply_async(ChunkProcessor.read_lines_in_chunk, (file, chunkStart, chunkSize)))

        for job in jobs:
            chunk_processor.process_chunk(job.get())

        pool.close()
