def unique_anti_nodes_locations() -> int:
    with open("./input") as file:
        content = file.read()
    grid = content.strip().split("\n")
    width, height = len(grid[0]), len(grid)
    antennas = {}

    # Locate antennas with identical frequencies (a-z, A-Z, 0-9)
    for y in range(height):
        for x in range(width):
            if grid[y][x] != ".":
                frequency = grid[y][x]
                antennas.setdefault(frequency, []).append({"x": x, "y": y})

    # Calculate unique anti-node locations
    anti_nodes = set()
    for frequency, positions in antennas.items():
        for i, pos1 in enumerate(positions):
            for j, pos2 in enumerate(positions):
                if i == j:
                    continue

                dx, dy = pos2["x"] - pos1["x"], pos2["y"] - pos1["y"]
                antinode_x, antinode_y = pos1["x"] + dx * 2, pos1["y"] + dy * 2

                # Check bounds
                if 0 <= antinode_x < width and 0 <= antinode_y < height:
                    anti_nodes.add(f"{antinode_x},{antinode_y}")
    print(len(anti_nodes))
    return len(anti_nodes)

def unique_locations_in_bounds() -> int:
    with open("./input") as file:
        content = file.read()
    grid = content.strip().split("\n")
    width, height = len(grid[0]), len(grid)
    antennas = {}

    # Locate antennas with identical frequencies (a-z, A-Z, 0-9)
    for y in range(height):
        for x in range(width):
            if grid[y][x] != ".":
                frequency = grid[y][x]
                antennas.setdefault(frequency, []).append({"x": x, "y": y})

    # Calculate all unique anti-node positions considering extended range
    anti_nodes = set()
    for frequency, positions in antennas.items():
        for pos1 in positions:
            for pos2 in positions:
                if pos1 == pos2:
                    continue

                dx, dy = pos2["x"] - pos1["x"], pos2["y"] - pos1["y"]

                # Explore extended positions
                for k in range(-50, 51):
                    antinode_x = pos1["x"] + dx * k
                    antinode_y = pos1["y"] + dy * k

                    # Check bounds
                    if 0 <= antinode_x < width and 0 <= antinode_y < height:
                        anti_nodes.add(f"{antinode_x},{antinode_y}")
    print(len(anti_nodes))
    return len(anti_nodes)

unique_anti_nodes_locations()
unique_locations_in_bounds()
