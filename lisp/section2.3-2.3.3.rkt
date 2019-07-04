#lang racket

(define (count-leaves tree)
  (cond ((null? tree) 0)
        ((not (pair? tree)) 1)
        (else (+ (count-leaves (car tree))
                 (count-leaves (cdr tree))))))

(define (memq item x)
  (cond ((null? x) #f)
        ((eq? item (car x)) x)
        (else (memq item (cdr x)))))

(define (equal? list1 list2)
  (cond ((and (null? list1) (null? list2) #t))
        ((eq? (car list1) (car list2)) (equal? (cdr list1) (cdr list2)))
        ((pair? (car list1)) (equal? (append (car list1) (cdr list1)) list1))
        ((pair? (car list2)) (equal? list1 (append (car list2) (cdr list2))))
        (else #f)))

(define (deriv exp var)
  (cond ((number? exp) 0)
        ((variable? exp)
         (if (same-variable? exp var) 1 0))
        ((sum? exp)
         (make-sum (deriv (addend exp) var)
                   (deriv (augend exp) var)))
        ((product? exp)
         (make-sum
          (make-product (multiplier exp)
                        (deriv (multiplicand exp) var))
          (make-product (multiplicand exp)
                        (deriv (multiplier exp) var))))
        ((exponent? exp)
         (make-product (exponent exp)
                       (make-product (make-exponent (base exp) (- (exponent exp) 1))
                                     (deriv (base exp) var))))
        (else
         (error "unknown expression type -- DERIV" exp))))

(define (variable? x) (symbol? x))

(define (=number? exp num)
  (and (number? exp) (= exp num)))

(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list a1 '+ a2))))

(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list m1 '* m2))))

(define (sum? x)
  (and (pair? x) (eq? (cadr x) '+)))

(define (addend s) (car s))
(define (augend2 s) (caddr s))

(define (product? x)
  (and (pair? x) (eq? (cadr x) '*)))

(define (multiplier p) (car p))
(define (multiplicand2 p) (caddr p))

(define (make-exponent b x)
  (cond ((=number? x 1) b)
        ((=number? x 0) 1)
        (else (list '** b x))))

(define (exponent? e)
  (and (pair? e) (eq? (car e) '**)))

(define (base e) (cadr e))
(define (exponent e) (caddr e))

(define (augend s)    
  (accumulate make-sum 0 (cddr s))) 
  
(define (multiplicand p)  
  (accumulate make-product 1 (cddr  p)))

(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))

(define (1element-of-set? x set)
  (cond ((null? set) #f)
        ((eq? x (car set)) #t)
        (else (1element-of-set? x (cdr set)))))

(define (1adjoin-set x set)
  (if (1element-of-set? x set)
      set
      (cons x set)))

(define (1intersection-set set1 set2)
  (cond ((or (null? set1) (null? set2)) '())
        ((1element-of-set? (car set1) set2)
         (cons (car set1)
               (1intersection-set (cdr set1) set2)))
        (else (1intersection-set (cdr set1) set2))))

(define (1union-set set1 set2)
  (cond ((null? set1) set2)
        ((null? set2) set1)
        ((1element-of-set? (car set1) set2)
         (1union-set (cdr set1) set2))
        (else (cons (car set1)
                    (1union-set (cdr set1) set2)))))

(define (delement-of-set? x set)
  (cond ((null? set) #f)
        ((eq? x (car set)) #t)
        (else (delement-of-set? x (cdr set)))))

(define (dadjoin-set x set)
  (cons x set))

(define (dunion-set set1 set2)
  (append set1 set2))

(define (dintersection-set set1 set2)
  (cond ((or (null? set1) (null? set2)) '())
        ((delement-of-set? (car set1) set2)
         (cons (car set1)
               (dintersection-set (cdr set1) set2)))
        (else (dintersection-set (cdr set1) set2))))

(define (element-of-set? x set)
  (cond ((null? set) #f)
        ((= x (car set)) #t)
        ((< x (car set)) #f)
        (else (element-of-set? x (cdr set)))))

(define (intersection-set set1 set2)
  (if (or (null? set1) (null? set2))
      '()
      (let ((x1 (car set1)) (x2 (car set2)))
        (cond ((= x1 x2)
               (cons x1
                     (intersection-set (cdr set1)
                                       (cdr set2))))
              ((< x1 x2)
               (intersection-set (cdr set1) set2))
              ((> x1 x2)
               (intersection-set set1 (cdr set2)))))))

(define (adjoin-set x set)
  (define (iter before item after)
    (cond ((null? after) (append before (list item)))
          ((> item (car after)) (iter (append before (list (car after))) item (cdr after)))
          ((< item (car after)) (append (append before (list item)) after))))
  (if (element-of-set? x set)
      set
      (iter '() x set)))

(define (union-set set1 set2)
  (cond ((null? set1) set2)
        ((null? set2) set1)
        (else (let ((x1 (car set1)) (x2 (car set2)))
                (cond ((= x1 x2) (cons x1
                                       (union-set (cdr set1) (cdr set2))))
                      ((< x1 x2) (cons x1
                                       (union-set (cdr set1) set2)))
                      ((> x1 x2) (cons x2
                                       (union-set set1 (cdr set2)))))))))

(define (entry tree) (car tree))

(define (left-branch tree) (cadr tree))

(define (right-branch tree) (caddr tree))

(define (make-tree entry left right)
  (list entry left right))

(define (telement-of-set? x set)
  (cond ((null? set) #f)
        ((= x (entry set)) #t)
        ((< x (entry set))
         (telement-of-set? x (left-branch set)))
        ((> x (entry set))
         (telement-of-set? x (right-branch set)))))

(define (tadjoin-set x set)
  (cond ((null? set) (make-tree x '() '()))
        ((= x (entry set)) set)
        ((< x (entry set))
         (make-tree (entry set)
                     (tadjoin-set x (left-branch set))
                     (right-branch set)))
        ((> x (entry set))
         (make-tree (entry set)
                     (left-branch set)
                     (tadjoin-set x (right-branch set))))))

(define (tree->list-1 tree)
  (if (null? tree)
      '()
      (append (tree->list-1 (left-branch tree))
              (cons (entry tree)
                    (tree->list-1 (right-branch tree))))))

(define (tree->list-2 tree)
  (define (copy-to-list tree result-list)
    (if (null? tree)
        result-list
        (copy-to-list (left-branch tree)
                      (cons (entry tree)
                            (copy-to-list (right-branch tree)
                                          result-list)))))
  (copy-to-list tree '()))

(define (list->tree elements)
  (car (partial-tree elements (length elements))))

(define (partial-tree elts n)
  (if (= n 0)
      (cons '() elts)
      (let ((left-size (quotient (- n 1) 2)))
        (let ((left-result (partial-tree elts left-size)))
          (let ((left-tree (car left-result))
                (non-left-elts (cdr left-result))
                (right-size (- n (+ left-size 1))))
            (let ((this-entry (car non-left-elts))
                  (right-result (partial-tree (cdr non-left-elts)
                                              right-size)))
              (let ((right-tree (car right-result))
                    (remaining-elts (cdr right-result)))
                (cons (make-tree this-entry left-tree right-tree)
                      remaining-elts))))))))

(define (unlookup given-key set-of-records)
  (cond ((null? set-of-records) #f)
        ((equal? given-key (key (car set-of-records)))
         (car set-of-records))
        (else (unlookup given-key (cdr set-of-records)))))

(define (lookup given-key tree-of-records)
  (cond? ((null? (entry tree-of-records)) #f)
         ((equal? given-key (key (entry set-of-records)))
          (entry set-of-records))
         ((< given-key (key (entry set-of-records)))
          (lookup given-key (left-branch tree-of-records)))
         ((> given-key (key (entry set-of-records)))
          (lookup given-key (right-branch set-of-records)))))