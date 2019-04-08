import runManage
import runUpdator
import multiprocessing


if __name__ == "__main__":

    pid_Updator =  multiprocessing.Process(target=runUpdator.run)
    pid_Manage =  multiprocessing.Process(target=runManage.run)

    processList = [pid_Updator,pid_Manage]

    for p in processList:
        p.start()

    for p in processList:
        p.join()
