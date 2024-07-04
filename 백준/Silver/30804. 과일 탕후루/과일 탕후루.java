import java.io.*;

public class Main {
    public static BufferedReader br;

    public static int n;
    public static int[] arr;
    public static int[] cntFruit;

    public static void main(String[] args) throws IOException{
        br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        arr = new int[n];
        cntFruit = new int[10];

        String tmp = br.readLine();
        for (int i = 0; i < n ; i++) {
            arr[i] = tmp.charAt(i << 1) - '0';
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(sol(0, 0, 0, 0, 0)));
        bw.close();
    }

    private static int sol(int left, int right, int cnt, int kind, int max) {
        if (right == n) {
            return max;
        }
        if (cntFruit[arr[right]] == 0) {
            kind++;
        }
        cntFruit[arr[right]]++;
        cnt++;
        if (kind > 2) {
            cntFruit[arr[left]]--;
            cnt--;
            if (cntFruit[arr[left]] == 0) {
                kind--;
            }
            left++;
        }
        max = Math.max(cnt, max);
        return sol(left, right + 1, cnt, kind, max);
    }
}
