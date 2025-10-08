#
# PySNMP MIB module NTWS-REGISTRATION-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NTWS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:13 2025
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
ntwsRegistrationChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 5))
ntwsRegistrationChassisMib.setRevisions(('2007-08-22 00:00',))
if mibBuilder.loadTexts: ntwsRegistrationChassisMib.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: ntwsRegistrationChassisMib.setOrganization('Nortel Networks')
ntwsChassisComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4))
ntwsChasCompPowerSupplies = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1))
ntwsChasCompFans = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2))
ntwsChasCompPowerSupply1 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1, 1))
ntwsChasCompPowerSupply2 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1, 2))
ntwsChasCompFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 1))
ntwsChasCompFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 2))
ntwsChasCompFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 3))
mibBuilder.exportSymbols("NTWS-REGISTRATION-CHASSIS-MIB", ntwsRegistrationChassisMib=ntwsRegistrationChassisMib, ntwsChasCompPowerSupply1=ntwsChasCompPowerSupply1, PYSNMP_MODULE_ID=ntwsRegistrationChassisMib, ntwsChasCompFan2=ntwsChasCompFan2, ntwsChasCompPowerSupplies=ntwsChasCompPowerSupplies, ntwsChasCompFan1=ntwsChasCompFan1, ntwsChasCompFans=ntwsChasCompFans, ntwsChassisComponents=ntwsChassisComponents, ntwsChasCompPowerSupply2=ntwsChasCompPowerSupply2, ntwsChasCompFan3=ntwsChasCompFan3)
