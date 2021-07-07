import re
input_filename = "text.txt"
result_filename ="../result.txt"


inputfile = open(filename, 'r')
resultfile = open(result_filename, 'w')
mytext = inputfile.read()
lookfor = r"[a-zA-Z/d]"
company_name = re.search(r'ДУБЛИКАТ\n(.*)\n', text).group(1)
bin_num = re.search(r'БИН (\d+)', text).group(1)
items = re.findall(r'\d+\.\n([^\n]+)\n([0-9, ]+) x ([0-9, ]+)\n([0-9, ]+)', text)
date = re.search(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}', text).group()
address = re.search(r'г\.[^\n]+', text).group()
total_price = re.search(r'ИТОГО:\n([0-9, ]+)', text).group(1)
print(f'Название компании: {company_name}\nНомер BIN: {bin_num}\nДата: {date}\nАдрес: {address}\n')

results = re.findall(lookfor, mytext)
for item in results:
    print(item)