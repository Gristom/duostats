URL = {
    'base': 'https://{proxy}.api.riotgames.com/lol/{url}',
    'summoner_by_name': 'summoner/v{version}/summoners/by-name/{names}',
    'ranked_stats': 'v{version}/stats/by-summoner/{summonerIds}/ranked',
    'match_history': 'match/v{version}/matchlists/by-account/{summonerIds}?queue=420&beginIndex={beginIndexs}',
    'match_info': 'match/v{version}/matches/{matchIds}'

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
