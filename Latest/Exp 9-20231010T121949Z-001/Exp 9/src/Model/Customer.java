package Model;

import java.util.Scanner;

public class Customer {
    private int customer_id;
    private String first_name;
    private String last_name;
    private String email;
    private long phone;
    private String customer_address;
    private String city;
    private String state;
    private String postalCode;
    private String country;

    // Setter and Getter methods for customer_id
    public void setCustomerId(int customer_id) {
        if (customer_id < 0) {
            throw new IllegalArgumentException("Customer ID cannot be negative.");
        }
        this.customer_id = customer_id;
    }

    public int getCustomerId() {
        return customer_id;
    }

    // Setter and Getter methods for first_name
    public void setFirstName(String first_name) {
        if (first_name == null || first_name.isEmpty()) {
            throw new IllegalArgumentException("First name cannot be null or empty.");
        }
        this.first_name = first_name;
    }

    public String getFirstName() {
        return first_name;
    }

    // Setter and Getter methods for last_name
    public void setLastName(String last_name) {
        if (last_name == null || last_name.isEmpty()) {
            throw new IllegalArgumentException("Last name cannot be null or empty.");
        }
        this.last_name = last_name;
    }

    public String getLastName() {
        return last_name;
    }

    // Setter and Getter methods for email
    public void setEmail(String email) {
        if (email == null || !email.contains("@")) {
            throw new IllegalArgumentException("Invalid email address.");
        }
        this.email = email;
    }

    public String getEmail() {
        return email;
    }

    // Setter and Getter methods for phone
    public void setPhone(long phone) {
        if (phone < 0) {
            throw new IllegalArgumentException("Phone number cannot be negative.");
        }
        this.phone = phone;
    }

    public long getPhone() {
        return phone;
    }

    // Setter and Getter methods for customer_address
    public void setCustomerAddress(String customer_address) {
        if (customer_address == null || customer_address.isEmpty()) {
            throw new IllegalArgumentException("Customer address cannot be null or empty.");
        }
        this.customer_address = customer_address;
    }

    public String getCustomerAddress() {
        return customer_address;
    }

    // Setter and Getter methods for city
    public void setCity(String city) {
        if (city == null || city.isEmpty()) {
            throw new IllegalArgumentException("City cannot be null or empty.");
        }
        this.city = city;
    }

    public String getCity() {
        return city;
    }

    // Setter and Getter methods for state
    public void setState(String state) {
        if (state == null || state.isEmpty()) {
            throw new IllegalArgumentException("State cannot be null or empty.");
        }
        this.state = state;
    }

    public String getState() {
        return state;
    }

    // Setter and Getter methods for postalCode
    public void setPostalCode(String postalCode) {
        if (postalCode == null || postalCode.isEmpty()) {
            throw new IllegalArgumentException("Postal code cannot be null or empty.");
        }
        this.postalCode = postalCode;
    }

    public String getPostalCode() {
        return postalCode;
    }

    // Setter and Getter methods for country
    public void setCountry(String country) {
        if (country == null || country.isEmpty()) {
            throw new IllegalArgumentException("Country cannot be null or empty.");
        }
        this.country = country;
    }

    public String getCountry() {
        return country;
    }

    public String getFirstname() {
        return first_name;
    }

    public String getLastname() {
        return last_name;
    }

    public void setCustomerInfo() {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter Customer ID: ");
            setCustomerId(scanner.nextInt());

            scanner.nextLine();  // Consume the newline
            System.out.print("Enter First Name: ");
            setFirstName(scanner.nextLine());

            System.out.print("Enter Last Name: ");
            setLastName(scanner.nextLine());

            System.out.print("Enter Email: ");
            setEmail(scanner.nextLine());

            System.out.print("Enter Phone: ");
            setPhone(scanner.nextLong());

            scanner.nextLine();  // Consume the newline
            System.out.print("Enter Customer Address: ");
            setCustomerAddress(scanner.nextLine());

            System.out.print("Enter City: ");
            setCity(scanner.nextLine());

            System.out.print("Enter State: ");
            setState(scanner.nextLine());

            System.out.print("Enter Postal Code: ");
            setPostalCode(scanner.nextLine());

            System.out.print("Enter Country: ");
            setCountry(scanner.nextLine());
        } catch (Exception e) {
            System.out.println("Invalid input. Please try again.");
            setCustomerInfo(); // Retry input
        } finally {
            scanner.close();
        }
    }
}
