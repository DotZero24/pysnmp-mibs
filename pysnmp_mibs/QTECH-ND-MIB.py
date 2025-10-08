#
# PySNMP MIB module QTECH-ND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-ND-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qtechNDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125))
qtechNDMIB.setRevisions(('2013-12-30 00:00',))
if mibBuilder.loadTexts: qtechNDMIB.setLastUpdated('201312300000Z')
if mibBuilder.loadTexts: qtechNDMIB.setOrganization('Qtech Networks.')
qtechNDMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 1))
qtechNDTotalActiveNeighbors = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechNDTotalActiveNeighbors.setStatus('current')
qtechNDTotalActiveDynamicNeighbors = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechNDTotalActiveDynamicNeighbors.setStatus('current')
qtechNDTotalStaticNeighbors = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechNDTotalStaticNeighbors.setStatus('current')
qtechNDTotalActiveStaticNeighbors = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechNDTotalActiveStaticNeighbors.setStatus('current')
qtechNDMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 2))
qtechNDMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 2, 1))
qtechNDMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 2, 2))
qtechNDMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 2, 1, 1)).setObjects(("QTECH-ND-MIB", "qtechNDObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechNDMIBCompliance = qtechNDMIBCompliance.setStatus('current')
qtechNDObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 125, 2, 2, 1)).setObjects(("QTECH-ND-MIB", "qtechNDTotalActiveNeighbors"), ("QTECH-ND-MIB", "qtechNDTotalActiveDynamicNeighbors"), ("QTECH-ND-MIB", "qtechNDTotalStaticNeighbors"), ("QTECH-ND-MIB", "qtechNDTotalActiveStaticNeighbors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechNDObjectsGroup = qtechNDObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-ND-MIB", qtechNDMIBObjects=qtechNDMIBObjects, qtechNDTotalActiveNeighbors=qtechNDTotalActiveNeighbors, qtechNDTotalActiveDynamicNeighbors=qtechNDTotalActiveDynamicNeighbors, qtechNDMIBConformance=qtechNDMIBConformance, qtechNDMIBGroups=qtechNDMIBGroups, qtechNDMIBCompliance=qtechNDMIBCompliance, qtechNDTotalActiveStaticNeighbors=qtechNDTotalActiveStaticNeighbors, qtechNDMIBCompliances=qtechNDMIBCompliances, qtechNDTotalStaticNeighbors=qtechNDTotalStaticNeighbors, qtechNDMIB=qtechNDMIB, PYSNMP_MODULE_ID=qtechNDMIB, qtechNDObjectsGroup=qtechNDObjectsGroup)
