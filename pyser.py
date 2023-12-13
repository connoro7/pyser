import click
import requests
import json

# reference: https://click.palletsprojects.com/en/8.1.x/
# reference: https://duckduckgo.com/duckduckgo-help-pages/settings/params/


@click.command()
@click.option('-n', '--num', default=1, type=int, show_default=True, help='show top N results') # TODO
@click.option('-d', '--ducky', is_flag=True, default=False, help='Automatically open the first result in browser') # TODO
@click.option('-s', '--site', type=str, default='', help='Specify site to search, equivalent to specifying \'site:example.com\'') # TODO
@click.option('-x', '--expand', is_flag=True, default=False, help='Show complete URL in search results') # TODO
@click.option('-r', '--region', type=str, default='us', help='Specify region to search, equivalent to specifying \'cr=countryXX\'') # TODO
@click.option('-j', '--json', is_flag=True, default=False, help='Output results in JSON format') # TODO
@click.option('-u', '--useragent', type=str, default='', help='Specify user agent') # TODO
@click.option('-v', '--version', is_flag=True, default=False, help='Show version') # TODO
@click.option('-d', '--debug', is_flag=True, default=False, help='Enable debug mode') # TODO
@click.argument('search_term', type=click.STRING)
def query(search_term, num, ducky, site, expand, region, json, version, debug):
    click.echo(f'Search term: {search_term}')
    click.echo(f'num: {num}')
    click.echo(f'ducky: {ducky}')
    click.echo(f'site: {site}')
    click.echo(f'expand: {expand}')
    click.echo(f'region: {region}')
    click.echo(f'json: {json}')
    click.echo(f'useragent: {useragent}')
    click.echo(f'version: {version}')
    click.echo(f'debug: {debug}')

    res = requests.get(f'https://api.duckduckgo.com/?q={search_term}&format=json&pretty=1')
    data = res.text
    data = data.replace("'", "\"")
    headers = res.headers
    headers = headers.replace("'", "\"")


    with open('data.json', 'w') as f:
        print(data, file=f)

    with open('headers.json', 'w') as f:
        print(headers, file=f)

    # print(headers, '\n', data)
    # click.echo('headers:\n\n', res.headers)
    # click.echo('json\n\n', res.json())

if __name__ == '__main__':
    query()
