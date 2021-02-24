s = 'abcdefg'
k = 2
print(s[0:2:-1])
def reverseStr(s, k) :
    n = len(s)
    if n <= k:
        return s[::-1]
    elif n > k and n < 2 * k:
        return s[0:k:-1] + s[k:n]
    else:
        return s[0:k:-1] + s[k:2 * k] + reverseStr(s[2 * k:], k)

print(reverseStr(s, k))