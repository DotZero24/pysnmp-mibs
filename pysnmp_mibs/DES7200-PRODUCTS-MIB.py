#
# PySNMP MIB module DES7200-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DES7200-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mySwitchProducts, myModules = mibBuilder.importSymbols("DES7200-SMI", "mySwitchProducts", "myModules")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
myProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 4, 1))
myProductsMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: myProductsMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: myProductsMIB.setOrganization('My Networks Co.,Ltd.')
des_7206 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 1, 1)).setLabel("des-7206")
des_7210 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 1, 2)).setLabel("des-7210")
des_7206E = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 1, 3)).setLabel("des-7206E")
des_7210E = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 1, 4)).setLabel("des-7210E")
mibBuilder.exportSymbols("DES7200-PRODUCTS-MIB", myProductsMIB=myProductsMIB, PYSNMP_MODULE_ID=myProductsMIB, des_7210=des_7210, des_7210E=des_7210E, des_7206=des_7206, des_7206E=des_7206E)
