from api import fetchLibraryData

raw_data = fetchLibraryData()
# print(type(raw_data))
print(raw_data["docs"][0]["author_name"])
print(raw_data["docs"][0]["title"])