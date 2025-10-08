#
# PySNMP MIB module CUBRO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cubro/CUBRO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cubro_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32182)).setLabel("cubro-MIB")
cubro_MIB.setRevisions(('2016-10-18 00:00',))
if mibBuilder.loadTexts: cubro_MIB.setLastUpdated('201610180000Z')
if mibBuilder.loadTexts: cubro_MIB.setOrganization('Cubro Acronet GsmbH')
packetmasterEX = MibIdentifier((1, 3, 6, 1, 4, 1, 32182, 1))
environment = MibIdentifier((1, 3, 6, 1, 4, 1, 32182, 1, 1))
psu = MibIdentifier((1, 3, 6, 1, 4, 1, 32182, 1, 1, 1))
temperature = MibIdentifier((1, 3, 6, 1, 4, 1, 32182, 1, 1, 2))
fan = MibIdentifier((1, 3, 6, 1, 4, 1, 32182, 1, 1, 3))
transceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4))
class EXPSUIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

psuNumber = MibScalar((1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psuNumber.setStatus('current')
psuTable = MibTable((1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2), )
if mibBuilder.loadTexts: psuTable.setStatus('current')
psuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1), ).setIndexNames((0, "CUBRO-MIB", "psuIndex"))
if mibBuilder.loadTexts: psuEntry.setStatus('current')
psuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1, 1), EXPSUIndex())
if mibBuilder.loadTexts: psuIndex.setStatus('current')
psuPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psuPresent.setStatus('current')
psuPower = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psuPower.setStatus('current')
psuType = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psuType.setStatus('current')
psuAlert = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psuAlert.setStatus('current')
class EXTEMPIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

tempNumber = MibScalar((1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempNumber.setStatus('current')
tempTable = MibTable((1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2), )
if mibBuilder.loadTexts: tempTable.setStatus('current')
tempEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1), ).setIndexNames((0, "CUBRO-MIB", "tempIndex"))
if mibBuilder.loadTexts: tempEntry.setStatus('current')
tempIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 1), EXTEMPIndex())
if mibBuilder.loadTexts: tempIndex.setStatus('current')
tempTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempTemp.setStatus('current')
tempLowerAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempLowerAlarm.setStatus('current')
tempHighAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempHighAlarm.setStatus('current')
tempCriticalLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempCriticalLimit.setStatus('current')
tempPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tempPosition.setStatus('current')
class EXFANIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

fanNumber = MibScalar((1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanNumber.setStatus('current')
fanTable = MibTable((1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2), )
if mibBuilder.loadTexts: fanTable.setStatus('current')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2, 1), ).setIndexNames((0, "CUBRO-MIB", "fanIndex"))
if mibBuilder.loadTexts: fanEntry.setStatus('current')
fanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2, 1, 1), EXFANIndex())
if mibBuilder.loadTexts: fanIndex.setStatus('current')
fanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStatus.setStatus('current')
fanSpeedRate = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanSpeedRate.setStatus('current')
fanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanMode.setStatus('current')
class EXTransceiverIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

