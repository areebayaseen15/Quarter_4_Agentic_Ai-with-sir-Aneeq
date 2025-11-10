

# Advanced Handoff customization

from tool import Agent , handoff

refund_agent = Agent(
    name ="Refund Agent",
    instructions ="You handle all refund-related processes."
)


# Customize handoff to refund Agent
customize_handoff = handoff(
    agent = refund_agent,
    tool_name_override = "cutom_refund_handoff"
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent should handle the user's request."
    handoffs = [customize_handoff]
)  