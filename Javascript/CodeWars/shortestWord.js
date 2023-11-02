function findShort(s) {
  const words = s.split(' ')
  return words.reduce((shortest, word) => Math.min(shortest, word.length), Infinity)
}





// function findShort(s){
//   //make array of words
//   let words = s.split(' ')
//   //call reduce method on words array
//   return words.reduce(
//     //takes 2 arguments
//     (shortest, word)) =>
//     //used to find the minimum value between shortest and word.length (tracks shorts word during reduction cycle)
//     Math.min
//     //comparing length of word with the shortest value
//     (shortest, word.length), 
//     //acts as a placeholder for shortest value
//     Infinity)
// }

//other option:
function findShort(s){
	var arr = s.split(' ');
	var smallest = arr[0];
	for (var i = 0; i < arr.length; i++) {
		if(arr[i].length < smallest.length){
			smallest = arr[i];
		}
	}
	return smallest.length;
}
