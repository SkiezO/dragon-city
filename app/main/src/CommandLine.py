import enum

import fire

from app.main.src.DataLoader import File, ProgressReporter
from app.main.src.DataLoader.ChunkProcessors import MongoProcessor

class ProcessorEnum(enum.Enum):
    """The Mongo Processor"""
    mongo = MongoProcessor


class CommandLine(object):
    def process_report(self, report_location, processor = 'mongo'):
        """
        You can select the processot you want. 
        The default value is Mongo
        
        :param report_location: /tpm/in/game_actions.csv 
        :param processor: [mongo, csv]
        """
        File.read(report_location, ProcessorEnum['mongo'].value(), ProgressReporter())
        return "Report processed successfully"

if __name__ == '__main__':
    fire.Fire(CommandLine())
