import generator as g
import process as p
import analyze as a

def main():
    coords = g.create_coords(cols=100, rand_lower=0, rand_upper=100)
    g.save_coords(coords)
    p.main()
    a.main()

if __name__ == "__main__":
    main()