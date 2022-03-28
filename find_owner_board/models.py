from django.conf import settings
from django.db import models

from accounts.models import User
from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.size
    limit_mb = 3
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("이미지의 최대 크기는 %s MB 입니다." % limit_mb)


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# 주인찾습니다 게시판
class FindOwnerBoard(TimestampedModel):
    find_board_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, db_index=True)
    status = models.CharField(max_length=20, choices=(
        ("찾는중", "찾는중"),
        ("찾았어요", "찾았어요"),
    ), default="찾는중", db_index=True)
    content = models.TextField()
    animal_type = models.CharField(max_length=10, choices=(
        ("강아지", "강아지"),
        ("고양이", "고양이"),
    ), default="강아지")

    dog_breed = models.CharField(max_length=30, choices=(
        ("전체", "전체"),
        ("기타", "기타"),
        ("믹스견", "믹스견"),
        ("모르겠어요", "모르겠어요"),
        ("골든리트리버", "골든리트리버"),
        ("래브라도 리트리버", "래브라도 리트리버"),
        ("그레이 하운드", "그레이 하운드"),
        ("그레이트 피레니즈", "그레이트 피레니즈"),
        ("아프간 하운드", "아프간 하운드"),
        ("닥스훈트", "닥스훈트"),
        ("달마시안", "달마시안"),
        ("도베르만", "도베르만"),
        ("로트와일러", "로트와일러"),
        ("셰퍼드", "셰퍼드"),
        ("말라뮤트", "말라뮤트"),
        ("말티즈", "말티즈"),
        ("푸들", "푸들"),
        ("스피츠", "스피츠"),
        ("볼 테리어", "볼 테리어"),
        ("보스턴 테리어", "보스턴 테리어"),
        ("슈나우져", "슈나우져"),
        ("보더콜리", "보더콜리"),
        ("불독", "불독"),
        ("비글", "비글"),
        ("비숑 프리제", "비숑 프리제"),
        ("빠삐용", "빠삐용"),
        ("사모예드", "사모예드"),
        ("삽살개", "삽살개"),
        ("샤페이", "샤페이"),
        ("시베리안 허스키", "시베리안 허스키"),
        ("시츄", "시츄"),
        ("시바", "시바"),
        ("코카 스파니엘", "코카 스파니엘"),
        ("오브차카", "오브차카"),
        ("요크셔테리어", "요크셔테리어"),
        ("치와와", "치와와"),
        ("차우차우", "차우차우"),
        ("웰시코기", "웰시코기"),
        ("페키니즈", "페키니즈"),
        ("진도개", "진도개"),
        ("포메라니안", "포메라니안"),
        ("퍼그", "퍼그"),
    ), default="전체")

    cat_breed = models.CharField(max_length=30, choices=(
        ("전체", "전체"),
        ("기타", "기타"),
        ("믹스묘", "믹스묘"),
        ("모르겠어요", "모르겠어요"),
        ("샴", "샴"),
        ("러시안 블루", "러시안 블루"),
        ("먼치킨", "먼치킨"),
        ("발레니즈", "발레니즈"),
        ("터키쉬 앙고라", "터키쉬 앙고라"),
        ("노르웨이 숲", "노르웨이 숲"),
        ("메인쿤", "메인쿤"),
        ("버만", "버만"),
        ("벵갈", "벵갈"),
        ("스핑크스", "스핑크스"),
        ("스코티쉬 폴드", "스코티쉬 폴드"),
        ("시베리안", "시베리안"),
        ("페르시안", "페르시안"),
        ("코리안 숏헤어", "코리안 숏헤어"),
        ("아메리칸 숏헤어", "아메리칸 숏헤어"),
        ("히말라얀", "히말라얀"),
        ("한국 고양이", "한국 고양이"),
    ), default="전체")

    size = models.CharField(max_length=10, choices=(
        ("소형", "소형"),
        ("중형", "중형"),
        ("대형", "대형"),
    ), default="소형")

    sex = models.CharField(max_length=10, choices=(
        ("미상", "미상"),
        ("암컷", "암컷"),
        ("수컷", "수컷"),
    ), default="미상")

    animal_tag = models.CharField(max_length=30)
    find_location = models.CharField(max_length=50)
    find_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-find_board_no']


# 주인찾습니다 게시판 댓글
class FindOwnerBoardComment(TimestampedModel):
    find_comment_no = models.AutoField(primary_key=True)
    comment_content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    find_board_no = models.ForeignKey(FindOwnerBoard, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['find_comment_no']


# 주인찾습니다 이미지
class FindOwnerBoardImage(TimestampedModel):
    find_image_no = models.AutoField(primary_key=True)
    image = models.ImageField(blank=False, null=False, validators=[validate_image])
    find_board_no = models.ForeignKey(FindOwnerBoard, on_delete=models.CASCADE, related_name="board_image")

    class Meta:
        ordering = ['-find_image_no']
