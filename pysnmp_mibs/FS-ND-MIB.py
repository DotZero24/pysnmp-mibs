#
# PySNMP MIB module FS-ND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-ND-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsNDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125))
fsNDMIB.setRevisions(('2013-12-30 00:00',))
if mibBuilder.loadTexts: fsNDMIB.setLastUpdated('201312300000Z')
if mibBuilder.loadTexts: fsNDMIB.setOrganization('FS Networks.')
fsNDMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 1))
fsNDTotalActiveNeighbors = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsNDTotalActiveNeighbors.setStatus('current')
fsNDTotalActiveDynamicNeighbors = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsNDTotalActiveDynamicNeighbors.setStatus('current')
fsNDTotalStaticNeighbors = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsNDTotalStaticNeighbors.setStatus('current')
fsNDTotalActiveStaticNeighbors = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsNDTotalActiveStaticNeighbors.setStatus('current')
fsNDMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 2))
fsNDMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 2, 1))
fsNDMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 2, 2))
fsNDMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 2, 1, 1)).setObjects(("FS-ND-MIB", "fsNDObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsNDMIBCompliance = fsNDMIBCompliance.setStatus('current')
fsNDObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 125, 2, 2, 1)).setObjects(("FS-ND-MIB", "fsNDTotalActiveNeighbors"), ("FS-ND-MIB", "fsNDTotalActiveDynamicNeighbors"), ("FS-ND-MIB", "fsNDTotalStaticNeighbors"), ("FS-ND-MIB", "fsNDTotalActiveStaticNeighbors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsNDObjectsGroup = fsNDObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("FS-ND-MIB", fsNDTotalStaticNeighbors=fsNDTotalStaticNeighbors, fsNDMIBGroups=fsNDMIBGroups, fsNDTotalActiveStaticNeighbors=fsNDTotalActiveStaticNeighbors, fsNDObjectsGroup=fsNDObjectsGroup, fsNDMIBConformance=fsNDMIBConformance, fsNDTotalActiveNeighbors=fsNDTotalActiveNeighbors, fsNDMIB=fsNDMIB, PYSNMP_MODULE_ID=fsNDMIB, fsNDTotalActiveDynamicNeighbors=fsNDTotalActiveDynamicNeighbors, fsNDMIBCompliance=fsNDMIBCompliance, fsNDMIBObjects=fsNDMIBObjects, fsNDMIBCompliances=fsNDMIBCompliances)
