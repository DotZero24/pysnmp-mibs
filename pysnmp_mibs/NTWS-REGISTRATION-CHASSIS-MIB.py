#
# PySNMP MIB module NTWS-REGISTRATION-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NTWS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:40 2025
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
mibBuilder.exportSymbols("NTWS-REGISTRATION-CHASSIS-MIB", ntwsChasCompPowerSupply2=ntwsChasCompPowerSupply2, ntwsChasCompFans=ntwsChasCompFans, ntwsChassisComponents=ntwsChassisComponents, ntwsChasCompFan3=ntwsChasCompFan3, PYSNMP_MODULE_ID=ntwsRegistrationChassisMib, ntwsChasCompPowerSupply1=ntwsChasCompPowerSupply1, ntwsChasCompFan1=ntwsChasCompFan1, ntwsChasCompFan2=ntwsChasCompFan2, ntwsChasCompPowerSupplies=ntwsChasCompPowerSupplies, ntwsRegistrationChassisMib=ntwsRegistrationChassisMib)
