#lang racket
(define (add-rat x y)
  (make-rat (+ (* (numer x) (denom y))
               (* (numer y) (denom x)))
            (* (denom x) (denom y))))

(define (sub-rat x y)
  (make-rat (- (* (numer x) (denom y))
               (* (numer y) (denom x)))
            (* (denom x) (denom y))))

(define (mul-rat x y)
  (make-rat (* (numer x) (numer y))
            (* (denom x) (denom y))))

(define (div-rat x y)
  (make-rat (* (numer x) (denom y))
            (* (numer y) (denom x))))

(define (equal-rat? x y)
  (= (* (numer x) (denom y))
     (* (numer y) (denom x))))

(define (make-rat n d)
  (let ((g (gcd n d)))
    (cons (/ n g) (/ d g))))

(define (numer x) (car x))

(define (denom x) (cdr x))

(define (print-rat x)
  (newline)
  (display (numer x))
  (display "/")
  (display (denom x)))

(define (gcd a b)
  (if (= b 0)
      a
      (gcd b (remainder a b))))

(define (abs x)
  (if (< x 0)
      (- x)
      x))

(define (average a b)
  (/ (+ a b) 2))

(define (make-segment start end) (cons start end))

(define (start-segment segment) (car segment))

(define (end-segment segment) (cdr segment))

(define (make-point x y) (cons x y))

(define (x-point point) (car point))

(define (y-point point) (cdr point))

(define (print-point p)
  (newline)
  (display "(")
  (display (x-point p))
  (display ",")
  (display (y-point p))
  (display ")"))

(define (midpoint-segment segment)
  (make-point (/ (+ (car (car segment))
                    (car (cdr segment)))
                 2)
              (/ (+ (cdr (car segment))
                    (cdr (cdr segment)))
                 2)))

(define (len-seg segment)
  (if (= (abs (- (x-point (car segment))
                 (x-point (cdr segment))))
         0)
      (abs (- (y-point (car segment))
              (y-point (cdr segment))))
      (abs (- (x-point (car segment))
              (x-point (cdr segment))))))

(define (make-rec point1 point2) (cons point1 point2))

(define (perimeter rectangle)
  (* 2 (+ (abs (- (x-point (car rectangle))
                  (x-point (cdr rectangle))))
          (abs (- (y-point (car rectangle))
                  (y-point (cdr rectangle)))))))

(define (area rectangle)
  (* (abs (- (x-point (car rectangle))
             (x-point (cdr rectangle))))
     (abs (- (y-point (car rectangle))
             (y-point (cdr rectangle))))))

(define (cons1 x y)
  (* (exp 2 x) (exp 3 y)))

(define (car1 z)
  (if (div3? z)
      (car (/ z 3))
      (log 2 z)))      

(define (cdr1 z)
  (if (even? z)
      (cdr (/ z 2))
      (log 3 z)))

(define (square x) (* x x))

(define (even? x)
  (= (remainder x 2) 0))

(define (div3? x)
  (= (remainder x 3) 0))

(define (exp b n)
  (cond ((= n 0) 1)
        ((even? n) (square (exp b (/ n 2))))
        (else (* b (exp b (- n 1))))))

(define (log b x)
  (cond ((= x 1) 0)
        ((= (remainder x b) 0) (+ 1 (log b (/ x b))))
        ((not (= (remainder x b) 0)) (error "Non-integer answer."))))

(define zero (lambda (f) (lambda (x) x)))

(define (add-1 n)
  (lambda (f) (lambda (x) (f ((n f) x)))))

(define (inc x) (+ x 1))

(define (add-interval x y)
  (make-interval (+ (lower-bound x) (lower-bound y))
                 (+ (upper-bound x) (upper-bound y))))

(define (mul-interval x y)
  (let ((p1 (* (lower-bound x) (lower-bound y)))
        (p2 (* (lower-bound x) (upper-bound y)))
        (p3 (* (upper-bound x) (lower-bound y)))
        (p4 (* (upper-bound x) (upper-bound y))))
    (make-interval (min p1 p2 p3 p4)
                   (max p1 p2 p3 p4))))

