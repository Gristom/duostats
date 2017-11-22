URL = {
    'base': 'https://{proxy}.api.riotgames.com/lol/{url}',
    'summoner_by_name': 'summoner/v{version}/summoners/by-name/{names}',
    'ranked_stats': 'v{version}/stats/by-summoner/{summonerIds}/ranked',
    'match_history': 'match/v{version}/matchlists/by-account/{summonerIds}?queue={queues}&season={seasons}&beginIndex={beginIndexs}',
    'match_info': 'match/v{version}/matches/{matchIds}',
    'champ_list': 'static-data/v{version}/champions?locale=en_US&dataById=true'

}

API_VERSIONS = {
    'champion': 3,
    'current-game': 3,
    'featured-games': 3,
    'game': 3,
    'league': 3,
    'lol-static-data': 3,
    'lol-status': 3,
    'match': 3,
    'matchlist': 3,
    'stats': 3,
    'summoner': 3,
    'team': 3
}

REGIONS = {
    'EUNE': 'eun1',
    'EUW': 'euw1',
    'NA': 'na1', 
    'KR': 'kr',
    'RUS': 'ru',
    'BR': 'br1',
    'OCE': 'oc1',
    'JP': 'jp1',
    'TR': 'tr1',
    'LAN': 'la1',
    'LAS': 'la2'
    
    
}

QUEUETYPE = {
    'Solo/Duo': '420',
    'Flex': '440',
        
}

SEASON = {
    'Preseason 3': '0',
    'Season 3 (2013)': '1',
    'Preseason 4': '2', 
    'Season 4 (2014)': '3',
    'Preseason 5': '4',
    'Season 5 (2015)': '5',
    'Preseason 6': '6',
    'Season 6 (2016)': '7',
    'Preseason 7)': '8',
    'Season 7 (2017)': '9',
    'Preseason 8': '10',
    'Season 8 (2018)': '11'    
    
}
