import redis
import rejson
import redisearch
from redisearch import TextField, TagField, NumericField, Query, IndexDefinition, IndexType

db_client = redis.Redis(host='localhost', port=6379, db=0)

schema = (
    TagField("$.sources", as_name="sources"),
    TagField("$.tags", as_name="tags"),
    TextField("$.id", as_name="id"),
    TextField("$.title", as_name="title"),
    TextField("$.image", as_name="image"),
    TextField("$.date", as_name="date"),
    TextField("$.body", as_name="body"),
    NumericField("$.popularity", as_name="popularity"),
)

rs = db_client.ft("idx:articles")
rs.create_index(schema, definition=IndexDefinition(
    prefix=["article:"], index_type=IndexType.JSON))
