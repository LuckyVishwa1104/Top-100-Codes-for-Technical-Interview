import 'dart:io';
import 'dart:math';

// euclidean algorithm - log(min(a,b))

int euclideanHcf(int num1, num2) {
  while (num2 > 0) {
    int temp = num1;
    num1 = num2;
    num2 = temp % num2;
  }
  return num1;
}

int brutForceHcf(int a, int b){
  int end = min(a, b);
  List<int> commonFactor = [];
  for (int i = 1; i <= end; i++){
    if (a%i==0 && b%i==0){
      commonFactor.add(i);
    }
  }
  return commonFactor.reduce(max);
}

void main() {
  try {
    while (true) {
      stdout.write("Enter a positive integer value : ");
      int num1 = int.parse(stdin.readLineSync()!);

      stdout.write("Enter a positive integer value : ");
      int num2 = int.parse(stdin.readLineSync()!);

      int maxLimit = 1000;

      if (num1 > maxLimit || num2 > maxLimit) {
        print("Enter a lesser value than 10000");
      } else if (num1 == 0 || num2 == 0) {
        print("Enter a valid integer value : ");
      } else {
        int result = brutForceHcf(num1.abs(), num2.abs());
        print("HCF - $result");
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
