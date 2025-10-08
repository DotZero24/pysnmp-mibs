#
# PySNMP MIB module ENVIRONMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/ENVIRONMENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntEnterpriseDataTasmanMgmt, = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
nnenvironmentMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3))
nnenvironmentMib.setRevisions(('1900-08-18 00:00',))
if mibBuilder.loadTexts: nnenvironmentMib.setLastUpdated('0008180000Z')
if mibBuilder.loadTexts: nnenvironmentMib.setOrganization('Nortel Networks')
class EnvState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("normal", 1), ("warning", 2), ("critical", 3), ("fail", 4), ("turned-off", 5))

class EnvInstalled(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("not-installed", 1), ("installed", 2))

class EnvStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("absent", 1), ("failed", 2), ("normal", 3))

class EnvType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("supply-AC-ONLY", 1), ("supply-AC-PoE", 2), ("supply-DC", 3), ("unknown", 4))

nnenvObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1))
nnenvNotificationEnables = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 2))
nnenvNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3))
nnenvTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0))
nnenvTempSensorGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 1))
nnenvTempSensorValue = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnenvTempSensorValue.setStatus('current')
nnenvTempSensorState = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 1, 2), EnvState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnenvTempSensorState.setStatus('current')
nnenvFanTable = MibTable((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 2), )
if mibBuilder.loadTexts: nnenvFanTable.setStatus('current')
nnenvFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 2, 1), ).setIndexNames((0, "ENVIRONMENT-MIB", "nnenvFanUnitIndex"))
if mibBuilder.loadTexts: nnenvFanEntry.setStatus('current')
nnenvFanUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nnenvFanUnitIndex.setStatus('current')
nnenvFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 2, 1, 2), EnvState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnenvFanState.setStatus('current')
nnenvPwrsupPowerFailCount = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnenvPwrsupPowerFailCount.setStatus('current')
nnenvPwrsupTable = MibTable((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4), )
if mibBuilder.loadTexts: nnenvPwrsupTable.setStatus('current')
nnenvPwrsupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1), ).setIndexNames((0, "ENVIRONMENT-MIB", "nnenvPwrsupIndex"))
if mibBuilder.loadTexts: nnenvPwrsupEntry.setStatus('current')
nnenvPwrsupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nnenvPwrsupIndex.setStatus('current')
nnenvPwrsupInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 2), EnvInstalled()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnenvPwrsupInstalled.setStatus('current')
nnenvPwrsupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 3), EnvStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnenvPwrsupStatus.setStatus('current')
nnenvPwrsupType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 4), EnvType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnenvPwrsupType.setStatus('current')
nnenvPwrsupUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnenvPwrsupUptime.setStatus('current')
nnenvPwrsupDowntime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnenvPwrsupDowntime.setStatus('current')
nnenvEnableTemperatureNotification = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nnenvEnableTemperatureNotification.setStatus('current')
nnenvEnableFanNotification = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 2, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nnenvEnableFanNotification.setStatus('current')
nnenvEnablePowerNotification = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 2, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nnenvEnablePowerNotification.setStatus('current')
nnenvTemperatureNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 1)).setObjects(("ENVIRONMENT-MIB", "nnenvTempSensorValue"), ("ENVIRONMENT-MIB", "nnenvTempSensorState"))
if mibBuilder.loadTexts: nnenvTemperatureNotification.setStatus('current')
nnenvFanNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 2)).setObjects(("ENVIRONMENT-MIB", "nnenvFanUnitIndex"), ("ENVIRONMENT-MIB", "nnenvFanState"))
if mibBuilder.loadTexts: nnenvFanNotification.setStatus('current')
nnenvPowerSupply1DownNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 3)).setObjects(("ENVIRONMENT-MIB", "nnenvPwrsupPowerFailCount"), ("ENVIRONMENT-MIB", "nnenvPwrsupIndex"), ("ENVIRONMENT-MIB", "nnenvPwrsupInstalled"), ("ENVIRONMENT-MIB", "nnenvPwrsupStatus"), ("ENVIRONMENT-MIB", "nnenvPwrsupType"), ("ENVIRONMENT-MIB", "nnenvPwrsupUptime"), ("ENVIRONMENT-MIB", "nnenvPwrsupDowntime"))
if mibBuilder.loadTexts: nnenvPowerSupply1DownNotification.setStatus('current')
nnenvPowerSupply1UpNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 4)).setObjects(("ENVIRONMENT-MIB", "nnenvPwrsupPowerFailCount"), ("ENVIRONMENT-MIB", "nnenvPwrsupIndex"), ("ENVIRONMENT-MIB", "nnenvPwrsupInstalled"), ("ENVIRONMENT-MIB", "nnenvPwrsupStatus"), ("ENVIRONMENT-MIB", "nnenvPwrsupType"), ("ENVIRONMENT-MIB", "nnenvPwrsupUptime"), ("ENVIRONMENT-MIB", "nnenvPwrsupDowntime"))
if mibBuilder.loadTexts: nnenvPowerSupply1UpNotification.setStatus('current')
nnenvPowerSupply2DownNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 5)).setObjects(("ENVIRONMENT-MIB", "nnenvPwrsupPowerFailCount"), ("ENVIRONMENT-MIB", "nnenvPwrsupIndex"), ("ENVIRONMENT-MIB", "nnenvPwrsupInstalled"), ("ENVIRONMENT-MIB", "nnenvPwrsupStatus"), ("ENVIRONMENT-MIB", "nnenvPwrsupType"), ("ENVIRONMENT-MIB", "nnenvPwrsupUptime"), ("ENVIRONMENT-MIB", "nnenvPwrsupDowntime"))
if mibBuilder.loadTexts: nnenvPowerSupply2DownNotification.setStatus('current')
nnenvPowerSupply2UpNotification = NotificationType((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 3, 0, 6)).setObjects(("ENVIRONMENT-MIB", "nnenvPwrsupPowerFailCount"), ("ENVIRONMENT-MIB", "nnenvPwrsupIndex"), ("ENVIRONMENT-MIB", "nnenvPwrsupInstalled"), ("ENVIRONMENT-MIB", "nnenvPwrsupStatus"), ("ENVIRONMENT-MIB", "nnenvPwrsupType"), ("ENVIRONMENT-MIB", "nnenvPwrsupUptime"), ("ENVIRONMENT-MIB", "nnenvPwrsupDowntime"))
if mibBuilder.loadTexts: nnenvPowerSupply2UpNotification.setStatus('current')
nnenvironementNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 3, 4)).setObjects(("ENVIRONMENT-MIB", "nnenvTemperatureNotification"), ("ENVIRONMENT-MIB", "nnenvFanNotification"), ("ENVIRONMENT-MIB", "nnenvPowerSupply1DownNotification"), ("ENVIRONMENT-MIB", "nnenvPowerSupply1UpNotification"), ("ENVIRONMENT-MIB", "nnenvPowerSupply2DownNotification"), ("ENVIRONMENT-MIB", "nnenvPowerSupply2UpNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nnenvironementNotificationGroup = nnenvironementNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ENVIRONMENT-MIB", nnenvironmentMib=nnenvironmentMib, nnenvPowerSupply1UpNotification=nnenvPowerSupply1UpNotification, nnenvPowerSupply2DownNotification=nnenvPowerSupply2DownNotification, nnenvPwrsupType=nnenvPwrsupType, EnvInstalled=EnvInstalled, nnenvObjects=nnenvObjects, nnenvPwrsupUptime=nnenvPwrsupUptime, nnenvPwrsupIndex=nnenvPwrsupIndex, nnenvFanState=nnenvFanState, nnenvPowerSupply1DownNotification=nnenvPowerSupply1DownNotification, nnenvFanTable=nnenvFanTable, nnenvTempSensorState=nnenvTempSensorState, nnenvPowerSupply2UpNotification=nnenvPowerSupply2UpNotification, nnenvTraps=nnenvTraps, nnenvPwrsupDowntime=nnenvPwrsupDowntime, nnenvFanEntry=nnenvFanEntry, nnenvPwrsupStatus=nnenvPwrsupStatus, nnenvNotificationEnables=nnenvNotificationEnables, nnenvEnableTemperatureNotification=nnenvEnableTemperatureNotification, nnenvEnableFanNotification=nnenvEnableFanNotification, nnenvFanNotification=nnenvFanNotification, EnvType=EnvType, EnvStatus=EnvStatus, nnenvPwrsupTable=nnenvPwrsupTable, nnenvPwrsupEntry=nnenvPwrsupEntry, nnenvPwrsupInstalled=nnenvPwrsupInstalled, nnenvTempSensorGroup=nnenvTempSensorGroup, nnenvNotifications=nnenvNotifications, EnvState=EnvState, nnenvTemperatureNotification=nnenvTemperatureNotification, nnenvironementNotificationGroup=nnenvironementNotificationGroup, PYSNMP_MODULE_ID=nnenvironmentMib, nnenvTempSensorValue=nnenvTempSensorValue, nnenvPwrsupPowerFailCount=nnenvPwrsupPowerFailCount, nnenvFanUnitIndex=nnenvFanUnitIndex, nnenvEnablePowerNotification=nnenvEnablePowerNotification)
