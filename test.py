import AMcomandPack as am

master = am.geo.Tk()


cv = am.geo.Canvas(master)
cv.pack()

cv.setOrigin(200,200)


cv.create_square(0,0,200, fillColor="green")
cv.create_circle(0,0,100, color="red")

cv.create_text(0, 0, text = "pYtHoN iS GrEaT")

master.mainloop()