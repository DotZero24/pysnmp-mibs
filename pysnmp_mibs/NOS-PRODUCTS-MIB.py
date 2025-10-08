#
# PySNMP MIB module NOS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/NOS-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
nos, = mibBuilder.importSymbols("Brocade-REG-MIB", "nos")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("NOS-PRODUCTS-MIB", vdx6720P24=vdx6720P24, bcsiRegistration=bcsiRegistration, bcsiCardTypes=bcsiCardTypes, vdx6746=vdx6746, PYSNMP_MODULE_ID=nosProducts, vdx6730P76=vdx6730P76, bcsiChassisTypes=bcsiChassisTypes, vdx6720P60=vdx6720P60, vdx6730P32=vdx6730P32, nosProducts=nosProducts, vdx6710P54=vdx6710P54)
