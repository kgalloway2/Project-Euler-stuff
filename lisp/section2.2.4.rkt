#lang racket

(define wave2 (beside wave (flip-vert wave)))

(define wave4 (below wave2 wave2))

(define (flipped-pairs painter)
  (let ((painter2 (beside painter (flip-vert painter))))
    (below painter2 painter2)))

(define wave4v2 (flipped-pairs wave))

(define (right-split painter n)
  (if (= n 0)
      painter
      (let ((smaller (right-split painter (- n 1))))
        (beside painter (below smaller smaller)))))

(define (up-split painter n)
  (if (= n 0)
      painter
      (let ((smaller (up-split painter (- n 1))))
        (below painter (beside smaller smaller)))))

(define (corner-split painter n)
  (if (= n 0)
      painter
      (let ((up (up-split painter (- n 1)))
            (right (right-split painter (- n 1))))
        (let ((top-left up)
              (bottom-right right)
              (corner (corner-split painter (- n 1))))
          (beside (below painter top-left)
                  (below bottom-right corner))))))

(define (square-limit painter n)
  (let ((quarter (corner-split painter n)))
    (let ((half (beside quarter (flip-horiz quarter))))
      (below (flip-vert half) half))))

(define (square-of-four tl tr bl br)
  (lambda (painter)
    (let ((top (beside (tl painter) (tr painter)))
          (bottom (beside (bl painter) (br painter))))
      (below bottom top))))

(define (flipped-pairsv2 painter)
  (let ((combine4 (square-of-four identity flip-vert
                                  identity flip-vert)))
    (combine4 painter)))

(define (square-limitv2 painter n)
  (let ((combine4 (square-of-four flip-horiz identity
                                  rotate180 flip-vert)))
    (combine4 (corner-split painter n))))

(define (split place type)
  (lambda (painter n)
    (if (= n 0)
        painter
        (let ((smaller ((split place type) painter (- n 1))))
          (place painter (type smaller smaller))))))

(define (frame-coord-map frame)
  (lambda (v)
    (add-vect
     (origin-frame frame)
     (add-vect (scale-vect (xcor-vect v)
                           (edge1-frame frame))
               (scale-vect (ycor-vect v)
                           (edge2-frame frame))))))

(define (make-vect x y) (cons x y))
(define (xcor-vect v) (car v))
(define (ycor-vect v) (cdr v))

(define (add-vect v w)
  (make-vect (+ (xcor-vect v) (xcor-vect w))
             (+ (ycor-vect v) (ycor-vect w))))

(define (sub-vect v w)
  (make-vect (- (xcor-vect v) (xcor-vect w))
             (- (ycor-vect v) (ycor-vect w))))

(define (scale-vect s v)
  (make-vect (* s (xcor-vect v))
             (* s (ycor-vect v))))

(define (make-frame1 origin edge1 edge2)
  (list origin edge1 edge2))

(define (or1 frame) (car frame))
(define (e11 frame) (cadr frame))
(define (e21 frame) (caddr frame))

(define (make-frame2 origin edge1 edge2)
  (cons origin (cons edge1 edge2)))

(define (or2 frame) (car frame))
(define (e12 frame) (cadr frame))
(define (e22 frame) (cddr frame))

(define (make-segment v1 v2) (cons v1 v2))
(define (start-segment seg) (cdar seg))
(define (end-segment seg) (cddr seg))

(define (segments->painter segment-list)
  (lambda (frame)
    (for-each
     (lambda (segment)
       (draw-line
        ((frame-coord-map frame) (start-segment segment))
        ((frame-coord-map frame) (end-segment segment))))
     segment-list)))

(define (outline frame)
  (segments->painter
   (let ((origin (or1 frame))
         (edge1 (e11 frame))
         (edge2 (e21 frame)))
     (let ((seg1 (make-segment origin (add-vect origin edge1)))
           (seg2 (make-segment origin (add-vect origin edge2)))
           (seg3 (make-segment (add-vect origin edge2) (add-vect origin (add-vect edge1 edge2))))
           (seg4 (make-segment (add-vect origin edge1) (add-vect origin (add-vect edge1 edge2)))))
       (list seg1 seg2 seg3 seg4)))))

