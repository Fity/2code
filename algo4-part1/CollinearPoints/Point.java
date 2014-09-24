/*************************************************************************
 * Name: Fity
 * Email: imfity@gmail.com
 *
 * Compilation:  javac Point.java
 * Execution:
 * Dependencies: StdDraw.java
 *
 * Description: An immutable data type for points in the plane.
 *
 *************************************************************************/

import java.util.Comparator;

public class Point implements Comparable<Point> {

    // compare points by slope
    public final Comparator<Point> SLOPE_ORDER; // YOUR DEFINITION HERE

    private final int x; // x coordinate
    private final int y; // y coordinate

    // create the point (x, y)
    public Point(int x, int y) {
        /* DO NOT MODIFY */
        this.x = x;
        this.y = y;
        this.SLOPE_ORDER = new BySlope(this);
    }

    // plot this point to standard drawing
    public void draw() {
        /* DO NOT MODIFY */
        StdDraw.point(x, y);
    }

    // draw line between this point and that point to standard drawing
    public void drawTo(Point that) {
        /* DO NOT MODIFY */
        StdDraw.line(this.x, this.y, that.x, that.y);
    }

    // slope between this point and that point
    public double slopeTo(Point that) {
        if (that == null)
            throw new NullPointerException();
        double dy = that.y - this.y;
        double dx = that.x - this.x;
        if (this.x == that.x) {
            if (this.y == that.y) {
                return Double.NEGATIVE_INFINITY;
            } else {
                return Double.POSITIVE_INFINITY;
            }
        } else if (this.y == that.y) {
            return 0;
        } else {
            return dy / dx;
        }
    }

    // is this point lexicographically smaller than that one?
    // comparing y-coordinates and breaking ties by x-coordinates
    public int compareTo(Point that) {
        if (this.y > that.y) {
            return 1;
        } else if (this.y < that.y) {
            return -1;
        } else {
            if (this.x > that.x) {
                return 1;
            } else if (this.x < that.x) {
                return -1;
            } else {
                return 0;
            }
        }
    }

    // return string representation of this point
    public String toString() {
        /* DO NOT MODIFY */
        return "(" + x + ", " + y + ")";
    }

    private static class BySlope implements Comparator<Point> {

        private Point base = null;

        public BySlope(Point base) {
            this.base = base;
        }

        @Override
        public int compare(Point p1, Point p2) {
            double slope1 = base.slopeTo(p1);
            double slope2 = base.slopeTo(p2);
            if (slope1 == slope2) {
                return 0;
            }
            if (slope1 > slope2) {
                return 1;
            } else {
                return -1;
            }
        }

    }

    // unit test
    public static void main(String[] args) {
        /* YOUR CODE HERE */
        Point p = new Point(30046, 12471);
        Point a = new Point(3624, 28635);
        Point b = new Point(30046, 6359);
        StdOut.println(p.compareTo(b));
        StdOut.println(p.slopeTo(a));
        StdOut.println(p.slopeTo(b));
    }
}
