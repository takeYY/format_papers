path_w = 'plus_n.txt'
path_r = 'not_n.txt'

s = ''
result = ''
# txtファイルの読み込み
with open(path_r) as f:
  s = f.read()

s_list = s.split(".")
for string in s_list:
  while (string.startswith(" ")):
    string = string[1:len(string)]
  string = string.replace("- ", "")
  if string == "":
    break
  result = result + "{}.\n".format(string)

print(result)

# ファイルへの書き込み
with open(path_w, mode='w') as f:
  f.write(result)

with open(path_w) as f:
  print(f.read())
