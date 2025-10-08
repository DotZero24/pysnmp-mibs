#
# PySNMP MIB module TRAPEZE-NETWORKS-CLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-CLUSTER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-CLUSTER-MIB", trpzClusterApAssignmentEntry=trpzClusterApAssignmentEntry, PYSNMP_MODULE_ID=trpzClusterMib, trpzClusterCompliance=trpzClusterCompliance, trpzClusterApAssignApNum=trpzClusterApAssignApNum, trpzClusterApAssignPamIp=trpzClusterApAssignPamIp, trpzClusterCompliances=trpzClusterCompliances, trpzClusterApAssignSamIp=trpzClusterApAssignSamIp, trpzClusterApAssignConnectedToPam=trpzClusterApAssignConnectedToPam, trpzClusterMib=trpzClusterMib, trpzClusterGroups=trpzClusterGroups, trpzClusterApAssignmentGroup=trpzClusterApAssignmentGroup, trpzClusterApAssignConnectedToSam=trpzClusterApAssignConnectedToSam, trpzClusterApAssignmentTable=trpzClusterApAssignmentTable, trpzClusterMibObjects=trpzClusterMibObjects, trpzClusterConformance=trpzClusterConformance)
