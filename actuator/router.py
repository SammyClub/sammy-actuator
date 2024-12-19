from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from anthropic.types.beta import BetaMessageParam, BetaToolResultBlockParam
from actuator.tools import (
    ComputerTool,
    ToolCollection,
)

router = APIRouter()


class ActuatorRequest(BaseModel):
    messages: List[BetaMessageParam]
    initial: bool = False


class ActuatorResponse(BaseModel):
    messages: List[BetaMessageParam]
    tool_results: Optional[List[BetaToolResultBlockParam]] = None


@router.post("/actuate", response_model=ActuatorResponse)
async def actuate_response(request: ActuatorRequest):
    try:
        tools = ToolCollection(ComputerTool(selected_screen=0))

        # If initial and only one user message (no conversation_id), run screenshot logic
        if request.initial and len(request.messages) == 1:
            request.messages = await perform_screenshot(tools, request.messages)
            return ActuatorResponse(messages=request.messages, tool_results=[])

        # Otherwise, actuate any tool requests in the last assistant message.
        last_assistant = next(
            (m for m in reversed(request.messages) if m["role"] == "assistant"), None
        )
        if not last_assistant:
            # No assistant message with tools to run
            return ActuatorResponse(messages=request.messages, tool_results=[])

        tool_uses = [c for c in last_assistant["content"] if c["type"] == "tool_use"]
        all_tool_results = []
        for tool_use in tool_uses:
            result = await tools.run(
                name=tool_use["name"], tool_input=tool_use["input"]
            )
            tool_result_block = {
                "type": "tool_result",
                "tool_use_id": tool_use["id"],
                "is_error": bool(result.error),
                "content": result.to_api_content(),
            }
            all_tool_results.append(tool_result_block)
            request.messages.append({"role": "user", "content": [tool_result_block]})

        return ActuatorResponse(
            messages=request.messages, tool_results=all_tool_results
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def perform_screenshot(
    tools: ToolCollection, messages: List[BetaMessageParam]
) -> List[BetaMessageParam]:
    messages.append(
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "Let me take a screenshot to see the current state.",
                },
                {
                    "type": "tool_use",
                    "id": "screenshot_request",
                    "name": "computer",
                    "input": {"action": "screenshot"},
                },
            ],
        }
    )
    screenshot_result = await tools.run(
        name="computer", tool_input={"action": "screenshot"}
    )
    messages.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": "screenshot_request",
                    "is_error": False,
                    "content": screenshot_result.to_api_content(),
                }
            ],
        }
    )
    return messages
