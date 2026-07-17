import 'dart:io';

int digitCount(int number, int digit){
  int count = 0;

  while (number > 0){
    int last_digit = number % 10;
    if (last_digit == digit) count += 1;
    number ~/= 10;
  }

  return count;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter number : ");
      int number = int.parse(stdin.readLineSync()!);

      stdout.write("Enter digit : ");
      int digit = int.parse(stdin.readLineSync()!);

      if (digit <= 0) {
        print("Enter positive integer number for digit");
      }
      else{
        int result = digitCount(number, digit);
        print("$digit occurs $result times in $number .");
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
