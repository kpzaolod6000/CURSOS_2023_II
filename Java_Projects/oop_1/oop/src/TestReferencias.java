public class TestReferencias {

    public static void main(String[] args) {
        Funcionario funcionario = new Funcionario();
        funcionario.setName("DIEGO");

        Gerente gerente = new Gerente();
        gerente.setName("JIMENA");

        funcionario.setSalary(2000);
        gerente.setSalary(10000 );
    }
}
