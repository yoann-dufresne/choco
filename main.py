

def choco_exp(H, L, h, l):
    print(H, L, h, l)
    if H == L == 1:
        return False

    # Pour la partie gauche de la tablette
    for x in range(1, l+1):
        val = choco_exp(H, L-x, h, l-x)
        if not val:
            return True

    # Pour la partie droite
    for x in range(l+1, L):
        val = choco_exp(H, x, h, l)
        if not val:
            return True

    # Pour la partie haute
    for x in range(1, h+1):
        val = choco_exp(H-x, L, h-x, l)
        if not val:
            return True

    # Pour la partie basse
    for x in range(h+1, H):
        val = choco_exp(x, L, h, l)
        if not val:
            return True

    return False



def choco_progdyn(H, L, h, l, states=None):
    print(H, L, h, l)
    if H == L == 1:
        return False

    if states is None:
        states = [[None]*(L+1) for _ in range(H+1)]

    # Saved values
    substates = states[H][L]
    if substates is not None:
        if substates[h][l] is not None:
            return substates[h][l]
    else:
        states[H][L] = [[None]*L for _ in range(H)]

    states[H][L][h][l] = True
    # Pour la partie gauche de la tablette
    for x in range(1, l+1):
        val = choco_progdyn(H, L-x, h, l-x, states)
        if not val:
            return True

    # Pour la partie droite
    for x in range(l+1, L):
        val = choco_progdyn(H, x, h, l, states)
        if not val:
            return True

    # Pour la partie haute
    for x in range(1, h+1):
        val = choco_progdyn(H-x, L, h-x, l, states)
        if not val:
            return True

    # Pour la partie basse
    for x in range(h+1, H):
        val = choco_progdyn(x, L, h, l, states)
        if not val:
            return True

    states[H][L][h][l] = False
    return False



def choco_progdyn_opti(H, L, h, l, states=None):
    print(H, L, h, l)
    if H == L == 1:
        return False

    # Rotations
    if H < L:
        tmp = H
        H = L
        L = tmp
        tmp = h
        h = l
        l = tmp
        # print("Rotation", H, L, h, l)

    # Symetry
    if h > H/2:
        h = H-1-h
        # print("Symetry", H, L, h, l)
    if l > L/2:
        l = L-1-l
        # print("Symetry", H, L, h, l)

    if states is None:
        states = [[None]*(L+1) for _ in range(H+1)]

    # Saved values
    substates = states[H][L]
    if substates is not None:
        if substates[h][l] is not None:
            return substates[h][l]
    else:
        states[H][L] = [[None]*L for _ in range(H)]

    states[H][L][h][l] = True
    # Pour la partie gauche de la tablette
    for x in range(1, l+1):
        val = choco_progdyn_opti(H, L-x, h, l-x, states)
        if not val:
            return True

    # Pour la partie droite
    for x in range(l+1, L):
        val = choco_progdyn_opti(H, x, h, l, states)
        if not val:
            return True

    # Pour la partie haute
    for x in range(1, h+1):
        val = choco_progdyn_opti(H-x, L, h-x, l, states)
        if not val:
            return True

    # Pour la partie basse
    for x in range(h+1, H):
        val = choco_progdyn_opti(x, L, h, l, states)
        if not val:
            return True

    states[H][L][h][l] = False
    return False



if __name__ == "__main__":
    H = L = 10
    h = 7
    l = 3
    # print(choco_exp(H, L, h, l))
    print(choco_progdyn(H, L, h, l))
    # print(choco_progdyn_opti(H, L, h, l))
