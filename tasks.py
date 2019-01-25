"""

Make-like task automation for Windows using python invoke

Supports:

inv clean
inv pep8
inv push <message>

Based on:

    https://github.com/mini-kep/parser-rosstat-kep/blob/dev/tasks.py

Original Windows workaround for invoke:

    https://github.com/pyinvoke/invoke/issues/371#issuecomment-259711426

"""
import os
import shutil


from sys import platform
from os import environ
from pathlib import Path

from invoke import Collection, task


def remove(path):
    if os.path.isfile(path):
        os.unlink(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


def all_files(directory):
    for _insider in directory.iterdir():
        if _insider.is_dir():
            subs = all_files(_insider.resolve())
            for _sub in subs:
                yield _sub.resolve()
        else:
            yield _insider.resolve()


class Folder:
    def __init__(self, path="."):
        self.directory = Path(path)

    @property
    def subdirs(self):
        return list(Path(x[0]) for x in os.walk(self.directory))

    @property
    def files(self):
        return list(all_files(self.directory))


def mask_by_suffix(extension, gen):
    return filter(lambda x: x.suffix == extension, gen)


def mask_by_name(name, gen):
    return filter(lambda x: x.stem == name, gen)


@task
def pep8(ctx, folder=''):
    for f in mask_by_suffix(".py", Folder(".").files):
        print("Formatting", f)
        ctx.run("autopep8 --aggressive --aggressive --in-place {}".format(f))


@task
def clean(ctx):
    # find . -name \*.pyc -delete
    for file in mask_by_suffix(".pyc", Folder(".").files):
        file.unlink()
        print("Deleted", file)
    # find . -name __pycache__ -delete
    for d in mask_by_name("__pycache__", Folder(".").subdirs):
        shutil.rmtree(d)
        print("Deleted", d)


def run(ctx, cmd):
    return ctx.run(cmd, hide=False, warn=True)


def run_all(ctx, commands):
    cmd = " && ".join(commands)
    return run(ctx, cmd)


@task
def ls(ctx):
    """List current directory"""
    run(ctx, "dir /b")


@task
def docs(ctx, subcommand):
    if subcommand == 'apidoc':
        run (ctx, "sphinx-apidoc -fM -o docs/source boo */test*")    
    if subcommand == 'make':
        run (ctx, "docs\make.bat html")
    if subcommand == 'show':
        run (ctx, 'start docs/build/html/index.html')


def quote(s):
    QUOTECHAR = '"'  # this is <">
    return f"{QUOTECHAR}{s}{QUOTECHAR}"


ns = Collection()
for t in [ls, clean, pep8, docs]:
    ns.add_task(t)


# Workaround for Windows execution
if platform == 'win32':
    # This is path to cmd.exe
    ns.configure({'run': {'shell': environ['COMSPEC']}})
