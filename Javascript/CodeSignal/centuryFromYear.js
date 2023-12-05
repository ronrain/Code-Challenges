// Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

// Example

// For year = 1905, the output should be
// solution(year) = 20;
// For year = 1700, the output should be
// solution(year) = 17.
// Input/Output

// [execution time limit] 4 seconds (js)

// [memory limit] 1 GB

// [input] integer year

// A positive integer, designating the year.

// Guaranteed constraints:
// 1 ≤ year ≤ 2005.

// [output] integer

// The number of the century the year is in.

function centuryFromYear(year){
  return Math.floor((year - 1) / 100) + 1
}

//year/100 gives us the first 2 number ex 2000/100 = 20; 1986/100 = 19.86
//Math.Floor() rounds decimal down ex 19.86 = 19; 17 = 17
//add 1 to give accurate century
//Math.floor brings it down^

let a = year - 1 //2000 - 1 = 1999
let b = a / 100 //1999 / 100 = 19.99
let c = Math.floor(b)//Math.floor(19.99) = 19
let d = c + 1//19 + 1 = 20 >>> 1999 is in the 20th century
