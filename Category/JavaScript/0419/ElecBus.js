const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]
let result = 0

function solution(K, N, M, chargers) {
  chargers.unshift(0)
  chargers.push(N)
  let current = 0
  let count = 0

  for (let i = 1; i < M+2; i++) {
    if (chargers[i] - chargers[i-1] > K) {
      count = 0
      break
    }
    
    if (chargers[i] - chargers[current] > K) {
      count += 1
      current = i - 1
    }
  }

  console.log(`#${count}`)
}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}