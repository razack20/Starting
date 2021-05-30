import json
dict1 ={"emp1": {"name": "Lisa","designation": "programmer","age": "34","salary": "54000"}}

out_file = open("myfile.json", "w")

json.dump(dict1, out_file, indent=6)

out_file.close()
