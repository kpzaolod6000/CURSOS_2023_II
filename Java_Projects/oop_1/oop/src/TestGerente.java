public class TestGerente {
    public static void main(String[] args) {
        // Funcionario gerente  = new Funcionario();
        Gerente gerente  = new Gerente();
        gerente.setSalary(6000);
        gerente.setClave("aluracusrsoonline");
        gerente.setTipo(1);

        System.out.println(gerente.getBonification());
        System.out.println(gerente.iniciarSesion("aluracusrsoonline"));

    }
}
