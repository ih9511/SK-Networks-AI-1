from pydantic import BaseModel


class OpenAIPaperSimilarityAnalysisResponseForm(BaseModel):
    similarity: float
    paperTitle: str

    @classmethod
    def fromOpenAIPaperSimilarityAnalysis(cls, indexList, distanceList, textList):
        resultList = []

        for index, faissIndex in enumerate(indexList):
            similarity = 1 - distanceList[index]
            resultList.append(cls(similarity=round(similarity, 4), paperTitle=textList[faissIndex]))

        return resultList