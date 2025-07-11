from faststream import Context, FastStream, apply_types
from faststream.confluent import KafkaBroker
from faststream.confluent.annotations import ContextRepo, KafkaMessage

broker = KafkaBroker("localhost:9092")
app = FastStream(broker)


@broker.subscriber("test-topic")
async def handle(
    msg: str,
    message: KafkaMessage,
    context: ContextRepo,
):
    with context.scope("correlation_id", message.correlation_id):
        call()


@apply_types
def call(
    message: KafkaMessage,
    correlation_id: str = Context(),
):
    assert correlation_id == message.correlation_id
