const calculateResult = (partB) => {
    return $0.innerText
        .split('\n\n') // Split the text into groups
        .reduce((ins, group) => {
            return group
                .trim()
                .split('\n') // Split each group into lines
                .map(line => {
                    const sortedElements = line.split(',').sort((a, b) => {
                        // Sort elements based on the `ins` matching condition
                        return ins.match(`${a}\\|${b}`) ? -1 : 1;
                    });
                    return { 
                        original: line, 
                        sorted: sortedElements 
                    };
                })
                .filter(({ original, sorted }) => {
                    // Filter based on whether partB logic matches
                    return (original === sorted.join(',')) ^ partB;
                })
                .reduce((sum, { sorted }) => {
                    // Add the middle element of sorted array to the sum
                    return sum + +sorted[Math.floor(sorted.length / 2)];
                }, 0); // Start with an initial sum of 0
        });
};

// Calculate for partA and partB
const partAResult = calculateResult(false); // partA
const partBResult = calculateResult(true);  // partB

console.log({ partAResult, partBResult });
