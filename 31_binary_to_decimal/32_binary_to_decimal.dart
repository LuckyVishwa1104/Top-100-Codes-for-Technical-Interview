import 'dart:io';
import 'dart:math';

int decimalToBinary(int bin) {
  int digit_sum = 0;
  String bin_str = bin.toString();
  int expo = 0;
  for (int i = (bin_str.length - 1); i >= 0; i++) {
    int poww = int.parse(bin_str[i]) * pow(2, expo).toInt();
    expo = expo + 1;
    digit_sum = digit_sum + poww;
  }
  return digit_sum;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num1 = int.parse(stdin.readLineSync()!);

      if (num1.toString().length < 4 || num1 <= 0) {
        print("Enter the value in decimal format");
      }  else {
        int result = decimalToBinary(num1);
        print("$num1  ===>   $result");
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
