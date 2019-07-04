#lang racket
(define (square x) (* x x))

(define (cube x) (* x x x))

(define (exp b n)
  (cond ((= n 0) 1)
        ((even? n) (square (exp b (/ n 2))))
        (else (* b (exp b (- n 1))))))

(define (identity x) x)

(define (sum-integers a b)
  (sum identity a inc b))

(define (sum-cubes a b)
  (sum cube a inc b))

(define (pi-sum a b)
  (define (pi-term x)
    (/ 1.0 (* x (+ x 2))))
  (define (pi-next x)
    (+ x 4))
  (sum pi-term a pi-next b))

(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))

(define (sum2 term a next b)
  (define (iter a  b result)
    (if (> a b)
        result
        (iter (next a) b (+ result (term a)))))
  (iter a b 0))

(define (inc n) (+ n 1))

(define (down n) (- n 1))

(define (even? n)
  (= (remainder n 2) 0))

(define (integral f a b dx)
  (define (add-dx x) (+ x dx))
  (* (sum f (+ a (/ dx 2.0)) add-dx b)
     dx))

(define (coeffcb x)
  (* (cond ((or (= x 0) (= x 1)) 1.0)
           ((even? (* x 1000)) 2.0)
           (else 4.0))
     (cube x)))

(define (integral2 f a b n)
  (define h (/ (- b a) n))
  (define (addh x) (+ x h))
  (* (sum f a addh (/ n n))
     (/ h 3.0)))

(define (product term a next b)
  (if (> a b)
      1
      (* (term a)
        (product term (next a) next b))))

(define (itproduct term a next b)
  (define (iter a b result)
    (if (> a b)
        result
        (iter (next a) b (* result (term a)))))
  (iter a b 1))

(define (factorial n)
  (product identity 1 inc n))

(define (pi-product n)
  (define (addthing n)
    (if (even? n)
        2.0
        1.0))
  (define (next-term n)
    (/  (+ n (addthing n)) (+ n (addthing (+ n 1)))))
  (itproduct next-term 1 inc n))

(define (accumulate combiner null-value term a next b)
  (if (> a b)
      null-value
      (combiner (term a)
                (accumulate combiner null-value term (next a) next b))))

(define (itaccumulate combiner null-value term a next b)
  (define (iter a b result)
    (if (> a b)
        result
        (iter (next a) b (combiner result (term a)))))
  (iter a b null-value))

(define (filtered-accumulate combiner null-value filter term a next b)
  (define (iter a b result)
    (if (> a b)
        result
        (if (filter a b)
            (iter (next a) b (combiner result (term a)))
            (iter (next a) b result))))
  (iter a b null-value))

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

(define (gcd a b)
  (if (= b 0)
      a
      (gcd b (remainder a b))))

(define (rel-prime? m n)
  (= (gcd m n) 1))

(define (average x y)
  (/ (+ x y) 2))

(define (positive? x)
  (> x 0))

(define (negative? x)
  (< x 0))

(define (abs x)
  (if (< x 0)
      (- x)
      x))

(define (close-enough? x y)
  (< (abs (- x y)) 0.001))

(define (search f neg-point pos-point)
  (let ((midpoint (average neg-point pos-point)))
    (if (close-enough? neg-point pos-point)
        midpoint
        (let ((test-value (f midpoint)))
          (cond ((positive? test-value)
                 (search f neg-point midpoint))
                ((negative? test-value)
                 (search f midpoint pos-point))
                (else midpoint))))))

(define (half-interval-method f a b)
  (let ((a-value (f a))
        (b-value (f b)))
    (cond ((and (negative? a-value) (positive? b-value)) (search f a b))
          ((and (negative? b-value) (positive? a-value)) (search f b a))
          (else
           (error "Values are not of opposite sign" a b)))))

(define tolerance 0.00001)

(define (fixed-point f first-guess)
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2)) tolerance))
  (define (try guess)
    (display guess)
    (newline)
    (let ((next (f guess)))
      (if (close-enough? guess next)
          next
          (try next))))
  (try first-guess))