(define (X frame)
  (segments->painter
   (let ((origin (or1 frame))
         (edge1 (e11 frame))
         (edge2 (e21 frame)))
     (let ((seg1 (make-segment origin (add-vect origin (add-vect edge1 edge2))))
           (seg2 (make-segment (add-vect origin edge1) (add-vect origin edge2))))
       (list seg1 seg2)))))

(define (diamond frame)
  (segments->painter
   (let ((origin (or1 frame))
         (edge1 (e11 frame))
         (edge2 (e21 frame)))
     (let ((seg1 (make-segment origin (add-vect origin edge1)))
           (seg2 (make-segment origin (add-vect origin edge2)))
           (seg3 (make-segment (add-vect origin edge2) (add-vect origin (add-vect edge1 edge2))))
           (seg4 (make-segment (add-vect origin edge1) (add-vect origin (add-vect edge1 edge2)))))
       (let ((AB (make-segment (mid seg1) (mid seg2)))
             (BC (make-segment (mid seg2) (mid seg3)))
             (CD (make-segment (mid seg3) (mid seg4)))
             (DA (make-segment (mid seg4) (mid seg1))))
         (list AB BC CD DA))))))
   

(define (mid segment)
  (make-vect (cons 0 0) (cons (/ (+ (car start-segment) (car end-segment)) 2)
                              (/ (+ (cdr start-segment) (cdr end-segment)) 2))))

(define (transform-painter painter origin corner1 corner2)
  (lambda (frame)
    (let ((m (frame-coord-map frame)))
      (let ((new-origin (m origin)))
        (painter
         (make-frame new-origin
                     (sub-vect (m corner1) new-origin)
                     (sub-vect (m corner2) new-origin)))))))

(define (flip-vert painter)
  (transform-painter painter
                     (make-vect 0.0 1.0)
                     (make-vect 1.0 1.0)
                     (make-vect 0.0 0.0)))

(define (flip-horiz painter)
  (transform-painter painter
                     (make-vect 1.0 0.0)
                     (make-vect 0.0 0.0)
                     (make-vect 1.0 1.0)))

(define (shrink-to-upper-right painter)
  (transform-painter painter
                     (make-vect 0.5 0.5)
                     (make-vect 1.0 0.5)
                     (make-vect 0.5 1.0)))

(define (rotate90 painter)
  (transform-painter painter
                     (make-vect 1.0 0.0)
                     (make-vect 1.0 1.0)
                     (make-vect 0.0 0.0)))

(define (rotate180 painter)
  (rotate90 (rotate90 painter)))

(define (rotate270 painter)
  (rotate90 (rotate180 painter)))

(define (squash-inwards painter)
  (transform-painter painter
                     (make-vect 0.0 0.0)
                     (make-vect 0.65 0.35)
                     (make-vect 0.35 0.65)))

(define (beside painter1 painter2)
  (let ((split-point (make-vect 0.5 0.0)))
    (let ((paint-left
           (transform-painter painter1
                              (make-vect 0.0 0.0)
                              split-point
                              (make-vect 0.0 1.0)))
          (paint-right
           (transform-painter painter2
                              split-point
                              (make-vect 1.0 0.0)
                              (make-vect 0.5 1.0))))
      (lambda (frame)
        (paint-left frame)
        (paint-right frame)))))

(define (below painter1 painter2)
  (let ((split-point (make-vect 0.0 0.5)))
    (let ((paint-bottom
           (transform-painter painter1
                              (make-vect 0.0 0.0)
                              (make-point 1.0 0.0)
                              split-point))
          (paint-top
           (transform-painter painter2
                              split-point
                              (make-vect 1.0 0.5)
                              (make-vect 0.0 1.0))))
      (lambda (frame)
        (paint-bottom frame)
        (paint-top frame)))))

(define (below2 painter1 painter2)
  (rotate90 (beside (rotate270 painter1) (rotate270 painter2))))
          
    