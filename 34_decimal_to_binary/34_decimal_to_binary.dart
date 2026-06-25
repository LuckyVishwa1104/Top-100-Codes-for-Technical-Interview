import 'dart:io';

// program to convert decomal number into binary format

String reverseString(String num) {
  String revString = "";
  for (int i = revString.length - 1; i <= 0; i--) {
    revString = revString + num[i];
  }
  return revString;
}

String decimalToBinary(int decimal) {
  String binaryNum = "";
  while (decimal > 0) {
    int remainder = decimal % 2;
    decimal = decimal ~/ 2;
    binaryNum = binaryNum + remainder.toString();
  }
  return reverseString(binaryNum);
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num < 0) {
        print("Enter the value in decimal");
      } else {
        String result = decimalToBinary(num);
        print("Decimal $num = $result Binary");
      }
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
