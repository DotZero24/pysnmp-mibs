#
# PySNMP MIB module CLAB-UPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/CLAB-UPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
clabCommonMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabCommonMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CLAB-UPS-MIB", clabUpsGroups=clabUpsGroups, mtaDevPwrSupplyBatteryTest=mtaDevPwrSupplyBatteryTest, mtaDevPwrSupplyFullChargeTime=mtaDevPwrSupplyFullChargeTime, mtaDevPwrSupplyAvailableMinutes=mtaDevPwrSupplyAvailableMinutes, clabUpsConformance=clabUpsConformance, mtaDevPwrSupplyConfigRunTime=mtaDevPwrSupplyConfigRunTime, mtaDevPwrSupplyConfigReplaceBatteryTime=mtaDevPwrSupplyConfigReplaceBatteryTime, clabUpsCompliances=clabUpsCompliances, clabUpsMib=clabUpsMib, PYSNMP_MODULE_ID=clabUpsMib, clabUpsNotifications=clabUpsNotifications, clabUpsMibCompliance=clabUpsMibCompliance, clabSupplemtalGroup=clabSupplemtalGroup, clabUpsObjects=clabUpsObjects, mtaDevPwrSupplyBatteryTestTime=mtaDevPwrSupplyBatteryTestTime, mtaDevPwrSupplyRatedMinutes=mtaDevPwrSupplyRatedMinutes)
