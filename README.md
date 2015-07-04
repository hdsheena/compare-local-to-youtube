# compare-local-to-youtube
I wanted to compare the videos I've uploaded to youtube to those on my local directory. Youtube will automatically detect and remove duplicates, but not until after I've uploaded the files. This wastes bandwidth and time.
I used the youtube API to get the titles of all the videos I've uploaded. They mostly include the file names, and the relevant piece for most of them is the numbered section of each name (ie: SAM_0001). Using that, I was able to easily detect which videos had not yet been uploaded.
