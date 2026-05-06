from pathlib import Path
import shutil

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand

from core.models import Project, ProjectAsset


class Command(BaseCommand):
    help = "Seed portfolio projects from the folders and media already in the workspace."

    def handle(self, *args, **options):
        base_dir = Path(settings.BASE_DIR)
        Path(settings.MEDIA_ROOT).mkdir(parents=True, exist_ok=True)

        legacy_titles = [
            "AI Chatbot with LangChain and Gemini",
            "Machine Learning Practice Collection",
            "Campus Skill Swap",
            "Sheet-to-Gmail n8n Automation",
            "AI Video Generation",
        ]
        Project.objects.filter(title__in=legacy_titles).delete()

        projects = [
            {
                "title": "Chatbot Project",
                "description": (
                    "A command-line AI chatbot that accepts user input, keeps the conversation going, and returns clear responses."
                ),
                "business_problem": (
                    "Users often need a simple assistant that can answer questions quickly without a full web app "
                    "or complicated interface, so this project focuses on creating an accessible chatbot experience in Python."
                ),
                "overview": (
                    "This project demonstrates a conversational chatbot workflow in Python. It accepts user prompts "
                    "through the terminal, returns AI-generated responses, and maintains a running chat history so "
                    "the conversation feels continuous instead of isolated."
                ),
                "key_features": (
                    "Interactive terminal chat loop\n"
                    "Exit handling with bye or exit commands\n"
                    "Conversation history tracking\n"
                    "Clear prompt-response structure"
                ),
                "role_contribution": (
                    "I built the chatbot logic, managed the user input loop, connected the model response flow, "
                    "and structured the conversation history so the assistant could respond in context."
                ),
                "biggest_challenge": (
                    "The biggest challenge was moving from a one-time prompt into a multi-turn conversation while "
                    "keeping the code readable and the responses stable."
                ),
                "what_learned": (
                    "I learned how to design a basic conversational AI workflow, handle repeated user input, "
                    "and think about the difference between a single model call and an ongoing chatbot experience."
                ),
                "included_files": (
                    "LangChainProject1/simple_chatbot_v2.py\n"
                    "LangChainProject1/requirements.txt\n"
                    "Chatbot.png"
                ),
                "information_needed": (
                    "Fill in here if you want to add:\n"
                    "- the exact assignment instructions\n"
                    "- a better one-sentence summary in your own voice\n"
                    "- a GitHub link or demo link if you have one"
                ),
                "technologies": "Python, Gemini API, LangChain, python-dotenv",
                "featured": True,
                "image": base_dir / "Chatbot.png",
                "assets": [
                    {
                        "title": "Chatbot Interface Screenshot",
                        "asset_type": "image",
                        "path": base_dir / "Chatbot.png",
                        "caption": "Screenshot used to represent the chatbot project in the portfolio.",
                    },
                ],
            },
            {
                "title": "LangChain Agent Project",
                "description": (
                    "A LangChain agent project that connects a Gemini model to a Python script for structured AI responses."
                ),
                "business_problem": (
                    "Developers need a repeatable way to integrate large language models into Python applications, "
                    "so this project explores how an agent framework can organize that interaction."
                ),
                "overview": (
                    "This project focuses on the agent side of the chatbot work. It uses LangChain's agent creation "
                    "tools with Gemini to define a system prompt, send messages, and receive responses in a more "
                    "structured framework than a plain script alone."
                ),
                "key_features": (
                    "LangChain agent setup\n"
                    "Gemini model integration\n"
                    "System prompt configuration\n"
                    "Prompt invocation through a structured messages format"
                ),
                "role_contribution": (
                    "I configured the LangChain agent, connected it to the Gemini model, loaded environment variables, "
                    "and tested the prompt-response workflow in Python."
                ),
                "biggest_challenge": (
                    "The biggest challenge was understanding how the agent, model connection, and messages structure "
                    "fit together so the script would return the expected output."
                ),
                "what_learned": (
                    "I learned how agent-based LLM frameworks differ from basic scripting and how prompt structure, "
                    "system instructions, and model setup affect the final response."
                ),
                "included_files": (
                    "LangChainProject1/simple_chatbot_v1.py\n"
                    "LangChainProject1/requirements.txt"
                ),
                "information_needed": (
                    "Fill in here if you want to add:\n"
                    "- why you chose LangChain for this project\n"
                    "- whether you want this page to mention Gemini by name in the title\n"
                    "- a GitHub or demo link"
                ),
                "technologies": "Python, LangChain, Gemini API, python-dotenv",
                "featured": True,
                "image": base_dir / "Langchain.png",
                "assets": [
                    {
                        "title": "LangChain Screenshot",
                        "asset_type": "image",
                        "path": base_dir / "Langchain.png",
                        "caption": "Screenshot used to represent the LangChain agent project.",
                    },
                ],
            },
            {
                "title": "n8n Agent Workflow Project",
                "description": (
                    "A multi-step n8n agent workflow that processes service requests, pricing, scheduling, and customer communication."
                ),
                "business_problem": (
                    "Service businesses often lose time manually reviewing requests, pricing jobs, offering appointment windows, "
                    "and writing customer emails, so this project automates that workflow."
                ),
                "overview": (
                    "This project uses several connected n8n workflows to turn incoming customer information into structured job data, "
                    "pricing estimates, appointment options, and a final email response. An orchestrator coordinates the other agents "
                    "so the process behaves like one automated system."
                ),
                "key_features": (
                    "Webhook-based workflow orchestration\n"
                    "Separate intake, pricing, scheduling, and communications agents\n"
                    "Gmail response delivery\n"
                    "JavaScript data transformation inside n8n\n"
                    "Gemini-based structured extraction and message generation"
                ),
                "role_contribution": (
                    "I designed the workflow structure, configured the agent JSON files, wrote the logic in the code nodes, "
                    "and connected the automation pieces into a working pipeline."
                ),
                "biggest_challenge": (
                    "The biggest challenge was coordinating data between multiple agents while keeping the JSON outputs clean enough "
                    "for the next step in the workflow to use reliably."
                ),
                "what_learned": (
                    "I learned how to orchestrate multiple automation agents, pass structured data across workflow steps, "
                    "and combine LLM output with deterministic business rules."
                ),
                "included_files": (
                    "SheetToGmail-N8N/Agent- Orchestrator.json\n"
                    "SheetToGmail-N8N/Agent- Intake.json\n"
                    "SheetToGmail-N8N/Agent- Pricing.json\n"
                    "SheetToGmail-N8N/Agent- Scheduling.json\n"
                    "SheetToGmail-N8N/Agent- Comms.json"
                ),
                "information_needed": (
                    "Fill in here if you want to add:\n"
                    "- a screenshot of the n8n canvas\n"
                    "- the original trigger source: Google Sheet, form, or other input\n"
                    "- a demo or repository link if available"
                ),
                "technologies": "n8n, Google Gemini, Gmail, JavaScript, Webhooks, JSON",
                "featured": True,
                "image": base_dir / "n8n1.png",
                "assets": [
                    {
                        "title": "n8n Workflow Overview",
                        "asset_type": "image",
                        "path": base_dir / "n8n1.png",
                        "caption": "Main n8n workflow canvas showing the automation structure.",
                    },
                    {
                        "title": "n8n Intake Flow",
                        "asset_type": "image",
                        "path": base_dir / "n8n2.png",
                        "caption": "Workflow step for collecting and organizing service request details.",
                    },
                    {
                        "title": "n8n Pricing Logic",
                        "asset_type": "image",
                        "path": base_dir / "n8n3.png",
                        "caption": "Automation step for transforming request data into a pricing response.",
                    },
                    {
                        "title": "n8n Scheduling Flow",
                        "asset_type": "image",
                        "path": base_dir / "n8n4.png",
                        "caption": "Scheduling logic used to prepare appointment options.",
                    },
                    {
                        "title": "n8n Gmail Response",
                        "asset_type": "image",
                        "path": base_dir / "n8n5.png",
                        "caption": "Final communication workflow for sending the customer response.",
                    },
                ],
            },
            {
                "title": "Google AI Studio Media Project",
                "description": (
                    "A media generation project using Google AI tools to create images and a cinematic video output."
                ),
                "business_problem": (
                    "Content creation can be time-intensive, so this project explores how AI-generated media can speed up concept development "
                    "and visual storytelling."
                ),
                "overview": (
                    "This project presents AI-generated visual media, including multiple still images and a short cinematic video. "
                    "It highlights how prompt-based generation can be used to create creative assets for storytelling, branding, or concept work."
                ),
                "key_features": (
                    "AI-generated still images\n"
                    "AI-generated cinematic video clip\n"
                    "Prompt-driven content creation\n"
                    "Portfolio-ready visual presentation"
                ),
                "role_contribution": (
                    "I created the prompts, generated the media outputs, selected the strongest assets, "
                    "and organized them for presentation in the portfolio."
                ),
                "biggest_challenge": (
                    "The biggest challenge was refining outputs until the visuals felt polished and consistent enough to present as a complete project."
                ),
                "what_learned": (
                    "I learned how prompt wording influences visual style, how to evaluate generated media critically, "
                    "and how to present AI-generated outputs as part of a finished project."
                ),
                "included_files": (
                    "Video Generation/A_breathtaking_cinematic_202602171502_dqslc.mp4\n"
                    "Video Generation/Gemini_Generated_Image_a8o41a8o41a8o41a.png\n"
                    "Video Generation/Gemini_Generated_Image_p0qrm7p0qrm7p0qr.png\n"
                    "Video Generation/Gemini_Generated_Image_yz4a49yz4a49yz4a.png"
                ),
                "information_needed": (
                    "Fill in here if you want to add:\n"
                    "- the exact prompt used\n"
                    "- whether this was created directly in Google AI Studio or with a connected Google model workflow\n"
                    "- a class or assignment goal for the media project"
                ),
                "technologies": "Google AI Studio, Gemini, AI Image Generation, AI Video Generation, Prompt Engineering",
                "featured": True,
                "image": base_dir / "Video Generation" / "Gemini_Generated_Image_a8o41a8o41a8o41a.png",
                "assets": [
                    {
                        "title": "Cinematic Video Output",
                        "asset_type": "video",
                        "path": base_dir / "Video Generation" / "A_breathtaking_cinematic_202602171502_dqslc.mp4",
                        "caption": "Generated cinematic video clip included with the project.",
                    },
                    {
                        "title": "Generated Image 1",
                        "asset_type": "image",
                        "path": base_dir / "Video Generation" / "Gemini_Generated_Image_a8o41a8o41a8o41a.png",
                        "caption": "AI-generated still image from the media project.",
                    },
                    {
                        "title": "Generated Image 2",
                        "asset_type": "image",
                        "path": base_dir / "Video Generation" / "Gemini_Generated_Image_p0qrm7p0qrm7p0qr.png",
                        "caption": "AI-generated still image from the media project.",
                    },
                    {
                        "title": "Generated Image 3",
                        "asset_type": "image",
                        "path": base_dir / "Video Generation" / "Gemini_Generated_Image_yz4a49yz4a49yz4a.png",
                        "caption": "AI-generated still image from the media project.",
                    },
                ],
            },
            {
                "title": "Machine Learning Project (scikit-learn)",
                "description": (
                    "A scikit-learn project collection that uses classification and regression models to analyze real datasets."
                ),
                "business_problem": (
                    "Data is most useful when it can support prediction and pattern recognition, so this project explores how machine learning "
                    "can be used to classify data and estimate outcomes from structured datasets."
                ),
                "overview": (
                    "This project groups together several machine learning practice scripts using datasets "
                    "such as digits, iris, California housing, diabetes, and auto MPG. The work demonstrates "
                    "core workflows like loading datasets, splitting train and test data, fitting models, "
                    "evaluating predictions, and visualizing results."
                ),
                "key_features": (
                    "Classification with digits and iris datasets\n"
                    "Regression with California housing and auto MPG data\n"
                    "Confusion matrices and scatterplot visualizations\n"
                    "Train/test split and model evaluation"
                ),
                "role_contribution": (
                    "I wrote the Python scripts, loaded the datasets, trained the models, created the plots, "
                    "and reviewed the model outputs to compare predicted and expected results."
                ),
                "biggest_challenge": (
                    "The biggest challenge was understanding which model and visualization best matched each dataset, "
                    "especially when moving between classification and regression tasks."
                ),
                "what_learned": (
                    "I learned how to use scikit-learn for different supervised learning problems, how to read confusion matrices, "
                    "and how model evaluation changes depending on the dataset and task."
                ),
                "included_files": (
                    "ml/ml1.py\n"
                    "ml/ml2.py\n"
                    "ml/iris.py\n"
                    "ml/diabetes.py\n"
                    "ml/mpg.py\n"
                    "ml/zipping.py\n"
                    "ml/requirements.txt"
                ),
                "information_needed": (
                    "Fill in here if you want to clarify:\n"
                    "- which dataset or script should be highlighted most\n"
                    "- whether you want to mention final accuracy numbers\n"
                    "- any charts or screenshots you want attached"
                ),
                "technologies": "Python, scikit-learn, pandas, seaborn, matplotlib, datasets",
                "featured": True,
                "image": base_dir / "ML.png",
                "assets": [
                    {
                        "title": "Machine Learning Screenshot",
                        "asset_type": "image",
                        "path": base_dir / "ML.png",
                        "caption": "Screenshot used to represent the machine learning project.",
                    },
                ],
            },
            {
                "title": "Campus SkillSwap Django Project",
                "description": (
                    "A Django web application where users can offer skills, request sessions, and leave reviews "
                    "after completed bookings."
                ),
                "business_problem": (
                    "Students often have useful skills to exchange but no central place to discover one another, "
                    "so this project creates a structured platform for skill-sharing on campus."
                ),
                "overview": (
                    "Campus Skill Swap is a marketplace-style Django app designed to help students share skills "
                    "with one another. Users can list skills, describe services, manage availability, send booking "
                    "requests, and submit reviews after completed sessions."
                ),
                "key_features": (
                    "User-created skill listings\n"
                    "Booking requests between users\n"
                    "Availability and contact preference tracking\n"
                    "Review and rating support\n"
                    "Django templates and database-backed workflows"
                ),
                "role_contribution": (
                    "I built the Django models, forms, views, routes, and templates needed for the marketplace flow, "
                    "including booking requests and review support."
                ),
                "biggest_challenge": (
                    "The biggest challenge was designing the relationships between users, skill listings, reviews, "
                    "and booking requests in a way that supported the full workflow."
                ),
                "what_learned": (
                    "I learned how to structure a multi-model Django application, manage user interactions across views, "
                    "and build a more complete CRUD-based web app."
                ),
                "included_files": (
                    "campus skill swap /manage.py\n"
                    "campus skill swap /campus_skillswap/settings.py\n"
                    "campus skill swap /marketplace/models.py\n"
                    "campus skill swap /marketplace/views.py\n"
                    "campus skill swap /marketplace/forms.py\n"
                    "campus skill swap /marketplace/templates/..."
                ),
                "information_needed": (
                    "Fill in here if available:\n"
                    "- screenshot of the marketplace home page or dashboard\n"
                    "- whether this was an individual or team project\n"
                    "- live deployment link or GitHub repository link"
                ),
                "technologies": "Python, Django, SQLite, HTML, CSS",
                "github_url": "https://github.com/makrieg/skill-swap",
                "featured": True,
                "image": base_dir / "Campus Skill Swap.png",
                "assets": [
                    {
                        "title": "Campus SkillSwap Screenshot",
                        "asset_type": "image",
                        "path": base_dir / "Campus Skill Swap.png",
                        "caption": "Screenshot used to represent the Campus SkillSwap Django project.",
                    },
                ],
            },
        ]

        for index, payload in enumerate(projects, start=1):
            image_path = payload.pop("image", None)
            assets = payload.pop("assets", [])
            payload["order"] = index

            project, _ = Project.objects.update_or_create(
                title=payload["title"],
                defaults=payload,
            )

            if image_path and image_path.exists():
                self._assign_file(project, "image", image_path)
            elif not image_path and project.image:
                project.image.delete(save=False)
                project.image = None
                project.save(update_fields=["image"])

            project.assets.all().delete()
            for asset_index, asset in enumerate(assets, start=1):
                record = ProjectAsset.objects.create(
                    project=project,
                    title=asset["title"],
                    asset_type=asset["asset_type"],
                    caption=asset.get("caption", ""),
                    order=asset_index,
                )
                path = asset.get("path")
                if path and Path(path).exists():
                    self._assign_file(record, "file", Path(path))

            self.stdout.write(self.style.SUCCESS(f"Seeded project: {project.title}"))

    def _assign_file(self, instance, field_name, source_path):
        destination = Path(settings.MEDIA_ROOT) / "projects" / "assets"
        destination.mkdir(parents=True, exist_ok=True)
        copied_path = destination / source_path.name
        shutil.copy2(source_path, copied_path)

        with copied_path.open("rb") as handle:
            getattr(instance, field_name).save(source_path.name, File(handle), save=False)

        instance.save()
