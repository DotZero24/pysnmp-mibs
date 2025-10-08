#
# PySNMP MIB module CISCO-AAL5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-AAL5-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:26:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
aal5VccEntry, = mibBuilder.importSymbols("ATM-MIB", "aal5VccEntry")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-AAL5-MIB", cAal5VccEntry=cAal5VccEntry, cAal5VccHCOutPkts=cAal5VccHCOutPkts, cAal5VccOutPkts=cAal5VccOutPkts, PYSNMP_MODULE_ID=ciscoAal5MIB, cAal5VccInDroppedPkts=cAal5VccInDroppedPkts, ciscoAal5MIBComplianceRev1=ciscoAal5MIBComplianceRev1, cAal5VccTable=cAal5VccTable, ciscoAal5MIBConformance=ciscoAal5MIBConformance, cAal5VccHCInPkts=cAal5VccHCInPkts, cAal5VccOutOctets=cAal5VccOutOctets, cAal5VccOutDroppedPkts=cAal5VccOutDroppedPkts, ciscoAal5MIBGroup=ciscoAal5MIBGroup, ciscoAal5MIBHCGroup=ciscoAal5MIBHCGroup, cAal5VccInDroppedOctets=cAal5VccInDroppedOctets, ciscoAal5MIBCompliances=ciscoAal5MIBCompliances, ciscoAal5MIB=ciscoAal5MIB, ciscoAal5VcStatsExtMIBGroup=ciscoAal5VcStatsExtMIBGroup, cAal5VccInOctets=cAal5VccInOctets, ciscoAal5MIBComplianceRev2=ciscoAal5MIBComplianceRev2, cAal5VccOutDroppedOctets=cAal5VccOutDroppedOctets, cAal5VccHCInOctets=cAal5VccHCInOctets, ciscoAal5MIBObjects=ciscoAal5MIBObjects, ciscoAal5MIBGroups=ciscoAal5MIBGroups, cAal5Connections=cAal5Connections, cAal5VccInPkts=cAal5VccInPkts, ciscoAal5MIBCompliance=ciscoAal5MIBCompliance, cAal5VccHCOutOctets=cAal5VccHCOutOctets)
