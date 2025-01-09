package br.com.fecaf;

import br.com.fecaf.model.Imc;

public class AppImc {
    public static void main(String[] args) {

        //Instanciar Objeto Imc
        Imc objImc = new Imc();

        objImc.peso = 84;
        objImc.altura = 1.90;

        objImc.calcularImc();
        objImc.statusImc();


    }
}
