blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
total_views=0
trending=0
for x in blog_views:
    total_views+=x
    if x>1000:
        trending+=1
        print('Trending')
    elif 500<= x <=1000:
        print('Average')
    elif x<500:
        print('Low traffic')
print('The total views=',total_views)
print(f"There are {trending} trending posts")