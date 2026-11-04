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

if __name__=="__main__":
    sql_text= read_sql_file("data/test.sql")
    table= extract_table_name(sql_text)
    print(f"Detected tables : {table} ")