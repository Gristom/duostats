import requests
from app import RiotConsts as Consts
import sys, time





class RiotAPI(object):



    def __init__(self, api_key, region):
        self.api_key = api_key 
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
                ),
            params=args
            )

        print(response.url)
        print("")
        #print(response.headers)
        #print("")
        
        
        #treat it like a dict

        try:        

            apprate1 = response.headers['X-App-Rate-Limit-Count'].replace(':', ',')
            allowedapprate1 = response.headers['X-App-Rate-Limit'].replace(':', ',')

            methodrate = response.headers['X-Method-Rate-Limit-Count'].replace(':', ',')
            allowedmethodrate = response.headers['X-Method-Rate-Limit'].replace(':', ',')

            apprate1 = apprate1.split(',')
            allowedapprate1 = allowedapprate1.split(',')

            methodrate = methodrate.split(',')
            allowedmethodrate = allowedmethodrate.split(',')

        except KeyError:

            time.sleep(5)
            print(response.headers)
            return response.json()

        
        alimitcount = []
        alimitallowed = []
        alimitsecs = []

        mlimitcount = []
        mlimitallowed = []
        mlimitsecs = []


        #print(apprate1)
        #print(allowedapprate1)
        #print("")
        #print(methodrate)
        #print(allowedmethodrate)
        #print("")
        #print("")
        #print("")
        #print(range(int(len(apprate1))//2))

        i = 0
        z = 0
     

        while i < (len(apprate1)):
            
            #print(i)
            alimitcount.append(int(apprate1[i]))
            alimitallowed.append(int(allowedapprate1[i]-10))
            alimitsecs.append(int(apprate1[i+1]))
            i = i+2

        while z < (len(methodrate)):

            #print(z)
            mlimitcount.append(int(methodrate[z]))
            mlimitallowed.append(int(allowedmethodrate[z]-10))
            mlimitsecs.append(int(methodrate[z+1]))
            z = z+2

        #print(alimitcount)
        #print(alimitallowed)
        #print(alimitsecs)
        #print("")
        #print(mlimitcount)
        #print(mlimitallowed)
        #print(mlimitsecs)

            

##        
##        alimitcount = int(apprate1[0])
##        alimitallowed = int(allowedapprate1[0])
##        alimitsecs = int(apprate1[2])
##        
##        alimit2count = int(apprate[1])
##        alimit2allowed = int(allowedapprate[1])
##        alimit2secs = int(apprate1[2])
##        
##        mlimitcount = int(methodrate[0])
##        mlimitallowed = int(allowedmethodrate[0])
##        mlimitsecs = int(allowedmethodrate[2])
##
##        
        








        #make wait = header wait time required


        for _ in range(3):

            for i in range(len(alimitcount)):
                
                if alimitcount[i] < alimitallowed[i]:
                    try:
                        print(range(len(alimitcount)))
                        print("Success stage " + str(i))
                        print(alimitcount[i])
                        print(alimitallowed[i])
                        
                    
                    except Exception:
                        typ, val, tb = sys.exc_info()
                        logger.error(traceback.format_exception(typ, val, tb))
                        time.sleep(5)
