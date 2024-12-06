<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>CSF Garments</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <header>
        <div class="navbar">
            <div class="logo">
                <h1>CSF Garments</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#products">Products</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section id="home" class="hero">
        <div class="hero-text">
            <h2>Your Trusted Garment Supplier</h2>
            <p>Quality, comfort, and style in every stitch</p>
            <a href="#products" class="cta-btn">Explore Products</a>
        </div>
    </section>

    <section id="about" class="about">
        <h2>About Us</h2>
        <p>CSF Garments is a leading manufacturer of high-quality garments. We specialize in a wide range of clothing products, ensuring top-notch quality and comfort for all customers.</p>
    </section>

    <section id="products" class="products">
        <h2>Our Products</h2>
        <div class="product-card">
            <img src="product1.jpg" alt="Product 1">
            <p>Premium T-Shirts</p>
        </div>
        <div class="product-card">
            <img src="product2.jpg" alt="Product 2">
            <p>Casual Wear</p>
        </div>
        <div class="product-card">
            <img src="product3.jpg" alt="Product 3">
            <p>Formal Shirts</p>
        </div>
    </section>

    <section id="contact" class="contact">
        <h2>Contact Us</h2>
        <p>Have any questions? Reach out to us:</p>
        <form action="submit_form.php" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            <button type="submit" class="submit-btn">Send Message</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2024 CSF Garments. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>

</html>
