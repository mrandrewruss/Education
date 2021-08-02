public class main
{
    public static void main(String[] args) {
        int kolayAge = 27;
        int annaAge = 29;
        int igorAge = 34;

        int min = 0;    //Минимальный возраст.
        int midlle = 0; //Максимальный возраст.
        int max = 0;    //Средний возраст.

        //Минимальный возраст.

        if (kolayAge <= annaAge && kolayAge <= igorAge)
        {
            min = kolayAge;
            System.out.println("минимальный возраст = " + min);
        }
        else if (annaAge <= kolayAge && annaAge <= igorAge)
        {
            min = annaAge;
            System.out.println("минимальный возраст = " + min);
        }
        else {
            min = igorAge;
            System.out.println("минимальный возраст = " + min);
        }

        //Максимальный возраст.

        if (kolayAge >= annaAge && kolayAge >= igorAge)
        {
            max = kolayAge;
            System.out.println("максимальный возраст = " + max);
        }
        else if (annaAge >= kolayAge && annaAge >= igorAge)
        {
            max = annaAge;
            System.out.println("максимальный возраст = " + max);
        }
        else {
            max = igorAge;
            System.out.println("максимальный возраст = " + max);
        }

        //Средний возраст.

        if (kolayAge >= annaAge && kolayAge <= igorAge || kolayAge <= annaAge && kolayAge >= igorAge)
        {
            midlle = kolayAge;
            System.out.println("Средний возраст = " + midlle);
        }
        else if (annaAge >= kolayAge && annaAge <= igorAge || annaAge <= kolayAge && annaAge >= igorAge)
        {
            midlle = annaAge;
            System.out.println("Средний возраст = " + midlle);
        }
        else {
            midlle = igorAge;
            System.out.println("Средний возраст = " + midlle);
        }
    }
}