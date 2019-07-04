#lang racket

(define (cons x y)
  (define (set-x! v) (set! x v))
  (define (set-y! v) (set! y x))
  (define (dispatch m)
  (cond ((eq? m 'car) x)
        ((eq? m 'cdr) y)
        ((eq? m 'set-car!) set-x!)
        ((eq? m 'set-cdr!) set-y!)
        (else (error "Undefined operation -- CONS" m))))
  dispatch)

(define (car z) (z 'car))
(define (cdr z) (z 'cdr))

(define (set-car! z new-value)
  ((z 'set-car!) new-value)
  z)

(define (set-cdr! z new-value)
  ((z 'set-cdr!) new-value)
  z)

(define (front-ptr queue) (car queue))

(define (rear-ptr queue) (cdr queue))

(define (set-front-ptr! queue item) (set-car! queue item))

(define (set-rear-ptr! queue item) (set-cdr! queue item))

(define (empty-queue? queue) (null? (front-ptr queue)))

(define (make-queue) (cons '() '()))

(define (front-queue queue)
  (if (empty-queue? queue)
      (error "FRONT called with an empty queue" queue)
      (car (front-ptr queue))))

(define (insert-queue! queue item)
  (let ((new-pair (cons item '())))
    (cond ((empty-queue? queue)
           (set-front-ptr! queue new-pair)
           (set-rear-ptr! queue new-pair)
           queue)
          (else
           (set-cdr! (rear-ptr queue) new-pair)
           (set-rear-ptr! queue new-pair)
           queue))))

(define (delete-queue! queue)
  (cond ((empty-queue? queue)
         (error "DELETE! called with an empty queue" queue))
        (else
         (set-front-ptr! queue (cdr (front-ptr queue)))
         queue)))

(define (print-queue queue)
  (display (front-ptr queue)))

(define (make-queue2)
  (let ((front-ptr '()))
    (let ((rear-ptr (last-pair front-ptr)))
     (define (empty-queue? queue) (null? front-ptr))
     (define (front-queue queue)
       (if (empty-queue? queue)
           (error "FRONT called with an empty list" queue)
           (car front-ptr)))
     (define (insert-queue! queue item)
       (if (empty-queue? queue)
           (set! front-ptr (list item))
           (set! front-ptr (append front-ptr (list item)))))
     (define (delete-queue! queue item)
       (if (empty-queue? queue)
           (error "DELETE! called with an empty queue" queue)
           (set! front-ptr (cdr front-ptr))))
      (define (print-queue) (display front-ptr))
     (define (dispatch m)
       (cond ((eq? m 'front-queue) front-queue)
             ((eq? m 'insert-queue!) insert-queue!)
             ((eq? m 'delete-queue!) delete-queue!)
             ((eq? m 'print-queue) print-queue)
             (else (error "Undefined operation -- MAKE-QUEUE" m))))
     dispatch)))

(define (last-pair items)
  (cond ((null? items) 0)
        (else
         (if (= (length items) 1)
             items
             (last-pair (cdr items))))))

(define (make-deque) (cons '() '()))

(define (empty-deque? deque) (null? (front-ptr deque)))

(define (front-deque deque) (car deque))
(define (rear-deque deque) (cdr deque))
(define (set-front-ptr-deque! deque item) (set-car! deque item))
(define (set-rear-ptr-deque! deque item) (set-cdr! deque item))

(define (front-insert-deque! deque item)
  (set-front-ptr-deque! deque (cons item (front-deque deque))))

(define (rear-insert-deque! deque item)
  (set-front-ptr-deque! deque (cons (front-deque deque) (rear-deque deque)))
  (set-rear-ptr-deque! deque item))

(define (front-delete-deque! deque)
  (set-front-ptr-deque! deque (cdr (front-deque deque))))

(define (rear-delete-deque! deque)
  (set-rear-ptr-deque! deque (last-pair deque))
  (set-front-ptr-deque! deque (all-but-last-pair deque)))