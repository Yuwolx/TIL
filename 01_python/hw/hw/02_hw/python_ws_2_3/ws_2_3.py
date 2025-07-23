"""
문제
영화관 시스템을 모델링하는 클래스를 정의하시오. 부모 클래스와 자식 클래스를 활용하여 영화관 시스템을 확장하고, 메서드를 오버라이딩하시오.
요구사항
3433번 문제에서 작성한 코드에서 이어서 작성한다.
"""

# 아래에 코드를 작성하시오.
class MovieTheater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
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

theater_1 = MovieTheater('메가박스',100)
theater_2 = MovieTheater('CGV',100)


class VIPMovieTheater(MovieTheater):
    def __init__(self, name, total_seats, vip_seats):
        super().__init__(name, total_seats)
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

vip_theater_1 = VIPMovieTheater('메가박스',100,3)
vip_theater_2 = VIPMovieTheater('CGV',100,20)

print(vip_theater_1.reserve_vip_seat())
print(vip_theater_1.reserve_vip_seat())
print(vip_theater_1.reserve_vip_seat())
print(vip_theater_1.reserve_seat())
print(vip_theater_1.reserve_vip_seat())

            



# MovieTheater 클래스를 상속받는 VIPMovieTheater 클래스를 정의한다. - done

# VIPMovieTheater 클래스는 VIP 좌석 수를 저장하는 vip_seats 인스턴스 변수를 가진다. - done

# 생성자에서 처리되어야 한다. - done

# VIPMovieTheater 클래스는 VIP 좌석을 예약하는 reserve_vip_seat 메서드를 가진다. - done

# reserve_vip_seat 메서드는 예약 가능한 VIP 좌석이 있는 경우, vip_seats를 1 감소시키고 예약 성공 메시지를 반환한다. -done

# 예약 가능한 VIP 좌석이 없는 경우, 예약 실패 메시지를 반환한다. - done

# VIPMovieTheater 클래스는 reserve_seat 메서드를 오버라이딩하여, VIP 좌석이 먼저 예약되도록 한다.

# VIP 좌석이 예약 가능한 경우, reserve_vip_seat 메서드를 호출하여 VIP 좌석을 예약한다.

# VIP 좌석이 예약 불가능한 경우, 부모 클래스의 reserve_seat 메서드를 호출하여 일반 좌석을 예약한다.