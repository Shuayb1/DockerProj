#!/usr/bin/env python
"""
Commandline tool for interacting with library
"""
import click

@click.command()
def hello(  ):
    click.echo('Hello World')
    
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()
