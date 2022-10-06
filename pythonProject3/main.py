from sys import argv
import os

import Base

import Rocket

if __name__ == "__main__":

    bases = []
    with open('targets.txt', "r") as file:
        for line in file:
            x, y, w = map(int, line.split())
            bases.append(Base.Base(x, y, w))

    r = int(argv[1])
    #r=2
    maxw = 0
    rocket_max = Rocket.Rocket(r, 0, 0, 0)

    # перебор пар точек

    for i in range(len(bases)):
        for j in range(i, len(bases)):
            #print('bases: {},{} and {},{}'.format(bases[i].x, bases[i].y, bases[j].x, bases[j].y))
            if bases[i].distance(bases[j]) < 2 * r:  # случай когда расстояние между точками меньше 2R
                if bases[i].distance(bases[j]) == 0: # совпадение точек
                    rocket1 = Rocket.Rocket(r, bases[i].x, bases[j].y, 0)
                    rocket1.get_damage(bases)
                    rocket2 = Rocket.Rocket(0, 0, 0, 0)
                else:                                   # не совпадение точек

                    centers = bases[i].get_centres(bases[j], r) #рассчет центров окружностей проходящих через обе точки
                    center1 = centers[0]
                    center2 = centers[1]

                    # рассчет и сравнение урона окружностей

                    rocket1 = Rocket.Rocket(r, center1[list(center1.keys())[0]],
                                            center1[list(center1.keys())[1]], 0)
                    rocket2 = Rocket.Rocket(r, center2[list(center2.keys())[0]],
                                            center2[list(center2.keys())[1]], 0)

                    rocket1.get_damage(bases)
                    rocket2.get_damage(bases)
                # _______________

                if rocket1.w > rocket_max.w:
                    rocket_max = rocket1
                    print('max found')
                elif rocket2.w > rocket_max.w:
                    rocket_max = rocket2
                    print('max found')



            elif bases[i].distance(bases[j]) == 2 * r:       #случай когда точки расположены на диаметре, центр окружности на середине отрезка соединяющего точки
                rocket = Rocket.Rocket(r, (bases[i].x + bases[j].x) / 2, (bases[i].y + bases[j].y) / 2, 0)
                rocket1.get_damage(bases)
                if rocket1.w > rocket_max.w:
                    rocket_max = rocket1

    print('best aim coordinates: [{},{}],  total damage: {}'.format(float(rocket_max.x),
                                                                    float(rocket_max.y),
                                                                    float(rocket_max.w)))
    #os.system('python Plot_results.py {} {} {}'.format(float(rocket_max.x), float(rocket_max.y),r))
