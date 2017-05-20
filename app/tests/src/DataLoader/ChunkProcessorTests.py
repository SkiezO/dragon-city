import collections
import unittest

from app import APP_ROOT_PATH, OS_SEPARATOR
from app.main.src.DataLoader import ChunkProcessor


class FileReaderTests(unittest.TestCase):
    test_chunked_file = "{0}{1}app{1}tests{1}resources{1}test_chunked_file.txt".format(APP_ROOT_PATH, OS_SEPARATOR)

    def testChunkfy(self):
        chunked = ChunkProcessor.chunkify(self.test_chunked_file)
        for chunkStart, chunkSize in chunked:
            self.assertEquals(0, chunkStart)
            self.assertEquals(chunkSize, 1048576)
            return
        self.fail("File not correctly chunked")

    def testReadLinesInChunk(self):
        chunked = ChunkProcessor.chunkify(self.test_chunked_file)
        first_line = next(chunked)
        lines_iterator = ChunkProcessor.read_lines_in_chunk(self.test_chunked_file, first_line[0], first_line[1])
        self.assertTrue(isinstance(lines_iterator, collections.Iterable))
        lines_list = []
        for line in lines_iterator:
            lines_list.append(line)
        self.assertListEqual(lines_list, [
            '21400,plankton,speed_up,50',
            '5000,plankton,purchase,15',
            '56300,plankton,speed_up,31',
            '65100,plankton,upgrade,50',
            '58700,plankton,purchase,48',
            '85300,plankton,purchase,25',
            '17000,plankton,upgrade,9',
            '64900,plankton,purchase,1',
            '36400,plankton,purchase,26',
            '99300,plankton,speed_up,36',
            '26100,plankton,purchase,7'
        ])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
