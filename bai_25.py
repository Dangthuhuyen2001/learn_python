"""Viết chương trình tính tần suất các từ từ input. Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái."""
freq = {} # frequency of words in text
line = input()
for word in line.split():
     freq[word] = freq.get(word,0)+1

words = sorted(freq.keys())
for w in words:
     print ("%s:%d" % (w,freq[w]))
print(freq)