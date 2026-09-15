import 'dart:io';

List<List<int>> pascleTriangle(int num){
  List<List<int>> pascleList = [];
  for (int i = 0; i < num; i++){
    List<int> currentList = [];
    for (int j = 0; j < i+1; j++){
      if (j == 0 || i == j) currentList.add(1);
      else currentList.add(pascleList[i-1][j-1] + pascleList[i-1][j]);
    }
    pascleList.add(currentList);
  }
  return pascleList;
}

void main(){
  try {
    while (true) {
      // program to find pascle triangle
      stdout.write('Enter the number : ');
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 10) {
        List<List<int>> result = pascleTriangle(num);
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
