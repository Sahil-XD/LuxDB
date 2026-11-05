def read_sql_file(file_path):
    with open(file_path,"r") as file:
        content=file.read()
        return content

def extract_table_name(sql_text):
    for line in sql_text.split("\n"):
        clean=line.strip()

        if clean.upper().startswith("CREATE TABLE"):
            parts=clean.split()
            table_name=parts[2].strip("(")
            return table_name
    return None

def extract_columns(sql_text: str):
    columns=[]

    for line in sql_text.split("\n"):

        clean=line.strip().rstrip(",")
        upper_line=clean.upper()

        if upper_line.startswith("CREATE TABLE") or upper_line.startswith(");") or not clean:
            continue

        words=clean.split()
        col_name=words[0]
        col_type=words[1]
        is_pk= "PRIMARY KEY" in upper_line

        columns.append({"name":col_name, "type": col_type, "is_pk": is_pk})
    return columns

if __name__=="__main__":
    sql_text= read_sql_file("data/test.sql")
    table = extract_table_name(sql_text)
    cols = extract_columns(sql_text)
    print(f"Table : {table} ")
    print(f"Columns : {cols}")