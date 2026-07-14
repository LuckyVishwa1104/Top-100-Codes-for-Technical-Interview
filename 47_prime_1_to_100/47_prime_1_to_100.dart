import 'dart:io';
import 'dart:math';

bool isPrime(int n) {
  if (n < 2) return false;
  for (var d = 2; d <= sqrt(n).toInt(); d++) {
    if (n % d == 0) return false;
  }
  return true;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter number in integer form : ");

      var result = [
        for (var n = 2; n <= 100; n++)
          if (isPrime(n)) n,
      ];
      print(result);

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
