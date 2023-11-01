function friend(friends){
  //start with an empty array that the names that only have 4 letters will be in
  const result = []
  //loop through the friends array
  for (i = 0; i < friends.length; i++){
    //create the if statement to match the length of each name
    if(friends[i].length === 4){
      //add the friend to the result array
      result.push(friends[i]) 
    }
  }
  //return the array of matching friends
  return result
}

//other option:
function friend(friends){
  //filter method is built-in; more concise; and doesnt need for a seperate array
  return friends.filter(n => n.length === 4)
}