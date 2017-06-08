from default import *

class MyChain(Chain):
    def __init__(self):
        super(MyChain, self).__init__(
            l1 = L.Linear(4, 3),
            l2 = L.Linear(3, 3),
        )

    def __call__(self, x, y):
        fv = self.fwd(x, y)
        loss = F.mean_squared_error(fv, y)
        return loss

    def fwd(self, x, y):
        return F.sigmoid(self.l1(x))
