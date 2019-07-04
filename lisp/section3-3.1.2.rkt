#lang racket

(define ogbalance 100)

(define (withdraw amount)
  (if (>= ogbalance amount)
      (begin (set! ogbalance (- ogbalance amount))
             ogbalance)
      "Insufficient funds"))

(define new-withdraw
  (let ((balance2 100))
    (lambda (amount)
      (if (>= balance2 amount)
          (begin (set! balance2 (- balance2 amount))
                 balance2)
          "Insufficient funds"))))

(define (make-withdraw balance)
  (lambda (amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds")))

(define W1 (make-withdraw 100))
(define W2 (make-withdraw 100))

(define (make-account balance . passwords)
  (let ((incorrect-attempts 0))
    (define (withdraw amount)
      (if (>= balance amount)
          (begin (set! balance (- balance amount))
                 balance)
          "Insufficient funds"))
    (define (deposit amount)
      (set! balance (+ balance amount))
      balance)
    (define (add-pass new-pass)
      (set! passwords (append passwords (list new-pass))))
    (define call-the-cops "Called the cops")
    (define (incorrect-password m)
      (set! incorrect-attempts (+ incorrect-attempts 1))
      (if (= incorrect-attempts 7)
          call-the-cops
          "Incorrect password"))
    (define (check-password input-password passwords)
      (cond ((null? passwords) #f)
            ((eq? input-password (car passwords)) #t)
            (else (check-password input-password (cdr passwords)))))         
    (define (dispatch input-password m)
      (if (check-password input-password passwords)
          (begin (set! incorrect-attempts 0)
                 (cond ((eq? m 'withdraw) withdraw)
                       ((eq? m 'deposit) deposit)
                       ((eq? m 'add-pass) add-pass)
                       (else (error "Unknown request -- MAKE-ACCOUNT"
                                    m))))
          incorrect-password))
    dispatch))

(define (make-joint account-name og-pass new-pass)
  (cond ((number? ((account-name og-pass 'withdraw) 0))
         (begin ((account-name og-pass 'add-pass) new-pass)
                account-name))
        (else account-name)))

(define (make-accumulator initial)
  (lambda (increment)
    (begin (set! initial (+ initial increment))
           initial)))

(define (make-monitored f)
  (let ((count 0))
    (lambda (input-f)
        (cond ((eq? input-f 'reset-counter) (set! count 0))
              ((eq? input-f 'how-many-calls?) count)
              (else (begin (set! count (+ count 1))
                           (display (f input-f))
                           (newline)
                           count))))))

;(define rand
 ; (let ((x random-init))
  ;  (lambda ()
   ;   (set! x (rand-update x))
    ;  x)))

;(define (estimate-pi trials)
 ; (sqrt (/ 6 (monte-carlo trials cesaro-test))))

;(define (cesaro-test)
 ; (= (gcd (rand) (rand)) 1))

(define (monte-carlo trials experiment)
  (define (iter trials-remaining trials-passed)
    (cond ((= trials-remaining 0)
           (/ trials-passed trials))
          ((experiment)
           (iter (- trials-remaining 1) (+ trials-passed 1)))
          (else
           (iter (- trials-remaining 1) trials-passed))))
  (iter trials 0))

(define (random-in-range low high)
  (let ((range (- high low)))
    (+ low (random range))))

(define (square z) (* z z))

(define (area x1 x2 y1 y2)
  (* (- y1 x1) (- y2 x2)))

(define (estimate-pi2 trials)
  (/ (* (estimate-integral in-the-circle? -3 -3 3 3 trials)
        (area -3.0 -3 3 3))
     (square 2)))

(define (in-the-circle?)
  (>= (square 2) (+ (square (- (car (rectangle-procedure -3 -3 3 3)) 0))
                    (square (- (car (rectangle-procedure -3 -3 3 3)) 0)))))

(define (rectangle-procedure x1 x2 y1 y2)
    (cons (random-in-range x1 y1)
          (random-in-range x2 y2)))

(define (estimate-integral P x1 x2 y1 y2 trials)
  (monte-carlo trials P))

;(define (rand operation)
 ; (let ((init original-init))
  ;  (cond ((eq? operation 'reset) (lambda (number) (set! init number)))
   ;       ((eq? operation 'generate) (begin (set! init (rand-update init))
    ;                                        init)))))