#
# PySNMP MIB module TRAPEZE-NETWORKS-CLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-CLUSTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
TrpzApNum, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-AP-TC", "TrpzApNum")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzClusterMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 21))
trpzClusterMib.setRevisions(('2011-02-24 00:01',))
if mibBuilder.loadTexts: trpzClusterMib.setLastUpdated('201102240001Z')
if mibBuilder.loadTexts: trpzClusterMib.setOrganization('Trapeze Networks')
trpzClusterMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1))
trpzClusterApAssignmentTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1), )
if mibBuilder.loadTexts: trpzClusterApAssignmentTable.setStatus('current')
trpzClusterApAssignmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignApNum"))
if mibBuilder.loadTexts: trpzClusterApAssignmentEntry.setStatus('current')
trpzClusterApAssignApNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 1), TrpzApNum())
if mibBuilder.loadTexts: trpzClusterApAssignApNum.setStatus('current')
trpzClusterApAssignPamIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClusterApAssignPamIp.setStatus('current')
trpzClusterApAssignSamIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClusterApAssignSamIp.setStatus('current')
trpzClusterApAssignConnectedToPam = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClusterApAssignConnectedToPam.setStatus('current')
trpzClusterApAssignConnectedToSam = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 21, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzClusterApAssignConnectedToSam.setStatus('current')
trpzClusterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 21, 2))
trpzClusterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 1))
trpzClusterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 2))
trpzClusterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignmentGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClusterCompliance = trpzClusterCompliance.setStatus('current')
trpzClusterApAssignmentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 21, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignPamIp"), ("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignSamIp"), ("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignConnectedToPam"), ("TRAPEZE-NETWORKS-CLUSTER-MIB", "trpzClusterApAssignConnectedToSam"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzClusterApAssignmentGroup = trpzClusterApAssignmentGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-CLUSTER-MIB", trpzClusterMibObjects=trpzClusterMibObjects, trpzClusterApAssignApNum=trpzClusterApAssignApNum, trpzClusterApAssignPamIp=trpzClusterApAssignPamIp, trpzClusterCompliance=trpzClusterCompliance, trpzClusterApAssignmentGroup=trpzClusterApAssignmentGroup, trpzClusterConformance=trpzClusterConformance, trpzClusterMib=trpzClusterMib, trpzClusterApAssignConnectedToSam=trpzClusterApAssignConnectedToSam, trpzClusterGroups=trpzClusterGroups, trpzClusterCompliances=trpzClusterCompliances, trpzClusterApAssignSamIp=trpzClusterApAssignSamIp, PYSNMP_MODULE_ID=trpzClusterMib, trpzClusterApAssignConnectedToPam=trpzClusterApAssignConnectedToPam, trpzClusterApAssignmentEntry=trpzClusterApAssignmentEntry, trpzClusterApAssignmentTable=trpzClusterApAssignmentTable)