(define (sqrt x)
  (fixed-point-of-transform (lambda (y) (/ x y))
                            average-damp
                            1.0))

(define (cube-root x)
  (fixed-point (average-damp (lambda (y) (/ x (square y))))
               1.0))

(define (fourth-root x)
  (fixed-point ((repeated average-damp 2) (lambda (y) (/ x (cube y))))
               1.0))

(define (fifth-root x)
  (fixed-point ((repeated average-damp 2) (lambda (y) (/ x (exp y 4))))
               1.0))

(define (nth-root n x)
  (fixed-point ((repeated average-damp (how-many-damps n)) (lambda (y) (/ x (exp y (- n 1)))))
               1.0))

(define (how-many-damps n)
  (define (iter n count)
    (if (< n (exp 2 count))
        (- count 1)
        (iter n (+ count 1))))
  (iter n 1))
           

(define (cont-frac n d k)
  (define (recur n d k count)
    (if (> count k)
        0
        (/ (n count) (+ (d count) (recur n d k (+ count 1))))))
  (recur n d k 0))

(define (cont-frac-iter n d k)
  (define (iter n d k result)
    (display result)
    (newline)
    (display (d k))
    (newline)
    (if (< k 1)
        result
        (iter n d (- k 1) (/ (n (- k 1)) (+ result (d (- k 1)))))))
  (iter n d k (/ (n k) (d k))))

(define (d-for-e i)
  (cond ((or (= (remainder i 3) 2) (= (remainder i 3) 0)) 1.0)
        (else (* 2 (+ 1 (mod i 3))))))

 (define (mod x y)
   (/ (- x (remainder x y)) y))

(define (tan-cf n d x k)
  (define (iter n d k result)
    (display result)
    (newline)
    (display (n x k))
    (newline)
    (display (d k))
    (newline)
    (if (< k 2)
        (/ result x)
        (iter n d (- k 1) (/ (n x k) (- (d (- k 1)) result)))))
  (iter n d k (/ (n x k) (d k))))

(define (n-for-tan x k)
  (if (= k 1)
      x
      (square x)))

(define (d-for-tan x)
  (- (* x 2.0) 1.0))

(define (average-damp f)
  (lambda (x) (average x (f x))))

(define (deriv g)
  (lambda (x)
    (/ (- (g (+ x dx)) (g x)) dx)))

(define dx 0.00001)

(define (newton-transform g)
  (lambda (x)
    (- x (/ (g x) ((deriv g) x)))))

(define (newtons-method g guess)
  (fixed-point (newton-transform g) guess))

(define (sqrt2 x)
  (fixed-point-of-transform (lambda (y) (- (square y) x))
                            newton-transform
                            1.0))

(define (fixed-point-of-transform g transform guess)
  (fixed-point (transform g) guess))

(define (cubic a b c)
  (lambda (x) (+ (cube x) (* a (square x)) (* b x) c)))

(define (double f)
  (lambda (x) (f (f x))))

(define (triple f)
  (lambda (x) (f (f (f x)))))

(define (compose g f)
  (lambda (x) (g (f x))))

(define (repeated f n)
  (define (iter orig f n count)
    (if (= count n)
        f
        (iter orig (compose orig f) n (+ count 1))))
  (iter f f n 1))

(define (smooth f)
  (lambda (x) (/  (+ (f (+ x dx)) (f x) (f (- x dx))) 3)))

(define (iterative-improve good-enough improve)
  (define (iter guess)
    ((if (good-enough guess)
         guess
         (iter (improve guess)))))
  (lambda (x) (iter x)))

(define (oldsqrt-good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))

(define (oldsqrt-improve guess x)
  (average guess (/ x guess)))

(define (oldsqrt x)
  (define (good-enough? guess x)
    (< (abs (- (square guess) x)) 0.001))
  (define (improve guess x)
    (average guess (/ x guess)))
  (define (sqrt-iter guess x)
    (if (good-enough? guess)
        guess
        (sqrt-iter (improve guess) x)))
  (sqrt-iter 1.0 x))