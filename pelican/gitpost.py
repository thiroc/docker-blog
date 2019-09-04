import os
import logging

from flask import Flask
from flask import request
from subprocess import Popen
from subprocess import PIPE

DOCROOT = '/srv/pelican'
LOGLEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d,%H:%M:%S'
LOGFILE = DOCROOT + '/log/gitpost.log'

app = Flask(__name__)
app.logger.setLevel(LOGLEVEL)

formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)
fh = logging.FileHandler(LOGFILE)
fh.setFormatter(formatter)

app.logger.addHandler(fh)

app.logger.info('Starting gitpost api application')

def log_error(command, output, error, returncode):
    msg = """
    Command: {cmd} => {ret}
    --------------

    Output:
        {out}

    Error:
        {err}
    """.format(cmd=command, out=output, err=error, ret=returncode)
    app.logger.error(msg)

def popen(cmd):
    app.logger.debug('Changing into {0}'.format(DOCROOT))
    app.logger.debug('Executing: {0}'.format(' '.join(cmd)))

    os.chdir(DOCROOT)
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    p.wait()
    out, err = p.communicate()
    if p.returncode != 0:
        log_error(cmd, out, err, p.returncode)

@app.route('/update', methods=['POST'])
def parse_request():
    app.logger.debug('Initiating master repo sync')
    app.logger.info('Updating blog')
    popen(['make', 'publish'])

    app.logger.info('Finished publishing')
    return 'Received:: {0}'.format(request.form)

if __name__ == '__main__':
        app.run()

