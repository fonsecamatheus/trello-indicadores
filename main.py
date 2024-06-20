from src.data_extract import DataExtract
from src.http_requester import CardsApi, ListsApi, MembersApi
from src.data_transform import DataTransform

if __name__ == "__main__":
    cards_api = CardsApi()
    response_cards_api = cards_api.http_response()
    data_cards = DataExtract(response_cards_api)
    cards_list = data_cards.data_cards_extract()
    transform_cards = DataTransform(cards_list)
    df_cards = transform_cards.data_cards_transform()

    lists_api = ListsApi()
    response_lists_api = lists_api.http_response()
    data_list = DataExtract(response_lists_api)
    lists_list =  data_list.data_lists_extract()
    transform_lists = DataTransform(lists_list)
    df_lists = transform_lists.data_lists_tranform()

    members_api = MembersApi()
    response_members_api = members_api.http_response()
    data_members = DataExtract(response_members_api)
    members_list = data_members.data_members_extract()
    transform_members = DataTransform(members_list)
    df_members = transform_members.data_members_tranform()

    print(df_cards)
    print(df_lists)
    print(df_members)

