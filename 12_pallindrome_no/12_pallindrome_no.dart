import 'dart:io';

String isPallindrome(int num) {
  String num_ = num.toString();
  String revNum = '';
  int i = num_.length - 1;
  while (i >= 0) {
    revNum = revNum + num_[i];
    i = i - 1;
  }
  return revNum;
}

void main() {
  try{
    while(true){

      stdout.write("Enter positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (isPallindrome(num) == num.toString()){
        print("$num is a pallindrome number");
      }
      else{
        print("$num is not a pallindrome number");
      }

      stdout.write("Do you want to continue? (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program Finished");
        break;
      }
    }
  }
  on FormatException catch(e){
    print("Invalid Input : $e");
  }
  on Exception catch(e){
    print("Exception caught : $e");
  }
}
