public class lab3 {
    public static void lab3(String[] args) {
        //9212
        //C3=2, Тип текстових змінних -> String
        //C17=15, Дія з рядком -> В заданому тексті замінити слова заданої довжини визначеним рядком
    	
	    Scanner in = new Scanner(System.in);
	    System.out.print("Input sentence: ");
	    String sentence = in.nextLine();
	    System.out.print("Input desired word: ");
	    String word = in.nextLine();
	    System.out.print("Input number of letters: ");
	    int number = in.nextInt();
	    String result = "";

	    String[] words = sentence.split(" ");
	    for (int i = 0; i < words.length; i++){
	      if (words[i].length() == number) {
	        words[i] = word;
	          }
	        }
	    for (int j =0; j < words.length; j++){
	      result += words[j] + " ";
	        }
	    System.out.println(result);
      
      
     
    }
}
