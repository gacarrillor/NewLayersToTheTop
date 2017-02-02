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
import os 

# Import the PyQt and QGIS libraries
from qgis.core import QgsMapLayerRegistry, QgsProject
from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QIcon, QAction

# Initialize Qt resources from file resources.py
import resources_rc

class NewLayersToTheTop:

    def __init__( self, iface ):
        self.iface = iface
        self.settings = QSettings()

    def initGui( self ):
        icon = QIcon()
        icon.addFile( ":/plugins/NewLayersToTheTop/default.png", state=QIcon.Off )
        icon.addFile( ":/plugins/NewLayersToTheTop/toTheTop.png", state=QIcon.On )
        self.action = QAction( icon, u"", self.iface.mainWindow() )
        self.action.toggled.connect( self.run )

        self.action.setCheckable( True )
        checked = self.settings.value( "/NewLayersToTheTop/checked", True, type=bool )
        self.action.setChecked( checked )

        self.iface.addToolBarIcon( self.action )
        self.iface.addPluginToMenu( u"New layers to the &top", self.action )

    def unload( self ):
        self.iface.removePluginMenu( u"New layers to the &top", self.action ) 
        self.iface.removeToolBarIcon(self.action)
        if self.action.isChecked():
            QgsMapLayerRegistry.instance().layersAdded.disconnect( self.changeLayerAdditionMode )

    def run( self ):
        checked = self.action.isChecked()
        if checked:
            self.action.setText( u"Click to make new layers to be added to the selected group" )
            QgsMapLayerRegistry.instance().layersAdded.connect( self.changeLayerAdditionMode )
            self.settings.setValue( "/NewLayersToTheTop/checked", True )
            #self.iface.messageBar().pushMessage( "'New layers to the top' (plugin)", u'From now on, new layers will be added to the top of the tree,', 0, 5 )
        else:
            self.action.setText( u"Click to make new layers to be added to the top of the tree" )
            QgsMapLayerRegistry.instance().layersAdded.disconnect( self.changeLayerAdditionMode )
            self.settings.setValue( "/NewLayersToTheTop/checked", False )
            #self.iface.messageBar().pushMessage( "'New layers to the top' (plugin)", u'From now on, new layers will be added to the selected group.', 0, 5 )

    def changeLayerAdditionMode( self, layers ):
        QgsProject.instance().layerTreeRegistryBridge().setLayerInsertionPoint( QgsProject.instance().layerTreeRoot(), 0 )
        # The following line also works. It's almost the same because selecting root makes it the insertion point
        #self.iface.layerTreeView().setCurrentIndex(iface.layerTreeView().layerTreeModel().node2index(QgsProject.instance().layerTreeRoot()))
        
        
