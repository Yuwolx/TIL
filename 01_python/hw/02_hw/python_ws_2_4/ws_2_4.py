# 아래에 코드를 작성하시오.


class MovieTheater:
    def __init__(self, name, total_seats, total_movies):
        self.name = name
        self.total_seats = total_seats
        self.total_movies = total_movies
        self.reserved_seats = 0

    def __str__(self):
        return self.name
    
    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            return "Reservation success"

        else:
            return "Reservation fail"

    def current_status(self):
        return f"total seats: {self.total_seats} | reserved seats: {self.reserved_seats}"
    
    def add_movie(self):
        self.total_movies += 1
        return "success add a movie"
    
    @staticmethod
    def description():
        return '"이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다."  "영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다."'
    


# MovieTheater 클래스는 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다

# add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.

# MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
# description 메서드는 아래 문장을 출력한다.
# '"이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다."
# "영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다."

theater_1 = MovieTheater('메가박스',100,3)
theater_2 = MovieTheater('CGV',100,5)


class VIPMovieTheater(MovieTheater):
    def __init__(self, name, total_seats, total_movies, vip_seats):
        super().__init__(name, total_seats, total_movies)
        self.vip_seats = vip_seats
        self.reserve_seats_vip = 0

    def reserve_vip_seat(self):
        if self.vip_seats > 0:
            self.vip_seats -= 1
            return f"Reservation VIP seats success. Remain seats: {self.vip_seats}"
        else:
            return "Reservation fail. There is no vip seats"
        
    def reserve_seat(self):
        if self.vip_seats > 0:
            return self.reserve_vip_seat()
            
        
        else:
            return super().reserve_seat()

vip_theater_1 = VIPMovieTheater('메가박스',100,3,3)
vip_theater_2 = VIPMovieTheater('CGV',100,5, 20)

print(theater_1.reserve_seat())
print(theater_1.reserve_seat())
print(theater_2.reserve_seat())
print(theater_1.add_movie())
print(theater_1.add_movie())
print(theater_1.current_status())
print(theater_2.current_status())
print(vip_theater_1.reserve_vip_seat())
print(vip_theater_1.reserve_vip_seat())
print(vip_theater_1.reserve_vip_seat())
print(vip_theater_1.reserve_seat())
print(vip_theater_1.reserve_vip_seat())

print(MovieTheater.description())
# MovieTheater 클래스는 모든 영화관이 공통으로 가지는 total_movies변수를 가진다.
# total_movies 변수를 MovieTheater 클래스에 클래스 변수로 추가한다.

# MovieTheater 클래스는 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다

# add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.

# MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
# description 메서드는 아래 문장을 출력한다.
# '"이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다."
# "영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다."

