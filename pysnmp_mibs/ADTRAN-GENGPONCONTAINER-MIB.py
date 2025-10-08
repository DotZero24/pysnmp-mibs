#
# PySNMP MIB module ADTRAN-GENGPONCONTAINER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-GENGPONCONTAINER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:52 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adComplianceShared, adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adComplianceShared", "adShared", "adIdentityShared")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenGponModuleIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 76))
if mibBuilder.loadTexts: adGenGponModuleIdentity.setLastUpdated('200808220000Z')
if mibBuilder.loadTexts: adGenGponModuleIdentity.setOrganization('ADTRAN, Inc.')
adGenGpon = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 76))
adGenGponConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 99, 10000, 76))
adGenGponProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 76, 1))
adGenGponProductID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 76, 1))
adGenGponProductConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 99, 10000, 76, 1))
mibBuilder.exportSymbols("ADTRAN-GENGPONCONTAINER-MIB", adGenGponProductConformance=adGenGponProductConformance, adGenGponConformance=adGenGponConformance, adGenGponProduct=adGenGponProduct, adGenGpon=adGenGpon, PYSNMP_MODULE_ID=adGenGponModuleIdentity, adGenGponProductID=adGenGponProductID, adGenGponModuleIdentity=adGenGponModuleIdentity)
