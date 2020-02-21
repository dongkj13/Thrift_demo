# Thrift_demo

## 首先定义thirft文件

```thrift
service HelloWorld {
string ping(),
string say(1:string msg)
}
```

## 用定义好的thrift文件生成我们需要的目标语言的源码。

```sh
thrift --gen py HelloWord.thrift
```

## 生成server端、client端代码

## 运行

```sh
python server.py

python client.py
```