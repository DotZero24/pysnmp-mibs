#
# PySNMP MIB module RBTWS-REGISTRATION-DEVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cabletron/RBTWS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rbtwsRegistration, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsRegistration")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbtwsRegistrationDevicesMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 6))
rbtwsRegistrationDevicesMib.setRevisions(('2007-08-22 00:00',))
if mibBuilder.loadTexts: rbtwsRegistrationDevicesMib.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: rbtwsRegistrationDevicesMib.setOrganization('Enterasys Networks')
rbtwsWirelessSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1))
rbtwsSwitch8100 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 1))
rbtwsSwitch8200 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 2))
rbtwsSwitch8400 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 3))
rbtwsSwitch8110 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 4))
rbtwsSwitch8500 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 5))
mibBuilder.exportSymbols("RBTWS-REGISTRATION-DEVICES-MIB", rbtwsRegistrationDevicesMib=rbtwsRegistrationDevicesMib, rbtwsSwitch8110=rbtwsSwitch8110, rbtwsSwitch8400=rbtwsSwitch8400, rbtwsSwitch8100=rbtwsSwitch8100, rbtwsSwitch8500=rbtwsSwitch8500, rbtwsSwitch8200=rbtwsSwitch8200, PYSNMP_MODULE_ID=rbtwsRegistrationDevicesMib, rbtwsWirelessSwitch=rbtwsWirelessSwitch)
