#
# PySNMP MIB module SVRNTCLU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/SVRNTCLU-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, mgmt, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "mgmt", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dec = MibIdentifier((1, 3, 6, 1, 4, 1, 36))
ema = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2))
class ObjectType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("objectUnknown", 1), ("objectOther", 2), ("share", 3), ("disk", 4), ("application", 5), ("ipAddress", 6), ("fileShare", 7))

class PolicyType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("policyUnknown", 1), ("policyOther", 2), ("inOrder", 3), ("random", 4), ("leastLoad", 5), ("roundRobin", 6))

class Boolean(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class DateAndTime(DisplayString):
    pass

class FailoverReason(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("reasonUnknown", 1), ("reasonOther", 2), ("reconfiguration", 3), ("failure", 4), ("failback", 5))

mib_extensions_1 = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18)).setLabel("mib-extensions-1")
svrSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 22))
svrCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4))
svrNTClu = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2))
svrNTCluObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1))
svrNTCluMibInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 1))
svrNTCluClusterInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2))
ntcExMgtMibMajorRev = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExMgtMibMajorRev.setStatus('mandatory')
ntcExMgtMibMinorRev = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExMgtMibMinorRev.setStatus('mandatory')
ntcExAlias = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExAlias.setStatus('mandatory')
ntcExGroupTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7), )
if mibBuilder.loadTexts: ntcExGroupTable.setStatus('mandatory')
ntcExGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1), ).setIndexNames((0, "SVRNTCLU-MIB", "ntcExGroupIndex"))
if mibBuilder.loadTexts: ntcExGroupEntry.setStatus('mandatory')
ntcExGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExGroupIndex.setStatus('mandatory')
ntcExGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExGroupName.setStatus('mandatory')
ntcExGroupComment = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExGroupComment.setStatus('mandatory')
ntcExGroupOnLine = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExGroupOnLine.setStatus('mandatory')
ntcExGroupFailedOver = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 5), Boolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExGroupFailedOver.setStatus('mandatory')
ntcExGroupPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 6), PolicyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExGroupPolicy.setStatus('mandatory')
ntcExGroupReevaluate = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 7), Boolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExGroupReevaluate.setStatus('mandatory')
ntcExGroupMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExGroupMembers.setStatus('mandatory')
ntcExGroupObjects = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 7, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExGroupObjects.setStatus('mandatory')
ntcExObjectTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8), )
if mibBuilder.loadTexts: ntcExObjectTable.setStatus('mandatory')
ntcExObjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1), ).setIndexNames((0, "SVRNTCLU-MIB", "ntcExObjectIndex"))
if mibBuilder.loadTexts: ntcExObjectEntry.setStatus('mandatory')
ntcExObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExObjectIndex.setStatus('mandatory')
ntcExObjectName = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExObjectName.setStatus('mandatory')
ntcExObjectComment = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExObjectComment.setStatus('mandatory')
ntcExObjectType = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 4), ObjectType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExObjectType.setStatus('mandatory')
ntcExObjectDrives = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExObjectDrives.setStatus('mandatory')
ntcExObjectIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 4, 2, 1, 2, 8, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcExObjectIpAddress.setStatus('mandatory')
mibBuilder.exportSymbols("SVRNTCLU-MIB", ntcExGroupOnLine=ntcExGroupOnLine, ntcExObjectName=ntcExObjectName, ntcExObjectComment=ntcExObjectComment, svrSystem=svrSystem, ntcExObjectDrives=ntcExObjectDrives, dec=dec, ntcExGroupIndex=ntcExGroupIndex, ntcExGroupTable=ntcExGroupTable, ntcExObjectIpAddress=ntcExObjectIpAddress, ntcExGroupPolicy=ntcExGroupPolicy, ntcExGroupEntry=ntcExGroupEntry, ntcExGroupReevaluate=ntcExGroupReevaluate, ntcExGroupName=ntcExGroupName, svrNTCluClusterInfo=svrNTCluClusterInfo, ntcExGroupFailedOver=ntcExGroupFailedOver, DateAndTime=DateAndTime, Boolean=Boolean, ema=ema, ntcExGroupObjects=ntcExGroupObjects, ntcExObjectTable=ntcExObjectTable, FailoverReason=FailoverReason, mib_extensions_1=mib_extensions_1, ntcExAlias=ntcExAlias, svrCluster=svrCluster, ntcExGroupMembers=ntcExGroupMembers, ntcExObjectIndex=ntcExObjectIndex, PolicyType=PolicyType, svrNTCluObjects=svrNTCluObjects, ntcExMgtMibMajorRev=ntcExMgtMibMajorRev, svrNTCluMibInfo=svrNTCluMibInfo, ObjectType=ObjectType, ntcExObjectEntry=ntcExObjectEntry, ntcExObjectType=ntcExObjectType, ntcExMgtMibMinorRev=ntcExMgtMibMinorRev, svrNTClu=svrNTClu, ntcExGroupComment=ntcExGroupComment)