##                    except:
                        #raise

                elif alimitcount[i] >= alimitallowed[i]:
                    
                    print(alimitcount[i])
                    print("Greater than or equal to:")
                    print(alimitallowed[i])
                    print("app limit count exceeded")
                    print(alimitcount[i])
                    print(alimitallowed[i])
                    print("")

                    print("waiting " + str(alimitsecs[i]))
                    time.sleep(alimitsecs[i])

                    args = {'api_key': self.api_key}
                    for key, value in params.items():
                        if key not in args:
                            args[key] = value
                    response = requests.get(
                        Consts.URL['base'].format(
                            proxy=self.region,
                            region=self.region,
                            url=api_url
                            ),
                        params=args
                        )


                    apprate1 = response.headers['X-App-Rate-Limit-Count'].replace(':', ',')
                    allowedapprate1 = response.headers['X-App-Rate-Limit'].replace(':', ',')

                    methodrate = response.headers['X-Method-Rate-Limit-Count'].replace(':', ',')
                    allowedmethodrate = response.headers['X-Method-Rate-Limit'].replace(':', ',')

                    apprate1 = apprate1.split(',')
                    allowedapprate1 = allowedapprate1.split(',')

                    methodrate = methodrate.split(',')
                    allowedmethodrate = allowedmethodrate.split(',')

                    
                    alimitcount = []
                    alimitallowed = []
                    alimitsecs = []

                    mlimitcount = []
                    mlimitallowed = []
                    mlimitsecs = []

                    i = 0
                    z = 0
                 

                    while i < (len(apprate1)):
                        
                        print(i)
                        alimitcount.append(int(apprate1[i]))
                        alimitallowed.append(int(allowedapprate1[i]))
                        alimitsecs.append(int(apprate1[i+1]))
                        i = i+2

                    while z < (len(methodrate)):

                        mlimitcount.append(int(methodrate[z]))
                        mlimitallowed.append(int(allowedmethodrate[z]))
                        mlimitsecs.append(int(methodrate[z+1]))
                        z = z+2

                        print(alimitcount)
                        print(alimitallowed)
                        print(alimitsecs)
                        print("")
                        print(mlimitcount)
                        print(mlimitallowed)
                        print(mlimitsecs)

                else:

                    print("App limit failed")

        for _ in range(3):

            for i in range(len(mlimitcount)):


                if mlimitcount[i] < mlimitallowed[i]:
                    try:
                        print("Success stage " + str(i))
                        print(alimitcount[i])
                        print(alimitallowed[i])

                    except Exception:
                        typ, val, tb = sys.exc_info()
                        logger.error(traceback.format_exception(typ, val, tb))
                        time.sleep(5)                    
            
                elif mlimitcount[i] >= mlimitallowed[i]:

                    print("method limit exceeded " + str(i))

                    print(mlimitcount)
                    print(mlimitallowed)
                    print("waiting " + str(mlimitsecs[i]))
                    time.sleep(mlimitsecs[i])
                    args = {'api_key': self.api_key}
                    for key, value in params.items():
                        if key not in args:
                            args[key] = value
                    response = requests.get(
                        Consts.URL['base'].format(
                            proxy=self.region,
                            region=self.region,
                            url=api_url
                            ),
                        params=args
                        )


                    apprate1 = response.headers['X-App-Rate-Limit-Count'].replace(':', ',')
                    allowedapprate1 = response.headers['X-App-Rate-Limit'].replace(':', ',')

                    methodrate = response.headers['X-Method-Rate-Limit-Count'].replace(':', ',')
                    allowedmethodrate = response.headers['X-Method-Rate-Limit'].replace(':', ',')

                    apprate1 = apprate1.split(',')
                    allowedapprate1 = allowedapprate1.split(',')

                    methodrate = methodrate.split(',')
                    allowedmethodrate = allowedmethodrate.split(',')

                    
                    alimitcount = []
                    alimitallowed = []
                    alimitsecs = []

                    mlimitcount = []
                    mlimitallowed = []
                    mlimitsecs = []

                    i = 0
                    z = 0
                 

                    while i < (len(apprate1)):
                        
                        print(i)
                        alimitcount.append(int(apprate1[i]))
                        alimitallowed.append(int(allowedapprate1[i]))
                        alimitsecs.append(int(apprate1[i+1]))
                        i = i+2

                    while z < (len(methodrate)):

                        mlimitcount.append(int(methodrate[z]))
                        mlimitallowed.append(int(allowedmethodrate[z]))
                        mlimitsecs.append(int(methodrate[z+1]))
                        z = z+2

                        print(alimitcount)
                        print(alimitallowed)
                        print(alimitsecs)
                        print("")
                        print(mlimitcount)
                        print(mlimitallowed)
                        print(mlimitsecs)


                else:

                    print("Method limit failed, This is bad?")


        return response.json()


##        class RetryError(Exception):
##            pass
##
##        def fancyretryloop(attempts, timeout=None, delay=0, backoff=1):
##            starttime = time.time()
##            success = set()
##            for i in range(attempts): 
##                success.add(True)
##                yield success.clear
##                if success:
##                    return response.json()
##                    break
##                duration = time.time() - starttime
##                if timeout is not None and duration > timeout:
##                    break
##                if delay:
##                    time.sleep(delay)
##                    delay = delay * backoff
##
##            e = sys.exc_info()[1]
##
##            # No pending exception? Make one
##            if e is None:
##                try: raise RetryError
##                except RetryError as e: pass
##
##
##            # Decorate exception with retry information:
##            e.args = e.args + ("on attempt {0} of {1} after {2:.3f} seconds".format(i, attempts + 1, duration),)
##
##            raise
##
##
##
##
##        for retry in fancyretryloop(10, timeout=30):
##            print("Something?")
##            if apprate[0] != allowedapprate[0] and apprate[1] != allowedapprate[1] and methodrate != allowedmethodrate:
##                retry()


##        starttime = time.time()
##        success = set()
##        for i in range(attempts):
##            if apprate[0] == allowedapprate[0] or apprate[1] == allowedapprate[1] or methodrate == allowedmethodrate:
##                print("Limit Reached, retrying...")
##                
##            else:
##                
##                success.add(True)
##            yield success.clear
##            if success:
##                return response.json()
##            duration = time.time() - starttime
##            if timeout is not None and duration > timeout:
##                break
##            if delay:
##                time.sleep(delay)
##                delay = delay * backoff
##
##        e = sys.exc_info()[1]
##
##        # No pending exception? Make one
##        if e is None:
##            try: raise RetryError
##            except RetryError as e: pass
##
##        # Decorate exception with retry information:
##        e.args = e.args + ("on attempt {0} of {1} after {2:.3f} seconds".format(i, attempts + 1, duration),)
##
##        raise

    

       
        
    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name
            )
        return self._request(api_url)


    def get_ranked_stats(self, summonerId):
        api_url = Consts.URL['ranked_stats'].format(
            version=Consts.API_VERSIONS['stats'],
            summonerIds=summonerId
            )
        return self._request(api_url)

    def get_match_history(self, summonerId, beginIndex):
        api_url = Consts.URL['match_history'].format(
            version=Consts.API_VERSIONS['matchlist'],
            summonerIds=summonerId,
            beginIndexs=beginIndex
            )
        return self._request(api_url)

    def get_match_info(self, matchId):
        api_url = Consts.URL['match_info'].format(
            version=Consts.API_VERSIONS['match'],
            matchIds=matchId
            )
        return self._request(api_url)

    def get_champ_list(self):
        api_url = Consts.URL['champ_list'].format(
            version=Consts.API_VERSIONS['match']
            )
        return self._request(api_url)
