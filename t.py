from app.misc.public import login_required_by_role


@login_required_by_role(role=1)
def ff(a, b, c):
    print(a)
    print(b)
    print(c)



ff(1,'2',3)
