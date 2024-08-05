---
title: Git&Github学习笔记
toc: true
tags:
	- git
	- github
categories:
	- 随笔
---

[toc]

很多年前我就使用过Github，但是这么多年我基本只会用`clone`来下载东西，从来没有通过本地进行推送过，原因也很简单，因为我本职工作还是产品设计，并不会系统的写一个大项目，但是最近我在学习swift的过程中，我很想实现在公司写的代码，在我家电脑也能同步出现，我知道这个问题通过NAS是可以实现的，但是感觉不够优雅，于是我就又找了一些Git的使用教程开始了稍微深入下的学习。

学习教程我找的是廖雪峰的Git学习教程：[Git教程](https://liaoxuefeng.com/books/git/introduction/)

要学习Git，首先是如何创建Git，我的设备是Mac+Win10。Mac本身自带有Git，Win10在官网下载安装下即可，这里不赘述了。

## 创建Git仓库

- 创建Git仓库：在本地随便创建一个文件夹，路径不要带中文，然后进入这个文件夹，输入`git init`。

```bash
 ~/Desktop/huixing/OpenSource/learnGit1/ git init
Initialized empty Git repository in /Users/daniellau/Desktop/huixing/OpenSource/learnGit1/.git/
 ~/Desktop/huixing/OpenSource/learnGit1/ [main]
```

输入完`git init`之后就出现了一个`[main]`，这个代表已经创建好git仓库，同时在`main`分支下。此时我们要做的就是可以在当前文件夹内创建文件，我们输入`echo "hello world" > test.md`创建一个`test.md`文件，并在这个文件中写入了一句“hello world”。

```bash
 ~/Desktop/huixing/OpenSource/learnGit1/ [main] echo "hello world" > test.md
 ~/Desktop/huixing/OpenSource/learnGit1/ [main] ls
test.md
```

此时我们查看下这个文件下所有文件，使用`ls -ah`查看所有文件，包括隐藏的文件。

```
 ~/Desktop/huixing/OpenSource/learnGit1/ [main] ls -ah
.       ..      .git    test.md
```

可以看到此时文件夹内包含一个`.git`目录跟`test.md`文件，说明这个Git仓库创建完成了。

## 本地使用Git

### Git基础操作

Git的使用之前我只用过`clone`，但是clone其实是最简单的，而且不是核心说白了就是下载，下面是我总结的Git的一些核心使用功能（可能不全，大神勿喷）：

- 查看仓库中的文件状态：`git status`，我们刚刚修改了本文，所以可以看到当前文件有修改。

```bash
 ~/Desktop/huixing/OpenSource/learngit/ [master*] git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   git-study-notes.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   git-study-notes.md
```

- 把文件添加到版本库：`git add filename`，如果需要把当前目录下所有有变更的文件都添加到版本库的话，直接使用`git add .`，这样会将当前目录下所有文件都提交到版本库。

```bash
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git add git-study-notes.md
 ~/Desktop/huixing/OpenSource/learngit/ [master+] git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   git-study-notes.md
```

- 把文件提交到仓库：`git commit -m "更新日志"`，上面已经把文件添加到版本库了，接下来就可以直接提交了，提交完我们再输入`git status`就可以看到没有变更的文件了。

```bash
 ~/Desktop/huixing/OpenSource/learngit/ [master+] git commit -m "更新文档"
[master 2eb6793] 更新文档
 1 file changed, 47 insertions(+), 4 deletions(-)
 ~/Desktop/huixing/OpenSource/learngit/ [master] git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

- 版本变动查看：`git diff`命令用于显示工作目录中文件的差异，可以查看未提交的更改、已暂存的更改，以及不同提交质检的差异。`git diff`可以显示当前工作目录中所有未暂存的更改，`git diff --cached`查看已经通过`git add`暂存但尚未提交的更改，`git diff HEAD`显示工作目录中所有未暂存和已暂存的更改。

- 版本回退：`git reset --hard HEAD^`，其中`HEAD^`代表是上一个提交（父提交），

  >  `--hard`：回退到上个已提交的版本；`--soft`：回退到上个版本的未提交状态；`--mixed`：回退到上个版本已添加但未提交的状态。

```
 ~/Desktop/huixing/OpenSource/learngit/ [master*] git reset --hard HEAD^
HEAD is now at a7ea889 git学习笔记初次提交
```

- 如果不小心回退错误了，可以再回退回来，首先我们通过`git reflog`查看所有提交。

```
2eb6793 (HEAD -> master) HEAD@{0}: reset: moving to 2eb6793
a7ea889 (origin/master, dev) HEAD@{1}: reset: moving to a7ea889
a7ea889 (origin/master, dev) HEAD@{2}: reset: moving to HEAD^
2eb6793 (HEAD -> master) HEAD@{3}: commit: 更新文档
a7ea889 (origin/master, dev) HEAD@{4}: checkout: moving from dev to master
a7ea889 (origin/master, dev) HEAD@{5}: checkout: moving from master to dev
a7ea889 (origin/master, dev) HEAD@{6}: merge dev: Fast-forward
0f264e0 HEAD@{7}: checkout: moving from dev to master
a7ea889 (origin/master, dev) HEAD@{8}: checkout: moving from master to dev
0f264e0 HEAD@{9}: checkout: moving from dev to master
a7ea889 (origin/master, dev) HEAD@{10}: commit: git学习笔记初次提交
0f264e0 HEAD@{11}: checkout: moving from master to dev
0f264e0 HEAD@{12}: merge dev: Fast-forward
8054cb6 HEAD@{13}: checkout: moving from dev to master
0f264e0 HEAD@{14}: checkout: moving from master to dev
8054cb6 HEAD@{15}: checkout: moving from dev to master
0f264e0 HEAD@{16}: commit: dev 增加
8054cb6 HEAD@{17}: checkout: moving from master to dev
8054cb6 HEAD@{18}: checkout: moving from dev to master
8054cb6 HEAD@{19}: checkout: moving from master to dev
8054cb6 HEAD@{20}: checkout: moving from master to master
8054cb6 HEAD@{21}: commit: test
59c9e41 HEAD@{22}: Branch: renamed refs/heads/main to refs/heads/master
59c9e41 HEAD@{24}: commit: test
```

- 然后比如我现在想回到`a7ea889`这个版本，我就可以通过`git reset --hard a7ea889`来进行恢复。

```
 ~/Desktop/huixing/OpenSource/learngit/ [master] git reset --hard a7ea889
HEAD is now at a7ea889 git学习笔记初次提交
```

- 日志查看：普通查看：`git log`；美化输出：`git log pretty=oneline`。

```bash
2651b23d2377fcd251f64b3bd79b877829d0062a (HEAD -> master, origin/master) 晚上22
点11分，家里windows电脑测试提交
eb69ca9a79be5b4edc7075ac7c93a1ded3fe0e3c 8月1日下午5点30修改提交
1e1596e2d2c9f5f439d3a63142d2b45eb810561a 8月1日下午13点38分提交更新
a7ea88956d0d83ebaf2b804ad20b772cb99718c2 (dev) git学习笔记初次提交
0f264e06e97eb05341ef3610c2e325d0dbfbb248 dev 增加
8054cb647c64b3a82f58e2a2eafdf2dc64f3aeb6 test
59c9e416a6b99afb917b1447e3c8ee510650b211 test
40ce877007cff1ce3e8b9249f1203bdd4b21f1e8 hhh
3cd45346ee768fe7f0f05b65b2e9c4444cfb539a first commit
```

- 撤销工作区修改：`git checkout -- filename`，通过当前指令将会撤销工作区的修改，不会影响暂存区，执行后，将会将代码恢复至暂存区的版本。

```bash
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git add readme.md
 ~/Desktop/huixing/OpenSource/learngit/ [master+] cat readme.md
# readme
Test111
hhh
这一行是dev的代码
我添加了一行文本，这行文本将被添加到暂存区。%
 ~/Desktop/huixing/OpenSource/learngit/ [master+] git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   git-study-notes.md
	modified:   readme.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   readme.md
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] cat readme.md
# readme
Test111
hhh
这一行是dev的代码
我添加了一行文本，这行文本将被添加到暂存区。
我现在又添加了一行代码，这样代码不添加到暂存区。%
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git checkout -- readme.md
 ~/Desktop/huixing/OpenSource/learngit/ [master+] cat readme.md
