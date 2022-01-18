Demo for HyperParameter and Video Capture
========================================

This demo shows how to develop operators and pipelines using pip-based repo, and control towhee/operator behavior with hyperpatameter.

Prepare
-------

towhee source code on brance `new_hub` is required for this demo:

```shell
$ git fetch -a            # sync the git repo
$ git checkout new_hub    # change to develop branch
$ pip uninstall towhee    # switch towhee version
$ python setup.py develop # or python setup.py develop
```

`towheeoperator` is a git repo hosting the source code for operator/pipeline.

```shell
$ git clone https://github.com/reiase/towheeoperator.git
$ cd towheeoperator
$ pip uninstall towheeoperator-imread towheeoperator-imshow
$ towhee develop -i imread # -i for installation
$ towhee develop -i imshow
$ towhee execute -n 100 video_cap/video_cap.yaml
```

Examples
--------

### develop operators

```shell
$ towhee develop -d imread # -d for development
$ towhee develop -d imshow
$ towhee execute -n 100 video_cap/video_cap.yaml
```

### control operator behavior with hyperparameter

```shell
$ towhee execute -n 100 -Dtowheeoperator.imread.scale=0.2 video_cap/video_cap.yaml
```
`towheeoperator.imread.scale` is the parameter controlling image scaling in `imread`.