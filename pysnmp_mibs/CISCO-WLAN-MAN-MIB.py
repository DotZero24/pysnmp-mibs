#
# PySNMP MIB module CISCO-WLAN-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-WLAN-MAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:13:11 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoWlanManMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 415))
ciscoWlanManMIB.setRevisions(('2004-03-22 00:00',))
if mibBuilder.loadTexts: ciscoWlanManMIB.setLastUpdated('200403220000Z')
if mibBuilder.loadTexts: ciscoWlanManMIB.setOrganization('Cisco System Inc.')
ciscoWlanManMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 0))
ciscoWlanManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1))
ciscoWlanManMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2))
cwmDeviceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1))
cwmNetworkConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 2))
cwmHttpServerEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmHttpServerEnabled.setStatus('current')
cwmTelnetLoginEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmTelnetLoginEnabled.setStatus('current')
ciscoWlanManMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1))
ciscoWlanManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2))
ciscoWlanManMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1, 1)).setObjects(("CISCO-WLAN-MAN-MIB", "cwmWirelessDeviceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWlanManMIBCompliance = ciscoWlanManMIBCompliance.setStatus('current')
cwmWirelessDeviceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2, 1)).setObjects(("CISCO-WLAN-MAN-MIB", "cwmHttpServerEnabled"), ("CISCO-WLAN-MAN-MIB", "cwmTelnetLoginEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmWirelessDeviceGroup = cwmWirelessDeviceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WLAN-MAN-MIB", ciscoWlanManMIBNotifs=ciscoWlanManMIBNotifs, cwmWirelessDeviceGroup=cwmWirelessDeviceGroup, cwmTelnetLoginEnabled=cwmTelnetLoginEnabled, ciscoWlanManMIB=ciscoWlanManMIB, PYSNMP_MODULE_ID=ciscoWlanManMIB, cwmHttpServerEnabled=cwmHttpServerEnabled, ciscoWlanManMIBCompliances=ciscoWlanManMIBCompliances, ciscoWlanManMIBGroups=ciscoWlanManMIBGroups, cwmNetworkConfig=cwmNetworkConfig, ciscoWlanManMIBObjects=ciscoWlanManMIBObjects, cwmDeviceConfig=cwmDeviceConfig, ciscoWlanManMIBConform=ciscoWlanManMIBConform, ciscoWlanManMIBCompliance=ciscoWlanManMIBCompliance)
