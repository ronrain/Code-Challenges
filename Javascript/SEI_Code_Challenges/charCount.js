/*------------------------------------------
								CHALLENGE
--------------------------------------------

1) Code a function named charCount that
	 accepts a string as its only argument and
	 returns an object with the count of each
	 character in the string.
2) The returned object should have properties
	 where the keys are a character in the
	 string and the value is how many times the
	 character appears in the string argument.
3) Upper and lower case characters should be
	 counted separately.
4) Space characters should be counted too.

	 For example:

		charCount("Hello there")

		would return an object like this -->
			{ H: 1, e: 3, l: 2, o: 1, ' ': 1, t: 1, h: 1, r: 1 }

------------------------------------------*/

// Write the function here....
function charCount(str){
  //set up an empty object
  newObject = {}
  //set up a loop that goes through each 
  for(let i = 0; i < str.length; i++) {
    //hasOwnProperty checks if a character in the object is the same" has the same property
    if (newObject.hasOwnProperty(str[i])) {
      //if the object does have the same property, then the count is increased by 1
      newObject[str[i]] += 1
    } else {
      //if it doesnt then the count stays the same
      newObject[str[i]] = 1
    }
  }
  return newObject;
}