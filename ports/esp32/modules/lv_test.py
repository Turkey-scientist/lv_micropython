import espidf as esp
import lvgl as lv
from ili9XXX import st7789
from ili9XXX import COLOR_MODE_BGR
from ili9XXX import PORTRAIT
#HSPI_HOST
print('lv_test start')

buf1 = esp.heap_caps_malloc(10*10, esp.MALLOC_CAP.DEFAULT)
buf2 = esp.heap_caps_malloc(10*10, esp.MALLOC_CAP.DEFAULT)

if buf1 and buf2:
    print("Double buffer")
elif buf1:
    print("Single buffer")
else:
    raise RuntimeError("Not enough DMA-able memory to allocate display buffer")

# disp = st7789(miso=-1, mosi=47, clk=21, cs=44, dc=43, rst=-1, power=-1, backlight=48,backlight_on=1, power_on=0, spihost=esp.SPI1_HOST, mhz=40, factor=4, hybrid=True,width=240, height=240, start_x=0, start_y=0, colormode=COLOR_MODE_BGR, rot=PORTRAIT,invert=True, double_buffer=True, half_duplex=True, asynchronous=False, initialize=True)
disp = st7789(
    mosi=47, 
    clk=21, 
    cs=44, 
    dc=43, 
    rst=-1,
    width=240, 
    height=240,
    start_x=0,
    start_y=0,
    rot=-2,
    factor=20
)

lv.init()

def event_handler(evt):
    code = evt.get_code()

    if code == lv.EVENT.CLICKED:
            print("Clicked event seen")
    elif code == lv.EVENT.VALUE_CHANGED:
        print("Value changed seen")

# create a simple button
btn1 = lv.btn(lv.scr_act())

# attach the callback
btn1.add_event_cb(event_handler,lv.EVENT.ALL, None)

btn1.align(lv.ALIGN.CENTER,0,-40)
label=lv.label(btn1)
label.set_text("Button")

# create a toggle button
btn2 = lv.btn(lv.scr_act())

# attach the callback
#btn2.add_event_cb(event_handler,lv.EVENT.VALUE_CHANGED,None)
btn2.add_event_cb(event_handler,lv.EVENT.ALL, None)

btn2.align(lv.ALIGN.CENTER,0,40)
btn2.add_flag(lv.obj.FLAG.CHECKABLE)
btn2.set_height(lv.SIZE.CONTENT)

label=lv.label(btn2)
label.set_text("Toggle")
label.center()

print('lv_test start end')