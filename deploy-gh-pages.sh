#!/bin/bash

#Simple script for deploying this blog to github pages.
git add result

git commit -m "Subtree"
git push origin `git subtree split --prefix result main`:gh-pages --force
git reset --hard HEAD~1
