package main

import (
	"bufio"
	"fmt"
	"os"
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

	// count occurrences of each number in the right list
	rightCount := make(map[int]int)
	for _, num := range rightNumbers {
		rightCount[num]++
	}

	// calculate the similarity score
	var similarityScore int
	for _, num := range leftNumbers {
		if count, exists := rightCount[num]; exists {
			similarityScore += num * count
		}
	}

	fmt.Println("Similarity score is:", similarityScore)
}
