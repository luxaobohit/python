<h1> Python中requests库的总结</h1>

<li>
  <h3><code>HTTP</code>协议</h3>
</li>
  <p>
  <code>HTTP</code>协议<code>Request </code>向服务器发送请求，请求消息的结构分为3部分，第一部分叫请求行， 第二部分叫<code>http header</code>, 第三部分是<code>body</code>. <code>header</code>和<code>body</code>之间有个空行.第一行中的<code>Method</code>表示请求方法，比如<code>POST</code>， <code>GET</code>， <code>Path-to-resoure</code>表示请求的资源，
<code>Http/version-number</code> 表示<code>HTTP</code>协议的版本号.当使用的是<code>GET</code> 方法的时候， <code>body</code>是为空的. 使用<code>POST</code>方法是可以添加参数。
  <li>
    <code>res = requests.get(url, params = params, **kwargs)</code>
  </li>
  <li>
    <code>res = requests.post(url, data = payload, json = None, **kwargs)</code>其中<code>json</code>是<code>body</code>中可以发送的数据.<code>params</code>是可以传入的参数.<code>get</code>和<code>post</code>还可以传入<code>headers = headers </code>参数和<code>verify = True/False</code>参数,<code>verify = True </code>和<code>verify = False </code>表示是否信任该网站（证书问题相关）.
  </li>
  </p>

<p><code>requests</code>请求方式采用<code>get</code>还是<code>post</code>通过Fiddler抓包分析，以及是否带<code>headers</code>

<li>
  <h3><code>requests</code>请求服务器应答后返回信息的处理</h3>
</li>
  <p>返回的是<code>HTML</code>就用<code>BeautifulSoup</code>中<code>select</code>方法来选取元素处理.</br>
  返回的是<code>json</code>就通过<code>python</code>自带的<code>json</code>库来处理变成<code>dict</code>然后提取出所需要的信息.

<li>
  <h3><code>re</code>正则表达式</h3>
</li>
<p><a href = "http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html">点击此处学习正则表达式</a></p>
