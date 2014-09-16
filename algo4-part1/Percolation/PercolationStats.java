public class PercolationStats {
    private double threshold;
    private double deviation;
    private double confidenceLo;
    private double confidenceHi;

    public PercolationStats(int N, int T) {
        // perform T independent computational experiments on an N-by-N grid
        if (N <= 0 || T <= 0)
            throw new java.lang.IllegalArgumentException("illegal argument.");
        double[] fraction = new double[T];
        for (int t = 0; t < T; t++) {
            int openCount = 0;
            Percolation p = new Percolation(N);
            int[] gids = new int[N * N + 1];
            for (int i = 1; i <= N * N; i++) {
                gids[i] = i;
            }
            while (!p.percolates()) {
                int blockedCount = N * N - openCount;
                int i = StdRandom.uniform(1, blockedCount + 1);
                int x = 0, y = 0;
                if (gids[i] % N == 0) {
                    x = gids[i] / N;
                    y = N;
                } else {
                    x = gids[i] / N + 1;
                    y = gids[i] % N;
                }
                p.open(x, y);
                openCount++;
                gids[i] = gids[blockedCount];
            }
            fraction[t] = openCount / (double) (N * N);
        }
        threshold = StdStats.mean(fraction);
        deviation = StdStats.stddev(fraction);
        confidenceLo = threshold - 1.96 * deviation / Math.sqrt((double) T);
        confidenceHi = threshold + 1.96 * deviation / Math.sqrt((double) T);
    }

    public double mean() {
        // sample mean of percolation threshold
        return this.threshold;
    }

    public double stddev() {
        // sample standard deviation of percolation threshold
        return this.deviation;
    }

    public double confidenceLo() {
        // returns lower bound of the 95% confidence interval
        return this.confidenceLo;
    }

    public double confidenceHi() {
        // returns upper bound of the 95% confidence interval
        return this.confidenceHi;
    }

    public static void main(String[] args) {
        // test client, described below
        int N = Integer.parseInt(args[1]);
        int T = Integer.parseInt(args[2]);

        PercolationStats stats = new PercolationStats(N, T);
        StdOut.println(String.format("mean                    = %f",
                stats.mean()));
        StdOut.println(String.format("stddev                  = %.16f",
                stats.stddev()));
        StdOut.println(String.format("95%% confidence interval = %.16f, %.16f",
                stats.confidenceLo(), stats.confidenceHi()));
    }
}
