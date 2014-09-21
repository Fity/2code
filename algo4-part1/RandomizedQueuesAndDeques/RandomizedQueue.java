import java.util.Iterator;
import java.util.NoSuchElementException;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private int size = 0;
    private Item[] itemList;
    private int capacity = 20;

    public RandomizedQueue() {
        // construct an empty randomized queue
        size = 0;
        capacity = 20;
        itemList = (Item[]) new Object[capacity];
    }

    public boolean isEmpty() {
        // is the queue empty?
        return (size == 0);
    }

    public int size() {
        // return the number of items on the queue
        return size;
    }

    public void enqueue(Item item) {
        // add the item
        if (item == null) {
            throw new NullPointerException();
        }
        if (size == capacity) {
            // full
            capacity *= 2;
            Item[] newList = (Item[]) new Object[capacity];
            for (int i = 0; i < size; i++) {
                newList[i] = itemList[i];
                itemList[i] = null;
            }
            itemList = newList;
        }
        itemList[size] = item;
        size++;
    }

    public Item dequeue() {
        // delete and return a random item
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        int index = StdRandom.uniform(0, size);
        Item item = itemList[index];
        itemList[index] = itemList[size - 1];
        itemList[size - 1] = null;
        size--;
        if (size < (capacity / 2)) {
            capacity /= 2;
            Item[] newList = (Item[]) new Object[capacity];
            for (int i = 0; i < size; i++) {
                newList[i] = itemList[i];
                itemList[i] = null;
            }
            itemList = newList;
        }
        return item;
    }

    public Item sample() {
        // return (but do not delete) a random item
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        int index = StdRandom.uniform(0, size);
        Item item = itemList[index];
        return item;
    }

    private class MyRQueueIterator implements Iterator<Item> {
        private int index = 0;
        private int[] order = null;

        public MyRQueueIterator() {
            index = 0;
            order = new int[size];
            for (int i = 0; i < size; i++) {
                order[i] = i;
            }
            StdRandom.shuffle(order);
        }

        @Override
        public boolean hasNext() {
            return (index != order.length);
        }

        @Override
        public Item next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            Item item = itemList[order[index]];
            index++;
            return item;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }

    }

    public Iterator<Item> iterator() {
        // return an independent iterator over items in random order
        return new MyRQueueIterator();
    }

}
