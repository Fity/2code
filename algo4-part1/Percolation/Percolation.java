public class Percolation {
    private static int[] x = { 0, 0, -1, 1 };
    private static int[] y = { -1, 1, 0, 0 };
    private int virtualTop = 0;
    private int virtualBottom;
    private boolean[][] isBlocked;
    private WeightedQuickUnionUF quickUnionData;
    private WeightedQuickUnionUF uf;
    private int N;

    public Percolation(int N) {
        // create N-by-N grid, with all sites blocked
        if (N <= 0) {
            throw new java.lang.IllegalArgumentException("illegal argument.");
        }
        quickUnionData = new WeightedQuickUnionUF(N * N + 2);
        uf = new WeightedQuickUnionUF(N * N + 2);
        isBlocked = new boolean[N + 1][N + 1];
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= N; j++) {
                isBlocked[i][j] = true;
            }
        }
        this.N = N;
        this.virtualBottom = N * N + 1;
    }

    private int getGridIndex(int i, int j) {
        return (i - 1) * this.N + j;
    }

    public void open(int i, int j) {
        // open site (row i, column j) if it is not already
        if (i <= 0 || i > this.N || j <= 0 || j > this.N) {
            throw new IndexOutOfBoundsException("row index i out of bounds");
        }
        if (isBlocked[i][j]) {
            if (i == 1) {
                this.quickUnionData.union(virtualTop, getGridIndex(i, j));
                this.uf.union(virtualTop, getGridIndex(i, j));
            }
            if (i == N) {
                this.quickUnionData.union(virtualBottom, getGridIndex(i, j));
            }
            isBlocked[i][j] = false;
            for (int k = 0; k < 4; k++) {
                int nx = i + x[k];
                int ny = j + y[k];
                if (nx <= 0 || nx > N || ny <= 0 || ny > N || isBlocked[nx][ny]) {
                    continue;
                }
                quickUnionData.union(getGridIndex(i, j), getGridIndex(nx, ny));
                uf.union(getGridIndex(i, j), getGridIndex(nx, ny));
            }
        }
    }

    public boolean isOpen(int i, int j) {
        // is site (row i, column j) open?
        if (i <= 0 || i > this.N || j <= 0 || j > this.N) {
            throw new IndexOutOfBoundsException("row index i out of bounds");
        }
        return !isBlocked[i][j];
    }

    public boolean isFull(int i, int j) {
        // is site (row i, column j) full?
        if (i <= 0 || i > this.N || j <= 0 || j > this.N) {
            throw new IndexOutOfBoundsException("row index i out of bounds");
        }
        return (isOpen(i, j) && uf.connected(virtualTop,
                getGridIndex(i, j)));
    }

    public boolean percolates() {
        // does the system percolate?
        return quickUnionData.connected(virtualTop, virtualBottom);
    }

}
