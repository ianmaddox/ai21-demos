import streamlit as st
from constants import DEFAULT_MODEL
from utils.completion import complete
from utils.studio_style import apply_studio_style

st.set_page_config(
    page_title="Moving Along website generator - Type A",
)


base_prompt = '''
Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Green Thumb Landscaping\nLocation: Portland, OR\nServices: Landscape Design, Lawn Maintenance, Tree Pruning, Irrigation Systems\nBenefits: Eco-friendly practices, Certified Arborists, 100% Customer Satisfaction Guarantee\nCopy: Enhance Your Outdoor Space with Professional Landscaping Services. From creative designs to sustainable maintenance, Green Thumb Landscaping has you covered. Our certified arborists and irrigation experts ensure your landscape stays lush and beautiful year-round. Experience the difference in Portland, OR!

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Tech Genie IT Solutions\nLocation: Austin, TX\nServices: IT Consulting, Network Security, Cloud Services, Data Backup & Recovery\nBenefits: 24/7 IT Support, Certified Technicians, Customized Solutions for Businesses\nCopy: Simplify Your IT with Tech Genie. Our team of certified technicians provides reliable IT solutions for businesses in Austin, TX. From comprehensive network security to cloud services, we've got your back 24/7. Focus on your core business while we handle your tech needs.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Fresh Bites Catering\nLocation: Chicago, IL\nServices: Corporate Catering, Event Planning, Custom Menu Design, Dietary Options\nBenefits: Farm-to-table Ingredients, Experienced Event Coordinators, On-time Delivery\nCopy: Elevate Your Events with Fresh Bites Catering. We bring a fresh twist to catering in Chicago, IL. Our farm-to-table ingredients and custom menu design ensure an unforgettable dining experience. Our experienced event coordinators take care of all the details, so you can savor every moment.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Artistic Ink Tattoo Studio\nLocation: Seattle, WA\nServices: Custom Tattoos, Cover-ups, Body Piercing, Tattoo Removal\nBenefits: Award-winning Artists, Strict Sanitary Standards, Free Consultations\nCopy: Express Yourself with Artistic Ink Tattoos. Our award-winning artists in Seattle, WA, create unique and meaningful tattoos that tell your story. Safety is our top priority, with strict sanitary standards. Book a free consultation to discuss your tattoo ideas today!

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Dance Fusion Studios\nLocation: Miami, FL\nServices: Ballet, Hip-Hop, Contemporary, Latin Dance, Fitness Classes\nBenefits: Certified Instructors, Spacious Dance Studios, Beginner to Advanced Levels\nCopy: Find Your Rhythm at Dance Fusion Studios. From classic ballet to high-energy hip-hop, we offer diverse dance classes in Miami, FL. Our certified instructors welcome dancers of all levels to experience the joy of movement in our spacious studios.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Wellness Haven Spa\nLocation: San Francisco, CA\nServices: Massage Therapy, Facial Treatments, Sauna, Aromatherapy\nBenefits: Relaxing Ambiance, Skilled Therapists, Personalized Spa Packages\nCopy: Unwind and Rejuvenate at Wellness Haven Spa. Treat yourself to a serene spa experience in San Francisco, CA. Our skilled therapists and soothing ambiance melt away stress, leaving you refreshed and revitalized. Explore our personalized spa packages for the ultimate indulgence.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Adventure Seekers Outdoor Gear\nLocation: Denver, CO\nServices: Camping Gear Rental, Hiking Equipment, Outdoor Apparel\nBenefits: High-Quality Gear, Expert Advice, Convenient Delivery Options\nCopy: Gear Up for the Great Outdoors at Adventure Seekers. Discover the beauty of Colorado with top-notch camping gear and outdoor apparel. Our expert team helps you choose the right equipment, and we offer convenient delivery options to make your adventures hassle-free.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Pawsome Pet Grooming\nLocation: Houston, TX\nServices: Dog Grooming, Cat Grooming, Nail Trimming, Ear Cleaning\nBenefits: Gentle Handling, Pet-Friendly Products, Tailored Grooming Packages\nCopy: Pamper Your Pets at Pawsome Pet Grooming. Our skilled groomers in Houston, TX, provide compassionate care for your furry friends. Using pet-friendly products and gentle handling, we ensure your pets leave looking and feeling their best.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Sunlit Yoga Studio\nLocation: Phoenix, AZ\nServices: Yoga Classes, Meditation Sessions, Wellness Workshops\nBenefits: Experienced Instructors, Welcoming Environment, Mind-Body Connection\nCopy: Embrace Wellness at Sunlit Yoga Studio. Join our community in Phoenix, AZ, and discover the transformative power of yoga and meditation. Our experienced instructors create a welcoming environment where you can explore the mind-body connection.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: The Vintage Bookshop\nLocation: Charleston, SC\nServices: Rare Books, Vintage Collectibles, Book Restoration, Book Appraisals\nBenefits: Extensive Collection, Knowledgeable Staff, Preservation Experts\nCopy: Journey through Time at The Vintage Bookshop. Delve into literary treasures and vintage collectibles in Charleston, SC. Our knowledgeable staff and preservation experts celebrate the beauty of rare books and offer book restoration services to preserve your own treasures.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Artisanal Coffee Roasters\nLocation: Portland, OR\nServices: Small-batch Coffee Roasting, Coffee Tasting Events, Wholesale Distribution\nBenefits: Single-Origin Beans, Sustainable Practices, Custom Blends\nCopy: Savor the Flavors of Artisanal Coffee Roasters. In Portland, OR, we take coffee seriously. Our small-batch roasting and single-origin beans deliver exceptional flavor profiles. Experience the art of coffee through our tasting events and explore custom blends for your business.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Harmony Wellness Center\nLocation: Santa Fe, NM\nServices: Holistic Healing, Reiki Therapy, Sound Healing, Wellness Retreats\nBenefits: Holistic Approach, Certified Practitioners, Nurturing Sanctuary\nCopy: Find Balance at Harmony Wellness Center. Embrace holistic healing in Santa Fe, NM. Our certified practitioners offer Reiki therapy and sound healing to promote physical, emotional, and spiritual well-being. Join our wellness retreats for a transformative journey.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: The Comic Vault\nLocation: New Orleans, LA\nServices: Comic Books, Graphic Novels, Collectible Merchandise, Pop Culture Events\nBenefits: Diverse Selection, Knowledgeable Staff, Comic Book Subscriptions\nCopy: Enter the World of The Comic Vault. For comic book enthusiasts in New Orleans, LA, we offer a treasure trove of graphic novels and collectible merchandise. Our knowledgeable staff is passionate about pop culture and can set up comic book subscriptions tailored to your preferences.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: The Green Thumb Nursery\nLocation: Seattle, WA\nServices: Indoor Plants, Outdoor Plants, Garden Design, Plant Care Workshops\nBenefits: Expert Advice, Quality Plants, Sustainable Gardening Practices\nCopy: Cultivate Beauty with The Green Thumb Nursery. Bring nature indoors with our selection of indoor plants or transform your outdoor space with expertly curated gardens. In Seattle, WA, we're your go-to source for quality plants and sustainable gardening practices.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Chef's Palette Culinary School\nLocation: San Diego, CA\nServices: Cooking Classes, Culinary Workshops, Private Chef Services\nBenefits: Experienced Chefs, Hands-On Learning, Customized Menus\nCopy: Unlock Your Culinary Creativity at Chef's Palette. Embark on a culinary journey in San Diego, CA. Our experienced chefs lead interactive cooking classes and workshops for aspiring foodies. Elevate your dining experience with private chef services and customized menus.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: ZenDen Meditation Center\nLocation: Boulder, CO\nServices: Guided Meditations, Mindfulness Workshops, Stress Reduction Programs\nBenefits: Tranquil Environment, Skilled Meditation Instructors, Mental Clarity\nCopy: Discover Inner Peace at ZenDen Meditation Center. Find solace and mental clarity in Boulder, CO. Our skilled meditation instructors guide you through transformative meditations and mindfulness workshops. Join our stress reduction programs and experience a tranquil haven.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Revive Fitness Studio\nLocation: Austin, TX\nServices: Personal Training, Group Fitness Classes, Nutrition Counseling\nBenefits: Certified Trainers, State-of-the-Art Equipment, Individualized Programs\nCopy: Elevate Your Fitness Journey at Revive Fitness Studio. Achieve your fitness goals in Austin, TX. Our certified trainers provide personalized attention in group classes and individual sessions. Embrace a healthier lifestyle with nutrition counseling and access to state-of-the-art equipment.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Wanderlust Travel Agency\nLocation: Honolulu, HI\nServices: Travel Planning, Destination Weddings, Adventure Tours\nBenefits: Expert Travel Advisors, Tailored Itineraries, Exclusive Deals\nCopy: Embark on Adventures with Wanderlust Travel Agency. Your dream vacation awaits in Honolulu, HI. Our expert travel advisors craft personalized itineraries, whether you're planning a destination wedding or seeking adrenaline-pumping adventure tours.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Golden Paws Veterinary Clinic\nLocation: Denver, CO\nServices: Preventive Care, Veterinary Surgery, Dental Services, Pet Boarding\nBenefits: Compassionate Care, State-of-the-Art Facilities, Fear-Free Environment\nCopy: Ensure Your Pet's Well-being at Golden Paws Veterinary Clinic. Our Denver, CO clinic offers compassionate care for your furry companions. From preventive care to veterinary surgery, we prioritize your pet's health and comfort in our fear-free environment.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Harmonic Sound Productions\nLocation: Nashville, TN\nServices: Music Production, Sound Engineering, Studio Recording\nBenefits: Grammy-winning Engineers, High-end Equipment, Tailored Music Production\nCopy: Create Your Masterpiece with Harmonic Sound Productions. In Nashville, TN, we bring your musical vision to life with Grammy-winning engineers and top-notch equipment. Whether you're recording a single or a full album, expect exceptional music production tailored to your style.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Stellar Tech Solutions\nLocation: San Francisco, CA\nServices: Web Development, App Development, Digital Marketing\nBenefits: Custom Solutions, Cutting-edge Technology, Proven Results\nCopy: Reach New Heights with Stellar Tech Solutions. Our San Francisco, CA team provides top-notch web and app development to enhance your online presence. From tailored solutions to effective digital marketing, we propel your business to success.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Blissful Bakes Bakery\nLocation: New York City, NY\nServices: Custom Cakes, Artisan Pastries, Wedding Desserts\nBenefits: Creative Designs, High-quality Ingredients, On-time Delivery\nCopy: Indulge in Blissful Bakes Bakery Delicacies. In New York City, NY, we craft custom cakes and artisan pastries that taste as good as they look. Trust us to sweeten your special occasions with our creative designs and high-quality ingredients.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Craft & Cork Winery\nLocation: Napa Valley, CA\nServices: Wine Tasting, Winery Tours, Private Events\nBenefits: Expert Sommeliers, Award-winning Wines, Scenic Vineyard Views\nCopy: Savor the Flavors at Craft & Cork Winery. Experience the essence of Napa Valley, CA, with our expert sommeliers and award-winning wines. Enjoy a wine tasting or winery tour, and host your private events amidst scenic vineyard views.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Stellar Prints Photography\nLocation: Seattle, WA\nServices: Portrait Photography, Event Photography, Photo Editing\nBenefits: Talented Photographers, High-resolution Images, Quick Turnaround\nCopy: Capture Precious Moments with Stellar Prints Photography. Our Seattle, WA photographers create stunning portraits and capture unforgettable events. We deliver high-resolution images with a quick turnaround, preserving your cherished memories.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: AquaFit Aquatic Center\nLocation: Miami, FL\nServices: Swimming Lessons, Water Aerobics, Aqua Therapy\nBenefits: Certified Instructors, Heated Pools, Personalized Programs\nCopy: Dive into Wellness at AquaFit Aquatic Center. In Miami, FL, we offer swimming lessons, water aerobics, and aqua therapy with certified instructors. Our heated pools create the perfect environment for personalized wellness programs.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Urban Trails Bike Shop\nLocation: Portland, OR\nServices: Bike Sales, Repairs, Bike Rentals, Guided Tours\nBenefits: Knowledgeable Staff, Top Bicycle Brands, Scenic Trails\nCopy: Pedal with Urban Trails Bike Shop. Explore Portland, OR, on two wheels with our top-notch bike sales, rentals, and guided tours. Our knowledgeable staff ensures you have the perfect bike for scenic adventures.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: The Fashion Emporium\nLocation: New York City, NY\nServices: Boutique Shopping, Personal Styling, Fashion Events\nBenefits: Trendy Collections, Expert Stylists, Exclusive Designer Collaborations\nCopy: Elevate Your Style at The Fashion Emporium. In the heart of New York City, NY, discover a curated selection of trendy collections and exclusive designer collaborations. Our expert stylists help you find the perfect look for any occasion.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Harmony Horizons Music School\nLocation: Nashville, TN\nServices: Music Lessons, Instrument Rentals, Performance Opportunities\nBenefits: Skilled Instructors, Flexible Scheduling, Recital Hall Access\nCopy: Discover Your Musical Talent at Harmony Horizons. Our Nashville, TN music school offers comprehensive music lessons and instrument rentals for all ages. Whether you're a beginner or an aspiring musician, our skilled instructors guide you on a harmonious journey.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Zenith Tech Repair\nLocation: Los Angeles, CA\nServices: Electronics Repair, Phone Screen Replacement, Computer Troubleshooting\nBenefits: Certified Technicians, Quick Turnaround, Affordable Prices\nCopy: Restore Functionality with Zenith Tech Repair. In Los Angeles, CA, we provide expert electronics repair and phone screen replacement services. Our certified technicians deliver quick solutions at affordable prices.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: GreenThumb Landscaping\nLocation: Portland, OR\nServices: Lawn Care, Landscape Design, Tree Trimming, Irrigation\nBenefits: Eco-friendly practices, Certified Arborists, Free Consultation\nCopy: Create Your Dream Landscape with GreenThumb Landscaping. Our team of certified arborists and landscape designers will transform your outdoor space into a lush and beautiful haven. From lawn care to tree trimming, we offer eco-friendly solutions. Schedule a free consultation now!

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: TechGenius IT Solutions\nLocation: Austin, TX\nServices: IT Support, Network Security, Cloud Solutions, Data Recovery\nBenefits: 24/7 IT support, Certified Technicians, Customized Solutions\nCopy: Stay Ahead with TechGenius IT Solutions. Our certified technicians provide 24/7 IT support, ensuring your business operates smoothly. Whether you need network security or cloud solutions, we offer customized plans to meet your needs. Contact us for reliable IT services!

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Pet Paradise Resort\nLocation: Denver, CO\nServices: Dog Boarding, Cat Sitting, Grooming, Doggy Daycare\nBenefits: Luxurious facilities, Certified Pet Caretakers, Webcam Access\nCopy: Pamper Your Pets at Pet Paradise Resort. We offer luxurious facilities and certified pet caretakers to ensure your furry friends have a wonderful stay. With webcam access, you can check on your pets anytime. From doggy daycare to grooming, we cater to all their needs.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Zen Yoga Studio\nLocation: San Francisco, CA\nServices: Yoga Classes, Meditation Workshops, Mindfulness Retreats\nBenefits: Experienced Instructors, Serene Atmosphere, Introductory Offers\nCopy: Find Your Inner Peace at Zen Yoga Studio. Our experienced instructors guide you through yoga and meditation classes in a serene atmosphere. Whether you're a beginner or experienced, we have something for everyone. Check out our introductory offers today!

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Express Print Solutions\nLocation: Chicago, IL\nServices: Printing Services, Graphic Design, Signage, Promotional Products\nBenefits: Fast Turnaround, Creative Design Team, Bulk Discounts\nCopy: Get Your Message Across with Express Print Solutions. From printing services to creative graphic design, we help your brand stand out. With fast turnaround times and bulk discounts, we ensure your promotional products are ready when you need them. Contact us for top-quality prints!

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: FitZone Fitness Center\nLocation: Miami Beach, FL\nServices: Personal Training, Group Classes, Nutrition Counseling\nBenefits: Certified Trainers, State-of-the-Art Equipment, Trial Membership\nCopy: Achieve Your Fitness Goals at FitZone Fitness Center. Our certified trainers and state-of-the-art equipment ensure you get the best workout experience. Join our group classes or opt for personalized training with nutrition counseling. Try our trial membership and start your fitness journey today!

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Stellar Event Planning\nLocation: New Orleans, LA\nServices: Event Management, Wedding Planning, Corporate Events\nBenefits: Experienced Planners, Unique Themes, Budget-Friendly Options\nCopy: Plan Your Dream Event with Stellar Event Planning. Our experienced planners bring your vision to life with unique themes and attention to detail. Whether it's a wedding or corporate event, we offer budget-friendly options without compromising on quality.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Chef's Palette Catering\nLocation: Seattle, WA\nServices: Catering for Events, Private Chef Services, Cooking Classes\nBenefits: Gourmet Menus, Experienced Chefs, Customized Offerings\nCopy: Savor Culinary Delights with Chef's Palette Catering. Our gourmet menus prepared by experienced chefs will delight your guests. From catering to private chef services, we tailor our offerings to suit your preferences. Join our cooking classes for an immersive culinary experience!

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Playland Fun Park\nLocation: Orlando, FL\nServices: Amusement Rides, Mini Golf, Arcade Games, Birthday Parties\nBenefits: All-Day Passes, Family-Friendly, Party Packages\nCopy: Create Lasting Memories at Playland Fun Park. With amusement rides, mini golf, and arcade games, we're the perfect destination for family fun. Get our all-day passes for unlimited play, and book a birthday party package for a special celebration!

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Wellness Haven Spa\nLocation: Asheville, NC\nServices: Massage Therapy, Facials, Aromatherapy, Yoga Classes\nBenefits: Relaxing Environment, Certified Therapists, Membership Plans\nCopy: Indulge in Tranquility at Wellness Haven Spa. Our certified therapists and relaxing environment will rejuvenate your body and mind. Enjoy a range of services, from massage therapy to yoga classes. Join our membership plans for regular pampering!

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Adventure Seekers Travel Agency\nLocation: Denver, CO\nServices: Vacation Packages, Adventure Tours, Hiking Expeditions\nBenefits: Expert Travel Planners, Custom Itineraries, Group Discounts\nCopy: Embark on Thrilling Journeys with Adventure Seekers Travel Agency. Our expert travel planners create custom itineraries for your dream vacations. Whether it's an adventure tour or a hiking expedition, we offer group discounts for memorable experiences.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Artistic Blooms Florist\nLocation: Portland, ME\nServices: Floral Arrangements, Wedding Flowers, Event Decor\nBenefits: Creative Designers, Fresh Blooms, Same-Day Delivery\nCopy: Celebrate with Elegance at Artistic Blooms Florist. Our creative designers use fresh blooms to craft stunning floral arrangements for your special moments. From wedding flowers to event decor, we provide same-day delivery for your convenience.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: The Bookworm Bookstore\nLocation: Boston, MA\nServices: Book Sales, Author Events, Book Clubs, Coffee Shop\nBenefits: Extensive Collection, Literary Events, Cozy Atmosphere\nCopy: Discover a World of Stories at The Bookworm Bookstore. We offer an extensive collection of books for all ages and genres. Join our author events and book clubs for literary discussions in our cozy coffee shop setting.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Mindful Eats Restaurant\nLocation: Boulder, CO\nServices: Plant-Based Cuisine, Farm-to-Table Dishes, Catering\nBenefits: Nutritious Menus, Sustainable Sourcing, Gluten-Free Options\nCopy: Nourish Your Body and Soul at Mindful Eats Restaurant. Our plant-based cuisine features farm-to-table dishes with sustainable sourcing. Enjoy our nutritious menus, including gluten-free options. Contact us for catering your next event.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Harmony Music Academy\nLocation: Nashville, TN\nServices: Music Lessons, Instrument Rentals, Recording Studio\nBenefits: Experienced Instructors, Recital Opportunities, Flexible Scheduling\nCopy: Embrace the Rhythm at Harmony Music Academy. Our experienced instructors offer music lessons for various instruments. Showcase your talent with recital opportunities, or rent our recording studio to capture your musical journey.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: MindCraft Escape Rooms\nLocation: San Diego, CA\nServices: Escape Games, Virtual Reality Adventures, Team Building\nBenefits: Immersive Themes, Challenging Puzzles, Corporate Packages\nCopy: Unleash Your Inner Detective at MindCraft Escape Rooms. Immerse yourself in thrilling escape games and virtual reality adventures. Strengthen teamwork and communication with our team-building activities, available in corporate packages.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Artisan Brew Co.\nLocation: Austin, TX\nServices: Craft Beer Tasting, Brewery Tours, Private Events\nBenefits: Locally Crafted Beers, Knowledgeable Brewers, Beer Club\nCopy: Savor Handcrafted Brews at Artisan Brew Co. Indulge in craft beer tasting, guided by our knowledgeable brewers. Join our beer club for exclusive releases, or book us for private events and brewery tours.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: FitFam Family Fitness\nLocation: Raleigh, NC\nServices: Family Workout Classes, Kids' Fitness, Parent-Child Activities\nBenefits: Certified Trainers, Fun Workouts, Family Memberships\nCopy: Stay Active Together at FitFam Family Fitness. Our certified trainers lead fun family workout classes and kids' fitness activities. Join us for parent-child activities and get fit as a family with our membership plans.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Curious Minds Science Center\nLocation: Seattle, WA\nServices: Science Exhibits, STEM Workshops, Birthday Parties\nBenefits: Hands-On Learning, Knowledgeable Educators, Members' Discounts\nCopy: Unleash Curiosity at Curious Minds Science Center. Our science exhibits and STEM workshops offer hands-on learning for all ages. Celebrate birthdays with interactive parties, and enjoy members' discounts on our programs.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Coastal Breeze Surf School\nLocation: Santa Barbara, CA\nServices: Surfing Lessons, Stand-Up Paddleboarding, Beach Rentals\nBenefits: Certified Instructors, Pristine Locations, Group Packages\nCopy: Catch the Wave with Coastal Breeze Surf School. Our certified instructors will teach you to ride the waves or stand-up paddleboard in pristine coastal locations. Enjoy special group packages for unforgettable beach adventures.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Thrive Green Eco-Friendly Cleaning\nLocation: Portland, OR\nServices: Residential Cleaning, Office Cleaning, Green Products\nBenefits: Safe Cleaning Solutions, Reliable Service, Recurring Discounts\nCopy: Clean with a Conscience at Thrive Green Eco-Friendly Cleaning. Our green products ensure safe and effective cleaning for homes and offices. Count on our reliable service and take advantage of recurring discounts.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Dapper Cuts Barber Shop\nLocation: New York City, NY\nServices: Men's Haircuts, Hot Shaves, Beard Grooming\nBenefits: Skilled Barbers, Classic Techniques, Membership Loyalty Program\nCopy: Elevate Your Style at Dapper Cuts Barber Shop. Our skilled barbers offer men's haircuts, hot shaves, and precise beard grooming. Experience classic techniques and join our membership loyalty program for exclusive perks.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Pet Pawsitivity Training Academy\nLocation: Chicago, IL\nServices: Dog Training, Puppy Socialization, Canine Behavior Therapy\nBenefits: Positive Reinforcement, Certified Trainers, Training Packages\nCopy: Train with Positivity at Pet Pawsitivity Training Academy. Our certified trainers use positive reinforcement to create a strong bond with your furry friend. Enroll in our puppy socialization classes or opt for canine behavior therapy with customized training packages.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Meditative Mind Wellness Center\nLocation: Sedona, AZ\nServices: Meditation Workshops, Energy Healing, Crystal Therapy\nBenefits: Spiritual Retreats, Tranquil Environment, Holistic Practitioners\nCopy: Find Inner Harmony at Meditative Mind Wellness Center. Join our meditation workshops and experience the transformative power of energy healing and crystal therapy. Immerse yourself in spiritual retreats with guidance from our holistic practitioners.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Rainbow Bites Vegan Cafe\nLocation: San Francisco, CA\nServices: Vegan Cuisine, Juice Bar, Gluten-Free Bakery\nBenefits: Plant-Based Options, Fresh Ingredients, Meal Subscriptions\nCopy: Savor the Flavors at Rainbow Bites Vegan Cafe. Indulge in delicious vegan cuisine from our juice bar and gluten-free bakery. With plant-based options and fresh ingredients, you can even subscribe to our meal plans for convenience.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Playful Paws Daycare\nLocation: Toronto, Canada\nServices: Dog Daycare, Dog Walking, Pet Sitting\nBenefits: Indoor Play Area, Certified Handlers, Pet First Aid\nCopy: Unleash the Fun at Playful Paws Daycare. Our indoor play area and certified handlers ensure a safe and playful environment for your furry companions. Choose from dog daycare or pet sitting services, knowing they're in caring hands with pet first aid knowledge.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Rejuvenate Spa Retreat\nLocation: Miami, FL\nServices: Spa Treatments, Couples' Packages, Detox Therapies\nBenefits: Luxurious Retreat, Skilled Therapists, Spa Memberships\nCopy: Experience Bliss at Rejuvenate Spa Retreat. Our skilled therapists offer a range of spa treatments and detox therapies in a luxurious retreat setting. Treat yourself and your loved one to couples' packages or join our spa memberships for regular relaxation.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Gourmet Grains Bakery\nLocation: Portland, OR\nServices: Artisan Breads, Pastry Delights, Custom Cakes\nBenefits: Organic Ingredients, Handcrafted Goodness, Online Ordering\nCopy: Indulge in Delicacies at Gourmet Grains Bakery. Our artisan breads and pastry delights are made with organic ingredients and handcrafted goodness. Customize your cakes for special occasions and enjoy the convenience of online ordering.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Harmony Haven Yoga Studio\nLocation: Sedona, AZ\nServices: Yoga Classes, Reiki Healing, Sound Therapy\nBenefits: Spiritual Retreats, Holistic Instructors, Wellness Workshops\nCopy: Find Balance at Harmony Haven Yoga Studio. Our holistic instructors guide you through yoga classes, Reiki healing, and sound therapy for complete well-being. Join our spiritual retreats or attend wellness workshops for inner harmony.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: Active Paws Adventure Club\nLocation: Vancouver, Canada\nServices: Dog Hiking, Outdoor Playdates, Pet Photography\nBenefits: Scenic Trails, Pet-Friendly Staff, Adventure Memberships\nCopy: Explore with Enthusiasm at Active Paws Adventure Club. Our dog hiking adventures and outdoor playdates are led by pet-friendly staff on scenic trails. Capture those precious moments with our pet photography services and become a member of our adventure club.

##

Write engaging and promotional website descriptions for small business website based on business details\nBusiness name: The Petal Palette Florist\nLocation: Charleston, SC\nServices: Floral Arrangements, Wedding Flowers, Event Decor\nBenefits: Artistic Designs, Fresh Blooms, Free Consultations\nCopy: Celebrate with Elegance at The Petal Palette Florist. Our artistic designs feature fresh blooms for stunning floral arrangements, wedding flowers, and event decor. Schedule a free consultation and let us bring beauty to your special occasions.

##

Write engaging and promotional website descriptions for small business website based on business details\n
'''

