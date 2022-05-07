from bs4 import BeautifulSoup
import requests
import reviewtracker.errors as errors

class ReviewTrackerParser():
    def parse_url(url: str) -> list:
        """ Parse url """
        r = requests.get(url)
        bs = BeautifulSoup(r.content, 'html.parser')

        # main review div html element
        mainReviewsDiv = bs.select('.mainReviews')

        if len(mainReviewsDiv) == 0:
            raise errors.ReviewsError(f'Could not find any reviews for {url}')

        reviews = []
        for i, div in enumerate(mainReviewsDiv):
            # handle each html element and build out a review object
            authorDiv = div.select_one('.consumerName')
            if not authorDiv:
                raise errors.ReviewsError('Missing author name div content')

            dateDiv = div.select_one('.consumerReviewDate')
            if not dateDiv:
                raise errors.ReviewsError('Missing review date div content')

            titleDiv = div.select_one('.reviewTitle')
            if not titleDiv:
                raise errors.ReviewsError('Missing review title div content')

            contentDiv = div.select_one('.reviewText')
            if not contentDiv:
                raise errors.ReviewsError('Missing review content div content')

            numStarsDiv = div.select_one('.numRec')
            if not numStarsDiv:
                raise errors.ReviewsError('Missing number of stars div content')

            loanType = div.select_one('.loanType')
            if not loanType:
                raise errors.ReviewsError('Missing review loan type div content')

            reviews.append({
                'title': titleDiv.text.strip(),
                'content': contentDiv.text.strip(),
                'author': authorDiv.text.strip(),
                'loan_type': loanType.text.strip(),
                'stars': numStarsDiv.text.strip().replace('(', '').replace(')', ' '),
                'date': dateDiv.text.strip(),
            })

        if len(reviews) == 0:
            raise errors.ReviewsError(f'Could not find any reviews for {url}')

        return reviews
