import 'dart:io';

int subsetSum(List<int> arr){
  int finalSum = 0;
  for (int i = 0; i < arr.length; i++){
    int currentSum = 0;
    for (int j = i; j < arr.length; j++){
      currentSum += arr[j];
      finalSum+=currentSum;
    }
  }
  return finalSum;
}

void main() {
  try {
    while (true) {
      // program to find sum of subset of array
      stdout.write('Enter space separated array elements : ');

      // Read input, split by space, parse to int, and convert to a List
      List<int> arr = stdin
          .readLineSync()!
          .trim()
          .split(RegExp(r'\s+'))
          .map(int.parse)
          .toList();

      if (arr.length <= 10) {
        int result = subsetSum(arr);
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
