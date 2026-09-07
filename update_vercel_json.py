import json

base_dir = r'e:\SANTINI DIGITAL\MARKETING\pages\SITES PADARIAS'
data_file = r'e:\SANTINI DIGITAL\MARKETING\reports\dashboard_padarias\padarias_data.js'

with open(data_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
raw_js = ''.join(lines[1:]).replace('const PADARIAS_DATA = ', '').strip().rstrip(';')
padarias = json.loads(raw_js)

CUSTOM_SLUGS = {
    'Panificadora Olivetanos | Casa de Pães e Doces': 'olivetanos',
    'Padaria Melissa': 'melissa',
    'Internacional Paes e Doces': 'internacional',
    'Padaria Giselle': 'giselle',
    'Panificadora Santa Mônica': 'santamonica',
    'Padaria Mix': 'mix',
    'Pães e Doces Beth Mania - São Francisco': 'bethmania',
    'Padaria Imperial Pães e Doces': 'imperial',
    'Panificadora e Confeitaria Jardim Samara': 'jardimsamara',
    'O Fidalgo': 'ofidalgo',
    'Padaria Flor do Bairro': 'flordobairro',
    'Arte e Pão da Vila Ré': 'arteepao',
    'Padaria e Pizzaria Okinawa': 'okinawa',
    'Panificadora Flor De Lirio': 'flordelirio',
    'Padaria Ápice': 'apice',
    'Panificadora Jandaia do Sul': 'jandaia',
    'Panificadora Eliana': 'eliana',
    'Padaria Vitória': 'vitoria',
    'Panificadora e Confeitaria Espacial': 'espacial',
    'Bella Massa': 'bellamassa',
    "Padaria E Confeitaria D'fofinhos": 'dfofinhos',
    'Panificadora Nova Esperança': 'novaesperanca',
    'Padaria Brilhante': 'brilhante',
    'Padaria Delícia': 'delicia',
    'Padaria Saint Louis': 'saintlouis',
    'Padaria Porta Del Rei': 'portadelrei',
    'Padaria Mel na Boca': 'melnaboca',
    'Panificadora Estrela Guia': 'estrelaguia',
    'Padaria e Doces - Jd. Marina': 'jdmarina',
    'Padaria Rosa Do Porto': 'rosadoporto',
    'Casa São Francisco Padaria': 'casasaofrancisco',
    'Padaria Canto do Buriti': 'cantodoburiti',
    'Padaria Rainha da Patriarca | Pães e Doces': 'rainhadapatriarca',
    'Padaria': 'padariazl',
    'Padaria Principe Davi': 'principedavi',
    'Panificadora Nova Imperador do Trigo': 'novaimperador',
    'Padaria rainha do Maringá': 'rainhadomaringa',
    'Panificadora São Pedro': 'saopedro',
    'Ponto do Pão': 'pontodopao',
    'Panificadora ArtPão': 'artpao',
    'Confeitaria Borges Vila Industrial': 'confeitariaborges',
    'Padaria Nova Astral': 'novaastral',
    'Padaria Alzira': 'alzira',
    'Padaria Santa Maria': 'santamaria',
    'Padaria Nova Manchester': 'novamanchester',
    'Padaria Tradição': 'tradicao',
    "Padaria Pão D' Ouro": 'paodouro',
    'Panificadora Viena Fama': 'vienafama',
    'Padaria Pizzaria & Restaurante Catarina': 'catarina',
    "Nova Rio D'Ouro": 'novariodouro',
    'Padaria das Flores': 'padariadasflores',
    'Ponto dos pães': 'pontodospaes',
    'Padaria Fantasia': 'fantasia'
}

rewrites = []

# Padarias & WWW host rules -> stay on /
rewrites.append({
    'source': '/:path*',
    'has': [{'type': 'host', 'value': 'padarias.santinidigital.com.br'}],
    'destination': '/:path*'
})
rewrites.append({
    'source': '/:path*',
    'has': [{'type': 'host', 'value': 'www.santinidigital.com.br'}],
    'destination': '/:path*'
})

# Add explicit rules for each bakery
for name, slug in CUSTOM_SLUGS.items():
    host_val = f'{slug}.santinidigital.com.br'
    rewrites.append({
        'source': '/',
        'has': [{'type': 'host', 'value': host_val}],
        'destination': f'/{slug}/index.html'
    })
    rewrites.append({
        'source': '/:path*',
        'has': [{'type': 'host', 'value': host_val}],
        'destination': f'/{slug}/:path*'
    })

vercel_config = {
    'version': 2,
    'cleanUrls': True,
    'trailingSlash': False,
    'rewrites': rewrites
}

with open(r'e:\SANTINI DIGITAL\MARKETING\pages\SITES PADARIAS\vercel.json', 'w', encoding='utf-8') as f:
    json.dump(vercel_config, f, indent=2)

print(f'vercel.json updated with {len(rewrites)} explicit rules!')
