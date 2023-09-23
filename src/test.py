import redis
import json
import random
import datetime
from redis.commands.json.path import Path

db_client = redis.Redis(host='localhost', port=6379, db=0)


class metadata:
    def __init__(self, name="", sources="", tags="", date="", popularity=0, image=""):
        self.title = name
        self.sources = sources
        self.tags = tags
        self.date = date
        self.popularity = popularity
        self.image = image


class payload:
    def __init__(self, id=-1, metadata=metadata(), body=""):
        self.id = id
        self.metadata = metadata
        self.body = body

    def to_dict(self):
        d = self.metadata.__dict__
        d.update({"id": self.id, "body": self.body})
        return d


def gen_word(len):
    word = ""
    for _ in range(len):
        word += chr(random.randint(97, 122))
    return word


def gen_name():
    name = ""
    num_names = random.randint(1, 2)
    for _ in range(num_names):
        name_len = random.randint(3, 10)
        name += gen_word(name_len) + " "
    return name[:-1]


def choose_source():
    sources = ["CNN", "FOX", "MSNBC", "ABC", "BBC"]
    ret = set()
    num_sources = random.randint(1, len(sources))
    for _ in range(num_sources):
        ret.add(random.choice(sources))

    return list(ret)


def gen_tags():
    tags = []
    num_tags = random.randint(1, 9)
    for _ in range(num_tags):
        tag_len = random.randint(3, 10)
        tags.append(gen_word(tag_len))

    return tags


def gen_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def gen_body():
    num_paragraphs = random.randint(1, 7)
    paragraphs = []
    for _ in range(num_paragraphs):
        paragraph = ""
        num_sentences = random.randint(1, 5)
        for _ in range(num_sentences):
            sentence = ""
            num_words = random.randint(3, 10)
            for _ in range(num_words):
                word_len = random.randint(3, 10)
                sentence += gen_word(word_len) + " "
            paragraph += sentence[:-1] + ". "
        paragraphs.append(paragraph[:-1])

    return "\n\r".join(paragraphs)


def gen_payload(id):
    name = gen_name()
    source = ",".join(choose_source())
    tags = ",".join(gen_tags())
    date = gen_date()
    popularity = random.randint(0, 100)
    image = ""
    body = gen_body()
    return payload(id, metadata(name, source, tags, date, popularity, image), body).to_dict()


a = {
    "sources": "",
    "tags": "",
    "id": "",
    "title": "",
    "image": "",
    "date": "",
    "body": "",
    "popularity": 0
}

db_client.json().set("-1", Path.root_path(), a)

for i in range(1, 3):
    db_client.json().set(f"{i}", Path.root_path(), gen_payload(i))
    # print(gen_payload())
