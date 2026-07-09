import 'dart:io';

// dart program to replace all zeros with one

// method to replace 0 by 1
int replaceZero(int num) {
  if (num == 0) return 1;

  int result = 0;
  int place = 1;

  while (num > 0) {
    int digit = num % 10;
    if (digit == 0) digit = 1;

    result += (place * digit);

    place *= 10;
    num ~/= 10;
  }

  return result;
}

// driver program to execute the method and eval the result
void main() {
  try {
    while (true) {
      stdout.write("Enter 1st Fraction (a/b) : ");
      int num = int.parse(stdin.readLineSync()!);

      int result = replaceZero(num.abs());

      if (num < 0)
        print("$num ===> ${-result}");
      else
        print("$num ===> $result");

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
