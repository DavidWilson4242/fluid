N = 128
DT = 0.10
ITER = 10

def IX(x, y):
  return x + y*N

def setBound(b, x):
  pass

def linearSolve(b, x, x0, a, c):
  cr = 1.0 / c
  for k in range(ITER):
    for j in range(1, N - 1):
      for i in range(1, N - 1):
        x[IX(i, j)] =                   \
          (x0[IX(i, j)] +               \
            a * (   x[IX(i + 1, j)]     \
                   +x[IX(i - 1, j)]     \
                   +x[IX(i,     j + 1)] \
                   +x[IX(i,     j - 1)] \
                )) * cr
    setBound(b, x)

def diffuse(b, x, x0, diff):
  a = DT * diff * (N - 2)**2
  linearSolve(b, x, x0, a, a*6 + 1, ITER, N)

# thanks to https://mikeash.com/pyblog/fluid-simulation-for-dummies.html
class Fluid:

  def __init__(self, diff, vesc):

    # diffusion, vescosity
    self.diff = diff
    self.vesc = vesc

    # current state
    self.vx  = [0] * N
    self.vy  = [0] * N
    self.den = [0] * N

    # previous state
    self.vx0  = [0] * N
    self.vy0  = [0] * N
    self.den0 = [0] * N

  def addDensity(self, x, y, amount):
    self.den[IX(x, y)] += amount

  def addVelocity(self, x, y, ax, ay):
    self.vx[IX(x, y)] += ax
    self.vy[IX(x, y)] += ay
