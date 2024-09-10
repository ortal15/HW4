# MAKE ALL OF THIS CONDITION FALSE

a = 0
b = 1
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 2
b = 4
c = 0
d = 0
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 4
c = 0
d = 7
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 2
c = 9
d = 0
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 8
c = 9
d = 0
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 7
b = 7
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 0
b = 3
c = 0
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 9
b = 8
c = 7
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 4
b = 9
c = 2
d = 2
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")
