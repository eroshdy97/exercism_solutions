def tally(rows):
    res = ["Team                           | MP |  W |  D |  L |  P"]
    data_dict = dict()
    for item in rows:
        match_info = item.split(";")
        if(match_info[0] not in data_dict):
            data_dict[match_info[0]] = [0, 0, 0, 0, 0]
        if(match_info[1] not in data_dict):
            data_dict[match_info[1]] = [0, 0, 0, 0, 0]

        # Reading

        if match_info[2] == "win":
            temp = data_dict[match_info[0]] # Win
            temp[0] += 1    # MP
            temp[1] += 1    # W
            temp[2] += 0    # D
            temp[3] += 0    # L
            temp[4] += 3    # P
            data_dict[match_info[0]] = temp
            temp = data_dict[match_info[1]] # Loss
            temp[0] += 1    # MP
            temp[1] += 0    # W
            temp[2] += 0    # D
            temp[3] += 1    # L
            temp[4] += 0    # P
            data_dict[match_info[1]] = temp

        elif match_info[2] == "loss":
            temp = data_dict[match_info[1]] # Win
            temp[0] += 1    # MP
            temp[1] += 1    # W
            temp[2] += 0    # D
            temp[3] += 0    # L
            temp[4] += 3    # P
            data_dict[match_info[1]] = temp
            temp = data_dict[match_info[0]] # Loss
            temp[0] += 1    # MP
            temp[1] += 0    # W
            temp[2] += 0    # D
            temp[3] += 1    # L
            temp[4] += 0    # P
            data_dict[match_info[0]] = temp

        elif match_info[2] == "draw":
            temp = data_dict[match_info[1]] # Draw
            temp[0] += 1    # MP
            temp[1] += 0    # W
            temp[2] += 1    # D
            temp[3] += 0    # L
            temp[4] += 1    # P
            data_dict[match_info[1]] = temp
            temp = data_dict[match_info[0]] # Draw
            temp[0] += 1    # MP
            temp[1] += 0    # W
            temp[2] += 1    # D
            temp[3] += 0    # L
            temp[4] += 1    # P
            data_dict[match_info[0]] = temp

    sorted_list = sorted(data_dict.items(), key=lambda item: (-item[1][4], item[0]))
    #sorted_list.reverse()
    #sorted_list = dict(sorted_list)

    # Formatting

    for key in sorted_list:
        name = key[0]
        data = key[1]
        txt = name + (31 - len(name)) * " "
        txt += "|" + (3 - len(str(data[0]))) * " " + str(data[0]) + " " # MP
        txt += "|" + (3 - len(str(data[1]))) * " " + str(data[1]) + " " # W
        txt += "|" + (3 - len(str(data[2]))) * " " + str(data[2]) + " " # D
        txt += "|" + (3 - len(str(data[3]))) * " " + str(data[3]) + " " # L
        txt += "|" + (3 - len(str(data[4]))) * " " + str(data[4]) # P

        res.append(txt)
    return res
