@namespace
class SpriteKind:
    egg = SpriteKind.create()
    chicken = SpriteKind.create()
    cow = SpriteKind.create()
    potato = SpriteKind.create()
    horse = SpriteKind.create()
    tree = SpriteKind.create()
    casa = SpriteKind.create()
    tocon = SpriteKind.create()

target: Sprite = None
leña = 0
inv_horses = 0
inv_chickens = 0
inv_potatoes = 0
inv_cows = 0
inv_eggs = 0
cost = 0
qty = 0
price = 0
name = ""
k = 0
trade_lock = False
Backpack = None
def on_overlap_trade(player2: Sprite, itemSprite: Sprite):
    global target
    target = itemSprite

def on_on_overlap(sprite, otherSprite):
    if controller.A.is_pressed():
        music.play(music.string_playable("- - - - - A F - ", 200),
            music.PlaybackMode.IN_BACKGROUND)
        game.show_long_text("Tienes " + ("" + str(leña)) + " de leña", DialogLayout.TOP)
sprites.on_overlap(SpriteKind.player, SpriteKind.casa, on_on_overlap)

def on_down_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-down
            """),
        500,
        False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_destroyed(sprite3):
    global arbol, leña
    tiles.set_wall_at(arbol.tilemap_location(), False)
    leña += 1
    pause(2000)
    arbol = sprites.create(img("""
            ...............cc...............
            ............ccc65c66............
            ............c6c55c76............
            ...........6cc7557c66...........
            ..........cc77777577c6..........
            .........666c677776cc66.........
            ........c7776c7c67657576........
            ........ccc666c666655666........
            ......c66cc7666667777c6766......
            .....c777c77667667767767776.....
            .....cc66cccc77c677cc666666.....
            ....c6766666c7c6767677777766....
            ...cc777666666677767777667c66...
            .666cc6677666667777777776677666.
            .67776677c676677777776677677776.
            cc6666ccc67767776777776cc7767666
            c666777667766776c776777c67776c66
            .c6777666ccc667c676cc666667776c.
            .cc6666766666cc66666666776cc666.
            ...66776c666666666677667766cccc.
            ...cc76c66766666667677667776c...
            ...6cccc677666666776777c77666...
            ......6ccc7c67767776c776cc......
            ........ccc6777c67776cc6........
            ...........cc77c67766...........
            .............6c6666.............
            ............ffeeeef.............
            ..........ffeeeeeeeef...........
            .............feeeffe............
            ..............fef...............
            ..............fef...............
            ...............f................
            """),
        SpriteKind.tree)
    tiles.place_on_random_tile(arbol, sprites.castle.tile_grass2)
    tiles.set_wall_at(arbol.tilemap_location(), True)
sprites.on_destroyed(SpriteKind.tree, on_on_destroyed)

def trade_price(kind: number):
    if kind == SpriteKind.egg:
        return 3
    elif kind == SpriteKind.cow:
        return 5
    elif kind == SpriteKind.potato:
        return 2
    elif kind == SpriteKind.chicken:
        return 6
    elif kind == SpriteKind.horse:
        return 12
    else:
        return 999999

def on_right_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-right
            """),
        500,
        False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_left_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-left
            """),
        500,
        False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_a_pressed():
    global trade_lock, k, name, price, qty, cost, inv_eggs, inv_cows, inv_potatoes, inv_chickens, inv_horses, leña
    if trade_lock:
        return
    trade_lock = True
    if target == None:
        trade_lock = False
        return
    if not (nena.overlapsWith(target)):
        trade_lock = False
        return
    k = target.kind()
    name = trade_name(k)
    price = trade_price(k)
    qty = game.ask_for_number("" + name + ": ¿cuántos quieres?", 2)
    if qty <= 0:
        trade_lock = False
        return
    cost = price * qty
    if leña < cost:
        game.show_long_text("" + """
                No tienes suficiente leña.
                Necesitas:
                """ + ("" + str(cost)) + "\nTienes: " + ("" + str(leña)),
            DialogLayout.BOTTOM)
        trade_lock = False
        return
    leña += 0 - cost
    if k == SpriteKind.egg:
        inv_eggs += qty
    elif k == SpriteKind.cow:
        inv_cows += qty
    elif k == SpriteKind.potato:
        inv_potatoes += qty
    elif k == SpriteKind.chicken:
        inv_chickens += qty
    elif k == SpriteKind.horse:
        inv_horses += qty
    game.show_long_text("Compraste " + ("" + str(qty)) + " " + name + "\nCoste: " + ("" + str(cost)) + " leña" + "\nTe queda: " + ("" + str(leña)),
        DialogLayout.BOTTOM)
    trade_lock = False
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def trade_name(kind2: number):
    if kind2 == SpriteKind.egg:
        return "Huevos"
    elif kind2 == SpriteKind.cow:
        return "Vacas"
    elif kind2 == SpriteKind.potato:
        return "Patatas"
    elif kind2 == SpriteKind.chicken:
        return "Gallinas"
    elif kind2 == SpriteKind.horse:
        return "Caballos"
    else:
        return "?"

def on_up_pressed():
    animation.run_image_animation(nena,
        assets.animation("""
            nena-animation-up
            """),
        500,
        False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap2(sprite22, otherSprite22):
    if controller.A.is_pressed():
        arbol.set_image(img("""
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ..............ffff..............
            .............fddddf.............
            .............fd44df.............
            .............ffddff.............
            .............feffef.............
            .............feeeef.............
            .............feeeef.............
            .............feeeef.............
            ............ffeeeef.............
            ..........ffeeeeeeeef...........
            .............feeeffe............
            ..............fef...............
            ..............fef...............
            ...............f................
            """))
        pause(2000)
        sprites.destroy(arbol)
sprites.on_overlap(SpriteKind.player, SpriteKind.tree, on_on_overlap2)

chicken2 = sprites.create(assets.image("""
    chicken
    """), SpriteKind.chicken)
egg2 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . e e . . . . . . .
        . . . . . . e d d e . . . . . .
        . . . . . e d d d 4 e . . . . .
        . . . . e d d 1 1 d 4 e . . . .
        . . . . e d 1 1 1 d d e . . . .
        . . . e d 1 1 1 1 d d 4 c . . .
        . . . e d 1 1 1 1 d d 4 c . . .
        . . c d d 1 1 1 d d d 4 e c . .
        . . c 4 d 1 1 d d d 4 e e c . .
        . . c e 4 d d 4 4 4 e e e c . .
        . . . c e 4 4 4 4 4 e e c . . .
        . . . c e e 4 4 4 e e e c . . .
        . . . . c c e e e e c c . . . .
        . . . . . . c c c c . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.egg)
arbol = sprites.create(img("""
        ...............cc...............
        ............ccc65c66............
        ............c6c55c76............
        ...........6cc7557c66...........
        ..........cc77777577c6..........
        .........666c677776cc66.........
        ........c7776c7c67657576........
        ........ccc666c666655666........
        ......c66cc7666667777c6766......
        .....c777c77667667767767776.....
        .....cc66cccc77c677cc666666.....
        ....c6766666c7c6767677777766....
        ...cc777666666677767777667c66...
        .666cc6677666667777777776677666.
        .67776677c676677777776677677776.
        cc6666ccc67767776777776cc7767666
        c666777667766776c776777c67776c66
        .c6777666ccc667c676cc666667776c.
        .cc6666766666cc66666666776cc666.
        ...66776c666666666677667766cccc.
        ...cc76c66766666667677667776c...
        ...6cccc677666666776777c77666...
        ......6ccc7c67767776c776cc......
        ........ccc6777c67776cc6........
        ...........cc77c67766...........
        .............6c6666.............
        ............ffeeeef.............
        ..........ffeeeeeeeef...........
        .............feeeffe............
        ..............fef...............
        ..............fef...............
        ...............f................
        """),
    SpriteKind.tree)
casa2 = sprites.create(img("""
        ....................e2e22e2e....................
        .................222eee22e2e222.................
        ..............222e22e2e22eee22e222..............
        ...........e22e22eeee2e22e2eeee22e22e...........
        ........eeee22e22e22e2e22e2e22e22e22eeee........
        .....222e22e22eeee22e2e22e2e22eeee22e22e222.....
        ...22eeee22e22e22e22eee22eee22e22e22e22eeee22...
        4cc22e22e22eeee22e22e2e22e2e22e22eeee22e22e22cc4
        6c6eee22e22e22e22e22e2e22e2e22e22e22e22e22eee6c6
        46622e22eeee22e22eeee2e22e2eeee22e22eeee22e22664
        46622e22e22e22eeee22e2e22e2e22eeee22e22e22e22664
        4cc22eeee22e22e22e22eee22eee22e22e22e22eeee22cc4
        6c622e22e22eeee22e22e2e22e2e22e22eeee22e22e226c6
        466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
        46622e22eeee22e22e22e2e22e2e22e22e22eeee22e22664
        4cc22e22e22e22e22eeee2e22e2eeee22e22e22e22e22cc4
        6c622eeee22e22eeee22eee22eee22eeee22e22eeee226c6
        46622e22e22eeee22e22e2e22e2e22e22eeee22e22e22664
        466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
        4cc22e22eeee22e22e22e2e22e2e22e22e22eeee22e22cc4
        6c622e22e22e22e22e22eee22eee22e22e22e22e22e226c6
        46622eeee22e22e22eeecc6666cceee22e22e22eeee22664
        46622e22e22e22eeecc6666666666cceee22e22e22e22664
        4cceee22e22eeecc66666cccccc66666cceee22e22eeecc4
        6c622e22eeecc66666cc64444446cc66666cceee22e226c6
        46622e22cc66666cc64444444444446cc66666cc22e22664
        46622cc6666ccc64444444444444444446ccc6666cc22664
        4ccc6666ccc6444bcc666666666666ccb4446ccc6666ccc4
        cccccccc6666666cb44444444444444bc6666666cccccccc
        64444444444446c444444444444444444c64444444444446
        66cb444444444cb411111111111111114bc444444444bc66
        666cccccccccccd166666666666666661dccccccccccc666
        6666444444444c116eeeeeeeeeeeeee611c4444444446666
        666e2222222e4c16e4e44e44e44e44ee61c4e2222222e666
        666eeeeeeeee4c16e4e44e44e44e44ee61c4eeeeeeeee666
        666eddddddde4c66f4e4effffffe44ee66c4eddddddde666
        666edffdffde4c66f4effffffffff4ee66c4edffdffde666
        666edccdccde4c66f4effffffffffeee66c4edccdccde666
        666eddddddde4c66f4eeeeeeeeeeeeee66c4eddddddde666
        c66edffdffde4c66e4e44e44e44e44ee66c4edffdffde66c
        c66edccdccde4c66e4e44e44e44e44ee66c4edccdccde66c
        cc66666666664c66e4e44e44e44feeee66c46666666666cc
        .c66444444444c66e4e44e44e44ffffe66c44444444466c.
        ..c64eee4eee4c66f4e44e44e44f44fe66c4eee4eee46c..
        ...c4eee4eee4c66f4e44e44e44effee66c4eee4eee4c...
        ....644444444c66f4e44e44e44e44ee66c444444446....
        .....64eee444c66f4e44e44e44e44ee66c444eee46.....
        ......6ccc666c66e4e44e44e44e44ee66c666ccc6......
        """),
    SpriteKind.casa)
cow2 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        b . . . d d d b b d . c b . . .
        d b d d 1 1 b 1 1 1 d d b . . .
        d d c 1 1 1 1 1 1 1 b d c . . .
        d d 1 1 1 1 1 1 1 b 1 b . . . .
        c 1 1 1 1 1 1 1 1 1 b b . . . .
        1 1 1 1 1 1 1 1 1 1 b b b . . .
        1 b b b 1 1 1 1 1 1 b b d c c .
        b b b b b 1 1 1 1 1 1 1 d c c c
        b f f f b 1 1 1 1 f f 1 d c c c
        b f f f b 1 1 1 1 f f 1 d c c c
        b f f f c c c c c f f 1 b c c f
        b c c c c b b b b c 1 1 b f f .
        1 1 b c c f b b f c 1 1 b . . .
        b 1 1 f c c c c c f 1 b . . . .
        1 b b b f f f f f b b . . . . .
        """),
    SpriteKind.cow)
