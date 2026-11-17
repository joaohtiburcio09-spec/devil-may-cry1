document.addEventListener("DOMContentLoaded", () => {
    // --- CAÇADORES ---
    const formCacador = document.getElementById("form-cacador");
    const listaCacadores = document.getElementById("lista-cacadores");

    async function carregarCacadores() {
        const res = await fetch("/api/cacadores");
        const dados = await res.json();
        listaCacadores.innerHTML = "";
        dados.forEach(c => {
            const li = document.createElement("li");
            li.innerHTML = `<strong>${c.nome}</strong> - ${c.especialidade} [Rank: ${c.rank_estilo}] 
                            <button onclick="deletarItem('/api/cacadores/${c.id}', carregarCacadores)">Excluir</button>`;
            listaCacadores.appendChild(li);
        });
    }

    if (formCacador) {
        formCacador.addEventListener("submit", async (e) => {
            e.preventDefault();
            await fetch("/api/cacadores", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    nome: document.getElementById("nome").value,
                    especialidade: document.getElementById("especialidade").value,
                    rank_estilo: document.getElementById("rank").value
                })
            });
            formCacador.reset();
            carregarCacadores();
        });
        carregarCacadores();
    }

    // --- DEMÔNIOS ---
    const formDemonio = document.getElementById("form-demonio");
    const listaDemonios = document.getElementById("lista-demonios");

    async function carregarDemonios() {
        const res = await fetch("/api/demonios");
        const dados = await res.json();
        listaDemonios.innerHTML = "";
        dados.forEach(d => {
            const li = document.createElement("li");
            li.innerHTML = `<strong>${d.nome}</strong> (${d.classe}) - Ameaça Nível ${d.nivel_ameaca} 
                            <button onclick="deletarItem('/api/demonios/${d.id}', carregarDemonios)">Excluir</button>`;
            listaDemonios.appendChild(li);
        });
    }

    if (formDemonio) {
        formDemonio.addEventListener("submit", async (e) => {
            e.preventDefault();
            await fetch("/api/demonios", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    nome: document.getElementById("nome-demonio").value,
                    classe: document.getElementById("classe-demonio").value,
                    nivel_ameaca: document.getElementById("ameaca-demonio").value
                })
            });
            formDemonio.reset();
            carregarDemonios();
        });
        carregarDemonios();
    }

    // --- MISSÕES ---
    const formMissao = document.getElementById("form-missao");
    const listaMissoes = document.getElementById("lista-missoes");

    async function carregarMissoes() {
        const res = await fetch("/api/missoes");
        const dados = await res.json();
        listaMissoes.innerHTML = "";
        dados.forEach(m => {
            const li = document.createElement("li");
            li.innerHTML = `<strong>${m.titulo}</strong> - ${m.recompensa} Orbs [${m.status}] 
                            <button onclick="concluirMissao(${m.id})">Concluir</button>
                            <button onclick="deletarItem('/api/missoes/${m.id}', carregarMissoes)">Excluir</button>`;
            listaMissoes.appendChild(li);
        });
    }

    if (formMissao) {
        formMissao.addEventListener("submit", async (e) => {
            e.preventDefault();
            await fetch("/api/missoes", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    titulo: document.getElementById("titulo-missao").value,
                    recompensa: document.getElementById("recompensa-missao").value
                })
            });
            formMissao.reset();
            carregarMissoes();
        });
        carregarMissoes();
    }

    // --- FUNÇÕES AUXILIARES GLOBAIS ---
    window.deletarItem = async (url, callback) => {
        await fetch(url, { method: "DELETE" });
        callback();
    };

    window.concluirMissao = async (id) => {
        await fetch(`/api/missoes/${id}/concluir`, { method: "PUT" });
        carregarMissoes();
    };
});