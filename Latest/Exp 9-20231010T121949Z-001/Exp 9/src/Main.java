//import Model.Product;
//import Model.Customer;
//import Model.Purchases;
//
//import java.util.Calendar;
//import java.util.Random;
//
//public class Main {
//    public static void main(String[] args) {
//        // Create an array of customers
//        Customer[] customerArray = new Customer[5];
//        Random random = new Random();
//        String[] customers={"Vineet","Chelani","Vansh","Nenwani","Ayush","Verma","Vaishnavi","Sonamwane","Vivek","Venkatchalam"};
//        String[] products={"Ghee","100","ParleG","10","Sev-Murmura","5","Honey","150","Bisleri","20"};
//        String[] brands={"Pantanjali","Parle","Balaji","Dabar","Bisleri"};
//        for (int i = 0; i < 5; i++) {
//            customerArray[i] = new Customer();
//            customerArray[i].setCustomerId(-2);
//            customerArray[i].setFirstName(customers[2*i]   );
//            customerArray[i].setLastName(customers[(2*i)+1]);
//            customerArray[i].setEmail("customer" + i + "@example.com");
//            customerArray[i].setPhone(Math.abs(random.nextLong())); // Use Math.abs to ensure non-negative            customerArray[i].setCustomerAddress("Address" + i);
//            customerArray[i].setCity("City" + i);
//            customerArray[i].setState("State" + i);
//            customerArray[i].setPostalCode("Postal" + i);
//            customerArray[i].setCountry("Country" + i);
//        }
//
//        // Create an array of products
//        Product[] productArray = new Product[3];
//        for (int i = 0; i < 3; i++) {
//            productArray[i] = new Product();
//            productArray[i].setProduct_id(i + 1);
//            productArray[i].setProductName(products[2*i]);
//            productArray[i].setProductBrand(brands[i]);
//            productArray[i].setProductPrice(Integer.parseInt(products[(2*i)+1])); // Random price
//            productArray[i].setProductQuantity(random.nextInt(100)); // Random quantity
//            productArray[i].setProductRating(random.nextFloat() * 5); // Random rating between 0 and 5
//            productArray[i].setProductAvailability(random.nextBoolean()); // Random availability
//        }
//
//        // Create purchase records
//        Purchases[] purchasesArray = new Purchases[10];
//        Calendar purchaseDate = Calendar.getInstance();
//        purchaseDate.set(Calendar.MONTH, 11);
//        purchaseDate.set(Calendar.DATE, 5);
//        purchaseDate.set(Calendar.YEAR, 1996);
//
//        for (int i = 0; i < 10; i++) {
//            purchasesArray[i] = new Purchases();
//            purchasesArray[i].set_purchased(customerArray[random.nextInt(5)], productArray[random.nextInt(3)], purchaseDate);
//        }
//
//        // Display purchase details
//        for (int i = 0; i < 5; i++) {
//            purchasesArray[i].Display_Purchase_Detail();
//        }
//    }
//}
import Model.Customer;
import Model.Product;
import Model.Purchases;

public class Main {
    public static void main(String[] args) {
        Customer customer = new Customer();
        customer.setCustomerInfo();
        Product product=new Product();
        product.setProductInfo();
        Purchases purchases=new Purchases();
        purchases.set_purchased(customer,product);
        purchases.Display_Purchase_Detail();

    }
}

