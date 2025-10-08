#
# PySNMP MIB module QTECH-ND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-ND-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-ND-MIB", qtechNDMIBCompliances=qtechNDMIBCompliances, PYSNMP_MODULE_ID=qtechNDMIB, qtechNDMIBCompliance=qtechNDMIBCompliance, qtechNDTotalActiveStaticNeighbors=qtechNDTotalActiveStaticNeighbors, qtechNDTotalActiveDynamicNeighbors=qtechNDTotalActiveDynamicNeighbors, qtechNDMIBConformance=qtechNDMIBConformance, qtechNDMIB=qtechNDMIB, qtechNDObjectsGroup=qtechNDObjectsGroup, qtechNDTotalStaticNeighbors=qtechNDTotalStaticNeighbors, qtechNDMIBObjects=qtechNDMIBObjects, qtechNDMIBGroups=qtechNDMIBGroups, qtechNDTotalActiveNeighbors=qtechNDTotalActiveNeighbors)