horse2 = sprites.create(img("""
        .........ff.....
        ........fccf....
        ....ffffcccf....
        ...fffcccccf....
        fffcffcccccff...
        fcfccffcccfff...
        ccfcfcccccccf...
        ccfcfccffcccf...
        ccfffcc1fffff...
        fffffcc1cffff...
        fffffbb1bf1cf...
        fffcccbbccccf...
        ffffcccccceeff..
        ffffffcceecccf..
        cfff..fceccccf..
        ff.....cecccff..
        f.....fffccccf..
        .....ff..ffff...
        ....ff..........
        """),
    SpriteKind.horse)
potato2 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . c c f f . . .
        . . . . . . . . c 4 4 e c f . .
        . . . . . . . c 4 4 4 e e c f .
        . 3 . . . . c e 4 4 e e e c f .
        . . . . c c e e e e e e c c f .
        . . . c e 4 4 e e e e c c c f .
        . . c e 4 4 4 4 e e e e c f . .
        . c e 4 4 4 4 4 e e e e c f . .
        . c e 4 4 4 4 e e e e e f . . .
        . c e e 4 4 e e e e e c f . . .
        . f e e e e e e e e c f . . . .
        . f c e e e e e e c f . . . . .
        . . f c e e c c f f . . . . . .
        . . . f f f f f . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.potato)
