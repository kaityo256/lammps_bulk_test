import random


class Atom:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.type = 1
        V0 = 1.0
        self.vx = V0 * random.uniform(-1, 1)
        self.vy = V0 * random.uniform(-1, 1)
        self.vz = V0 * random.uniform(-1, 1)


def make_config(m, s):
    s = 1.55
    h = 0.5 * s
    atoms = []
    for ix in range(0, m):
        for iy in range(0, m):
            for iz in range(0, m):
                x = ix * s
                y = iy * s
                z = iz * s
                atoms.append(Atom(x, y, z))
                atoms.append(Atom(x, y + h, z + h))
                atoms.append(Atom(x + h, y, z + h))
                atoms.append(Atom(x + h, y + h, z))
    return atoms


def save_file(filename, atoms, L):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write(f"{len(atoms)} atoms\n")
        f.write("1 atom types\n\n")
        f.write(f"0 {L} xlo xhi\n")
        f.write(f"0 {L} ylo yhi\n")
        f.write(f"0 {L} zlo zhi\n")
        f.write("\n")
        f.write("Atoms\n\n")
        for i, a in enumerate(atoms):
            f.write(f"{i+1} {a.type} {a.x} {a.y} {a.z}\n")
        f.write("\n")
        f.write("Velocities\n\n")
        for i, a in enumerate(atoms):
            f.write(f"{i+1} {a.vx} {a.vy} {a.vz}\n")
    print(f"Generated {filename}")


if __name__ == "__main__":
    S = 1.55  # Lattice Constant
    M = 50  # Lattice Count
    L = M * S  # Lattice Size
    atoms = make_config(M, S)
    save_file("test.atoms", atoms, L)
