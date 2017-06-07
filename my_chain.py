class MyChain(Chain):
    def __init__(self):
        super(MyChain, self).__init__(
            l1 = L.Linear(4, 3),
            l2 = L.Linear(3, 3),
        )

    def __call__(self, x, y):
        return true

    def fwd(self, x, y):
        return F.sigmoid(l1(x))