nena = sprites.create(assets.image("""
    nena-front
    """), SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    nivel2
    """))
controller.move_sprite(nena)
scene.camera_follow_sprite(nena)
tiles.place_on_tile(nena, tiles.get_tile_location(7, 4))
tiles.place_on_tile(casa2, tiles.get_tile_location(7, 2))
tiles.place_on_tile(chicken2, tiles.get_tile_location(4, 2))
tiles.place_on_tile(potato2, tiles.get_tile_location(4, 4))
tiles.place_on_tile(egg2, tiles.get_tile_location(10, 2))
tiles.place_on_tile(cow2, tiles.get_tile_location(10, 4))
tiles.place_on_tile(horse2, tiles.get_tile_location(7, 5))
tiles.place_on_random_tile(arbol, sprites.castle.tile_grass2)
tiles.set_wall_at(arbol.tilemap_location(), True)
sprites.on_overlap(SpriteKind.player, SpriteKind.egg, on_overlap_trade)
sprites.on_overlap(SpriteKind.player, SpriteKind.cow, on_overlap_trade)
sprites.on_overlap(SpriteKind.player, SpriteKind.potato, on_overlap_trade)
sprites.on_overlap(SpriteKind.player, SpriteKind.chicken, on_overlap_trade)
sprites.on_overlap(SpriteKind.player, SpriteKind.horse, on_overlap_trade)
