#
# PySNMP MIB module NTWS-REGISTRATION-DEVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NTWS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ntwsRegistration, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsRegistration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NTWS-REGISTRATION-DEVICES-MIB", ntwsWirelessSwitch=ntwsWirelessSwitch, PYSNMP_MODULE_ID=ntwsRegistrationDevicesMib, ntwsSwitch2360=ntwsSwitch2360, ntwsSwitch2800=ntwsSwitch2800, ntwsSwitch2382=ntwsSwitch2382, ntwsSwitch2350=ntwsSwitch2350, ntwsSwitch2372=ntwsSwitch2372, ntwsRegistrationDevicesMib=ntwsRegistrationDevicesMib, ntwsSwitch2380=ntwsSwitch2380)
