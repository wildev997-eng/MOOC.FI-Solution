def is_it_valid(pic: str):
    from datetime import datetime

    if len(pic) > 11:
        return False

    year = []
    cnt_mark = ""
    control_str = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    control_sum = []
    
    for index in range(len(pic)-1):
        if index < 6:
            year.append(pic[index])
            control_sum.append(pic[index])
        elif index < 7:
            cnt_mark = str(pic[index])
        elif index < 10:
            control_sum.append(pic[index])
    
    if cnt_mark not in "-+A":
        return False
    else:
        day = "".join(year[0:2])
        month = "".join(year[2:4])
        year = "".join(year[4:6])
        join_control = "".join(control_sum)
        z = int(join_control) % 31
        
        if control_str[z] != pic[-1]:
            return False
        else:
            try:
                if cnt_mark == "+":
                    usr_bday = datetime(1800 + int(year), int(month), int(day))
                    return True
                
                if cnt_mark == "-":
                    usr_bday = datetime(1900 + int(year), int(month), int(day))
                    return True
                
                if cnt_mark == "A":
                    usr_bday = datetime(2000 + int(year), int(month), int(day))
                    return True

            except ValueError:
                return False
