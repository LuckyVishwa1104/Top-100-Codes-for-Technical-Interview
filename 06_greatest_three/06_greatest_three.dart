import "dart:io";

// program to find greatest among the three numbers

int greatesAmongThree(int a, int b, int c){
  if( a > b && a > c){
    return a;
  }
  else if(b > a && b > c){
    return b;
  }
  else{
    return c;
  }
}

void main(){
  try{
  stdout.write("Enter First number : ");
  int a = int.parse(stdin.readLineSync()!);

  stdout.write("Enter second number : ");
  int b = int.parse(stdin.readLineSync()!);

  stdout.write("Enter third number : ");
  int c = int.parse(stdin.readLineSync()!);

  if (a == b && b == c){
    print("All number are equal");
  }
  else{
    int result = greatesAmongThree(a, b, c);
    print("$result is greatest among three numbers");
  }
  }
  on FormatException catch(e){
    print("Invalid input : $e");
  }
  on Exception catch(e){
    print("Exception caught : $e");
  }
  catch(e){
    print("Exception caught : $e");
  }
}

