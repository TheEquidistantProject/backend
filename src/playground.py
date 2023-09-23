import redis
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

r = redis.Redis(host='localhost', port=6379, db=0)

schema = (
    TextField("$.sources", as_name="sources"),
    TextField("$.tags", as_name="tags"),
    TextField("$.id", as_name="id"),
    TextField("$.title", as_name="title"),
    TextField("$.image", as_name="image"),
    TextField("$.date", as_name="date"),
    TextField("$.body", as_name="body"),
    NumericField("$.popularity", as_name="popularity"),
)

rs = r.ft("i")
rs.create_index(schema, definition=IndexDefinition(prefix=[""]))

print(rs.search(Query("*")))
for key in r.keys():
    print(r.get(key))
