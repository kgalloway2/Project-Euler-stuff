#lang racket
(define (list-ref items n)
  (if (null? items)
      '()
      (if (= n 0)
          (car items)
          (list-ref (cdr items) (- n 1)))))

(define squares (list 1 4 9 16 25))

(define odds (list 1 3 5 7))

(define (even? m) (= (remainder m 2) 0))

(define (odd? m) (= (remainder m 2) 1))

(define (square x) (* x x))

(define (abs x)
  (if (< x 0)
      (- x)
      x))

(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

(define (length2 items)
  (define (length-iter a count)
    (if (null? a)
        count
        (length-iter (cdr a) (+ count 1))))
  (length-iter items 0))

(define (append list1 list2)
  (if (null? list1)
      list2
      (cons (car list1) (append (cdr list1) list2))))

(define (last-pair list)
  (list-ref list (- (length list) 1)))

(define (reverse items)
  (define (rev-iter items)
    (if (= (length items) 1)
        items
        (cons (last-pair items) (rev-iter (all-but-last items)))))
  (rev-iter items))

(define (reverse2 items)
  (if (null? items)
      items
      (cons (last-pair items) (reverse2 (cdr items)))))

(define (all-but-last items)
  (define (last-iter items)
    (if (= (length items) 2)
        (list (car items))
        (cons (car items) (last-iter (cdr items)))))
  (last-iter items))

(define (same-parity x . y)
  (let ((parity (remainder x 2)))
    (define (par-iter items parity)
      (if (null? items)
          items
          (if (= parity (remainder (car items) 2))
              (cons (car items) (par-iter (cdr items) parity))
              (par-iter (cdr items) parity))))
    (cons x (par-iter y parity))))

(define (scale-list items factor)
  (if (null? items)
      items
      (cons (* (car items) factor)
            (scale-list (cdr items) factor))))

(define (scale-list2 items factor)
  (map (lambda (x) (* x factor))
       items))

(define (map2 proc items)
  (if (null? items)
      items
      (cons (proc (car items))
            (map proc (cdr items)))))

(define (square-list1 items)
  (if (null? items)
      items
      (cons (square (car items))
            (square-list1 (cdr items)))))

(define (square-list2 items)
  (map square items))

(define (square-list3 items)
  (define (iter things answer)
    (if (null? things)
        answer
        (iter (cdr things)
              (cons (square (car things))
                    answer))))
  (iter items '()))

(define (square-list4 items)
  (define (iter things answer)
    (if (null? things)
        answer
        (iter (cdr things)
              (cons answer
                    (square (car things))))))
  (iter items '()))

(define (list-even? items)
  (for-each (lambda (x)
              (if (even? x)
                  (display x)
                  (display " ")))
            items))
  