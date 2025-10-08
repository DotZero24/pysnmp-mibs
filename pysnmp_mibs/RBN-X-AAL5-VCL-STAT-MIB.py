#
# PySNMP MIB module RBN-X-AAL5-VCL-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ericsson/RBN-X-AAL5-VCL-STAT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
atmVclVpi, atmVclVci = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi", "atmVclVci")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rbnExperiment, = mibBuilder.importSymbols("RBN-SMI", "rbnExperiment")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnXAal5VclStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 3, 1))
if mibBuilder.loadTexts: rbnXAal5VclStatMIB.setLastUpdated('9804171645Z')
if mibBuilder.loadTexts: rbnXAal5VclStatMIB.setOrganization('RedBack Networks, Inc.')
rbnXAal5VclStatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1))
rbnXAtmAal5VclStatTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1), )
if mibBuilder.loadTexts: rbnXAtmAal5VclStatTable.setStatus('deprecated')
rbnXAtmAal5VclStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: rbnXAtmAal5VclStatEntry.setStatus('deprecated')
rbnXAtmAal5VclInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclInPkts.setStatus('deprecated')
rbnXAtmAal5VclOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclOutPkts.setStatus('deprecated')
rbnXAtmAal5VclInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclInOctets.setStatus('deprecated')
rbnXAtmAal5VclOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 3, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnXAtmAal5VclOutOctets.setStatus('deprecated')
rbnXAal5VclStatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2))
rbnXAal5VclStatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 1))
rbnXAal5VclStatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 2))
rbnXAal5VclStatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 2, 1)).setObjects(("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAal5VclStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnXAal5VclStatMIBCompliance = rbnXAal5VclStatMIBCompliance.setStatus('current')
rbnXAal5VclStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 3, 1, 2, 1, 1)).setObjects(("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclInPkts"), ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclOutPkts"), ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclInOctets"), ("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnXAal5VclStatGroup = rbnXAal5VclStatGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-X-AAL5-VCL-STAT-MIB", rbnXAtmAal5VclOutOctets=rbnXAtmAal5VclOutOctets, rbnXAtmAal5VclStatEntry=rbnXAtmAal5VclStatEntry, rbnXAal5VclStatGroup=rbnXAal5VclStatGroup, rbnXAal5VclStatMIB=rbnXAal5VclStatMIB, rbnXAal5VclStatMIBCompliance=rbnXAal5VclStatMIBCompliance, rbnXAal5VclStatMIBConformance=rbnXAal5VclStatMIBConformance, PYSNMP_MODULE_ID=rbnXAal5VclStatMIB, rbnXAtmAal5VclInOctets=rbnXAtmAal5VclInOctets, rbnXAtmAal5VclStatTable=rbnXAtmAal5VclStatTable, rbnXAal5VclStatMIBGroups=rbnXAal5VclStatMIBGroups, rbnXAal5VclStatMIBObjects=rbnXAal5VclStatMIBObjects, rbnXAtmAal5VclInPkts=rbnXAtmAal5VclInPkts, rbnXAtmAal5VclOutPkts=rbnXAtmAal5VclOutPkts, rbnXAal5VclStatMIBCompliances=rbnXAal5VclStatMIBCompliances)
