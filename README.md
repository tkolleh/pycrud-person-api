---
title: Python CRUD on Person Project Notes
date: 2020-10-28
author: tkolleh
pandocomatic_:
  use-template: marked
  pandoc:
    self-contained: true
tags:
  - project
  - interview
---

# Python CRUD on Person Project Notes

## MongoDB design

```{.plantuml caption="MongoDB Documents"}
@startuml
Person o-- PersonCollection
@enduml
```

## MongoDB document versioning pattern

This pattern can handle larger number of documents with infrequent revisions, and the majority of searches (GETs) are for the current document version.


## Test Data

All test data was generated using [mockaroo](https://mockaroo.com/).
