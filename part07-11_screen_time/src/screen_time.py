from datetime import datetime, timedelta

file = input("Filename:")
start_dt = input("Starting date:")
hmd = int(input("How many days:"))
date_catch = datetime.strptime(start_dt, "%d.%m.%Y")
date_1 = date_catch.strftime("%d.%m.%Y")
end_date = date_catch + timedelta(days = hmd - 1)
date_2 = end_date.strftime("%d.%m.%Y")

with open(file, "w") as filing:
    dt = {}
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    ttm = 0
    for index in range(hmd):
        what_days = date_catch + timedelta(days=index)
        d = what_days.strftime("%d.%m.%Y")
        screen = input(f"Screen time {d}:")
        spliter = screen.split(" ")
        for num in spliter:
            ttm += int(num)
        dt[d] = spliter
    avg = ttm / hmd
    filing.write(f"Time period: {date_1}-{date_2} \n")
    filing.write(f"Total minutes: {ttm} \n")
    filing.write(f"Average minutes: {avg} \n")

    collection = []
    for index, name in dt.items():
            data = []
            data.append(index)
            data.extend(name)
            collection.append(data)

    for index in collection:
        line = f"{index[0]}: "
        for content in index:
            if index[0] not in content:
                line += f"{content}/"
        line = line[:-1]
        filing.write(line + "\n")
    
    print(f"Data stored in file {file}")
