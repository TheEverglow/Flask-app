import random

def dict_creation(names, data):
    return {x:y for x,y in zip(names.split('\t'), data.split('\t'))}

def search_by_id(movie_id, data):

    int_movie_id = int(movie_id[2:])

    if (int_movie_id < len(data) and int_movie_id > 0):
        
        while(int_movie_id > 0):
            data_id = data[int_movie_id].split('\t')[0]

            if data_id == movie_id:
                return dict_creation(data[0], data[int_movie_id])

            int_movie_id -= 1

    return None

def search_by_title(title, data):
    answer = []
    
    for row in data:
        if(row.split('\t')[2] == title):
            answer.append(dict_creation(data[0], row))

    return answer

def search_by_year(year, data):
    answer = []

    if (len(str(year)) != 4):
        return []
    
    for row in data:
        if row.split('\t')[5] == str(year):
            answer.append(dict_creation(data[0], row))

    return answer

cache = []
def generate_random(data, q):
    while(True):
        i = random.randint(0, len(data) - 1)
        movie_id = data[i].split('\t')[0]

        if(movie_id not in q['likes'].keys() and movie_id not in cache):
            cache.append(movie_id)
            return movie_id, random.random()


def recommendation(k, q, data):
    answer = {}

    while(len(answer) <= k):
        temp = generate_random(data, q)
        answer[temp[0]] = temp[1]

    cache.clear()

    return answer



       