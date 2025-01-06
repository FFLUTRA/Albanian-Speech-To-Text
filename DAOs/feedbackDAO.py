from abc import ABC, abstractmethod

class FeedbackDAO(ABC):
    
    @abstractmethod
    def submit_feedback(self, feedback) -> None:
        pass

    @abstractmethod
    def get_feedbacks_by_user_id(self, feedback) -> list:
        pass

    @abstractmethod
    def update_feedback(self, feedback_id, feedback_data) -> None:
        pass

    @abstractmethod
    def delete_feedback(self, feedback_id) -> None:
        pass