Mellanox Exporter

I needed a tool to read from cl-support files and but every log file to a graylog
 server

So i wrote one

You'll need to specify the source directory where the cl-support files reside

then a graylog server with tcp gelf receiver

and run this tool once

it will

- de-compress
- seek log files in /var/log folder
- read them line by line and push the logs to gray log server

Why is this needed ?

i have a large fabric and sn2700 has only 2 puny cpus 
forwarding a lot of logs was not an option 

so i download the cl-supports then upload them to graylog.
