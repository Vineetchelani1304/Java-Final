package Model;

import java.util.Scanner;

public class Product {
    private int product_id;
    private String product_name;
    private String product_brand;
    private float product_price;
    private int product_quantity;
    private float product_rating;
    private boolean product_availability;

    // Setter and Getter methods for product_id
    public void setProduct_id(int product_id) {
        if (product_id < 0) {
            throw new IllegalArgumentException("Product ID cannot be negative.");
        }
        this.product_id = product_id;
    }

    public int getProduct_id() {
        return product_id;
    }

    // Setter and Getter methods for product_name
    public void setProduct_name(String product_name) {
        if (product_name == null || product_name.isEmpty()) {
            throw new IllegalArgumentException("Product name cannot be null or empty.");
        }
        this.product_name = product_name;
    }

    public String getProduct_name() {
        return product_name;
    }

    // Setter and Getter methods for product_brand
    public void setProduct_brand(String product_brand) {
        if (product_brand == null || product_brand.isEmpty()) {
            throw new IllegalArgumentException("Product brand cannot be null or empty.");
        }
        this.product_brand = product_brand;
    }

    public String getProduct_brand() {
        return product_brand;
    }

    // Setter and Getter methods for product_price
    public void setProduct_price(float product_price) {
        if (product_price < 0) {
            throw new IllegalArgumentException("Product price cannot be negative.");
        }
        this.product_price = product_price;
    }

    public float getProduct_price() {
        return product_price;
    }

    // Setter and Getter methods for product_quantity
    public void setProduct_quantity(int product_quantity) {
        if (product_quantity < 0) {
            throw new IllegalArgumentException("Product quantity cannot be negative.");
        }
        this.product_quantity = product_quantity;
    }

    public int getProduct_quantity() {
        return product_quantity;
    }

    // Setter and Getter methods for product_rating
    public void setProduct_rating(float product_rating) {
        if (product_rating < 0 || product_rating > 5) {
            throw new IllegalArgumentException("Product rating should be between 0 and 5.");
        }
        this.product_rating = product_rating;
    }

    public float getProduct_rating() {
        return product_rating;
    }

    // Setter and Getter methods for product_availability
    public void setProduct_availability(boolean product_availability) {
        this.product_availability = product_availability;
    }

    public boolean isProduct_availability() {
        return product_availability;
    }

    public void setProductInfo() {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter Product ID: ");
            setProduct_id(scanner.nextInt());

            scanner.nextLine();  // Consume the newline
            System.out.print("Enter Product Name: ");
            setProduct_name(scanner.nextLine());

            System.out.print("Enter Product Brand: ");
            setProduct_brand(scanner.nextLine());

            System.out.print("Enter Product Price: ");
            setProduct_price(scanner.nextFloat());

            System.out.print("Enter Product Quantity: ");
            setProduct_quantity(scanner.nextInt());

            System.out.print("Enter Product Rating: ");
            setProduct_rating(scanner.nextFloat());

            scanner.nextLine();  // Consume the newline
            System.out.print("Enter Product Availability (true/false): ");
            setProduct_availability(scanner.nextBoolean());

            scanner.nextLine();  // Consume any remaining newline

        } catch (Exception e) {
            System.out.println("Invalid input. Please try again.");
            // Clear the input buffer
            scanner.nextLine();
            setProductInfo(); // Retry input
        } finally {
            scanner.close();  // Close the scanner after all input is done
        }
    }

}
