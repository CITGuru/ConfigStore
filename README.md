# ConfigStore 

A Python module for handling config files. It helps handles persist config files and also giving the ability to set, get, update and delete config settings

> Easily load and persist config without having to think about where and how

It's built base on nodejs [configstore](https:#github.com/yeoman/configstore)

Config is stored in a JSON file located in `$XDG_CONFIG_HOME` or `~/.localconfig`.<br>
Example: `~/.localconfig/configstore/name.json`

## Installation

```bash
pip install pyconfig
```

## Usage

```python
from pyconfig import ConfigStore

# create a Configstore instance with a unique name e.g. gnit
# Package name and optionally some default values
conf = ConfigStore("Gnit", {"foo": 'bar'});

print(conf.get('foo'));
#>>> 'bar'

conf.set('awesome', True);
print(conf.get('awesome'));
#>>> True

# Use dot-notation to set nested properties
conf.set('bar.baz', True);
print(conf.get('bar'));
#>>> {"baz": True}

# escape dot-notation to set nested properties
conf.set('bar.baz\\.bag', True);
print(conf.get('bar'));
#>>> {"baz.bag": True}

conf.delete('awesome');
print(conf.get('awesome'));
#>>>
```

## API

### Configstore(packageName, [defaults], globalConfigPath)

Returns a new instance.

#### packageName

Type: `str`

Name of your package.

#### defaults

Type: `dicts`

Default config.

#### globalConfigPath

Type: `bool`<br>
Default: `False`

Store the config at `$CONFIG/package-name/config.json` instead of the default `$CONFIG/configstore/package-name.json`. This is not recommended as you might end up conflicting with other tools, rendering the "without having to think" idea moot.

### Features

You can use dot-notation to set, get, update and delete nested dict properties

### .set(key, value)

Set an item.

### .set(object)

Set multiple items at once.

### .get(key)

Get an item.

### .has(key)

Check if an item exists.

### .delete(key)

Delete an item.

### .clear()

Delete all items.

### .all()

Get all the config as a dict or replace the current config with an object:

```python
conf.all({
	hello: 'world'
}) 
```

### .size

Get the item count.

### .path

Get the path to the config file. Can be used to show the user where the config file is located or even better open it for them.

## Contribute

Yes, you can contribute. Just dm on twitter:[@OyetokeT](http://twitter.com/@OyetokeT)

## TODO

There are couple of things I still need to add

1. Dot-notation: Currently, you can only set configs using this feature. (get, delete)

2. Stream: I planned to add a param that'll indicate that you want it to hit the file for every operation. Well that's how it works currently though. But to make it smarter, we don't need to hit the file for (size, get, has, all) operation. We are going to call the `.all()` once to get the configs in dicts and do the operation just using dict properties.

and more...

## License
Copyright - 2018

Oyetoke Toby twitter:[@OyetokeT](http://twitter.com/@OyetokeT)

MIT LICENSE