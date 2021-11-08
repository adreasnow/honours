import os



def __init_plugin__(self=None):
    from pymol import plugins
    plugins.addmenuitemqt('OEEF Scan', oeefscanGui)

def oeefscanGui(): 
    gui = None
    gui = make_gui()
    gui.show()

def make_gui():
    from pymol import cmd
    from pymol.Qt import QtWidgets
    from pymol.Qt.utils import loadUi

    gui = QtWidgets.QDialog()
    uifile = os.path.join(os.path.dirname(__file__), 'gui.ui')
    form = loadUi(uifile, gui)


    def plotEField(vecCSV, vecCSVS="Null", diff=False, bubble=5, radius=0.2, minH=0, maxH=130, alpha=1, dipolescale=0.3,
               fieldscale=2, fieldcolour="fcba03", dipolecolour="038cfc", perturbeddipolecolour="f54284", state=1, 
               name="", highlightvec=0, highlightstereo="Null", flipcolour=False):
        import numpy as np
        from csv import reader
        import colorsys

        from pymol.cgo import BEGIN, POINTS, END, ALPHA, COLOR, SPHERE, CYLINDER, CONE, cyl_text
        from pymol import vfont
        from pymol import cmd

        
        def hex2rgb(hex):
            r = (int(hex[0:2], 16))/255
            g = (int(hex[2:4], 16))/255
            b = (int(hex[4:6], 16))/255
            return([r, g, b])

        def cart2sph(x, y, z):
            hxy = np.hypot(x, y)
            r = np.hypot(hxy, z)
            el = np.arctan2(z, hxy)
            az = np.arctan2(y, x)
            return az, el, r

        def sph2cart(az, el, r):
            rcos_theta = r * np.cos(el)
            x = rcos_theta * np.cos(az)
            y = rcos_theta * np.sin(az)
            z = r * np.sin(el)
            return x, y, z

        def num_to_rgb(val, max_val=3):
            i = (val * 255 / max_val)
            r = round(np.sin(0.024 * i + 0) * 127 + 128)/255
            g = round(np.sin(0.024 * i + 2) * 127 + 128)/255
            b = round(np.sin(0.024 * i + 4) * 127 + 128)/255
            return (r, g, b)

        # reads in the CSV of x, y, z, energy
        if diff == True:
            with open(vecCSV, "r") as f:
                vecs = list(reader(f))[1:]

            dellist = []
            for i in range(len(vecs)):
                if float(vecs[i][0]) == 0.0 and float(vecs[i][1]) == 0.0 and float(vecs[i][2]) == 0.0 and float(vecs[i][3]) != 0.0:
                    dellist += [i]

            for i in reversed(dellist):
                del vecs[i]

            # extracts only the energy
            er = []
            for i in vecs[1:]:
                er += [float(i[3])]

            with open(vecCSVS, "r") as f:
                vecss = list(reader(f))[1:]

            dellist = []
            for i in range(len(vecss)):
                if float(vecss[i][0]) == 0.0 and float(vecss[i][1]) == 0.0 and float(vecss[i][2]) == 0.0 and float(vecss[i][3]) != 0.0:
                    dellist += [i]

            for i in reversed(dellist):
                del vecss[i]

            # extracts only the energy
            es = []
            for i in vecss[1:]:
                es += [float(i[3])]

            if highlightstereo == "Null":
                e = np.absolute(np.subtract(np.array(es),np.array(er)))
            if highlightstereo == "r":
                e = np.subtract(np.array(er),np.array(es))
            if highlightstereo == "s":
                e = np.subtract(np.array(es),np.array(er))



        elif diff == False:
            with open(vecCSV, "r") as f:
                vecs = list(reader(f))[1:]

            dellist = []
            for i in range(len(vecs)):
                if float(vecs[i][0]) == 0.0 and float(vecs[i][1]) == 0.0 and float(vecs[i][2]) == 0.0 and float(vecs[i][3]) != 0.0:
                    dellist += [i]

            for i in reversed(dellist):
                del vecs[i]

            # extracts only the energy
            e = []
            for i in vecs[1:]:
                e += [float(i[3])]



        # identifies the lowest energy perturbation

        if diff == False:
            counter = 0
            for i in range(len(e)):
                if e[i] == min(e):
                    minnum = counter+1
                counter += 1

            maxe = max(e)
            mine = min(e)
        
        if diff == True:
            deltar = np.subtract(er, es)
            deltas = np.subtract(es, er)
            best_r_e = min(deltar)
            best_s_e = min(deltas)

            counter = 0
            for i in range(len(deltas)):
                if deltas[i] == best_s_e:
                    best_s_e_num = counter+1
                counter += 1
            counter = 0
            for i in range(len(deltar)):
                if deltar[i] == best_r_e:
                    best_r_e_num = counter+1
                counter += 1

            e = np.add(e, abs(min(e)))
            counter = 0
            for i in range(len(e)):
                if e[i] == max(e):
                    minnum = counter+1
                counter += 1       
        if highlightstereo == "Null":
            e = np.subtract(e, max(e))

        if highlightvec != 0:
            minnum = highlightvec
        if highlightstereo == "r":
            minnum = best_r_e_num
            e = deltar
        if highlightstereo == "s":
            minnum = best_s_e_num
            e = deltas

        maxe = max(e)
        mine = min(e) 

        # shifts all the values up to make them positive
        e = np.add(-min(e), e)
        # normalises the energies between 0 and 1
        norm = np.divide(e,max(e))
        # scales it to the colour range
        norm = np.multiply(norm, maxH-minH)

        if flipcolour == True:
            for i in range(len(norm)):
                norm[i] = -norm[i]+maxH
        
        if highlightstereo == "Null":
            # flips the colour range
            norm = abs(np.subtract(max(norm), norm))
        # offsets it
        norm = np.add(norm, minH)

        colours = []
        # generates rgb values off of the normalised values

        for i in norm:
            r, g, b = colorsys.hsv_to_rgb(i/360, 1, 1)
            colours += [[r, g, b]]

        rampradius = 0.1
        ramplen = 12
        rampsegments = 10
        rampseglength = ramplen/(rampsegments+1)
        rampyoffset = -7.0
        textthickness = 0.05

        rampcols = []
        hperseg = int(abs(maxH-minH)/(rampsegments+1))

        
        if minH < maxH:
            for i in range(int(minH), int(maxH), hperseg):
                r, g, b = colorsys.hsv_to_rgb(float(i)/360, 1, 1)
                rampcols += [[r, g, b]]
        else:
            for i in reversed(range(int(maxH), int(minH), hperseg)):
                r, g, b = colorsys.hsv_to_rgb(float(i)/360, 1, 1)
                rampcols += [[r, g, b]]

        # build the ramp, made up of a number of segments
        ramp = []
        for i in range(rampsegments):
            ramp += [CYLINDER]
            ramp += [-(ramplen-((0.5*ramplen)+0.5*rampseglength)) + (i*rampseglength) , rampyoffset, 0.0]
            ramp += [-(ramplen-((0.5*ramplen)+0.5*rampseglength)) + ((i+1)*rampseglength), rampyoffset, 0.0]
            ramp += [rampradius]
            ramp += rampcols[i]
            ramp += rampcols[i+1]
        cmd.load_cgo(ramp, 'ramp{}'.format(name), state=state)

        cgo = []
        axes = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
        pos = [-(ramplen-((0.5*ramplen)+0.5*rampseglength)) + ((rampsegments+1)+0.2), rampyoffset-0.5, 0.0]
        cyl_text(cgo, vfont.plain, pos, str(round(maxe, 1)), textthickness, axes=axes)
        cmd.load_cgo(cgo, 'rampmax{}'.format(name), state=state)
        cgo = []
        pos = [-(ramplen-((0.5*ramplen)+0.5*rampseglength)) - (2.5+rampseglength), rampyoffset-0.5, 0.0]
        cyl_text(cgo, vfont.plain, pos, str(round(mine, 1)), textthickness, axes=axes)
        cmd.load_cgo(cgo, 'rampmin{}'.format(name), state=state)
        cgo = []
        pos = [-6, rampyoffset-2, 0.0]
        if diff == False:
            cyl_text(cgo, vfont.plain, pos, "Stabilisation Energy (kj/mol)", textthickness, axes=axes)
        elif diff == True:
            cyl_text(cgo, vfont.plain, pos, "R/S Splitting (kj/mol)", textthickness, axes=axes)
        cmd.load_cgo(cgo, 'ramplabel{}'.format(name), state=state)
        

        # builds the cgo sphere opbjects
        sphere = []
        for i in range(1, len(vecs)):
            r, g, b = colours[i-1][0], colours[i-1][1], colours[i-1][2]
            az, el, rad = cart2sph(float(vecs[i][0]), float(vecs[i][1]), float(vecs[i][2]))
            # inverts the data so that the points are showing where the valuse are coming from 
            x, y, z = sph2cart(az, el, -bubble)
            sphere += [BEGIN, POINTS]
            sphere += [END]
            sphere += [ALPHA, alpha]
            sphere += [COLOR, r, g, b]
            sphere += [SPHERE, x, y, z, radius]


        cmd.load_cgo(sphere,'field_points{}'.format(name), state=state)
        
        # sets the arrog geometry
        arrowradius = 0.1
        conelength = 0.5
        coneradius = 0.4

        if highlightstereo == "Null":
            ####################################### MAX STABILISATION ##################################### 
            # sets the end of the arrow to be at the point of the minimum energy perturbation
            endxyz = vecs[minnum][0:3]

            #inverts this to the other side of the origin
            az, el, r = cart2sph(float(endxyz[0]), float(endxyz[1]), float(endxyz[2]))
            endxyz = sph2cart(az, el, -(bubble-fieldscale))
            startxyz = sph2cart(az, el, -(bubble+fieldscale))
            conexyz = sph2cart(az, el, -(bubble-fieldscale-conelength))

            conergb = hex2rgb(fieldcolour)
            arrow = []
            # arrow += [BEGIN, POINTS]
            arrow += [CYLINDER]
            arrow += startxyz
            arrow += endxyz
            arrow += [arrowradius]
            arrow += conergb
            arrow += conergb
            arrow += [CONE]
            arrow += endxyz
            arrow += conexyz
            arrow += [coneradius, 0.0]
            arrow += conergb
            arrow += conergb
            arrow += [1.0, 0.0]
            # arrow += [END]

            cmd.load_cgo(arrow, 'max_stabilisation{}'.format(name), state=state)
            cgo = []
            pos = [startxyz[0], startxyz[1], startxyz[2]]
            cyl_text(cgo, vfont.plain, pos, "Best Separation", textthickness, axes=axes)
            cmd.load_cgo(cgo, 'diff{}'.format(name), state=state)


        if diff == True:
            if highlightstereo == "r":
                ####################################### BEST R ##################################### 
                # sets the end of the arrow to be at the point of the minimum energy perturbation
                endxyz = vecs[best_r_e_num][0:3]

                #inverts this to the other side of the origin
                az, el, r = cart2sph(float(endxyz[0]), float(endxyz[1]), float(endxyz[2]))
                endxyz = sph2cart(az, el, -(bubble-fieldscale))
                startxyz = sph2cart(az, el, -(bubble+fieldscale))
                conexyz = sph2cart(az, el, -(bubble-fieldscale-conelength))

                conergb = hex2rgb(fieldcolour)
                arrow = []
                # arrow += [BEGIN, POINTS]
                arrow += [CYLINDER]
                arrow += startxyz
                arrow += endxyz
                arrow += [arrowradius]
                arrow += conergb
                arrow += conergb
                arrow += [CONE]
                arrow += endxyz
                arrow += conexyz
                arrow += [coneradius, 0.0]
                arrow += conergb
                arrow += conergb
                arrow += [1.0, 0.0]
                # arrow += [END]

                cmd.load_cgo(arrow, 'best_r_selection{}'.format(name), state=state)
                cgo = []
                pos = [startxyz[0], startxyz[1], startxyz[2]]
                cyl_text(cgo, vfont.plain, pos, "Best R selection", textthickness, axes=axes)
                cmd.load_cgo(cgo, 'rlabel{}'.format(name), state=state)

            if highlightstereo == "s":
                ####################################### BEST S ##################################### 
                # sets the end of the arrow to be at the point of the minimum energy perturbation
                endxyz = vecs[best_s_e_num][0:3]

                #inverts this to the other side of the origin
                az, el, r = cart2sph(float(endxyz[0]), float(endxyz[1]), float(endxyz[2]))
                endxyz = sph2cart(az, el, -(bubble-fieldscale))
                startxyz = sph2cart(az, el, -(bubble+fieldscale))
                conexyz = sph2cart(az, el, -(bubble-fieldscale-conelength))

                conergb = hex2rgb(fieldcolour)
                arrow = []
                # arrow += [BEGIN, POINTS]
                arrow += [CYLINDER]
                arrow += startxyz
                arrow += endxyz
                arrow += [arrowradius]
                arrow += conergb
                arrow += conergb
                arrow += [CONE]
                arrow += endxyz
                arrow += conexyz
                arrow += [coneradius, 0.0]
                arrow += conergb
                arrow += conergb
                arrow += [1.0, 0.0]
                # arrow += [END]

                cmd.load_cgo(arrow, 'best_s_selection{}'.format(name), state=state)
                cgo = []
                pos = [startxyz[0], startxyz[1], startxyz[2]]
                cyl_text(cgo, vfont.plain, pos, "Best S selection", textthickness, axes=axes)
                cmd.load_cgo(cgo, 'slabel{}'.format(name), state=state)

        # cmd.center(origin=1)
        # cmd.zoom(complete=1)
        ####################################### mol dipole ##################################### 

        x = vecs[0][4]
        y = vecs[0][5]
        z = vecs[0][6]
        # sets the arrow geometry
        arrowradius = 0.1
        conelength = 0.5
        coneradius = 0.4

        # sets the end of the arrow to be at the point of the minimum energy perturbation
        endxyz = [x, y, z]    

        #inverts this to the other side of the origin
        az, el, r = cart2sph(float(endxyz[0]), float(endxyz[1]), float(endxyz[2]))
        endxyz = sph2cart(az, el, dipolescale*(r-(0.5*r)))
        startxyz = sph2cart(az, el, dipolescale*(r+(0.5*r)))
        conexyz = sph2cart(az, el, (dipolescale*(r-(0.5*r)))-conelength)

        conergb = hex2rgb(dipolecolour)
        arrow = []
        # arrow += [BEGIN, POINTS]
        arrow += [CYLINDER]
        arrow += startxyz
        arrow += endxyz
        arrow += [arrowradius]
        arrow += conergb
        arrow += conergb
        arrow += [CONE]
        arrow += endxyz
        arrow += conexyz
        arrow += [coneradius, 0.0]
        arrow += conergb
        arrow += conergb
        arrow += [1.0, 0.0]
        # arrow += [END]

        cmd.load_cgo(arrow, 'molecular_dipole{}'.format(name), state=state)
        cgo = []
        pos = [startxyz[0], startxyz[1], startxyz[2]]
        cyl_text(cgo, vfont.plain, pos, "u".format(), textthickness, axes=axes)
        cmd.load_cgo(cgo, 'molecular_dipole_label{}'.format(name), state=state)

        ####################################### perturbed dipole ##################################### 

        x = vecs[0][4]
        y = vecs[0][5]
        z = vecs[0][6]
        # sets the arrog geometry
        arrowradius = 0.1
        conelength = 0.5
        coneradius = 0.4

        # sets the end of the arrow to be at the point of the minimum energy perturbation
        endxyz = vecs[minnum][4:7]

        #inverts this to the other side of the origin
        az, el, r = cart2sph(float(endxyz[0]), float(endxyz[1]), float(endxyz[2]))
        endxyz = sph2cart(az, el, dipolescale*(r-(0.5*r)))
        startxyz = sph2cart(az, el, dipolescale*(r+(0.5*r)))
        conexyz = sph2cart(az, el, (dipolescale*(r-(0.5*r)))-conelength)

        conergb = hex2rgb(perturbeddipolecolour)
        arrow = []
        # arrow += [BEGIN, POINTS]
        arrow += [CYLINDER]
        arrow += startxyz
        arrow += endxyz
        arrow += [arrowradius]
        arrow += conergb
        arrow += conergb
        arrow += [CONE]
        arrow += endxyz
        arrow += conexyz
        arrow += [coneradius, 0.0]
        arrow += conergb
        arrow += conergb
        arrow += [1.0, 0.0]
        # arrow += [END]

        cmd.load_cgo(arrow, 'max_perturbed_dipole{}'.format(name), state=state)
        cgo = []
        pos = [startxyz[0], startxyz[1], startxyz[2]]
        cyl_text(cgo, vfont.plain, pos, "u(F)".format(name), textthickness, axes=axes)
        cmd.load_cgo(cgo, 'max_perturbed_dipole_label{}'.format(name), state=state)
        cmd.reset()
        return(minnum)

    def browse_r():
        form.vecCSV.setText(QtWidgets.QFileDialog.getOpenFileName()[0])

    def browse_s():
        form.vecCSVS.setText(QtWidgets.QFileDialog.getOpenFileName()[0])
    
    def colourpicker_fieldcolour():
        colour = QtWidgets.QColorDialog.getColor()
        r = colour.red()
        g = colour.green()
        b = colour.blue()
        rgb = '%02x%02x%02x' % (r, g, b)
        form.fieldcolour.setText(rgb)

    def colourpicker_dipolecolour():
        colour = QtWidgets.QColorDialog.getColor()
        r = colour.red()
        g = colour.green()
        b = colour.blue()
        rgb = '%02x%02x%02x' % (r, g, b)
        form.dipolecolour.setText(rgb)

    def colourpicker_perturbeddipolecolour():
        colour = QtWidgets.QColorDialog.getColor()
        r = colour.red()
        g = colour.green()
        b = colour.blue()
        rgb = '%02x%02x%02x' % (r, g, b)
        form.perturbeddipolecolour.setText(rgb)

    def runoeefscanGui():
        csv1 = form.vecCSV.text()
        csv2 = form.vecCSVS.text()

        if csv2 != "":
            if form.diff.checkState() == 0:
                diff = False
            else:
                diff = True
        else:
            diff = False

        bubble = form.bubble.value()
        radius = form.radius.value()
        minH = form.minH.value()
        maxH = form.maxH.value()
        alpha = form.alpha.value()
        dipolescale = form.dipolescale.value()
        fieldscale = form.fieldscale.value()
        fieldcolour=form.fieldcolour.text()
        dipolecolour=form.dipolecolour.text()
        perturbeddipolecolour=form.perturbeddipolecolour.text()
        state = form.state.value()
        name = form.name.text()
        highlightvec = form.highlightvec.value()

        if diff == True:
            if form.highlight_null.isChecked() == True:
                highlightstereo="Null"
            elif form.highlight_r.isChecked() == True:
                highlightstereo="r"
            elif form.highlight_s.isChecked() == True:
                highlightstereo="s"
        else:
            highlightstereo="Null"

        if form.flipcolour.checkState() == 0:
            flipcolour = False
        else:
            flipcolour = True

        print(state)
        return(plotEField(csv1,
            vecCSVS=csv2,
            diff=diff,
            bubble=bubble,
            radius=radius,
            minH=minH,
            maxH=maxH,
            alpha=alpha,
            dipolescale=dipolescale,
            fieldscale=fieldscale,
            fieldcolour=fieldcolour,
            dipolecolour=dipolecolour,
            perturbeddipolecolour=perturbeddipolecolour,
            state=state,
            name=name,
            highlightvec=highlightvec,
            highlightstereo=highlightstereo,
            flipcolour=flipcolour
            ))

    form.buttonBox.accepted.connect(runoeefscanGui)
    form.buttonBox.rejected.connect(form.close)
    form.vecCSVbrowse.clicked.connect(browse_r)
    form.vecCSVSbrowse.clicked.connect(browse_s)
    form.fieldcolour_button.clicked.connect(colourpicker_fieldcolour)
    form.dipolecolour_button.clicked.connect(colourpicker_dipolecolour)
    form.perturbeddipolecolour_button.clicked.connect(colourpicker_perturbeddipolecolour)

    return(gui)


