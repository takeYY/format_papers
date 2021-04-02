path_w = 'text/plus_n.txt'
path_r = 'text/not_n.txt'

s_l = []
s = ''
result = ''
# txtファイルの読み込み
with open(path_r) as f:
  s_l = [s.strip() for s in f.readlines()]

# 改行をスペースでjoin
s = ' '.join(s_l)

s_list = s.split('. ')

for idx, string in enumerate(s_list):
  while (string.startswith(' ')):
    string = string[1:len(string)]
  string = string.replace('- ', '')
  if idx + 1 == len(s_list):
    result += f"{string}\n"
    break
  result += f"{string}.\n"

# ファイルへの書き込み
with open(path_w, mode='w') as f:
  f.write(result)

with open(path_w) as f:
  print(f.read())
