messyStr = "986-Maria, ( D@t@ Engineer );; 27y  "
print(f"Before Cleaning  {messyStr}")
clean = f"name: {messyStr[4:9].lower()} | role: {messyStr[13:26].replace('@', 'a').lower()} | age: {messyStr[-5:-3]}"
print(f"After Cleaning  {clean}")