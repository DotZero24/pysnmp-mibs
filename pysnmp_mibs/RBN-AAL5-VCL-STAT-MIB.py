#
# PySNMP MIB module RBN-AAL5-VCL-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ericsson/RBN-AAL5-VCL-STAT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
rbnXAtmAal5VclStatEntry, = mibBuilder.importSymbols("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclStatEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnAal5VclStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 1))
rbnAal5VclStatMIB.setRevisions(('2002-05-29 00:00', '1998-04-17 16:45',))
if mibBuilder.loadTexts: rbnAal5VclStatMIB.setLastUpdated('200205290000Z')
if mibBuilder.loadTexts: rbnAal5VclStatMIB.setOrganization('RedBack Networks, Inc.')
rbnAal5VclStatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 1, 1))
rbnAtmAal5VclStatTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 1, 1, 1), )
if mibBuilder.loadTexts: rbnAtmAal5VclStatTable.setStatus('current')
rbnAtmAal5VclStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 1, 1, 1, 1), )
rbnXAtmAal5VclStatEntry.registerAugmentions(("RBN-AAL5-VCL-STAT-MIB", "rbnAtmAal5VclStatEntry"))
rbnAtmAal5VclStatEntry.setIndexNames(*rbnXAtmAal5VclStatEntry.getIndexNames())
if mibBuilder.loadTexts: rbnAtmAal5VclStatEntry.setStatus('current')
rbnAtmAal5VclOutDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAtmAal5VclOutDrops.setStatus('current')
rbnAal5VclStatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 1, 2))
rbnAal5VclStatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 1))
rbnAal5VclStatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 2))
rbnAal5VclStatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 2, 1)).setObjects(("RBN-AAL5-VCL-STAT-MIB", "rbnAal5VclStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAal5VclStatMIBCompliance = rbnAal5VclStatMIBCompliance.setStatus('current')
rbnAal5VclStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 1, 2, 1, 1)).setObjects(("RBN-AAL5-VCL-STAT-MIB", "rbnAtmAal5VclOutDrops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAal5VclStatGroup = rbnAal5VclStatGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-AAL5-VCL-STAT-MIB", rbnAtmAal5VclStatTable=rbnAtmAal5VclStatTable, rbnAal5VclStatMIBConformance=rbnAal5VclStatMIBConformance, rbnAal5VclStatMIBObjects=rbnAal5VclStatMIBObjects, rbnAtmAal5VclOutDrops=rbnAtmAal5VclOutDrops, rbnAal5VclStatMIBCompliances=rbnAal5VclStatMIBCompliances, rbnAal5VclStatMIB=rbnAal5VclStatMIB, rbnAal5VclStatGroup=rbnAal5VclStatGroup, PYSNMP_MODULE_ID=rbnAal5VclStatMIB, rbnAal5VclStatMIBGroups=rbnAal5VclStatMIBGroups, rbnAtmAal5VclStatEntry=rbnAtmAal5VclStatEntry, rbnAal5VclStatMIBCompliance=rbnAal5VclStatMIBCompliance)
