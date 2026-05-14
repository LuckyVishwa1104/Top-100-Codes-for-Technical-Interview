import 'dart:io';

// program to reverse a number 

String reverseNumber(int num) {
  String revNum = "";
  while (num > 0) {
    int lastDigit = num % 10;
    revNum = revNum + lastDigit.toString();
    num = num ~/ 10;
  }
  return revNum;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 0) {
        print("Enter a integer value greater than Zero");
      } else {
        int result = int.parse(reverseNumber(num));
        print("$num.  ===>.  $result");
      }

      stdout.write("Do you want to continue? (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program Finished");
        break;
      }
    }
  } on FormatException catch (e) {
    print("Invalid Input : $e");
  } on UnsupportedError catch (e) {
    print("Divide by Zero exception : $e");
  } on Exception catch (e) {
    print("Exception caught : $e");
  }
}
