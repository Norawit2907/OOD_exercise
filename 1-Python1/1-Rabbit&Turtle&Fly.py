print("*** Rabbit & Turtle ***")
d, vr, vt, vf= input("Enter Input : ").split()
d = int(d)
vr = int(vr)
vt = int(vt)
vf = int(vf)

vd = vt - vr
td = d / vd
ans = vf * td
format_ans = "{:.2f}".format(ans)
print(format_ans)