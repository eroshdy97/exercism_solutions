def transform(legacy_data :dict):
    ans = dict()

    for key in legacy_data:
        for value in legacy_data[key]:
            ans[value.lower()] = key

    return ans
