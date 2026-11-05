from turtledemo.chaos import line

def read_sql_file(file_path):
    with open(file_path,"r") as file:
        content=file.read()
        return content

def parse_sql(sql_text: str):
    schema = { "table": {}, "relationships": []}
    current_table = None

    for line in sql_text.split("\n"):
        clean = line.strip().rstrip(",")
        upper_line = clean.upper()

        if upper_line.startswith("CREATE TABLE"):
            current_table=clean.split()[2].split("(")[0].strip()
            schema["table"][current_table]=[]

        elif upper_line.startswith(");"):
            current_table=None

        elif current_table and clean:
            words = clean.split()
            col_name = words[0]
            col_type = words[1]
            is_pk = "PRIMARY KEY" in upper_line

            if "REFERENCES" in upper_line:
                words_upper = upper_line.split()
                ref_index = words_upper.index("REFERENCES")
                target_table = (words[ref_index+1].split("("))[0]
                schema["relationships"].append({"from": current_table, "to": target_table})

            schema["table"][current_table].append({"name": col_name, "type": col_type, "is_pk": is_pk})

    return schema


if __name__=="__main__":
    sql_text= read_sql_file("data/test.sql")
    result = parse_sql(sql_text)

    print("---Parsed Schema---")
    print(result)