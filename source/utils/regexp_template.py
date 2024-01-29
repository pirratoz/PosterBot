from re import search


class RegexpTemplate:
    request_moder_fullname = lambda string: search("(?<=fullname: )[\S ]+", string)[0]
    requet_moder_username = lambda string: search("(?<=username: )[\S ]+", string)[0]
