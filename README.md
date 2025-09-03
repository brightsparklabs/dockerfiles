# dockerfiles

Scripts and files for the `Docker` images used as base templates at
brightSPARK Labs.

# Build

```shell
./gradlew buildDockerImages
```

# Publish

- Tag the new version of the repo:

```shell
git checkout develop
git pull
git tag -m '<ticket>: Tag version v<X.Y.Z>' -a '<X.Y.Z>'
git checkout master
git pull
git merge develop
git branch -l
# Delete any old branches with `git branch -D <branch>`
git push --all
git push --tags
```

- The CI server will automatically publish the new images.

# Licenses

Refer to the `LICENSE` file for details.

