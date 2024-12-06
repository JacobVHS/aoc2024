package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, _ := os.Open("./input")
	defer file.Close()

	var grid []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		grid = append(grid, scanner.Text())
	}

	// Directions: up=0,right=1,down=2,left=3
	// Turns right: dir = (dir+1)%4
	// Movement: up: row-1; right: col+1; down: row+1; left: col-1
	dR := []int{-1, 0, 1, 0}
	dC := []int{0, 1, 0, -1}

	var startR, startC, dir int
	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[r]); c++ {
			switch grid[r][c] {
			case '^':
				startR, startC, dir = r, c, 0
			case '>':
				startR, startC, dir = r, c, 1
			case 'v':
				startR, startC, dir = r, c, 2
			case '<':
				startR, startC, dir = r, c, 3
			}
		}
	}

	visited := make(map[[2]int]bool)
	r, c := startR, startC
	visited[[2]int{r, c}] = true

	for {
		frontR := r + dR[dir]
		frontC := c + dC[dir]

		// Check if in front is blocked or out of bounds
		if frontR < 0 || frontR >= len(grid) || frontC < 0 || frontC >= len(grid[0]) || grid[frontR][frontC] == '#' {
			// turn right
			dir = (dir + 1) % 4
		} else {
			// move forward
			r, c = frontR, frontC
			if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[0]) {
				break
			}
			visited[[2]int{r, c}] = true
		}

		// If out of the map after moving
		if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[0]) {
			break
		}
	}

	fmt.Println(len(visited))
}
