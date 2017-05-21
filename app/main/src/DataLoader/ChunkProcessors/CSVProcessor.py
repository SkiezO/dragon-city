import os
from pathlib import Path

from app import APP_ROOT_PATH, OS_SEPARATOR
from app.main.src.DataLoader.Adapters import ReportLineToModelsAdapter
from app.main.src.DataLoader.ChunkProcessors import ChunkProcessor


class CSVProcessor(ChunkProcessor):
    OUTPUT_FODLER = Path(APP_ROOT_PATH + OS_SEPARATOR + 'target' + OS_SEPARATOR + '__temp')

    def __init__(self):
        if not self.OUTPUT_FODLER.exists():
            self.OUTPUT_FODLER.mkdir(777, True)

    def process_line(self, line):
        adapter_result = ReportLineToModelsAdapter(line.split(','))

        if adapter_result.game_action.name not in ['purchase', 'speed_up', 'upgrade']:
            return

        user_temp_file = Path(str(self.OUTPUT_FODLER.absolute()) + OS_SEPARATOR + adapter_result.user.id)
        if not user_temp_file.is_file():
            user_temp_file.touch()
        # TODO: add safe thread file writing
        user_temp_file_open = user_temp_file.open('r')
        line = user_temp_file_open.readline().split(',')
        user_id = adapter_result.user.id
        spent = int(line[1] if len(line) == 2 else 0) + adapter_result.offer.amount
        user_temp_file_open.close()
        user_temp_file_open = user_temp_file.open('w')
        user_temp_file_open.write("{0},{1}\n".format(user_id, spent))
        user_temp_file_open.close()
        return

    def process_chunk(self, line_list):
        for line in line_list:
            self.process_line(line)

    def close(self):
        filenames = self.OUTPUT_FODLER.iterdir()
        with open(str(self.OUTPUT_FODLER) + OS_SEPARATOR + '..' + OS_SEPARATOR + 'users.csv', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
                os.remove(fname)
        self.OUTPUT_FODLER.rmdir()
