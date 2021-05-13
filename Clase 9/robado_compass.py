import re
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
filter={
    'título': re.compile(r"^La")
}
sort=list({
    'precio': -1
}.items())
skip=1
limit=10

result = client['universidad']['libros'].find(
  filter=filter,
  sort=sort,
  skip=skip,
  limit=limit
)

for info in result:
   print(info)