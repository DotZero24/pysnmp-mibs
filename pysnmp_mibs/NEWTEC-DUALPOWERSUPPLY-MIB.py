#
# PySNMP MIB module NEWTEC-DUALPOWERSUPPLY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/newtec/NEWTEC-DUALPOWERSUPPLY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
NtcAlarmState, = mibBuilder.importSymbols("NEWTEC-TC-MIB", "NtcAlarmState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntcDualPowerSupply = ModuleIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000))
ntcDualPowerSupply.setRevisions(('2012-11-13 12:00',))
if mibBuilder.loadTexts: ntcDualPowerSupply.setLastUpdated('201211131200Z')
if mibBuilder.loadTexts: ntcDualPowerSupply.setOrganization('Newtec Cy')
ntcDualPSObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 1))
if mibBuilder.loadTexts: ntcDualPSObjects.setStatus('current')
ntcDualPSConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 2))
if mibBuilder.loadTexts: ntcDualPSConformance.setStatus('current')
ntcDualPSAlarm = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 1, 1))
if mibBuilder.loadTexts: ntcDualPSAlarm.setStatus('current')
ntcDualPSConfCompliance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 2, 1))
if mibBuilder.loadTexts: ntcDualPSConfCompliance.setStatus('current')
ntcDualPSConfGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 2, 2))
if mibBuilder.loadTexts: ntcDualPSConfGroup.setStatus('current')
ntcDualPSAlmPowerSupplyAFailure = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 1, 1, 1), NtcAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcDualPSAlmPowerSupplyAFailure.setStatus('current')
ntcDualPSAlmPowerSupplyBFailure = MibScalar((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 1, 1, 2), NtcAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcDualPSAlmPowerSupplyBFailure.setStatus('current')
ntcDualPSConfGrpV1Standard = ObjectGroup((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 2, 2, 1)).setObjects(("NEWTEC-DUALPOWERSUPPLY-MIB", "ntcDualPSAlmPowerSupplyAFailure"), ("NEWTEC-DUALPOWERSUPPLY-MIB", "ntcDualPSAlmPowerSupplyBFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcDualPSConfGrpV1Standard = ntcDualPSConfGrpV1Standard.setStatus('current')
ntcDualPSConfCompV1Standard = ModuleCompliance((1, 3, 6, 1, 4, 1, 5835, 5, 2, 3000, 2, 1, 1)).setObjects(("NEWTEC-DUALPOWERSUPPLY-MIB", "ntcDualPSConfGrpV1Standard"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcDualPSConfCompV1Standard = ntcDualPSConfCompV1Standard.setStatus('current')
mibBuilder.exportSymbols("NEWTEC-DUALPOWERSUPPLY-MIB", ntcDualPSAlmPowerSupplyAFailure=ntcDualPSAlmPowerSupplyAFailure, ntcDualPSAlarm=ntcDualPSAlarm, PYSNMP_MODULE_ID=ntcDualPowerSupply, ntcDualPSConfCompliance=ntcDualPSConfCompliance, ntcDualPSAlmPowerSupplyBFailure=ntcDualPSAlmPowerSupplyBFailure, ntcDualPSConfCompV1Standard=ntcDualPSConfCompV1Standard, ntcDualPSConfGroup=ntcDualPSConfGroup, ntcDualPSConformance=ntcDualPSConformance, ntcDualPSObjects=ntcDualPSObjects, ntcDualPowerSupply=ntcDualPowerSupply, ntcDualPSConfGrpV1Standard=ntcDualPSConfGrpV1Standard)
