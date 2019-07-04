#lang racket
(define (count-leaves x)
    (cond ((null? x) 0)
          ((not (pair? x)) 1)
          (else (+ (count-leaves (car x))
                   (count-leaves (cdr x))))))

(define (list-ref items n)
  (if (null? items)
      '()
      (if (= n 0)
          (car items)
          (list-ref (cdr items) (- n 1)))))

(define (even? m) (= (remainder m 2) 0))

(define (odd? m) (= (remainder m 2) 1))

(define (square x) (* x x))

(define (inc x) (+ x 1))

(define (abs x)
  (if (< x 0)
      (- x)
      x))

(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

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

(define (deep-reverse items)
  (define (rev-iter items)
    (if (< (count-leaves items) 3)
        (list (reverse (car items)))
        (cons (reverse (last-pair items)) (rev-iter (all-but-last items)))))
  (rev-iter items))

(define (all-but-last items)
  (define (last-iter items)
    (cond ((= (length items) 1) items)
          ((= (length items) 2) (list (car items)))
          (else (cons (car items) (last-iter (cdr items))))))
  (last-iter items))

(define (fringe L)
  (define (fringe-iter L)
    (if (= 1 (count-leaves L))
        (list L)
        (cons (cond ((= (count-leaves (car L)) 1) (car L))
                    (else (fringe (car L))))
              (fringe-iter (car (cdr L))))))
  (fringe-iter L))

(define x (list 1 (list 2 (list 3 4))))

(define (make-mobile left right)
  (list left right))

(define (make-branch length structure)
  (list length structure))

(define (left-branch mobile)
  (car mobile))

(define (right-branch mobile)
  (cdr mobile))

(define (branch-length branch)
  (car branch))

(define (branch-structure branch)
  (cdr branch))

(define (total-weight mobile)
  (define (iter mobile)
    (if (= (count-leaves mobile) 4)
        (+ (car (cdr (left-branch mobile))) (car (cdr (car (right-branch mobile)))))
        (+ (iter (left-branch mobile)) (iter (right-branch mobile)))))
  (iter mobile))

(define (scale-tree tree factor)
  (cond ((null? tree) tree)
        ((not (pair? tree)) (* tree factor))
        (else (cons (scale-tree (car tree) factor)
                    (scale-tree (cdr tree) factor)))))

(define (scale-tree2 tree factor)
  (map (lambda (sub-tree)
         (if (pair? sub-tree)
             (scale-tree sub-tree factor)
             (* sub-tree factor)))
       tree))

(define (square-tree-map tree)
  (map (lambda (sub-tree)
         (if (pair? sub-tree)
             (square-tree-map sub-tree)
             (square sub-tree)))
       tree))

(define (tree-map oper tree)
  (map (lambda (sub-tree)
         (if (pair? sub-tree)
             (tree-map oper sub-tree)
             (oper sub-tree)))
       tree))

(define (subsets s)
  (if (null? s)
      (list s)
      (let ((rest (subsets (cdr s))))
        (append rest (map (lambda (x)
                            (cons (car s) x))
                          rest)))))
