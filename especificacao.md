<h1>Funções para o bot do @grupos_ti</h1>

<h3> Navegação por categorias:</h3>
<ul>
<li>Permite que o usuário veja todos os grupos e canais, por meio de botões que aparecerão na tela</li>
<li>Inicialmente, os botões seriam "Grupos", "Canais" e "Todos", que indicariam ao bot para mostrar, respectivamente, "somente grupos", "somente canais", ou "ambas as opções" (opção padrão).</li>
<li>Nessa mesma mensagem inicial, também apareceriam os botões "Todos" ou "Selecionar Idiomas". Se o usuário optasse por "todos" (opção padrão), apareceriam grupos/canais de todos os idiomas. Se optasse por "Selecionar Idiomas", poderia escolher os idiomas <i>(pt, en, es, de, it).</i></li>
<li>Então, apareceriam categorias, como "Programação" ou "Linux", em forma de botões. Ao selecionar alguma delas, ou o bot mostraria mais opções de categorias (caso ele selecionasse "Linux", por exemplo, em que apareceria "Ubuntu", "Arch", etc..), ou mostraria apenas grupos de uma sub-categoria (caso ele selecionasse "Ubuntu", por exemplo, já que não haveria mais sub-categorias para mostrar).</li>
<li><i>Essa função de navegação por categorias só ocorreria no privado do Bot. Ela não poderia ser usada em grupos, por exemplo.</i></li>
<li><i>Sempre seriam mostradas as opções "Voltar" e "Mostrar grupos/canais"</i>.</li>
</ul>

<h3>Busca inline de grupos/canais:</h3>
<ul>
<li><i>Seria um recurso</i> <a href="https://core.telegram.org/bots/inline">inline</a>.</li>
<li>Possibilitaria buscar grupos e canais via inline</li>
</ul>
Usaria a seguinte sintaxe:
<pre>@grupos_tiBot [#grupo|#canal] [#pt, #br, #en, #es, #it, #de] <i>sua busca aqui</i></pre>
Caso algum campo opcional fosse otimido, seria usada a opção padrão (buscar tudo)


<b>Exemplos na prática</b>:
<ul><li>Para buscar grupos e canais de Zabbix:</li>
<pre>@grupos_tiBot zabbix</pre>
<li>Para buscar grupos de Python regionais:</li>
<pre>@grupos_tiBot #grupo #br python</pre>
<li>Para buscar canais de Linux em inglês e espanhol:</li>
<pre>@grupos_tiBot #canal #en #pt linux</pre>
</ul>
