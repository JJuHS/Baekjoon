import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static int tc;
    public static int n;
    public static int l;
    public static int[] arr;

    public static int minTime;
    public static int maxTime;

    public static BufferedReader br;
    public static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        int tc = Integer.parseInt(st.nextToken());
        for (int t = 0; t < tc; t++) {
            st = new StringTokenizer(br.readLine());
            l = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());

            arr = new int[n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                arr[i] = Integer.parseInt(st.nextToken());
            }
            sol(n, l, arr);
        }
    }

    public static void sol(int n, int l, int[] arr) {
        minTime = Integer.MIN_VALUE;
        maxTime = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            int minTmpTime = Math.min(arr[i], l - arr[i]);
            int maxTmpTime = Math.max(arr[i], l - arr[i]);

            minTime = Math.max(minTmpTime, minTime);
            maxTime = Math.max(maxTmpTime, maxTime);
        }
        System.out.println(minTime + " " + maxTime);
    }
}
