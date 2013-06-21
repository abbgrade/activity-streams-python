# activity-streams-python

Activity Streams Parser for Python


## Installation

	git clone git@github.com:apparentlymart/activity-streams-python.git
	cd activity-streams-python
	sudo python setup.py install

## Example

    from activitystreams.atom import make_activities_from_feed
    import urllib2
    import xml.etree.ElementTree

    url = 'https://github.com/apparentlymart/activity-streams-python/commits/master.atom'
    response = urllib2.urlopen(url)
    contents = response.read()
    xml_tree = xml.etree.ElementTree.fromstring(contents)
    xml_tree.getroot = lambda: xml_tree
    activities = make_activities_from_feed(xml_tree)
    for activity in activities:
        print activity.actor.name, activity.verb, activity.object.object_type, activity.object.url