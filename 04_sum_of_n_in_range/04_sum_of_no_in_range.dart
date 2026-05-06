import 'dart:io';

// program to find sum of range with provide starting and ending values

int summation(int a, int b){
  int result = 0;
  for(int i = 0; i <= b; i++){
    result = result + i;
  }
  return result;
}

void main(){
  try{
    stdout.write("Enter starting range : ");
    int a = int.parse(stdin.readLineSync()!);
    stdout.write("Enter ending range : ");
    int b = int.parse(stdin.readLineSync()!);

    if (a < 0 || b < 0){
      print("Enter positive integer value");
    }
    else{
      int result = summation(a, b);
      print("Sum of range between $a and $b is : $result");
    }

  }
  on FormatException catch (e){
    print("Invalid input : $e");
  }
  catch (e){
    print("Exception caught : $e");
  }
}


