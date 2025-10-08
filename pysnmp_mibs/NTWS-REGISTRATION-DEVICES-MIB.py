#
# PySNMP MIB module NTWS-REGISTRATION-DEVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NTWS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ntwsRegistration, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsRegistration")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsRegistrationDevicesMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 6))
ntwsRegistrationDevicesMib.setRevisions(('2008-08-08 00:01', '2007-08-22 00:00',))
if mibBuilder.loadTexts: ntwsRegistrationDevicesMib.setLastUpdated('200808080001Z')
if mibBuilder.loadTexts: ntwsRegistrationDevicesMib.setOrganization('Nortel Networks')
ntwsWirelessSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1))
ntwsSwitch2360 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 2))
ntwsSwitch2380 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 3))
ntwsSwitch2350 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 4))
ntwsSwitch2372 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 5))
ntwsSwitch2382 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 6))
ntwsSwitch2800 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 7))
mibBuilder.exportSymbols("NTWS-REGISTRATION-DEVICES-MIB", ntwsSwitch2800=ntwsSwitch2800, ntwsSwitch2380=ntwsSwitch2380, ntwsRegistrationDevicesMib=ntwsRegistrationDevicesMib, ntwsSwitch2350=ntwsSwitch2350, PYSNMP_MODULE_ID=ntwsRegistrationDevicesMib, ntwsSwitch2372=ntwsSwitch2372, ntwsWirelessSwitch=ntwsWirelessSwitch, ntwsSwitch2360=ntwsSwitch2360, ntwsSwitch2382=ntwsSwitch2382)
