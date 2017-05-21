import multiprocessing
import threading

from app.main.src.DataLoader import ProgressReporter
from app.main.src.DataLoader.ChunkProcessors import ChunkProcessor


class File:
    @staticmethod
    def worker(cp, jr):
        cp.process_chunk(jr['lines'])
        return jr

    @staticmethod
    def read(file: str, chunk_processor: ChunkProcessor, progress_reporter: ProgressReporter):
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        jobs = []
        for chunkStart, chunkSize in ChunkProcessor.chunkify(file):
            chunk_result = ChunkProcessor.read_lines_in_chunk(file, chunkStart, chunkSize)
            jobs.append(pool.apply_async(File.worker, (chunk_processor, chunk_result)))
            progress_reporter.increase_file_size(chunkSize)

        progress_reporter.reset_clock()
        for job in jobs:
            job_result = job.get()
            progress_reporter.process_chunk(job_result['chunk_size'], job_result['lines'])

        pool.close()
