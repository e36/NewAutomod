import configparser
import multiprocessing as mp
from collectors import comment_scraper_entrypoint, submission_scraper_entrypoint
from handlers import comment_handler, submission_handler

if __name__ == "__main__":

    # init configparser and read the config file
    # probably wrap some error handling around this
    config = configparser.ConfigParser()
    config.read('config')

    general_config = config['General']
    worker_config = config['Workers']

    comments_queue = mp.Queue(1000)
    submissions_queue = mp.Queue(1000)

    comment_collector_proc = mp.Process(target=comment_scraper_entrypoint, args=( comments_queue, None, None))
    submission_collector_proc = mp.Process(target=submission_scraper_entrypoint, args=( submissions_queue, None, None))
    comment_handler_proc = mp.Process(target=comment_handler, args=(comments_queue,))
    submission_handler_proc = mp.Process(target=submission_handler, args=(submissions_queue,))

    submission_collector_proc.start()
    submission_handler_proc.start()
    comment_collector_proc.start()
    comment_handler_proc.start()

    #here is where we ideally spawn another thread/process that will re-spawn these guys in case of catastrophic failure


