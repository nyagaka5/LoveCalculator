import random
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LoveResult

@csrf_exempt
def home(request):
    # Scenario 1: The user clicked "Calculate Love %" (Form Submitted)
    if request.method == "POST":
        your_name = request.POST.get("your_name", "").strip()
        crush_name = request.POST.get("crush_name", "").strip()

        if your_name and crush_name:
            # Generate a random love score percentage
            score = random.randint(40, 100)

            # Save the calculation directly into your PostgreSQL database
            result = LoveResult.objects.create(
                your_name=your_name,
                crush_name=crush_name,
                score=score
            )

            # Display the result screen to the user
            return HttpResponse(f"""
                <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin-top: 100px; color: #333;">
                    <div style="display: inline-block; background: #fff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #e91e63;">
                        <h1 style="color: #e91e63; margin-bottom: 10px;">Love Match Found! ❤️</h1>
                        <p style="font-size: 22px; margin: 20px 0;">
                            <strong>{result.your_name}</strong> & <strong>{result.crush_name}</strong>
                        </p>
                        <div style="font-size: 64px; font-weight: bold; color: #e91e63; margin: 20px 0;">
                            {result.score}%
                        </div>
                        <p style="color: #777; font-size: 14px; margin-bottom: 30px;">
                            ✨ This result has been safely stored in your pgAdmin database.
                        </p>
                        <a href="/" style="text-decoration: none; background: #e91e63; color: white; padding: 12px 25px; border-radius: 25px; font-weight: bold; transition: 0.2s;">
                            Try Another Match
                        </a>
                    </div>
                </div>
            """)

    # Scenario 2: The user just landed on the page (Show Input Form)
    return HttpResponse("""
        <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin-top: 100px; color: #333;">
            <div style="display: inline-block; background: #fff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: left; max-width: 350px; width: 100%;">
                <h1 style="text-align: center; color: #e91e63; margin-top: 0;">Love Calculator ❤️</h1>
                <p style="text-align: center; color: #666; font-size: 14px; margin-bottom: 30px;">
                    Enter two names to see your true compatibility score.
                </p>
                
                <form method="POST">
                    <div style="margin-bottom: 20px;">
                        <label style="display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px;">Your Name:</label>
                        <input type="text" name="your_name" required placeholder="Type your name..." 
                               style="width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #ccc; box-sizing: border-box; font-size: 15px;">
                    </div>
                    
                    <div style="margin-bottom: 25px;">
                        <label style="display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px;">Crush's Name:</label>
                        <input type="text" name="crush_name" required placeholder="Type their name..." 
                               style="width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #ccc; box-sizing: border-box; font-size: 15px;">
                    </div>
                    
                    <button type="submit" 
                            style="width: 100%; background: #e91e63; color: white; border: none; padding: 12px; border-radius: 6px; font-size: 16px; font-weight: bold; cursor: pointer;">
                        Calculate Love %
                    </button>
                </form>
            </div>
        </div>
    """)