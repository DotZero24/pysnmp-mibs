#
# PySNMP MIB module FS-ETHERLIKE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-ETHERLIKE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
IfIndex, = mibBuilder.importSymbols("FS-TC", "IfIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsEtherlikeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55))
fsEtherlikeMIB.setRevisions(('2009-09-17 00:00',))
if mibBuilder.loadTexts: fsEtherlikeMIB.setLastUpdated('200909170000Z')
if mibBuilder.loadTexts: fsEtherlikeMIB.setOrganization('FS.COM Inc..')
fsEtherlikeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 1))
fsEtherlikeTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 1, 1), )
if mibBuilder.loadTexts: fsEtherlikeTable.setStatus('current')
fsEtherlikeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 1, 1, 1), ).setIndexNames((0, "FS-ETHERLIKE-MIB", "fsEtherlikeIfIndex"))
if mibBuilder.loadTexts: fsEtherlikeEntry.setStatus('current')
fsEtherlikeIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 1, 1, 1, 1), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsEtherlikeIfIndex.setStatus('current')
fsLocIfCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsLocIfCollisions.setStatus('current')
fsEtherlikeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 3))
fsEtherlikeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 3, 1))
fsEtherlikeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 3, 2))
fsEtherlikeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 3, 1, 1)).setObjects(("FS-ETHERLIKE-MIB", "fscollisionMIBGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsEtherlikeMIBCompliance = fsEtherlikeMIBCompliance.setStatus('current')
fscollisionMIBGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 55, 3, 2, 1)).setObjects(("FS-ETHERLIKE-MIB", "fsEtherlikeIfIndex"), ("FS-ETHERLIKE-MIB", "fsLocIfCollisions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fscollisionMIBGroups = fscollisionMIBGroups.setStatus('current')
mibBuilder.exportSymbols("FS-ETHERLIKE-MIB", fsEtherlikeMIB=fsEtherlikeMIB, fsLocIfCollisions=fsLocIfCollisions, fsEtherlikeEntry=fsEtherlikeEntry, fsEtherlikeMIBCompliances=fsEtherlikeMIBCompliances, fsEtherlikeMIBCompliance=fsEtherlikeMIBCompliance, fscollisionMIBGroups=fscollisionMIBGroups, fsEtherlikeTable=fsEtherlikeTable, fsEtherlikeMIBConformance=fsEtherlikeMIBConformance, fsEtherlikeIfIndex=fsEtherlikeIfIndex, fsEtherlikeMIBObjects=fsEtherlikeMIBObjects, fsEtherlikeMIBGroups=fsEtherlikeMIBGroups, PYSNMP_MODULE_ID=fsEtherlikeMIB)
