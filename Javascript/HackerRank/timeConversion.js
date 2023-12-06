function timeConversion(s){
  let amPm = s.charAt(8) //identifies what character is at what index, using 8 becaus thats the index that has either P or A
  let military = "" //stores hour converted

  if(amPm == 'A'){
    if(s.substring(0,2) == '12'){//detects first case of midnight
      //substring takes consecutive characters from a string and 0,2 will give us character from index 0 to index 1
      military = "00"
    }else{
      military = s.substring(0,2)//does not change 
    }
  } else{//PM
      if(s.substring(0,2)=='12'){
        military = s.substring(0,2)//cover do nothing
      } else {//have to add 12
        //turn into an integer using parsInt
        //use 10 for base 10
        military = parseInt(s.substring(0,2), 10) + 12
      }
  }
  // 12 AM > 00
  //1 AM to 12PM > do nothing
  //i PM to 11PM  > add 12 to hour

  //military is only the first 2 indices so you must add the end indeces
  return(military + s.substring(2,8))
}