def query(prompt):
    config = {
        "numResults": 1,
        "minTokens": 30,
        "maxTokens": 64,
        "temperature": 0.95,
        "topKReturn": 0,
        "topP":0.98,
        "countPenalty": {
            "scale": 0,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        "frequencyPenalty": {
            "scale": 225,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        "presencePenalty": {
            "scale": 1.2,
            "applyToNumbers": False,
            "applyToPunctuations": False,
            "applyToStopwords": False,
            "applyToWhitespaces": False,
            "applyToEmojis": False
        },
        "stopSequences":["##"]
    }

    res = complete(model_type=DEFAULT_MODEL,
                   prompt=prompt,
                   **config)

    return res["completions"][0]["data"]["text"]


if __name__ == '__main__':

    apply_studio_style()
    st.title("Moving Along website generator - Type A")
    st.markdown("###### This is a demo of the Moving Along website generator. It  produces engaging and promotional website copy following MA's brand voice.")

    inp_business_name = st.text_input("Enter the name of the business:", value="El Zapato Magico")
    inp_location = st.text_input("Enter the location of the business:", value="Seattle")
    inp_services = st.text_area("List your services here:", value="- Custom shoes\n- Custom boots\n- Shoe repair\n- Shoe cleaning\n- Shoe accessories")
    inp_benefits = st.text_area("List the benefits of your services here:", value="- High quality\n- Professional\n- Friendly\n- Hand crafted by magical elves\n- Guaranteed 98% curse free")

    prompt = base_prompt + f"Business name: {inp_business_name}\nLocation: {inp_location}\nServices: {inp_services}\nBenefits: {inp_benefits}\nCopy: "

    if st.button(label="Generate Copy"):
        st.session_state["short-form-save_results_ind"] = []
        with st.spinner("Loading..."):
            st.session_state["short-form-result"] = {
                "completion": query(prompt),
            }

    if "short-form-result" in st.session_state:
        result = st.session_state["short-form-result"]["completion"]
        st.text("")
        st.text_area("Generated Product Description", result, height=200)




