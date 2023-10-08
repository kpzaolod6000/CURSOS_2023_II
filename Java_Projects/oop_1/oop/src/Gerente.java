public class Gerente extends Funcionario{

    private String clave;
    public void setClave(String clave){
        this.clave = clave;
    }

    public boolean iniciarSesion(String clave){
        return this.clave == clave;
    }

    //  sobreescritura de metodo
    public double getBonification(){
        return super.getSalary() + super.getBonification();
    }
}
