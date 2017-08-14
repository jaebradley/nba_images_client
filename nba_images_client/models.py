from enum import Enum


class Team(Enum):
    ATLANTA_HAWKS = 'Atlanta Hawks'
    BOSTON_CELTICS = 'Boston Celtics'
    BROOKLYN_NETS = 'Brooklyn Nets'
    CHARLOTTE_HORNETS = 'Charlotte Hornets'
    CHICAGO_BULLS = 'Chicago Bulls'
    CLEVELAND_CAVALIERS = 'Cleveland Cavaliers'
    DALLAS_MAVERICKS = 'Dallas Mavericks'
    DENVER_NUGGETS = 'Denver Nuggets'
    DETROIT_PISTONS = 'Detroit Pistons'
    GOLDEN_STATE_WARRIORS = 'Golden State Warriors'
    HOUSTON_ROCKETS = 'Houston Rockets'
    INDIANA_PACERS = 'Indiana Pacers'
    LOS_ANGELES_CLIPPERS = 'Los Angeles Clippers'
    LOS_ANGELES_LAKERS = 'Los Angeles Lakers'
    MEMPHIS_GRIZZLIES = 'Memphis Grizzlies'
    MIAMI_HEAT = 'Miami Heat'
    MILWAUKEE_BUCKS = 'Milwaukee Bucks'
    MINNESOTA_TIMBERWOLVES = 'Minnesota Timberwolves'
    NEW_ORLEANS_PELICANS = 'New Orleans Pelicans'
    NEW_YORK_KNICKS = 'New York Knicks'
    OKLAHOMA_CITY_THUNDER = 'Oklahoma City Thunder'
    ORLANDO_MAGIC = 'Orlando Magic'
    PHILADELPHIA_76ERS = 'Philadelphia 76ers'
    PHOENIX_SUNS = 'Phoenix Suns'
    PORTLAND_TRAIL_BLAZERS = 'Portland Trail Blazers'
    SACRAMENTO_KINGS = 'Sacramento Kings'
    SAN_ANTONIO_SPURS = 'San Antonio Spurs'
    TORONTO_RAPTORS = 'Toronto Raptors'
    UTAH_JAZZ = 'Utah Jazz'
    WASHINGTON_WIZARDS = 'Washington Wizards'

    @staticmethod
    def get_abbreviation(team):
        return team_to_abbreviation_map.get(team)


team_to_abbreviation_map = {
    Team.ATLANTA_HAWKS: 'ATL',
    Team.BOSTON_CELTICS: 'BOS',
    Team.BROOKLYN_NETS: 'BKN',
    Team.CHARLOTTE_HORNETS: 'CHA',
    Team.CHICAGO_BULLS: 'CHI',
    Team.CLEVELAND_CAVALIERS: 'CLE',
    Team.DALLAS_MAVERICKS: 'DAL',
    Team.DENVER_NUGGETS: 'DEN',
    Team.DETROIT_PISTONS: 'DET',
    Team.GOLDEN_STATE_WARRIORS: 'GSW',
    Team.HOUSTON_ROCKETS: 'HOU',
    Team.INDIANA_PACERS: 'IND',
    Team.LOS_ANGELES_CLIPPERS: 'LAC',
    Team.LOS_ANGELES_LAKERS: 'LAL',
    Team.MEMPHIS_GRIZZLIES: 'MEM',
    Team.MIAMI_HEAT: 'MIA',
    Team.MILWAUKEE_BUCKS: 'MIL',
    Team.MINNESOTA_TIMBERWOLVES: 'MIN',
    Team.NEW_ORLEANS_PELICANS: 'NOP',
    Team.NEW_YORK_KNICKS: 'NYK',
    Team.OKLAHOMA_CITY_THUNDER: 'OKC',
    Team.ORLANDO_MAGIC: 'ORL',
    Team.PHILADELPHIA_76ERS: 'PHI',
    Team.PHOENIX_SUNS: 'PHX',
    Team.PORTLAND_TRAIL_BLAZERS: 'POR',
    Team.SACRAMENTO_KINGS: 'SAC',
    Team.SAN_ANTONIO_SPURS: 'SAS',
    Team.TORONTO_RAPTORS: 'TOR',
    Team.UTAH_JAZZ: 'UTA',
    Team.WASHINGTON_WIZARDS: 'WAS',
}


class FileType(Enum):
    PNG = 'PNG'
    JPG = 'JPG'

    @staticmethod
    def get_extension(file_type):
        return file_type_to_extension_map.get(file_type)


file_type_to_extension_map = {
    FileType.PNG: '.png',
    FileType.JPG: '.jpg',
}


class ImageDimensions:
    def __init__(self, height, length):
        self.height = height
        self.length = length
