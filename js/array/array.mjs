(function main() {
  console.log("Array module executing...\n");

  // Empty array
  const empty = [];

  // Non-empty array
  // Arrays are dynamic + mutable by default
  const array = [1, 2, 3, 4, 5];
  console.log(`array: ${formatArray(array)}`);

  // Array with mixed types
  const mixedTypes = [1, true, "cat", 0.5];
  console.log(`mixedTypes: ${formatArray(mixedTypes)}`);

  // Array initialized with all zeros
  const zeros = new Array(3).fill(0);
  console.log(`zeros: ${formatArray(zeros)}`);

  // Array with elements uninitialized
  const uninitialized = new Array(3);
  console.log(`uninitialized: ${formatArray(uninitialized)}`); // All elements are undefined

  // Access
  const value = array[0];
  console.log(`value at 0: ${value} \n`);

  // Length
  const length = array.length;
  console.log(`array length: ${length} \n`);

  // Prepend
  array.unshift(0);
  console.log("array.unshift(0)")
  console.log(`array: ${formatArray(array)}`);

  // Append
  array.push(6);
  console.log("array.push(6)")
  console.log(`array: ${formatArray(array)}`);

  // Insert at index (inserting 2 at index 2)
  array.splice(2, 0, 2);
  console.log("array.splice(2, 0, 2)");
  console.log(`array: ${formatArray(array)}`);

  // Pop last
  const last = array.pop();
  console.log("array.pop()");
  console.log(`last element: ${last}`);
  console.log(`array: ${formatArray(array)}`);

  // Pop first
  const first = array.shift();
  console.log("array.shift()");
  console.log(`first element: ${first}`);
  console.log(`array: ${formatArray(array)}`);

  // Remove at index (removing from index 2)
  const removed = array.splice(2, 1);
  console.log("array.splice(2, 1)");
  console.log(`removed element: ${removed}`);
  console.log(`array: ${formatArray(array)}`);

  // Shallow copy (works for array with primitives)
  const shallowCopy = [...array];
  console.log(`shallow copy: ${formatArray(shallowCopy)}`);

  // Deep copy (works for array with objects)
  const deepCopy = JSON.parse(JSON.stringify(array));
  console.log(`deep copy: ${formatArray(deepCopy)}`);

  // Merge
  const merged = [...array, ...[6, 7, 8]];
  console.log(`merged array: ${formatArray(merged)}`);

  // Map
  const mapped = array.map((value, index, arr) => (value * 2) + index);
  console.log(`mapped array (each value multipled by 2 + index): ${formatArray(mapped)}`);

  // Filter
  const filtered = array.filter((value, index, arr) => value % 2 === 0);
  console.log(`filtered array (only keep even numbers): ${formatArray(filtered)}`);

  // Reduce
  const sum = array.reduce((accum, value, index, arr) => accum + value, 0);
  console.log(`reduced array (sum of all elements): ${sum}\n`);

  // Find
  const target = array.find((value, index, array) => value == 2);
  console.log(`target value 2: ${target}\n`);

  const targetNotFound = array.find((value, index, array) => value == 7);
  console.log(`target value not found: ${targetNotFound}\n`);

  // Find index
  const targetIndex = array.findIndex((value, index, array) => value == 2);
  console.log(`target value index: ${targetIndex}\n`);

  // Sort array of numbers
  array.sort((a, b) => a - b);
  console.log(`sorted array: ${formatArray(array)}`);
  
  // Sort array of strings
  // array.sort()

  /* All pairs */
  const pairs = [];
  for (let i = 0; i < array.length - 1; i++) {
    for (let j = i + 1; j < array.length; j++) {
      pairs.push([array[i], array[j]])
    }
  }
  console.log(`all pairs: [[${pairs.join("],[")}]]\n`);

  /* All triplets */
  const triplets = [];
  for (let i = 0; i < array.length - 2; i++) {
    for (let j = i + 1; j < array.length - 1; j++) {
      for (let k = j + 1; k < array.length; k++) {
        triplets.push([array[i], array[j], array[k]]);
      }
    }
  }
  console.log(`all triplets: [[${triplets.join("],[")}]]\n`);

  /* Subsequences with length k */
  const k = 4;
  const result = [];

  function subsequences(index, k, subsequence) {
    if (subsequence.length === k) {
      result.push([...subsequence]);
      return;
    }

    if (index === array.length) return;

    // include element at index
    subsequence.push(array[index]);
    subsequences(index + 1, k, subsequence);

    // exclude element at index
    subsequence.pop();
    subsequences(index + 1, k, subsequence);
  }

  subsequences(0, k, []);
  console.log(`all subsequences with length ${k}: [[${result.join("],[")}]]\n`); 

  function formatArray(array) {
    return `[${array.join(",")}]\n`
  }

})();