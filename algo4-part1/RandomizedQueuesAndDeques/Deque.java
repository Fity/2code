import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
    private int size = 0;
    private Node<Item> first, last;

    public Deque() {
        // construct an empty deque
        first = null;
        last = null;
        size = 0;
    }

    private static class Node<Item> {
        private Item value;
        private Node<Item> next;
        private Node<Item> prev;

        Node(Item item) {
            value = item;
            next = null;
            prev = null;
        }

    }

    public boolean isEmpty() {
        // is the deque empty?
        return (size == 0);
    }

    public int size() {
        // return the number of items on the deque
        return size;
    }

    public void addFirst(Item item) {
        // insert the item at the front
        if (item == null) {
            throw new NullPointerException();
        }
        Node<Item> node = new Node<Item>(item);
        if (isEmpty()) {
            first = node;
            last = node;
        } else {
            node.next = first;
            first.prev = node;
            first = node;
        }
        size++;
    }

    public void addLast(Item item) {
        // insert the item at the end
        if (item == null) {
            throw new NullPointerException();
        }
        Node<Item> node = new Node<Item>(item);
        if (isEmpty()) {
            first = node;
            last = node;
        } else {
            last.next = node;
            node.prev = last;
            last = node;
        }
        size++;
    }

    public Item removeFirst() {
        // delete and return the item at the front
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        Item item = null;
        item = first.value;
        if (size == 1) {
            first = null;
            last = null;
        } else {
            first = first.next;
            first.prev = null;
        }
        size--;
        return item;
    }

    public Item removeLast() {
        // delete and return the item at the end
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        Item item = last.value;
        if (size == 1) {
            first = null;
            last = null;
        } else {
            Node<Item> oldLast = last;
            last = oldLast.prev;
            last.next = null;
            oldLast.prev = null;
        }
        size--;
        return item;
    }

    private class MyDequeIterator implements Iterator<Item> {
        private Node<Item> cur = first;

        public Node<Item> getCur() {
            return cur;
        }

        public void setCur(Node<Item> ncur) {
            this.cur = ncur;
        }

        public boolean hasNext() {
            return (cur != null);
        }

        public Item next() {
            if (cur == null) {
                throw new NoSuchElementException();
            }
            Item item = cur.value;
            cur = cur.next;
            return item;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }

    }

    public Iterator<Item> iterator() {
        // return an iterator over items in order from front to end
        return new MyDequeIterator();
    }
}