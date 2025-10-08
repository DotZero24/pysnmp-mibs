#
# PySNMP MIB module PEPLINK-BALANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/peplink/PEPLINK-BALANCE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
peplinkBalance = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 1))
peplinkBalance.setRevisions(('2009-03-05 00:00', '2009-03-05 00:00',))
if mibBuilder.loadTexts: peplinkBalance.setLastUpdated('200903050000Z')
if mibBuilder.loadTexts: peplinkBalance.setOrganization('Peplink')
class TableIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class ConnectionNum(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NameString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '80a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 80)

class PortSpeedType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 0), ("auto", 1), ("fullDulplex10", 2), ("halfDulplex10", 3), ("fullDulplex100", 4), ("halfDulplex100", 5), ("fullDulplex1000", 6), ("halfDulplex1000", 7))

balanceStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 1, 1))
balanceSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 1, 1, 1))
balFirmware = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 1), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: balFirmware.setStatus('current')
balSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 2), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: balSerialNumber.setStatus('current')
balTime = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 3), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: balTime.setStatus('current')
balUpTime = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: balUpTime.setStatus('current')
balanceLan = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 6))
balLanStatus = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 6, 1), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: balLanStatus.setStatus('current')
balLanIp = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 6, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: balLanIp.setStatus('current')
balLanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 6, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: balLanSubnetMask.setStatus('current')
balLinkStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2))
balLinkNumber = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: balLinkNumber.setStatus('current')
linkTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2), )
if mibBuilder.loadTexts: linkTable.setStatus('current')
linkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1), ).setIndexNames((0, "PEPLINK-BALANCE-MIB", "linkConnNum"))
if mibBuilder.loadTexts: linkEntry.setStatus('current')
linkConnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 1), ConnectionNum())
if mibBuilder.loadTexts: linkConnNum.setStatus('current')
linkName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 2), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkName.setStatus('current')
linkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 3), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkStatus.setStatus('current')
linkThroughputIn = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkThroughputIn.setStatus('current')
linkThroughputOut = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkThroughputOut.setStatus('current')
linkDataTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkDataTransferred.setStatus('current')
linkIpTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 3), )
if mibBuilder.loadTexts: linkIpTable.setStatus('current')
linkIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 3, 1), ).setIndexNames((0, "PEPLINK-BALANCE-MIB", "linkIpConnNum"), (0, "PEPLINK-BALANCE-MIB", "linkIpIndex"))
if mibBuilder.loadTexts: linkIpEntry.setStatus('current')
linkIpConnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 3, 1, 1), ConnectionNum())
if mibBuilder.loadTexts: linkIpConnNum.setStatus('current')
linkIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 3, 1, 2), TableIndex())
if mibBuilder.loadTexts: linkIpIndex.setStatus('current')
linkIp = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkIp.setStatus('current')
wanUsageTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 1, 1, 3), )
if mibBuilder.loadTexts: wanUsageTable.setStatus('current')
wanUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 1, 1, 3, 1), ).setIndexNames((0, "PEPLINK-BALANCE-MIB", "wanUsageIndex"))
if mibBuilder.loadTexts: wanUsageEntry.setStatus('current')
wanUsageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 3, 1, 1), TableIndex())
if mibBuilder.loadTexts: wanUsageIndex.setStatus('current')
wanUsageThroughputIn = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageThroughputIn.setStatus('current')
wanUsageThroughputOut = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageThroughputOut.setStatus('current')
wanUsageDataTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageDataTransferred.setStatus('current')
balanceMaintenance = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 1, 2))
balReboot = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 2, 1), NameString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: balReboot.setStatus('current')
balanceLanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 1, 3))
portLanSpeedConfig = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 3, 1), PortSpeedType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portLanSpeedConfig.setStatus('current')
portWanSpeedConfigTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 1, 3, 2), )
if mibBuilder.loadTexts: portWanSpeedConfigTable.setStatus('current')
portWanSpeedConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 1, 3, 2, 1), ).setIndexNames((0, "PEPLINK-BALANCE-MIB", "portWanSpeedConfigIndex"))
if mibBuilder.loadTexts: portWanSpeedConfigEntry.setStatus('current')
portWanSpeedConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 3, 2, 1, 1), TableIndex())
if mibBuilder.loadTexts: portWanSpeedConfigIndex.setStatus('current')
portWanSpeedConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 1, 3, 2, 1, 2), PortSpeedType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portWanSpeedConfig.setStatus('current')
lanConfigIp = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanConfigIp.setStatus('current')
lanConfigSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 23695, 1, 3, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanConfigSubnetMask.setStatus('current')
balanceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 1, 50))
balCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 1, 50, 1))
balGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 1, 50, 2))
balCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 23695, 1, 50, 1, 1)).setObjects(("PEPLINK-BALANCE-MIB", "balSystemGroup"), ("PEPLINK-BALANCE-MIB", "balLinkGroup"), ("PEPLINK-BALANCE-MIB", "balWanGroup"), ("PEPLINK-BALANCE-MIB", "balSetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    balCompliance = balCompliance.setStatus('current')
balSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 23695, 1, 50, 2, 1)).setObjects(("PEPLINK-BALANCE-MIB", "balFirmware"), ("PEPLINK-BALANCE-MIB", "balSerialNumber"), ("PEPLINK-BALANCE-MIB", "balTime"), ("PEPLINK-BALANCE-MIB", "balUpTime"), ("PEPLINK-BALANCE-MIB", "balLanStatus"), ("PEPLINK-BALANCE-MIB", "balLanIp"), ("PEPLINK-BALANCE-MIB", "balLanSubnetMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    balSystemGroup = balSystemGroup.setStatus('current')
balLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 23695, 1, 50, 2, 2)).setObjects(("PEPLINK-BALANCE-MIB", "balLinkNumber"), ("PEPLINK-BALANCE-MIB", "linkName"), ("PEPLINK-BALANCE-MIB", "linkStatus"), ("PEPLINK-BALANCE-MIB", "linkIp"), ("PEPLINK-BALANCE-MIB", "linkThroughputIn"), ("PEPLINK-BALANCE-MIB", "linkThroughputOut"), ("PEPLINK-BALANCE-MIB", "linkDataTransferred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    balLinkGroup = balLinkGroup.setStatus('current')
balWanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 23695, 1, 50, 2, 3)).setObjects(("PEPLINK-BALANCE-MIB", "wanUsageThroughputIn"), ("PEPLINK-BALANCE-MIB", "wanUsageThroughputOut"), ("PEPLINK-BALANCE-MIB", "wanUsageDataTransferred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    balWanGroup = balWanGroup.setStatus('current')
balSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 23695, 1, 50, 2, 4)).setObjects(("PEPLINK-BALANCE-MIB", "balReboot"), ("PEPLINK-BALANCE-MIB", "portWanSpeedConfig"), ("PEPLINK-BALANCE-MIB", "portLanSpeedConfig"), ("PEPLINK-BALANCE-MIB", "lanConfigIp"), ("PEPLINK-BALANCE-MIB", "lanConfigSubnetMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    balSetGroup = balSetGroup.setStatus('current')
mibBuilder.exportSymbols("PEPLINK-BALANCE-MIB", balFirmware=balFirmware, balanceSystem=balanceSystem, PortSpeedType=PortSpeedType, balanceConformance=balanceConformance, balSystemGroup=balSystemGroup, linkIpEntry=linkIpEntry, portWanSpeedConfigIndex=portWanSpeedConfigIndex, NameString=NameString, balLinkGroup=balLinkGroup, lanConfigIp=lanConfigIp, balCompliances=balCompliances, balSetGroup=balSetGroup, linkConnNum=linkConnNum, peplinkBalance=peplinkBalance, linkName=linkName, balUpTime=balUpTime, wanUsageThroughputOut=wanUsageThroughputOut, balanceMaintenance=balanceMaintenance, linkIpTable=linkIpTable, balanceLan=balanceLan, linkTable=linkTable, balSerialNumber=balSerialNumber, linkStatus=linkStatus, ConnectionNum=ConnectionNum, balLinkStatus=balLinkStatus, balLanSubnetMask=balLanSubnetMask, wanUsageIndex=wanUsageIndex, wanUsageDataTransferred=wanUsageDataTransferred, linkIpIndex=linkIpIndex, linkIp=linkIp, linkEntry=linkEntry, PYSNMP_MODULE_ID=peplinkBalance, wanUsageEntry=wanUsageEntry, portWanSpeedConfig=portWanSpeedConfig, linkThroughputIn=linkThroughputIn, balanceStatus=balanceStatus, linkIpConnNum=linkIpConnNum, portWanSpeedConfigEntry=portWanSpeedConfigEntry, balGroups=balGroups, balTime=balTime, balCompliance=balCompliance, balLanStatus=balLanStatus, portWanSpeedConfigTable=portWanSpeedConfigTable, balWanGroup=balWanGroup, wanUsageThroughputIn=wanUsageThroughputIn, balanceLanConfig=balanceLanConfig, balLinkNumber=balLinkNumber, balReboot=balReboot, portLanSpeedConfig=portLanSpeedConfig, linkThroughputOut=linkThroughputOut, TableIndex=TableIndex, wanUsageTable=wanUsageTable, balLanIp=balLanIp, linkDataTransferred=linkDataTransferred, lanConfigSubnetMask=lanConfigSubnetMask)
