#
# PySNMP MIB module NOS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/brocade/NOS-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nos, = mibBuilder.importSymbols("Brocade-REG-MIB", "nos")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nosProducts = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 2, 1))
if mibBuilder.loadTexts: nosProducts.setLastUpdated('0110101500Z')
if mibBuilder.loadTexts: nosProducts.setOrganization('Brocade Communications Systems, Inc.,')
bcsiRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1))
bcsiChassisTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1))
bcsiCardTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 2))
vdx6720P24 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 1))
vdx6720P60 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 2))
vdx6730P32 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 3))
vdx6730P76 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 4))
vdx6710P54 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 5))
vdx6746 = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 2, 2, 1, 1, 1, 112))
mibBuilder.exportSymbols("NOS-PRODUCTS-MIB", bcsiCardTypes=bcsiCardTypes, vdx6730P32=vdx6730P32, bcsiRegistration=bcsiRegistration, nosProducts=nosProducts, vdx6720P60=vdx6720P60, vdx6730P76=vdx6730P76, PYSNMP_MODULE_ID=nosProducts, bcsiChassisTypes=bcsiChassisTypes, vdx6746=vdx6746, vdx6710P54=vdx6710P54, vdx6720P24=vdx6720P24)
