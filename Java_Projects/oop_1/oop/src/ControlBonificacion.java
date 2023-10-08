public class ControlBonificacion {
    private  double suma;
    public double registrarSalario(Funcionario funcionario){
        this.suma = funcionario.getBonification() + this.suma;
        System.out.println("Calculo actual: " + this.suma);
        return this.suma;
    }

    public double registrarSalario(Gerente gerente){
        this.suma = gerente.getBonification() + this.suma;
        System.out.println("Calculo actual: " + this.suma);
        return this.suma;
    }
    public double registrarSalario(Contador contador){
        this.suma = contador.getBonification() + this.suma;
        System.out.println("Calculo actual: " + this.suma);
        return this.suma;
    }

}
