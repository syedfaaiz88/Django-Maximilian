from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "a-day-at-the-beach",
        "image": "beach.jpg",
        "author": "Samantha",
        "date": date(2023, 6, 15),
        "title": "Relaxing by the Sea",
        "excerpt": "The sun, the sand, the waves - a perfect day at the beach. Here's what made it so special!",
        "content": """
          There's nothing quite like the feeling of the warm sun on your skin and the sound of the waves crashing on the shore.
          Our day at the beach was filled with laughter, sunshine, and relaxation. We built sandcastles, swam in the sea, and enjoyed 
          a beautiful sunset.
          
          The highlight of the day was definitely the beach volleyball game, where everyone joined in for some fun and friendly competition.
          We ended the day with a beach bonfire, roasting marshmallows and sharing stories under the starry sky.
        """
    },
    {
        "slug": "exploring-ancient-ruins",
        "image": "ruins.jpg",
        "author": "John",
        "date": date(2022, 9, 12),
        "title": "A Journey Through Time",
        "excerpt": "Stepping into history by exploring ancient ruins. A day of discovery and awe.",
        "content": """
          Walking through the remnants of ancient civilizations was a surreal experience. The ruins told stories of a time long past, 
          with each stone and artifact revealing a piece of history. 
          
          The grandeur of the architecture and the intricate details of the carvings were mesmerizing. We learned about the culture, 
          traditions, and everyday life of the people who once inhabited these lands.
          
          The adventure was not just about history but also about appreciating the beauty and resilience of these ancient structures 
          that have withstood the test of time.
        """
    },
    {
        "slug": "cooking-gourmet-meals",
        "image": "cooking.jpg",
        "author": "Emily",
        "date": date(2023, 2, 28),
        "title": "Mastering the Art of Cooking",
        "excerpt": "Turning simple ingredients into gourmet dishes. Join me on my culinary journey.",
        "content": """
          Cooking has always been my passion, and recently, I decided to take it to the next level. From experimenting with new recipes
          to perfecting classic dishes, every moment in the kitchen has been a delightful experience.
          
          The process of selecting fresh ingredients, the aroma of spices, and the satisfaction of seeing the final dish come together 
          is truly rewarding. My latest creations include a delectable mushroom risotto, a rich and creamy chocolate mousse, and a 
          perfectly seared steak with a side of garlic butter asparagus.
          
          Cooking is not just about feeding the body but also about nourishing the soul. It's a creative outlet and a way to bring 
          joy to myself and others.
        """
    },
    {
        "slug": "cycling-adventures",
        "image": "cycling.jpg",
        "author": "Michael",
        "date": date(2021, 11, 5),
        "title": "Pedal Power",
        "excerpt": "Exploring new trails and enjoying the freedom of cycling. Here's my latest adventure.",
        "content": """
          There's a unique sense of freedom that comes with cycling. The wind in your face, the open road ahead, and the thrill of 
          discovering new trails make every ride an adventure.
          
          My recent cycling trip took me through scenic landscapes, challenging terrains, and peaceful countryside. Each day brought 
          new sights and experiences, from picturesque villages to breathtaking mountain views.
          
          Cycling is not just a great way to stay fit but also a wonderful opportunity to connect with nature and explore the world 
          around us. Every pedal stroke is a step towards new discoveries.
        """
    },
    {
        "slug": "urban-gardening",
        "image": "gardening.jpg",
        "author": "Rachel",
        "date": date(2023, 4, 20),
        "title": "Greening the Concrete Jungle",
        "excerpt": "Transforming urban spaces into green havens. My journey in urban gardening.",
        "content": """
          Living in the city doesn't mean you can't enjoy the beauty of nature. Urban gardening has allowed me to create a green oasis
          right in the heart of the concrete jungle.
          
          From container gardening to vertical gardens, I've experimented with various techniques to maximize space and grow a 
          variety of plants. My balcony is now home to vibrant flowers, aromatic herbs, and even some vegetables.
          
          Gardening has brought a sense of peace and fulfillment to my life. It's amazing to see how a little bit of green can 
          transform a space and bring joy to everyday living.
        """
    },
    {
        "slug": "art-in-the-city",
        "image": "street-art.jpg",
        "author": "David",
        "date": date(2023, 1, 18),
        "title": "Street Art Chronicles",
        "excerpt": "Exploring the vibrant street art scene in the city. A visual feast for the eyes.",
        "content": """
          The streets of the city are alive with art. From colorful murals to thought-provoking graffiti, street art has become an
          integral part of the urban landscape.
          
          Each piece of art tells a story, reflects the culture, and adds a unique character to the city. I spent a day exploring 
          different neighborhoods, capturing the beauty and creativity of street art.
          
          Street art is more than just visual appeal; it's a form of expression, a way to communicate messages, and a celebration of 
          artistic freedom. It's a reminder that art can be found in the most unexpected places.
        """
    },
    {
        "slug": "tech-conference-2023",
        "image": "tech-conference.jpg",
        "author": "Anna",
        "date": date(2023, 5, 10),
        "title": "Innovations in Tech",
        "excerpt": "Attending the latest tech conference and discovering groundbreaking innovations.",
        "content": """
          The tech conference was a hub of innovation and creativity. Industry leaders, startups, and tech enthusiasts gathered to 
          showcase the latest advancements and share insights into the future of technology.
          
          From AI and machine learning to blockchain and IoT, the conference covered a wide range of topics. The keynote speeches 
          were inspiring, the workshops were informative, and the networking opportunities were invaluable.
          
          The experience left me with a sense of excitement and optimism about the future of technology and its potential to solve 
          real-world problems and improve our lives.
        """
    },
    {
        "slug": "yoga-and-mindfulness",
        "image": "yoga.jpg",
        "author": "Sophia",
        "date": date(2022, 8, 25),
        "title": "Finding Inner Peace",
        "excerpt": "Embracing yoga and mindfulness for a balanced and peaceful life.",
        "content": """
          Yoga and mindfulness have become essential practices in my daily routine. They offer a way to connect with myself, find 
          balance, and cultivate inner peace.
          
          Through yoga, I've learned the importance of breath control, flexibility, and strength. Mindfulness practices have helped 
          me stay present, manage stress, and appreciate the little moments in life.
          
          These practices have not only improved my physical health but also my mental and emotional well-being. They are a reminder 
          that self-care and self-awareness are key to living a fulfilling life.
        """
    },
    {
        "slug": "photography-walk",
        "image": "photography.jpg",
        "author": "James",
        "date": date(2023, 3, 22),
        "title": "Capturing Moments",
        "excerpt": "A photography walk through the city, capturing the beauty in everyday moments.",
        "content": """
          Photography has a way of making us see the world differently. During my recent photography walk, I set out to capture the 
          beauty in everyday moments and ordinary scenes.
          
          From the bustling streets to the quiet parks, every corner of the city offered something unique. The play of light and 
          shadow, the vibrant colors, and the candid expressions of people going about their day all became subjects for my lens.
          
          Photography is not just about taking pictures; it's about telling stories and preserving memories. It's a creative outlet 
          that allows me to share my perspective with the world.
        """
    },
    {
        "slug": "volunteering-journey",
        "image": "volunteering.jpg",
        "author": "Linda",
        "date": date(2022, 12, 5),
        "title": "Giving Back to the Community",
        "excerpt": "My experiences and reflections on volunteering and making a difference.",
        "content": """
          Volunteering has been one of the most rewarding experiences of my life. It's a chance to give back to the community, help 
          those in need, and make a positive impact.
          
          From working at food banks to participating in community clean-up drives, each volunteering opportunity has taught me 
          valuable lessons about empathy, compassion, and teamwork.
          
          The connections I've made and the stories I've heard have been inspiring. Volunteering reminds me that even small acts of 
          kindness can make a big difference and that we all have the power to contribute to a better world.
        """
    }
]


def get_date(post):
  return post['date']

# Create your views here.


def index(request):
    sorted_posts = sorted(all_posts ,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": post
    })
