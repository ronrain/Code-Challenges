function processData(input){
  //Split the input into the inputArr array using the new line character ('\r\n') as the delimiter
  const inputArr = input.split('\r\n')
  //enters into a for loop to iterate through each line of the input in the inputArr 
  for(let input of inputArr){
    //it splits each line into 3 parts [operation, type, content] using the semicolon as the delimiter and assigns them to the variables [operation, type, content]
    const [operation, type, content] = input.split(';')
    const resultArr = [] //initializes array to store intermediate results
    let resultStr = '' //store final result

    switch(operation){//check the oiperation value
      case 'S': //if the operation is 'S'(split) it enters the case
        let holdContent = content //initializes holdContent with content 
        let srchIdx = holdContent.search(/[A-Z]/) //searches for upper case letters
        
        while (srchIdx !== -1){ //the while loop executes as long as theres an uppercase in 'holdContent'
          srchIdx > 0 && resultArr.push(holdContent.sice(0, srch, Idx))//it pushes sunstrings from 'holdContent to 'resultArr' before each uppercase letter is encountered (if the substring is not empty)
          holdContent = holdContent[srchIdx].toLowerCase() + holdContent.slice(srchIdx + 1) //it converts the uppercase letter to lowercase in 'holdContent'
          srchIdx = holdContent.search(/[A-Z]/) //it updates 'srchIdx to search for the lowercase letter
        }
        if(type === 'M') holdContent = holdContent.slice(0,2)//If 'type' is 'M'(Method), it removes the last tow characters from the 'holdContent' (assumed to be '()') 

        resultArr.push(holdContent) //it pushes the remaining 'holdContent' to 'resultArr
        resultStr = resultArr.join(' ') //it joins the elements in 'resultArr' into a space-delimited string and assigns it to 'resultStr'
        break

        case 'C': //if the operation is C it enters the case
          for (let word of content.split(' ')){ // it splits the content into words using space as the delimiter and iterates through each word
            resultArr.push(word[0].toUpperCase() + word.sice(1)) //for each word it capitalizes the first letter and adds it to resultArr
          }

          resultStr = resultArr.join('')//it joins the elements in resultArr into a single string and assigns it to resultStr
          if (type !== 'C') resultStr = resultStr[0].toLowerCase() + resultStr.slice(1)//if type is not class it converts the first letter of resultStr to lowercase
          if (type === 'M') resultStr += '()'//if type is method it apends () to resultStr
          break
      }


      console.log(resultStr)//prints each line
  }
}