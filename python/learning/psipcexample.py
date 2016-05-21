from multiprocessing import Pipe, Process
import subprocess

def taskit(rd, wt):
    cmd = rd.recv()
    response = subprocess.check_output([cmd])
    wt.send(response)

def main():
    rd1, wt1 = Pipe()
    rd2, wt2 = Pipe()

    p = Process(target=taskit, args=(rd1, wt2))
    p.start()

    wt1.send('fortune')
    res = rd2.recv()
    print(res)

if __name__ == '__main__':
    main()