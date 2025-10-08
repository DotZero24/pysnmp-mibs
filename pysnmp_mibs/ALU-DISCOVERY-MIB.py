#
# PySNMP MIB module ALU-DISCOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/ALU-DISCOVERY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:20:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeStamp, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "TruthValue", "TextualConvention")
tmnxChassisIndex, tmnxChassisNotifyHwIndex = mibBuilder.importSymbols("TIMETRA-CHASSIS-MIB", "tmnxChassisIndex", "tmnxChassisNotifyHwIndex")
alcatelObjects, alcatelNotifyPrefix, alcatelCommonMIBModules, alcatelConformance = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "alcatelObjects", "alcatelNotifyPrefix", "alcatelCommonMIBModules", "alcatelConformance")
aluDiscoveryMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 5, 4))
aluDiscoveryMIBModule.setRevisions(('1909-01-18 00:00',))
if mibBuilder.loadTexts: aluDiscoveryMIBModule.setLastUpdated('0901190000Z')
if mibBuilder.loadTexts: aluDiscoveryMIBModule.setOrganization('Nokia')
aluDiscoveryObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4))
aluDiscoveryMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4))
aluDiscoveryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1))
aluDiscoveryNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 4))
aluDiscoveryNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 4, 0))
class AluDiscoveryStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5))
    namedValues = NamedValues(("noAutoDiscovery", 0), ("inProgress", 1), ("halted", 2), ("terminated", 4), ("successful", 5))

class AluDiscoveryStage(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("selfDiscovery", 1), ("aquiringNetwork", 2), ("aquiringConfig", 3), ("testAndCommitConfig", 4))

class AluDiscoveryCircuitId(DisplayString):
    status = 'current'

class AluDiscoveryFailureFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("configConflict", 0), ("eqNotReady", 1), ("noPortsReady", 2), ("noNetworkFound", 3), ("ipRequestFailed", 4), ("portSelectFailed", 5), ("configLoadingProblem", 6), ("configTestingFailed", 7), ("configCommitProblem", 8))

aluDiscoveryTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1), )
if mibBuilder.loadTexts: aluDiscoveryTable.setStatus('current')
aluDiscoveryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1), ).setIndexNames((0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"))
if mibBuilder.loadTexts: aluDiscoveryEntry.setStatus('current')
aluDiscoveryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 1), AluDiscoveryStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryStatus.setStatus('current')
aluDiscoveryStage = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 2), AluDiscoveryStage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryStage.setStatus('current')
aluDiscoveryStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryStartTime.setStatus('current')
aluDiscoveryEndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryEndTime.setStatus('current')
aluDiscoverySystemIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoverySystemIpAddr.setStatus('current')
aluDiscoverySystemSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoverySystemSubnet.setStatus('current')
aluDiscoveryLocalCircId = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 7), AluDiscoveryCircuitId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryLocalCircId.setStatus('current')
aluDiscoveryLocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryLocalIpAddr.setStatus('current')
aluDiscoveryLocalSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryLocalSubnet.setStatus('current')
aluDiscoveryGatewayCircId = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 10), AluDiscoveryCircuitId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryGatewayCircId.setStatus('current')
aluDiscoveryGatewayRemId = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryGatewayRemId.setStatus('current')
aluDiscoveryGatewayIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryGatewayIpAddr.setStatus('current')
aluDiscoveryServerIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryServerIpAddr.setStatus('current')
aluDiscoveryFailureFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 1, 1, 14), AluDiscoveryFailureFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aluDiscoveryFailureFlags.setStatus('current')
aluDiscoveryBofInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 2))
aluSbiAutoDiscover = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aluSbiAutoDiscover.setStatus('current')
aluSbiAutoDiscoverId = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50)).clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aluSbiAutoDiscoverId.setStatus('current')
aluSbiAutoDiscoverVlan = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 4, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aluSbiAutoDiscoverVlan.setStatus('current')
aluDiscoveryStarted = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 4, 0, 1))
if mibBuilder.loadTexts: aluDiscoveryStarted.setStatus('current')
aluDiscoveryTerminated = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 4, 0, 2)).setObjects(("ALU-DISCOVERY-MIB", "aluDiscoveryFailureFlags"))
if mibBuilder.loadTexts: aluDiscoveryTerminated.setStatus('current')
aluDiscoverySuccessful = NotificationType((1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 4, 0, 3)).setObjects(("ALU-DISCOVERY-MIB", "aluDiscoverySystemIpAddr"), ("ALU-DISCOVERY-MIB", "aluDiscoveryLocalCircId"), ("ALU-DISCOVERY-MIB", "aluDiscoveryLocalIpAddr"), ("ALU-DISCOVERY-MIB", "aluDiscoveryGatewayCircId"), ("ALU-DISCOVERY-MIB", "aluDiscoveryGatewayIpAddr"))
if mibBuilder.loadTexts: aluDiscoverySuccessful.setStatus('current')
aluDiscoveryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 1))
aluDiscoveryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 2))
aluDiscoveryComp7705 = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 1, 1))
aluDiscoveryComp7705V1v0 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 1, 1, 1)).setObjects(("ALU-DISCOVERY-MIB", "aluDiscoveryGroup"), ("ALU-DISCOVERY-MIB", "aluDiscoveryNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluDiscoveryComp7705V1v0 = aluDiscoveryComp7705V1v0.setStatus('current')
aluDiscoveryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 2, 1)).setObjects(("ALU-DISCOVERY-MIB", "aluDiscoveryStatus"), ("ALU-DISCOVERY-MIB", "aluDiscoveryStage"), ("ALU-DISCOVERY-MIB", "aluDiscoveryStartTime"), ("ALU-DISCOVERY-MIB", "aluDiscoveryEndTime"), ("ALU-DISCOVERY-MIB", "aluDiscoverySystemIpAddr"), ("ALU-DISCOVERY-MIB", "aluDiscoverySystemSubnet"), ("ALU-DISCOVERY-MIB", "aluDiscoveryLocalCircId"), ("ALU-DISCOVERY-MIB", "aluDiscoveryLocalIpAddr"), ("ALU-DISCOVERY-MIB", "aluDiscoveryLocalSubnet"), ("ALU-DISCOVERY-MIB", "aluDiscoveryGatewayCircId"), ("ALU-DISCOVERY-MIB", "aluDiscoveryGatewayRemId"), ("ALU-DISCOVERY-MIB", "aluDiscoveryGatewayIpAddr"), ("ALU-DISCOVERY-MIB", "aluDiscoveryServerIpAddr"), ("ALU-DISCOVERY-MIB", "aluDiscoveryFailureFlags"), ("ALU-DISCOVERY-MIB", "aluSbiAutoDiscover"), ("ALU-DISCOVERY-MIB", "aluSbiAutoDiscoverId"), ("ALU-DISCOVERY-MIB", "aluSbiAutoDiscoverVlan"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluDiscoveryGroup = aluDiscoveryGroup.setStatus('current')
aluDiscoveryNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 4, 1, 2, 2)).setObjects(("ALU-DISCOVERY-MIB", "aluDiscoveryStarted"), ("ALU-DISCOVERY-MIB", "aluDiscoveryTerminated"), ("ALU-DISCOVERY-MIB", "aluDiscoverySuccessful"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aluDiscoveryNotificationGroup = aluDiscoveryNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ALU-DISCOVERY-MIB", aluDiscoverySuccessful=aluDiscoverySuccessful, aluDiscoveryObjs=aluDiscoveryObjs, AluDiscoveryFailureFlags=AluDiscoveryFailureFlags, aluDiscoveryLocalCircId=aluDiscoveryLocalCircId, aluDiscoverySystemSubnet=aluDiscoverySystemSubnet, aluDiscoveryCompliances=aluDiscoveryCompliances, AluDiscoveryStage=AluDiscoveryStage, aluDiscoveryLocalIpAddr=aluDiscoveryLocalIpAddr, PYSNMP_MODULE_ID=aluDiscoveryMIBModule, aluDiscoveryComp7705V1v0=aluDiscoveryComp7705V1v0, aluDiscoveryConformance=aluDiscoveryConformance, aluDiscoveryStartTime=aluDiscoveryStartTime, aluDiscoveryGatewayCircId=aluDiscoveryGatewayCircId, aluDiscoveryEntry=aluDiscoveryEntry, AluDiscoveryCircuitId=AluDiscoveryCircuitId, aluDiscoveryGatewayRemId=aluDiscoveryGatewayRemId, aluDiscoveryEndTime=aluDiscoveryEndTime, aluDiscoverySystemIpAddr=aluDiscoverySystemIpAddr, aluDiscoveryGroups=aluDiscoveryGroups, aluSbiAutoDiscoverId=aluSbiAutoDiscoverId, aluSbiAutoDiscoverVlan=aluSbiAutoDiscoverVlan, aluDiscoveryGatewayIpAddr=aluDiscoveryGatewayIpAddr, aluDiscoveryNotificationGroup=aluDiscoveryNotificationGroup, aluDiscoveryNotifications=aluDiscoveryNotifications, aluDiscoveryStarted=aluDiscoveryStarted, aluDiscoveryMIBModule=aluDiscoveryMIBModule, aluDiscoveryMIBConformance=aluDiscoveryMIBConformance, aluDiscoveryLocalSubnet=aluDiscoveryLocalSubnet, aluDiscoveryServerIpAddr=aluDiscoveryServerIpAddr, aluDiscoveryGroup=aluDiscoveryGroup, aluDiscoveryTerminated=aluDiscoveryTerminated, aluDiscoveryBofInfo=aluDiscoveryBofInfo, aluDiscoveryStage=aluDiscoveryStage, aluDiscoveryStatus=aluDiscoveryStatus, aluSbiAutoDiscover=aluSbiAutoDiscover, AluDiscoveryStatus=AluDiscoveryStatus, aluDiscoveryNotificationsPrefix=aluDiscoveryNotificationsPrefix, aluDiscoveryTable=aluDiscoveryTable, aluDiscoveryFailureFlags=aluDiscoveryFailureFlags, aluDiscoveryComp7705=aluDiscoveryComp7705)
