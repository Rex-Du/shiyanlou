文本插值

通常使用两对大括号来进行文本的插值操作。使用起来非常简单方便。

<span>Hello: {{ name }}</span>

在大括号中，我们还可以使用简单的 javascript 表达式，比如算术操作，三元运算等。

{{ number + 1 }}
{{ ok ? 'YES' : 'NO' }}
{{ message.split('').reverse().join('') }}

HTML 插值

文本插值通常只能插入纯文本内容，如果想要插入 html 代码并显示正确的效果，则可以使用 v-html 指令。

<div v-html="html"></div>

接着图的右边，我把内容分为了三个部分，上方的 template，中间的 script ，下方的 style 。基本上所有的组件文件都是这样的结构，前面介绍的基本语法，都是在 template 和 script 中进行操作，style 是用来对这个组件的样式进行调节的。注意在 style 标签中，有一个 scoped 的字符串，如果添加了这个单词，那么你写的样式代码就只会在这个组件文件中生效，即限制了 css 的作用域。如果没有这个单词，那么你写的样式代码将会影响到整个页面，其他组件的样式也会受到影响，所以为了保证样式的正确使用，一般建议加上 scoped 这个单词，除非你的目的就是写全局的样式。

安装依赖
cd syl-editor
npm install