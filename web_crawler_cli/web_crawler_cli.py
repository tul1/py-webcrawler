import os
import sys
import click

from pathlib import Path

from web_crawler import WebCrawler
from web_crawler.utils.web_crawler_logger import WebCrawlerLogger


CONTEXT_SETTINGS = dict(auto_envvar_prefix='WEBCRAWLER')


class Context(object):

    def __init__(self):
        self.verbose = False
        self.config_dir = str(Path.home())
        self.service = None
        self._logger = WebCrawlerLogger().get_logger()

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)
    
    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)

pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))


class WebCrawlerCLI(click.MultiCommand):

    def list_commands(self, ctx):
        commands = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith('cmd_'):
                commands.append(filename[4:-3])
        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__(f'web_crawler_cli.commands.cmd_{name}', None, None, ['cli'])
        except ImportError as err:
            WebCrawlerLogger().get_logger().error(err)
            return
        return mod.cli


@click.command(cls=WebCrawlerCLI, context_settings=CONTEXT_SETTINGS)
@click.option('-u', '--url', default=lambda: os.environ.get('WEB_CRAWLER_URL',''), help='Url to crawl.')
@click.option('-v', '--verbose', default=False, help='Enables verbose mode.')
@pass_context
def cli(ctx, verbose, url):
    """Web Crawler command line interface."""
    ctx.verbose = verbose
    ctx.service = WebCrawler(url)
