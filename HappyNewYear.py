def countDown(start):
    print("start")
    let nextNumber = start - 1
    if nextNumber > 0:
        setTimeout(countDown, 100, nextNumber)
    else
        setTimeout(def(){print("HAPPY NEW YEAR!");}, 1000,nextNumber);

count = parseInt(prompt("How many seconds before the ball drops???"));
countDown(count);
