#
# PySNMP MIB module CLAB-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/CLAB-UPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
clabCommonMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabCommonMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
clabUpsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 4, 1))
clabUpsMib.setRevisions(('2018-01-18 00:00', '2010-04-28 00:00', '2009-05-06 00:00', '2007-01-19 17:00', '2005-01-28 00:00',))
if mibBuilder.loadTexts: clabUpsMib.setLastUpdated('201801180000Z')
if mibBuilder.loadTexts: clabUpsMib.setOrganization('Cable Television Laboratories, Inc.')
clabUpsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 1, 0))
clabUpsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 1, 1))
clabUpsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 1, 2))
clabUpsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 1, 2, 1))
clabUpsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 1, 2, 2))
clabSupplemtalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1))
mtaDevPwrSupplyBatteryTest = MibScalar((1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disableAutoTesting", 1), ("testScheduled", 2), ("testInProgress", 3), ("testPending", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtaDevPwrSupplyBatteryTest.setStatus('current')
mtaDevPwrSupplyConfigRunTime = MibScalar((1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 2), Integer32()).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtaDevPwrSupplyConfigRunTime.setStatus('current')
mtaDevPwrSupplyRatedMinutes = MibScalar((1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 3), Integer32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaDevPwrSupplyRatedMinutes.setStatus('current')
mtaDevPwrSupplyAvailableMinutes = MibScalar((1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 4), Integer32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaDevPwrSupplyAvailableMinutes.setStatus('current')
mtaDevPwrSupplyConfigReplaceBatteryTime = MibScalar((1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 5), Integer32()).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtaDevPwrSupplyConfigReplaceBatteryTime.setStatus('current')
mtaDevPwrSupplyFullChargeTime = MibScalar((1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtaDevPwrSupplyFullChargeTime.setStatus('current')
mtaDevPwrSupplyBatteryTestTime = MibScalar((1, 3, 6, 1, 4, 1, 4491, 4, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtaDevPwrSupplyBatteryTestTime.setStatus('current')
clabUpsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 4, 1, 2, 2, 1)).setObjects(("UPS-MIB", "upsSubsetIdentGroup"), ("UPS-MIB", "upsFullBatteryGroup"), ("UPS-MIB", "upsBasicInputGroup"), ("UPS-MIB", "upsBasicOutputGroup"), ("UPS-MIB", "upsBasicAlarmGroup"), ("UPS-MIB", "upsBasicControlGroup"), ("UPS-MIB", "upsBasicConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clabUpsMibCompliance = clabUpsMibCompliance.setStatus('current')
mibBuilder.exportSymbols("CLAB-UPS-MIB", clabUpsObjects=clabUpsObjects, clabUpsConformance=clabUpsConformance, PYSNMP_MODULE_ID=clabUpsMib, clabSupplemtalGroup=clabSupplemtalGroup, mtaDevPwrSupplyFullChargeTime=mtaDevPwrSupplyFullChargeTime, mtaDevPwrSupplyRatedMinutes=mtaDevPwrSupplyRatedMinutes, clabUpsMibCompliance=clabUpsMibCompliance, clabUpsNotifications=clabUpsNotifications, mtaDevPwrSupplyBatteryTestTime=mtaDevPwrSupplyBatteryTestTime, mtaDevPwrSupplyBatteryTest=mtaDevPwrSupplyBatteryTest, clabUpsGroups=clabUpsGroups, clabUpsMib=clabUpsMib, mtaDevPwrSupplyConfigReplaceBatteryTime=mtaDevPwrSupplyConfigReplaceBatteryTime, clabUpsCompliances=clabUpsCompliances, mtaDevPwrSupplyAvailableMinutes=mtaDevPwrSupplyAvailableMinutes, mtaDevPwrSupplyConfigRunTime=mtaDevPwrSupplyConfigRunTime)
