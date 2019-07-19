### OncoNetExplainer: Explainable Predictions of Cancer Types Based on Gene Expression Data
Code and supplementary materials for our paper titled "Explainable Prediction of Cancer Types Based on Gene Expression Data" submitted to The 19th annual IEEE International Conference on Bioinformatics and Bioengineering(BIBE 2019) to be held in Athens, Greece. 

#### Methods
In this paper, we collect genomics data about 9,074 cancer patients covering 33 different cancer types from The Cancer Genome Atlas(TCGA) and train a CNN and VGG16 networks using guided-gradient class activation map(GradCAM). 

Then we identify most significant biomarkers and rank top genes across different cancer types based on mean absolute impact. 
Both models show high confidence at predicting different cancer types correctly at least 94% of the cases. 

To provide comparison with baselines, we further identify top genes for each cancer type and cancer specific driver genes using gradient boosted trees and SHapley Additive exPlanations(SHAP), which are further validated with the annotation from the TumorPortal.

#### Data collections
Gene expression about 33 different tumor types have been downloaded from The Cancer Genome Atlas(TCGA) portal covering 9,074 samples. See [here](https://github.com/rezacsedu/XAI_Cancer_Pred/tree/master/Data) for more details about the data. 

#### Data availability
The preprocessed data can be downloaded from [here](https://data.fit.fraunhofer.de/index.php/s/4yXxzSoRgnI18XY) with the password of '123' (without quote). 

#### A quick instructions on using GradCAM and ranking important biomarkers
A quick example on a small dataset can be performed as follows: 
* $ cd GradCAM_FI
* $ python3 load_data.py (make sure that the data in CSV format in the 'data' folder)
* $ python3 model.py
* $ python3 grad_cam.py

#### Examples of explanation using CNN and SHAP
CNN and VGG16 networks using guided-gradient class activation map~(GradCAM). Further, we generated heat-maps for all the classes based on GradCAM to identify the most significant biomarkers and compute the feature importance in terms of mean absolute impact~(MAI) to rank top genes across cancer types. 

The following figures shows the generated heat-map examples for selected cancer types. Each column represents the result from one  fold. Rows represent the heat-maps of BRCA, KIRC, COAD, LUAD, and PRAD cancer types (from top-down):

<img src="https://github.com/rezacsedu/XAI_Cancer_Pred/blob/master/images/grid.png" width="500" height="500">

The following figures shows common driver genes across 33 cancer types:

![](images/common.png)

Nevertheless, a Python notebook will be added soon to show the steps more transparently. 

#### Examples of explanation using SHAP and Gradient Boosted Trees
Refer the [Python notebook](https://github.com/rezacsedu/XAI_Cancer_Pred/blob/master/Notebooks/GeneExpression_Classification_SHAP_XBoost.ipynb) to get an idea how to use SHAP and gradient boosted trees to generate feature importance and explanation about the prediction. 

First, we process the data (see the Python notebook). Then we train a GBT algorithm. Then SHAP explainer is used to provide explanation. The following figure shows clinical features contribution pushing the prediction higher in red and pushing the prediction lower are in blue: 

![](images/shap.png)

The following figure shows clinical features contribution in which features are ordered on the y-axis in a descending order according to their MAI~(each dot represents SHAP value for a specific feature):

![](images/fi.png)

### Citation request
If you use the code of this repository in your research, please consider citing the folowing papers:

    @inproceedings{karim2019XAI,
        title={Explainable Prediction of Cancer Types Based on Gene Expression Data},
        author={Karim, Md Rezaul and Beyan Deniz and Decker, Stefan},
        booktitle={The 19th annual IEEE International Conference on Bioinformatics and Bioengineering (BIBE 2019)},
        year={2019}
    }

### Contributing
For any questions, feel free to open an issue or contact at rezaul.karim@rwth-aachen.de
