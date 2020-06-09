import java.util.Scanner;

public class Main {
  //9212
  //C2=0, O1="+"
  //C3=2, C=2
  //C5=2, O2="%"
  //C7=0 -> byte
  public static void main(String[] args){
    double S = 0;
    final int C=2;
    Scanner x = new Scanner(System.in);
        System.out.print("Input a: \n" );
        int a = x.nextByte();
        System.out.print("Input n: \n");
        int n = x.nextByte();
        System.out.print("Input b: \n");
        int b = x.nextByte();
        System.out.print("Input m: \n");
        int m = x.nextByte();
    
    if ((a<=n)&&(b<=m)){
        for (byte i = (byte) a; i <= n; i++){
            if(i==-2){
                System.out.println("Деление на 0");
                S = 0;
                break;
            }
            else {
                for (byte j = (byte) b; j <= m; j++){
                  S = S + ((double)(i%j)/(i+C));
          }
        System.out.println(S);
            }
        }
    }
    else System.out.println("Неккоректные значения");
  }  
}