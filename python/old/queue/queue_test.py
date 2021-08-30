#!python

from queue import Queue
import unittest


class QueueTest(unittest.TestCase):

    def test_init(self):
        q = Queue()
        assert q.front() is None
        assert q.queue.size == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = Queue(['A', 'B', 'C'])
        assert q.front() == 'A'
        assert q.queue.size == 3
        assert q.is_empty() is False

    def test_size(self):
        q = Queue()
        assert q.queue.size == 0
        q.enqueue('A')
        assert q.queue.size == 1
        q.enqueue('B')
        assert q.queue.size == 2
        q.dequeue()
        assert q.queue.size == 1
        q.dequeue()
        assert q.queue.size == 0

    def test_enqueue(self):
        q = Queue()
        q.enqueue('A')
        assert q.front() == 'A'
        assert q.queue.size == 1
        q.enqueue('B')
        assert q.front() == 'A'
        assert q.queue.size == 2
        q.enqueue('C')
        assert q.front() == 'A'
        assert q.queue.size == 3
        assert q.is_empty() is False

    def test_front(self):
        q = Queue()
        assert q.front() is None
        q.enqueue('A')
        assert q.front() == 'A'
        q.enqueue('B')
        assert q.front() == 'A'
        q.dequeue()
        assert q.front() == 'B'
        q.dequeue()
        assert q.front() is None

    def test_dequeue(self):
        q = Queue(['A', 'B', 'C'])
        assert q.dequeue() == 'A'
        assert q.queue.size == 2
        assert q.dequeue() == 'B'
        assert q.queue.size == 1
        assert q.dequeue() == 'C'
        assert q.queue.size == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.dequeue()


if __name__ == '__main__':
    unittest.main()
