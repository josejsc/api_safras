import json

def build_login_body(user:str = "STRFEEDVCS01", password:str = ""):
      body = {"id":1,
              "oms": {"ip":"0.0.0.0",
                      "channel":"API",
                      "language":"PT"},
                "pass":password,
                "service":"m",
                "name":"LoginRequest",
                "sessionId":"",
                "transport":"Polling",
                "type":"s","sync":True,
                "version":1,
                "user":user}
      return {'JSONRequest': json.dumps(body)} 



def build_symbol_search_request(session_id:str,  symbol:str, source:int = 100):
    body =  {"id": 3,
            "name": "SymbolSearchRequest",
            "sessionId": session_id,
            "type": "q",
            "sync": True,
            "timeoutHandler": 120,
            "failActionType": "closeconnection",
            "source": source,
            "max": 100,
            "symbol": symbol,
            "description": "",
            "market": "",
            "page": 0,
            "match": False }

    return {'JSONRequest': json.dumps(body)} 


def build_quoterequest(session_id:str, symbol:list ):
   body = {"id": 3,
     "name":"QuotesRequest",
     "sessionId":session_id,
     "type":"n",
     "sync":True,
     "timeoutHandler":120,
     "failActionType":"alert",
     "fields":"",
     "realtime":True,
     "symbols":symbol,
     "sign":False}
   
   return {'JSONRequest': json.dumps(body)} 


def build_logoutbody( session_id:str,user:str, id = 1):
    body = {"id":id,
            "name":"LogoutAdvRequest",
            "sessionId":session_id,
            "type":"s",
            "sync":True,
            "version":1,
            "advUser":user,
            "reason":"texto"}
    return {'JSONRequest': json.dumps(body)} 


def search_all_quotes(session_id:str, id:int = 1, source:int = 100, symbol:str = 'WIN', max_n:int = 200 ):
        print('searching all quotes')

        
        body = {"id":id,
                "name":"SymbolSearchRequest",
                "sessionId":session_id,
                "type":"q","sync":True,"source":100,"max":max_n,"symbol":"","description":"","market":"V","page":0,"match":False}
        

        return {'JSONRequest': json.dumps(body)} 
    

