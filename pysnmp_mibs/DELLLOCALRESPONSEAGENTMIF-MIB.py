#
# PySNMP MIB module DELLLOCALRESPONSEAGENTMIF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/DELLLOCALRESPONSEAGENTMIF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:23:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DmiInteger(Integer32):
    pass

class DmiDisplaystring(DisplayString):
    pass

class DmiDate(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(28, 28)
    fixedLength = 28

class DmiComponentIndex(Integer32):
    pass

dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
server = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10890))
localresponseagent = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10890, 3))
dmtfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1))
tComponentid = MibTable((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1), )
if mibBuilder.loadTexts: tComponentid.setStatus('mandatory')
eComponentid = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1), ).setIndexNames((0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eComponentid.setStatus('mandatory')
a1Manufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Manufacturer.setStatus('mandatory')
a1Product = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Product.setStatus('mandatory')
a1Version = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 3), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Version.setStatus('mandatory')
a1SerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 4), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1SerialNumber.setStatus('mandatory')
a1Installation = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 5), DmiDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Installation.setStatus('mandatory')
a1Verify = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("vAnErrorOccurredCheckStatusCode", 0), ("vThisComponentDoesNotExist", 1), ("vTheVerifyIsNotSupported", 2), ("vReserved", 3), ("vThisComponentExistsButTheFunctionalityI", 4), ("vThisComponentExistsButTheFunctionality1", 5), ("vThisComponentExistsAndIsNotFunctioningC", 6), ("vThisComponentExistsAndIsFunctioningCorr", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Verify.setStatus('mandatory')
tActionResponseTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2), )
if mibBuilder.loadTexts: tActionResponseTable.setStatus('mandatory')
eActionResponseTable = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1), ).setIndexNames((0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"), (0, "DELLLOCALRESPONSEAGENTMIF-MIB", "a2Actionname"))
if mibBuilder.loadTexts: eActionResponseTable.setStatus('mandatory')
a2Actionname = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3, 7, 13, 14, 160, 168, 172, 200, 202, 204, 206, 208, 210, 212, 214, 220, 225))).clone(namedValues=NamedValues(("vUnknown", 0), ("vAdaptec-HostAdapterFailed", 3), ("vAdaptec-LogicalUnitFailed", 7), ("vApc-SystemOnLowUtilityPower", 13), ("vApc-SystemOnLowBatteryPower", 14), ("vTemperatureSensorDetectedAFailure", 160), ("vFanSensorDetectedAFailure", 168), ("vVoltageSensorDetectedAFailure", 172), ("vTemperatureSensorWarningDetected", 200), ("vVoltageSensorWarningDetected", 202), ("vFanSensorWarningDetected", 204), ("vCurrentSensorDetectedAFailure", 206), ("vCurrentSensorWarningDetected", 208), ("vPowerSupplyLostRedundancyDetected", 210), ("vPowerSupplyDegradedRedundancyDetected", 212), ("vPowerSupplyDetectedAFailure", 214), ("vChassisIntrusionDetected", 220), ("vLostConnectionToDiskPod", 225)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Actionname.setStatus('mandatory')
a2Actionresponse = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 2), DmiDisplaystring()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a2Actionresponse.setStatus('mandatory')
a2Actionexecute = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 3), DmiDisplaystring()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a2Actionexecute.setStatus('mandatory')
a2Actionsource = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 4), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Actionsource.setStatus('mandatory')
tActionCapabilities = MibTable((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 3), )
if mibBuilder.loadTexts: tActionCapabilities.setStatus('mandatory')
eActionCapabilities = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 3, 1), ).setIndexNames((0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eActionCapabilities.setStatus('mandatory')
a3LraCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 3, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3LraCapabilities.setStatus('mandatory')
tMiftomib = MibTable((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99), )
if mibBuilder.loadTexts: tMiftomib.setStatus('mandatory')
eMiftomib = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1), ).setIndexNames((0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eMiftomib.setStatus('mandatory')
a99DellLocalResponseAgentMib = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a99DellLocalResponseAgentMib.setStatus('mandatory')
a99MibOid = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a99MibOid.setStatus('mandatory')
a99DisableTraps = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1, 3), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a99DisableTraps.setStatus('mandatory')
mibBuilder.exportSymbols("DELLLOCALRESPONSEAGENTMIF-MIB", a2Actionname=a2Actionname, dell=dell, DmiDate=DmiDate, a1SerialNumber=a1SerialNumber, a1Verify=a1Verify, eActionResponseTable=eActionResponseTable, a2Actionexecute=a2Actionexecute, a1Manufacturer=a1Manufacturer, tMiftomib=tMiftomib, a99DisableTraps=a99DisableTraps, eComponentid=eComponentid, a2Actionresponse=a2Actionresponse, tActionCapabilities=tActionCapabilities, a99MibOid=a99MibOid, eMiftomib=eMiftomib, DmiDisplaystring=DmiDisplaystring, a2Actionsource=a2Actionsource, DmiInteger=DmiInteger, a1Installation=a1Installation, a1Product=a1Product, a99DellLocalResponseAgentMib=a99DellLocalResponseAgentMib, server=server, a3LraCapabilities=a3LraCapabilities, tActionResponseTable=tActionResponseTable, dmtfGroups=dmtfGroups, localresponseagent=localresponseagent, eActionCapabilities=eActionCapabilities, DmiComponentIndex=DmiComponentIndex, a1Version=a1Version, tComponentid=tComponentid)
