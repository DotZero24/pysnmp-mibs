#
# PySNMP MIB module PEPWAVE-MAX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/peplink/PEPWAVE-MAX-MIB
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
pepwaveMAX = ModuleIdentity((1, 3, 6, 1, 4, 1, 27662, 1))
pepwaveMAX.setRevisions(('2012-06-06 00:00',))
if mibBuilder.loadTexts: pepwaveMAX.setLastUpdated('201206060000Z')
if mibBuilder.loadTexts: pepwaveMAX.setOrganization('Pepwave')
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

maxStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1))
maxSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1))
maxFirmware = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 1), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxFirmware.setStatus('current')
maxSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 2), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxSerialNumber.setStatus('current')
maxTime = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 3), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxTime.setStatus('current')
maxUpTime = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxUpTime.setStatus('current')
maxLan = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6))
maxLanStatus = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 1), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLanStatus.setStatus('current')
maxLanIp = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLanIp.setStatus('current')
maxLanSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLanSubnetMask.setStatus('current')
maxLinkStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2))
maxLinkNumber = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: maxLinkNumber.setStatus('current')
linkTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2), )
if mibBuilder.loadTexts: linkTable.setStatus('current')
linkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "linkConnNum"))
if mibBuilder.loadTexts: linkEntry.setStatus('current')
linkConnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 1), ConnectionNum())
if mibBuilder.loadTexts: linkConnNum.setStatus('current')
linkName = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 2), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkName.setStatus('current')
linkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 3), NameString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkStatus.setStatus('current')
linkThroughputIn = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkThroughputIn.setStatus('current')
linkThroughputOut = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkThroughputOut.setStatus('current')
linkDataTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkDataTransferred.setStatus('current')
linkIpTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3), )
if mibBuilder.loadTexts: linkIpTable.setStatus('current')
linkIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "linkIpConnNum"), (0, "PEPWAVE-MAX-MIB", "linkIpIndex"))
if mibBuilder.loadTexts: linkIpEntry.setStatus('current')
linkIpConnNum = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 1), ConnectionNum())
if mibBuilder.loadTexts: linkIpConnNum.setStatus('current')
linkIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 2), TableIndex())
if mibBuilder.loadTexts: linkIpIndex.setStatus('current')
linkIp = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkIp.setStatus('current')
wanUsageTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3), )
if mibBuilder.loadTexts: wanUsageTable.setStatus('current')
wanUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "wanUsageIndex"))
if mibBuilder.loadTexts: wanUsageEntry.setStatus('current')
wanUsageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 1), TableIndex())
if mibBuilder.loadTexts: wanUsageIndex.setStatus('current')
wanUsageThroughputIn = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageThroughputIn.setStatus('current')
wanUsageThroughputOut = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageThroughputOut.setStatus('current')
wanUsageDataTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wanUsageDataTransferred.setStatus('current')
maxMaintenance = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 2))
maxReboot = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 2, 1), NameString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: maxReboot.setStatus('current')
maxLanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 3))
portLanSpeedConfig = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 3, 1), PortSpeedType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portLanSpeedConfig.setStatus('current')
portWanSpeedConfigTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2), )
if mibBuilder.loadTexts: portWanSpeedConfigTable.setStatus('current')
portWanSpeedConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1), ).setIndexNames((0, "PEPWAVE-MAX-MIB", "portWanSpeedConfigIndex"))
if mibBuilder.loadTexts: portWanSpeedConfigEntry.setStatus('current')
portWanSpeedConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1, 1), TableIndex())
if mibBuilder.loadTexts: portWanSpeedConfigIndex.setStatus('current')
portWanSpeedConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1, 2), PortSpeedType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portWanSpeedConfig.setStatus('current')
lanConfigIp = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanConfigIp.setStatus('current')
lanConfigSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 27662, 1, 3, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lanConfigSubnetMask.setStatus('current')
maxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 50))
maxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 50, 1))
maxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2))
maxCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27662, 1, 50, 1, 1)).setObjects(("PEPWAVE-MAX-MIB", "maxSystemGroup"), ("PEPWAVE-MAX-MIB", "maxLinkGroup"), ("PEPWAVE-MAX-MIB", "maxWanGroup"), ("PEPWAVE-MAX-MIB", "maxSetGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxCompliance = maxCompliance.setStatus('current')
maxSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 1)).setObjects(("PEPWAVE-MAX-MIB", "maxFirmware"), ("PEPWAVE-MAX-MIB", "maxSerialNumber"), ("PEPWAVE-MAX-MIB", "maxTime"), ("PEPWAVE-MAX-MIB", "maxUpTime"), ("PEPWAVE-MAX-MIB", "maxLanStatus"), ("PEPWAVE-MAX-MIB", "maxLanIp"), ("PEPWAVE-MAX-MIB", "maxLanSubnetMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxSystemGroup = maxSystemGroup.setStatus('current')
maxLinkGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 2)).setObjects(("PEPWAVE-MAX-MIB", "maxLinkNumber"), ("PEPWAVE-MAX-MIB", "linkName"), ("PEPWAVE-MAX-MIB", "linkStatus"), ("PEPWAVE-MAX-MIB", "linkIp"), ("PEPWAVE-MAX-MIB", "linkThroughputIn"), ("PEPWAVE-MAX-MIB", "linkThroughputOut"), ("PEPWAVE-MAX-MIB", "linkDataTransferred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxLinkGroup = maxLinkGroup.setStatus('current')
maxWanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 3)).setObjects(("PEPWAVE-MAX-MIB", "wanUsageThroughputIn"), ("PEPWAVE-MAX-MIB", "wanUsageThroughputOut"), ("PEPWAVE-MAX-MIB", "wanUsageDataTransferred"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxWanGroup = maxWanGroup.setStatus('current')
maxSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 4)).setObjects(("PEPWAVE-MAX-MIB", "maxReboot"), ("PEPWAVE-MAX-MIB", "portWanSpeedConfig"), ("PEPWAVE-MAX-MIB", "portLanSpeedConfig"), ("PEPWAVE-MAX-MIB", "lanConfigIp"), ("PEPWAVE-MAX-MIB", "lanConfigSubnetMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    maxSetGroup = maxSetGroup.setStatus('current')
mibBuilder.exportSymbols("PEPWAVE-MAX-MIB", maxSetGroup=maxSetGroup, PortSpeedType=PortSpeedType, maxUpTime=maxUpTime, linkIpEntry=linkIpEntry, portWanSpeedConfigIndex=portWanSpeedConfigIndex, NameString=NameString, lanConfigIp=lanConfigIp, linkConnNum=linkConnNum, maxFirmware=maxFirmware, maxLanIp=maxLanIp, maxWanGroup=maxWanGroup, maxLinkStatus=maxLinkStatus, linkName=linkName, maxSystemGroup=maxSystemGroup, wanUsageThroughputOut=wanUsageThroughputOut, maxSerialNumber=maxSerialNumber, linkIpTable=linkIpTable, maxMaintenance=maxMaintenance, maxLinkNumber=maxLinkNumber, linkTable=linkTable, maxStatus=maxStatus, maxSystem=maxSystem, linkStatus=linkStatus, ConnectionNum=ConnectionNum, pepwaveMAX=pepwaveMAX, wanUsageIndex=wanUsageIndex, wanUsageDataTransferred=wanUsageDataTransferred, maxReboot=maxReboot, linkIpIndex=linkIpIndex, maxLanConfig=maxLanConfig, maxConformance=maxConformance, linkIp=linkIp, maxCompliances=maxCompliances, linkEntry=linkEntry, maxLanStatus=maxLanStatus, maxTime=maxTime, wanUsageEntry=wanUsageEntry, portWanSpeedConfig=portWanSpeedConfig, linkThroughputIn=linkThroughputIn, maxLan=maxLan, portWanSpeedConfigEntry=portWanSpeedConfigEntry, linkIpConnNum=linkIpConnNum, maxLinkGroup=maxLinkGroup, portWanSpeedConfigTable=portWanSpeedConfigTable, maxLanSubnetMask=maxLanSubnetMask, wanUsageThroughputIn=wanUsageThroughputIn, maxGroups=maxGroups, PYSNMP_MODULE_ID=pepwaveMAX, portLanSpeedConfig=portLanSpeedConfig, maxCompliance=maxCompliance, linkThroughputOut=linkThroughputOut, TableIndex=TableIndex, wanUsageTable=wanUsageTable, linkDataTransferred=linkDataTransferred, lanConfigSubnetMask=lanConfigSubnetMask)
