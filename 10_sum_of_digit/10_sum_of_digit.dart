import 'dart:io';

// DART program to find sum of all digit of a number

int sumOfDigit(int num) {
  int sum = 0;
  while (num > 0) {
    sum = sum + (num % 10);
    num = num ~/ 10;
  }

  return sum;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 0) {
        print("Enter a integer value greater than Zero");
      } else {
        int result = sumOfDigit(num);
        print("Sum of digit of $num is $result");
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