# readme
Test111
hhh
这一行是dev的代码
我添加了一行文本，这行文本将被添加到暂存区。
```

- 撤销暂存区修改：`git restore --staged file`，如果需要撤销暂存区的所有提交，可以执行当前指令，只会影响暂存区，不会影响工作区。

```
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git add readme.md
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] cat readme.md
# readme
Test111
hhh
这一行是dev的代码
我添加了一行文本，这行文本将被添加到暂存区。
我现在添加一行文本，这行文本先被添加到暂存区，接着再从暂存区撤销。%
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git restore --staged readme.md
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] cat readme.md
# readme
Test111
hhh
这一行是dev的代码
我添加了一行文本，这行文本将被添加到暂存区。%                                    ~/Desktop/huixing/OpenSource/learngit/ [master+*]
```

- 删除文件：`git rm file`，要删除文件不能光从本地删除，如果光从本地删除，此时版本库中还是有这个文件存在的。此时输入`git status`可以看到这个文件还存在于版本库中，然后我们可以用git rm file来删除这个文件。

```bash
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] rm readme.md
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   git-study-notes.md

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   git-study-notes.md
	deleted:    readme.md

 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git rm readme.md
rm 'readme.md'
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   git-study-notes.md
	deleted:    readme.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   git-study-notes.md
