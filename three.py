def count_words(s):
    words=s.split()
    return len(words)

print(count_words("Hello world"))              # 2
print(count_words("This is a test sentence.")) # 5
print(count_words(""))                         # 0
print(count_words("   multiple   spaces   "))  # 2
