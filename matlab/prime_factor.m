function L = primefactor(N)

L=2;
for k=1:N-2
    while rem(N,L)==0
        N=N/L;
    end
    if N>L
        L=L+1;
    else
        break
    end
end