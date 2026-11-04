def read_sql_file(file_path):
    with open(file_path,"r") as file:
        content=file.read()
        return content

if __name__=="__main__":
    sql_text= read_sql_file("data/test.sql")
    print("--Loaded SQL--")
    print(sql_text)