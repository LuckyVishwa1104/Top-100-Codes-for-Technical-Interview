import 'dart:io';

int lastNonZeroDigit(int num){
  int fact = 1;
  for (int i = num; i >= 1; i--){
    fact = fact * i;
  }
  while (fact > 0){
    int unit = fact % 10;
    if(unit != 0) return unit;
    fact = fact ~/ 10;
  }
  return 0;
}

void main(){
  try {
    while (true) {
      // program to find last non zero digit of a factorial of a particular number
      stdout.write('Enter the number : ');
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 20) {
        int result = lastNonZeroDigit(num);
        print(result);
      } else {
        print("Input is to large");
      }

      stdout.write("Do you want to continue the program (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program finished!");
        break;
      }
    }
  } on FormatException catch (fe) {
    print("Invalid Input - $fe");
  } on UnsupportedError catch (ue) {
    print("Divide by zero exception - $ue");
  } on Exception catch (e) {
    print("Exception caught - $e");
  }

}
