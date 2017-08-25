from RiotAPI import RiotAPI
from collections import Counter
import heapq
import re
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP




#What this program does

#Return Match IDs
#Check for IDs that match
#Confirm match is ranked solo
#Confirm on same team (teamId), participantId, winner
#Check Win loss ratio in games played together
#Check win loss ratio when playing without your partner
#Check win loss ratio when partner plays without you





#Features/fixes to add

#Compare to win loss ratio for solo games to duo games
#Create measurements for deltas ie "Boosted Animal, great synergy etc"
#Determine how many matches to check? Or rate limiter?
#Add Season qualifyer to URL (SEASON 2017 only)
#Why is there one more game than OP.GG?
#Solve issue if partners play against each other (add match id to solo lists?)
#Graphs for site
#Highest win % Champion Combo (Best synergy) (and KDA)
#Highest win % Champion Solo and KDA
#Highest win % Champion Duo and KDA
#Most played champs with KDA both solo and duo
#Summoner name and icon at top of stats window
#Premade stats for popular duos
#Remove redundant calc of stats (not solo no duo)
#Rate limiter
#Create way to periodically update active users



global winchamps1
global winchamps2
global winchampscommon
global winchampscount

global playedchampscommon
global playedchampscount

global p1champscount
global p2champscount

global p1winchampscount
global p2winchampscount

global p1champs
global p2champs

global p1winchamps
global p2winchamps

global losechamps1
global losechamps2
global losechampscommon


global wincount
global gamecount

global wincountcommon
global gamecountcommon

global wincountp1solo
global wincountp2solo

global gamecountp1solo
global gamecountp2solo

global winchampsdict
global winratecommon

global matchlistsolo1
global matchlistsolo2

global p1solochamps
global p2solochamps
global p1solowinchamps
global p2solowinchamps

global p1solowinrate
global p2solowinrate

global p1soloplayedchamps
global p2soloplayedchamps

global p1soloplayechampscount
global p2soloplayedchampscount

global p1solowinchampscount
global p2solowinchampscount

global p1solowinrate
global p2solowinrate

global winpercentcommon
global winpercentp1solo
global winpercentp2solo


winpercentcommon = 0
winpercentp1solo = 0
winpercentp2solo = 0
    
gamecount = 0
wincount = 0

wincountcommon = 0
gamecountcommon = 0

wincountp1solo = 0
wincountp2solo = 0

gamecountp1solo = 0
gamecountp2solo = 0

winchamps1 = []
winchamps2 = []

p1winchamps = []
p2winchamps = []

winchampscommon = []
winchampscount = {}
playedchampscount = {}
p1champscount = {}
p2champscount = {}

p1winchampscount = {}
p2winchampscount = {}

playedchampscommon = []
p1champs = []
p2champs = []

p1solochamps = []
p2solochamps = []

p1solowinchamps = []
p2solowinchamps = []

losechamps1 = []
losechamps2 = []
losechampscommon = []
winchampsdict = {}

winratecommon = {}
p1solowinrate = {}
p2solowinrate = {}

p1solowinrate = {}
p2solowinrate = {}

matchlistsolo1 = []
matchlistsolo2 = []

p1soloplayedchamps = []
p2soloplayedchamps = []

p1soloplayedchampscount = {}
p2soloplayedchampscount = {}

p1solowinchampscount = {}
p2solowinchampscount = {}


