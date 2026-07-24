import 'dart:io';

void main() {
  try {
    while (true) {
      stdout.write("Enter the no of element of list : ");
      int arrlen = int.parse(stdin.readLineSync()!);
      stdout.write("Enter the element of the list ");
      List<int> arr = [];
      for (int i = 0; i < arrlen; i++) {
        int arrEle = int.parse(stdin.readLineSync()!);
        arr.add(arrEle);
      }
      int maxEle = arr[0];
      void isLargest(int index) {
        if (index >= arrlen) return; // recursion termination
        if (arr[index] > maxEle) {
          maxEle = arr[index];
        }
        isLargest(index + 1); // recursion iteratino 
      }

      isLargest(0);  // recursion initialization

      print("Larget elemet is - $maxEle");

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
