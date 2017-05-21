import multiprocessing
import threading

from app.main.src.DataLoader import ProgressReporter
from app.main.src.DataLoader.ChunkProcessors import ChunkProcessor


class File:
    @staticmethod
    def innerLambda(cp, jr):
        cp.process_chunk(jr['lines'])
        return jr


    @staticmethod
    def read(file: str, chunk_processor: ChunkProcessor, progress_reporter: ProgressReporter):
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        jobs = []
        for chunkStart, chunkSize in ChunkProcessor.chunkify(file):
            jobs.append(pool.apply_async(ChunkProcessor.read_lines_in_chunk, (file, chunkStart, chunkSize)))
            progress_reporter.increase_file_size(chunkSize)

        progress_reporter.reset_clock()
        jobs2 = []
        for job in jobs:
            job_result = job.get()
            #chunk_processor.process_chunk(job_result['lines'])
            #progress_reporter.process_chunk(job_result['chunk_size'], job_result['lines'])
            jobs2.append(pool.apply_async(File.innerLambda, (chunk_processor, job_result)))
            jobs2.append(pool.apply_async(File.innerLambda, (chunk_processor, progress_reporter, job_result)))


        for job in jobs2:
            job_result = job.get()
            progress_reporter.process_chunk(job_result['chunk_size'], job_result['lines'])

        pool.close()
