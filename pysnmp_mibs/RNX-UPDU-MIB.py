#
# PySNMP MIB module RNX-UPDU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bachmann/RNX-UPDU-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rnx = ModuleIdentity((1, 3, 6, 1, 4, 1, 55108))
rnx.setRevisions(('2022-07-06 00:00', '2022-06-22 00:00', '2020-12-16 00:00', '2020-06-18 00:00',))
if mibBuilder.loadTexts: rnx.setLastUpdated('202207060000Z')
if mibBuilder.loadTexts: rnx.setOrganization('Riedo Networks Ltd.')
upduMib = MibIdentifier((1, 3, 6, 1, 4, 1, 55108, 1))
class Watts(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class VoltAmpereReactives(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class VoltAmperes(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class WattHours(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class VoltAmpereReactiveHours(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd'

class MilliAmperes(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class TenthMilliAmperes(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class MilliVolts(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class TenthDegreesCelsius(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class Permil(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

upduInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 55108, 1, 1))
upduInventory = MibIdentifier((1, 3, 6, 1, 4, 1, 55108, 1, 2))
upduMeasurements = MibIdentifier((1, 3, 6, 1, 4, 1, 55108, 1, 3))
upduControl = MibIdentifier((1, 3, 6, 1, 4, 1, 55108, 1, 4))
upduConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 55108, 1, 5))
upduInfoPartNumber = MibScalar((1, 3, 6, 1, 4, 1, 55108, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduInfoPartNumber.setStatus('current')
upduInfoSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 55108, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduInfoSerialNumber.setStatus('current')
upduInfoLotNumber = MibScalar((1, 3, 6, 1, 4, 1, 55108, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduInfoLotNumber.setStatus('current')
upduModuleTable = MibTable((1, 3, 6, 1, 4, 1, 55108, 1, 2, 1), )
if mibBuilder.loadTexts: upduModuleTable.setStatus('current')
upduModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1), ).setIndexNames((0, "RNX-UPDU-MIB", "upduModuleIndex"))
if mibBuilder.loadTexts: upduModuleEntry.setStatus('current')
upduModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8)))
if mibBuilder.loadTexts: upduModuleIndex.setStatus('current')
upduModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("icm", 1), ("meterModule", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduModuleType.setStatus('current')
upduModulePartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduModulePartNumber.setStatus('current')
upduModuleSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduModuleSerialNumber.setStatus('current')
upduModuleLotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduModuleLotNumber.setStatus('current')
upduMeterTable = MibTable((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1), )
if mibBuilder.loadTexts: upduMeterTable.setStatus('current')
upduMeterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1), ).setIndexNames((0, "RNX-UPDU-MIB", "upduModuleIndex"), (0, "RNX-UPDU-MIB", "upduMeterIndex"))
if mibBuilder.loadTexts: upduMeterEntry.setStatus('current')
upduMeterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 11)))
if mibBuilder.loadTexts: upduMeterIndex.setStatus('current')
upduMeterName = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduMeterName.setStatus('current')
upduMeterType = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("pduTotal", 0), ("pduTotalCalc", 1), ("phaseTotal", 2), ("phaseTotalCalc", 3), ("moduleTotal", 4), ("moduleTotalCalc", 5), ("outlet", 6), ("outletGroup", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduMeterType.setStatus('current')
upduMeterEnergyP = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 4), WattHours()).setUnits('Wh').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduMeterEnergyP.setStatus('current')
upduMeterEnergyR1 = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 5), VoltAmpereReactiveHours()).setUnits('varh').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduMeterEnergyR1.setStatus('current')
upduMeterEnergyR4 = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 6), VoltAmpereReactiveHours()).setUnits('varh').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduMeterEnergyR4.setStatus('current')
upduMeterPowerP = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 7), Watts()).setUnits('W').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduMeterPowerP.setStatus('current')
upduMeterPowerQ = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 8), VoltAmpereReactives()).setUnits('var').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduMeterPowerQ.setStatus('current')
upduMeterPowerS = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 9), VoltAmperes()).setUnits('VA').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduMeterPowerS.setStatus('current')
upduMeterUrms = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 10), MilliVolts()).setUnits('mV').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduMeterUrms.setStatus('current')
upduMeterIrms = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 11), MilliAmperes()).setUnits('mA').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduMeterIrms.setStatus('current')
upduMeterSystemName = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduMeterSystemName.setStatus('current')
upduMeterCustomName = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upduMeterCustomName.setStatus('current')
upduMeterDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upduMeterDescription.setStatus('current')
upduSensorTable = MibTable((1, 3, 6, 1, 4, 1, 55108, 1, 3, 2), )
if mibBuilder.loadTexts: upduSensorTable.setStatus('current')
upduSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1), ).setIndexNames((0, "RNX-UPDU-MIB", "upduSensorPort"))
if mibBuilder.loadTexts: upduSensorEntry.setStatus('current')
upduSensorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)))
if mibBuilder.loadTexts: upduSensorPort.setStatus('current')
upduSensorPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduSensorPortName.setStatus('current')
upduSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("temp", 1), ("tempHumidity", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduSensorType.setStatus('current')
upduSensorTemperatureCelsius = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1, 4), TenthDegreesCelsius()).setUnits('deg-C/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduSensorTemperatureCelsius.setStatus('current')
upduSensorHumidity = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1, 5), Permil()).setUnits('/1000').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduSensorHumidity.setStatus('current')
upduRcmTable = MibTable((1, 3, 6, 1, 4, 1, 55108, 1, 3, 3), )
if mibBuilder.loadTexts: upduRcmTable.setStatus('current')
upduRcmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1), ).setIndexNames((0, "RNX-UPDU-MIB", "upduModuleIndex"), (0, "RNX-UPDU-MIB", "upduRcmIndex"))
if mibBuilder.loadTexts: upduRcmEntry.setStatus('current')
upduRcmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 11)))
if mibBuilder.loadTexts: upduRcmIndex.setStatus('current')
upduRcmName = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduRcmName.setStatus('current')
upduRcmCurrentRms = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1, 3), TenthMilliAmperes()).setUnits('mA/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduRcmCurrentRms.setStatus('current')
upduRcmCurrentDc = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1, 4), TenthMilliAmperes()).setUnits('mA/10').setMaxAccess("readonly")
if mibBuilder.loadTexts: upduRcmCurrentDc.setStatus('current')
upduRcmSensorQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 0), ("nodata", 1), ("timeout", 2), ("internalerror", 3), ("selftestfailed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduRcmSensorQuality.setStatus('current')
upduRelayTable = MibTable((1, 3, 6, 1, 4, 1, 55108, 1, 4, 1), )
if mibBuilder.loadTexts: upduRelayTable.setStatus('current')
upduRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1), ).setIndexNames((0, "RNX-UPDU-MIB", "upduModuleIndex"), (0, "RNX-UPDU-MIB", "upduRelayIndex"))
if mibBuilder.loadTexts: upduRelayEntry.setStatus('current')
upduRelayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: upduRelayIndex.setStatus('current')
upduRelayMeterNames = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduRelayMeterNames.setStatus('current')
upduRelayAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("unknown", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: upduRelayAdminStatus.setStatus('current')
upduRelayOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("unknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduRelayOperStatus.setStatus('current')
upduRelayCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ok", 0), ("failed", 1), ("unknown", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: upduRelayCondition.setStatus('current')
upduMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 55108, 1, 5, 1))
upduMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 55108, 1, 5, 2))
upduMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 55108, 1, 5, 1, 1)).setObjects(("RNX-UPDU-MIB", "upduMibGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upduMibCompliance = upduMibCompliance.setStatus('current')
upduMibGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 55108, 1, 5, 2, 1)).setObjects(("RNX-UPDU-MIB", "upduInfoPartNumber"), ("RNX-UPDU-MIB", "upduInfoSerialNumber"), ("RNX-UPDU-MIB", "upduInfoLotNumber"), ("RNX-UPDU-MIB", "upduModuleType"), ("RNX-UPDU-MIB", "upduModulePartNumber"), ("RNX-UPDU-MIB", "upduModuleSerialNumber"), ("RNX-UPDU-MIB", "upduModuleLotNumber"), ("RNX-UPDU-MIB", "upduMeterName"), ("RNX-UPDU-MIB", "upduMeterType"), ("RNX-UPDU-MIB", "upduMeterEnergyP"), ("RNX-UPDU-MIB", "upduMeterEnergyR1"), ("RNX-UPDU-MIB", "upduMeterEnergyR4"), ("RNX-UPDU-MIB", "upduMeterPowerP"), ("RNX-UPDU-MIB", "upduMeterPowerQ"), ("RNX-UPDU-MIB", "upduMeterPowerS"), ("RNX-UPDU-MIB", "upduMeterUrms"), ("RNX-UPDU-MIB", "upduMeterIrms"), ("RNX-UPDU-MIB", "upduMeterSystemName"), ("RNX-UPDU-MIB", "upduMeterCustomName"), ("RNX-UPDU-MIB", "upduMeterDescription"), ("RNX-UPDU-MIB", "upduRelayMeterNames"), ("RNX-UPDU-MIB", "upduRelayAdminStatus"), ("RNX-UPDU-MIB", "upduRelayOperStatus"), ("RNX-UPDU-MIB", "upduRelayCondition"), ("RNX-UPDU-MIB", "upduSensorPortName"), ("RNX-UPDU-MIB", "upduSensorType"), ("RNX-UPDU-MIB", "upduSensorTemperatureCelsius"), ("RNX-UPDU-MIB", "upduSensorHumidity"), ("RNX-UPDU-MIB", "upduRcmName"), ("RNX-UPDU-MIB", "upduRcmCurrentRms"), ("RNX-UPDU-MIB", "upduRcmCurrentDc"), ("RNX-UPDU-MIB", "upduRcmSensorQuality"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    upduMibGroupRev1 = upduMibGroupRev1.setStatus('current')
mibBuilder.exportSymbols("RNX-UPDU-MIB", MilliAmperes=MilliAmperes, upduRelayCondition=upduRelayCondition, upduRelayAdminStatus=upduRelayAdminStatus, upduRcmCurrentDc=upduRcmCurrentDc, upduRelayIndex=upduRelayIndex, upduMeterDescription=upduMeterDescription, TenthMilliAmperes=TenthMilliAmperes, upduMeterTable=upduMeterTable, upduMib=upduMib, upduRelayTable=upduRelayTable, upduMeasurements=upduMeasurements, upduMeterPowerQ=upduMeterPowerQ, upduRelayEntry=upduRelayEntry, upduMibCompliances=upduMibCompliances, Watts=Watts, rnx=rnx, upduModuleLotNumber=upduModuleLotNumber, upduMeterType=upduMeterType, upduRcmEntry=upduRcmEntry, upduRelayOperStatus=upduRelayOperStatus, upduSensorPort=upduSensorPort, upduInfoSerialNumber=upduInfoSerialNumber, upduMeterIndex=upduMeterIndex, MilliVolts=MilliVolts, upduRcmCurrentRms=upduRcmCurrentRms, upduMeterEnergyP=upduMeterEnergyP, VoltAmpereReactives=VoltAmpereReactives, upduRcmSensorQuality=upduRcmSensorQuality, upduMibGroupRev1=upduMibGroupRev1, upduInfoPartNumber=upduInfoPartNumber, upduConformance=upduConformance, upduSensorEntry=upduSensorEntry, upduSensorPortName=upduSensorPortName, upduSensorType=upduSensorType, upduRcmName=upduRcmName, upduInventory=upduInventory, upduMeterEnergyR1=upduMeterEnergyR1, upduMeterEntry=upduMeterEntry, upduMeterSystemName=upduMeterSystemName, upduInfo=upduInfo, upduSensorHumidity=upduSensorHumidity, upduModuleSerialNumber=upduModuleSerialNumber, upduSensorTemperatureCelsius=upduSensorTemperatureCelsius, upduModuleTable=upduModuleTable, VoltAmpereReactiveHours=VoltAmpereReactiveHours, VoltAmperes=VoltAmperes, upduRcmIndex=upduRcmIndex, upduMeterName=upduMeterName, WattHours=WattHours, upduModuleEntry=upduModuleEntry, upduMeterUrms=upduMeterUrms, upduModuleIndex=upduModuleIndex, upduControl=upduControl, upduMibCompliance=upduMibCompliance, upduMibGroups=upduMibGroups, upduModuleType=upduModuleType, upduMeterPowerP=upduMeterPowerP, upduRcmTable=upduRcmTable, upduMeterCustomName=upduMeterCustomName, upduRelayMeterNames=upduRelayMeterNames, upduMeterPowerS=upduMeterPowerS, upduSensorTable=upduSensorTable, PYSNMP_MODULE_ID=rnx, TenthDegreesCelsius=TenthDegreesCelsius, Permil=Permil, upduModulePartNumber=upduModulePartNumber, upduInfoLotNumber=upduInfoLotNumber, upduMeterEnergyR4=upduMeterEnergyR4, upduMeterIrms=upduMeterIrms)
