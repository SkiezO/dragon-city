import sys
import unittest

from app import APP_ROOT_PATH, OS_SEPARATOR
from app.main.src.DataLoader.ChunkProcessors import LinePrinterProcessor, DragonCityProcessor
from app.main.src.DataLoader.File import File


class FileTests(unittest.TestCase):
    file_reader = File()
    test_chunked_file = "{0}{1}app{1}tests{1}resources{1}test_chunked_file.txt".format(APP_ROOT_PATH, OS_SEPARATOR)

    def test_read_line_printer_processor(self):
        line_printer = LinePrinterProcessor()
        self.file_reader.read(self.test_chunked_file, line_printer)
        output = sys.stdout.getvalue().strip().split("\n")
        self.assertListEqual(output, [
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

    def test_read_dragon_city_processor(self):
        processor = DragonCityProcessor()
        self.file_reader.read(self.test_chunked_file, processor)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
