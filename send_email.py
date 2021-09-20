import json
from datetime import datetime
from csv import writer
import sys
import pandas as pd

## python send_email.py "path to template.json" "path to customer.csv"
## "path to output email" "path to error.csv"

# #print(str(sys.argv))
# template_dir = "email_template.json"
# cus_dir = "customers.csv"
# dir_succ = "output_emails/"
# dir_err = "error.csv"

template_dir = argv[1]
cus_dir = argv[2]
dir_succ = argv[3]
dir_err = argv[4]

df = pd.read_csv(cus_dir)
#fill tất cả chỗ trống trong file csv thành "none"
df = df.fillna("none")

list_title = df['TITLE'].tolist()
list_fname = df['FIRST_NAME'].tolist()
list_lname = df['LAST_NAME'].tolist()
list_email = df['EMAIL'].tolist()
#print(list_email)


row, column = df.shape
#print("Number of rows and column ", row , column)

with open(template_dir) as f:
  template = json.load(f)
#print(template["from"])

today_time = datetime.today().strftime('%d %b %Y')


list_err = []
list_succ = []
for i in range(row):
  if(list_email[i] == "none"):
    err = [list_title[i], list_fname[i], list_lname[i]]
    list_err.append(err)
  else:
    new_body = template["body"]
    new_body = new_body.replace("{{TODAY}}", today_time)
    new_body = new_body.replace("{{TITLE}}", list_title[i])
    new_body = new_body.replace("{{FIRST_NAME}}", list_fname[i] )
    new_body = new_body.replace("{{LAST_NAME}}", list_lname[i] )

    new_email = dict()
    new_email["from"] = template["from"]
    new_email["to"] = list_email[i]
    new_email["subject"] = template["subject"]
    new_email["mimeType"] = template["mimeType"]
    new_email["body"] = new_body
    #print(new_email)
    list_succ.append(new_email)

# print(list_err)
# print(list_succ)


# lưu các khách hàng lỗi vào file error.csv
with open(dir_err, 'a') as f_object:
    writer_object = writer(f_object)
    for i in range(len(list_err)):
      writer_object.writerow(list_err[i])
    f_object.close()

# lưu các mẫu tin nhắn thành công vào thư mục output_email
for i in range(len(list_succ)):
  with open(dir_succ + str(i) + ".json", "w") as f:
    json.dump(list_succ[i],f)

print("Completed! please check your output file...")

