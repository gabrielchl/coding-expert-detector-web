import java.util.Arrays;

public class Test {
    private static int runTest(int[] p, int[] y) {
        int[] realy = Solution.permutationEquation(p);
        System.out.println("Test case: " + Arrays.toString(p));
        System.out.println("Expected: " + Arrays.toString(y));
        System.out.println("Your output: " + Arrays.toString(realy));
        if (Arrays.equals(y, realy)) {
            System.out.println("✔ PASS\n");
            return 1;
        } else {
            System.out.println("✘ FAIL\n");
            return 0;
        }
    }

    public static void main(String[] args) {
        runTest(new int[] {5,2,1,3,4}, new int[] {4,2,5,1,3});
        runTest(new int[] {1}, new int[] {1});
        runTest(new int[] {3,1,5,2,4}, new int[] {4,5,2,3,1});
        runTest(new int[] {1,2,3,4,5}, new int[] {1,2,3,4,5});
        runTest(new int[] {3,6,4,5,2,1}, new int[] {2,4,6,1,3,5});
    }
}
