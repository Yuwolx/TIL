import csv

# with open('data.csv', 'w', newline='', encoding='utf-8') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['name','age','occupation'])
#     csv_writer.writerow(['name_1','age_1','occupation_1'])
#     csv_writer.writerow(['name_2','age_2','occupation_2'])
#     csv_writer.writerow(['name_3','age_3','occupation_3'])
# #passing line is defaulted 

with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['name','age','occupation']
    csv_write = csv.DictWriter(file, fieldnames)
    csv_write.writeheader()
    csv_write.writerow({'name':'dd','age':'dd','occupation':'dd'})
    csv_write.writerow({'name':'dd','age':'dd','occupation':'dd'})