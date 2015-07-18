<h1> Python中requests库的总结</h1>

<li>
  <code>HTTP</code>协议
</li>
  <p>
  <code>HTTP</code>协议<code>Request </code>消息的结构分为3部分，第一部分叫请求行， 第二部分叫<code>http header</code>, 第三部分是<code>body</code>. <code>header</code>和<code>body</code>之间有个空行.
　　第一行中的<code>Method</code>表示请求方法，比如<code>POST</code>， <code>GET</code>， <code>Path-to-resoure</code>表示请求的资源，
<code>Http/version-number</code> 表示<code>HTTP</code>协议的版本号.当使用的是<code>GET</code> 方法的时候， <code>body</code>是为空的. 使用<code>POST</code>方法是可以添加参数。

<p>requests向服务器发送请求，请求方式有两种<code>get</code>和<code>post</code>
<li>get method
