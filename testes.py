import requests
import pandas as pd 
import json
from search_builder import build_symbol_search_request, build_quoterequest, build_logoutbody,build_login_body, search_all_quotes


class safras_connect():
    def __init__(self ):
        self.HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.URL = "https://strfeedrt04.cma.com.br/execute"
        self.source_id = '100'
        self.user = "STRFEEDVCS01"  
        self.session_id = ''

    
    def login_init(self):
        login_body = build_login_body(self.user)
        login_res = requests.post(self.URL, headers=self.HEADERS, data=login_body)
        self.session_id = login_res.json()['sessionId'] 
        return None

    def logout_process(self):
        body_logout = build_logoutbody(session_id= self.session_id, user =self.user )
        res_logout = requests.post(self.URL, headers= self.HEADERS, data= body_logout)
        status_lougout = res_logout.json()
        print({'End of session': status_lougout['success']})
    
    
    def clean_list_of_symbols(self, dict_of_symbols):
       return [ {"sourceId":self.source_id,"symbol": k  } for k in dict_of_symbols.keys()]

    def get_snapshot_of_list(self, list_of_symbols):
        clean_list = self.clean_list_of_symbols(list_of_symbols)
        body_symbols_snapshot =build_quoterequest(session_id= self.session_id, symbol= clean_list)
        #Requisição dos snapshots 
        res_quotes = requests.post(self.URL, headers= self.HEADERS, data= body_symbols_snapshot)
        return res_quotes.json()
        
        



if __name__== '__main__':


    with open('symbols_market.json', 'r', encoding='utf8') as file:
        symbols = json.load( file )
    #Pegando dados de milho
    milho = [mk for mk in symbols if mk['market'] == 'MILHO'][0]

    sf_object = safras_connect()
    sf_object.login_init()

    json_to_clean = sf_object.get_snapshot_of_list(milho['symbols'])
    print(json_to_clean)

    sf_object.logout_process()