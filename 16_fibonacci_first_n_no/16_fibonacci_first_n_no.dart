import 'dart:io';

// program to find first n numbers in fibonacci series

List<int> fibonacciSeries(int num){
  int n1 = 0;
  int n2 = 1;
  List<int> fiboSeries = [n1];

  for (int i = 0; i <= num; i++){
    fiboSeries.add(n2);
    int n3 = n1 + n2;
    n1 = n2;
    n2 = n3;
  }

  return fiboSeries;
}

void main(){

  try{

    while(true){
      stdout.write("Enter range value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num < 0) {
        print("Enter integer value greater than 0");
      } else {
        List<int> result = fibonacciSeries(num);
        print(result);
      }

      stdout.write("Do you want to continue? (y/n) : ");
      String choice = stdin.readLineSync()!.toLowerCase();
      if (choice == 'n') {
        print("Program Finished");
        break;
      }
    }

  } on FormatException catch (e) {
    print("Invalid input : $e");
  } on Exception catch (e) {
    print("Exception caught : $e");
  }

}