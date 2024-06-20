import pprint
from typing import Any, Dict, List


class DataExtract:
    def __init__(self, response: List[Dict[str, Any]]) -> None:
        self.response = response
        self.cards_lists = []
        self.lists_lists = []
        self.members_lists = []

    def data_cards_extract(self) -> List[Dict[str, Any]]:
        for i in self.response:
            if 'checkItems' in i['badges'] and 'checkItemsChecked' in i['badges']:
                missing_checks = i['badges']['checkItems'] - i['badges']['checkItemsChecked']
                
                data_cards_dict = {
                    'data_inicio': i.get('start'),
                    'data_termino': i.get('due'),
                    'id_checklist': i.get('idChecklists'),
                    'id_list': i.get('idList'),
                    'id_members': i.get('idMembers'),
                    'nome': i.get('name'),
                    'url': i.get('url'),
                    'checks_faltantes': missing_checks
                }

                self.cards_lists.append(data_cards_dict)
        return self.cards_lists
    
    def data_lists_extract(self) -> List[Dict[str, str]]:
        for i in self.response:  
    
            data_lists_dict = {
                i.get('id') : i.get('name')
            }
            
            self.lists_lists.append(data_lists_dict)
        return self.lists_lists
    
    def data_members_extract(self) -> List[Dict[str, str]]:
        for i in self.response:
            data_members_dict = {
                i.get('id') : i.get('fullName')
            }

            self.members_lists.append(data_members_dict)
        return self.members_lists