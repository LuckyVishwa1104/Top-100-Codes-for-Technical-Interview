import 'dart:io';

// dart program to find 

int decodingCount(int num){
  int cnt = 1;
  String numStr = num.toString();

  for (int i = 0; i < numStr.length -1; i++){
    if(numStr[i+1] == '0'){
      continue;
    }

    int currentDigit = int.parse(numStr[i]);
    int nextDigit = int.parse(numStr[i+1]);

    if(currentDigit == 1 || nextDigit == 2 && nextDigit < 7){
      cnt+=1;
    }
  }
  return cnt;
}

void main() {
  try {
    while (true) {
      stdout.write("Enter number in integer form : ");
      int num = int.parse(stdin.readLineSync()!);

      if (num <= 0){
        print("Enter positive integer value");
      }
      else{
        int result = decodingCount(num.abs());
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
