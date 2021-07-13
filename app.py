import pandas as pd

from dijkstar import Graph, find_path
def load(speed , time):
  dist_df = pd.read_csv('Node_details.csv')
  cost_df = pd.read_csv('traffic_timed_nodes.csv')
  graph = Graph()
  Time = time
  for ind in range(0,20):
    src = dist_df.iloc[ind,0]
    tar = dist_df.iloc[ind,1]
    tm = ''
    if int(Time.split(':')[1]) < 30:
      tm = Time.split(':')[0]+':00'
    else :
      tm = Time.split(':')[0]+':30'
    graph.add_edge(src , tar, ( dist_df.iloc[ind,2] / speed ) + cost_df.loc[src,tm]+ cost_df.loc[tar,tm])
    graph.add_edge(tar,src, ( dist_df.iloc[ind,2] / speed ) + cost_df.loc[src,tm]+ cost_df.loc[tar,tm])
  return graph
def path(speed,time,src,tar):
  grp = load(speed,time)
  return find_path(grp, src,tar).nodes


print(path(70,'09:00',1,4))

  
from flask import Flask
app = Flask(__name__)
  
@app.route('/')
def hello_name():
   return 'Welcome To API endpoint add in url /<src>_<tar>'

@app.route('/<src>/<tar>')
def Traverse(src,tar):
    src = int(src)
    tar = int(tar)
    return str(path(70,'09:00',src,tar))

if __name__ == '__main__':
   app.run(debug = True)