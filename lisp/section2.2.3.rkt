#lang racket

(define nil '())

(define (square x) (* x x))

(define (even? m) (= (remainder m 2) 0))

(define (odd? m) (= (remainder m 2) 1))

(define (inc n) (+ n 1))

(define (prime? n)
  (if (= n 1)
      #f
      (= (smallest-divisor n) n)))

(define (smallest-divisor n)
  (find-divisor n 2))

(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (+ test-divisor 1)))))

(define (divides? a b)
  (= (remainder b a) 0))

(define (fib k)
  (cond ((= k 0) 0)
        ((= k 1) 1)
        (else (+ (fib (- k 1)) (fib (- k 2))))))

(define (sum-odd-squares tree)
  (cond ((null tree) 0)
        ((not (pair? tree))
         (if (odd? tree) (square tree) 0))
        (else (+ (sum-odd-squares (car tree))
                 (sum-odd-squares (cdr tree))))))

(define (even-fibs n)
  (define (next k)
    (if (> k n)
        '()
        (let ((f (fib k)))
          (if (even? f)
              (cons f (next (+ k 1)))
              (next (+ k 1))))))
  (next 0))

(define (filter predicate sequence)
  (cond ((null? sequence) '())
        ((predicate (car sequence))
         (cons (car sequence)
               (filter predicate (cdr sequence))))
        (else (filter predicate (cdr sequence)))))

(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))

(define (enumerate-interval low high)
  (if (> low high)
      '()
      (cons low (enumerate-interval (+ low 1) high))))

(define (enumerate-tree tree)
  (cond ((null? tree) tree)
        ((not (pair? tree)) (list tree))
        (else (append (enumerate-tree (car tree))
                      (enumerate-tree (cdr tree))))))

(define (fold-left op init seq)
  (define (iter result rest)
    (if (null? rest)
        result
        (iter (op result (car rest))
                  (cdr rest))))
  (iter init seq))

(define (reverse sequence)
  (accumulate (lambda (x y)
                (enumerate-tree (list y x)))
              nil sequence))

(define (reverse2 sequence)
  (fold-left (lambda (x y)
               (enumerate-tree (list y x)))
             nil sequence))

(define (sum-odd-squares2 tree)
  (accumulate +
              0
              (map square
                   (filter odd?
                           (enumerate-tree tree)))))

(define (even-fibs2 n)
  (accumulate cons
              '()
              (filter even?
                      (map fib
                           (enumerate-interval 0 n)))))

(define (list-fib-squares n)
  (accumulate cons
              '()
              (map square
                   (map fib
                        (enumerate-interval 0 n)))))

(define (product-of-squares-of-odd-elements sequence)
  (accumulate *
              1
              (map square
                   (filter odd? sequence))))

