import java.io.*;
import java.util.*;

public class QueueQues {
    static void mergeSort(int[] array, int[] tmp, PrintWriter out, int from, int until) {
        if (from + 1 < until) {
            int mid = (from + until) >>> 1;
            mergeSort(array, tmp, out, from, mid);
            mergeSort(array, tmp, out, mid, until);
            for (int i = from, j = mid, k = from; k < until; ++k) {
                if (i < mid && (j == until || array[i] <= array[j])) {
                    tmp[k] = array[i++];
                } else {
                    tmp[k] = array[j++];
                }
            }
            System.arraycopy(tmp, from, array, from, until - from);
            out.print(from + 1);
            out.print(" ");
            out.print(until);
            out.print(" ");
            out.print(array[from]);
            out.print(" ");
            out.println(array[until - 1]);
        }
    }

    public static void main(String[] args) throws IOException {
        try (BufferedReader in = new BufferedReader(new FileReader("input.txt"));
             PrintWriter out = new PrintWriter(new FileWriter("output.txt"))) {
            int n = Integer.parseInt(in.readLine());
            StringTokenizer st = new StringTokenizer(in.readLine());
            int[] array = new int[n];
            for (int i = 0; i < n; ++i) {
                array[i] = Integer.parseInt(st.nextToken());
            }
            mergeSort(array, new int[n], out, 0, n);
            for (int i = 0; i < n; ++i) {
                out.print(array[i]);
                if (i + 1 < n) {
                    out.print(" ");
                } else {
                    out.println();
                }
            }
        }
    }
}
