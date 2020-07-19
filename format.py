path_w = 'test_w.txt'
path_eng = 'english.txt'
path_jpn = 'japanese.txt'
s = ''
eng_s = []
jpn_s = []

# txtファイルの読み込み
with open(path_eng) as f:
  eng_s = [s.strip() for s in f.readlines()]

with open(path_jpn) as f:
  jpn_s = [s.strip() for s in f.readlines()]

print(len(eng_s))
print(len(jpn_s))

if len(eng_s) == len(jpn_s):
  for i in range(len(eng_s)):
    s = s + "{}. {}\n\t- =={}==\n".format((i+1),eng_s[i],jpn_s[i])
else:
  print("英語と日本語の行数が正しくありません！")

print(s)

# ファイルへの書き込み
with open(path_w, mode='w') as f:
    f.write(s)

with open(path_w) as f:
    print(f.read())