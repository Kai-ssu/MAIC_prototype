import gi
import math
from math import pi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk

class Handler:
    def on_window1_destroy(self, *args):
        gtk.main_quit()
    
    def on_weightequals_pressed(self, button):    
        urmass = builder.get_object('weight-pln').get_text()
       
        pln = [
            float(urmass) * 0.38,   # mercury
            float(urmass) * 0.91,   # venus
            float(urmass) * 1,      # earth
            float(urmass) * 0.38,   # mars
            float(urmass) * 2.34,   # jupiter
            float(urmass) * 0.93,   # saturn
            float(urmass) * 0.92,   # uranus
            float(urmass) * 1.12    # neptune
        ]

        ans = []
        planets = [
            'weight_mercury', 'weight_venus', 'weight_earth', 'weight_mars', 'weight_jupiter', 
            'weight_saturn', 'weight_uranus', 'weight_neptune'
        ]
        for count in range(0, 8):
            ans.append(builder.get_object(planets[count]))
            ans[count].set_text(str("{:.3}".format(pln[count])))
        
    def on_magequals_pressed(self, button):
        foc_l = builder.get_object('mag-fltele').get_text()
        foc_e = builder.get_object('mag-fceye').get_text()
        mag = float(foc_l) / float(foc_e)
        answer = builder.get_object('mag-answer')
        answer.set_text(str("{:.3}".format(mag)))

    def on_keplerequals_pressed(self, button):
        M = builder.get_object('kepler-mass').get_text()
        R = builder.get_object('kepler-distance').get_text()
        plan_motion = ((math.pi * 4) * (float(R)**3)) / ((6.67*(10**-11))) * float(M)
        t = math.sqrt(plan_motion)
        answer = builder.get_object('kepler-answer')
        answer.set_text(str("{:.3}".format(t)))

    def on_astdequals_pressed(self, button):
        para = builder.get_object('astd-parallax').get_text()
        distance = 1 / float(para)
        answer = builder.get_object('astd-answer')
        answer.set_text(str("{:.3}".format(distance)))

    def on_apertequals_pressed(self, button):
        lens = builder.get_object('apert-lens').get_text()
        aper = builder.get_object('apert-circle').get_text()
        aperture = float(lens) / float(aper)
        answer = builder.get_object('apert-answer')
        answer.set_text(str("{:.3}".format(aperture)))

    def on_focalratioequals_pressed(self, button):
        foc_length = builder.get_object('fcr-length').get_text()
        lens_aperture = builder.get_object('fcr-lens').get_text()
        fr = float(foc_length) / float(lens_aperture)
        answer = builder.get_object('focal-ratio-answer')
        answer.set_text(str("{:.3}".format(fr)))

    def on_flequals_pressed(self, button):
        foc_ratio = builder.get_object('fl-ratio').get_text()
        lens_aper = builder.get_object('fl-lens').get_text()
        fl = float(foc_ratio) * float(lens_aper)
        answer = builder.get_object('fl-answer')
        answer.set_text(str("{:.3}".format(fl)))

    def on_drakeequals_pressed(self, button):
        R = builder.get_object('drake-r').get_text()
        f_p = builder.get_object('drake-fp').get_text()
        n_e = builder.get_object('drake-ne').get_text()
        f_l = builder.get_object('drake-fl').get_text()
        f_i = builder.get_object('drake-fi').get_text()
        f_c = builder.get_object('drake-fc').get_text()
        L   = builder.get_object('drake-l').get_text()
        drake = float(R) * float(f_p) * float(n_e) * float(f_l) * float(f_i) * float(f_c) * float(L)
        answer = builder.get_object('drake-answer')
        answer.set_text(str("{:.3}".format(drake)))

    def on_voltequals_pressed(self, button):
        cur1 = builder.get_object('voltage-current').get_text()
        res1 = builder.get_object('voltage-resistance').get_text()
        voltage = float(cur1) * float(res1)
        answer = builder.get_object('voltage-answer')
        answer.set_text(str("{:.3}".format(voltage)))

    def on_currentequals_pressed(self, button):
        vol1 = builder.get_object('current-voltage').get_text()
        res2 = builder.get_object('current-resistance').get_text()
        current = float(vol1) / float(res2)
        answer = builder.get_object('current-answer')
        answer.set_text(str("{:.3}".format(current)))

    def on_wattequals_pressed(self, button):
        cur2 = builder.get_object('wattage-current').get_text()
        vol2 = builder.get_object('wattage-voltage').get_text()
        wattage = float(cur2) * float(vol2)
        answer = builder.get_object('watt-answer')
        answer.set_text(str("{:.3}".format(wattage)))

    def on_velequals_pressed(self, button):
        f_pos = builder.get_object('vel-fpos').get_text()
        i_pos = builder.get_object('vel-ipos').get_text()
        f_time = builder.get_object('vel-ftime').get_text()
        i_time = builder.get_object('vel-itime').get_text()
        ave_sv = (float(f_pos) - float(i_pos)) / (float(f_time) - float(i_time))
        answer = builder.get_object('vel-answer')
        answer.set_text(str("{:.3}".format(ave_sv)))

    def on_speedvelequals_pressed(self, button):
        dis = builder.get_object('speed-distance').get_text()
        time = builder.get_object('speed-time').get_text()
        speed = float(dis) / float(time)
        answer = builder.get_object('speed-vel-answer')
        answer.set_text(str("{:.3}".format(speed)))

    def on_stelmagequals_pressed(self, button):
        d_o = builder.get_object('stelmag-obj').get_text()
        d_eye = builder.get_object('stelmag-eye').get_text()
        stelmag = (float(d_o) / float(d_eye))**2
        answer = builder.get_object('stelmag-answer')
        answer.set_text(str("{:.3}".format(stelmag)))

    def on_lawequals_pressed(self, button):
        grav = float(6.67*(10**(-11)))
        mass1 = builder.get_object('mass1-entry')
        mass2 = builder.get_object('mass2-entry')
        dis = builder.get_object('distance-mass-entry')
        fgrav = grav * ((float(mass1.get_text()) * float(mass2.get_text()))/ (float(dis.get_text())**22))
        answer = builder.get_object('law-answer')
        answer.set_text(str("{:.3}".format(fgrav)))
        
    def on_lengthequals_pressed(self, button):
        length_entry = builder.get_object('length-entry').get_text()
        length_unit1 = builder.get_object('length-unit1').get_text()
        length_unit2 = builder.get_object('length-unit2').get_text()

        length = {
            'm (meter)km (kilometer)': '/1000.0',
            'm (meter)cm (centimeter)': '*100.0',
            'm (meter)mm (millimeter)': '*1000.0 ',
            'm (meter)μm (micrometer)': '*(10.0**6)',
            'm (meter)nm (nanometer)': '*(10.0**9)',
            'm (meter)mi (mile)': '*0.000621371',
            'm (meter)yd (yard)': '*1.09361',
            'm (meter)ft (foot)': '*3.28084',
            'm (meter)in (inch)': '*39.3701',
            'm (meter)NM (nautical mile)': '/1852.0',
            'km (kilometer)m (meter)': '*1000.0',
            'km (kilometer)cm (centimeter)': '*100000.0',
            'km (kilometer)mm (millimeter)': '*(10.0**6)',
            'km (kilometer)μm (micrometer)': '*(10.0**9)',
            'km (kilometer)nm (nanometer)': '*(10.0**12)',
            'km (kilometer)mi (mile)': '*0.621371',
            'km (kilometer)yd (yard)': '*1093.61',
            'km (kilometer)ft (foot)': '*3280.84',
            'km (kilometer)in (inch)': '*39370.1',
            'km (kilometer)NM (nautical mile)': '/1.852',
            'cm (centimeter)km (kilometer)': '/100000.0',
            'cm (centimeter)m (meter)': '/100.0',
            'cm (centimeter)mm (millimeter)': '*(10.0)',
            'cm (centimeter)μm (micrometer)': '*(10000.0)',
            'cm (centimeter)nm (nanometer)': '*(10.0**7)',
            'cm (centimeter)mi (mile)': '/160934.0',
            'cm (centimeter)yd (yard)': '/91.44',
            'cm (centimeter)ft (foot)': '/30.48', 
            'cm (centimeter)in (inch)': '/2.54',
            'cm (centimeter)NM (nautical mile)': '/185200.0',
            'mm (millimeter)km (kilometer)': '*(10.0**(-6))',
            'mm (millimeter)m (meter)': '/1000.0',
            'mm (millimeter)cm (centimeter)': '/(10.0)',
            'mm (millimeter)μm (micrometer)': '*1000.0',
            'mm (millimeter)nm (nanometer)': '*(10.0**6)',
            'mm (millimeter)mi (mile)': '/(1.609*(10**6))',
            'mm (millimeter)yd (yard)': '/914.0',
            'mm (millimeter)ft (foot)': '/305.0',
            'mm (millimeter)in (inch)': '/25.4',
            'mm (millimeter)NM (nautical mile)': '/(1.852*(10**6))',
            'μm (micrometer)km (kilometer)': '/(10.0**9)',
            'μm (micrometer)m (meter)': '/(10.0**6)',
            'μm (micrometer)cm (centimeter)': '/(10000.0)',
            'μm (micrometer)mm (millimeter)': '/1000.0',
            'μm (micrometer)nm (nanometer)': '*1000.0',
            'μm (micrometer)mi (mile)': '/(1.609*(10**9))',
            'μm (micrometer)yd (yard)': '/914400.0',
            'μm (micrometer)ft (foot)': '/304800.0',
            'μm (micrometer)in (inch)': '/25400.0',
            'μm (micrometer)NM (nautical mile)': '/(1.852*(10**9))',
            'nm (nanometer)km (kilometer)': '/(10.0**12)',
            'nm (nanometer)m (meter)': '/(10.0**9)',
            'nm (nanometer)cm (centimeter)': '/(10.0**7)',
            'nm (nanometer)mm (millimeter)': '/(10.0**6)',
            'nm (nanometer)μm (micrometer)': '*1000.0',
            'nm (nanometer)mi (mile)': '/(1.609*(10**12))',
            'nm (nanometer)yd (yard)': '/(9.144*(10**8))',
            'nm (nanometer)ft (foot)': '/(3.048*(10**8))',
            'nm (nanometer)in (inch)': '/(2.54*(10**7))',
            'nm (nanometer)NM (nautical mile)': '/(1.852*(10**12))',
            'mi (mile)km (kilometer)': '*1.609',
            'mi (mile)m (meter)': '*1609.0',
            'mi (mile)cm (centimeter)': '*160934.0',
            'mi (mile)mm (millimeter)': '*(1.609*(10.0**6))',
            'mi (mile)μm (micrometer)': '*(1.609*(10.0**9))',
            'mi (mile)nm (nanometer)': '*(1.609*(10.0**12))',
            'mi (mile)yd (yard)': '*1760.0',
            'mi (mile)ft (foot)': '*5280.0',
            'mi (mile)in (inch)': '*63360.0',
            'mi (mile)NM (nautical mile)': '/1.151',
            'yd (yard)km (kilometer)': '/1094.0',
            'yd (yard)m (meter)': '/1.094',
            'yd (yard)cm (centimeter)': '*91.44',
            'yd (yard)mm (millimeter)': '*914.0',
            'yd (yard)μm (micrometer)': '*914400.0',
            'yd (yard)nm (nanometer)': '*(9.144*(10.0**8))',
            'yd (yard)mi (mile)': '/1760.0',
            'yd (yard)ft (foot)': '*3.0',
            'yd (yard)in (inch)': '*36.0',
            'yd (yard)NM (nautical mile)': '/2025.0',
            'ft (foot)km (kilometer)': '/3281.0',
            'ft (foot)m (meter)': '/3.281',
            'ft (foot)cm (centimeter)': '*30.48',
            'ft (foot)mm (millimeter)': '*305.0',
            'ft (foot)μm (micrometer)': '*304800.0',
            'ft (foot)nm (nanometer)': '*(3.048*(10.0**8))',
            'ft (foot)mi (mile)': '/5280.0',
            'ft (foot)yd (yard)': '/3.0',
            'ft (foot)in (inch)': '*12.0',
            'ft (foot)NM (nautical mile)': '/6076.0',
            'in (inch)km (kilometer)': '/39370.0',
            'in (inch)m (meter)': '/39.37',
            'in (inch)cm (centimeter)': '*2.54',
            'in (inch)mm (millimeter)': '*25.4',
            'in (inch)μm (micrometer)': '*25400.0',
            'in (inch)nm (nanometer)': '*(2.54*(10.0**7))',
            'in (inch)mi (mile)': '/63360.0',
            'in (inch)yd (yard)': '/36.0',
            'in (inch)ft (foot)': '/12.0',
            'in (inch)NM (nautical mile)': '/72913.0',
            'NM (nautical mile)km (kilometer)': '*1.852',
            'NM (nautical mile)m (meter)': '*1852.0',
            'NM (nautical mile)cm (centimeter)': '*185200.0',
            'NM (nautical mile)mm (millimeter)': '*(1.852*(10**6))',
            'NM (nautical mile)μm (micrometer)': '*(1.852*(10**9))',
            'NM (nautical mile)nm (nanometer)': '*(1.852*(10**12))',
            'NM (nautical mile)mi (mile)': '*1.151',
            'NM (nautical mile)yd (yard)': '*2025.0',
            'NM (nautical mile)ft (foot)': '*6076.0',
            'NM (nautical mile)in (inch)': '*72913.0',
            'km (kilometer)km (kilometer)': '*1',
            'm (meter)m (meter)': '*1',
            'cm (centimeter)cm (centimeter)': '*1',
            'mm (millimeter)mm (millimeter)': '*1',
            'μm (micrometer)μm (micrometer)': '*1',
            'nm (nanometer)nm (nanometer)': '*1',
            'mi (mile)mi (mile)': '*1',
            'yd (yard)yd (yard)': '*1',
            'ft (foot)ft (foot)': '*1',
            'in (inch)in (inch)': '*1',
            'NM (nautical mile)NM (nautical mile)': '*1'

        }

        conv = eval('%s %s' % (float(length_entry), length[length_unit1 + length_unit2]))

        answer = builder.get_object('length-answer')
        answer.set_text(str(conv))   
        answer_sci = builder.get_object('length-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))
        
    def on_volumeequals_pressed(self, button):
        volume_entry = builder.get_object('volume-entry').get_text()
        volume_unit1 = builder.get_object('volume-unit1').get_text()
        volume_unit2 = builder.get_object('volume-unit2').get_text()
        
        volume = {
            'litermilliliter': '*1000.0',
            'literfluid ounce': '*35.195',
            'literUS liquid gallon': '/3.785',
            'literUS liquid quart': '*1.057',
            'literUS liquid pint': '*2.113',
            'literUS legal cup': '*4.167',
            'literUS tablespoon': '*67.628',
            'literUS teaspoon': '*203.0',
            'litercubic meter': '/1000.0',
            'literImperial gallon': '/4.546',
            'literImperial quart': '/1.137',
            'literImperial pint': '*1.76',
            'literImperial cup': '*3.52',
            'literImperial tablespoon': '*56.3121',
            'literImperial teaspoon': '*169.0',
            'litercubic foot': '/28.317',
            'litercubic inch': '*61.024',
            'milliliterliter': '/1000.0',
            'milliliterfluid ounce': '/29.574',
            'milliliterUS liquid gallon': '/3785.0',
            'milliliterUS liquid quart': '/946.0',
            'milliliterUS liquid pint': '/473.0',
            'milliliterUS legal cup': '/240.0',
            'milliliterUS tablespoon': '/14.787',
            'milliliterUS teaspoon': '/4.929',
            'millilitercubic meter': '/(10.0**6)',
            'milliliterImperial gallon': '/4546.0',
            'milliliterImperial quart': '/1137.0',
            'milliliterImperial pint': '/568.0',
            'milliliterImperial cup': '/284.0',
            'milliliterImperial tablespoon': '/17.758',
            'milliliterImperial teaspoon': '/5.919',
            'millilitercubic foot': '/28317.0',
            'millilitercubic inch': '/16.387',
            'fluid ounceliter': '/33.814',
            'fluid ouncemilliliter': '*29.574',
            'fluid ounceUS liquid gallon': '/128.0',
            'fluid ounceUS liquid quart': '/32.0',
            'fluid ounceUS liquid pint': '/16.0',
            'fluid ounceUS legal cup': '/8.115',
            'fluid ounceUS tablespoon': '*2.0',
            'fluid ounceUS teaspoon': '*6.0',
            'fluid ouncecubic meter': '/33814.0',
            'fluid ounceImperial gallon': '/154.0',
            'fluid ounceImperial quart': '/38.43',
            'fluid ounceImperial pint': '/19.215',
            'fluid ounceImperial cup': '/9.608',
            'fluid ounceImperial tablespoon': '*1.665',
            'fluid ounceImperial teaspoon': '*4.996',
            'fluid ouncecubic foot': '/958.0',
            'fluid ouncecubic inch': '*1.805',
            'US liquid gallonliter': '*3.785',
            'US liquid gallonmilliliter': '*3785.0',
            'US liquid gallonfluid ounce': '*128.0',
            'US liquid gallonUS liquid quart': '*4.0',
            'US liquid gallonUS liquid pint': '*8.0',
            'US liquid gallonUS legal cup': '*15.773',
            'US liquid gallonUS tablespoon': '*256.0',
            'US liquid gallonUS teaspoon': '*768.0',
            'US liquid galloncubic meter': '/264.0',
            'US liquid gallonImperial gallon': '/1.201',
            'US liquid gallonImperial quart': '*3.331',
            'US liquid gallonImperial pint': '*6.661',
            'US liquid gallonImperial cup': '*13.323',
            'US liquid gallonImperial tablespoon': '*213.0',
            'US liquid gallonImperial teaspoon': '*639.0',
            'US liquid galloncubic foot': '7.481',
            'US liquid galloncubic inch': '*231.0',
            'US liquid quartliter': '/1.057',
            'US liquid quartmilliliter': '*946.0',
            'US liquid quartfluid ounce': '*32.0',
            'US liquid quartUS liquid gallon': '/4.0',
            'US liquid quartUS liquid pint': '*2.0',
            'US liquid quartUS legal cup': '*3.943',
            'US liquid quartUS tablespoon': '*64.0',
            'US liquid quartUS teaspoon': '*192.0',
            'US liquid quartcubic meter': '/1057.0',
            'US liquid quartImperial gallon': '/4.804',
            'US liquid quartImperial quart': '/1.201',
            'US liquid quartImperial pint': '*1.665',
            'US liquid quartImperial cup': '*3.331',
            'US liquid quartImperial tablespoon': '*53.291',
            'US liquid quartImperial teaspoon': '*160.0',
            'US liquid quartcubic foot': '/29.922',
            'US liquid quartcubic inch': '*57.75',
            'US liquid pintliter': '/2.113',
            'US liquid pintmilliliter': '*473.0',
            'US liquid pintfluid ounce': '*16.0',
            'US liquid pintUS liquid gallon': '/8.0',
            'US liquid pintUS liquid quart': '/2.0',
            'US liquid pintUS legal cup': '*1.972',
            'US liquid pintUS tablespoon': '*32.0',
            'US liquid pintUS teaspoon': '*96.0',
            'US liquid pintcubic meter': '/2113.0',
            'US liquid pintImperial gallon': '/9.608',
            'US liquid pintImperial quart': '/2.402',
            'US liquid pintImperial pint': '/1.201',
            'US liquid pintImperial cup': '*1.665',
            'US liquid pintImperial tablespoon': '*26.646',
            'US liquid pintImperial teaspoon': '79.937',
            'US liquid pintcubic foot': '/59.844',
            'US liquid pintcubic inch': '*28.875',
            'US legal cupliter': '/4.167',
            'US legal cupmilliliter': '*240.0',
            'US legal cupfluid ounce': '*8.115',
            'US legal cupUS liquid gallon': '/15.773',
            'US legal cupUS liquid quart': '/3.943',
            'US legal cupUS liquid pint': '1.972',
            'US legal cupUS tablespoon': '*16.231',
            'US legal cupUS teaspoon': '*48.692',
            'US legal cupcubic meter': '/4167.0',
            'US legal cupImperial gallon': '/18.942',
            'US legal cupImperial quart': '/4.736',
            'US legal cupImperial pint': '/2.368',
            'US legal cupImperial cup': '/1.184',
            'US legal cupImperial tablespoon': '*13.515',
            'US legal cupImperial teaspoon': '*40.545',
            'US legal cupcubic foot': '/118.0',
            'US legal cupcubic inch': '*14.646',
            'US tablespoonliter': '/67.628',
            'US tablespoonmilliliter': '*14.787',
            'US tablespoonfluid ounce': '/2.0',
            'US tablespoonUS liquid gallon': '/256.0',
            'US tablespoonUS liquid quart': '/64.0',
            'US tablespoonUS liquid pint': '/32.0',
            'US tablespoonUS legal cup': '/16.231',
            'US tablespoonUS teaspoon': '*3.0',
            'US tablespooncubic meter': '/67628.0',
            'US tablespoonImperial gallon': '/307.0',
            'US tablespoonImperial quart': '/76.861',
            'US tablespoonImperial pint': '/38.43',
            'US tablespoonImperial cup': '/19.215',
            'US tablespoonImperial tablespoon': '/1.201',
            'US tablespoonImperial teaspoon': '*2.498',
            'US tablespooncubic foot': '/1915.0',
            'US tablespooncubic inch': '/1.108',
            'US teaspoonliter': '/203.0',
            'US teaspoonmilliliter': '*4.929',
            'US teaspoonfluid ounce': '/6.0',
            'US teaspoonUS liquid gallon': '/768.0',
            'US teaspoonUS liquid quart': '/192.0',
            'US teaspoonUS liquid pint': '/96.0',
            'US teaspoonUS legal cup': '/48.892',
            'US teaspoonUS tablespoon': '/3.0',
            'US teaspooncubic meter': '/202884.0',
            'US teaspoonImperial gallon': '/922.0',
            'US teaspoonImperial quart': '/231.0',
            'US teaspoonImperial pint': '/115.0',
            'US teaspoonImperial cup': '/57.646', 
            'US teaspoonImperial tablespoon': '/3.603',
            'US teaspoonImperial teaspoon': '/1.201',
            'US teaspooncubic foot': '/5745.0',
            'US teaspooncubic inch': '/3.325',
            'cubic meterliter': '*1000.0', 
            'cubic metermilliliter': '*(10.0**6)',
            'cubic meterfluid ounce': '*33814.0',
            'cubic meterUS liquid gallon': '*264.0',
            'cubic meterUS liquid quart': '*1057.0',
            'cubic meterUS liquid pint': '*2113.0',
            'cubic meterUS legal cup': '*4167.0',
            'cubic meterUS tablespoon': '*67628.0',
            'cubic meterUS teaspoon': '*202884.0',
            'cubic meterImperial gallon': '*220.0',
            'cubic meterImperial quart': '*879.877',
            'cubic meterImperial pint': '*1760.0',
            'cubic meterImperial cup': '*3520.0',
            'cubic meterImperial tablespoon': '*56312.0',
            'cubic meterImperial teaspoon': '*168936.0',
            'cubic metercubic foot': '*35.315',
            'cubic metercubic inch': '*61024.0',
            'Imperial gallonliter': '*4.546',
            'Imperial gallonmilliliter': '*4546.0',
            'Imperial gallonfluid ounce': '*154.0',
            'Imperial gallonUS liquid gallon': '*1.201',
            'Imperial gallonUS liquid quart': '*4.804',
            'Imperial gallonUS liquid pint': '*9.608',
            'Imperial gallonUS legal cup': '*18.942',
            'Imperial gallonUS tablespoon': '*307.0',
            'Imperial gallonUS teaspoon': '*922.0',
            'Imperial galloncubic meter': '/220.0',
            'Imperial gallonImperial quart': '*4.0',
            'Imperial gallonImperial pint': '*8.0',
            'Imperial gallonImperial cup': '*16.0',
            'Imperial gallonImperial tablespoon': '*256.0',
            'Imperial gallonImperial teaspoon': '*768.0',
            'Imperial galloncubic foot': '/6.229',
            'Imperial galloncubic inch': '*277.0',
            'Imperial quartliter': '*1.137',
            'Imperial quartmilliliter': '*1137.0',
            'Imperial quartfluid ounce': '*38.43',
            'Imperial quartUS liquid gallon': '/3.331',
            'Imperial quartUS liquid quart': '*1.201',
            'Imperial quartUS liquid pint': '*2.402',
            'Imperial quartUS legal cup': '*4.736',
            'Imperial quartUS tablespoon': '*76.861',
            'Imperial quartUS teaspoon': '*231.0',
            'Imperial quartcubic meter': '/880.0',
            'Imperial quartImperial gallon': '/4.0',
            'Imperial quartImperial pint': '*2.0',
            'Imperial quartImperial cup': '*4.0',
            'Imperial quartImperial tablespoon': '*64.0',
            'Imperial quartImperial teaspoon': '*192.0',
            'Imperial quartcubic foot': '/24.915',
            'Imperial quartcubic inch': '*69.355',
            'Imperial pintliter': '/1.76',
            'Imperial pintmilliliter': '/568.0',
            'Imperial pintfluid ounce': '*19.215',
            'Imperial pintUS liquid gallon': '/6.661',
            'Imperial pintUS liquid quart': '1.665',
            'Imperial pintUS liquid pint': '*1.201',
            'Imperial pintUS legal cup': '*2.368',
            'Imperial pintUS tablespoon': '*38.43',
            'Imperial pintUS teaspoon': '*115.0',
            'Imperial pintcubic meter': '/1760.0',
            'Imperial pintImperial gallon': '/8.0',
            'Imperial pintImperial quart': '2.0',
            'Imperial pintImperial cup': '*2.0',
            'Imperial pintImperial tablespoon': '32.0',
            'Imperial pintImperial teaspoon': '*96.0',
            'Imperial pintcubic foot': '/49.831',
            'Imperial pintcubic inch': '*34.677',
            'Imperial cupliter': '/3.52',
            'Imperial cupmilliliter': '*284.0',
            'Imperial cupfluid ounce': '*9.608',
            'Imperial cupUS liquid gallon': '/13.323',
            'Imperial cupUS liquid quart': '/3.331',
            'Imperial cupUS liquid pint': '/1.665',
            'Imperial cupUS legal cup': '*1.184',
            'Imperial cupUS tablespoon': '*19.215',
            'Imperial cupUS teaspoon': '*57.646',
            'Imperial cupcubic meter': '/3520.0',
            'Imperial cupImperial gallon': '/16.0',
            'Imperial cupImperial quart': '/4.0',
            'Imperial cupImperial pint': '/2.0',
            'Imperial cupImperial tablespoon': '*16.0',
            'Imperial cupImperial teaspoon': '*48.0',
            'Imperial cupcubic foot': '/99.661',
            'Imperial cupcubic inch': '*17.339',
            'Imperial tablespoonliter': '/56.312',
            'Imperial tablespoonmilliliter': '*17.758',
            'Imperial tablespoonfluid ounce': '/1.665',
            'Imperial tablespoonUS liquid gallon': '/213.0',
            'Imperial tablespoonUS liquid quart': '/53.291',
            'Imperial tablespoonUS liquid pint': '/26.646',
            'Imperial tablespoonUS legal cup': '/13.515',
            'Imperial tablespoonUS tablespoon': '*1.201',
            'Imperial tablespoonUS teaspoon': '*3.603',
            'Imperial tablespooncubic meter': '/56312.0',
            'Imperial tablespoonImperial gallon': '/256.0',
            'Imperial tablespoonImperial quart': '/64.0',
            'Imperial tablespoonImperial pint': '/32.0',
            'Imperial tablespoonImperial cup': '/16.0',
            'Imperial tablespoonImperial teaspoon': '*3.0',
            'Imperial tablespooncubic foot': '/1595.0',
            'Imperial tablespooncubic inch': '*1.084',
            'Imperial teaspoonliter': '/169.0',
            'Imperial teaspoonmilliliter': '*5.919',
            'Imperial teaspoonfluid ounce': '/4.996',
            'Imperial teaspoonUS liquid gallon': '/639.0',
            'Imperial teaspoonUS liquid quart': '/160.0',
            'Imperial teaspoonUS liquid pint': '/79.937',
            'Imperial teaspoonUS legal cup': '/40.545',
            'Imperial teaspoonUS tablespoon': '/2.498',
            'Imperial teaspoonUS teaspoon': '*1.201',
            'Imperial teaspooncubic meter': '/168936.0',
            'Imperial teaspoonImperial gallon': '/768.0',
            'Imperial teaspoonImperial quart': '/192.0',
            'Imperial teaspoonImperial pint': '/96.0',
            'Imperial teaspoonImperial cup': '/48.0',
            'Imperial teaspoonImperial tablespoon': '/3.0',
            'Imperial teaspooncubic foot': '/4784.0',
            'Imperial teaspooncubic inch': '/2.768',
            'cubic footliter': '*28.317',
            'cubic footmilliliter': '*28317.0',
            'cubic footfluid ounce': '*958.0',
            'cubic footUS liquid gallon': '*7.481',
            'cubic footUS liquid quart': '*29.922',
            'cubic footUS liquid pint': '*59.844',
            'cubic footUS legal cup': '*118.0',
            'cubic footUS tablespoon': '*1915.0',
            'cubic footUS teaspoon': '*5745.0',
            'cubic footcubic meter': '/35.315',
            'cubic footImperial gallon': '*6.229',
            'cubic footImperial quart': '*24.915',
            'cubic footImperial pint': '*49.831',
            'cubic footImperial cup': '*99.661',
            'cubic footImperial tablespoon': '*1595.0',
            'cubic footImperial teaspoon': '*4784.0',
            'cubic footcubic inch': '*1728.0',
            'cubic inchliter': '/61.024',
            'cubic inchmilliliter': '*16.387',
            'cubic inchfluid ounce': '/1.805',
            'cubic inchUS liquid gallon': '/231.0',
            'cubic inchUS liquid quart': '/57.75',
            'cubic inchUS liquid pint': '/28.875',
            'cubic inchUS legal cup': '/14.646',
            'cubic inchUS tablespoon': '*1.108',
            'cubic inchUS teaspoon': '*3.325',
            'cubic inchcubic meter': '/61024.0',
            'cubic inchImperial gallon': '/277.0',
            'cubic inchImperial quart': '/69.355',
            'cubic inchImperial pint': '/34.677',
            'cubic inchImperial cup': '/17.339',
            'cubic inchImperial tablespoon': '/1.084',
            'cubic inchImperial teaspoon': '*2.768',
            'cubic inchcubic foot': '/1728.0',
            'literliter': '*1',
            'millilitermilliliter': '*1',
            'fluid ouncefluid ounce': '*1',
            'US liquid gallonUS liquid gallon': '*1',
            'US liquid quartUS liquid quart': '*1',
            'US liquid pintUS liquid pint': '*1',
            'US legal cupUS legal cup': '*1',
            'US tablespoonUS tablespoon': '*1',
            'US teaspoonUS teaspoon': '*1',
            'cubic metercubic meter': '*1',
            'Imperial gallonImperial gallon': '*1',
            'Imperial quartImperial quart': '*1',
            'Imperial pintImperial pint': '*1',
            'Imperial cupImperial cup': '*1',
            'Imperial tablespoonImperial tablespoon': '*1',
            'Imperial teaspoonImperial teaspoon': '*1',
            'cubic footcubic foot': '*1',
            'cubic inchcubic inch': '*1'
        }
        
        conv = eval('%s %s' % (float(volume_entry), volume[volume_unit1 + volume_unit2]))

        answer = builder.get_object('volume-answer')
        answer.set_text(str(conv))
        answer_sci = builder.get_object('volume-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))

    def on_massequals_pressed(self, button):
        mass_entry = builder.get_object('mass-entry').get_text()
        mass_unit1 = builder.get_object('mass-unit1').get_text()
        mass_unit2 = builder.get_object('mass-unit2').get_text()
        
        mass ={
            'kilogramtonne': '/1000.0',
            'kilogramgram': '*1000.0',
            'kilogrammilligram': '*(10.0**6)',
            'kilogrammicrogram': '*(10.0**9)',
            'kilogramImperial ton': '/1016.0',
            'kilogramUS ton': '/907.0',
            'kilogramstone': '/6.35',
            'kilogrampound': '*2.205',
            'kilogramounce': '*35.274',
            'tonnekilogram': '*1000.0',
            'tonnegram': '*(10.0**6)',
            'tonnemilligram': '*(10.0**9)',
            'tonnemicrogram': '*(10.0**12)',
            'tonneImperial ton': '/1.016',
            'tonneUS ton': '*1.102',
            'tonnestone': '*157.0',
            'tonnepound': '*2205.0',
            'tonneounce': '*35274.0',
            'gramkilogram': '/1000.0',
            'gramtonne': '/(10.0**6)',
            'grammilligram': '*1000.0',
            'grammicrogram': '*(10.0**6)',
            'gramImperial ton': '/(1.016*(10**6))',
            'gramUS ton': '/907185.0',
            'gramstone': '/6350.0',
            'grampound': '/454.0',
            'gramounce': '28.35',
            'milligramkilogram': '/(10.0**6)',
            'milligramtonne': '/(10.0**9)',
            'milligramgram': '/1000.0',
            'milligrammicrogram': '*1000.0',
            'milligramImperial ton': '/(1.016*(10**9))',
            'milligramUS ton': '/(9.072*(10**8))',
            'milligramstone': '/(6.35*(10**6))',
            'milligrampound': '/453592.0',
            'milligramounce': '/28350.0',
            'microgramkilogram': '/(10.0**9)',
            'microgramtonne': '/(10.0**12)',
            'microgramgram': '(10.0**6)',
            'microgrammilligram': '/1000.0',
            'microgramImperial ton': '/(1.016*(10**12))',
            'microgramUS ton': '/(9.072*(10**11))',
            'microgramstone': '/(6.35*(10**9))',
            'microgrampound': '/(4.536*(10**8))',
            'microgramounce': '/(2.835*(10**7))',
            'Imperial tonkilogram': '*1016.0',
            'Imperial tontonne': '*1.016',
            'Imperial tongram': '*(1.016*(10.0**6))',
            'Imperial tonmilligram': '*(1.016*(10.0**9))',
            'Imperial tonmicrogram': '*(1.016*(10**12)',
            'Imperial tonUS ton': '*1.12',
            'Imperial tonstone': '*160.0',
            'Imperial tonpound': '*2240.0',
            'Imperial tonounce': '*35840.0',
            'US tonkilogram': '*907.0',
            'US tontonne': '/1.102',
            'US tongram': '*907185.0',
            'US tonmilligram': '*(9.072*(10.0**8))',
            'US tonmicrogram': '*(9.072*(10.0**11))',
            'US tonImperial ton': '/1.12',
            'US tonstone': '*143.0',
            'US tonpound': '*2000.0',
            'US tonounce': '*32000.0',
            'stonekilogram': '*6.35',
            'stonetonne': '/157.0',
            'stonegram': '*6350.0',
            'stonemilligram': '*(6.35*(10.0**6))',
            'stonemicrogram': '*(6.35*(10.0**9))',
            'stoneImperial ton': '/160.0',
            'stoneUS ton': '/143.0',
            'stonepound': '*14.0',
            'stoneounce': '*224.0',
            'poundkilogram': '/2.205',
            'poundtonne': '/2205.0',
            'poundgram': '*454.0',
            'poundmilligram': '*453592.0',
            'poundmicrogram': '*(4.536*(10.0**8))',
            'poundImperial ton': '/2240.0',
            'poundUS ton': '/2000.0',
            'poundstone': '/14.0',
            'poundounce': '*16.0',
            'ouncekilogram': '/35.274',
            'ouncetonne': '/35274.0',
            'ouncegram': '*28.35',
            'ouncemilligram': '*28350.0',
            'ouncemicrogram': '*(2.835*(10.0**7))',
            'ounceImperial ton': '/35840.0',
            'ounceUS ton': '/32000.0',
            'ouncestone': '/224.0',
            'ouncepound': '/16.0',
            'kilogramkilogram': '*1',
            'tonnetonne': '*1',
            'gramgram': '*1',
            'milligrammilligram': '*1',
            'microgrammicrogram': '*1',
            'Imperial tonImperial ton': '*1',
            'US tonUS ton': '*1',
            'stonestone': '*1',
            'poundpound': '*1',
            'ounceounce': '*1'
        }

        conv = eval('%s %s' % (float(mass_entry), mass[mass_unit1 + mass_unit2]))
        
        answer = builder.get_object('mass-answer')
        answer.set_text(str(conv))
        answer_sci = builder.get_object('mass-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))

    def on_speedequals_pressed(self, button):
        speed_entry = builder.get_object('speed-entry').get_text()
        speed_unit1 = builder.get_object('speed-unit1').get_text()
        speed_unit2 = builder.get_object('speed-unit2').get_text()
        
        speed = {
            'miles per hourfeet per second': '*1.467',
            'miles per hourmeter per second': '/2.237',
            'miles per hourkilometer per hour': '*1.609',
            'miles per hourknot': '/1.151',
            'feet per secondmiles per hour': '/1.467',
            'feet per secondmeter per second': '/3.281',
            'feet per secondkilometer per hour': '*1.097',
            'feet per secondknot': '/1.688',
            'meter per secondmiles per hour': '*2.237',
            'meter per secondfeet per second': '*3.281',
            'meter per secondkilometer per hour': '*3.6',
            'meter per secondknot': '*1.944',
            'kilometer per hourmiles per hour': '/1.609',
            'kilometer per hourfeet per second': '/1.097',
            'kilometer per hourmeter per second': '/3.6',
            'kilometer per hourknot': '/1.852',
            'knotmiles per hour': '*1.151',
            'knotfeet per second': '*1.688',
            'knotmeter per second': '/1.944',
            'knotkilometer per hour': '*1.852',
            'miles per hourmiles per hour': '*1',
            'feet per secondfeet per second': '*1',
            'meter per secondmeter per second': '*1',
            'kilometer per hourkilometer per hour': '*1',
            'knotknot': '*1'

        }
        
        conv = eval('%s %s' % (float(speed_entry), speed[speed_unit1 + speed_unit2]))
        
        answer = builder.get_object('speed-answe')
        answer.set_text(str(conv))
        answer_sci = builder.get_object('speed-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))

    def on_energyequals_pressed(self, button):
        energy_entry = builder.get_object('energy-entry').get_text()
        energy_unit1 = builder.get_object('energy-unit1').get_text()
        energy_unit2 = builder.get_object('energy-unit2').get_text()
        
        energy = {
            'joulekilojoule': '/1000.0',
            'joulegramcalorie': '/4.184',
            'joulekilocalorie': '/4184.0',
            'joulewatt hour': '/3600.0',
            'joulekilowatt hour': '/(3.6*(10**6))',
            'jouleelectron volt': '*(6.242*(10**18))',
            'jouleBritish thermal unit': '/1055.0',
            'jouleUS therm': '/(1.055*(10**8))',
            'joulefoot-pound': '/1.356',
            'kilojoulejoule': '*1000.0',
            'kilojoulegramcalorie': '*239.0',
            'kilojoulekilocalorie': '/4.184',
            'kilojoulewatt hour': '/3.6',
            'kilojoulekilowatt hour': '/3600.0',
            'kilojouleelectron volt': '*(6.242*(10**21))',
            'kilojouleBritish thermal unit': '/1.055',
            'kilojouleUS therm': '/105480.0',
            'kilojoulefoot-pound': '*738.0',
            'gramcaloriejoule': '*4.184',
            'gramcaloriekilojoule': '/239.0',
            'gramcaloriekilocalorie': '/1000.0',
            'gramcaloriewatt hour': '860.0',
            'gramcaloriekilowatt hour': '/860421.0',
            'gramcalorieelectron volt': '*(2.611*(10**19)',
            'gramcalorieBritish thermal unit': '/252.0',
            'gramcalorieUS therm': '/(2.521*(10**7))',
            'gramcaloriefoot-pound': '*3.086',
            'kilocaloriejoule': '*4184.0',
            'kilocaloriekilojoule': '*4.184',
            'kilocaloriegramcalorie': '*1000.0',
            'kilocaloriewatt hour': '*1.162',
            'kilocaloriekilowatt hour': '/860.0',
            'kilocalorieelectron volt': '*(2.611*(10**22))',
            'kilocalorieBritish thermal unit': '*3.966',
            'kilocalorieUS therm': '/25210.0',
            'kilocaloriefoot-pound': '*3086.0',
            'watt hourjoule': '*3600.0',
            'watt hourjoule': '*3.6',
            'watt hourgramcalorie': '*860.0',
            'watt hourkilocalorie': '/1.162',
            'watt hourkilowatt hour': '/1000.0',
            'watt hourelectron volt': '*(2.247*(10**22))',
            'watt hourBritish thermal unit': '*3.412',
            'watt hourUS therm': '/29300.0',
            'watt hourfoot-pound': '*2655.0',
            'kilowatt hourjoule': '*(3.6*(10**6))',
            'kilowatt hourkilojoule': '*3600.0',
            'kilowatt hourgramcalorie': '*860421.0',
            'kilowatt hourkilocalorie': '*860.0',
            'kilowatt hourwatt hour': '*1000.0',
            'kilowatt hourelectron volt': '*(2.247*(10**25))',
            'kilowatt hourBritish thermal unit': '*3412.0',
            'kilowatt hourUS therm': '/29.3',
            'kilowatt hourfoot-pound': '*(2.655*(10**6))',
            'electron voltjoule': '/(6.242*(10**18))',
            'electron voltkilojoule': '/(6.242*(10**21))',
            'electron voltgramcalorie': '/(2.611*(10**19))',
            'electron voltkilocalorie': '/(2.611*(10**22))',
            'electron voltwatt hour': '/(2.247*(10**22))',
            'electron voltkilowatt hour': '/(2.247*(10**25))',
            'electron voltBritish thermal unit': '/(6.585*(10**21))',
            'electron voltUS therm': '/(6.584*(10**26))',
            'electron voltfoot-pound': '/(8.462*(10**18))',
            'British thermal unitjoule': '*1055.0',
            'British thermal unitkilojoule': '*1.055',
            'British thermal unitgramcalorie': '*252.0',
            'British thermal unitkilocalorie': '/3.966',
            'British thermal unitwatt hour': '/3.412',
            'British thermal unitkilowatt hour': '/3412.0',
            'British thermal unitelectron volt': '*(6.585*(10**21))',
            'British thermal unitUS therm': '/99976.0',
            'British thermal unitfoot-pound': '*778.0',
            'US thermjoule': '*(1.055*(10**8))',
            'US thermkilojoule': '*105480.0',
            'US thermgramcalorie': '*105480.0',
            'US thermkilocalorie': '*25210.0',
            'US thermwatt hour': '*29300.0',
            'US thermkilowatt hour': '*29.3',
            'US thermelectron volt': '*(6.584*(10**26))',
            'US thermBritish thermal unit': '*99976.0',
            'US thermfoot-pound': '*(7.78*(10**7))',
            'foot-poundjoule': '*1.356',
            'foot-poundkilojoule': '/738.0',
            'foot-poundgramcalorie': '/3.086',
            'foot-poundkilocalorie': '/3086.0',
            'foot-poundwatt hour': '/2655.0',
            'foot-poundkilowatt hour': '/(2.655*(10**6))',
            'foot-poundelectron volt': '*(8.462*(10**18))',
            'foot-poundBritish thermal unit': '/778.0',
            'foot-poundUS therm': '/(7.78*(10**7))',
            'joulejoule': '*1',
            'kilojoulekilojoule': '*1',
            'gramcaloriegramcalorie': '*1',
            'kilocaloriekilocalorie': '*1',
            'watt hourwatt hour': '*1',
            'kilowatt hourkilowatt hour': '*1',
            'electron voltelectron volt': '*1',
            'British thermal unitBritish thermal unit': '*1',
            'US thermUS therm': '*1',
            'foot-poundfoot-pound': '*1'
        }

        conv = eval('%s %s' % (float(energy_entry), energy[energy_unit1 + energy_unit2]))
        
        answer = builder.get_object('energy-answer')
        answer.set_text(str(conv))
        answer_sci = builder.get_object('energy-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))

    def on_pressureequals_pressed(self, button):
        pressure_entry = builder.get_object('pressure-entry').get_text()
        pressure_unit1 = builder.get_object('pressure-unit1').get_text()
        pressure_unit2 = builder.get_object('pressure-unit2').get_text()
        
        pressure = {
            'barpascal': '*100000.0',
            'barpound per square inch': '*14.504',
            'barstandard atmosphere': '/1.013 ',
            'bartorr': '*750.0 ',
            'pascalbar': '/100000.0',
            'pascalpound per square inch': '/6895.0',
            'pascalstandard atmosphere': '/101325.0',
            'pascaltorr': '/133.0',
            'pound per square inchbar': '/14.504',
            'pound per square inchpascal': '*6895.0',
            'pound per square inchstandard atmosphere': '/14.696',
            'pound per square inchtorr': '*51.715',
            'standard atmospherebar':'*1.013',
            'standard atmospherepascal':'*101325.0',
            'standard atmospherepound per square inch':'*14.696',
            'standard atmospheretorr':'*760',
            'torrbar': '/750.0',
            'torrpascal': '*133.0',
            'torrpound per square inch': '/51.715',
            'torrstandard atmosphere': '/760.0',
            'barbar': '*1',
            'pascalpascal': '*1',
            'pound per square inchpound per square inch': '*1',
            'standard atmospherestandard atmosphere': '*1',
            'torrtorr': '*1'

        }

        conv = eval('%s %s' % (float(pressure_entry), pressure[pressure_unit1 + pressure_unit2]))
        
        answer = builder.get_object('pressure-answer')
        answer.set_text(str(conv))
        answer_sci = builder.get_object('pressure-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))

    def on_timeequals_pressed(self, button):
        time_entry = builder.get_object('time-entry').get_text()
        time_unit1 = builder.get_object('time-unit1').get_text()
        time_unit2 = builder.get_object('time-unit2').get_text()

        time = {
            'nanosecondmicrosecond': '/1000',
            'nanosecondmillisecond': '/1e+6',
            'nanosecondsecond': '/1e+9',
            'nanosecondminute': '/6e+10',
            'nanosecondhour': '/3.6e+12',
            'nanosecondday': '/8.64e+13',
            'nanosecondweek': '/6.048e+14',
            'nanosecondmonth': '/2.628e+15',
            'nanosecondcalendar year': '/3.154e+16',
            'nanoseconddecade': '/3.154e+17',
            'nanosecondcentury': '/3.154e+18',
            'microsecondnanosecond': '*1000',
            'microsecondmillisecond': '/1000',
            'microsecondsecond': '/1e+6',
            'microsecondminute': '/6e+7',
            'microsecondhour': '/3.6e+9',
            'microsecondday': '/8.64e+10',
            'microsecondweek': '/6.048e+11',
            'microsecondmonth': '/2.628+12',
            'microsecondcalendar year': '/3.154e+13',
            'microseconddecade': '/3.154e+14',
            'microsecondcentury': '/3.154e+15',
            'millisecondnanosecond': '*1e+6',
            'millisecondmicrosecond': '*1000',
            'millisecondsecond': '/1000',
            'millisecondminute': '/60000',
            'millisecondhour': '/3.6e+6',
            'millisecondday': '/8.64e+7',
            'millisecondweek': '/6.048e+8',
            'millisecondmonth': '/2.628e+9',
            'millisecondcalendar year': '/3.154e+10',
            'milliseconddecade': '/3.154e+11',
            'millisecondcentury': '/3.154+12',
            'secondnanosecond': '*1e+9',
            'secondmicrosecond': '*1e+6',
            'secondmillisecond': '*1000',
            'secondminute': '*60',
            'secondhour': '/3600',
            'secondday': '/86400',
            'secondweek': '/604800',
            'secondmonth': '/2.628e+6',
            'secondcalendar year': '/3.154e+7',
            'seconddecade': '/3.154e+8',
            'secondcentury': '/3.154e+9',
            'minutenanosecond': '*6e+10',
            'minutemicrosecond': '*6e+7',
            'minutemillisecond': '*60000',
            'minutesecond': '*60',
            'minutehour': '/60',
            'minuteday': '/1440',
            'minuteweek': '/10080',
            'minutemonth': '/43800',
            'minutecalendar year': '/525600',
            'minutedecade': '/5.256e+6',
            'minutecentury': '/5.256e+7',
            'nanosecondnanosecond': '*1',
            'microsecondmicrosecond': '*1',
            'millisecondmillisecond': '*1',
            'secondsecond': '*1',
            'minuteminute': '*1',
            'hourhour': '*1',
            'dayday' : '*1',
            'weekweek': '*1',
            'monthmonth': '*1',
            'calendar yearcalendar year': '*1',
            'decadedecade': '*1',
            'centurycentury': '*1'
        }
        conv = eval('%s %s' % (float(time_entry), time[time_unit1 + time_unit2]))
        
        answer = builder.get_object('time-answer')
        answer.set_text(str(conv))
        answer_sci = builder.get_object('time-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))

    def on_tempequals_pressed(self, button):
        temp_entry = builder.get_object('temp-entry').get_text()
        temp_unit1 = builder.get_object('temp-unit1').get_text()
        temp_unit2 = builder.get_object('temp-unit2').get_text()
    
        temp = {
            'CelciusFahrenheit': '*(9/5)+32',
            'CelciusKelvin': '+273.15',
            'FahrenheitCelcius': '-32*(5/9)',
            'FahrenheitKelvin': '-32*(5/9)+273.15',
            'KelvinCelcius': '-273.15',
            'KelvinFahrenheit': '-273.15*(9/5)+32',
            'CelciusCelcius': '*1',
            'FahrenheitFahrenheit': '*1',
            'KelvinKelvin': '*1'
        }
        
        conv = eval('%s %s' % (float(temp_entry), temp[temp_unit1 + temp_unit2]))

        answer = builder.get_object('temp-answer')
        answer.set_text(str(conv))
        answer_sci = builder.get_object('temp-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))

    def on_freqequals_pressed(self, button):
        freq_entry = builder.get_object('freq-entry').get_text()
        freq_unit1 = builder.get_object('freq-unit1').get_text()
        freq_unit2 = builder.get_object('freq-unit2').get_text()
        
        freq = {
            'hertzkilohertz': '/1000',
            'hertzmegahertz': '/1000000',
            'hertzgigahertz': '/1000000000',
            'kilohertzhertz': '*1000',
            'kilohertzmegahertz': '/1000',
            'kilohertzgigahertz': '/1000000',
            'megahertzhertz': '*1000000',
            'megahertzkilohertz': '*1000',
            'megahertzgigahertz': '/1000',
            'gigahertzhertz': '*1000000000',
            'gigahertzkilohertz': '*1000000',
            'gigahertzmegahertz': '*1000',
            'hertzhertz': '*1',
            'kilohertzkilohertz': '*1',
            'megahertzmegahertz': '*1',
            'gigahertzgigahertz': '*1'
        }
     
        conv = eval('%s %s' % (float(freq_entry), freq[freq_unit1 + freq_unit2])) 
        
        answer = builder.get_object('freq-answer')
        answer.set_text(str(conv))
        answer_sci = builder.get_object('freq-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))

    def on_planeequals_pressed(self, button):
        plane_entry = builder.get_object('plane-entry').get_text()
        plane_unit1 = builder.get_object('plane-unit1').get_text()
        plane_unit2 = builder.get_object('plane-unit2').get_text()
        
        plane = {
            'degreegradian': '*(200/180)',
            'degreemilliradian': '*(1000*math.pi)/180',
            'degreeminute of arc': '*60',
            'degreeradian': '*math.pi/180',
            'degreesecond of arc': '*3600',
            'gradiandegree': '*180/200',
            'gradianmilliradian': '*(1000*math.pi)/200',
            'gradianminute of arc': '*54',
            'gradianradian': '*math.pi/200',
            'gradiansecond of arc': '*3240',
            'milliradiandegree': '*180/(1000*math.pi)',
            'milliradiangradian': '*200/(1000*math.pi)',
            'milliradianminute of arc': '*(60*180)/(1000*math.pi)',
            'milliradianradian': '/1000',
            'milliradiansecond of arc': '*(3600*180)/(1000*math.pi)',
            'minute of arcdegree': '/60',
            'minute of arcgradian': '/54',
            'minute of arcmilliradian': '*(1000*math.pi)/(60*180)',
            'minute of arcradian': '*math.pi/(60*180)',
            'minute of arcsecond of arc': '*60',
            'radiandegree': '*180/math.pi',
            'radiangradian': '*200/math.pi',
            'radianmilliradian': '*1000',
            'radianminute of arc': '*(60*180)/math.pi',
            'radiansecond of arc': '*(3600*180)/math.pi',
            'second of arcdegree': '/3600',
            'second of arcgradian': '/3240',
            'second of arcmilliradian': '*(1000*math.pi)/(180*3600)',
            'second of arcminute of arc': '/60',
            'second of arcradian': '*math.pi/(180*3600)',
            'degreedegree': '*1',
            'gradiangradian': '*1',
            'milliradianmilliradian': '*1',
            'minute of arcminute of arc': '*1',
            'radianradian': '*1',
            'second of arcsecond of arc': '*1'
        }
      
        conv = eval('%s %s' % (float(plane_entry), plane[plane_unit1 + plane_unit2]))

        answer = builder.get_object('plane-answer')
        answer.set_text(str(conv))
        answer_sci = builder.get_object('plane-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))
    
    def on_fuelequals_pressed(self, button):
        fuel_entry = builder.get_object('fuel-entry').get_text()
        fuel_unit1 = builder.get_object('fuel-unit1').get_text()
        fuel_unit2 = builder.get_object('fuel-unit2').get_text()
        #from kilometer per liter
        if  fuel_unit1 == 'kilometer per liter' and fuel_unit2 == 'miles per gallon':
            conv = float(fuel_entry)*2.352
        elif fuel_unit1 == 'kilometer per liter' and fuel_unit2 == 'liter per 100 kilometer':
            conv = 100/float(fuel_entry)
        #from miles per gallon
        elif fuel_unit1 == 'miles per gallon' and fuel_unit2 == 'kilometer per liter':
            conv = float(fuel_entry)/2.352
        elif fuel_unit1 == 'miles per gallon' and fuel_unit2 == 'liter per 100 kilometer':
            conv = float(fuel_entry)*235.215
        #from liter per 100 kilometer
        elif fuel_unit1 == 'liter per 100 kilometer' and fuel_unit2 == 'kilometer per liter':
            conv = 100/float(fuel_entry)
        elif fuel_unit1 == 'liter per 100 kilometer' and fuel_unit2 == 'miles per gallon':
            conv = 235.215/float(fuel_entry)
        else:
            conv = fuel_entry
        answer = builder.get_object('fuel-answer')
        answer.set_text(str(conv))
        answer_sci = builder.get_object('fuel-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))

    def on_areaequals_pressed(self, button):
        area_entry = builder.get_object('area-entry').get_text()
        area_unit1 = builder.get_object('area-unit1').get_text()
        area_unit2 = builder.get_object('area-unit2').get_text()
        
        area = {
            'square kilometersquare meter': '/1e+6',
            'square kilometersquare yard': '*1.196e+6',
            'square kilometersquare feet': '*1.076e+7',
            'square kilometersquare inch': '*1.55e+9',
            'square kilometerhectare': '*100',
            'square kilometeracre': '*247.105',
            'square metersquare kilometer': '/1e-6',
            'square metersquare yard': '*1.19599',
            'square metersquare feet': '*10.764',
            'square metersquare inch': '*1550',
            'square meterhectare': '/10000',
            'square meteracre': '/4047',
            'square yardsquare kilometer': '/1.196e+6',
            'square yardsquare meter': '/1.196',
            'square yardsquare feet': '*9',
            'square yardsquare inch': '*1296',
            'square yardhectare': '/11960',
            'square yardacre': '/4840',
            'square feetsquare kilometer': '/1.076e+7',
            'square feetsquare meter': '/10.764',
            'square feetsquare yard': '/9',
            'square feetsquare inch': '*144',
            'square feethectare': '107639',
            'square feetacre': '/43560',
            'square inchsquare kilometer': '/1.55e+9',
            'square inchsquare meter': '/1550',
            'square inchsquare yard': '/1296',
            'square inchsquare feet': '/144',
            'square inchhectare': '/1.55e+7',
            'square inchacre': '/6.273e+6',
            'hectaresquare kilometer': '/100',
            'hectaresquare meter': '*10000',
            'hectaresquare yard': '*11960',
            'hectaresquare inch': '*1.55e+7',
            'hectaresquare feet': '*107639',
            'hectareacre': '*2.471',
            'acresquare kilometer': '/247',
            'acresquare meter': '*4047',
            'acresquare yard': '*4840',
            'acresquare feet': '*43560',
            'acresquare inch': '*6.27e+6',
            'acrehectare': '/2.471',
            'square kilometersquare kilometer': '*1',
            'square metersquare meter': '*1',
            'square yardsquare yard': '*1',
            'square feetsquare feet': '*1',
            'square inchsquare inch': '*1',
            'hectarehectare': '*1',
            'acreacre': '*1'
        }

        conv = eval('%s %s' % (float(area_entry), area[area_unit1 + area_unit2]))

        answer = builder.get_object('area-answer')
        answer.set_text(str(conv))
        answer_sci = builder.get_object('area-scinot-answer')
        answer_sci.set_text(str("{:.3e}".format(conv)))

    stack = gtk.Stack()
    stack_switcher = gtk.StackSwitcher()
    stack_switcher.set_stack(stack)

builder = gtk.Builder()
builder.add_from_file("GUI-MAIC.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

gtk.main()