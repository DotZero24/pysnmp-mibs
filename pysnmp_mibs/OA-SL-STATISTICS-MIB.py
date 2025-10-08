#
# PySNMP MIB module OA-SL-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mrv/OA-SL-STATISTICS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:43 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oaSlStatistics = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9))
oaSlStatistics.setRevisions(('2007-03-18 00:00',))
if mibBuilder.loadTexts: oaSlStatistics.setLastUpdated('200703180000Z')
if mibBuilder.loadTexts: oaSlStatistics.setOrganization('MRV Communications, Inc.')
nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 629))
nbSwitchG1 = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1))
nbSwitchG1Il = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50))
nbPortParams = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10))
oaSlStatConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101))
oaSlStatGenSupport = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSlStatGenSupport.setStatus('current')
oaSlStatTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2), )
if mibBuilder.loadTexts: oaSlStatTable.setStatus('current')
oaSlStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1), ).setIndexNames((0, "OA-SL-STATISTICS-MIB", "oaSlStatPortIndex"), (0, "OA-SL-STATISTICS-MIB", "oaSlStatServiceLevel"))
if mibBuilder.loadTexts: oaSlStatEntry.setStatus('current')
oaSlStatPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSlStatPortIndex.setStatus('current')
oaSlStatServiceLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSlStatServiceLevel.setStatus('current')
oaSlStatAggrOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oaSlStatAggrOctets.setStatus('current')
oaSlStatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 1))
oaSlStatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 2))
oaSlStatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 1, 1)).setObjects(("OA-SL-STATISTICS-MIB", "oaSlStatMandatoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oaSlStatMIBCompliance = oaSlStatMIBCompliance.setStatus('current')
oaSlStatMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 9, 101, 2, 1)).setObjects(("OA-SL-STATISTICS-MIB", "oaSlStatGenSupport"), ("OA-SL-STATISTICS-MIB", "oaSlStatPortIndex"), ("OA-SL-STATISTICS-MIB", "oaSlStatServiceLevel"), ("OA-SL-STATISTICS-MIB", "oaSlStatAggrOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oaSlStatMandatoryGroup = oaSlStatMandatoryGroup.setStatus('current')
mibBuilder.exportSymbols("OA-SL-STATISTICS-MIB", oaSlStatTable=oaSlStatTable, oaSlStatMIBCompliance=oaSlStatMIBCompliance, oaSlStatEntry=oaSlStatEntry, nbSwitchG1Il=nbSwitchG1Il, oaSlStatConformance=oaSlStatConformance, oaSlStatGenSupport=oaSlStatGenSupport, oaSlStatPortIndex=oaSlStatPortIndex, oaSlStatServiceLevel=oaSlStatServiceLevel, oaSlStatMIBCompliances=oaSlStatMIBCompliances, oaSlStatMandatoryGroup=oaSlStatMandatoryGroup, PYSNMP_MODULE_ID=oaSlStatistics, oaSlStatAggrOctets=oaSlStatAggrOctets, oaSlStatistics=oaSlStatistics, oaSlStatMIBGroups=oaSlStatMIBGroups, nbPortParams=nbPortParams, nbase=nbase, nbSwitchG1=nbSwitchG1)
