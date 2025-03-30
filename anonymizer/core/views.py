from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, HttpResponse
from django.conf import settings
import os
from .utils import anonymize_csv

def upload_file(request):
    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_file = request.FILES['file']
        
        # media 폴더에 파일 저장
        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        # 비식별화 수행
        anonymized_file_path, preview_html = anonymize_csv(file_path)

        # 비식별화된 파일의 이름 추출
        anonymized_filename = os.path.basename(anonymized_file_path)

        return render(request, 'core/file_uploaded.html', {
            'uploaded_file_name': filename,  # 원본 파일명
            'anonymized_file_name': anonymized_filename,  # 비식별화된 파일명
            'preview': preview_html  # 미리보기 데이터
        })

    return render(request, 'core/upload.html')


def download_file(request, filename):
    """파일 다운로드 뷰"""
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    else:
        return HttpResponse("파일을 찾을 수 없습니다.", status=404)
