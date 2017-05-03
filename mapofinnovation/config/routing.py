"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    map.connect('/map', controller="uifunc", action="index")
    map.connect('/about', controller="uifunc", action="about")
    map.connect('/about/goals', controller="uifunc", action="goals")
    map.connect('/docs', controller="uifunc", action="userDocs")
    map.connect('/docs/developer', controller="uifunc", action="devDocs")
    map.connect('/contact', controller="uifunc", action="contactus")
    map.connect('/wiki', controller="uifunc", action="wiki")
    map.connect('/join', controller="uifunc", action="joinus")
    map.connect('/editspace', controller="uifunc", action="editspace")
    map.connect('/gig', controller="uifunc", action="gigmap")
    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    return map
