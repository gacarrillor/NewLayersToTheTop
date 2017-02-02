"""
/***************************************************************************
 NewLayersToTheTop
                                 A QGIS plugin
 Control whether new layers will be added to the selected group (default QGIS behavior) or to the top of the QGIS Layer Tree (aka ToC).
                             -------------------
        begin                : 2017-02-01
        copyright            : (C) 2017 by German Carrillo, GeoTux
        email                : gcarrillo@linuxmail.org
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
def name():
    return "New layers to the top"
def description():
    return "Control whether new layers will be added to the selected group (default QGIS behavior) or to the top of the QGIS Layer Tree (aka ToC)."
def version():
    return "Version 1.0"
def icon():
    return "toTheTop.png"
def qgisMinimumVersion():
    return "2.0"
def classFactory(iface):
    from newLayersToTheTop import NewLayersToTheTop
    return NewLayersToTheTop(iface)
