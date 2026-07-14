# DevOps CI 入门实操项目

这是一个给 DevOps CI 新人练手的小项目。目标不是写复杂业务，而是把 CI 的核心链路跑通：

1. 代码提交
2. 自动安装依赖
3. 自动执行测试
4. 自动做静态检查
5. 构建 Docker 镜像
6. 在 Pull Request 或 push 时自动验证

## 你会学到什么

- Git 的基本工作流
- CI 流水线的阶段划分
- 单元测试为什么是 CI 的底座
- Dockerfile 如何把应用打包成镜像
- GitHub Actions 的基础语法
- 失败流水线如何定位问题

## 项目结构

```text
devops-ci-lab/
  app/
    calculator.py
  tests/
    test_calculator.py
  .github/
    workflows/
      ci.yml
  Dockerfile
  Makefile
  requirements.txt
  README.md
```

## 本地练习

安装依赖：

```bash
python -m pip install -r requirements.txt
```

运行测试：

```bash
python -m pytest
```

运行静态检查：

```bash
python -m ruff check .
```

构建 Docker 镜像：

```bash
docker build -t devops-ci-lab:local .
```

运行容器：

```bash
docker run --rm devops-ci-lab:local
```

## 第一次 CI 实操

1. 在 GitHub 创建一个空仓库，例如 `devops-ci-lab`。
2. 在本地执行：

```bash
git init
git add .
git commit -m "init ci lab"
git branch -M main
git remote add origin https://github.com/<你的用户名>/devops-ci-lab.git
git push -u origin main
```

3. 打开 GitHub 仓库的 `Actions` 页面，观察 `CI` 工作流。
4. 故意把 `app/calculator.py` 里的加法写错，再提交一次，观察 CI 失败。
5. 修复代码，再提交，观察 CI 恢复成功。

## 学习节奏建议

第一周只盯住一件事：让 CI 跑起来，并能看懂失败原因。

每天练 30 到 60 分钟即可。不要急着背工具名，先形成肌肉记忆：改代码、跑测试、提交、看流水线、修失败。
