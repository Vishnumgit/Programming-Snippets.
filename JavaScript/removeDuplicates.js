function removeDuplicates(array) {
    // Uses ES6 Set to instantly extract unique items
    return [...new Set(array)];
}

// Example Usage
const numbers =;
const uniqueNumbers = removeDuplicates(numbers);
console.log("Original Array:", numbers);
console.log("Deduplicated Array:", uniqueNumbers);
