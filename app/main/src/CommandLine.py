import fire

from app.main.src.DataLoader import File, ProgressReporter
from app.main.src.DataLoader.ChunkProcessors import DragonCityProcessor


class CommandLine(object):

  def process_report(self, report_location):
      File.read(report_location, DragonCityProcessor(), ProgressReporter())
      return "Report processed successfully"

if __name__ == '__main__':
  fire.Fire(CommandLine())
