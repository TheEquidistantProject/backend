import redis
import json
import random
import datetime

db_client = redis.Redis(host='localhost', port=6379, db=0)


class metadata:
    def __init__(self, name="", authors=[], tags=[], date="", popularity=0, image=""):
        self.name = name
        self.authors = authors
        self.tags = tags
        self.date = date
        self.popularity = popularity
        self.image = image


class payload:
    def __init__(self, metadata=metadata(), body=""):
        self.metadata = metadata
        self.body = body

    def to_dict(self):
        return {"metadata": self.metadata.__dict__, "body": self.body}


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


def choose_author():
    authors = ["CNN", "FOX", "MSNBC", "ABC", "BBC"]
    ret = set()
    num_authors = random.randint(1, len(authors))
    for _ in range(num_authors):
        ret.add(random.choice(authors))

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


def gen_payload():
    name = gen_name()
    author = choose_author()
    tags = gen_tags()
    date = gen_date()
    popularity = random.randint(0, 100)
    image = ""
    body = gen_body()
    return payload(metadata(name, author, tags, date, popularity, image), body).to_dict()


for i in range(1, 31):
    db_client.set(i, json.dumps(gen_payload()))
    print(gen_payload())