```

- 恢复文件：恢复文件分为两种情况，首先是只执行了`git rm file`，没有执行`git commit`时可以按下面的指令操作。先执行`git restore --staged filename`，然后再执行`git restore filename`，然后就可以看到文件被恢复了。

```
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git rm readme.md
rm 'readme.md'
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git restore --staged readme.md
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   git-study-notes.md

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   git-study-notes.md
	deleted:    readme.md

 ~/Desktop/huixing/OpenSource/learngit/ [master+*] ls
generateMobilePhoneNumber.py git-study-notes.md
 ~/Desktop/huixing/OpenSource/learngit/ [master+*] git restore readme.md
 ~/Desktop/huixing/OpenSource/learngit/ [master] ls
generateMobilePhoneNumber.py readme.md
git-study-notes.md
```

- 恢复文件：另一种情况是已经执行了`git commit`时，可以从之前的版本进行回复，比如通过上一个提交中恢复`git checkout HEAD~1 -- readme.md`。

```
 ~/Desktop/huixing/OpenSource/learngit/ [master] ls
generateMobilePhoneNumber.py git-study-notes.md
 ~/Desktop/huixing/OpenSource/learngit/ [master] git checkout HEAD~1 -- readme.md
 ~/Desktop/huixing/OpenSource/learngit/ [master+] ls
generateMobilePhoneNumber.py readme.md
git-study-notes.md
```

### 分支管理

Git还有一个很方便的功能就是可以进行分支管理，我之前经常写脚本的时候就会遇到我写好了一个脚本，跑起来没有任何问题，但是当我想修改时，往往会复制一份这个脚本，如果使用Git的话就不需要这么做了，我们只需要创建一个分支就可以解决了。

- 创建分支：首先我们创建一个`dev`分支，然后切换到该分支。使用指令`git checkout -b dev`，其中`-b`代表创建，`checkout`代表切换，`dev`代表分支的名称。Git2.23版本之后引入了新的命令`git switch -c dev`，其中`switch`代表切换，`-c`代表create创建，从可读性来说更好，建议使用最新的指令。

```
 ~/Desktop/huixing/OpenSource/learngit/ [master] git checkout -b dev
Switched to a new branch 'dev'
```

- 查看所有分支：通过`git branch`可以查看所有分支，我们来试试看：

```
 ~/Desktop/huixing/OpenSource/learngit/ [heads/dev] git branch -d dev
* dev
  master
```

- 可以看到，我们当前分支已经处于刚刚创建的`dev`分支上了，`*`代表当前分支。然后我们在创建一个`test`分支，这次我们仅创建，不切换，使用`git branch test`。

```
 ~/Desktop/huixing/OpenSource/learngit/ [heads/dev] git branch
* dev
  master
  test
```

- 切换分支：然后我们通过`git checkout test`来切换到`test`分支。这里特别注意，切换分支时，使用`git switch test`更容易理解，

```
 ~/Desktop/huixing/OpenSource/learngit/ [test] git switch test
Switched to branch 'test'
```

现在我做的所有改动都是在`test`分支上的，另外两个分支都没有我现在的内容。现在我们可以切换回`master`分支，可以发现`master`分支并没有我现在新录入的内容。

- 我现在在`test`分支做了很多修改，当我要切换到`dev`分支时，系统会阻止我直接切换，原因是我的`test`分支做了很多改动，直接切换的话，可能会导致数据丢失。

```
 ~/Desktop/huixing/OpenSource/learngit/ [test] git switch dev
error: Your local changes to the following files would be overwritten by checkout:
	git-study-notes.md
