from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from .forms import ResumeUploadForm
from .utils import extract_text_from_pdf, calculate_match_score


def upload_resume(request):
    """Home page - resume upload form batave che."""
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()  # pehla save kare che jethi file disk par aavi jay

            # PDF ma thi text kadho
            resume_text = extract_text_from_pdf(resume.resume_file.path)

            # Score calculate karo
            score, matched, missing = calculate_match_score(
                resume_text, resume.job_description
            )

            # Result database ma save karo
            resume.match_score = score
            resume.matched_keywords = ', '.join(sorted(matched))
            resume.missing_keywords = ', '.join(sorted(missing))
            resume.save()

            return redirect('result', pk=resume.pk)
    else:
        form = ResumeUploadForm()

    return render(request, 'checker/upload.html', {'form': form})


def result(request, pk):
    """Result page - score, matched ane missing keywords batave che."""
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'checker/result.html', {'resume': resume})


def history(request):
    """Aa pehla thayela badha resume checks ni list."""
    resumes = Resume.objects.all().order_by('-uploaded_at')
    return render(request, 'checker/history.html', {'resumes': resumes})
