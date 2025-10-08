#
# PySNMP MIB module TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:56 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB", trpzChasCompFan3=trpzChasCompFan3, trpzChasCompPowerSupply1=trpzChasCompPowerSupply1, trpzRegistrationChassisMib=trpzRegistrationChassisMib, trpzChasCompPowerSupply2=trpzChasCompPowerSupply2, trpzChassisComponents=trpzChassisComponents, trpzChasCompFan1=trpzChasCompFan1, trpzChasCompFans=trpzChasCompFans, trpzChasCompPowerSupplies=trpzChasCompPowerSupplies, trpzChasCompFan2=trpzChasCompFan2, PYSNMP_MODULE_ID=trpzRegistrationChassisMib)
