from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
# some fastapi imports

app = FastAPI() # initalize fastapi

app.mount("/s1/characters", StaticFiles(directory="s1/characters"))
app.mount("/s2/characters", StaticFiles(directory="s2/characters"))
app.mount("/s1/episodes", StaticFiles(directory="s1/episodes"))
app.mount("/s2/episodes", StaticFiles(directory="s2/episodes"))
app.mount("/s3/episodes", StaticFiles(directory="s2/episodes-s3"))
# season 3 ep's are in s2 because they're almost the same
@app.get("/")
async def s1():
      return {"Welcome to SG-API":"You can access JSON content files by path /s1/() or /s2/()"}
# this pops up when youre at root level

# below you enter the http exception handling, just returns JSON string for 404, 400, 500, 502, 403
@app.exception_handler(404)
async def not_found(request: Request, exc: HTTPException):
      return JSONResponse(
              status_code=404,
              content={"Error": "404 Not Found", "Info": "Either the incorrect path was entered, the incorrect file extension was entered, or a filesystem issue. if the issue is not because of your system/instance, make an issue in the GitHub."}
              )

@app.exception_handler(400)
async def bad(request: Request, exc: HTTPException):
      return JSONResponse(
              status_code=400,
              content={"Error": "400 Bad Request", "Info": "Client caused an error faulting the server in processing the request."}
              )
@app.exception_handler(500)
async def bad(request: Request, exc: HTTPException):
      return JSONResponse(
              status_code=500,
              content={"Error": "500 Internal Server Error", "Info": "Someting went wrong internally, contact the administrator"}
              )

@app.exception_handler(502)
async def bad(request: Request, exc: HTTPException):
      return JSONResponse(
              status_code=502,
              content={"Error": "502 Bad Gateway", "Info": "The weakest link in the connection chain (the last one) failed. Contact the administrator."}
              )

@app.exception_handler(403)
async def bad(request: Request, exc: HTTPException):
      return JSONResponse(
              status_code=403,
              content={"Error": "403 Forbidden", "Info": "You do not have permission to access this endpoint. GET OUT!"}
              )
# here below, defines uvicorn and its settings to run the api
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2456, reload=True) # the port here does not need to be edited to modify your server port

# to run, type "uvicorn main:app --reload --port {YOUR_PORT}"
