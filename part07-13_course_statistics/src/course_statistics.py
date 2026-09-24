def retrieve_all():
    import json
    import urllib.request


    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    profile = json.loads(data)
    data_crs = []
    for index in profile:
        if index["enabled"] != False:
            collect = (index["fullName"],index['name'],index["year"], sum(index["exercises"]))
            data_crs.append(collect)
    
    return data_crs

def retrieve_course(course_name: str):
    import json
    import urllib.request

    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = my_request.read()
    profile = json.loads(data)

    weeks = 0
    students_num = 0
    hours = 0
    exercises = 0

    for index,content in profile.items():
        students_num = max(students_num, content["students"])
        weeks += 1
        hours += content["hour_total"]
        exercises += content["exercise_total"]
    
    hours_avg = hours/students_num
    exercises_average = exercises / students_num

    summary_data = {
        'weeks':(weeks), 
        'students':(students_num), 
        'hours':(hours), 
        'hours_average':(int(hours_avg)), 
        'exercises':(exercises),
        'exercises_average':(int(exercises_average))
        }

    return summary_data