# 🥐 Sites de Padarias Artesanais — Santini Digital

Projeto de alta performance com **57 Landing Pages** dedicadas para padarias artesanais, preparadas para deploy na **Vercel** com roteamento automático de subdomínios sob o domínio principal `santinidigital.com.br`.

---

## 🌐 Como Funciona o Roteamento de Subdomínios na Vercel

O arquivo `vercel.json` captura o Host HTTP e mapeia qualquer subdomínio automaticamente para a pasta correspondente:
- `olivetanos.santinidigital.com.br` ➡️ `/olivetanos/`
- `melissa.santinidigital.com.br` ➡️ `/melissa/`
- `giselle.santinidigital.com.br` ➡️ `/giselle/`
- `santinidigital.com.br` ou subdomínio de teste ➡️ Vitrine Central (`/index.html`)

---

## ⚙️ Configuração de DNS (Registro.br / Cloudflare / GoDaddy)

Para ativar todos os subdomínios de uma só vez:

1. Acesse o painel de DNS do domínio **`santinidigital.com.br`**.
2. Adicione um apontamento **CNAME Wildcard**:
   - **Tipo**: `CNAME`
   - **Nome / Host**: `*` (ou `*.santinidigital.com.br`)
   - **Destino / Valor**: `cname.vercel-dns.com`
   - **TTL**: Automático ou 1 hora (Proxy DNS desativado / DNS Only se estiver na Cloudflare).
3. No painel do seu projeto na **Vercel**:
   - Vá em **Settings > Domains**
   - Adicione o domínio curinga: `*.santinidigital.com.br`
   - A Vercel emitirá automaticamente certificados SSL Let's Encrypt para todos os subdomínios!

---

## 📋 Lista de Subdomínios Disponíveis (57 Padarias)

