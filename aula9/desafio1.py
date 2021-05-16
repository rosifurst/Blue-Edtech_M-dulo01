for i in range(1000,10000):

  parte1 = i // 100
  parte2 = i % 100

  if (parte1 + parte2)**2 == i:
    print(i)


for i in range(32, 100): 
  
  parte1 = (i*i)%100 
  parte2 = int(i*i/100)

  if parte1+ parte2 == i:
     print(f'{i}^2: {i*i}')