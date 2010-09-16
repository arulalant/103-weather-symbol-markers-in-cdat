import vcs, cdms2, cdutil
import time,os, sys

# Open data file:
filepath = os.path.join(sys.prefix, 'sample_data/clt.nc')
cdmsfile = cdms2.open( filepath )

# Extract a 3 dimensional data set and get a subset of the time dimension
#data = cdmsfile('clt', longitude=(-180, 180), latitude = (-180., 180.)) 
data = cdmsfile('clt', longitude=(60, 100), latitude = (0., 40.))   # for india 

# Initial VCS.
v = vcs.init()


# Now get the line 'continents' object.
lc = v.getline('continents')
# Change line attribute values
lc.color=30#light blue #244 # light blue #250 dark blue
lc.width=1
#lc.list()
cf_asd = v.getboxfill( 'ASD' )
cf_asd.datawc(1e20,1e20,1e20,1e20) # change to default region
#cf_asd.datawc(0,0,80,80)
cf_asd.level_1=1e20          # change to default minimum level
cf_asd.level_2=1e20          # change to default maximum level
cf_asd.color_1=240         # change 1st color index value
cf_asd.color_2=240  # change 2nd color index value
cf_asd.yticlabels1={0:'0',5:'5',10:'10',15:'15',20:'20',25:'25',30:'30',35:'35',40:'40'}

# our own template
# Assign the variable "t_asd" to the persistent 'ASD' template.
t_asd = v.gettemplate( 'ASD' )

		
t_asd.data.priority = 1
t_asd.legend.priority = 0
					  
t_asd.max.priority = 0
t_asd.min.priority = 0
t_asd.mean.priority = 0
#t_asd.source.priority = 1
t_asd.title.priority = 0
t_asd.units.priority = 0
t_asd.crdate.priority = 0
t_asd.crtime.priority = 0
t_asd.dataname.priority = 0
t_asd.zunits.priority = 0
t_asd.tunits.priority = 0
t_asd.xname.priority = 0
t_asd.yname.priority = 0
		
t_asd.xvalue.priority = 0
t_asd.yvalue.priority = 0
t_asd.tvalue.priority = 0
t_asd.zvalue.priority = 0
t_asd.box1.priority = 0
            
t_asd.xlabel2.priority = 1
t_asd.xtic2.priority = 0
# set the right y-axis (second y axis) to be blank (priority=0)
t_asd.ylabel2.priority = 0
t_asd.ytic2.priority = 0
# set the top x-axis (secind y axis) to be blank
t_asd.xlabel1.priority = 0
t_asd.xtic1.priority = 0
# set the right y-axis (second y axis) to be blank (priority=0)
t_asd.ylabel1.priority = 1
#t_asd.ymintic1.priority = 1
t_asd.ytic1.priority = 0
		
t_asd.scalefont(0.1) # lat and long text font size

#t_asd.ylabel1.list()

v.plot( data, t_asd ,cf_asd,bg=0)

v.update()


arr=[]
t=[]
c=[]
s=[]
for i in range(0,14):
	arr.append(0)
	t.append(0)
	c.append(0)
	s.append(0)
# plotting marker
m=v.createmarker()
mytmpl=v.createtemplate()
m.viewport=[mytmpl.data.x1,mytmpl.data.x2,mytmpl.data.y1,mytmpl.data.y2] # this sets the area used for drawing
m.worldcoordinate=[60.,100.,0,40]
#use m.viewport and m.wordcoordinate to define you're area
t[0]=None
t[1]=113
c[0]=None
c[1]=85



s[0]=10
s[1]=10
s[2]=10
s[3]=10
s[4]=10
s[5]=10
s[6]=10
s[7]=10
s[8]=10
s[9]=20
s[10]=20
s[11]=10
s[12]=20
s[13]=10





m.type=[190,191,192,193,194,195,196,197,198,199,200,201,202]	
m.color=[241,241,241,241,241,241,241,241,241,241,242,242,242]
size=[]
for i in range(0,14):
	size.append(s[i])

m.size=size

m.x=[[64],[68],[76],[70],[77],[65],[78],[81],[88],[86],[89],[92],[95]]#,[64],[62],[64],[68],[70],[73],[75],[78],[82],[84],[86],[89],[92],[95],[97],[74],[79],]
m.y=[[33],[35],[35],[15],[25],[18],[18],[35],[5],[35],[15],[35],[35]]#,[15],[10],[10],[10],[15],[10],[6],[12],[10],[10],[10],[10],[10],[10],[10],[25],[25],]
v.update()
v.plot(m,bg=0)

#v.svg("/home/arulalan/marker3",width=30,height=30,units="cm")
raw_input()7