(define (map2 p sequence)
  (accumulate (lambda (x y)
                (cons (if (not (pair? x))
                          (p x)
                          (map p x))
                      y))
              '() sequence))

(define (append seq1 seq2)
  (accumulate cons seq2 seq1))

(define (length sequence)
  (accumulate (lambda (x y)
                (+ (if (not (pair? x))
                       1
                       (length sequence))
                   y))
              0 sequence))

(define (horner-eval x coefficient-sequence)
  (accumulate (lambda (this-coeff higher-terms)
                (if (not (pair? this-coeff))
                    (+ this-coeff (* higher-terms x))
                    (horner-eval x (cdr coefficient-sequence))))
              0
              coefficient-sequence))

(define (count-leavesfail t)
  (accumulate + 0 (map (lambda (x)
                         (if (pair? x)
                             (count-leaves x)
                             1))
                       t)))

(define s (list (list 1 2 3) (list 4 5 6) (list 7 8 9) (list 10 11 12)))

(define s1 (list (list 1 2) (list 3 4)))

(define (count-leaves tree)
  (cond ((null? tree) 0)
        ((not (pair? tree)) 1)
        (else (+ (count-leaves (car tree))
                 (count-leaves (cdr tree))))))

(define (accumulate-n op init seqs)
  (if (null? (car seqs))
      '()
      (cons (accumulate op init (if (pair? (car seqs))
                                    (map car seqs)
                                    seqs))
            (accumulate-n op init (if (pair? (car seqs))
                                      (if (pair? (map cdr seqs))
                                          (if (= (count-leaves (car (map cdr seqs))) 1)
                                              (map car (map cdr seqs))
                                              (map cdr seqs))
                                          seqs)
                                      (list '()))))))

(define m1 (list (list 1 4 7)
                 (list 2 5 8)
                 (list 3 6 9)))

(define m2 (list (list 1 2)
                 (list 3 4)))

(define m3 (list (list 5 6)
                 (list 7 8)))

(define (dot-product v w)
  (accumulate + 0 (map * v w)))

(define (matrix-*-vector m v)
  (map (lambda (r) (dot-product r v))
       m))

(define (transpose mat)
  (accumulate-n cons '() mat))

(define (matrix-*-matrix m n)
  (let ((cols (transpose n)))
    (map (lambda (m-row)
           (matrix-*-vector cols m-row))
         m)))

(define (thing n) (accumulate append
                          nil
                          (map (lambda (i)
                                 (map (lambda (j) (list i j))
                                      (enumerate-interval 1 (- i 1))))
                               (enumerate-interval 1 n))))

(define (flatmap proc seq)
  (accumulate append nil (map proc seq)))

(define (prime-sum? pair)
  (prime? (+ (car pair) (cadr pair))))

(define (make-pair-sum pair)
  (list (car pair) (cadr pair) (+ (car pair) (cadr pair))))

(define (prime-sum-pairs n)
  (map make-pair-sum
       (filter prime-sum? (unique-pairs n))))

(define (permutations s)
  (if (null? s)
      (list nil)
      (flatmap (lambda (x)
                 (map (lambda (p) (cons x p))
                      (permutations (remove x s))))
               s)))

(define (removedef item sequence)
  (filter (lambda (x) (not (= x item)))
          sequence))

(define (unique-pairs n)
  (accumulate append nil (map (lambda (i)
                                (map (lambda (j) (list i j))
                                     (enumerate-interval 1 (- i 1))))
                              (enumerate-interval 1 n))))

(define (triples n)
  (flatmap (lambda (i)
             (flatmap (lambda (j)
                    (map (lambda (k) (list i j k))
                         (enumerate-interval 1 n)))
                  (enumerate-interval 1 n)))
           (enumerate-interval 1 n)))

(define (check-sum s triples)
  (filter (lambda (triple) (= s (+ (car triple) (cadr triple) (caddr triple)))) triples))

(define (distinct triples)
  (filter (lambda (triple) (and (not (= (car triple) (cadr triple)))
                                (not (= (car triple) (caddr triple)))
                                (not (= (cadr triple) (caddr triple))))) triples))

(define (triple-sum sum n)
  (check-sum sum (distinct (triples n))))

(define (queensfailed board-size)
  (define (queen-cols k)
    (if (= k 0)
        (list (empty-board board-size))
        (filter
         (lambda (positions) (safe? k positions))
         (flatmap
          (lambda (rest-of-queens)
            (map (lambda (new-row)
                   (adjoin-position new-row board-size rest-of-queens))
                 (enumerate-interval 1 board-size)))
          (queen-cols (- k 1))))))
  (queen-cols board-size))

(define (empty-board n)
  (define (iter count result)
    (if (= count n)
        result
        (iter (+ count 1) (append result (list 0)))))
  (iter 0 nil))

(define (adjoin-position new-row k rest-of-queens)
  (define (iter count result)
    (cond ((> count k) result)
          ((= count new-row) (iter (+ count 1) (append result (list 1))))
          (else (iter (+ count 1) (append result (list 0))))))
  (iter 1 nil))

(define (pos item list)
  (define (iter count list)
    (if (= (car list) item)
        count
        (iter (+ count 1) (cdr list))))
  (iter 1 list))

(define (item-at-pos pos list)
  (define (iter count list)
    (if (= count pos)
        (car list)
        (iter (+ count 1) (cdr list))))
  (iter 1 list))

(define (safe? k positions)
  (let ((new-queen (pos 1 (if (pair? (item-at-pos k positions))
                              (item-at-pos k positions)
                              (list (item-at-pos k positions))))))
    (define (iter new-queen count)
      (cond ((= count k) #t)
            ((= new-queen (pos 1 (item-at-pos count positions))) #f)
            (else (iter new-queen (+ count 1)))))
    (iter new-queen 1)))