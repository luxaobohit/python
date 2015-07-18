<h1> Python中requests库的总结</h1>

<li>
  <h3><code>HTTP</code>协议</h3>
</li>
  <p>
  <code>HTTP</code>协议<code>Request </code>消息的结构分为3部分，第一部分叫请求行， 第二部分叫<code>http header</code>, 第三部分是<code>body</code>. <code>header</code>和<code>body</code>之间有个空行.</br>
  第一行中的<code>Method</code>表示请求方法，比如<code>POST</code>， <code>GET</code>， <code>Path-to-resoure</code>表示请求的资源，
<code>Http/version-number</code> 表示<code>HTTP</code>协议的版本号.当使用的是<code>GET</code> 方法的时候， <code>body</code>是为空的. 使用<code>POST</code>方法是可以添加参数。
  <li>
    <code>res = requests.get(url, params = params, **kwargs)</code>
  </li>
  <li>
    <code>res = requests.post(url, data = payload, json = None, **kwargs)</code>其中<code>json</code>是<code>body</code>中可以发送的数据.<code>params</code>是可以传入的参数.
  </li>
  </p>

<p><code>requests</code>向服务器发送请求，请求方式有两种<code>get</code>和<code>post</code>
<li>get method
