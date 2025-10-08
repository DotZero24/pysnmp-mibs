#
# PySNMP MIB module OA-SL-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mrv/OA-SL-STATISTICS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("OA-SL-STATISTICS-MIB", nbPortParams=nbPortParams, oaSlStatAggrOctets=oaSlStatAggrOctets, oaSlStatMIBCompliance=oaSlStatMIBCompliance, oaSlStatConformance=oaSlStatConformance, oaSlStatPortIndex=oaSlStatPortIndex, oaSlStatTable=oaSlStatTable, nbase=nbase, oaSlStatMandatoryGroup=oaSlStatMandatoryGroup, oaSlStatistics=oaSlStatistics, oaSlStatEntry=oaSlStatEntry, oaSlStatMIBCompliances=oaSlStatMIBCompliances, PYSNMP_MODULE_ID=oaSlStatistics, nbSwitchG1Il=nbSwitchG1Il, nbSwitchG1=nbSwitchG1, oaSlStatServiceLevel=oaSlStatServiceLevel, oaSlStatMIBGroups=oaSlStatMIBGroups, oaSlStatGenSupport=oaSlStatGenSupport)
