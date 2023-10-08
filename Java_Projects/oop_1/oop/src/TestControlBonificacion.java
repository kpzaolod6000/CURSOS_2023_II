public class TestControlBonificacion {

    public static void main(String[] args){
        Funcionario funcionario = new Funcionario();

        Gerente gerente = new Gerente();
        Contador alexiz = new Contador();

        funcionario.setSalary(2000);
        gerente.setSalary(10000 );
        alexiz.setSalary(5000);

        ControlBonificacion controlBonificacion = new ControlBonificacion();
        controlBonificacion.registrarSalario(funcionario);
        controlBonificacion.registrarSalario(gerente);
        controlBonificacion.registrarSalario(alexiz);
    }
}
