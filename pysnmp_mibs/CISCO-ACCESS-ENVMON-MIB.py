#
# PySNMP MIB module CISCO-ACCESS-ENVMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-ACCESS-ENVMON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoEnvMonVoltageStatusDescr, ciscoEnvMonTemperatureState, ciscoEnvMonVoltageState, ciscoEnvMonSupplyStatusEntry, ciscoEnvMonTemperatureStatusDescr = mibBuilder.importSymbols("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr", "ciscoEnvMonTemperatureState", "ciscoEnvMonVoltageState", "ciscoEnvMonSupplyStatusEntry", "ciscoEnvMonTemperatureStatusDescr")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAccessEnvMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 61))
ciscoAccessEnvMonMIB.setRevisions(('1998-08-05 00:00',))
if mibBuilder.loadTexts: ciscoAccessEnvMonMIB.setLastUpdated('9808050000Z')
if mibBuilder.loadTexts: ciscoAccessEnvMonMIB.setOrganization('Cisco Systems, Inc.')
caemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 1))
caemSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1), )
if mibBuilder.loadTexts: caemSupplyStatusTable.setStatus('current')
caemSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1), )
ciscoEnvMonSupplyStatusEntry.registerAugmentions(("CISCO-ACCESS-ENVMON-MIB", "caemSupplyStatusEntry"))
caemSupplyStatusEntry.setIndexNames(*ciscoEnvMonSupplyStatusEntry.getIndexNames())
if mibBuilder.loadTexts: caemSupplyStatusEntry.setStatus('current')
caemSupplyFailedComponent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 61, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("inputVoltage", 2), ("dcOutputVoltage", 3), ("thermal", 4), ("multiple", 5), ("fan", 6), ("overvoltage", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: caemSupplyFailedComponent.setStatus('current')
caemMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 2))
caemMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0))
caemTemperatureNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 1)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonTemperatureState"))
if mibBuilder.loadTexts: caemTemperatureNotification.setStatus('current')
caemVoltageNotification = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 61, 2, 0, 2)).setObjects(("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageStatusDescr"), ("CISCO-ENVMON-MIB", "ciscoEnvMonVoltageState"))
if mibBuilder.loadTexts: caemVoltageNotification.setStatus('current')
caemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3))
caemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 1))
caemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2))
caemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 1, 1)).setObjects(("CISCO-ACCESS-ENVMON-MIB", "caemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caemCompliance = caemCompliance.setStatus('current')
caemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 61, 3, 2, 1)).setObjects(("CISCO-ACCESS-ENVMON-MIB", "caemSupplyFailedComponent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    caemGroup = caemGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ACCESS-ENVMON-MIB", caemGroup=caemGroup, caemObjects=caemObjects, caemConformance=caemConformance, ciscoAccessEnvMonMIB=ciscoAccessEnvMonMIB, PYSNMP_MODULE_ID=ciscoAccessEnvMonMIB, caemMIBNotificationPrefix=caemMIBNotificationPrefix, caemCompliance=caemCompliance, caemCompliances=caemCompliances, caemGroups=caemGroups, caemVoltageNotification=caemVoltageNotification, caemTemperatureNotification=caemTemperatureNotification, caemSupplyFailedComponent=caemSupplyFailedComponent, caemSupplyStatusTable=caemSupplyStatusTable, caemSupplyStatusEntry=caemSupplyStatusEntry, caemMIBNotifications=caemMIBNotifications)
