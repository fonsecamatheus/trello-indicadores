from src.data_extract import DataExtract
from src.http_requester import CardsApi, ListsApi, MembersApi

if __name__ == "__main__":
    members_api = MembersApi()
    response = members_api.http_response()
    data_members = DataExtract(response)
    members_lists = data_members.data_members_extract()
    print(members_lists)