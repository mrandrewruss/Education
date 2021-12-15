import java.util.Arrays;

public class Loader {
    public static void main(String[] args) {

        //Количество ингридиентов
        int powderAmount = 400; // g
        int milkAmount = 100; // ml
        int sugarAmount = 50; // g
        int eggsCount = 10; // items
        int oilAmount = 30; // ml
        int appleCount = 1;

        boolean canBake = false;

        /**
         * Pancakes: powder - 400 g, sugar - 10 g, milk - 1 l, oil - 30 ml
         * powderAmount >= 400 && milkAmount >= 1000 && sugarAmount >= 10 && oilAmount >= 30)
         *
         * Omelette: milk - 300 ml, powder - 5 g, eggs - 5
         * powderAmount >= 5 && milkAmount >= 300 && eggsCount >= 5
         *
         * Apple pie: apples - 3, milk - 100 ml, powder - 300 g, eggs - 4
         * powderAmount >= 300 && milkAmount >= 100 && eggsCount >= 4 && appleCount >= 3
         */

        if (powderAmount >= 400 && milkAmount >= 1000 && sugarAmount >= 10 && oilAmount >= 30)
        {
            System.out.println("Вы можете испечь - Pancakes");
            canBake = true;
        }

        if (powderAmount >= 5 && milkAmount >= 300 && eggsCount >= 5)
        {
            System.out.println("Вы можете испечь - Omelette");
            canBake = true;
        }

        if (powderAmount >= 300 && milkAmount >= 100 && eggsCount >= 4 && appleCount >= 3)
        {
            System.out.println("Вы можете испечь - Apple pie");
            canBake = true;
        }

        if (canBake == false)
        {
            System.out.println("Недостаточно ингридиентов что бы что-нибудь приготовить");
        }
    }
}