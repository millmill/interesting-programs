public class Main {

    public static void main(String[] args) {
        Dog2 d = new Dog2();
        Cat2 c = new Cat2();

        if (c instanceof Pet){
            c.play();
        }

        if (d instanceof Pet){
            d.play();
        }

        Pet p;
        Random rand = new Random();
        int n = rand.nextInt(2);

        if (n == 0) {
            p = new Dog2();
        } else {
            p = new Cat2();
        }

        p.play();
    }
}




public interface Pet {
    void play();
}



public class Dog2 implements Pet {
    public void play() {
        System.out.println("The dog plays with its owner.");
        }
}



public class Cat2 implements Pet {
    public void play() {
        System.out.println("The cat plays with its owner.");
    }
}
