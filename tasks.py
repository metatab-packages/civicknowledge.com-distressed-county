# Task definitions for invoke
# You must first install invoke, https://www.pyinvoke.org/

# You can also create you own tasks
from invoke import task
import metapack as mp

from metapack_build.tasks.package import ns

# To configure options for invoke functions you can:
# - Set values in the 'invoke' section of `~/.metapack.yaml
# - Use one of the other invoke config options:
#   http://docs.pyinvoke.org/en/stable/concepts/configuration.html#the-configuration-hierarchy
# - Set the configuration in this file:

# ns.configure(
#    {
#        'metapack':
#            {
#                's3_bucket': 'bucket_name',
#                'wp_site': 'wp sot name',
#                'groups': None,
#                'tags': None
#            }
#    }
# )

# However, the `groups` and `tags` hould really be set in the `metatada.csv`
# file, and `s3_bucket` and `wp_site` should be set at the collection or global level


@task
def set_descriptions(c):
    """Set the descriptions of the columns from the upstram data source"""
    
    pkg = mp.open_package('.')
    r = pkg.resource('distressed_counties')
    
    
    ur = pkg.reference('ffeic_distressed') # Upstream resource
    upkg = ur.resolved_url.package_url.doc # Upstrem package
    
    ucols = upkg.resource(ur.resource.name).columns()
    
    dmap = { c['header']:c['description'] for c in ucols}
    
    def get_desc(h):
        for k,v in dmap.items():
            if h.startswith(k):
                
                if '_pop_pct' in h:
                    return "Percentage of population in county in tracts with flag: "+v
                elif '_pop' in h:
                    return "Population in county in tracts with flag: "+v
                elif '_pct' in h:
                    return "Percentage of tracts in county with flag: "+v
                else:
                    return "Count of tracts in county with flag: "+v
             
    
    for c in r.schema_term.find('Table.Column'):
        desc = get_desc(c.name)
        
        if desc and not c['description']:
            c['description'] = desc
        
    
    pkg.write()
    

ns.add_task(set_descriptions)
