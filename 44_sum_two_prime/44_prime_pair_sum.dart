import 'dart:io';
import 'dart:math';

List<int> primeRange(int num) {
  List<int> primeNoRange = [];
  for (int i = 2; i <= num; i++){
    bool isPrime = true;
    for(int j = 2; j <= sqrt(i).toInt(); j++){
      if(i % j == 0){
        isPrime = false;
        break;
      }
    }
    if (isPrime){
      primeNoRange.add(i);
    }
  }
  return primeNoRange;
}

List<List<int>> primeSumPair(int num){
  List<List<int>> primeSumPairs = [];
  List<int> primeRangeList = primeRange(num);
  int end = primeRangeList.length;
  for (int i = 0; i < end ; i++){
    for(int j = i; j < end; j++){
      if(primeRangeList[i] + primeRangeList[j] == num){
        primeSumPairs.add([primeRangeList[i], primeRangeList[j]]);
      }
    }
  }
  return primeSumPairs;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter 1st Fraction (a/b) : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 0){
        print("Enter positive integer value");
      }
      else{
        List<List<int>> result = primeSumPair(num);
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
