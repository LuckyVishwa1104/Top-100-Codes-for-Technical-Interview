import 'dart:io';

// program to find the prime factors of a number

// method to check the prime nature of the number
bool isPrime(int number){
  for (int i = 2; i < (number ~/ 2) + 1; i++){
    if (number % i == 0){
      return false;
    }
  }
  return true;
}

// method to generate list of all prime factors of a number
List<int> primeFactors(int num){
  List<int> factorList = [];
  for (int i = 2; i < (num ~/ 2) + 1; i++){
    if (num % i == 0){
      factorList.add(i);
    }
  }
  factorList.add(num);

  List <int> primeFactorList = [];

  for (int i = 0; i < factorList.length; i ++){
    if (isPrime(factorList[i]) == true){
      primeFactorList.add(factorList[i]);
    }
  }

  return primeFactorList;
}

void main(){

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
        List<int> result = primeFactors(num);
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