import os

from openai import OpenAI
from dotenv import load_dotenv

from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def openai_runnable(input):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "system",
            "content": [
                {
                "type": "text",
                "text": "You are ChatGPT, a professional sommelier who has gone through a rigorous training process step by step, driven by a deep curiosity about wine. You possess a keen sense of smell, a keen sense of exploration, and an awareness of the many details in wine.\r\n\r\nYour task is to accurately identify the wine in question and recommend an appropriate food pairing based on the provided wine reviews in triple quotes.\r\n\r\n### Task Instructions:\r\n\r\n**Pairing Recommendation**:\r\n- Recommend an appropriate food pairing that complements the identified wine.\r\n- Take into account the wine’s characteristics (e.g., a full-bodied red wine with high tannins pairs well with rich, fatty meats).\r\n- Suggest alternative pairings such as cheese, desserts, or even specific dishes that enhance the wine's profile.\r\n"
                }
            ]
            },
            {
            "role": "user",
            "content": [
                {
                "type": "image_url",
                "image_url": {
                    "url": "https://images.vivino.com/thumbs/tiV02HEuQPaNoSRcWA3r2g_pb_x600.png"
                }
                },
                {
                "type": "text",
                "text": input
                }
            ]
            },
            {
            "role": "assistant",
            "content": [
                {
                "type": "text",
                "text": "이 와인은 아마로네 델라 발폴리첼라(Amarone della Valpolicella)입니다. 아마로네는 이탈리아 베네토 지역의 레드 와인으로, 말린 포도로 만들어져 풍부하고 강렬한 맛을 자랑합니다. 주요 특징으로는 높은 알코올 도수, 부드러운 탄닌, 블랙 체리, 자두 등의 과일 향과 함께 초콜릿, 커피, 허브의 복합적인 풍미가 있습니다.\n\n아마로네와 어울리는 음식 추천:\n\n1. **붉은 고기**: 특히 소고기 스테이크, 양고기 스튜, 육류가 풍부한 요리와 잘 어울립니다.\n2. **야생 게임 고기**: 사냥으로 잡은 고기 요리, 예를 들어 야생 멧돼지 스튜나 사슴고기 요리도 잘 맞습니다.\n3. **치즈**: 강렬한 치즈, 특히 파르미지아노 레지아노, 고르곤졸라 같은 블루 치즈와 페코리노 같은 강한 치즈가 좋습니다.\n4"
                }
            ]
            },
            {
            "role": "assistant",
            "content": [
                {
                "type": "text",
                "text": ". **파스타**: 트러플 소스를 곁들인 파스타, 라구 소스가 들어간 파스타와도 훌륭한 조화를 이룹니다.\n5. **리조또**: 특히 버섯 리조또나 트러플 리조또와 잘 어울립니다.\n6. **다크 초콜릿 디저트**: 다크 초콜릿을 사용한 디저트, 예를 들어 다크 초콜릿 무스나 초콜릿 트러플과도 잘 어울립니다.\n\n이러한 음식들은 아마로네의 풍부한 맛과 복합적인 향을 잘 보완해주며, 와인의 특성을 더욱 돋보이게 해줄 것입니다."
                }
            ]
            }
        ],
        temperature=0,
        max_tokens=4095,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )

    return "".join([x.message.content for x in response.choices])

if __name__ == '__main__':
    

    runnable = RunnableLambda(openai_runnable)

    # Async variant:
    # await runnable.ainvoke(5)
    chain = runnable | StrOutputParser()

    response = chain.invoke("이 와인과 어울리는 음식을 알려줘")