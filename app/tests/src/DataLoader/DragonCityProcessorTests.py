import unittest

from app.main.src.DataLoader.ChunkProcessors import DragonCityProcessor


class DragonCityProcessorTests(unittest.TestCase):
    dragon_city_processor = DragonCityProcessor()

    def test_process_line(self):
        process_line_result = self.dragon_city_processor.process_line("21400,plankton,speed_up,50")


