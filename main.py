from src.data_extract import DataExtract
from src.http_requester import CardsApi, ListsApi, MembersApi

if __name__ == "__main__":
    cards_api = CardsApi()
    response_cards_api = cards_api.http_response()
    data_cards = DataExtract(response_cards_api)
    cards_list = data_cards.data_cards_extract()

    lists_api = ListsApi()
    response_lists_api = lists_api.http_response()
    data_list = DataExtract(response_lists_api)
    lists_list =  data_list.data_lists_extract()

    members_api = MembersApi()
    response_members_api = members_api.http_response()
    data_members = DataExtract(response_members_api)
    members_list = data_members.data_members_extract()

