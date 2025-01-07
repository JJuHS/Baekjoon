import java.io.*;
import java.util.*;

public class Main {

    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        LinkedList arr = new LinkedList();
        int target = -1;

        while (st.hasMoreTokens()) {
            int number = Integer.parseInt(st.nextToken());
            arr.add(target, number);
            target = number;
        }

        while (m-- > 0) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            int i = Integer.parseInt(st.nextToken());
            int j = st.hasMoreTokens() ? Integer.parseInt(st.nextToken()) : -1;

            switch (command) {
                case "BN":
                    arr.print(arr.next[i]);
                    arr.add(i, j);
                    break;
                case "BP":
                    arr.print(arr.prev[i]);
                    arr.add(arr.prev[i], j);
                    break;
                case "CN":
                    arr.print(arr.next[i]);
                    arr.delete(arr.next[i]);
                    break;
                default:
                    arr.print(arr.prev[i]);
                    arr.delete(arr.prev[i]);
            }
        }

        System.out.print(sb.toString());
    }

    static class LinkedList {
        int[] prev;
        int[] next;

        LinkedList() {
            prev = new int[1000001];
            next = new int[1000001];
        }

        void add(int target, int node) {
            if (target == -1) {
                prev[node] = next[node] = node;
            } else {
                prev[node] = target;
                next[node] = next[target];
                prev[next[target]] = node;
                next[target] = node;
            }
        }

        void delete(int target) {
            prev[next[target]] = prev[target];
            next[prev[target]] = next[target];
        }

        void print(int num) {
            sb.append(num).append("\n");
        }
    }
}
