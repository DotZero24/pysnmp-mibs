#
# PySNMP MIB module RBTWS-REGISTRATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/RBTWS-REGISTRATION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rbtwsRegistration, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsRegistration")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsRegistrationMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 3))
rbtwsRegistrationMib.setRevisions(('2006-05-22 00:08', '2005-01-01 00:00',))
if mibBuilder.loadTexts: rbtwsRegistrationMib.setLastUpdated('200605301630Z')
if mibBuilder.loadTexts: rbtwsRegistrationMib.setOrganization('Enterasys Networks')
rbtwsChassisComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4))
rbtwsChasCompPowerSupplies = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1))
rbtwsChasCompFans = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2))
rbtwsChasCompPowerSupply1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1, 1))
rbtwsChasCompPowerSupply2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1, 2))
rbtwsChasCompFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 1))
rbtwsChasCompFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 2))
rbtwsChasCompFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 3))
rbtwsWirelessSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1))
rbtwsSwitch8100 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 1))
rbtwsSwitch8200 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 2))
rbtwsSwitch8400 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 3))
mibBuilder.exportSymbols("RBTWS-REGISTRATION-MIB", rbtwsSwitch8100=rbtwsSwitch8100, rbtwsChasCompFans=rbtwsChasCompFans, rbtwsRegistrationMib=rbtwsRegistrationMib, rbtwsChasCompFan2=rbtwsChasCompFan2, rbtwsChassisComponents=rbtwsChassisComponents, rbtwsChasCompFan3=rbtwsChasCompFan3, rbtwsSwitch8200=rbtwsSwitch8200, rbtwsChasCompFan1=rbtwsChasCompFan1, PYSNMP_MODULE_ID=rbtwsRegistrationMib, rbtwsChasCompPowerSupply2=rbtwsChasCompPowerSupply2, rbtwsWirelessSwitch=rbtwsWirelessSwitch, rbtwsSwitch8400=rbtwsSwitch8400, rbtwsChasCompPowerSupplies=rbtwsChasCompPowerSupplies, rbtwsChasCompPowerSupply1=rbtwsChasCompPowerSupply1)
