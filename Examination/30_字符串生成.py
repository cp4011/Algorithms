# 通过
def solve(s):
    stack = []
    def func(s, stack):
        if not s:
            return ""
        a = list(s)
        n = len(s)
        ans = ""
        for i in range(n):
            if s[i] == "%":
                stack.append(i)
            elif s[i] == "#":
                if stack:
                    k = stack.pop()
                    ans += s[k + 1:i] * int(s[k - 1])
                    return ''.join(a[:k-1] + [ans] + a[i+1:])
    while "#" in s:
        s = func(s, stack)
    return s

s = input()
print(solve(s))


"""3%acm#2%acm#
acmacmacmacmacm"""