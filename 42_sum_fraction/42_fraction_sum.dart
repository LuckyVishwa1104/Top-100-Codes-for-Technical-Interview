import 'dart:io';

// euclidean algorithm - log(min(a,b)) for find HCF of two number
int euclideanHcf(int num1, num2) {
  while (num2 > 0) {
    int temp = num1;
    num1 = num2;
    num2 = temp % num2;
  }
  return num1;
}

List<int> fractionalSum(int nume1, int deno1, int nume2, int deno2) {
  int nume3 = (nume1 * deno2) + (deno1 * nume2);
  int deno3 = (deno1 * deno2);
  int hcf = euclideanHcf(nume3.abs(), deno3.abs());
  nume3 = nume3 ~/ hcf;
  deno3 = deno3 ~/ hcf;
  if (deno3 < 0) {
    nume3 *= -1;
    deno3 *= -1;
  }
  return [nume3, deno3];
}

void main() {
    try {
    while (true) {
      stdout.write("Enter 1st Fraction (a/b) : ");
      var [nume1, deno1] = stdin.readLineSync()!.split("/").map(int.parse).toList();

      stdout.write("Enter 2nd Fraction (c/d) : ");
      var [nume2, deno2] = stdin.readLineSync()!.split("/").map(int.parse).toList();

      if(deno1 == 0 || deno2 == 0){
        print("Enter integer values for denominators");
      }
      else{
        List<int> result = fractionalSum(nume1, deno1, nume2, deno2);
        print("($nume1/$deno1) + ($nume2/$deno2)  =====>  (${result[0]}/${result[1]})");
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
