# Task Recommendation System

## Overview

The Task Recommendation System uses a Nearest Neighbors algorithm to recommend tasks based on a specified time input. By analyzing task start times, durations, and completion statuses, the system identifies tasks that are similar to the given time.

## Installation

To run the Task Recommendation System, you'll need Python and the following libraries:

- `pandas`
- `numpy`
- `scikit-learn`

You can install these dependencies using `pip`. Run the following command in your terminal:

```bash
pip install pandas numpy scikit-learn
```

## Running the Script

1. **Download the Script**: Ensure you have the script file, e.g., `task_recommendation.py`.

2. **Execute the Script**: Run the script using Python:

   ```bash
   python task_recommendation.py
   ```

   You can also test the recommendation system with a specific time. For example, to get recommendations for 5:00 PM:

   ```python
   print("Task at 5:00 PM:", task_recommendation_system('05:00 PM'))
   ```

## Assumptions

- **Time Format**: The time format provided should be `'%I:%M %p'` (e.g., `'05:00 PM'`).
- **Same Day Assumption**: The script assumes that all tasks are scheduled within the same day and does not handle multi-day tasks.
- **Feature Representation**: The features used include start time in minutes, duration, and completion status. Overlaps or breaks between tasks are not considered.

## Recommendation Algorithm

The recommendation system uses the Nearest Neighbors algorithm from the `scikit-learn` library. Here’s how it works:

1. **Feature Extraction**: Converts start times to minutes and encodes the completion status as binary values (1 for completed, 0 for not completed). Calculates task durations in minutes.
2. **Model Training**: The Nearest Neighbors model is trained on the extracted features.
3. **Task Recommendation**: For a given time, the model finds the nearest neighbors based on features and recommends tasks similar to the provided time.

## Code Description

1. **Sample Dataset**: Includes tasks with attributes like start time, end time, and completion status.
2. **Data Preparation**: 
   - Converts time to `datetime` objects for manipulation.
   - Calculates the duration of each task.
   - Encodes the completion status as binary values.
   - Converts start times to minutes for feature representation.
3. **Model Training**: Uses `NearestNeighbors` from `scikit-learn` to fit the model.
4. **Recommendation Function**: Recommends tasks based on the provided time.

## Example Usage

```python
print("Task at 5:00 PM:", task_recommendation_system('05:00 PM'))
```

## Testing and Validation

### Sample Dataset

The script includes a sample dataset with tasks to demonstrate functionality.

### Testing Function

To validate the recommendations, you can use a test function. Modify or create test cases based on real-world scenarios to ensure accuracy.

### Validation Metrics

Consider using metrics like precision and recall to evaluate the accuracy of recommendations, based on actual or expected results.

## Areas for Potential Improvement

1. **Handling Multi-Day Tasks**: Extend functionality to handle tasks spanning multiple days.
2. **Feature Enhancement**: Add more features (e.g., task priority) for better recommendations.
3. **Dynamic Data Integration**: Integrate with real-time data sources for up-to-date recommendations.
4. **User Feedback**: Implement feedback mechanisms to refine recommendations based on user preferences.
5. **Scalability**: Optimize the system to handle larger datasets efficiently.
