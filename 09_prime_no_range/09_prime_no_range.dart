import 'dart:io';
import 'dart:math';

List<int> primeList(int num) {

  List<int> primeList = [];

  for (int i = 2; i <= num; i++) {
    bool isNotPrime = false;
    int temp = sqrt(i).toInt() + 1;
    for (int j = 2; j < temp; j++) {
      if (i % j == 0) {
        isNotPrime = true;
      }
    }

    if (!isNotPrime) {
      primeList.add(i);
    }
  }

  return primeList;
}

void main() {
  while (true) {
    try {
      stdout.write("Enter a integer value greater than 1 : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 1) {
        print("Enter a positive integer value number greate than 1");
      } else {
        List<int> result = primeList(num);
        print(result);
      }
    } on FormatException catch (e) {
      print("Invaild Input : $e");
    } on Exception catch (e) {
      print("Exception caught : $e");
    }
    stdout.write("Do you want to continue? (y/n) : ");
    String choice = stdin.readLineSync()!.toLowerCase();
    if (choice == 'n') {
      print("Program Finished");
      break;
    }
  }
}
