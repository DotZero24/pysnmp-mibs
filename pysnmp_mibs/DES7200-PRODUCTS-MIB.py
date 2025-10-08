#
# PySNMP MIB module DES7200-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DES7200-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
myModules, mySwitchProducts = mibBuilder.importSymbols("DES7200-SMI", "myModules", "mySwitchProducts")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
myProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 4, 1))
myProductsMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: myProductsMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: myProductsMIB.setOrganization('My Networks Co.,Ltd.')
des_7206 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 1, 1)).setLabel("des-7206")
des_7210 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 1, 2)).setLabel("des-7210")
des_7206E = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 1, 3)).setLabel("des-7206E")
des_7210E = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 1, 4)).setLabel("des-7210E")
mibBuilder.exportSymbols("DES7200-PRODUCTS-MIB", des_7206E=des_7206E, des_7210=des_7210, myProductsMIB=myProductsMIB, des_7206=des_7206, PYSNMP_MODULE_ID=myProductsMIB, des_7210E=des_7210E)
