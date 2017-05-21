import threading
import time


class ProgressReporter:
    PRINT_SIZE = 1000

    def __init__(self):
        self.start_time = time.time()
        self.file_size = 0
        self.progress_chunk = 0
        self.progress_lines = 0
        self.print_count = 0

    def reset_clock(self):
        print("Set up spent {0} seconds. Starting processing lines.".format( round(time.time() - self.start_time, 4)))
        self.start_time = time.time()

    def increase_file_size(self, chunk_size):
        self.file_size += chunk_size

    def process_chunk(self, progress_size: int, progress_lines: list):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.progress_chunk += progress_size
            self.progress_lines += len(progress_lines)
            lines_per_chunk = self.progress_lines / self.progress_chunk
            remaining = (self.file_size - self.progress_chunk) * lines_per_chunk
            if int(self.progress_lines / ProgressReporter.PRINT_SIZE) == self. print_count:
                self.print_count += 1
                ProgressReporter.print_stats(self.progress_lines, remaining, self.start_time)
        finally:
            lock.release()

    @staticmethod
    def print_stats(progress, remaining, start_time):
        elapsed_time = time.time() - start_time
        average_time = float(elapsed_time) / float(progress)
        remaining_time = average_time * float(remaining)
        print("{0} lines processed in {1:.4f} seconds. Time remaining: {2:.4f} seconds.".format(progress, elapsed_time, remaining_time))
