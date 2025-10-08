#
# PySNMP MIB module CISCO-FLOW-CLONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-FLOW-CLONE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:12:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TimeStamp, RowStatus, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowStatus", "StorageType", "TextualConvention")
ciscoFlowCloneMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 765))
ciscoFlowCloneMIB.setRevisions(('2010-07-08 00:00',))
if mibBuilder.loadTexts: ciscoFlowCloneMIB.setLastUpdated('201010190000Z')
if mibBuilder.loadTexts: ciscoFlowCloneMIB.setOrganization('Cisco Systems, Inc.')
ciscoFlowCloneMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 0))
ciscoFlowCloneMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1))
ciscoFlowCloneMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 2))
class CloneProfileIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CloneFlowIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class CloneProfilePointType(TextualConvention, Integer32):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("none", 3), ("interface", 4))

class CloneProfilePointIdentifier(InterfaceIndexOrZero):
    status = 'current'

cfcCloneProfiles = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1))
cfcCloneProfileIdNext = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 1), CloneProfileIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileIdNext.setStatus('current')
cfcCloneProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2), )
if mibBuilder.loadTexts: cfcCloneProfileTable.setStatus('current')
cfcCloneProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"))
if mibBuilder.loadTexts: cfcCloneProfileEntry.setStatus('current')
cfcCloneProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 1), CloneProfileIdentifier())
if mibBuilder.loadTexts: cfcCloneProfileId.setStatus('current')
cfcCloneProfileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileStatus.setStatus('current')
cfcCloneProfileStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileStorageType.setStatus('current')
cfcCloneProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileName.setStatus('current')
cfcCloneProfileDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileDescription.setStatus('current')
cfcCloneProfileCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileCreateTime.setStatus('current')
cfcCloneProfileFlowCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 7), Gauge32()).setUnits('traffic flows').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileFlowCount.setStatus('current')
cfcCloneProfileFlowType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("ip", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileFlowType.setStatus('current')
cfcCloneTargetType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("system", 2), ("interface", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneTargetType.setStatus('current')
cfcCloneTargetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneTargetIfIndex.setStatus('current')
cfcCloneProfileEgressIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 11), CloneProfilePointType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileEgressIfType.setStatus('current')
cfcCloneProfileEgressIf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 2, 1, 12), CloneProfilePointIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcCloneProfileEgressIf.setStatus('current')
cfcCloneProfileTableChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcCloneProfileTableChanged.setStatus('current')
cfcFlows = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2))
cfcFlowIpTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1), )
if mibBuilder.loadTexts: cfcFlowIpTable.setStatus('current')
cfcFlowIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"), (0, "CISCO-FLOW-CLONE-MIB", "cfcFlowIndex"))
if mibBuilder.loadTexts: cfcFlowIpEntry.setStatus('current')
cfcFlowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 1), CloneFlowIdentifier())
if mibBuilder.loadTexts: cfcFlowIndex.setStatus('current')
cfcFlowIpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpStatus.setStatus('current')
cfcFlowIpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 3), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpStorageType.setStatus('current')
cfcFlowIpAddrSrcType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 4), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrSrcType.setStatus('current')
cfcFlowIpAddrSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrSrc.setStatus('current')
cfcFlowIpAddrDstType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 6), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrDstType.setStatus('current')
cfcFlowIpAddrDst = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfcFlowIpAddrDst.setStatus('current')
cfcFlowIpCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 2, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFlowIpCreateTime.setStatus('current')
cfcFlowStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3))
cfcFlowStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1), )
if mibBuilder.loadTexts: cfcFlowStatsTable.setStatus('current')
cfcFlowStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-FLOW-CLONE-MIB", "cfcCloneProfileId"), (0, "CISCO-FLOW-CLONE-MIB", "cfcFlowIndex"))
if mibBuilder.loadTexts: cfcFlowStatsEntry.setStatus('current')
cfcFlowPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1, 1), Counter64()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFlowPkts.setStatus('current')
cfcFlowOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 765, 1, 3, 1, 1, 2), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFlowOctets.setStatus('current')
ciscoFlowCloneMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 1))
ciscoFlowCloneMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2))
ciscoCloneFlowCompliance01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 1, 1)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileGroup"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowGroup"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCloneFlowCompliance01 = ciscoCloneFlowCompliance01.setStatus('current')
cfcCloneProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 1)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileIdNext"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileStatus"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileStorageType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileName"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileDescription"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileCreateTime"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileFlowCount"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileFlowType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneTargetType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneTargetIfIndex"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileEgressIfType"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileEgressIf"), ("CISCO-FLOW-CLONE-MIB", "cfcCloneProfileTableChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcCloneProfileGroup = cfcCloneProfileGroup.setStatus('current')
cfcFlowGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 2)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcFlowIpStatus"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpStorageType"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrSrcType"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrSrc"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrDstType"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpAddrDst"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowIpCreateTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcFlowGroup = cfcFlowGroup.setStatus('current')
cfcFlowStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 765, 2, 2, 3)).setObjects(("CISCO-FLOW-CLONE-MIB", "cfcFlowPkts"), ("CISCO-FLOW-CLONE-MIB", "cfcFlowOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcFlowStatsGroup = cfcFlowStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FLOW-CLONE-MIB", cfcCloneProfileName=cfcCloneProfileName, cfcCloneProfileCreateTime=cfcCloneProfileCreateTime, cfcCloneProfileEgressIfType=cfcCloneProfileEgressIfType, cfcFlows=cfcFlows, ciscoFlowCloneMIBObjects=ciscoFlowCloneMIBObjects, cfcFlowIndex=cfcFlowIndex, cfcCloneProfileEgressIf=cfcCloneProfileEgressIf, cfcCloneProfileStorageType=cfcCloneProfileStorageType, cfcCloneTargetIfIndex=cfcCloneTargetIfIndex, cfcFlowIpTable=cfcFlowIpTable, ciscoFlowCloneMIBCompliances=ciscoFlowCloneMIBCompliances, cfcCloneProfileTableChanged=cfcCloneProfileTableChanged, cfcFlowIpAddrSrcType=cfcFlowIpAddrSrcType, cfcCloneProfileGroup=cfcCloneProfileGroup, cfcCloneProfileId=cfcCloneProfileId, ciscoFlowCloneMIBConformance=ciscoFlowCloneMIBConformance, cfcCloneTargetType=cfcCloneTargetType, cfcFlowIpCreateTime=cfcFlowIpCreateTime, CloneProfilePointType=CloneProfilePointType, cfcFlowStats=cfcFlowStats, CloneProfilePointIdentifier=CloneProfilePointIdentifier, CloneProfileIdentifier=CloneProfileIdentifier, cfcFlowIpStatus=cfcFlowIpStatus, cfcFlowStatsEntry=cfcFlowStatsEntry, cfcCloneProfileIdNext=cfcCloneProfileIdNext, cfcFlowPkts=cfcFlowPkts, cfcFlowOctets=cfcFlowOctets, ciscoFlowCloneMIB=ciscoFlowCloneMIB, cfcCloneProfiles=cfcCloneProfiles, cfcCloneProfileDescription=cfcCloneProfileDescription, cfcFlowIpStorageType=cfcFlowIpStorageType, cfcFlowIpAddrSrc=cfcFlowIpAddrSrc, PYSNMP_MODULE_ID=ciscoFlowCloneMIB, ciscoFlowCloneMIBNotifications=ciscoFlowCloneMIBNotifications, cfcFlowIpAddrDstType=cfcFlowIpAddrDstType, cfcCloneProfileStatus=cfcCloneProfileStatus, cfcCloneProfileFlowType=cfcCloneProfileFlowType, cfcFlowIpAddrDst=cfcFlowIpAddrDst, ciscoFlowCloneMIBGroups=ciscoFlowCloneMIBGroups, ciscoCloneFlowCompliance01=ciscoCloneFlowCompliance01, cfcFlowStatsGroup=cfcFlowStatsGroup, CloneFlowIdentifier=CloneFlowIdentifier, cfcCloneProfileTable=cfcCloneProfileTable, cfcFlowStatsTable=cfcFlowStatsTable, cfcCloneProfileFlowCount=cfcCloneProfileFlowCount, cfcFlowIpEntry=cfcFlowIpEntry, cfcFlowGroup=cfcFlowGroup, cfcCloneProfileEntry=cfcCloneProfileEntry)
