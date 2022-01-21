import math
def doppler(vx, vy, oy, v, x, period, wSpeed,duration,timeC):
    #we want to simulate a source creating pulses at some period and then when it hits the observer, it records one, and we take this to measure frequency
    obs = {
        'vx' : vx,
        'vy': vy,
        'x': 0,
        'y': oy *timeC
    }
    src = {
        'v':v,
        'x':x * timeC,
    }
    times = []
    bubbles = []
    time = 0 
    wSpeed = wSpeed
    period = period* timeC
    for i in range(duration * timeC):
        if time % period == 0 or (time - period/50) % period == 0 :
            bubbles.append({
                'd': 0,
                'x': src['x'],
            })
        #update bubbles
        obs['x'] += obs['vx']
        obs['y'] += obs['vy']
        src['x'] += src['v']
        #couldve used a while loop instead :/
        for i2 in bubbles[:]:
            i2['d'] += wSpeed
            dist = math.sqrt((i2['x'] - obs['x'])**2 + (obs['y'])**2)
            if i2['d'] >= dist:
                bubbles.remove(i2)
                times.append(time/timeC)
        time += 1
    return times
#I want the simulation to last 20 seconds, each frame is 0.0001 seconds
def processtimes(times):
    for i in range(len(times)):
        if i % 2 == 0 and i < len(times) - 1:
            print(1/(times[i+1] - times[i])/50)
    print('seperator')
    for i in range(len(times)):
        if i % 2 == 0 and i < len(times) - 1:
            print((times[i+1] + times[i])/2)
#for standard doppler, -50 = vo, 100 = vs, dx = 1000, To =1, vw = 350
def case1():
    times = doppler(50,0,0,-100,1000,1,350,30, 10000)
    processtimes(times)
#for case 3 doppler, -50 = vxo, 100 = vx, dx = 1000, To =1, vw = 350, dy = 100
def case3():
    times = doppler(50,0,100,-100,1000,1,350,30, 10000)
    processtimes(times)
#for case 4, -100  =vox, 10 = voy, dx = 2000, To = 1, vw = 350, dy = 0, vx = 150
def case4():
    times = doppler(100,10,100,-150,2000,1,350,30,10000)
    processtimes(times)
    #goal of this: I want big numbers BIG. I want no crossover. Mening . .. they must head towards each other, vy must be big
    # vox = -100, voy = 25, dx = 17000m To = 0.5, vw = 350, dy = 500, vx = 50
def casefour():
    times = doppler(100,25,-500,-50,17000,0.5,350,100,100000)
    processtimes(times)
    # vox = 100, voy = -20, dx = 5  To = 1, vw = 350, dy = 500, vx = -50
def case4tsu():
    times = doppler(-100,-20,500,50,5,1,350,30,100000)
    processtimes(times)
case4tsu()
# doppler(vx, vy, oy, v, x, period, wSpeed,duration,timeC):