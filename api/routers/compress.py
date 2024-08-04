from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from queries.compress_file import compress

router = APIRouter()


@router.post("/compress/")
async def compress_file(file: UploadFile = File(...)):
    content = await file.read()
    results = compress(content)
    return JSONResponse(results)
