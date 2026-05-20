import 'dart:io';

// program to find fibonacci series on a particular range

List<int> fibonacciSeries(int num) {
  int n1 = 0;
  int n2 = 1;
  List<int> fiboSeries = [n1];

  while (n2 <= num) {
    fiboSeries.add(n2);
    int n3 = n1 + n2;
    n1 = n2;
    n2 = n3;
  }

  return fiboSeries;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter range value : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 1) {
        print("Enter integer value greater than 1");
      } else {
        List<int> result = fibonacciSeries(num);
        print(result);
      }
    }
  } on FormatException catch (e) {
    print("Invalid input : $e");
  } on Exception catch (e) {
    print("Exception caught : $e");
  }
}
