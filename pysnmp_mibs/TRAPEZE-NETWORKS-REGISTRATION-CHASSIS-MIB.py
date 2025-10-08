#
# PySNMP MIB module TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:21 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzRegistration, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzRegistration")
trpzRegistrationChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 3, 5))
trpzRegistrationChassisMib.setRevisions(('2007-08-22 00:00',))
if mibBuilder.loadTexts: trpzRegistrationChassisMib.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: trpzRegistrationChassisMib.setOrganization('Trapeze Networks')
trpzChassisComponents = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4))
trpzChasCompPowerSupplies = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 1))
trpzChasCompFans = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2))
trpzChasCompPowerSupply1 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 1, 1))
trpzChasCompPowerSupply2 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 1, 2))
trpzChasCompFan1 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 1))
trpzChasCompFan2 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 2))
trpzChasCompFan3 = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 3))
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB", trpzChasCompFan3=trpzChasCompFan3, trpzChasCompFans=trpzChasCompFans, trpzChasCompPowerSupplies=trpzChasCompPowerSupplies, trpzChasCompPowerSupply1=trpzChasCompPowerSupply1, trpzChasCompFan1=trpzChasCompFan1, trpzChassisComponents=trpzChassisComponents, trpzRegistrationChassisMib=trpzRegistrationChassisMib, PYSNMP_MODULE_ID=trpzRegistrationChassisMib, trpzChasCompPowerSupply2=trpzChasCompPowerSupply2, trpzChasCompFan2=trpzChasCompFan2)
