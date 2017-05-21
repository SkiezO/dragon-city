
# Usage

## Windows

```powershell
.\bin\dc --help
.\bin\dc process-report C:/temp/game_actions.csv
```

## Shell

```sh
./bin/dc --help
./bin/dc process-report /tpm/game_actions.csv
```

## Support Mongo

```sh
docker docker run --name dragon-city-mongo -p 27017:27017 -d mongo
./bin/dc process-report /tpm/game_actions.csv mongo
```