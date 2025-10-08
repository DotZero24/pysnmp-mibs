#
# PySNMP MIB module FS-ND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-ND-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-ND-MIB", fsNDMIBObjects=fsNDMIBObjects, fsNDMIBCompliance=fsNDMIBCompliance, fsNDTotalActiveStaticNeighbors=fsNDTotalActiveStaticNeighbors, fsNDTotalActiveNeighbors=fsNDTotalActiveNeighbors, fsNDTotalActiveDynamicNeighbors=fsNDTotalActiveDynamicNeighbors, fsNDMIB=fsNDMIB, fsNDMIBCompliances=fsNDMIBCompliances, PYSNMP_MODULE_ID=fsNDMIB, fsNDMIBConformance=fsNDMIBConformance, fsNDObjectsGroup=fsNDObjectsGroup, fsNDTotalStaticNeighbors=fsNDTotalStaticNeighbors, fsNDMIBGroups=fsNDMIBGroups)
