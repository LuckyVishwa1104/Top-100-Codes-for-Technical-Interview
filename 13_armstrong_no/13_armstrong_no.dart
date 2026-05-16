import 'dart:io';

int isArmStrong(int num) {
  int numLen = 0;
  while ((num ~/ 10) > 0) {
    numLen = numLen + 1;
  }

  double sumOfDigit = 0;
  while (num > 0) {
    sumOfDigit = sumOfDigit + ((num % 10) * (1 / numLen));
    num = num ~/ 10;
  }
  return sumOfDigit.toInt();
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 0) {
        print("Enter a value positve and greate than or equal to zero");
      } else {
        int result = isArmStrong(num);
        if (result == num) {
          print("$num is a Armstrong number");
        } else {
          print("Not a Armstrong number.");
        }
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
