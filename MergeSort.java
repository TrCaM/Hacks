import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class MergeSort {

    static class FastScanner {
        static BufferedReader br;
        static StringTokenizer st;

        FastScanner(File f) {
            try {
                br = new BufferedReader(new FileReader(f));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        public FastScanner(InputStream f) {
            br = new BufferedReader(new InputStreamReader(f));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

    static FastScanner newInput() throws IOException {
        if (System.getProperty("JUDGE") != null) {
            return new FastScanner(new File("input.txt"));
        } else {
            return new FastScanner(System.in);
        }
    }

    static PrintWriter newOutput() throws IOException {
        if (System.getProperty("JUDGE") != null) {
            return new PrintWriter("output.txt");
        } else {
            return new PrintWriter(System.out);
        }
    }

    public static void main(String[] args) throws IOException {
        try (PrintWriter out = newOutput()) {
            FastScanner in = newInput();

            int[] mem = new int[in.nextInt()];

            for (int i = 0; i < mem.length; i++) {
                mem[i] = in.nextInt();
            }
            StringBuilder sb = new StringBuilder();
            for (int i: sort(mem,0, mem.length-1, out)
                 ) {
                sb.append(i+ " ");
            }
            out.println(sb.deleteCharAt(sb.length()-1));
        }
    }

    public static int[] sort(int[] array, int li, int ri, PrintWriter output){
        if (li == ri){
            int[] out = {array[li]};
            return out;
        }
        int split = li+ (ri-li)/2;
        int[] left_array = sort(array, li, split, output);
        int[] right_array= sort(array, split+1,ri, output);

        int i= 0;
        int j= 0;
        int[] toReturn = new int[ri-li+1];
        int ind =0;
        while(i<left_array.length || j<right_array.length){
            if(left_array[i]<= right_array[j]){
                toReturn[ind++] = left_array[i++];
            } else{
                toReturn[ind++] = right_array[j++];
            }
            if (i== left_array.length){
                while (j<right_array.length){
                    toReturn[ind++] = right_array[j++];;
                }
                break;
            }
            if (j== right_array.length){
                while (i<left_array.length){
                    toReturn[ind++] = left_array[i++];
                }
                break;
            }
        }
        output.format("%d %d %d %d%n",li+1, ri+1, toReturn[0], toReturn[toReturn.length-1]);
        return toReturn;
    }

}