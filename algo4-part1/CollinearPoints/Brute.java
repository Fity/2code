import java.util.Arrays;


public class Brute {

    public static void main(String[] args) {
        // rescale coordinates and turn on animation mode
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        StdDraw.show(0);
//        StdDraw.setPenRadius(0.01); // make the points a bit larger

        // read in the input
        String filename = args[0];
        In in = new In(filename);
        int N = in.readInt();

        Point[] points = new Point[N];
        for (int i = 0; i < N; i++) {
            int x = in.readInt();
            int y = in.readInt();
            Point p = new Point(x, y);
            points[i] = p;
            p.draw();
        }
        Arrays.sort(points);
        for (int i = 0; i < N; i++) {
            Point p = points[i];
            for (int j = i + 1; j < N; j++) {
                double slopej = p.slopeTo(points[j]);
                for (int k = j + 1; k < N; k++) {
                    double slopek = p.slopeTo(points[k]);
                    if (slopej != slopek) {
                        continue;
                    }
                    for (int l = k + 1; l < N; l++) {
                        double slopel = p.slopeTo(points[l]);
                        if (slopek != slopel) {
                            continue;
                        }
                        StdOut.printf("%s -> %s -> %s -> %s\n", p, points[j],
                                points[k], points[l]);
                        p.drawTo(points[j]);
                        points[j].drawTo(points[k]);
                        points[k].drawTo(points[l]);
                    }
                }
            }
        }

        // display to screen all at once
        StdDraw.show(0);

        // reset the pen radius
        StdDraw.setPenRadius();
    }
}