def main():

    global playedchampscount
    global winchampscount
    global winratecommon
    global p1champscount
    global p2champscount
    global p1winchamps
    global p2winchamps
    global p1winchampscount
    global p2winchampscount
    global matchlistsolo1
    global matchlistsolo2
    global p1solochamps
    global p2solochamps
    global p1solowinchamps
    global p2solowinchamps
    global p1soloplayedchamps
    global p2soloplayedchamps
    global p1soloplayedchampscount
    global p2soloplayedchampscount
    global p1solowinchampscount
    global p2solowinchampscount
    


    

    #Api Key to update

    api = RiotAPI('API KEY GOES HERE')



    #clist1 = api.get_champ_list()

    clist1 = {'data': {'89': {'id': 89, 'key': 'Leona', 'name': 'Leona', 'title': 'the Radiant Dawn'}, '110': {'id': 110, 'key': 'Varus', 'name': 'Varus', 'title': 'the Arrow of Retribution'}, '111': {'id': 111, 'key': 'Nautilus', 'name': 'Nautilus', 'title': 'the Titan of the Depths'}, '112': {'id': 112, 'key': 'Viktor', 'name': 'Viktor', 'title': 'the Machine Herald'}, '113': {'id': 113, 'key': 'Sejuani', 'name': 'Sejuani', 'title': 'Fury of the North'}, '114': {'id': 114, 'key': 'Fiora', 'name': 'Fiora', 'title': 'the Grand Duelist'}, '236': {'id': 236, 'key': 'Lucian', 'name': 'Lucian', 'title': 'the Purifier'}, '115': {'id': 115, 'key': 'Ziggs', 'name': 'Ziggs', 'title': 'the Hexplosives Expert'}, '117': {'id': 117, 'key': 'Lulu', 'name': 'Lulu', 'title': 'the Fae Sorceress'}, '90': {'id': 90, 'key': 'Malzahar', 'name': 'Malzahar', 'title': 'the Prophet of the Void'}, '238': {'id': 238, 'key': 'Zed', 'name': 'Zed', 'title': 'the Master of Shadows'}, '91': {'id': 91, 'key': 'Talon', 'name': 'Talon', 'title': "the Blade's Shadow"}, '119': {'id': 119, 'key': 'Draven', 'name': 'Draven', 'title': 'the Glorious Executioner'}, '92': {'id': 92, 'key': 'Riven', 'name': 'Riven', 'title': 'the Exile'}, '96': {'id': 96, 'key': 'KogMaw', 'name': "Kog'Maw", 'title': 'the Mouth of the Abyss'}, '10': {'id': 10, 'key': 'Kayle', 'name': 'Kayle', 'title': 'The Judicator'}, '98': {'id': 98, 'key': 'Shen', 'name': 'Shen', 'title': 'the Eye of Twilight'}, '99': {'id': 99, 'key': 'Lux', 'name': 'Lux', 'title': 'the Lady of Luminosity'}, '11': {'id': 11, 'key': 'MasterYi', 'name': 'Master Yi', 'title': 'the Wuju Bladesman'}, '12': {'id': 12, 'key': 'Alistar', 'name': 'Alistar', 'title': 'the Minotaur'}, '13': {'id': 13, 'key': 'Ryze', 'name': 'Ryze', 'title': 'the Rune Mage'}, '14': {'id': 14, 'key': 'Sion', 'name': 'Sion', 'title': 'The Undead Juggernaut'}, '15': {'id': 15, 'key': 'Sivir', 'name': 'Sivir', 'title': 'the Battle Mistress'}, '16': {'id': 16, 'key': 'Soraka', 'name': 'Soraka', 'title': 'the Starchild'}, '17': {'id': 17, 'key': 'Teemo', 'name': 'Teemo', 'title': 'the Swift Scout'}, '18': {'id': 18, 'key': 'Tristana', 'name': 'Tristana', 'title': 'the Yordle Gunner'}, '19': {'id': 19, 'key': 'Warwick', 'name': 'Warwick', 'title': 'the Uncaged Wrath of Zaun'}, '240': {'id': 240, 'key': 'Kled', 'name': 'Kled', 'title': 'the Cantankerous Cavalier'}, '120': {'id': 120, 'key': 'Hecarim', 'name': 'Hecarim', 'title': 'the Shadow of War'}, '121': {'id': 121, 'key': 'Khazix', 'name': "Kha'Zix", 'title': 'the Voidreaver'}, '1': {'id': 1, 'key': 'Annie', 'name': 'Annie', 'title': 'the Dark Child'}, '122': {'id': 122, 'key': 'Darius', 'name': 'Darius', 'title': 'the Hand of Noxus'}, '2': {'id': 2, 'key': 'Olaf', 'name': 'Olaf', 'title': 'the Berserker'}, '245': {'id': 245, 'key': 'Ekko', 'name': 'Ekko', 'title': 'the Boy Who Shattered Time'}, '3': {'id': 3, 'key': 'Galio', 'name': 'Galio', 'title': 'the Colossus'}, '4': {'id': 4, 'key': 'TwistedFate', 'name': 'Twisted Fate', 'title': 'the Card Master'}, '126': {'id': 126, 'key': 'Jayce', 'name': 'Jayce', 'title': 'the Defender of Tomorrow'}, '5': {'id': 5, 'key': 'XinZhao', 'name': 'Xin Zhao', 'title': 'the Seneschal of Demacia'}, '127': {'id': 127, 'key': 'Lissandra', 'name': 'Lissandra', 'title': 'the Ice Witch'}, '6': {'id': 6, 'key': 'Urgot', 'name': 'Urgot', 'title': 'the Dreadnought'}, '7': {'id': 7, 'key': 'Leblanc', 'name': 'LeBlanc', 'title': 'the Deceiver'}, '8': {'id': 8, 'key': 'Vladimir', 'name': 'Vladimir', 'title': 'the Crimson Reaper'}, '9': {'id': 9, 'key': 'Fiddlesticks', 'name': 'Fiddlesticks', 'title': 'the Harbinger of Doom'}, '20': {'id': 20, 'key': 'Nunu', 'name': 'Nunu', 'title': 'the Yeti Rider'}, '21': {'id': 21, 'key': 'MissFortune', 'name': 'Miss Fortune', 'title': 'the Bounty Hunter'}, '22': {'id': 22, 'key': 'Ashe', 'name': 'Ashe', 'title': 'the Frost Archer'}, '23': {'id': 23, 'key': 'Tryndamere', 'name': 'Tryndamere', 'title': 'the Barbarian King'}, '24': {'id': 24, 'key': 'Jax', 'name': 'Jax', 'title': 'Grandmaster at Arms'}, '25': {'id': 25, 'key': 'Morgana', 'name': 'Morgana', 'title': 'Fallen Angel'}, '26': {'id': 26, 'key': 'Zilean', 'name': 'Zilean', 'title': 'the Chronokeeper'}, '27': {'id': 27, 'key': 'Singed', 'name': 'Singed', 'title': 'the Mad Chemist'}, '28': {'id': 28, 'key': 'Evelynn', 'name': 'Evelynn', 'title': 'the Widowmaker'}, '29': {'id': 29, 'key': 'Twitch', 'name': 'Twitch', 'title': 'the Plague Rat'}, '131': {'id': 131, 'key': 'Diana', 'name': 'Diana', 'title': 'Scorn of the Moon'}, '133': {'id': 133, 'key': 'Quinn', 'name': 'Quinn', 'title': "Demacia's Wings"}, '254': {'id': 254, 'key': 'Vi', 'name': 'Vi', 'title': 'the Piltover Enforcer'}, '497': {'id': 497, 'key': 'Rakan', 'name': 'Rakan', 'title': 'The Charmer'}, '134': {'id': 134, 'key': 'Syndra', 'name': 'Syndra', 'title': 'the Dark Sovereign'}, '498': {'id': 498, 'key': 'Xayah', 'name': 'Xayah', 'title': 'the Rebel'}, '136': {'id': 136, 'key': 'AurelionSol', 'name': 'Aurelion Sol', 'title': 'The Star Forger'}, '412': {'id': 412, 'key': 'Thresh', 'name': 'Thresh', 'title': 'the Chain Warden'}, '30': {'id': 30, 'key': 'Karthus', 'name': 'Karthus', 'title': 'the Deathsinger'}, '31': {'id': 31, 'key': 'Chogath', 'name': "Cho'Gath", 'title': 'the Terror of the Void'}, '32': {'id': 32, 'key': 'Amumu', 'name': 'Amumu', 'title': 'the Sad Mummy'}, '33': {'id': 33, 'key': 'Rammus', 'name': 'Rammus', 'title': 'the Armordillo'}, '34': {'id': 34, 'key': 'Anivia', 'name': 'Anivia', 'title': 'the Cryophoenix'}, '35': {'id': 35, 'key': 'Shaco', 'name': 'Shaco', 'title': 'the Demon Jester'}, '36': {'id': 36, 'key': 'DrMundo', 'name': 'Dr. Mundo', 'title': 'the Madman of Zaun'}, '37': {'id': 37, 'key': 'Sona', 'name': 'Sona', 'title': 'Maven of the Strings'}, '38': {'id': 38, 'key': 'Kassadin', 'name': 'Kassadin', 'title': 'the Void Walker'}, '39': {'id': 39, 'key': 'Irelia', 'name': 'Irelia', 'title': 'the Will of the Blades'}, '141': {'id': 141, 'key': 'Kayn', 'name': 'Kayn', 'title': 'the Shadow Reaper'}, '143': {'id': 143, 'key': 'Zyra', 'name': 'Zyra', 'title': 'Rise of the Thorns'}, '266': {'id': 266, 'key': 'Aatrox', 'name': 'Aatrox', 'title': 'the Darkin Blade'}, '420': {'id': 420, 'key': 'Illaoi', 'name': 'Illaoi', 'title': 'the Kraken Priestess'}, '267': {'id': 267, 'key': 'Nami', 'name': 'Nami', 'title': 'the Tidecaller'}, '421': {'id': 421, 'key': 'RekSai', 'name': "Rek'Sai", 'title': 'the Void Burrower'}, '268': {'id': 268, 'key': 'Azir', 'name': 'Azir', 'title': 'the Emperor of the Sands'}, '427': {'id': 427, 'key': 'Ivern', 'name': 'Ivern', 'title': 'the Green Father'}, '429': {'id': 429, 'key': 'Kalista', 'name': 'Kalista', 'title': 'the Spear of Vengeance'}, '40': {'id': 40, 'key': 'Janna', 'name': 'Janna', 'title': "the Storm's Fury"}, '41': {'id': 41, 'key': 'Gangplank', 'name': 'Gangplank', 'title': 'the Saltwater Scourge'}, '42': {'id': 42, 'key': 'Corki', 'name': 'Corki', 'title': 'the Daring Bombardier'}, '43': {'id': 43, 'key': 'Karma', 'name': 'Karma', 'title': 'the Enlightened One'}, '44': {'id': 44, 'key': 'Taric', 'name': 'Taric', 'title': 'the Shield of Valoran'}, '45': {'id': 45, 'key': 'Veigar', 'name': 'Veigar', 'title': 'the Tiny Master of Evil'}, '48': {'id': 48, 'key': 'Trundle', 'name': 'Trundle', 'title': 'the Troll King'}, '150': {'id': 150, 'key': 'Gnar', 'name': 'Gnar', 'title': 'the Missing Link'}, '154': {'id': 154, 'key': 'Zac', 'name': 'Zac', 'title': 'the Secret Weapon'}, '432': {'id': 432, 'key': 'Bard', 'name': 'Bard', 'title': 'the Wandering Caretaker'}, '157': {'id': 157, 'key': 'Yasuo', 'name': 'Yasuo', 'title': 'the Unforgiven'}, '50': {'id': 50, 'key': 'Swain', 'name': 'Swain', 'title': 'the Master Tactician'}, '51': {'id': 51, 'key': 'Caitlyn', 'name': 'Caitlyn', 'title': 'the Sheriff of Piltover'}, '53': {'id': 53, 'key': 'Blitzcrank', 'name': 'Blitzcrank', 'title': 'the Great Steam Golem'}, '54': {'id': 54, 'key': 'Malphite', 'name': 'Malphite', 'title': 'Shard of the Monolith'}, '55': {'id': 55, 'key': 'Katarina', 'name': 'Katarina', 'title': 'the Sinister Blade'}, '56': {'id': 56, 'key': 'Nocturne', 'name': 'Nocturne', 'title': 'the Eternal Nightmare'}, '57': {'id': 57, 'key': 'Maokai', 'name': 'Maokai', 'title': 'the Twisted Treant'}, '58': {'id': 58, 'key': 'Renekton', 'name': 'Renekton', 'title': 'the Butcher of the Sands'}, '59': {'id': 59, 'key': 'JarvanIV', 'name': 'Jarvan IV', 'title': 'the Exemplar of Demacia'}, '161': {'id': 161, 'key': 'Velkoz', 'name': "Vel'Koz", 'title': 'the Eye of the Void'}, '163': {'id': 163, 'key': 'Taliyah', 'name': 'Taliyah', 'title': 'the Stoneweaver'}, '164': {'id': 164, 'key': 'Camille', 'name': 'Camille', 'title': 'the Steel Shadow'}, '201': {'id': 201, 'key': 'Braum', 'name': 'Braum', 'title': 'the Heart of the Freljord'}, '202': {'id': 202, 'key': 'Jhin', 'name': 'Jhin', 'title': 'the Virtuoso'}, '203': {'id': 203, 'key': 'Kindred', 'name': 'Kindred', 'title': 'The Eternal Hunters'}, '60': {'id': 60, 'key': 'Elise', 'name': 'Elise', 'title': 'the Spider Queen'}, '61': {'id': 61, 'key': 'Orianna', 'name': 'Orianna', 'title': 'the Lady of Clockwork'}, '62': {'id': 62, 'key': 'MonkeyKing', 'name': 'Wukong', 'title': 'the Monkey King'}, '63': {'id': 63, 'key': 'Brand', 'name': 'Brand', 'title': 'the Burning Vengeance'}, '64': {'id': 64, 'key': 'LeeSin', 'name': 'Lee Sin', 'title': 'the Blind Monk'}, '67': {'id': 67, 'key': 'Vayne', 'name': 'Vayne', 'title': 'the Night Hunter'}, '68': {'id': 68, 'key': 'Rumble', 'name': 'Rumble', 'title': 'the Mechanized Menace'}, '69': {'id': 69, 'key': 'Cassiopeia', 'name': 'Cassiopeia', 'title': "the Serpent's Embrace"}, '72': {'id': 72, 'key': 'Skarner', 'name': 'Skarner', 'title': 'the Crystal Vanguard'}, '74': {'id': 74, 'key': 'Heimerdinger', 'name': 'Heimerdinger', 'title': 'the Revered Inventor'}, '75': {'id': 75, 'key': 'Nasus', 'name': 'Nasus', 'title': 'the Curator of the Sands'}, '76': {'id': 76, 'key': 'Nidalee', 'name': 'Nidalee', 'title': 'the Bestial Huntress'}, '77': {'id': 77, 'key': 'Udyr', 'name': 'Udyr', 'title': 'the Spirit Walker'}, '78': {'id': 78, 'key': 'Poppy', 'name': 'Poppy', 'title': 'Keeper of the Hammer'}, '79': {'id': 79, 'key': 'Gragas', 'name': 'Gragas', 'title': 'the Rabble Rouser'}, '222': {'id': 222, 'key': 'Jinx', 'name': 'Jinx', 'title': 'the Loose Cannon'}, '101': {'id': 101, 'key': 'Xerath', 'name': 'Xerath', 'title': 'the Magus Ascendant'}, '102': {'id': 102, 'key': 'Shyvana', 'name': 'Shyvana', 'title': 'the Half-Dragon'}, '223': {'id': 223, 'key': 'TahmKench', 'name': 'Tahm Kench', 'title': 'the River King'}, '103': {'id': 103, 'key': 'Ahri', 'name': 'Ahri', 'title': 'the Nine-Tailed Fox'}, '104': {'id': 104, 'key': 'Graves', 'name': 'Graves', 'title': 'the Outlaw'}, '105': {'id': 105, 'key': 'Fizz', 'name': 'Fizz', 'title': 'the Tidal Trickster'}, '106': {'id': 106, 'key': 'Volibear', 'name': 'Volibear', 'title': "the Thunder's Roar"}, '80': {'id': 80, 'key': 'Pantheon', 'name': 'Pantheon', 'title': 'the Artisan of War'}, '107': {'id': 107, 'key': 'Rengar', 'name': 'Rengar', 'title': 'the Pridestalker'}, '81': {'id': 81, 'key': 'Ezreal', 'name': 'Ezreal', 'title': 'the Prodigal Explorer'}, '82': {'id': 82, 'key': 'Mordekaiser', 'name': 'Mordekaiser', 'title': 'the Iron Revenant'}, '83': {'id': 83, 'key': 'Yorick', 'name': 'Yorick', 'title': 'Shepherd of Souls'}, '84': {'id': 84, 'key': 'Akali', 'name': 'Akali', 'title': 'the Fist of Shadow'}, '85': {'id': 85, 'key': 'Kennen', 'name': 'Kennen', 'title': 'the Heart of the Tempest'}, '86': {'id': 86, 'key': 'Garen', 'name': 'Garen', 'title': 'The Might of Demacia'}}, 'type': 'champion', 'version': '7.15.1'}
    
    clist2 = clist1

    #print(clist1)

    cl1 = clist1['data']
    cl2 = clist2['data']

    for key in cl1:
        cl1[key]['Solowins'] = 0
        cl1[key]['Sologames'] = 0
        cl1[key]['Duowins'] = 0
        cl1[key]['Duogames'] = 0
        cl1[key]['Solokills'] = 0
        cl1[key]['Duokills'] = 0
        cl1[key]['Solokills'] = 0
        cl1[key]['Duoassists'] = 0
        cl1[key]['Soloassists'] = 0
        cl1[key]['Duodeaths'] = 0
        cl1[key]['Solodeaths'] = 0
        cl1[key]['DuoKDA'] = 0
        cl1[key]['SoloKDA'] = 0
        cl1[key]['Duoavgk'] = 0
        cl1[key]['Soloavgk'] = 0
        cl1[key]['Duoavgd'] = 0
        cl1[key]['Soloavgd'] = 0
        cl1[key]['Duoavga'] = 0
        cl1[key]['Soloavga'] = 0


    for key in cl2:
        cl2[key]['Solowins'] = 0
        cl2[key]['Sologames'] = 0
        cl2[key]['Duowins'] = 0
        cl2[key]['Duogames'] = 0
        cl2[key]['Solokills'] = 0
        cl2[key]['Duokills'] = 0
        cl2[key]['Solokills'] = 0
        cl2[key]['Duoassists'] = 0
        cl2[key]['Soloassists'] = 0
        cl2[key]['Duodeaths'] = 0
        cl2[key]['Solodeaths'] = 0
        cl2[key]['DuoKDA'] = 0
        cl2[key]['SoloKDA'] = 0
        cl2[key]['Duoavgk'] = 0
        cl2[key]['Soloavgk'] = 0
        cl2[key]['Duoavgd'] = 0
        cl2[key]['Soloavgd'] = 0
        cl2[key]['Duoavga'] = 0
        cl2[key]['Soloavga'] = 0
        

    #Famous Duos


    #Peng Yiliang    
    #TSM SlGHTSTONE

    #Peng Yiliang    
    #TSM SlGHTSTONE

    #doubleliftfanboy
    #Biofrost

    #doublelift
    #Biofrost

    #doublelift (65% WR!)
    #swifte

    #chowdog
    #chapanya


        

    #Get Summoner1name

    r1 = api.get_summoner_by_name('Gristom')
    print(r1['accountId'])

    sum1id = r1['accountId']
    
    #Get Summoner2name
    
    r2 = api.get_summoner_by_name('Alexninja')
    print(r2['accountId'])

    sum2id = r2['accountId']


    

    #Get match ids for sum1

    matchlist1 = []

    
    

    m1 = api.get_match_history(sum1id, 0)
    


    



    for i in range(len(m1['matches'])):
        
        matchlist1.append(m1['matches'][i]['gameId'])


    while m1['endIndex'] != m1['totalGames']:
        
        y = m1['endIndex']
        m1 = api.get_match_history(sum1id, y)

        for i in range(len(m1['matches'])):
        
            matchlist1.append(m1['matches'][i]['gameId'])

        


    print("MATCH LIST #1")
    print(len(matchlist1))        

        


    #Get match ids for sum2

    matchlist2 = []

    m2 = api.get_match_history(sum2id, 0)


 

    for i in range(len(m2['matches'])):
        
        matchlist2.append(m2['matches'][i]['gameId'])


    while m2['endIndex'] != m2['totalGames']:

        y = m2['endIndex']
        m2 = api.get_match_history(sum2id, y)

        for i in range(len(m2['matches'])):
        
            matchlist2.append(m2['matches'][i]['gameId'])



        

    print("MATCH LIST #2")
    print(len(matchlist2)) 


    #Create common match list

    matchlistcommon = sorted(list(set(matchlist1).intersection(matchlist2)), reverse=True)

    print("")
    print(matchlistcommon)


    #Create solo (uncommon) match list

    matchlistsolo1 = sorted([x for x in matchlist1 if x not in matchlistcommon], reverse=True)

    matchlistsolo2 = sorted([x for x in matchlist2 if x not in matchlistcommon], reverse=True)

    #Find win percent playing as duo

    def duorate():

        global winchampsdict
        global winchampscount
        global playedchampscount
        global winratecommon
        global p1champscount
        global p2champscount
        global p1winchampscount
        global p2winchampscount

        for i in range(len(matchlistcommon)):

            global winchamps1
            global winchamps2
            global winchampscommon
            global playedchampscommon

            global losechamps1
            global losechamps2
            global losechampscommon

            global p1champs
            global p2champs

            global p1winchamps
            global p2winchamps

            global matchlistsolo1
            global matchlistsolo2

            

        
            #matchlist1.append(m1['matches'][i]['gameId'])

            pid1 = 0
            pid2 = 0

           
            
            j1 = api.get_match_info(matchlistcommon[i])

            if j1['participantIdentities'][0]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][0]['participantId'])

            elif j1['participantIdentities'][1]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][1]['participantId'])

            elif j1['participantIdentities'][2]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][2]['participantId'])

            elif j1['participantIdentities'][3]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][3]['participantId'])

            elif j1['participantIdentities'][4]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][4]['participantId'])
                
            elif j1['participantIdentities'][5]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][5]['participantId'])

            elif j1['participantIdentities'][6]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][6]['participantId'])

            elif j1['participantIdentities'][7]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][7]['participantId'])

            elif j1['participantIdentities'][8]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][8]['participantId'])

            elif j1['participantIdentities'][9]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][9]['participantId'])

            else:

                print("Summoner 1 Not Found")


            if j1['participantIdentities'][0]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][0]['participantId'])

            elif j1['participantIdentities'][1]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][1]['participantId'])

            elif j1['participantIdentities'][2]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][2]['participantId'])

            elif j1['participantIdentities'][3]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][3]['participantId'])

            elif j1['participantIdentities'][4]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][4]['participantId'])
                
            elif j1['participantIdentities'][5]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][5]['participantId'])

            elif j1['participantIdentities'][6]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][6]['participantId'])

            elif j1['participantIdentities'][7]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][7]['participantId'])

            elif j1['participantIdentities'][8]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][8]['participantId'])

            elif j1['participantIdentities'][9]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][9]['participantId'])

            else:

                print("Summoner 2 Not Found")




            global wincountcommon
            global gamecountcommon

            if j1['gameDuration'] < 360:

                gamecountcommon=gamecountcommon


            elif j1['participants'][pid1-1]['stats']['win'] == True and j1['participants'][pid2-1]['stats']['win'] == True:
                

                print(j1['participants'][pid1-1]['championId'])
                print(j1['participants'][pid2-1]['championId'])

                winchamps1.append(j1['participants'][pid1-1]['championId'])
                winchamps2.append(j1['participants'][pid2-1]['championId'])

                winchampscommon.append(str([j1['participants'][pid1-1]['championId'], j1['participants'][pid2-1]['championId']]))

                playedchampscommon.append(str([j1['participants'][pid1-1]['championId'], j1['participants'][pid2-1]['championId']]))

                p1winchamps.append(j1['participants'][pid1-1]['championId'])
                p2winchamps.append(j1['participants'][pid2-1]['championId']) 

                p1champs.append(j1['participants'][pid1-1]['championId'])
                p2champs.append(j1['participants'][pid2-1]['championId'])                
                

                cl1[str(j1['participants'][pid1-1]['championId'])]['Duowins'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Duowins'] + 1
                cl1[str(j1['participants'][pid1-1]['championId'])]['Duogames'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Duogames'] + 1

                cl2[str(j1['participants'][pid2-1]['championId'])]['Duowins'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Duowins'] + 1
                cl2[str(j1['participants'][pid2-1]['championId'])]['Duogames'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Duogames'] + 1

                cl1[str(j1['participants'][pid1-1]['championId'])]['Duokills'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Duokills'] + j1['participants'][pid1-1]['stats']['kills']
                cl1[str(j1['participants'][pid1-1]['championId'])]['Duodeaths'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Duodeaths'] + j1['participants'][pid1-1]['stats']['deaths']
                cl1[str(j1['participants'][pid1-1]['championId'])]['Duoassists'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Duoassists'] + j1['participants'][pid1-1]['stats']['assists']
                
                cl2[str(j1['participants'][pid2-1]['championId'])]['Duokills'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Duokills'] + j1['participants'][pid2-1]['stats']['kills']
                cl2[str(j1['participants'][pid2-1]['championId'])]['Duodeaths'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Duodeaths'] + j1['participants'][pid2-1]['stats']['deaths']
                cl2[str(j1['participants'][pid2-1]['championId'])]['Duoassists'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Duoassists'] + j1['participants'][pid2-1]['stats']['assists']
                

                
                wincountcommon=wincountcommon+1
                gamecountcommon=gamecountcommon+1

            elif j1['participants'][pid1-1]['stats']['win'] == False and j1['participants'][pid2-1]['stats']['win'] == False:


                print(j1['participants'][pid1-1]['championId'])
                print(j1['participants'][pid2-1]['championId'])

                losechamps1.append(j1['participants'][pid1-1]['championId'])
                losechamps2.append(j1['participants'][pid2-1]['championId'])

                losechampscommon.append([j1['participants'][pid1-1]['championId'], j1['participants'][pid2-1]['championId']])

                playedchampscommon.append(str([j1['participants'][pid1-1]['championId'], j1['participants'][pid2-1]['championId']]))

                p1champs.append(j1['participants'][pid1-1]['championId'])
                p2champs.append(j1['participants'][pid2-1]['championId']) 

              
                cl1[str(j1['participants'][pid1-1]['championId'])]['Duogames'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Duogames'] + 1

               
                cl2[str(j1['participants'][pid2-1]['championId'])]['Duogames'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Duogames'] + 1


                cl1[str(j1['participants'][pid1-1]['championId'])]['Duokills'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Duokills'] + j1['participants'][pid1-1]['stats']['kills']
                cl1[str(j1['participants'][pid1-1]['championId'])]['Duodeaths'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Duodeaths'] + j1['participants'][pid1-1]['stats']['deaths']
                cl1[str(j1['participants'][pid1-1]['championId'])]['Duoassists'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Duoassists'] + j1['participants'][pid1-1]['stats']['assists']
                
                cl2[str(j1['participants'][pid2-1]['championId'])]['Duokills'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Duokills'] + j1['participants'][pid2-1]['stats']['kills']
                cl2[str(j1['participants'][pid2-1]['championId'])]['Duodeaths'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Duodeaths'] + j1['participants'][pid2-1]['stats']['deaths']
                cl2[str(j1['participants'][pid2-1]['championId'])]['Duoassists'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Duoassists'] + j1['participants'][pid2-1]['stats']['assists']


                
                gamecountcommon=gamecountcommon+1

            else:

                matchlistsolo1.append(matchlistcommon[i])
                matchlistsolo2.append(matchlistcommon[i])

                matchlistsolo1 = sorted(matchlistsolo1, reverse=True)
                matchlistsolo2 = sorted(matchlistsolo2, reverse=True)

                gamecountcommon=gamecountcommon

        for key in cl1:

                try:
                    cl1[key]['DuoKDA'] = (cl1[key]['Duokills']+cl1[key]['Duoassists'])/cl1[key]['Duodeaths']
                except ZeroDivisionError:
                    cl1[key]['DuoKDA'] = 0

                try:
                    cl1[key]['SoloKDA'] = (cl1[key]['Solokills']+cl1[key]['Soloassists'])/cl1[key]['Solodeaths']
                except ZeroDivisionError:
                    cl1[key]['SoloKDA'] = 0

                try:
                    cl1[key]['Duoavgk'] = cl1[key]['Duokills']/cl1[key]['Duogames']
                except ZeroDivisionError:
                    cl1[key]['Duoavgk'] = 0

                try:
                    cl1[key]['Soloavgk'] = cl1[key]['Solokills']/cl1[key]['Sologames']
                except ZeroDivisionError:
                    cl1[key]['Soloavgk'] = 0


                try:
                    cl1[key]['Duoavgd'] = cl1[key]['Duodeaths']/cl1[key]['Duogames']
                except ZeroDivisionError:
                    cl1[key]['Duoavgd'] = 0

                try:
                    cl1[key]['Soloavgd'] = cl1[key]['Solodeaths']/cl1[key]['Sologames']
                except ZeroDivisionError:
                    cl1[key]['Soloavgd'] = 0


                try:
                    cl1[key]['Duoavga'] = cl1[key]['Duoassists']/cl1[key]['Duogames']
                except ZeroDivisionError:
                    cl1[key]['Duoavga'] = 0

                try:
                    cl1[key]['Soloavga'] = cl1[key]['Soloassists']/cl1[key]['Sologames']
                except ZeroDivisionError:
                    cl1[key]['Soloavga'] = 0  


        for key in cl2:
            
                try:
                    cl2[key]['DuoKDA'] = (cl2[key]['Duokills']+cl2[key]['Duoassists'])/cl2[key]['Duodeaths']
                except ZeroDivisionError:
                    cl2[key]['DuoKDA'] = 0

                try:
                    cl2[key]['SoloKDA'] = (cl2[key]['Solokills']+cl2[key]['Soloassists'])/cl2[key]['Solodeaths']
                except ZeroDivisionError:
                    cl2[key]['SoloKDA'] = 0

                try:
                    cl2[key]['Duoavgk'] = cl2[key]['Duokills']/cl2[key]['Duogames']
                except ZeroDivisionError:
                    cl2[key]['Duoavgk'] = 0

                try:
                    cl2[key]['Soloavgk'] = cl2[key]['Solokills']/cl2[key]['Sologames']
                except ZeroDivisionError:
                    cl2[key]['Soloavgk'] = 0


                try:
                    cl2[key]['Duoavgd'] = cl2[key]['Duodeaths']/cl2[key]['Duogames']
                except ZeroDivisionError:
                    cl2[key]['Duoavgd'] = 0

                try:
                    cl2[key]['Soloavgd'] = cl2[key]['Solodeaths']/cl2[key]['Sologames']
                except ZeroDivisionError:
                    cl2[key]['Soloavgd'] = 0


                try:
                    cl2[key]['Duoavga'] = cl2[key]['Duoassists']/cl2[key]['Duogames']
                except ZeroDivisionError:
                    cl2[key]['Duoavga'] = 0

                try:
                    cl2[key]['Soloavga'] = cl2[key]['Soloassists']/cl2[key]['Sologames']
                except ZeroDivisionError:
                    cl2[key]['Soloavga'] = 0


                
        #winchampsdict = {winchampscommon:0 for winchampscommon in a}
        winchampscount = Counter(winchampscommon)
        playedchampscount = Counter(playedchampscommon)

        p1champscount = Counter(p1champs)
        p2champscount = Counter(p2champs)

        p1winchampscount = Counter(p1winchamps)
        p2winchampscount = Counter(p2winchamps)

        
        
        winchampsdict = dict.fromkeys(winchampscommon, 0)
        #losechampsdict = dict.fromkeys(losechampscommon, 0)


                

        print(wincountcommon)
        print(gamecountcommon)
        winpercentcommon=wincountcommon/gamecountcommon*100
        print(winpercentcommon)


        
    #Find win percentage playing without partner

    def solorate():

        global p1solochamps
        global p2solochamps
        global p1solowinchamps
        global p2solowinchamps
        global p1soloplayedchamps
        global p2soloplayedchamps
        global p1soloplayedchampscount
        global p1solowinchampscount
        global p2solowinchampscount


        for i in range(len(matchlistsolo1)):


            pid1 = 0
            pid2 = 0
            
            j1 = api.get_match_info(matchlistsolo1[i])

            if j1['participantIdentities'][0]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][0]['participantId'])

            elif j1['participantIdentities'][1]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][1]['participantId'])

            elif j1['participantIdentities'][2]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][2]['participantId'])

            elif j1['participantIdentities'][3]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][3]['participantId'])

            elif j1['participantIdentities'][4]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][4]['participantId'])
                
            elif j1['participantIdentities'][5]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][5]['participantId'])

            elif j1['participantIdentities'][6]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][6]['participantId'])

            elif j1['participantIdentities'][7]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][7]['participantId'])

            elif j1['participantIdentities'][8]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][8]['participantId'])

            elif j1['participantIdentities'][9]['player']['currentAccountId'] == sum1id:

                pid1=(j1['participantIdentities'][9]['participantId'])

            else:

                print("Error")


            global wincountp1solo
            global gamecountp1solo


            if j1['gameDuration'] < 360:

                gamecountp1solo=gamecountp1solo


            elif j1['participants'][pid1-1]['stats']['win'] == True:

                cl1[str(j1['participants'][pid1-1]['championId'])]['Solowins'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Solowins'] + 1
                cl1[str(j1['participants'][pid1-1]['championId'])]['Sologames'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Sologames'] + 1


                cl1[str(j1['participants'][pid1-1]['championId'])]['Solokills'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Solokills'] + j1['participants'][pid1-1]['stats']['kills']
                cl1[str(j1['participants'][pid1-1]['championId'])]['Solodeaths'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Solodeaths'] + j1['participants'][pid1-1]['stats']['deaths']
                cl1[str(j1['participants'][pid1-1]['championId'])]['Soloassists'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Soloassists'] + j1['participants'][pid1-1]['stats']['assists']


                p1solowinchamps.append(j1['participants'][pid1-1]['championId'])
                

                p1soloplayedchamps.append(j1['participants'][pid1-1]['championId'])
               

                
                wincountp1solo=wincountp1solo+1
                gamecountp1solo=gamecountp1solo+1

            elif j1['participants'][pid1-1]['stats']['win'] == False:


                cl1[str(j1['participants'][pid1-1]['championId'])]['Sologames'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Sologames'] + 1


                cl1[str(j1['participants'][pid1-1]['championId'])]['Solokills'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Solokills'] + j1['participants'][pid1-1]['stats']['kills']
                cl1[str(j1['participants'][pid1-1]['championId'])]['Solodeaths'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Solodeaths'] + j1['participants'][pid1-1]['stats']['deaths']
                cl1[str(j1['participants'][pid1-1]['championId'])]['Soloassists'] = cl1[str(j1['participants'][pid1-1]['championId'])]['Soloassists'] + j1['participants'][pid1-1]['stats']['assists']

                p1soloplayedchamps.append(j1['participants'][pid1-1]['championId'])

                gamecountp1solo=gamecountp1solo+1

            else:

                gamecountp1solo=gamecountp1solo

            for key in cl1:

                try:
                    cl1[key]['DuoKDA'] = (cl1[key]['Duokills']+cl1[key]['Duoassists'])/cl1[key]['Duodeaths']
                except ZeroDivisionError:
                    cl1[key]['DuoKDA'] = 0

                try:
                    cl1[key]['SoloKDA'] = (cl1[key]['Solokills']+cl1[key]['Soloassists'])/cl1[key]['Solodeaths']
                except ZeroDivisionError:
                    cl1[key]['SoloKDA'] = 0

                try:
                    cl1[key]['Duoavgk'] = cl1[key]['Duokills']/cl1[key]['Duogames']
                except ZeroDivisionError:
                    cl1[key]['Duoavgk'] = 0

                try:
                    cl1[key]['Soloavgk'] = cl1[key]['Solokills']/cl1[key]['Sologames']
                except ZeroDivisionError:
                    cl1[key]['Soloavgk'] = 0


                try:
                    cl1[key]['Duoavgd'] = cl1[key]['Duodeaths']/cl1[key]['Duogames']
                except ZeroDivisionError:
                    cl1[key]['Duoavgd'] = 0

                try:
                    cl1[key]['Soloavgd'] = cl1[key]['Solodeaths']/cl1[key]['Sologames']
                except ZeroDivisionError:
                    cl1[key]['Soloavgd'] = 0


                try:
                    cl1[key]['Duoavga'] = cl1[key]['Duoassists']/cl1[key]['Duogames']
                except ZeroDivisionError:
                    cl1[key]['Duoavga'] = 0

                try:
                    cl1[key]['Soloavga'] = cl1[key]['Soloassists']/cl1[key]['Sologames']
                except ZeroDivisionError:
                    cl1[key]['Soloavga'] = 0



            p1solowinchampscount = Counter(p1solowinchamps)
            p1soloplayedchampscount = Counter(p1soloplayedchamps)



            p1champscount = Counter(p1champs)
   

            p1winchampscount = Counter(p1winchamps)
         

        
        
            p1solowinchampsdict = dict.fromkeys(p1solowinchamps, 0)


            print(wincountp1solo)
            print(gamecountp1solo)
            winpercentp1solo=wincountp1solo/gamecountp1solo*100
            print(winpercentp1solo)

    #Your partners rate when not playing with you                

    def partnerrate():

        global p1solochamps
        global p2solochamps
        global p1solowinchamps
        global p2solowinchamps
        global p1soloplayedchamps
        global p2soloplayedchamps
        global p2soloplayedchampscount
        global p1solowinchampscount
        global p2solowinchampscount

        for i in range(len(matchlistsolo2)):


            pid1 = 0
            pid2 = 0
            
            j1 = api.get_match_info(matchlistsolo2[i])

            if j1['participantIdentities'][0]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][0]['participantId'])

            elif j1['participantIdentities'][1]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][1]['participantId'])

            elif j1['participantIdentities'][2]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][2]['participantId'])

            elif j1['participantIdentities'][3]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][3]['participantId'])

            elif j1['participantIdentities'][4]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][4]['participantId'])
                
            elif j1['participantIdentities'][5]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][5]['participantId'])

            elif j1['participantIdentities'][6]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][6]['participantId'])

            elif j1['participantIdentities'][7]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][7]['participantId'])

            elif j1['participantIdentities'][8]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][8]['participantId'])

            elif j1['participantIdentities'][9]['player']['currentAccountId'] == sum2id:

                pid2=(j1['participantIdentities'][9]['participantId'])

            else:

                print("Error")


            global wincountp2solo
            global gamecountp2solo



            if j1['gameDuration'] < 360:

                gamecountp2solo=gamecountp2solo
                print("REMAKE")
                print(gamecountp2solo)
            


            elif j1['participants'][pid2-1]['stats']['win'] == True:

                cl2[str(j1['participants'][pid2-1]['championId'])]['Solowins'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Solowins'] + 1
                cl2[str(j1['participants'][pid2-1]['championId'])]['Sologames'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Sologames'] + 1


                cl2[str(j1['participants'][pid2-1]['championId'])]['Solokills'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Solokills'] + j1['participants'][pid2-1]['stats']['kills']
                cl2[str(j1['participants'][pid2-1]['championId'])]['Solodeaths'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Solodeaths'] + j1['participants'][pid2-1]['stats']['deaths']
                cl2[str(j1['participants'][pid2-1]['championId'])]['Soloassists'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Soloassists'] + j1['participants'][pid2-1]['stats']['assists']                

                p2solowinchamps.append(j1['participants'][pid2-1]['championId'])
                

                p2soloplayedchamps.append(j1['participants'][pid2-1]['championId'])


                        
                wincountp2solo=wincountp2solo+1
                gamecountp2solo=gamecountp2solo+1

                print("WIN")
                print(gamecountp2solo)

            elif j1['participants'][pid2-1]['stats']['win'] == False:


                cl2[str(j1['participants'][pid2-1]['championId'])]['Sologames'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Sologames'] + 1


                cl2[str(j1['participants'][pid2-1]['championId'])]['Solokills'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Solokills'] + j1['participants'][pid2-1]['stats']['kills']
                cl2[str(j1['participants'][pid2-1]['championId'])]['Solodeaths'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Solodeaths'] + j1['participants'][pid2-1]['stats']['deaths']
                cl2[str(j1['participants'][pid2-1]['championId'])]['Soloassists'] = cl2[str(j1['participants'][pid2-1]['championId'])]['Soloassists'] + j1['participants'][pid2-1]['stats']['assists'] 

                p2soloplayedchamps.append(j1['participants'][pid2-1]['championId'])


                gamecountp2solo=gamecountp2solo+1

                print("LOSE")
                print(gamecountp2solo)

            else:

                gamecountp2solo=gamecountp2solo
                print("winlose not found error")



            print(wincountp2solo)
            print(gamecountp2solo)
            winpercentp2solo=wincountp2solo/gamecountp2solo*100
            print(winpercentp2solo)
            

            for key in cl2:
            
                try:
                    cl2[key]['DuoKDA'] = (cl2[key]['Duokills']+cl2[key]['Duoassists'])/cl2[key]['Duodeaths']
                except ZeroDivisionError:
                    cl2[key]['DuoKDA'] = 0

                try:
                    cl2[key]['SoloKDA'] = (cl2[key]['Solokills']+cl2[key]['Soloassists'])/cl2[key]['Solodeaths']
                except ZeroDivisionError:
                    cl2[key]['SoloKDA'] = 0

                try:
                    cl2[key]['Duoavgk'] = cl2[key]['Duokills']/cl2[key]['Duogames']
                except ZeroDivisionError:
                    cl2[key]['Duoavgk'] = 0

                try:
                    cl2[key]['Soloavgk'] = cl2[key]['Solokills']/cl2[key]['Sologames']
                except ZeroDivisionError:
                    cl2[key]['Soloavgk'] = 0


                try:
                    cl2[key]['Duoavgd'] = cl2[key]['Duodeaths']/cl2[key]['Duogames']
                except ZeroDivisionError:
                    cl2[key]['Duoavgd'] = 0

                try:
                    cl2[key]['Soloavgd'] = cl2[key]['Solodeaths']/cl2[key]['Sologames']
                except ZeroDivisionError:
                    cl2[key]['Soloavgd'] = 0


                try:
                    cl2[key]['Duoavga'] = cl2[key]['Duoassists']/cl2[key]['Duogames']
                except ZeroDivisionError:
                    cl2[key]['Duoavga'] = 0

                try:
                    cl2[key]['Soloavga'] = cl2[key]['Soloassists']/cl2[key]['Sologames']
                except ZeroDivisionError:
                    cl2[key]['Soloavga'] = 0




            p2solowinchampscount = Counter(p2solowinchamps)
            p2soloplayedchampscount = Counter(p2soloplayedchamps)

           
            p2champscount = Counter(p2champs)

          
            p2winchampscount = Counter(p2winchamps)

        
        
            
            p2solowinchampsdict = dict.fromkeys(p2solowinchamps, 0)
               

        

        

        #print(j1['participantIdentities'][0]['player']['summonerId'])

        #print(j1)
  
    #j1 = api.get_match_info(matchlistcommon[-1])
    #print(j1)

    duorate()
    solorate()
    partnerrate()

    


    playedchampsind = []

    wrcommon = []
    c1common = []
    c2common = []

    wrp1solo = []
    wrp2solo = []

    c1namecommon = []
    c2namecommon = []

    commonwr = []

    p1solowr = []
    p2solowr = []

    gpcommon = []
    
    k1common = []
    k2common = []
    d1common = []
    d2common = []
    a1common = []
    a2common = []
    kda1common = []
    kda2common = []

    maxwr = []

    maxwin = []
    maxwinp1 = []
    maxwinp2 = []
    
    maxwinpercent = []
    maxwrgp = []

    maxwinratecommon = []
    winratemax = {}

    maxwinc1 = []
    maxwinc2 = []
    maxwinc1name = []
    maxwinc2name = []
    maxwink1 = []
    maxwink2 = []
    maxwind1 = []
    maxwind2 = []
    maxwina1 = []
    maxwina2 = []
    maxwinkda1 = []
    maxwinkda2 = []

    p1win = {}
    p2win = {}


    #solo stats

    c1soloname = []
    c2soloname = []
        
    k1solo = []
    k2solo = []

    d1solo = []
    d2solo = []

    a1solo = []
    a2solo = []

    kda1solo = []
    kda2solo = []

    gp1 = []
    gp2 = []


    # if v >= 2** controls minimum games played with champ combo to register

    playedchampscount = {k: v for k, v, in playedchampscount.items() if v >= 0}
    playedchampskeys = heapq.nlargest(200, playedchampscount, key=playedchampscount.get)

    maxwrchampscount = playedchampscount

    maxwrchampscount = {k: v for k, v, in maxwrchampscount.items() if v >= 0}#was 2
    maxwrchampskeys = heapq.nlargest(200, maxwrchampscount, key=maxwrchampscount.get)


    p1champscount = {k: v for k, v, in p1champscount.items() if v >= 0}
    p2champscount = {k: v for k, v, in p2champscount.items() if v >= 0}

    p1champskeys = heapq.nlargest(200, p1champscount, key=p1champscount.get)
    p2champskeys = heapq.nlargest(200, p2champscount, key=p2champscount.get)


    #need alternative if no champ with 5 played
    
    p1champsmaxwr = {k: v for k, v, in p1champscount.items() if v >= 0}#was2
    p2champsmaxwr = {k: v for k, v, in p2champscount.items() if v >= 0}#was2

    p1champsmaxwrkeys = heapq.nlargest(200, p1champscount, key=p1champscount.get)
    p2champsmaxwrkeys = heapq.nlargest(200, p2champscount, key=p2champscount.get)


    p1soloplayedchampscount = {k: v for k, v, in p1soloplayedchampscount.items() if v >= 0}
    p1soloplayedchampskeys = heapq.nlargest(200, p1soloplayedchampscount, key=p1soloplayedchampscount.get)

    p2soloplayedchampscount = {k: v for k, v, in p2soloplayedchampscount.items() if v >= 0}
    p2soloplayedchampskeys = heapq.nlargest(200, p2soloplayedchampscount, key=p2soloplayedchampscount.get)

    print(p1solowinrate)        

    

    
    

    



    for i in range(len(playedchampskeys)):
        
        playedchampsind.append(playedchampskeys[i].translate(str.maketrans('','','[](){}<>,')))
        playedchampsind[i] = playedchampsind[i].split()
        gpcommon.append(playedchampscount[playedchampskeys[i]])

    for i in range(len(p1soloplayedchampskeys)):
        
        gp1.append(p1soloplayedchampscount[p1soloplayedchampskeys[i]])

    for i in range(len(p2soloplayedchampskeys)):
        
        gp2.append(p2soloplayedchampscount[p2soloplayedchampskeys[i]])
        

  

    for key in playedchampscount:
        try:
            winratecommon[key] = winchampscount[key]/playedchampscount[key]
            wrcommon.append(winchampscount[key]/playedchampscount[key])
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")


    for key in maxwrchampscount:
        try:
            winratemax[key] = winchampscount[key]/maxwrchampscount[key]
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")
            

    for key in p1champsmaxwr:
        try:
            p1win[key] = p1winchampscount[key]/p1champscount[key]
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")

    for key in p2champsmaxwr:
        try:
            p2win[key] = p2winchampscount[key]/p2champscount[key]
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")


    for key in p1soloplayedchampscount:
        try:
            p1solowinrate[key] = p1solowinchampscount[key]/p1soloplayedchampscount[key]
            wrp1solo.append(p1solowinchampscount[key]/p1soloplayedchampscount[key])
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")
        except IndexError:
            print("Index Error")

    for key in p2soloplayedchampscount:
        try:
            p2solowinrate[key] = p2solowinchampscount[key]/p2soloplayedchampscount[key]
            wrp2solo.append(p2solowinchampscount[key]/p2soloplayedchampscount[key])
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")
        except IndexError:
            print("Index Error")


    



    for key in playedchampskeys:
        try:
            commonwr.append((winratecommon[key])*100)
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")


    for key in maxwrchampskeys:
        try:
            maxwin.append(winratemax[key])
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")
            

    for key in p1champsmaxwrkeys:
        try:
            maxwinp1.append(p1win[key])
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")

    for key in p2champsmaxwrkeys:
        try:
            maxwinp2.append(p2win[key])
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")

    for key in p1soloplayedchampskeys:
        try:
            p1solowr.append((p1solowinrate[key])*100)
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")

    for key in p2soloplayedchampskeys:
        try:
            p2solowr.append((p2solowinrate[key])*100)
        except ZeroDivisionError:
            print("not enough games played")
        except KeyError:
            print("not enough games played")


            


    print("PLAYEDCHAMPSIND")
    print(playedchampsind)

    for i in range(len(playedchampsind)):
        
        c1common.append(playedchampsind[i][0])
        c2common.append(playedchampsind[i][1])

    for i in range(len(c1common)):

        c1namecommon.append(cl1[c1common[i]]['name'])
        c2namecommon.append(cl2[c2common[i]]['name'])
        
        k1common.append(cl1[c1common[i]]['Duoavgk'])
        k2common.append(cl2[c2common[i]]['Duoavgk'])

        d1common.append(cl1[c1common[i]]['Duoavgd'])
        d2common.append(cl2[c2common[i]]['Duoavgd'])

        a1common.append(cl1[c1common[i]]['Duoavga'])
        a2common.append(cl2[c2common[i]]['Duoavga'])

        kda1common.append(cl1[c1common[i]]['DuoKDA'])
        kda2common.append(cl2[c2common[i]]['DuoKDA'])



    for i in range(len(p1soloplayedchampskeys)):

        c1soloname.append(cl1[str(p1soloplayedchampskeys[i])]['name'])
        
        k1solo.append(cl1[str(p1soloplayedchampskeys[i])]['Soloavgk'])

        d1solo.append(cl1[str(p1soloplayedchampskeys[i])]['Soloavgd'])

        a1solo.append(cl1[str(p1soloplayedchampskeys[i])]['Soloavga'])
    
        kda1solo.append(cl1[str(p1soloplayedchampskeys[i])]['SoloKDA'])


    for i in range(len(p2soloplayedchampskeys)):

        c2soloname.append(cl2[str(p2soloplayedchampskeys[i])]['name'])
        
        k2solo.append(cl2[str(p2soloplayedchampskeys[i])]['Soloavgk'])

        d2solo.append(cl2[str(p2soloplayedchampskeys[i])]['Soloavgd'])

        a2solo.append(cl2[str(p2soloplayedchampskeys[i])]['Soloavga'])
    
        kda2solo.append(cl2[str(p2soloplayedchampskeys[i])]['SoloKDA'])


        
       
    print(winpercentcommon)
    print(winpercentp1solo)
    print(winpercentp2solo)
    print("This is it....")
    print(gamecountcommon)
    print(gamecountp1solo)
    print(gamecountp2solo)


    for i in range(len(c1namecommon)):

        print("")
        print("Games Played: " + str(gpcommon[i]))
        print("Win Rate: " + str(Decimal(commonwr[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))) 
        print(c1namecommon[i] + ": "+str(Decimal(k1common[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+"/"+str(Decimal(d1common[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+"/"+str(Decimal(a1common[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+" KDA: "+str(Decimal(kda1common[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
        print(c2namecommon[i] + ": "+str(Decimal(k2common[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+"/"+str(Decimal(d2common[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+"/"+str(Decimal(a2common[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+" KDA: "+str(Decimal(kda2common[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
        print("")


    for i in range(len(c1soloname)):

        print("")
        print("Games Played: " + str(gp1[i]))
        print("Win Rate: " + str(Decimal(p1solowr[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))) 
        print(c1soloname[i] + ": "+str(Decimal(k1solo[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+"/"+str(Decimal(d1solo[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+"/"+str(Decimal(a1solo[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+" KDA: "+str(Decimal(kda1solo[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
        print("")

    for i in range(len(c2soloname)):

        print("")
        print("Games Played: " + str(gp2[i]))
        print("Win Rate: " + str(Decimal(p2solowr[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))) 
        print(c2soloname[i] + ": "+str(Decimal(k2solo[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+"/"+str(Decimal(d2solo[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+"/"+str(Decimal(a2solo[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))+" KDA: "+str(Decimal(kda2solo[i]).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
        print("")

    
        



    #Maxwrcommonchamps
    
    maxwinrate = max(winratemax, key=winratemax.get)
    

    maxwinpercent = (winchampscount[maxwinrate]/playedchampscount[maxwinrate]) * 100

    maxwr.append(maxwinrate.translate(str.maketrans('','','[](){}<>,')))
    
    maxwr[0] = maxwr[0].split()
    
    maxwinc1 = maxwr[0][0]
    maxwinc2 = maxwr[0][1]

    maxwrgp = playedchampscount[maxwinrate]

    maxwinc1name = cl1[maxwinc1]['name']
    maxwinc2name = cl2[maxwinc2]['name']

    maxwink1 = cl1[maxwinc1]['Duoavgk']
    maxwink2 = cl2[maxwinc2]['Duoavgk']
    
    maxwind1 = cl1[maxwinc1]['Duoavgd']
    maxwind2 = cl2[maxwinc2]['Duoavgd']
    
    maxwina1 = cl1[maxwinc1]['Duoavga']
    maxwina2 = cl2[maxwinc2]['Duoavga']
    
    maxwinkda1 = cl1[maxwinc1]['DuoKDA']
    maxwinkda2 = cl2[maxwinc2]['DuoKDA']



    print("")
    print(maxwrgp)
    print(maxwinpercent)
    print(maxwinc1name)
    print(maxwinc2name)
    print(maxwinc1)
    print(maxwinc2)
    print(maxwink1)
    print(maxwink2)
    print(maxwind1)
    print(maxwind2)
    print(maxwina1)
    print(maxwina2)
    print(maxwinkda1)
    print(maxwinkda2)
    print("")


    #Max win rate individual champs

    p1maxwinrate = max(p1win, key=p1win.get)    
    p2maxwinrate = max(p2win, key=p2win.get)

    maxwinpercentp1 = p1winchampscount[p1maxwinrate]/p1champscount[p1maxwinrate]
    maxwinpercentp2 = p2winchampscount[p2maxwinrate]/p2champscount[p2maxwinrate]


    p1maxwinname = cl1[str(p1maxwinrate)]['name']
    p2maxwinname = cl2[str(p2maxwinrate)]['name']

    p1maxwingames = cl1[str(p1maxwinrate)]['Duogames']
    p2maxwingames = cl2[str(p2maxwinrate)]['Duogames']

    print(p1maxwinname)
    print(p2maxwinname)
    print(p1maxwingames)
    print(p2maxwingames)                               
    print(maxwinpercentp1)
    print(maxwinpercentp2)



    

if __name__ == "__main__":
    main()
