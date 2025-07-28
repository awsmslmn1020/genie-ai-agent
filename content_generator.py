def get_template(target):
    if target == "Brand":
        return {
            "subject": "Let's Connect You with the Right Influencers (No Upfront Cost)",
            "body": """Hi {{name}},

I’m reaching out from imaconnect — we help brands grow through strategic influencer partnerships with zero upfront cost.

Here’s what we do:
✅ We match your brand with premium influencers based on niche, audience, and intent
✅ You only pay once the post is approved and live
✅ We ensure performance, compliance, and smooth collaboration

Interested in a no-obligation proposal tailored to your brand?
Let’s connect via: www.imaconnect.online or reply to this email.

Looking forward to hearing from you."""
        }
    else:
        return {
            "subject": "Collaborate with Brands That Pay – No Upfront Cost",
            "body": """Hi {{name}},

I'm reaching out from imaconnect, an agency that connects creators like you with real, paid brand deals.

You get matched with brands that fit your audience.
We take a small commission only from sponsorship amount after the deal is confirmed.
You don't pay anything upfront, and there's no obligation unless we land you real opportunities.

Reply to this email or DM us on IG @ima_connect!"""
        }