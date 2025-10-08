#
# PySNMP MIB module NEWTEC-DUALPOWERSUPPLY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/newtec/NEWTEC-DUALPOWERSUPPLY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntcFunction, = mibBuilder.importSymbols("NEWTEC-MAIN-MIB", "ntcFunction")
NtcAlarmState, = mibBuilder.importSymbols("NEWTEC-TC-MIB", "NtcAlarmState")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NEWTEC-DUALPOWERSUPPLY-MIB", ntcDualPSAlmPowerSupplyAFailure=ntcDualPSAlmPowerSupplyAFailure, PYSNMP_MODULE_ID=ntcDualPowerSupply, ntcDualPSConfGroup=ntcDualPSConfGroup, ntcDualPSAlmPowerSupplyBFailure=ntcDualPSAlmPowerSupplyBFailure, ntcDualPSConformance=ntcDualPSConformance, ntcDualPSObjects=ntcDualPSObjects, ntcDualPSAlarm=ntcDualPSAlarm, ntcDualPSConfGrpV1Standard=ntcDualPSConfGrpV1Standard, ntcDualPowerSupply=ntcDualPowerSupply, ntcDualPSConfCompliance=ntcDualPSConfCompliance, ntcDualPSConfCompV1Standard=ntcDualPSConfCompV1Standard)
