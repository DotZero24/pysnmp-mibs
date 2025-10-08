#
# PySNMP MIB module QTECH-ETHERLIKE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-ETHERLIKE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
IfIndex, = mibBuilder.importSymbols("QTECH-TC", "IfIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qtechEtherlikeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55))
qtechEtherlikeMIB.setRevisions(('2009-09-17 00:00',))
if mibBuilder.loadTexts: qtechEtherlikeMIB.setLastUpdated('200909170000Z')
if mibBuilder.loadTexts: qtechEtherlikeMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechEtherlikeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 1))
qtechEtherlikeTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 1, 1), )
if mibBuilder.loadTexts: qtechEtherlikeTable.setStatus('current')
qtechEtherlikeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 1, 1, 1), ).setIndexNames((0, "QTECH-ETHERLIKE-MIB", "qtechEtherlikeIfIndex"))
if mibBuilder.loadTexts: qtechEtherlikeEntry.setStatus('current')
qtechEtherlikeIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 1, 1, 1, 1), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechEtherlikeIfIndex.setStatus('current')
qtechLocIfCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechLocIfCollisions.setStatus('current')
qtechEtherlikeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 3))
qtechEtherlikeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 3, 1))
qtechEtherlikeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 3, 2))
qtechEtherlikeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 3, 1, 1)).setObjects(("QTECH-ETHERLIKE-MIB", "qtechcollisionMIBGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechEtherlikeMIBCompliance = qtechEtherlikeMIBCompliance.setStatus('current')
qtechcollisionMIBGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 55, 3, 2, 1)).setObjects(("QTECH-ETHERLIKE-MIB", "qtechEtherlikeIfIndex"), ("QTECH-ETHERLIKE-MIB", "qtechLocIfCollisions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechcollisionMIBGroups = qtechcollisionMIBGroups.setStatus('current')
mibBuilder.exportSymbols("QTECH-ETHERLIKE-MIB", qtechEtherlikeMIBObjects=qtechEtherlikeMIBObjects, qtechEtherlikeMIBCompliance=qtechEtherlikeMIBCompliance, qtechEtherlikeTable=qtechEtherlikeTable, qtechEtherlikeEntry=qtechEtherlikeEntry, PYSNMP_MODULE_ID=qtechEtherlikeMIB, qtechEtherlikeMIB=qtechEtherlikeMIB, qtechEtherlikeMIBCompliances=qtechEtherlikeMIBCompliances, qtechEtherlikeMIBConformance=qtechEtherlikeMIBConformance, qtechEtherlikeIfIndex=qtechEtherlikeIfIndex, qtechcollisionMIBGroups=qtechcollisionMIBGroups, qtechLocIfCollisions=qtechLocIfCollisions, qtechEtherlikeMIBGroups=qtechEtherlikeMIBGroups)
