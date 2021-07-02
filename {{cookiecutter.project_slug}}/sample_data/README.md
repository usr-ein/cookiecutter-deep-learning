# Sample Data Guidelines

This is Machine Learning, we won't deal with a small amount of data, but at least 10 GBs. Therefore, datasets shan't be commited into this repository.

To host dataset, either:

 - [Host it yourself on AcademicTorrents](https://academictorrents.com/) if it's a public dataset
 - Save it to AWS S3 and keep a local copy
 - Save it locally

## Commiting the files nonetheless

If you decide, nonetheless, to commit large data files, here are a few guidelines to abid by to prevent Git LFS from kicking in:

 - Keep the individual file size strictly under 50 MiB (!= MB). This is the trigger for Git LFS.
 - Do no exceed a total of 4 GiB for the sample data. Going above a total of 5 GiB will make cloning slow and use a lot of bandwidth, which might make GitHub convert the remote repo into Git LFS.
 - Do not delete those files later. Files deleted later are still tracked in GIT, and hence still contribute to the total size. When you add the data, don't edit the data, but instead write a script or something to convert it to whatever you need.

## Git Large File System

Git LFS is the solution in theory, but in practice it's a pain to deal with. I don't want to use it, but there is no option to explicitly disable it in GitHub.

After some extraneous testing, I've found that as long as the individual file sizes are strictly under 50 MiB, then GitHub won't prompt you to use Git LFS. Furthermore, GitHub imposes a limit on the total repo size and the bandwidth used when pulling/pushing. I have found that as long as the total repo size is less than 5 GiB, Git LFS isn't kicked in either. It may still not kick in above 5 GiB of total repo size, but I haven't tested beyong that limit.

If you see a file which should be large in binary format but instead just contains something resembling:

```
version https://git-lfs.github.com/spec/v1
oid sha256:4cac19622fc3ada9c0fdeadb33f88f367b541f38b89102a3f1261ac81fd5bcb5
size 84977953
```

Then I would advise you to remove the repo from GitHub and start over, because [the process to uninstall Git LFS once it has taken hold is neigh impossible to carry out without casualties](https://github.com/git-lfs/git-lfs/issues/3026).
