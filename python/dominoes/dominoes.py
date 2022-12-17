def can_chain(dominoes :list):
    if dominoes == []:
        return dominoes

    if len(dominoes) == 1:
        if dominoes[0][0] == dominoes[0][1]:
            return dominoes
        else:
            return None
            
    temp = dominoes
    listed = []
    listed.append(temp.pop())
    while temp:
        found :bool = False
        item = listed[-1]
        if (item[1], item[1]) in temp:
            listed.append((item[1], item[1]))
            temp.remove((item[1], item[1]))
            found = True
            continue
        for nxt in temp:       
            if item[1] == nxt[0]:
                listed.append(nxt)
                temp.remove(nxt)
                found = True
                break
            elif item[1] == nxt[1]:
                listed.append((nxt[1], nxt[0]))
                temp.remove(nxt)
                found = True
                break
        
        if not found:
            all_listed = [ele for tup in listed for ele in tup]
            all_temp = [ele for tup in temp for ele in tup]
            bond = [x for x in all_temp if x in all_listed]
            if can_chain(temp) != None and bond:
                return dominoes
            listed = []
            return None

    if listed[0][0] == listed[-1][1]:
        return dominoes

    else:
        return None
