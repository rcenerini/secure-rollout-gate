# S1.6 - Atualiza o bloco automatico de docs/HANDOFF.md com o estado do Git.
# Uso (na raiz do repositorio):  powershell -File scripts/handoff.ps1
# Nao roda testes (a stack so e definida na S2.1) e nao altera nada fora do bloco.
$ErrorActionPreference = 'Stop'

$raiz = (git rev-parse --show-toplevel).Trim()
$arquivo = Join-Path $raiz 'docs/HANDOFF.md'
if (-not (Test-Path $arquivo)) { throw "Nao encontrei $arquivo" }

$inicio = '<!-- HANDOFF-AUTO:INICIO -->'
$fim    = '<!-- HANDOFF-AUTO:FIM -->'

$agora   = Get-Date -Format 'dd/MM/yyyy HH:mm'
$branch  = (git rev-parse --abbrev-ref HEAD).Trim()
$status  = (git status --short) -join "`n"
if ([string]::IsNullOrWhiteSpace($status)) { $status = '(arvore de trabalho limpa)' }
$commits = (git log --oneline -5) -join "`n"

$bloco = @"
$inicio
## Estado automatico (gerado por scripts/handoff.ps1)
- Gerado em: $agora
- Branch: $branch

Alteracoes nao commitadas:
``````
$status
``````

Ultimos commits:
``````
$commits
``````
$fim
"@

$conteudo = [System.IO.File]::ReadAllText($arquivo)
$i = $conteudo.IndexOf($inicio)
$f = $conteudo.IndexOf($fim)

if ($i -ge 0 -and $f -gt $i) {
    $novo = $conteudo.Substring(0, $i) + $bloco + $conteudo.Substring($f + $fim.Length)
} else {
    $novo = $conteudo.TrimEnd() + "`n`n" + $bloco + "`n"
}

$utf8 = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($arquivo, $novo, $utf8)
Write-Host "HANDOFF atualizado: $arquivo"
Write-Host 'Preencha a mao: historia em andamento, proximo passo exato, o que foi e o que nao foi feito, modelo e tier usados.'
