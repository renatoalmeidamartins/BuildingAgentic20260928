from bedrock_agentcore.memory import MemoryClient

client = MemoryClient(region_name="us-east-1")
memory_id = "test_memory-41Qu1lDe5S"
actor_id = "user-123"
session_id = "sess_id"

client.create_event(         
    memory_id = memory_id,  # yours will have a different unique name after running create-memory.py, check it.
    actor_id = actor_id,
    session_id = session_id,
    messages=[ 
        ("I'm having trouble with my order #12345", "USER"), 
        ("I'm sorry to hear that. Let me look up your order.", "ASSISTANT"), ("lookup_order(order_id='12345')", "TOOL")
    ]
)


events = client.list_events(
	memory_id = memory_id,
	actor_id = actor_id,
	session_id = session_id)
print (events)



