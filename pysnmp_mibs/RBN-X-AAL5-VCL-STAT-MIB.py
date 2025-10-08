#
# PySNMP MIB module RBN-X-AAL5-VCL-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ericsson/RBN-X-AAL5-VCL-STAT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
atmVclVci, atmVclVpi = mibBuilder.importSymbols("ATM-MIB", "atmVclVci", "atmVclVpi")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rbnExperiment, = mibBuilder.importSymbols("RBN-SMI", "rbnExperiment")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RBN-X-AAL5-VCL-STAT-MIB", PYSNMP_MODULE_ID=rbnXAal5VclStatMIB, rbnXAtmAal5VclInPkts=rbnXAtmAal5VclInPkts, rbnXAtmAal5VclInOctets=rbnXAtmAal5VclInOctets, rbnXAal5VclStatMIBConformance=rbnXAal5VclStatMIBConformance, rbnXAal5VclStatGroup=rbnXAal5VclStatGroup, rbnXAal5VclStatMIB=rbnXAal5VclStatMIB, rbnXAtmAal5VclStatEntry=rbnXAtmAal5VclStatEntry, rbnXAal5VclStatMIBObjects=rbnXAal5VclStatMIBObjects, rbnXAtmAal5VclStatTable=rbnXAtmAal5VclStatTable, rbnXAtmAal5VclOutPkts=rbnXAtmAal5VclOutPkts, rbnXAtmAal5VclOutOctets=rbnXAtmAal5VclOutOctets, rbnXAal5VclStatMIBCompliances=rbnXAal5VclStatMIBCompliances, rbnXAal5VclStatMIBGroups=rbnXAal5VclStatMIBGroups, rbnXAal5VclStatMIBCompliance=rbnXAal5VclStatMIBCompliance)
