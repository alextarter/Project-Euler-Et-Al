d=3; k=10^(d-1);
P=0; N=1; M=1;
n=10*k-1;
while n>=k
    m=10*k-1;
    while m>=n
        if n*m<P
            break
        else
            if str2double(reverse(num2str(n*m)))==n*m
                P=n*m;
                N=n;
                M=m;
            end
        end
        m=m-1;
    end
    n=n-1;
end
[P,N,M]