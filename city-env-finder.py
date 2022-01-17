import sys
# import subprocess
import os
import json

if __name__ == "__main__:
  city = os.environ.get("CITY")
  res = ""
  with open("kubernetes_deployment_mapping.json") as json_file:
    data = json.load(json_file)
    for env in data['prod']:
      for i in data['prod'][env]:
        if i == city:
          os.environ['ENV'] = str(env)
          res = str(env)
        
  #save_path = '/var/lib/jenkins/jobs/recycle-live-city/workspace"
  #file_name = "env_result.txt"
  #complete_name = os.path.join(save_path, file_name)
  f = open("env_result.txt", "w")
  f.write(res)
  f.close()
  # sys.path.append(os.environ['WORKSPACE'])
  # sys.path.append('city_env_checker/bin/activate')
