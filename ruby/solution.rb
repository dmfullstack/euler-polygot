def solution(n)
  sol = 0
  (0..n-1).each do |x|
    if x%3 == 0 || x%5 == 0
      sol += x 
    end
  end
  return sol
end