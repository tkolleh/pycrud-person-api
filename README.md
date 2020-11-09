<!-- --- -->
<!-- title: Python CRUD on Person Project Notes -->
<!-- date: 2020-10-28 -->
<!-- author: tkolleh -->
<!-- pandocomatic_: -->
<!--   use-template: marked -->
<!--   pandoc: -->
<!--     self-contained: true -->
<!-- tags: -->
<!--   - project -->
<!--   - interview -->
<!-- --- -->

# CRUD on person project, Python edition

 CRUD on person projects are a series of simple API applications for the exploration of different languages, frameworks and libraries.

# Build from source

Place a configuration file (*config.ini*) in the project root directory. The same directory as the *Dockerfile*, *setup.sh*, and *build-image.sh* files. Ensure that the bash scripts are executable by running `chmod u+x <script name>`.

Run the *build-image.sh* file to build.

# Run the application

Ensure docker is installed and running. Execute the *setup.sh* file to start a docker container as an executable with the application.

# Design

## MongoDB document versioning pattern

This pattern can handle larger number of documents with infrequent revisions, and the majority of searches (GETs) are for the current document version. The `persons` collection contains current document versions. Changes to the current document trigger the creation of a revision. Saved in the `person_revisions` collection.

