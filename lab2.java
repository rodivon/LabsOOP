public class Lab3 {
    public static void main(String args[]) {
        double A[][] = {{0, 7, 7},
                        {5, 1, 8},
                        {4, 8, 4},
                        {3, 2, 0}};
        double B[][] = {{8, 1, 4},
                        {2, 7, 1},
                        {4, 7, 1},
                        {1, 5, 9}};
        double S = 0;
        double S1 = 0;

        if (A.length == B.length) {
            int maxl = 0;

            for (int i = 0; i < A.length; i++) {
                if (A[i].length != B[i].length) {
                    System.out.println("Невірні вхідні дані!"); 
                }
            }

            for (int i = 0; i < A.length; i++) {
                if (A[i].length > maxl) maxl = A[i].length;
            }
            double C[][] = new double[A.length][maxl];

            for (int i = 0; i < A.length; i++) {
                for (int j = 0; j < A[i].length; j++) {
                    C[i][j] = (double) A[i][j] + (double) B[i][j];
                }
            }

            System.out.println("Матриця С:");
            for (int i = 0; i < C.length; i++) {
                for (int j = 0; j < C[i].length; j++) {
                    System.out.print(C[i][j] + " ");
                }
                System.out.println(" ");
            }

            for (int i = 0; i < C.length; i++) {
                if (i % 2 == 1) {
                    double max = C[i][0];
                    for (int j = 1; j < C[i].length; j++) {
                        if (C[i][j] > max) {
                            max = C[i][j]; 
                    }
                }
                S += max;
            }
            
                if (i % 2 == 0) {
                    double min = C[0][i];
                    for (int j = 1; j < C[i].length; j++) {
                        if (C[i][j] < min) {
                            min = C[i][j];
                
                            }
                        }
                S1 += min;
            }
            }
            System.out.println("\nCума найбільших елементів в рядках матриці з непарними номерами  дорівнює: " + S);
            System.out.println("\nСума найменших елементів в рядках матриці з парними номерами  дорівнює: " + S1);
        }
        else System.out.println("Матриці різного розміру!");
}
}