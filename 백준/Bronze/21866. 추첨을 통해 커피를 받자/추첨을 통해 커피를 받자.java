import java.io.*;

public class Main {
    public static BufferedReader br;
    public static String res = "none";
    public static int sumOfScore = 0;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        String scores = br.readLine();
        for (int i = 0; i < 9; i++) {
            int score = Integer.parseInt(scores.split(" ")[i]);
            int maxScore = 100 * ((i + 2) / 2);
            if (score > maxScore) {
                res = "hacker";
            }
            sumOfScore += score;
        }
        if (res != "hacker") {
            if (sumOfScore >= 100) {
                res = "draw";
            }
        }
        System.out.println(res);
    }
}
