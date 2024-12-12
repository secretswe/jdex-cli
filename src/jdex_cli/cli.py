import click
from typing import Optional
from tomlkit import dumps, parse, TOMLDocument, document, toml_file
from jdex_toml import JdexToml

from pathlib import Path
import os
import os.path
from dataclasses import dataclass


@dataclass
class Options:
    root: Path
    config_path: Path
    config: Optional[JdexToml]
    verbosity: bool


@click.group()
@click.option("--root", default=".", help="Root of directory tree")
@click.option("--config", default=None, help="Config file.")
@click.option("-v", "--verbose", count=True)
@click.pass_context
def cli(ctx, root, config, verbose):
    rp = Path(root or os.getcwd())
    cp = Path(config) if config else rp.joinpath(".jdex.toml")
    ctx.obj = Options(
        root=rp, config_path=cp, config=JdexToml.from_file(cp), verbosity=verbose
    )
    if verbose:
        print(ctx.obj)
        print(str(ctx.obj.config))
        print(str(ctx.obj.config.doc.unwrap()))


@cli.command()
@click.pass_context
def init(ctx):
    """Initialize a directory as a jdex directory."""
    if ctx.obj.config_path.is_file():
        raise click.ClickException(
            f"Cannot initialize jdex: {ctx.obj.config_path} file already exists"
        )
    JdexToml.new().write(ctx.obj.config_path)


@cli.command()
@click.pass_context
def path():
    print("path")


@cli.command()
@click.pass_context
def create():
    print("create")
