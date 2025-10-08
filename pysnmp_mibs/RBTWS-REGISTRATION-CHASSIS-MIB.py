#
# PySNMP MIB module RBTWS-REGISTRATION-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cabletron/RBTWS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:23 2025
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
rbtwsRegistrationChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 5))
rbtwsRegistrationChassisMib.setRevisions(('2007-08-22 00:00',))
if mibBuilder.loadTexts: rbtwsRegistrationChassisMib.setLastUpdated('200708231753Z')
if mibBuilder.loadTexts: rbtwsRegistrationChassisMib.setOrganization('Enterasys Networks')
rbtwsChassisComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4))
rbtwsChasCompPowerSupplies = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1))
rbtwsChasCompFans = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2))
rbtwsChasCompPowerSupply1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1, 1))
rbtwsChasCompPowerSupply2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 1, 2))
rbtwsChasCompFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 1))
rbtwsChasCompFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 2))
rbtwsChasCompFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 4, 2, 3))
mibBuilder.exportSymbols("RBTWS-REGISTRATION-CHASSIS-MIB", rbtwsRegistrationChassisMib=rbtwsRegistrationChassisMib, rbtwsChasCompFan3=rbtwsChasCompFan3, rbtwsChasCompFan1=rbtwsChasCompFan1, rbtwsChasCompFan2=rbtwsChasCompFan2, rbtwsChasCompPowerSupply2=rbtwsChasCompPowerSupply2, rbtwsChasCompPowerSupplies=rbtwsChasCompPowerSupplies, PYSNMP_MODULE_ID=rbtwsRegistrationChassisMib, rbtwsChasCompFans=rbtwsChasCompFans, rbtwsChasCompPowerSupply1=rbtwsChasCompPowerSupply1, rbtwsChassisComponents=rbtwsChassisComponents)
