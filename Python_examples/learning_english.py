import re
import pymongo


def main():
    file = "1x08.srt"
    f = open(
        file,
        'r')
    # s = f.readline()
    # print(s)
    client = pymongo.MongoClient()
    db = client['english']
    for line in f:
        if line.isspace():
            continue
        if line.endswith("\n"):
            line = line[:-1]
        if line.startswith("00") or line.startswith("<"):
            continue
        # line.strip()
        if line.isdigit():
            continue
        lis = re.findall(r"[\w']+", line)
        for word in lis:
            cursor = db.words.find_one({"word": word})
            if cursor is not None:
                cursor_word = db.words.update_one(
                    {"word": word},
                    {"$inc": {"count": +1}}
                )
                print(1)
            else:
                cursor_word = db.words.insert_one({
                    "word": word,
                    "count": 1,
                    "relevance": 1
                })
                print(2)

    f.close()


def get_words():
    client = pymongo.MongoClient()
    db = client['english']
    words = db.words.find().sort([
        ("count", pymongo.DESCENDING)
    ])
    my_file = open("1x08.txt", "w")
    i = 0
    start_spaces = 4
    for word in words:
        print(word["word"] + " " + str(word["count"]))
        number_of_spaces = 20 - len(word["word"])
        i += 1
        if i < 10:
            start_spaces = 4
        if 9 < i < 99:
            start_spaces = 3
        if 99 < i < 999:
            start_spaces = 2
        if 999 < i < 9999:
            start_spaces = 1


        my_file.write(str(i) + start_spaces * " " + word["word"] + number_of_spaces * " " + str(word["count"]) + "\n")


if __name__ == "__main__":
    # main()
    get_words()
