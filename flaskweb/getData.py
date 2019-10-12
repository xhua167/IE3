from flaskweb import db
import datetime

def meanRating(services):
    for j in services:
        length = len(j['Rating'])
        if length == 0:
            j['meanRating'] = 0
        else:
            sum1 = sum(j['Rating'])
            meanRating = sum1 / length
            meanRating = round(meanRating, 1)
            j['meanRating'] = meanRating
    services = sorted(services, key=lambda k: -(k.get('meanRating')))
    return services

def getServices(name):
    cursor = db.Services.find({'Type':name})
    services = []
    for i in cursor:
        if i['Type'] != 'hotlines':
            if i['What'] != 'Unknown' and i['Latitude'] != 'Unknown' and i['Longitude'] != 'Unknown':
                services.append(i)
        else:
            if i['What'] != 'Unknown':
                services.append(i)
    services = meanRating(services)
    return services

def getServicesPage(data, offset=0, per_page=10):
    return data[offset: offset + per_page]

def getInfo(name, id_):
    data = getServices(name)
    for i in data:
        if str(i.get('id_')) == id_:
            return i

def updateRating(name, id_, rating, email):
    alist = db.Services.find_one({'Type': name, 'id_': int(id_)}).get('Rating')
    ratingDic = db.user.find_one({'email': email}).get('rating')
    key = name + id_
    if key not in ratingDic.keys():
        ratingDic[key] = int(rating)
        alist.append(int(rating))
    else:
        oldrating = int(ratingDic[key])
        ratingDic[key] = int(rating)
        alist.remove(oldrating)
        alist.append(int(rating))
    db.Services.update_one(
        {'Type': name, 'id_': int(id_)},
        {'$set': {
            'Rating': alist
        }}
    )
    db.user.update_one(
        {'email': email},
        {'$set': {
            'rating': ratingDic
        }}
    )
    return 'success'

def updateFavorite(email, service_name, service_id):
    alist = db.user.find_one({'email': email}).get('favorite')
    service = {'Type': service_name, 'id_': service_id}
    if service not in alist:
        alist.insert(0, service)
        db.user.update_one(
            {'email': email},
            {'$set': {
                'favorite': alist
            }}
        )
        return 'success'
    else:
        return 'fail'

def remFavorite(email, service_name, service_id):
    alist = db.user.find_one({'email': email}).get('favorite')
    service = {'Type': service_name, 'id_': service_id}
    if service in alist:
        alist.remove(service)
        db.user.update_one(
            {'email': email},
            {'$set': {
                'favorite': alist
            }}
        )
        return 'success'
    else:
        return 'fail'


def getFavorite(email):
    alist = db.user.find_one({'email': email}).get('favorite')
    favoData = []
    for i in alist:
        favoData.append(getInfo(i['Type'], i['id_']))
    return favoData


def pass_today():
    dic = {'0':'Monday', '1':'Tuesday', '2':'Wednesday', '3':'Thursday',
           '4':'Friday', '5':'Saturday', '6':'Sunday'}
    day = datetime.datetime.today().weekday()
    return dic[str(day)]
