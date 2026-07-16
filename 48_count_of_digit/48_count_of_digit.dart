import 'dart:io';

// method to calculate the digit count of number
int digitCount(int num){
  int cnt = 0;
  if(0 == num){
    return 1;
  }
  while (num > 0){
    cnt += 1;
    num ~/= 10;
  }
  return cnt;
}

// drivr program
void main() {
  try {
    while (true) {
      stdout.write("Enter number in integer form : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num < 0){
        num *= -1;
      }

      int result = digitCount(num);
      print("Count of digint in $num ===> $result");

      stdout.write("Do you want to continue the program (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program finished!");
        break;
      }
    }
  } on FormatException catch (e) {
    print("Invalid input : $e");
  } on UnsupportedError catch (e) {
    print("Divide by zero exception : $e");
  } on Exception catch (e) {
    print("Exception caught : $e");
  }
}
