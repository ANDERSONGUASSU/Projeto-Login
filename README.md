
<h1>Projeto de Gerenciamento de Usuários</h1>

<h2>Descrição do Projeto</h2>
<p>Este projeto é uma aplicação para gerenciamento de usuários, incluindo funcionalidades como cadastro, login, alteração de senha e verificação por email. Utiliza o framework <code>customtkinter</code> para a interface gráfica e <code>SQLAlchemy</code> para gerenciamento do banco de dados.</p>

<h2>Funcionalidades Principais</h2>
<ul>
<li>Cadastro de novos usuários.</li>
<li>Autenticação de usuários.</li>
<li>Atualização de senha.</li>
<li>Envio de código de verificação por email.</li>
</ul>

<h2>Configuração e Instalação</h2>

<h3>Requisitos</h3>
<ul>
<li>Python 3.8 ou superior</li>
<li>Pacotes listados em <code>requirements.txt</code></li>
</ul>

<h3>Passos de Instalação</h3>
<ol>
<li>Clone o repositório:
<pre><code>git clone &lt;URL do repositório&gt;
cd &lt;d</code></pre>
</li>
<li>Crie um ambiente virtual:
<pre><code>python -m venv venv
source venv/bin/activate # ou .\venv\Scripts\activate no Windows</code></pre>
</li>
<li>Instale as dependências:
<pre><code>pip install -r requirements.txt</code></pre>
</li>
<li>Crie um arquivo <code>.env</code> na raiz do projeto com as seguintes variáveis:
<pre><code>DB_MENAGER=&lt;seu_gerenciador_de_banco_de_dados&gt;
DB_USER=&lt;seu_usuario_de_banco_de_dados&gt;
PASSWORD=&lt;sua_senha_de_banco_de_dados&gt;
HOST=&lt;seu_host_de_banco_de_dados&gt;
DB=&lt;nome_do_seu_banco_de_dados&gt;
EMAIL=&lt;seu_email_para_envio_de_codigo_de_verificacao&gt;
EMAIL_PASSWORD=&lt;token_de_senha_gerado&gt;</code></pre>
</li>
<li>Gere um token de senha para seu email:
<ol>
<li>Vá para <a href="https://security.google.com/settings/security/apppasswords">Google App Passwords</a>.</li>
<li>Selecione a opção “Outro” para definir um nome para seu projeto.</li>
<li>Gere o token e use-o na variável <code>EMAIL_PASSWORD</code>.</li>
</ol>
</li>
<li>Inicialize o banco de dados:
<pre><code>python -c 'from models import Base, engine; Base.metadata.create_all(engine)'</code></pre>
</li>
</ol>

<h2>Uso</h2>

<ol>
<li>Para iniciar a aplicação, execute:
<pre><code>python main.View.py</code></pre>
</li>
<li>Utilize a interface gráfica para:
<ul>
<li>Registrar novos usuários.</li>
<li>Fazer login.</li>
<li>Alterar senha.</li>
<li>Enviar código de verificação por email.</li>
</ul>
</li>
</ol>

<h2>Estrutura do Projeto</h2>

<ul>
<li><strong>view/</strong>
<ul>
<li><code>registerView.py</code>: Tela de cadastro de novos usuários.</li>
<li><code>changePassword.py</code>: Tela de alteração de senha.</li>
<li><code>main.View.py</code>: Tela principal após login.</li>
</ul>
</li>
<li><strong>controller/</strong>
<ul>
<li><code>controllerUser.py</code>: Controlador para operações com usuários.</li>
</ul>
</li>
<li><strong>models/</strong>
<ul>
<li><code>models.py</code>: Definições do banco de dados e do modelo de usuário.</li>
</ul>
</li>
<li><strong>config/</strong>
<ul>
<li>Configurações e URL do banco de dados.</li>
</ul>
</li>
</ul>

<h2>Contribuição</h2>

<ol>
<li>Faça um fork do projeto.</li>
<li>Crie uma branch para sua feature (<code>git checkout -b feature/AmazingFeature</code>).</li>
<li>Commit suas mudanças (<code>git commit -m 'Add some AmazingFeature'</code>).</li>
<li>Push para a branch (<code>git push origin feature/AmazingFeature</code>).</li>
<li>Abra um Pull Request.</li>
</ol>

<h2>Contato</h2>

<p>Para suporte ou contribuições, entre em contato através do email: <code>&lt;seu_email&gt;</code></p>

</body>
</html>