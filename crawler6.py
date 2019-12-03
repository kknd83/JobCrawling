import simplejson as json

test_arr = {"1":90, "2":32, "3":65, "4":100, "5":78}

print(json.dumps(test_arr,sort_keys=True, indent=4*' '))