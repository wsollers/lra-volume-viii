Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $Root
try {
    $previous = $env:LRA_PRINT_EDITION
    $env:LRA_PRINT_EDITION = "1"
    latexmk -g -lualatex -interaction=nonstopmode -halt-on-error -jobname=main-print main.tex @args
}
finally {
    if ($null -eq $previous) {
        Remove-Item Env:\LRA_PRINT_EDITION -ErrorAction SilentlyContinue
    }
    else {
        $env:LRA_PRINT_EDITION = $previous
    }
    Pop-Location
}
