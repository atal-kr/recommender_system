from recommender_service.settings import JSON_SETTING
RECOMMENDATION_ENGINE = JSON_SETTING['RECOMMENDATION_ENGINE']
CONTENT_SEEN_LIMIT=RECOMMENDATION_ENGINE["CONTENT_SEEN_LIMIT"]
MOU=RECOMMENDATION_ENGINE["MOU"]
BUCKET = RECOMMENDATION_ENGINE["BUCKET"]
REC_MINLIMIT = RECOMMENDATION_ENGINE["RECOMMENDATION_MINLIMIT"]
REC_MAXLIMIT = RECOMMENDATION_ENGINE["RECOMMENDATION_MAXLIMIT"]
DECIDER_ENABLE = RECOMMENDATION_ENGINE["DECIDER_ENABLE"]
LIVE_LIMIT = RECOMMENDATION_ENGINE['CIRCLE_LIVE_LIMIT']
NO_OF_DAYS = RECOMMENDATION_ENGINE['NO_OF_DAYS_NOTIFICATION']
NOD_RECENCY = RECOMMENDATION_ENGINE["NO_OF_DAYS_RECENCY"]
RMF =RECOMMENDATION_ENGINE['RECENCY_MOU_FACTOR']
RCF =RECOMMENDATION_ENGINE['RECENCY_CONFIDENCE_FACTOR']
COLADSTART_AB_ENABLE = RECOMMENDATION_ENGINE['COLADSTART_AB_ENABLE']







