import cProfile
import pstats
import os
import cts


def main():
    stat_file = "../../cts.stats"
    stat_log = "../../ctsstats.log"
    try:
        print "removing old .stat file"
        os.remove(stat_file)
    except WindowsError:
        print "old .stat file did not exist"
    try:
        print "removing old stat .log file"
        os.remove(stat_log)
    except WindowsError:
        print "old stat .log file did not exist"
    cProfile.run('cts.main()', stat_file)
    with open(stat_log, 'w') as f:
        p = pstats.Stats(stat_file, stream=f)
        p.sort_stats('time').print_stats()

if __name__ == '__main__':
    main()
