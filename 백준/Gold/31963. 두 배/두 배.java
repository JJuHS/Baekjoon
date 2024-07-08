import java.io.*;
import java.util.*;

public class Main {
    public static int n, res;
    public static int[] arr;

    public static BufferedReader br;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        String s = br.readLine();

        for (int i = 0; i < n; i++) {
            arr[i] = s.charAt(2 * i) - '0';
        }

        System.out.println(sol(arr, n));
    }

    private static int sol(int[] arr, int n) {
        int[] cnt_arr = new int[n];
        for (int i = 1; i < n ; i++) {
            int ratio = (int) (Math.ceil(Math.log(arr[i - 1] / arr[i])) + cnt_arr[i - 1]);
            if (ratio > 0) {
                cnt_arr[i] = Math.max(0, ratio);
                res += cnt_arr[i];
            }
        }
        return res;
    }
}
