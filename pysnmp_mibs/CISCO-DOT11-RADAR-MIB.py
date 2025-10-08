#
# PySNMP MIB module CISCO-DOT11-RADAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-DOT11-RADAR-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoDot11RadarMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 627))
ciscoDot11RadarMIB.setRevisions(('2007-05-07 00:00',))
if mibBuilder.loadTexts: ciscoDot11RadarMIB.setLastUpdated('200705070000Z')
if mibBuilder.loadTexts: ciscoDot11RadarMIB.setOrganization('Cisco System Inc.')
ciscoDot11RadarMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 0))
ciscoDot11RadarMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 1))
ciscoDot11RadarMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 2))
cdrDot11RadarNotifConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 1))
cdrDot11RadarDetectInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2))
cdrDot11NewFrequency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 1), Unsigned32().clone(0)).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdrDot11NewFrequency.setStatus('current')
cdrDot11PreferFrequency = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 2), Unsigned32().clone(0)).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdrDot11PreferFrequency.setStatus('current')
cdrChannelSwitchLastTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdrChannelSwitchLastTime.setStatus('current')
cdrChannelReturnLastTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 2, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdrChannelReturnLastTime.setStatus('current')
cdrChannelSwitchNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdrChannelSwitchNotifEnabled.setStatus('current')
cdrChannelReturnNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 627, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdrChannelReturnNotifEnabled.setStatus('current')
ciscoDot11RadarChannelSwitch = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 627, 0, 1)).setObjects(("CISCO-DOT11-RADAR-MIB", "cdrDot11NewFrequency"), ("CISCO-DOT11-RADAR-MIB", "cdrChannelSwitchLastTime"))
if mibBuilder.loadTexts: ciscoDot11RadarChannelSwitch.setStatus('current')
ciscoDot11RadarChannelReturn = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 627, 0, 2)).setObjects(("CISCO-DOT11-RADAR-MIB", "cdrDot11PreferFrequency"), ("CISCO-DOT11-RADAR-MIB", "cdrChannelReturnLastTime"))
if mibBuilder.loadTexts: ciscoDot11RadarChannelReturn.setStatus('current')
ciscoDot11RadarMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 1))
ciscoDot11RadarMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2))
ciscoDot11RadarCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 1, 1)).setObjects(("CISCO-DOT11-RADAR-MIB", "cdrDot11RadarNotifObjectGroup"), ("CISCO-DOT11-RADAR-MIB", "ciscoDot11RadarDetectInfoGroup"), ("CISCO-DOT11-RADAR-MIB", "ciscoDot11RadarNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadarCompliance = ciscoDot11RadarCompliance.setStatus('current')
cdrDot11RadarNotifObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2, 1)).setObjects(("CISCO-DOT11-RADAR-MIB", "cdrChannelSwitchNotifEnabled"), ("CISCO-DOT11-RADAR-MIB", "cdrChannelReturnNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdrDot11RadarNotifObjectGroup = cdrDot11RadarNotifObjectGroup.setStatus('current')
ciscoDot11RadarDetectInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2, 2)).setObjects(("CISCO-DOT11-RADAR-MIB", "cdrDot11NewFrequency"), ("CISCO-DOT11-RADAR-MIB", "cdrDot11PreferFrequency"), ("CISCO-DOT11-RADAR-MIB", "cdrChannelSwitchLastTime"), ("CISCO-DOT11-RADAR-MIB", "cdrChannelReturnLastTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadarDetectInfoGroup = ciscoDot11RadarDetectInfoGroup.setStatus('current')
ciscoDot11RadarNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 627, 2, 2, 3)).setObjects(("CISCO-DOT11-RADAR-MIB", "ciscoDot11RadarChannelSwitch"), ("CISCO-DOT11-RADAR-MIB", "ciscoDot11RadarChannelReturn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadarNotificationGroup = ciscoDot11RadarNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-RADAR-MIB", cdrDot11NewFrequency=cdrDot11NewFrequency, ciscoDot11RadarMIBNotifs=ciscoDot11RadarMIBNotifs, ciscoDot11RadarChannelSwitch=ciscoDot11RadarChannelSwitch, ciscoDot11RadarMIBConform=ciscoDot11RadarMIBConform, cdrDot11RadarNotifConfig=cdrDot11RadarNotifConfig, cdrDot11RadarDetectInfo=cdrDot11RadarDetectInfo, ciscoDot11RadarDetectInfoGroup=ciscoDot11RadarDetectInfoGroup, cdrChannelReturnNotifEnabled=cdrChannelReturnNotifEnabled, cdrDot11RadarNotifObjectGroup=cdrDot11RadarNotifObjectGroup, ciscoDot11RadarMIBCompliances=ciscoDot11RadarMIBCompliances, PYSNMP_MODULE_ID=ciscoDot11RadarMIB, ciscoDot11RadarChannelReturn=ciscoDot11RadarChannelReturn, ciscoDot11RadarMIBGroups=ciscoDot11RadarMIBGroups, ciscoDot11RadarNotificationGroup=ciscoDot11RadarNotificationGroup, cdrChannelReturnLastTime=cdrChannelReturnLastTime, cdrChannelSwitchLastTime=cdrChannelSwitchLastTime, cdrChannelSwitchNotifEnabled=cdrChannelSwitchNotifEnabled, cdrDot11PreferFrequency=cdrDot11PreferFrequency, ciscoDot11RadarMIB=ciscoDot11RadarMIB, ciscoDot11RadarCompliance=ciscoDot11RadarCompliance, ciscoDot11RadarMIBObjects=ciscoDot11RadarMIBObjects)
