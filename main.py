while True:
    if input.rotation(Rotation.PITCH) > 2:
        light.set_all(light.rgb(255,0,255))
    else:
        light.clear()
