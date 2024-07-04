import java.io.*;

public class Main {
    public static int n;
    public static int k;
    public static int[] arr;

    public static int answer = Integer.MAX_VALUE;
    public static BufferedReader br;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();
        String[] tmp2 = tmp.split(" ");
        n = Integer.parseInt(tmp2[0]);
        k = Integer.parseInt(tmp2[1]);
        String tmp3 = br.readLine();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(tmp3.split(" ")[i]);
        }
        sol(arr, n, k);
        System.out.println(answer);
    }

    private static void sol(int[] arr, int n, int k) {
        for (int i = 0; i < n; i++) {
            int[] res = new int[n];
            res[i] = arr[i];

            boolean  flag = false;
            for (int j = i -1; j >= 0; j--) {
                res[j] = res[j + 1] - k;
                if (res[j] <= 0) {
                    flag = true;
                    break;
                }
            }

            if (!flag) {
                for (int j = i + 1; j < n; j++) {
                    res[j] = res[j - 1] + k;
                }

                int cnt = 0;
                for (int j = 0; j < n; j++) {
                    if (arr[j] != res[j]) {
                        cnt++;
                    }
                }
            answer = Math.min(answer, cnt);
            }
        }
    }
}
