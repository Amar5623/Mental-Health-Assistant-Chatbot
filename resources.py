class MentalHealthResources:
    @staticmethod
    def get_crisis_resources():
        return {
            "US": {
                "National Suicide Prevention Lifeline": {
                    "phone": "1-800-273-8255",
                    "website": "https://suicidepreventionlifeline.org/",
                    "description": "24/7, free and confidential support for people in distress."
                },
                "Crisis Text Line": {
                    "text": "HOME to 741741",
                    "website": "https://www.crisistextline.org/",
                    "description": "Text-based crisis support available 24/7."
                },
                "SAMHSA's National Helpline": {
                    "phone": "1-800-662-4357",
                    "website": "https://www.samhsa.gov/find-help/national-helpline",
                    "description": "Treatment referral and information service for individuals facing mental health or substance use disorders."
                }
            },
            "International": {
                "International Association for Suicide Prevention": {
                    "website": "https://www.iasp.info/resources/Crisis_Centres/",
                    "description": "Directory of crisis centers around the world."
                },
                "Befrienders Worldwide": {
                    "website": "https://www.befrienders.org/",
                    "description": "Global network of crisis helplines providing emotional support."
                }
            }
        }
    
    @staticmethod
    def get_therapy_resources():
        return {
            "Online Therapy Services": {
                "BetterHelp": {
                    "website": "https://www.betterhelp.com/",
                    "description": "Online counseling platform with licensed therapists."
                },
                "Talkspace": {
                    "website": "https://www.talkspace.com/",
                    "description": "Online therapy with licensed therapists via text, audio, or video."
                },
                "7 Cups": {
                    "website": "https://www.7cups.com/",
                    "description": "Online emotional support from trained listeners and therapists."
                }
            },
            "Finding a Therapist": {
                "Psychology Today": {
                    "website": "https://www.psychologytoday.com/us/therapists",
                    "description": "Directory to find therapists in your area."
                },
                "Therapy for Black Girls": {
                    "website": "https://therapyforblackgirls.com/",
                    "description": "Resource for connecting Black women with culturally competent therapists."
                },
                "Open Path Psychotherapy Collective": {
                    "website": "https://openpathcollective.org/",
                    "description": "Affordable therapy options for individuals, couples, and families."
                }
            }
        }
    
    @staticmethod
    def get_self_help_resources():
        return {
            "Apps": {
                "Headspace": {
                    "website": "https://www.headspace.com/",
                    "description": "Meditation and mindfulness app to help with stress, anxiety, and sleep."
                },
                "Calm": {
                    "website": "https://www.calm.com/",
                    "description": "App for meditation, sleep stories, and relaxation."
                },
                "Woebot": {
                    "website": "https://woebothealth.com/",
                    "description": "AI chatbot that uses cognitive-behavioral therapy techniques."
                }
            },
            "Websites": {
                "MoodGYM": {
                    "website": "https://moodgym.com.au/",
                    "description": "Interactive self-help program for preventing and coping with depression and anxiety."
                },
                "Mental Health America": {
                    "website": "https://www.mhanational.org/",
                    "description": "Resources, tools, and information about mental health conditions."
                },
                "NAMI (National Alliance on Mental Illness)": {
                    "website": "https://www.nami.org/",
                    "description": "Education, support, and advocacy for individuals affected by mental illness."
                }
            },
            "Books": {
                "Feeling Good: The New Mood Therapy": {
                    "author": "David D. Burns",
                    "description": "Classic book on cognitive behavioral therapy techniques for depression and anxiety."
                },
                "The Anxiety and Phobia Workbook": {
                    "author": "Edmund J. Bourne",
                    "description": "Practical workbook with exercises for managing anxiety and phobias."
                },
                "The Mindful Way Through Depression": {
                    "author": "Mark Williams, John Teasdale, Zindel Segal, and Jon Kabat-Zinn",
                    "description": "Combines cognitive therapy with mindfulness practices to prevent depression relapse."
                }
            }
        }
    
    @staticmethod
    def format_resources_for_chat(resource_type="all"):
        """Format resources into a readable chat message"""
        message = "Here are some mental health resources that might be helpful:\n\n"
        
        if resource_type == "crisis" or resource_type == "all":
            crisis = MentalHealthResources.get_crisis_resources()
            message += "🚨 CRISIS RESOURCES 🚨\n"
            message += "If you're in immediate danger, please call emergency services (911 in the US).\n\n"
            
            for region, resources in crisis.items():
                message += f"{region}:\n"
                for name, info in resources.items():
                    message += f"• {name}: "
                    if "phone" in info:
                        message += f"Call {info['phone']}. "
                    if "text" in info:
                        message += f"Text {info['text']}. "
                    message += f"Website: {info['website']}\n"
            
            message += "\n"
        
        if resource_type == "therapy" or resource_type == "all":
            therapy = MentalHealthResources.get_therapy_resources()
            message += "🧠 THERAPY RESOURCES 🧠\n"
            
            for category, resources in therapy.items():
                message += f"{category}:\n"
                for name, info in resources.items():
                    message += f"• {name}: {info['description']} Website: {info['website']}\n"
            
            message += "\n"
        
        if resource_type == "self_help" or resource_type == "all":
            self_help = MentalHealthResources.get_self_help_resources()
            message += "📚 SELF-HELP RESOURCES 📚\n"
            
            for category, resources in self_help.items():
                message += f"{category}:\n"
                for name, info in resources.items():
                    message += f"• {name}: "
                    if "author" in info:
                        message += f"by {info['author']}. "
                    message += f"{info['description']}"
                    if "website" in info:
                        message += f" Website: {info['website']}"
                    message += "\n"
        
        message += "\nRemember, seeking help is a sign of strength, not weakness. You deserve support."
        
        return message
