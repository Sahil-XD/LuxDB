import json
from backend.parser.sql_parser import parse_sql

def read_sql_file(file_path : str):
    with open(file_path,"r") as file:
        content = file.read()
        return content

if __name__=="__main__":
    sql_text = read_sql_file("data/test.sql")
    result = parse_sql(sql_text)

    print("--Parsed Schema--")
    print(json.dumps(result,indent=2))