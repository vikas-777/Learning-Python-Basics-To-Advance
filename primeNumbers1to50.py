for i in range(2,50):
    prime=True
    for n in range(2,i):
        if i%n==0:
            prime = False
            break
    if prime:
            print(f"{i}",end=" ")