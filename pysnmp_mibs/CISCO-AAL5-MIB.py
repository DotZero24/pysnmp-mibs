#
# PySNMP MIB module CISCO-AAL5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-AAL5-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
aal5VccEntry, = mibBuilder.importSymbols("ATM-MIB", "aal5VccEntry")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAal5MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 66))
ciscoAal5MIB.setRevisions(('2003-09-22 00:00', '2002-10-17 00:00', '1996-11-15 00:00',))
if mibBuilder.loadTexts: ciscoAal5MIB.setLastUpdated('200309220000Z')
if mibBuilder.loadTexts: ciscoAal5MIB.setOrganization('Cisco Systems, Inc.')
ciscoAal5MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 66, 1))
cAal5Connections = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1))
cAal5VccTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1), )
if mibBuilder.loadTexts: cAal5VccTable.setStatus('current')
cAal5VccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1), )
aal5VccEntry.registerAugmentions(("CISCO-AAL5-MIB", "cAal5VccEntry"))
cAal5VccEntry.setIndexNames(*aal5VccEntry.getIndexNames())
if mibBuilder.loadTexts: cAal5VccEntry.setStatus('current')
cAal5VccInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInPkts.setStatus('current')
cAal5VccOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutPkts.setStatus('current')
cAal5VccInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 3), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInOctets.setStatus('current')
cAal5VccOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 4), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutOctets.setStatus('current')
cAal5VccInDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInDroppedPkts.setStatus('current')
cAal5VccOutDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutDroppedPkts.setStatus('current')
cAal5VccInDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 7), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInDroppedOctets.setStatus('current')
cAal5VccOutDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 8), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutDroppedOctets.setStatus('current')
cAal5VccHCInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccHCInPkts.setStatus('current')
cAal5VccHCOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccHCOutPkts.setStatus('current')
cAal5VccHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccHCInOctets.setStatus('current')
cAal5VccHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccHCOutOctets.setStatus('current')
ciscoAal5MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 66, 3))
ciscoAal5MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1))
ciscoAal5MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2))
ciscoAal5MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1, 1)).setObjects(("CISCO-AAL5-MIB", "ciscoAal5MIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5MIBCompliance = ciscoAal5MIBCompliance.setStatus('deprecated')
ciscoAal5MIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1, 2)).setObjects(("CISCO-AAL5-MIB", "ciscoAal5MIBGroup"), ("CISCO-AAL5-MIB", "ciscoAal5VcStatsExtMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5MIBComplianceRev1 = ciscoAal5MIBComplianceRev1.setStatus('deprecated')
ciscoAal5MIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1, 3)).setObjects(("CISCO-AAL5-MIB", "ciscoAal5MIBGroup"), ("CISCO-AAL5-MIB", "ciscoAal5VcStatsExtMIBGroup"), ("CISCO-AAL5-MIB", "ciscoAal5MIBHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5MIBComplianceRev2 = ciscoAal5MIBComplianceRev2.setStatus('current')
ciscoAal5MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2, 1)).setObjects(("CISCO-AAL5-MIB", "cAal5VccInPkts"), ("CISCO-AAL5-MIB", "cAal5VccOutPkts"), ("CISCO-AAL5-MIB", "cAal5VccInOctets"), ("CISCO-AAL5-MIB", "cAal5VccOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5MIBGroup = ciscoAal5MIBGroup.setStatus('current')
ciscoAal5VcStatsExtMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2, 2)).setObjects(("CISCO-AAL5-MIB", "cAal5VccInDroppedPkts"), ("CISCO-AAL5-MIB", "cAal5VccOutDroppedPkts"), ("CISCO-AAL5-MIB", "cAal5VccInDroppedOctets"), ("CISCO-AAL5-MIB", "cAal5VccOutDroppedOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5VcStatsExtMIBGroup = ciscoAal5VcStatsExtMIBGroup.setStatus('current')
ciscoAal5MIBHCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2, 3)).setObjects(("CISCO-AAL5-MIB", "cAal5VccHCInPkts"), ("CISCO-AAL5-MIB", "cAal5VccHCOutPkts"), ("CISCO-AAL5-MIB", "cAal5VccHCInOctets"), ("CISCO-AAL5-MIB", "cAal5VccHCOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5MIBHCGroup = ciscoAal5MIBHCGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAL5-MIB", ciscoAal5MIBConformance=ciscoAal5MIBConformance, cAal5VccInDroppedOctets=cAal5VccInDroppedOctets, cAal5VccHCInPkts=cAal5VccHCInPkts, cAal5VccEntry=cAal5VccEntry, cAal5VccOutDroppedPkts=cAal5VccOutDroppedPkts, ciscoAal5MIB=ciscoAal5MIB, ciscoAal5MIBComplianceRev2=ciscoAal5MIBComplianceRev2, cAal5VccHCInOctets=cAal5VccHCInOctets, cAal5VccHCOutOctets=cAal5VccHCOutOctets, ciscoAal5MIBCompliances=ciscoAal5MIBCompliances, cAal5VccInDroppedPkts=cAal5VccInDroppedPkts, ciscoAal5MIBHCGroup=ciscoAal5MIBHCGroup, cAal5VccOutPkts=cAal5VccOutPkts, ciscoAal5MIBComplianceRev1=ciscoAal5MIBComplianceRev1, cAal5VccInOctets=cAal5VccInOctets, ciscoAal5MIBObjects=ciscoAal5MIBObjects, cAal5Connections=cAal5Connections, cAal5VccOutOctets=cAal5VccOutOctets, cAal5VccOutDroppedOctets=cAal5VccOutDroppedOctets, cAal5VccHCOutPkts=cAal5VccHCOutPkts, cAal5VccTable=cAal5VccTable, cAal5VccInPkts=cAal5VccInPkts, PYSNMP_MODULE_ID=ciscoAal5MIB, ciscoAal5MIBGroups=ciscoAal5MIBGroups, ciscoAal5VcStatsExtMIBGroup=ciscoAal5VcStatsExtMIBGroup, ciscoAal5MIBCompliance=ciscoAal5MIBCompliance, ciscoAal5MIBGroup=ciscoAal5MIBGroup)
