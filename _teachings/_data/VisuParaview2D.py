# trace generated using paraview version 5.10.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
import os
import re
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


pwd = os.getcwd()

for roots,dirs,files in os.walk(pwd+'/dump'):
    for file in files :
        m = re.search('([^\.]*)\.sol\.ptset1\.xmf', file)
        if m :
            fileName = m.group(1)
                
folder = os.path.split(pwd)[1]



# create a new 'Xdmf3ReaderS'
injectionRandomsolptset1xmf = Xdmf3ReaderS(registrationName='InjectionRandom.sol.ptset1.xmf', FileName=[pwd+'/dump/'+fileName+'.sol.ptset1.xmf'])
injectionRandomsolptset1xmf.PointArrays = ['ACTIVATION_STATE', 'DIAMETER', 'DIAMETER_INITIAL', 'DRAG_RELAXATION_TIME', 'EL_GRP_LOCATION', 'FLUID_FRACTION', 'F_DRAG', 'F_MORSE', 'F_MORSE_OVER_F_DRAG', 'GLOBAL_INDEX', 'GLOBAL_PT_INDEX', 'INJECTOR', 'LOCATION', 'MYRANK_IN_CELL', 'NSUBSTEPS', 'PT_GRP_LOCATION', 'RESIDENCE_TIME', 'RE_P', 'RHO', 'SUBDOMAIN_LOCATION', 'TF_GAS', 'U', 'U_GAS', 'VOLUME', 'VOLWEIGHT', 'WEIGHT']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

