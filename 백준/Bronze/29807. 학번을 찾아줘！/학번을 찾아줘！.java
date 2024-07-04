import java.io.*;
import java.util.Arrays;

public class Main {
    public static int T;
    public static int[] arr;
    public static BufferedReader br;
    public static int res;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        String s = br.readLine();
        arr = new int[5];
        for (int i = 0; i <T ; i++) {
            arr[i] = Integer.parseInt(s.split(" ")[i]);
        }
        if (T == 4) {
            arr[4] = 0;
        }
        if (T == 3) {
            arr[3] = 0;
        }
        if (T == 2) {
            arr[2] = 0;
        }
        if (T == 1) {
            arr[1] = 0;
        }
        sol(arr);
    }

    private static void sol(int[] arr) {
        if (arr[0] > arr[2]) {
            res += 508 * (arr[0] - arr[2]);
        } else {
            res += 108 * (arr[2] - arr[0]);
        }

        if (arr[1] > arr[3]) {
            res += 212 * (arr[1] - arr[3]);
        } else {
            res += 305 * (arr[3] - arr[1]);
        }

        res += 707 * arr[4];

        res *= 4763;
        System.out.println(res);
    }
}
