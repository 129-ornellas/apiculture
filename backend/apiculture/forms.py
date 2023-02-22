from pydantic import BaseModel, validator


class GetForm(BaseModel):
    url: str

    @validator("url")
    def valid_url(cls, value):
        if not value:
            raise ValueError("URL is required")
        cleaned_url = value.strip()
        if not cleaned_url.startswith("http://") and not cleaned_url.startswith("https://"):
            cleaned_url = f"http://{cleaned_url}"
        return cleaned_url