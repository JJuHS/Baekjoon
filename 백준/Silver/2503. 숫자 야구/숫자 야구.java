import java.io.*;
import java.util.*;
import java.text.*;

public class Main {
    public static ArrayList<String> arr = new ArrayList<>();
    public static ArrayList<String> noAns = new ArrayList<>();
    public static int n, res;
    public static BufferedReader br;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());    // 주어지는 숫자 개수
        // 123부터 987까지 arr에 넣기
        for (int i = 1; i < 10; i++) {
            for (int j = 1; j < 10 ; j++) {
                for (int k = 1; k < 10 ; k++) {
                    if (i!=j && i!= k && j!= k) {
                        arr.add(String.valueOf(100 * i + 10 * j + k));
                    }
                }
            }
        }
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String tmp = st.nextToken();    // 세 자리 숫자
            int s = Integer.parseInt(st.nextToken());    // 스트라이크
            int b = Integer.parseInt(st.nextToken());   // 볼
            for (int j = 0; j < arr.size(); j++) {
                if (noAns.contains(arr.get(j))) {
                    continue;
                }
                int numS = 0;
                int numB = 0;
                for (int k = 0; k < 3 ; k++) {
                    if (tmp.charAt(k) == arr.get(j).charAt(k)) {
                        numS++;
                    } else if (arr.get(j).contains(String.valueOf(tmp.charAt(k)))) {
                        numB++;
                    }
                }
                if (s != numS || b!= numB) {
                    noAns.add(arr.get(j));
                }
            }
        }
        System.out.println(arr.size() - noAns.size());
    }
}
