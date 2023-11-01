function addBinary(a,b) {
  const myNum = a + b
  return parseInt(myNum).toString(2)
}

//parseInt changes the a/b into an integer if given a string
//using 2 because binary is based 2