import enum

import fire

from app import set_persistence_engine
from app.main.src.DataLoader import File, ProgressReporter
from app.main.src.DataLoader.ChunkProcessors import MongoProcessor, CSVProcessor


class ProcessorEnum(enum.Enum):
    """The Mongo Processor"""
    mongo = {'engine': 'Mongo', 'processor': MongoProcessor}
    csv = {'engine': 'Mongo', 'processor': CSVProcessor}


class CommandLine(object):
    def process_report(self, report_location, processor = 'csv'):
        """
        You can select the processot you want. 
        The default value is Mongo
        
        :param report_location: /tpm/in/game_actions.csv 
        :param processor: [mongo, csv]
        """
        set_persistence_engine(ProcessorEnum[processor].value['engine'])
        File.read(report_location, ProcessorEnum[processor].value['processor'](), ProgressReporter())
        return "Report processed successfully"

if __name__ == '__main__':
    fire.Fire(CommandLine())
