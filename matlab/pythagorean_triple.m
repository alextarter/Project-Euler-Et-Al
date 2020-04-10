n=1000; b=ceil(n/2)-2;
for k=ceil(n/2):-1:2
    a=ceil(n/2)-k+1;
    while ceil(n/2)<a+k<floor(2*n/3) && a<k
        if n*(a+k)-a*k==n^2/2
            b=k;
            return
        end
        a=a+1;
    end
end
[a,b,n-a-b]