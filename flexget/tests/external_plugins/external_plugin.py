from __future__ import unicode_literals, division, absolute_import
from builtins import *  # pylint: disable=unused-import, redefined-builtin

from flexget import plugin
from flexget.entry import Entry
from flexget.event import event


class ExternalPlugin(object):
    schema = {'type': 'boolean'}

    def on_task_input(self, task, config):
        return [Entry('test entry', 'fake url')]


@event('plugin.register')
def register_plugin():
    plugin.register(ExternalPlugin, 'external_plugin', api_ver=2)
