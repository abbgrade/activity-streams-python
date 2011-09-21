from rfc3339 import rfc3339

class Activity(object):
    actor = None
    object = None
    target = None
    verb = None
    time = None
    generator = None
    icon_url = None
    service_provider = None
    links = None

    def __init__(self, actor=None, object=None, target=None, verb=None, time=None, generator=None, icon_url=None, service_provider=None, links=None):
        self.actor = actor
        self.object = object
        self.target = target
        self.verb = verb
        self.time = time
        self.service_provider = service_provider
        self.generator = generator
        self.icon_url = icon_url

        if links is not None:
            self.links = links
        else:
            self.links = []
            
    def to_json(self):
        activity_dict = {
            'actor': self.actor,
            'object': self.object,
            'target': self.target,
            'verb': self.verb,
            'published': self.time,
            'service_provider': self.service_provider,
            'generator': self.generator,
            'icon_url': self.icon_url
        }
        return jsonify(activity_dict)

class Object(object):
    id = None
    name = None
    url = None
    object_type = None
    summary = None
    image = None
    in_reply_to_object = None
    attached_objects = None
    reply_objects = None
    reaction_activities = None
    action_links = None
    upstream_duplicate_ids = None
    downstream_duplicate_ids = None
    links = None

    def __init__(self, id=None, name=None, url=None, object_type=None, summary=None, image=None, in_reply_to_object=None, attached_objects=None, reply_objects=None, reaction_activities=None, action_links=None, upstream_duplicate_ids=None, downstream_duplicate_ids=None, links=None):
        self.id = id
        self.name = name
        self.url = url
        self.object_type = object_type
        self.summary = summary
        self.image = image
        self.in_reply_to_object = in_reply_to_object

        if attached_objects is not None:
            self.attached_objects = attached_objects
        else:
            self.attached_objects = []

        if reply_objects is not None:
            self.reply_objects = reply_objects
        else:
            self.reply_objects = []

        if reaction_activities is not None:
            self.reaction_activities = reaction_activities
        else:
            self.reaction_activities = []

        if action_links is not None:
            self.action_links = action_links
        else:
            self.action_links = []

        if upstream_duplicate_ids is not None:
            self.upstream_duplicate_ids = upstream_duplicate_ids
        else:
            self.upstream_duplicate_ids = []

        if downstream_duplicate_ids is not None:
            self.downstream_duplicate_ids = downstream_duplicate_ids
        else:
            self.downstream_duplicate_ids = []

        if links is not None:
            self.links = links
        else:
            self.links = []
        
    def to_json(self):
        object_dict = {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'object_type': self.object_type,
            'summary': self.summary,
            'image': self.image,
            'attachments': None,
            #'in_reply_to_object': self.in_reply_to_object,
            #'reply_objects': self.reply_objects,
            #'reaction_activities': self.reaction_activites,
            #'action_links': self.action_links,
            'upstream_duplicate_ids': self.upstream_duplicate_ids,
            'downstream_duplicate_ids': self.downstream_duplicate_ids
            #'links': self.links,
        }
        if self.attached_objects:
            attachments = []
            for obj in self.attached_objects:
                attachments.append(obj.to_json())
            object_dict['attachments'] = attachments
        return jsonify(object_dict)


class MediaLink(object):
    url = None
    media_type = None
    width = None
    height = None
    duration = None

    def __init__(self, url=None, media_type=None, width=None, height=None, duration=None):
        self.url = url
        self.media_type = media_type
        self.width = width
        self.height = height
        self.duration = duration
        
    def to_json(self):
        medialink_dict = {
            'url': self.url,
            'media_type': self.media_type,
            'width': self.width, 
            'height': self.height,
            'duration': self.duration 
        }
        return medialink_dict


class ActionLink(object):
    url = None
    caption = None

    def __init__(self, url=None, caption=None):
        self.url = url
        self.caption = caption


class Link(object):
    url = None
    media_type = None
    rel = None

    def __init__(self, url=None, media_type=None, rel=None):
        self.url = url
        self.media_type = media_type
        self.rel = rel


def jsonify(dictionary):
    classes = ['actor', 'generator', 'object', 'provider', 'target', 'author'
                'image' ]
    datetimes = ['published', 'updated']
    for d in datetimes:
        if d in dictionary.keys() and dictionary[d]:
            dictionary[d] = rfc3339(dictionary[d])
    for c in classes:
        if c in dictionary.keys() and dictionary[c]:
            dictionary[c] = dictionary[c].to_json()
    for k,v in dictionary.items():
        if v == []:
            dictionary[k] = None
    return dictionary
    