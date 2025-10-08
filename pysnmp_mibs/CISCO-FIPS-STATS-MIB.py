#
# PySNMP MIB module CISCO-FIPS-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-FIPS-STATS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFipsStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 999999))
ciscoFipsStatsMIB.setRevisions(('2003-03-10 00:00',))
if mibBuilder.loadTexts: ciscoFipsStatsMIB.setLastUpdated('200303100000Z')
if mibBuilder.loadTexts: ciscoFipsStatsMIB.setOrganization('Cisco Systems, Inc.')
ciscoFipsStatsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 0))
ciscoFipsStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1))
ciscoFipsStatsMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2))
cfipsStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1))
cfipsStatsGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1))
cfipsPostStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 999999, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("running", 1), ("passed", 2), ("failed", 3), ("notAvailable", 4))).clone('notAvailable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfipsPostStatus.setStatus('current')
ciscoFipsStatsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1))
ciscoFipsStatsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2))
ciscoFipsStatsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 1, 1)).setObjects(("CISCO-FIPS-STATS-MIB", "ciscoFipsStatsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFipsStatsMIBCompliance = ciscoFipsStatsMIBCompliance.setStatus('current')
ciscoFipsStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 999999, 2, 2, 1)).setObjects(("CISCO-FIPS-STATS-MIB", "cfipsPostStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFipsStatsMIBGroup = ciscoFipsStatsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FIPS-STATS-MIB", ciscoFipsStatsMIBObjects=ciscoFipsStatsMIBObjects, cfipsPostStatus=cfipsPostStatus, ciscoFipsStatsMIBCompliances=ciscoFipsStatsMIBCompliances, ciscoFipsStatsMIBCompliance=ciscoFipsStatsMIBCompliance, cfipsStatsGlobal=cfipsStatsGlobal, ciscoFipsStatsMIBGroups=ciscoFipsStatsMIBGroups, ciscoFipsStatsMIBGroup=ciscoFipsStatsMIBGroup, PYSNMP_MODULE_ID=ciscoFipsStatsMIB, ciscoFipsStatsMIBConform=ciscoFipsStatsMIBConform, cfipsStats=cfipsStats, ciscoFipsStatsMIBNotifs=ciscoFipsStatsMIBNotifs, ciscoFipsStatsMIB=ciscoFipsStatsMIB)
