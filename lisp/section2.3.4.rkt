#lang racket

(define (make-leaf symbol weight)
  (list 'leaf symbol weight))

(define (leaf? object)
  (eq? (car object) 'leaf))

(define (symbol-leaf x) (cadr x))

(define (weight-leaf x) (caddr x))

(define (make-code-tree left right)
  (list left
        right
        (append (symbols left) (symbols right))
        (+ (weight left) (weight right))))

(define (left-branch tree) (car tree))

(define (right-branch tree) (cadr tree))

(define (symbols tree)
  (if (leaf? tree)
      (list (symbol-leaf tree))
      (caddr tree)))

(define (weight tree)
  (if (leaf? tree)
      (weight-leaf tree)
      (cadddr tree)))

(define (decode bits tree)
  (define (decode-1 bits current-branch)
    (if (null? bits)
        '()
        (let ((next-branch
               (choose-branch (car bits) current-branch)))
          (if (leaf? next-branch)
              (cons (symbol-leaf next-branch)
                    (decode-1 (cdr bits) tree))
              (decode-1 (cdr bits) next-branch)))))
  (decode-1 bits tree))

(define (choose-branch bit branch)
  (cond ((= bit 0) (left-branch branch))
        ((= bit 1) (right-branch branch))
        (else (error "bad bit -- CHOOSE-BRANCH" bit))))

(define (adjoin-set x set)
  (cond ((null? set) (list x))
        ((< (weight x) (weight (car set))) (cons x set))
        (else (cons (car set)
                    (adjoin-set x (cdr set))))))

(define (make-leaf-set pairs)
  (if (null? pairs)
      '()
      (let ((pair (car pairs)))
        (adjoin-set (make-leaf (car pair)     ;symbol
                               (cadr pair))   ;frequency
                    (make-leaf-set (cdr pairs))))))

(define (encode-symbol message tree)
  (define (encode-symbol1 message og-tree current-tree)
    (if (null? message)
        '()
        (cond ((not (in-tree? (car message) (symbols current-tree))) (error "symbol not in tree -- ENCODE-SYMBOL" (car message)))
              ((leaf? (right-branch current-tree)) (if (eq? (car message) (symbol-leaf (right-branch current-tree)))
                                                       (cons 1 (encode-symbol1 (cdr message) og-tree og-tree))
                                                       (cons 0 (encode-symbol1 (cdr message) og-tree og-tree))))
              ((leaf? (left-branch current-tree)) (if (eq? (car message) (symbol-leaf (left-branch current-tree)))
                                                      (cons 0 (encode-symbol1 (cdr message) og-tree og-tree))
                                                      (cons 1 (encode-symbol1 message og-tree (right-branch current-tree)))))
              ((in-tree? (car message) (symbols (left-branch current-tree))) (cons 0 (encode-symbol1 message og-tree (left-branch current-tree))))
              ((in-tree? (car message) (symbols (right-branch current-tree))) (cons 1 (encode-symbol1 message og-tree (right-branch current-tree)))))))
  (encode-symbol1 message tree tree))

(define (in-tree? x symbols)
  (cond ((null? symbols) #f)
        ((eq? x (car symbols)) #t)
        (else (in-tree? x (cdr symbols)))))
            
(define sample-tree
  (make-code-tree (make-leaf 'A 4)
                  (make-code-tree
                   (make-leaf 'B 2)
                   (make-code-tree (make-leaf 'D 1)
                                   (make-leaf 'C 1)))))

(define sample-message '(0 1 1 0 0 1 0 1 0 1 1 1 0))

(define sample-message2 '(A D A B B C A))

(define sample-freq (list '(D 1) '(B 2) '(A 4) '(C 1)))

(define rock-freq (list '(A 2) '(BOOM 1) '(GET 2) '(JOB 2) '(NA 16) '(SHA 3) '(YIP 9) '(WAH 1)))

(define rock-message '(GET A JOB SHA NA NA NA NA NA NA NA NA GET A JOB SHA NA NA NA NA NA NA NA NA WAH YIP YIP YIP YIP YIP YIP YIP YIP YIP SHA BOOM))

(define (generate-huffman-tree pairs)
  (successive-merge (make-leaf-set pairs)))

(define (successive-merge pairs)
  (define (suc-iter total-weight pairs)
    (if (= total-weight (last-pair (car pairs)))
        (car pairs)
        (successive-merge (cons (make-code-tree (cadr pairs) (car pairs)) (cddr pairs)))))
  (suc-iter (total-weight pairs) pairs))

(define (total-weight pairs)
  (define (iter pairs result)
    (if (null? pairs)
        result
        (iter (cdr pairs) (+ result (weight (car pairs))))))
  (iter pairs 0))

(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))
  
(define (list-ref items n)
  (if (null? items)
      '()
      (if (= n 0)
          (car items)
          (list-ref (cdr items) (- n 1)))))

(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

(define (last-pair list)
  (list-ref list (- (length list) 1)))