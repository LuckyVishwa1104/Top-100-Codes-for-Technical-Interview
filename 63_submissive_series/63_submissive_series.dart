import 'dart:io';

int submissiveSeries(int num){
  int sum = 0;
  int i = 1;
  int temp = 1;
  while (i <= num){
    int prod = 1;
    for (int j = 0; j < i; j++){
      prod = prod * temp;
      temp += 1;
    }
    sum+=prod;
    i+=1;
  }
  return sum;
}

void main(){
  try {
    while (true) {
      // program to find sum of submissive series
      stdout.write("Enter number : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num <=20){
        int result = submissiveSeries(num);
        print(result);
      }
      else{
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
