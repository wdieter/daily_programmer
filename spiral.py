def next_blocked(a, y, x, dx, dy, n) :
    if False in [0 <= x+dx < n, 0 <= y+dy < n]: return True
    if(a[y+dy][x+dx] != 0): return True
    return False      
        
def spiral(n, c, clock = True):
    a = [[0 for i in range(n)] for k in range(n)]
    cs = {0:(0,0), 1:(n-1, 0), 2: (n-1, n-1), 3: (0, n-1)}
    comp = {'s': (1,0), 'w': (0,-1), 'n': (-1,0), 'e': (0,1)}
    o = ['e','s','w','n']
    y = cs[c][1]
    x = cs[c][0]
    d = 1
    if clock == False: 
        c = (c + 1)%4 
        d = -1
    dx = comp[o[c]][1]
    dy= comp[o[c]][0]
    for p in range(1,(n**2)+1) :
        if(next_blocked(a, y, x, dx, dy, n)):
            c = (c + d)%4
            dx = comp[o[c]][1]
            dy= comp[o[c]][0]
        a[y][x] = str(p).rjust(len(str(n**2)))
        y += dy
        x += dx
    for i in a:
        print (" ".join(i))

spiral(10,2,False)
