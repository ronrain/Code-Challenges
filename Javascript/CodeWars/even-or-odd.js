function evenOrOdd(number) {
  if (number % 2 === 0){
    return 'Even'
  } else if (number % 2 !== 0){
    return 'Odd'
  } else //Did not need the else
    return 'Odd' 
}

//other option
function evenOrOdd(number){
  return (number % 2 === 0 ? 'Even' : 'Odd')
}