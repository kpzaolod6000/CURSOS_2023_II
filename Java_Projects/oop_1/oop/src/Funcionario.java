// public abstract class Funcionario { // las clases abstractas no pueden ser intanciadas
//los metodos abstract tampoco tienen cuerpo y obliga a los hijos a sobreescribir dicho metodo
public class Funcionario {
    private String name;
    private String nroDoc;
    private double salary;
    private int tipo;
    public Funcionario() {
    }
//    public Funcionario(string name, string nroDoc, string salary) {
//        this.name = name; 
//        this.nroDoc = nroDoc;
//        this.salary = salary;
//    }

    public void setName(String name) {
        this.name = name;
    }

    public void setNroDoc(String nroDoc) {
        this.nroDoc = nroDoc;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public String getName() {
        return name;
    }
    public String getNroDoc() {
        return nroDoc;
    }

    public double getSalary() {
        return salary;
    }

    public double getBonification(){
        return this.salary * 0.05;
    }

    public int getTipo() {
        return tipo;
    }

    public void setTipo(int tipo) {
        this.tipo = tipo;
    }
}
