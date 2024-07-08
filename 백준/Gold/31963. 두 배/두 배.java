import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // n을 입력 받는다
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        // 배열의 값을 입력 받는다
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // sol 함수를 호출하여 결과를 출력한다
        System.out.println(sol(arr, n));
    }

    // sol 함수는 Python의 sol 함수와 동일한 기능을 수행한다
    public static long sol(int[] arr, int n) {
        long tmp = 0;
        long[] cnt_arr = new long[n];
        for (int i = 1; i < n; i++) {
            // arr[i - 1] / arr[i]의 비율을 구하고 로그를 계산한다
            double ratio = Math.ceil(Math.log(arr[i - 1] / (double)arr[i]) / Math.log(2)) + cnt_arr[i - 1];
            // 비율이 0보다 크면 cnt_arr[i]를 갱신하고 tmp에 더한다
            if (ratio > 0) {
                cnt_arr[i] = Math.max(0, (long)ratio);
                tmp += cnt_arr[i];
            }
        }
        return tmp;
    }
}
