import 'dart:io';

int powerOfNumber(int num, int pow) {
  int result = 1;

  for (int i = 0; i < pow; i++) {
    result = result * num;
  }

  return result;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a number : ");
      int num = int.parse(stdin.readLineSync()!);

      stdout.write("Enter a number : ");
      int pow = int.parse(stdin.readLineSync()!);

      if (num <= 0 || pow <= 0) {
        print("Enter positive integer value");
      } else {
        int result = powerOfNumber(num, pow);
        print(result);
      }

      stdout.write("Do you want to continue? (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program Finished");
        break;
      }
    }
  } on FormatException catch (e) {
    print("Invalid input : $e");
  } on Exception catch (e) {
    print("Exception caught : $e");
  }
}
