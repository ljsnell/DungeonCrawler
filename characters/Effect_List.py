from characters import Status_Effect

Status_Creator = Status_Effect.Status_Effect

SLOW = Status_Creator(name='slow', hit_percent=25, proc_chance=20)
# Currently unused effects
POISON = Status_Creator(name='poison', hit_percent=33,
                        proc_chance=50)  # 1 damage per proc
BLIND = Status_Creator(name='blind', hit_percent=10,
                       proc_chance=100)  # Reduced Accuracy