transceiverNumber = MibScalar((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: transceiverNumber.setStatus('current')
transceiverTable = MibTable((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2), )
if mibBuilder.loadTexts: transceiverTable.setStatus('current')
transceiverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1), ).setIndexNames((0, "CUBRO-MIB", "transIndex"))
if mibBuilder.loadTexts: transceiverEntry.setStatus('current')
transIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 1), EXTransceiverIndex())
if mibBuilder.loadTexts: transIndex.setStatus('current')
transName = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transName.setStatus('current')
transDiagnosticImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transDiagnosticImplemented.setStatus('current')
transOpticalTransmitPower = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transOpticalTransmitPower.setStatus('current')
transOpticalTransmitHighAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transOpticalTransmitHighAlarm.setStatus('current')
transOpticalTransmitHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transOpticalTransmitHighWarn.setStatus('current')
transOpticalTransmitLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transOpticalTransmitLowWarn.setStatus('current')
transOpticalTransmitLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transOpticalTransmitLowAlarm.setStatus('current')
transOpticalReceivePower = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transOpticalReceivePower.setStatus('current')
transOpticalReceiveHighAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transOpticalReceiveHighAlarm.setStatus('current')
transOpticalReceiveHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transOpticalReceiveHighWarn.setStatus('current')
transOpticalReceiveLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transOpticalReceiveLowWarn.setStatus('current')
transOpticalReceiveLowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transOpticalReceiveLowAlarm.setStatus('current')
envConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 32182, 1, 1, 10))
envGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 1))
envCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 2))
envCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 2, 1)).setObjects(("CUBRO-MIB", "envTempGroup"), ("CUBRO-MIB", "envPSUGroup"), ("CUBRO-MIB", "envTempGroup"), ("CUBRO-MIB", "envFanGroup"), ("CUBRO-MIB", "transmitterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    envCompliance = envCompliance.setStatus('current')
envPSUGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 1, 1)).setObjects(("CUBRO-MIB", "psuNumber"), ("CUBRO-MIB", "psuPresent"), ("CUBRO-MIB", "psuPower"), ("CUBRO-MIB", "psuType"), ("CUBRO-MIB", "psuAlert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    envPSUGroup = envPSUGroup.setStatus('current')
envTempGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 1, 2)).setObjects(("CUBRO-MIB", "tempNumber"), ("CUBRO-MIB", "tempTemp"), ("CUBRO-MIB", "tempLowerAlarm"), ("CUBRO-MIB", "tempHighAlarm"), ("CUBRO-MIB", "tempCriticalLimit"), ("CUBRO-MIB", "tempPosition"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    envTempGroup = envTempGroup.setStatus('current')
envFanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 1, 3)).setObjects(("CUBRO-MIB", "fanNumber"), ("CUBRO-MIB", "fanStatus"), ("CUBRO-MIB", "fanSpeedRate"), ("CUBRO-MIB", "fanMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    envFanGroup = envFanGroup.setStatus('current')
transmitterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 1, 4)).setObjects(("CUBRO-MIB", "transceiverNumber"), ("CUBRO-MIB", "transName"), ("CUBRO-MIB", "transDiagnosticImplemented"), ("CUBRO-MIB", "transOpticalTransmitPower"), ("CUBRO-MIB", "transOpticalTransmitHighAlarm"), ("CUBRO-MIB", "transOpticalTransmitHighWarn"), ("CUBRO-MIB", "transOpticalTransmitLowWarn"), ("CUBRO-MIB", "transOpticalTransmitLowAlarm"), ("CUBRO-MIB", "transOpticalReceivePower"), ("CUBRO-MIB", "transOpticalReceiveHighAlarm"), ("CUBRO-MIB", "transOpticalReceiveHighWarn"), ("CUBRO-MIB", "transOpticalReceiveLowWarn"), ("CUBRO-MIB", "transOpticalReceiveLowAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    transmitterGroup = transmitterGroup.setStatus('current')
mibBuilder.exportSymbols("CUBRO-MIB", envPSUGroup=envPSUGroup, psuEntry=psuEntry, PYSNMP_MODULE_ID=cubro_MIB, transOpticalReceiveHighAlarm=transOpticalReceiveHighAlarm, transOpticalReceiveHighWarn=transOpticalReceiveHighWarn, transName=transName, tempLowerAlarm=tempLowerAlarm, transOpticalTransmitHighWarn=transOpticalTransmitHighWarn, tempTemp=tempTemp, transceiverEntry=transceiverEntry, transOpticalReceivePower=transOpticalReceivePower, tempHighAlarm=tempHighAlarm, fanEntry=fanEntry, psuPresent=psuPresent, transmitterGroup=transmitterGroup, transceiverNumber=transceiverNumber, tempPosition=tempPosition, fanMode=fanMode, psuIndex=psuIndex, EXFANIndex=EXFANIndex, fanStatus=fanStatus, psuType=psuType, envFanGroup=envFanGroup, cubro_MIB=cubro_MIB, transDiagnosticImplemented=transDiagnosticImplemented, temperature=temperature, EXTransceiverIndex=EXTransceiverIndex, transOpticalTransmitLowAlarm=transOpticalTransmitLowAlarm, envGroups=envGroups, psuAlert=psuAlert, packetmasterEX=packetmasterEX, transOpticalTransmitLowWarn=transOpticalTransmitLowWarn, transOpticalTransmitPower=transOpticalTransmitPower, psu=psu, envConformance=envConformance, envTempGroup=envTempGroup, transOpticalTransmitHighAlarm=transOpticalTransmitHighAlarm, transOpticalReceiveLowAlarm=transOpticalReceiveLowAlarm, tempCriticalLimit=tempCriticalLimit, EXPSUIndex=EXPSUIndex, tempEntry=tempEntry, fanNumber=fanNumber, psuTable=psuTable, tempTable=tempTable, tempIndex=tempIndex, fan=fan, fanSpeedRate=fanSpeedRate, transceiverTable=transceiverTable, envCompliance=envCompliance, fanIndex=fanIndex, envCompliances=envCompliances, transIndex=transIndex, transOpticalReceiveLowWarn=transOpticalReceiveLowWarn, psuNumber=psuNumber, fanTable=fanTable, environment=environment, EXTEMPIndex=EXTEMPIndex, tempNumber=tempNumber, transceiver=transceiver, psuPower=psuPower)
