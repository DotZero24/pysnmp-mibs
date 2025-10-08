#
# PySNMP MIB module RBN-AAL5-VCL-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ericsson/RBN-AAL5-VCL-STAT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:25:45 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
rbnXAtmAal5VclStatEntry, = mibBuilder.importSymbols("RBN-X-AAL5-VCL-STAT-MIB", "rbnXAtmAal5VclStatEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("RBN-AAL5-VCL-STAT-MIB", rbnAtmAal5VclStatTable=rbnAtmAal5VclStatTable, rbnAal5VclStatGroup=rbnAal5VclStatGroup, rbnAal5VclStatMIBCompliance=rbnAal5VclStatMIBCompliance, rbnAal5VclStatMIBObjects=rbnAal5VclStatMIBObjects, rbnAal5VclStatMIBConformance=rbnAal5VclStatMIBConformance, rbnAtmAal5VclOutDrops=rbnAtmAal5VclOutDrops, rbnAal5VclStatMIB=rbnAal5VclStatMIB, PYSNMP_MODULE_ID=rbnAal5VclStatMIB, rbnAal5VclStatMIBCompliances=rbnAal5VclStatMIBCompliances, rbnAal5VclStatMIBGroups=rbnAal5VclStatMIBGroups, rbnAtmAal5VclStatEntry=rbnAtmAal5VclStatEntry)
