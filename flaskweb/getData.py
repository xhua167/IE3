from flaskweb import db
import datetime

# Method to calculate the mean rating,
# accept a list of services and return a list
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

# Method to get the services from the db based on types
# Accept the service type, return a list of services
def getServices(name):
    cursor = db.Services.find({'Type':name})
    services = []
    for i in cursor:
        # Use the services that contain description and coordinate
        if i['Type'] != 'hotlines':
            if i['What'] != 'Unknown' and i['Latitude'] != 'Unknown' and i['Longitude'] != 'Unknown':
                services.append(i)
        else:
            if i['What'] != 'Unknown':
                services.append(i)
    services = meanRating(services)
    return services

# Method to set the pagination
# Accept a list of data
def getServicesPage(data, offset=0, per_page=10):
    return data[offset: offset + per_page]

# Method to return a specific service with detailed information
# Accept the type and the id_
def getInfo(name, id_):
    data = getServices(name)
    for i in data:
        if str(i.get('id_')) == id_:
            return i

# Method to update the rating, each user can only give one rating to one service
# Accept the service type and id_, the rating(str) and user email
def updateRating(name, id_, rating, email):
    alist = db.Services.find_one({'Type': name, 'id_': int(id_)}).get('Rating')
    ratingDic = db.user.find_one({'email': email}).get('rating')
    key = name + id_

    # check whether the user has given a rating the this service,
    # If no, add the new rating. Else replace the previous rating
    if key not in ratingDic.keys():
        ratingDic[key] = int(rating)
        alist.append(int(rating))
    else:
        oldrating = int(ratingDic[key])
        ratingDic[key] = int(rating)
        alist.remove(oldrating)
        alist.append(int(rating))

    # Update both user and services db
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

# Method to add the user's favorite
# Accept user's email, the favorited service's type and id_
# Users' favorite store the type and the id_
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

# Method to remove the user's favorite
# Accept user's email, the favorited service's type and id_
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

# Method to get the detailed favorited service
# Accept user's email and return a list of services
def getFavorite(email):
    alist = db.user.find_one({'email': email}).get('favorite')
    favoData = []
    for i in alist:
        favoData.append(getInfo(i['Type'], i['id_']))
    return favoData

# Method to return the today's day
def pass_today():
    dic = {'0':'Monday', '1':'Tuesday', '2':'Wednesday', '3':'Thursday',
           '4':'Friday', '5':'Saturday', '6':'Sunday'}
    day = datetime.datetime.today().weekday()
    return dic[str(day)]

# Method to determine if there is a map in search display page
# Accept a list of services, return yes or no
def ifMap(data):
    map = 'yes'
    if len(data) == 1 and data[0]['Type'] == 'hotlines':
        map = 'no'
    else:
        typeList = []
        for i in data:
            typeList.append(i['Type'])
        if len(set(typeList)) == 1 and typeList[0] == 'hotlines':
            map = 'no'
        else:
            for i in data:
                if i['Type'] != 'hotlines':
                    temp = i
                    data.remove(i)
                    data.insert(0,temp)
                    break
    return map