| Padaria | Subdomínio | Pasta no Projeto |
| :--- | :--- | :--- |
| **Padaria Melissa** | `melissa.santinidigital.com.br` | `/melissa/` |
| **Internacional Paes e Doces** | `internacional.santinidigital.com.br` | `/internacional/` |
| **Padaria Giselle** | `giselle.santinidigital.com.br` | `/giselle/` |
| **Panificadora Santa Mônica** | `santamonica.santinidigital.com.br` | `/santamonica/` |
| **Padaria Mix** | `mix.santinidigital.com.br` | `/mix/` |
| **Pães e Doces Beth Mania - São Francisco** | `bethmania.santinidigital.com.br` | `/bethmania/` |
| **Padaria Imperial Pães e Doces** | `imperial.santinidigital.com.br` | `/imperial/` |
| **Panificadora e Confeitaria Jardim Samara** | `jardimsamara.santinidigital.com.br` | `/jardimsamara/` |
| **O Fidalgo** | `ofidalgo.santinidigital.com.br` | `/ofidalgo/` |
| **Padaria Nova Granada** | `padaria-nova-granada.santinidigital.com.br` | `/padaria-nova-granada/` |
| **Padaria Flor do Bairro** | `flordobairro.santinidigital.com.br` | `/flordobairro/` |
| **Arte e Pão da Vila Ré** | `arteepao.santinidigital.com.br` | `/arteepao/` |
| **Padaria e Pizzaria Okinawa** | `okinawa.santinidigital.com.br` | `/okinawa/` |
| **Panificadora Flor De Lirio** | `flordelirio.santinidigital.com.br` | `/flordelirio/` |
| **Padaria Ápice** | `apice.santinidigital.com.br` | `/apice/` |
| **Panificadora Jandaia do Sul** | `jandaia.santinidigital.com.br` | `/jandaia/` |
| **Requinte Centro Gastronômico** | `requinte-centro-gastronomico.santinidigital.com.br` | `/requinte-centro-gastronomico/` |
| **Panificadora Eliana** | `eliana.santinidigital.com.br` | `/eliana/` |
| **Padaria Vitória** | `vitoria.santinidigital.com.br` | `/vitoria/` |
| **Panificadora e Confeitaria Espacial** | `espacial.santinidigital.com.br` | `/espacial/` |
| **Bella Massa** | `bellamassa.santinidigital.com.br` | `/bellamassa/` |
| **Padaria E Confeitaria D'fofinhos** | `dfofinhos.santinidigital.com.br` | `/dfofinhos/` |
| **Panificadora Nova Esperança** | `novaesperanca.santinidigital.com.br` | `/novaesperanca/` |
| **Padaria Brilhante** | `brilhante.santinidigital.com.br` | `/brilhante/` |
| **Padaria Delícia** | `delicia.santinidigital.com.br` | `/delicia/` |
| **Padaria Saint Louis** | `saintlouis.santinidigital.com.br` | `/saintlouis/` |
| **Padaria Porta Del Rei** | `portadelrei.santinidigital.com.br` | `/portadelrei/` |
| **Padaria Mel na Boca** | `melnaboca.santinidigital.com.br` | `/melnaboca/` |
| **Panificadora Estrela Guia** | `estrelaguia.santinidigital.com.br` | `/estrelaguia/` |
| **Padaria e Doces - Jd. Marina** | `jdmarina.santinidigital.com.br` | `/jdmarina/` |
| **Padaria Rosa Do Porto** | `rosadoporto.santinidigital.com.br` | `/rosadoporto/` |
| **Casa São Francisco Padaria** | `casasaofrancisco.santinidigital.com.br` | `/casasaofrancisco/` |
| **Padaria Canto do Buriti** | `cantodoburiti.santinidigital.com.br` | `/cantodoburiti/` |
| **Padaria Rainha da Patriarca | Pães e Doces** | `padaria-rainha-da-patriarca-paes-e-doces.santinidigital.com.br` | `/padaria-rainha-da-patriarca-paes-e-doces/` |
| **Padaria** | `padariazl.santinidigital.com.br` | `/padariazl/` |
| **Padaria Principe Davi** | `principedavi.santinidigital.com.br` | `/principedavi/` |
| **Panificadora Nova Imperador do Trigo** | `novaimperador.santinidigital.com.br` | `/novaimperador/` |
| **Padaria rainha do Maringá** | `rainhadomaringa.santinidigital.com.br` | `/rainhadomaringa/` |
| **Panificadora São Pedro** | `saopedro.santinidigital.com.br` | `/saopedro/` |
| **Ponto do Pão** | `pontodopao.santinidigital.com.br` | `/pontodopao/` |
| **Panificadora ArtPão** | `artpao.santinidigital.com.br` | `/artpao/` |
| **Confeitaria Borges Vila Industrial** | `confeitariaborges.santinidigital.com.br` | `/confeitariaborges/` |
| **Bella Massa** | `bellamassa-2.santinidigital.com.br` | `/bellamassa-2/` |
| **Padaria Nova Astral** | `novaastral.santinidigital.com.br` | `/novaastral/` |
| **Padaria Alzira** | `alzira.santinidigital.com.br` | `/alzira/` |
| **Padaria Santa Maria** | `santamaria.santinidigital.com.br` | `/santamaria/` |
| **Padaria Nova Manchester** | `novamanchester.santinidigital.com.br` | `/novamanchester/` |
| **Padaria Tradição** | `tradicao.santinidigital.com.br` | `/tradicao/` |
| **Padaria Pão D' Ouro** | `paodouro.santinidigital.com.br` | `/paodouro/` |
| **Padaria Sabor do Trigo** | `padaria-sabor-do-trigo.santinidigital.com.br` | `/padaria-sabor-do-trigo/` |
| **Panificadora Viena Fama** | `vienafama.santinidigital.com.br` | `/vienafama/` |
| **Padaria Pizzaria & Restaurante Catarina** | `catarina.santinidigital.com.br` | `/catarina/` |
| **Nova Rio D'Ouro** | `novariodouro.santinidigital.com.br` | `/novariodouro/` |
| **Padaria das Flores** | `padariadasflores.santinidigital.com.br` | `/padariadasflores/` |
| **Ponto dos pães** | `pontodospaes.santinidigital.com.br` | `/pontodospaes/` |
| **Padaria Fantasia** | `fantasia.santinidigital.com.br` | `/fantasia/` |
| **Panificadora Olivetanos | Casa de Pães e Doces** | `panificadora-olivetanos-casa-de-paes-e-doces.santinidigital.com.br` | `/panificadora-olivetanos-casa-de-paes-e-doces/` |