Please commit your changes or stash them before you switch branches.
```

按照正常的提交流程提交到版本库，这里还有一种做法可以使用`git stash`保存未提交的更改。

- 合并分支：现在`test`版本已经提交到版本库了，此时我们可以切换到`dev`版本进行版本合并，使用`git merge test`就可以把test版本的内容合并到`dev`，这里有可能存在冲突，存在冲突的情况就需要手动处理了。

```
 ~/Desktop/huixing/OpenSource/learngit/ [dev] git merge test
Updating a64220e..716d6b5
Fast-forward
 git-study-notes.md | 31 ++++++++++++++++++++++++++++++-
 1 file changed, 30 insertions(+), 1 deletion(-)
```

- 删除分支：合并完之后我们可以删除掉`test`分支，使用`git branch -d test`来删除`test`分支。

```
 ~/Desktop/huixing/OpenSource/learngit/ [dev] git branch -d test
Deleted branch test (was 716d6b5).
```

- 解决冲突：我们分别在两个分支`dev`跟`feature1`上的同一个文件`readme.md`编辑最后一行为不同的内容，从而导致这两个版本存在冲突，然后我们执行`git merge feature1`，此时Git会提示存在冲突。

```
 ~/Desktop/huixing/OpenSource/learngit/ [dev] git merge feature1
Auto-merging readme.md
CONFLICT (content): Merge conflict in readme.md
Automatic merge failed; fix conflicts and then commit the result.
 ~/Desktop/huixing/OpenSource/learngit/ [dev|merge+*]
```

我们查看下存在冲突的文件，使用`cat readme.md`进行查看。此时需要手动编辑当前文本，把`<<<<<<<`与`>>>>>>>`之间的代码手动编辑并解决冲突。

```
 ~/Desktop/huixing/OpenSource/learngit/ [dev|merge+*] cat readme.md
# readme
Test111
hhh
这一行是dev的代码
<<<<<<< HEAD
Creating a new branch is quick & simple.
=======
Creating a new branch is quick AND simple.

>>>>>>> feature1
```

- 解决完冲突之后再次提交。然后通过`git log --graph --pretty=oneline --abbrev-commit`来查看下日志，可以看到其中两个分支合并到了一起。最后删除`feature1`分支。

```
*   bb24a13 (HEAD -> dev) 解决冲突
|\
| * 5312add (feature1) AND simple
* | 695abbd & simple
|/
* 6a4cbc6 111
* ac38a92 删除test分支前提交
* 716d6b5 合并分支前提交，8月5日14点11分
* 94fb068 test
* a64220e (master) 切换分支前提交下
* ba085a3 "删除readme.md"
* ac60221 "test,下午13点30分提交"
* 1667a26 11点27提交
* 2651b23 (origin/master) 晚上22点11分，家里windows电脑测试提交
* eb69ca9 8月1日下午5点30修改提交
* 1e1596e 8月1日下午13点38分提交更新
* a7ea889 git学习笔记初次提交
* 0f264e0 dev 增加
* 8054cb6 test
* 59c9e41 test
* 40ce877 hhh
* 3cd4534 first commit
```

- 查看合并分支图：`git log --graph`。

```
*   commit bb24a132f8cd3e35b5e370cdd89b34d318587d0e (HEAD -> dev)
|\  Merge: 695abbd 5312add
| | Author: huixing <contact@liuyude.com>
| | Date:   Mon Aug 5 14:48:59 2024 +0800
| |
| |     解决冲突
| |
| * commit 5312addc649675d35024087f444069fd024bc31c
| | Author: huixing <contact@liuyude.com>
| | Date:   Mon Aug 5 14:36:39 2024 +0800
| |
| |     AND simple
| |
* | commit 695abbdc53ecdc570546547c2829887ceb7a0d52
|/  Author: huixing <contact@liuyude.com>
|   Date:   Mon Aug 5 14:38:00 2024 +0800
|
|       & simple
|
* commit 6a4cbc6a6e1a25ae7bd3e0602cfb2a93659933e0
| Author: huixing <contact@liuyude.com>
| Date:   Mon Aug 5 14:35:00 2024 +0800
|
|     111
```

- 标签管理：使用`git tag tagname`可以创建标签，使用`git tag`查看所有标签

```
 ~/Desktop/huixing/OpenSource/learngit/ [master] git tag v1.0
 ~/Desktop/huixing/OpenSource/learngit/ [master] git tag
v1.0
```

