import click

from web_crawler_cli.web_crawler_cli import pass_context


@click.group()
@click.version_option()
def cli():
    """ Manages Web Crawler """

@cli.command('run')
@pass_context
def crawl_run(ctx):
    """ Crawl the url web """
    ctx.log(ctx.service.run())
