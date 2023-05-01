let star = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

center = 4

for (let i = 0; i < 5; i++) {
  for (let j = center - i; j < center + i + 1; j++) {
    star[j] = '*'
  }
  console.log(star.join(''))
}