#changing interaction mode based on data extents
renderView1.CameraPosition = [2.8669257972069317e-06, 6.484424375230446e-08, 10000.0]
renderView1.CameraFocalPoint = [2.8669257972069317e-06, 6.484424375230446e-08, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# get display properties
injectionRandomsolptset1xmfDisplay = GetDisplayProperties(injectionRandomsolptset1xmf, view=renderView1)

# get color transfer function/color map for 'LOCATION'
lOCATIONLUT = GetColorTransferFunction('LOCATION')

# get opacity transfer function/opacity map for 'LOCATION'
lOCATIONPWF = GetOpacityTransferFunction('LOCATION')

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# create a new 'Xdmf3ReaderS'
injectionRandomsolxmf = Xdmf3ReaderS(registrationName='InjectionRandom.sol.xmf', FileName=[pwd+'/dump/'+fileName+'.sol.xmf'])
injectionRandomsolxmf.PointArrays = ['ABS_NODEVOL', 'BND_FLAG', 'DELTA_PAIRBASED', 'LINSOL_POISSON_RHS', 'LINSOL_REAL_ID_RHS', 'MULTIPLICITY', 'NU', 'NUMBER_OF_NEIGHBOURS', 'NU_ARTIF', 'NU_T', 'P_OVER_RHO', 'Q_CRITERION', 'U', 'U_MEAN', 'U_MEAN_CONFIDENCE', 'U_RMS', 'U_STAR', 'VELOCITY_SOURCE', 'VWF', 'VWF_DIFFUSIVITY']
injectionRandomsolxmf.CellArrays = ['PROC_COLOR', 'SKEWNESS', 'SUBDOMAIN_COLOR']

# show data in view
injectionRandomsolxmfDisplay = Show(injectionRandomsolxmf, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'ABS_NODEVOL'
aBS_NODEVOLLUT = GetColorTransferFunction('ABS_NODEVOL')

# get opacity transfer function/opacity map for 'ABS_NODEVOL'
aBS_NODEVOLPWF = GetOpacityTransferFunction('ABS_NODEVOL')

# trace defaults for the display properties.
injectionRandomsolxmfDisplay.Representation = 'Surface'
injectionRandomsolxmfDisplay.ColorArrayName = ['POINTS', 'ABS_NODEVOL']
injectionRandomsolxmfDisplay.LookupTable = aBS_NODEVOLLUT
injectionRandomsolxmfDisplay.SelectTCoordArray = 'None'
injectionRandomsolxmfDisplay.SelectNormalArray = 'None'
injectionRandomsolxmfDisplay.SelectTangentArray = 'None'
injectionRandomsolxmfDisplay.OSPRayScaleArray = 'ABS_NODEVOL'
injectionRandomsolxmfDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
injectionRandomsolxmfDisplay.SelectOrientationVectors = 'U'
injectionRandomsolxmfDisplay.ScaleFactor = 3.000000142492354e-05
injectionRandomsolxmfDisplay.SelectScaleArray = 'ABS_NODEVOL'
injectionRandomsolxmfDisplay.GlyphType = 'Arrow'
injectionRandomsolxmfDisplay.GlyphTableIndexArray = 'ABS_NODEVOL'
injectionRandomsolxmfDisplay.GaussianRadius = 1.500000071246177e-06
injectionRandomsolxmfDisplay.SetScaleArray = ['POINTS', 'ABS_NODEVOL']
injectionRandomsolxmfDisplay.ScaleTransferFunction = 'PiecewiseFunction'
injectionRandomsolxmfDisplay.OpacityArray = ['POINTS', 'ABS_NODEVOL']
injectionRandomsolxmfDisplay.OpacityTransferFunction = 'PiecewiseFunction'
injectionRandomsolxmfDisplay.DataAxesGrid = 'GridAxesRepresentation'
injectionRandomsolxmfDisplay.PolarAxes = 'PolarAxesRepresentation'
injectionRandomsolxmfDisplay.ScalarOpacityFunction = aBS_NODEVOLPWF
injectionRandomsolxmfDisplay.ScalarOpacityUnitDistance = 1.924650421625425e-05
injectionRandomsolxmfDisplay.OpacityArrayName = ['POINTS', 'ABS_NODEVOL']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
injectionRandomsolxmfDisplay.ScaleTransferFunction.Points = [2.0758071910681464e-12, 0.0, 0.5, 0.0, 1.068152510885767e-11, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
injectionRandomsolxmfDisplay.OpacityTransferFunction.Points = [2.0758071910681464e-12, 0.0, 0.5, 0.0, 1.068152510885767e-11, 1.0, 0.5, 0.0]

# show color bar/color legend
injectionRandomsolxmfDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera(False)

# reset view to fit data
renderView1.ResetCamera(True)

# set active source
SetActiveSource(injectionRandomsolptset1xmf)

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=injectionRandomsolptset1xmf,
    GlyphType='Sphere')
glyph1.OrientationArray = ['POINTS', 'EL_GRP_LOCATION']
glyph1.ScaleArray = ['POINTS', 'LOCATION']
glyph1.ScaleFactor = 4.5014594434178434e-06
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'All Points'

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'LOCATION']
glyph1Display.LookupTable = lOCATIONLUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'Normals'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'LOCATION'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'EL_GRP_LOCATION'
glyph1Display.ScaleFactor = 0.0004415894625708461
glyph1Display.SelectScaleArray = 'LOCATION'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'LOCATION'
glyph1Display.GaussianRadius = 2.2079473128542305e-05
glyph1Display.SetScaleArray = ['POINTS', 'LOCATION']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'LOCATION']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [871.0, 0.0, 0.5, 0.0, 981.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [871.0, 0.0, 0.5, 0.0, 981.0, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on glyph1
glyph1.OrientationArray = ['POINTS', 'No orientation array']

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on glyph1
glyph1.ScaleArray = ['POINTS', 'No scale array']

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on glyph1
glyph1.ScaleFactor = 3e-06

# hide data in view
Hide(injectionRandomsolptset1xmf, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'ACTIVATION_STATE'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(lOCATIONLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'ACTIVATION_STATE'
aCTIVATION_STATELUT = GetColorTransferFunction('ACTIVATION_STATE')

# get opacity transfer function/opacity map for 'ACTIVATION_STATE'
aCTIVATION_STATEPWF = GetOpacityTransferFunction('ACTIVATION_STATE')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
aCTIVATION_STATELUT.ApplyPreset('Activation_3-4', False)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
aCTIVATION_STATEPWF.ApplyPreset('Activation_3-4', False)

# set active source
SetActiveSource(injectionRandomsolxmf)

# set scalar coloring
ColorBy(injectionRandomsolxmfDisplay, ('POINTS', 'VWF'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(aBS_NODEVOLLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
injectionRandomsolxmfDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
injectionRandomsolxmfDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'VWF'
vWFLUT = GetColorTransferFunction('VWF')

# get opacity transfer function/opacity map for 'VWF'
vWFPWF = GetOpacityTransferFunction('VWF')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1370, 761)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0001500000071246177, 0.0, 0.0005875497690715627]
renderView1.CameraFocalPoint = [0.0001500000071246177, 0.0, 0.0]
renderView1.CameraParallelScale = 9.249943441685427e-05

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).