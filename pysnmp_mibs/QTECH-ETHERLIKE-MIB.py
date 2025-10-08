#
# PySNMP MIB module QTECH-ETHERLIKE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-ETHERLIKE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
IfIndex, = mibBuilder.importSymbols("QTECH-TC", "IfIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-ETHERLIKE-MIB", qtechEtherlikeMIBConformance=qtechEtherlikeMIBConformance, qtechcollisionMIBGroups=qtechcollisionMIBGroups, qtechEtherlikeEntry=qtechEtherlikeEntry, PYSNMP_MODULE_ID=qtechEtherlikeMIB, qtechEtherlikeTable=qtechEtherlikeTable, qtechEtherlikeMIBCompliance=qtechEtherlikeMIBCompliance, qtechEtherlikeIfIndex=qtechEtherlikeIfIndex, qtechEtherlikeMIBGroups=qtechEtherlikeMIBGroups, qtechEtherlikeMIBCompliances=qtechEtherlikeMIBCompliances, qtechLocIfCollisions=qtechLocIfCollisions, qtechEtherlikeMIB=qtechEtherlikeMIB, qtechEtherlikeMIBObjects=qtechEtherlikeMIBObjects)
