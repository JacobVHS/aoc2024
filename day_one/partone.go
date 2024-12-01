package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	// open the file
	file, err := os.Open("./input")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	// initialize arrays to store the numbers
	var leftNumbers []int
	var rightNumbers []int

	// read the file line by line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		if len(parts) == 2 {
			left, err1 := strconv.Atoi(parts[0])
			right, err2 := strconv.Atoi(parts[1])
			if err1 == nil && err2 == nil {
				leftNumbers = append(leftNumbers, left)
				rightNumbers = append(rightNumbers, right)
			}
		}
	}

	// check for any errors during scanning
	if err := scanner.Err(); err != nil {
		panic(err)
	}

	// sort both lists in ascending order
	sort.Ints(leftNumbers)
	sort.Ints(rightNumbers)

	// calculate the total distance
	var totalDistance int
	for i := 0; i < len(leftNumbers); i++ {
		distance := leftNumbers[i] - rightNumbers[i]
		if distance < 0 {
			distance = -distance
		}
		totalDistance += distance
	}

	fmt.Println("Total distance is:", totalDistance)
}
