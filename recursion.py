def mystery( n ):
   if n > 0:
       print(n,"mystery function is called. ")
      # print(n, end=" ")
       mystery( n-1)
       print( n, end = " " )
   # else, do nothing
# inside main:
mystery( 5 )
