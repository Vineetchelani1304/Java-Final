package Model;
import java.util.Calendar;

public class Purchases {
    private Customer c1;             // Customer object representing the customer who made the purchase
    private Product p1;              // Product object representing the purchased product
    private Calendar purchase_date;  // Calendar object representing the date of the purchase

    // Setter method to set the purchased details (customer, product, and purchase date)
    public void set_purchased(Customer c2, Product p2, Calendar temppurchase_data) {
        c1 = c2;                     // Assigning the provided customer object to the c1 variable
        p1 = p2;                     // Assigning the provided product object to the p1 variable
        purchase_date = temppurchase_data;  // Assigning the provided calendar object to the purchase_date variable
    }

    public void set_purchased(Customer c1,Product p1)
    {
        this.c1=c1;
        this.p1=p1;
    }

    // Method to display the purchase details
    public void Display_Purchase_Detail(int i) {
        System.out.println("Customer Name = " + c1.getFirstname() + " " + c1.getLastname() +" \nProduct Name = "+ p1.getProduct_name()+"\nProduct Brand "+p1.getProduct_brand()+"\nProduct Price $"+p1.getProduct_price()+"\nPurchase Date is " + purchase_date.getTime()+"\n\n");
        // Printing the customer's first name, last name, and the date of purchase using the Calendar object.
    }
    public void Display_Purchase_Detail() {
        System.out.println("Customer Name = " + c1.getFirstname() + " " + c1.getLastname() +" \nProduct Name = "+ p1.getProduct_name()+"\nProduct Brand "+p1.getProduct_brand()+"\nProduct Price $"+p1.getProduct_price()+"\n");
        // Printing the customer's first name, last name, and the date of purchase using the Calendar object.
    }
}