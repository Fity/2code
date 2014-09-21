public class Subset {
    public static void main(String[] args) {
        int k = Integer.parseInt(args[0]);
        RandomizedQueue<String> rq = new RandomizedQueue<>();

        for (String s : StdIn.readAllStrings()) {
            rq.enqueue(s);
        }
        for (int i = 0; i < k; i++) {
            String string = rq.dequeue();
            StdOut.println(string);
        }
    }
}
