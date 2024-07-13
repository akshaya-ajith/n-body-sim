from space import universe, body

def main():
    bodies = []
    total_e = 0
    u = universe(bodies, total_e)
    u.run()

if __name__ == "__main__":
    main()