#
# PySNMP MIB module FS-ETHERLIKE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-ETHERLIKE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
IfIndex, = mibBuilder.importSymbols("FS-TC", "IfIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-ETHERLIKE-MIB", fsEtherlikeMIBCompliances=fsEtherlikeMIBCompliances, fsEtherlikeTable=fsEtherlikeTable, fsEtherlikeMIBObjects=fsEtherlikeMIBObjects, fsLocIfCollisions=fsLocIfCollisions, fsEtherlikeIfIndex=fsEtherlikeIfIndex, fsEtherlikeMIB=fsEtherlikeMIB, PYSNMP_MODULE_ID=fsEtherlikeMIB, fsEtherlikeMIBConformance=fsEtherlikeMIBConformance, fsEtherlikeEntry=fsEtherlikeEntry, fsEtherlikeMIBGroups=fsEtherlikeMIBGroups, fsEtherlikeMIBCompliance=fsEtherlikeMIBCompliance, fscollisionMIBGroups=fscollisionMIBGroups)
