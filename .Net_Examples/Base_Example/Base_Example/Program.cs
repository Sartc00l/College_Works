using Animals;
namespace Programm
{
    static class Programm
    {
        static void Main(string[] args)
        {
            Dogs dog = new Dogs("Мухтар", 4);
            Bird bird =new Bird("Чижик");
            Cats cat = new Cats("Ya'qub Qamar Ad-Din Dibiazah");
            dog.KnockOwner();
            dog.Hunt();
            dog.MakeSound();
            Console.WriteLine();
            bird.Fly();
            bird.MakeSound();
            bird.Hunt();
            Console.WriteLine();
            cat.BreakAvase();
            cat.Hunt();
            cat.MakeSound();
        }
    }
}
namespace Animals
{
    class Animals
    {
        public string name;
        public Animals(string _name) 
        {
            name = _name;
        }
        void Eat()
        {
            Console.WriteLine($"{name}\tкушает");
        }
        void Walk()
        {
            Console.WriteLine($"{name}\tходит");
        }
        void Drink()
        {
            Console.WriteLine($"{name}\tпьет");
        }
        public virtual void MakeSound()
        {
            Console.WriteLine($"{name} издает какой-то звук");
        }
        public virtual void Hunt()
        {
            Console.Write($"{name} охотиться    ");
        }
    }
    class Cats : Animals
    {
        public Cats(string name) : base(name) {}
        public void BreakAvase()
        {
            Console.WriteLine($"{name}  разбила вазу!!!!!");
        }
        public void Crouch()
        {
            Console.WriteLine($"{name} тихонько крадется");
        }
        public override void Hunt()
        {
            base.Hunt();
            Console.Write("на мышку\n");
        }
        public override void MakeSound()
        {
            Console.WriteLine($"{name} мяукает");

        }
    }

    class Dogs : Animals
    {

        private int dogSize;
        public Dogs(string name,int _dogSize) : base(name) 
        {
            dogSize = _dogSize;
        }

        public void KnockOwner()
        {
            if (dogSize > 2) {
                Console.WriteLine($"{name} опрокинула хозяина!!!");
            }
            else
            {
                Console.WriteLine($"{name} не опрокинула хозяина!! (она маленькая)");
            }
        }

        public override void Hunt()
        {
            base.Hunt(); 
            Console.Write($" на гуся\n");
        }

        public override void MakeSound() {
            Console.WriteLine($"{name} лает");
        }
    }

    class Bird : Animals
    {
        public Bird(string name) : base(name) { }
        public void Fly()
        {
            Console.WriteLine($"{name} летает!!!");
        }
        public override void Hunt() 
        {
            base.Hunt();
            Console.Write("на жучка\n");
        }
        public override void MakeSound()
        {
            Console.WriteLine($"{name} чирикает");
        }
    }
}