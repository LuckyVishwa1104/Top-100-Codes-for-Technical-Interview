import 'dart:io';

// program to find factor of a numbers

List<int> factorOfNumber(int num) {
  List<int> factorList = [1];
  for (int i = 2; i < (num ~/ 2) + 1; i++) {
    if (num % i == 0) {
      factorList.add(i);
    }
  }

  if (num != 1) {
    factorList.add(num);
  }
  return factorList;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num = int.parse(stdin.readLineSync()!);

      int maxLimit = 1000;

      if (num > maxLimit) {
        print("Enter a lesser value than 10000");
      } else if (num <= 0) {
        print("Enter a valid integer value : ");
      } else {
        List<int> result = factorOfNumber(num);
        print(result);
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
