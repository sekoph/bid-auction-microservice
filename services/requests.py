import httpx
import py_eureka_client.eureka_client as eureka_client
from typing import Dict, Optional, Any

async def get_service_url(service_name):
    client = eureka_client.get_client()
    app = client.applications.get_application(service_name)
    up_instances = app.up_instances
    inst = up_instances[0]
    print("this is the instance",inst)
    if inst:
        print(f"http://{inst.ipAddr}:{inst.port.port}")
        return f"http://{inst.ipAddr}:{inst.port.port}"
    return None



async def fetch_data(url: str, service_name: str, method: str, headers: Optional[Dict[str, str]] = None, payload: Optional[Dict[str, Any]] = None):
    service_url = await get_service_url(service_name)
    if not service_url:
        return {"error" : f"{service_name} not found"}
    
    # form the url
    url = f"{service_url}/{url}"
    async with httpx.AsyncClient() as client:
        try:
            if method.lower() == "get":
                response = await client.get(url, headers=headers)
            elif method.lower() == "put":
                response = await client.put(url, headers=headers, json=payload)
            elif method.lower() == "post":
                response = await client.post(url, headers=headers, json=payload)
            elif method.lower() == "delete":
                response = await client.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported http method: {method}")
            response.raise_for_status()  # Raise error if the request fails
            return response.json()
        
        except httpx.HTTPStatusError as e:
            print(f"HTTP error: {e.response.status_code} - {e.response.text}")
            return {"error": str(e)}
        
        except Exception as e:
            print(f"request failed: {e}")
            return {"error": str(e)}