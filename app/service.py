from imageai.Prediction import ImagePrediction
import os


class ProcessImageService:
    def process(self, params):

        # execution_path = os.getcwd()
        prediction = ImagePrediction()
        prediction.setModelTypeAsResNet()
        prediction.setModelPath(
            "../aimodel/resnet50_weights_tf_dim_ordering_tf_kernels.h5")
        prediction.loadModel()
        predictions, percentage_probabilities = prediction.predictImage(
            "../images/sample.jpeg", result_count=1)

        # for index in range(len(predictions)):
        # print(predictions[index], " : ", percentage_probabilities[index])

        return {"object": predictions[0], "probability": percentage_probabilities[0]}
