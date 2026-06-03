import 'dart:io';

// Friendly number - two numbers for which  sum of their factor are equal to every other number are called as friendly pai number

List<int> properFactors(int num){
  List<int> factors = [];
  for (int i = 1; i <= (num ~/2); i++){
    if(num % i == 0){
      factors.add(i);
    }
  }
  return factors;
}

int factorSum(List<int> fact){
  int sum = 0;
  for (int i =0; i<fact.length; i++){
    sum+=fact[i];
  }
  return sum;
}

bool isFirendly(num1, num2){
  if (num1 == num2){
    return false;
  }
  int sum1 = factorSum(properFactors(num1));
  int sum2 = factorSum(properFactors(num2));
  return (num1 == sum2 && num2 == sum1);
}

void main(){
  try{
    while(true){
      stdout.write("Enter a positive integer value : ");
      int num1 = int.parse(stdin.readLineSync()!);

      stdout.write("Enter a positive integer value : ");
      int num2 = int.parse(stdin.readLineSync()!);

      int maxLimit = 1000;

      if (num1 > maxLimit || num2 > maxLimit) {
        print("Enter a lesser value than 10000");
      } else if (num1 <= 0 || num2 <= 0) {
        print("Enter a valid integer value : ");
      } else {
        bool result = isFirendly(num1, num2);
        if(result){
          print("$num1 and $num2 are friendly number.");
        }
        else{
          print("$num1 and $num2 are not friendly number.");
        }
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