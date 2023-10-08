import java.awt.desktop.SystemEventListener;

public class TestFuncionario {
    public static void main(String[] args) {
        Funcionario diego;
        diego = new Funcionario();
        diego.setName("kelvin");
        diego.setNroDoc("222");
        diego.setSalary(89.888);
        diego.setTipo(0);

        System.out.println(diego.getName());
        System.out.println(diego.getBonification());
    }
}
