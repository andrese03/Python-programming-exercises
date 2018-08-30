# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

raw = input('Write a number: ')

a = int('%s' % (raw))
aa = int('%s%s' % (raw, raw))
aaa = int('%s%s%s' % (raw, raw, raw))
aaaa = int('%s%s%s%s' % (raw, raw, raw, raw))

print(a + aa + aaa + aaaa)