package br.com.fecaf.model;

public class Imc {

        //Atributos
        public int peso;
        public double altura;
        public double imc;
        //Metodo
        public void calcularImc(){
            imc = peso / (altura * altura);
            System.out.println("O imc é: " + imc);
        }
        public void statusImc(){
            if (imc < 18.5){
                System.out.println("O status é baixo peso ...");
            } else if (imc >= 18.5 && imc < 24.99) {
                System.out.println("O status é normal ...");
            } else if (imc >= 25 && imc <= 29.99) {
                System.out.println("O status é sobrepeso ...");
            }else {
                System.out.println("O status é obeso ...");
            }
        }
}
