import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Fast {
    public static void main(String[] args) {
        // rescale coordinates and turn on animation mode
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        StdDraw.show(0);

        // read in the input
        String filename = args[0];
        In in = new In(filename);
        int N = in.readInt();

        Point[] points = new Point[N];
        HashMap<Point, Integer> pointMap = new HashMap<>();
        int[][] edges = new int[N][N];
        for (int i = 0; i < N; i++) {
            int x = in.readInt();
            int y = in.readInt();
            Point p = new Point(x, y);
            points[i] = p;
            pointMap.put(p, i);
            p.draw();
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                edges[i][j] = 0;
            }
        }
        for (int i = 0; i < N; i++) {
            swap(points, i, 0);
            Arrays.sort(points, 1, N, points[0].SLOPE_ORDER);
            Point p = points[0];
            int pCount = 0;
            double lastSlope = 1.0;
            List<Point> pList = new ArrayList<Point>();
            for (int j = 1; j < N; j++) {
                double currentSlope = p.slopeTo(points[j]);
                if (j == 1) {
                    pCount = 1;
                    pList.add(p);
                } else if (currentSlope != lastSlope) {
                    if (pCount >= 4) {
                        printLine(pList, pointMap, edges);
                    }
                    pList.clear();
                    pCount = 1;
                    pList.add(p);
                }
                pCount++;
                pList.add(points[j]);
                lastSlope = currentSlope;
            }
            if (pList.size() >= 4) {
                printLine(pList, pointMap, edges);
            }
        }

        // display to screen all at once
        StdDraw.show(0);

        // reset the pen radius
        StdDraw.setPenRadius();
    }

    private static void printLine(List<Point> pList,
            HashMap<Point, Integer> pointMap, int[][] edges) {
        boolean isFirst = true;
        int lastIndex = -1;
        boolean drawed = false;
        for (Point point : pList) {
            if (isFirst) {
                isFirst = false;
                lastIndex = pointMap.get(point);
            } else {
                int currentIndex = pointMap.get(point);
                if (edges[lastIndex][currentIndex] == 0) {
                    edges[lastIndex][currentIndex] = 1;
                    edges[currentIndex][lastIndex] = 1;
                } else {
                    drawed = true;
                    break;
                }
                lastIndex = currentIndex;
            }
        }
        if (!drawed) {
            Point last = null;
            isFirst = true;
            for (Point point : pList) {
                if (isFirst) {
                    isFirst = false;
                    StdOut.printf("%s", point);
                    last = point;
                } else {
                    StdOut.printf(" -> %s", point);
                    last.drawTo(point);
                    last = point;
                }
            }
            StdOut.println();
        }
    }

    private static void swap(Point[] points, int i, int j) {
        Point p = points[i];
        points[i] = points[j];
        points[j] = p;
        return;
    }

}
