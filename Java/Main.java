class Main {
    public static void main(String[] args) {
        System.out.println("hola mundo");

        UberX car = new UberX("AMK123", new Account("José Cuevas", "JO123"), "Tesla", "Model X");
        car.setPassenger(4);
        car.printDataCar();

        UberVan car2 = new UberVan("123ASD", new Account("Hola Carebola", "JO123"));
        car2.setPassenger(6);
        car2.printDataCar();

    }
}