(define (mul-interval2 x y)
  (cond ((and (neg? (lower-bound x)) (pos? (upper-bound x)) (pos? (lower-bound y)) (pos? (upper-bound y))) (make-interval (* (lower-bound x) (upper-bound y))
                                                                                                                          (* (upper-bound x) (upper-bound y))))
        
        ((and (neg? (lower-bound x)) (pos? (upper-bound x)) (neg? (lower-bound y)) (pos? (upper-bound y))) (make-interval (min (* (lower-bound x) (upper-bound y))
                                                                                                                               (* (upper-bound x) (lower-bound y)))
                                                                                                                          (max (* (upper-bound x) (upper-bound y))
                                                                                                                               (* (lower-bound x) (lower-bound y)))))

        ((and (neg? (lower-bound x)) (neg? (upper-bound x)) (pos? (lower-bound y)) (pos? (upper-bound y))) (make-interval (* (lower-bound x) (upper-bound y))
                                                                                                                          (* (upper-bound x) (lower-bound y))))

        ((and (neg? (lower-bound x)) (neg? (upper-bound x)) (neg? (lower-bound y)) (pos? (upper-bound y))) (make-interval (* (lower-bound x) (upper-bound y))
                                                                                                                          (* (lower-bound x) (lower-bound y))))

        ((and (neg? (lower-bound x)) (neg? (upper-bound x)) (neg? (lower-bound y)) (neg? (upper-bound y))) (make-interval (* (upper-bound x) (upper-bound y))
                                                                                                                          (* (lower-bound x) (lower-bound y))))

        ((and (pos? (lower-bound x)) (pos? (upper-bound x)) (neg? (lower-bound y)) (neg? (upper-bound y))) (make-interval (* (upper-bound x) (lower-bound y))
                                                                                                                          (* (lower-bound x) (upper-bound y))))

        ((and (pos? (lower-bound x)) (pos? (upper-bound x)) (neg? (lower-bound y)) (pos? (upper-bound y))) (make-interval (* (upper-bound x) (lower-bound y))
                                                                                                                          (* (upper-bound x) (upper-bound y))))

        ((and (pos? (lower-bound x)) (pos? (upper-bound x)) (pos? (lower-bound y)) (pos? (upper-bound y))) (make-interval (* (lower-bound x) (lower-bound y))
                                                                                                                          (* (upper-bound x) (upper-bound y))))

        ((and (neg? (lower-bound x)) (pos? (upper-bound x)) (neg? (lower-bound y)) (neg? (upper-bound y))) (make-interval (* (upper-bound x) (lower-bound y))
                                                                                                                          (* (lower-bound x) (lower-bound y))))
        (else (error "Stupid Ben didn't account for 0, which is probably what the interval has." x y))))


(define (sub-interval x y)
  (make-interval (- (lower-bound x) (lower-bound y))
                 (- (upper-bound x) (upper-bound y))))

(define (div-interval x y)
  (if (and (= (lower-bound x) (lower-bound y)) (= (upper-bound x) (upper-bound y)))
      (make-interval 1 1)
      (if (= (width-interval y) 0)
          (error "Cannot divide by an interval that spans 0." y)
          (mul-interval x
                        (make-interval (/ 1.0 (upper-bound y))
                                       (/ 1.0 (lower-bound y)))))))

(define (make-interval a b) (cons a b))

(define (upper-bound x) (cdr x))

(define (lower-bound x) (car x))

(define (width-interval x)
  (/ (- (cdr x) (car x)) 2.0))

(define (neg? m) (< m 0))

(define (pos? m) (> m 0))

(define (make-center-width c w)
  (make-interval (- c w) (+ c w)))

(define (center i)
  (/ (+ (lower-bound i) (upper-bound i)) 2))

(define (width i)
  (/ (- (upper-bound i) (lower-bound i)) 2))

(define (make-center-percent c percent)
  (make-interval (- c (* c percent))
                 (+ c (* c percent))))

(define (percent i)
  (/ (- (upper-bound i) (lower-bound i)) 2 (center i)))

(define (par1 r1 r2)
  (div-interval (mul-interval r1 r2)
                (add-interval r1 r2)))

(define (par2 r1 r2)
  (let ((one (make-interval 1 1)))
    (div-interval one
                  (add-interval (div-interval one r1)
                                (div-interval one r2)))))