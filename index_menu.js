//Menu Hamburguer
//Função criada no html pelo onclick: menuShow

function menuShow() {
    //se o menu tá sendo exibido (ele é igual a block)
    //itens_hamburguer é o id da nav
    if(itens_hamburguer.style.display == 'block') {
        //e eu cliquei, ele recebe none (ele esconde)
        itens_hamburguer.style.display = 'none'

    //se ele tiver escondido, mostro com o block ao clicar
    } else {
        itens_hamburguer.style.display = 'block'

    }
}