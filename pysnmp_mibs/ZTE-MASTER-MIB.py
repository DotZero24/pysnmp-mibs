#
# PySNMP MIB module ZTE-MASTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zte/ZTE-MASTER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zxAn, = mibBuilder.importSymbols("ZTE-AN-TC-MIB", "zxAn")
zxAnPonMib = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1010))
zxAnCesMib = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1013))
zxAnEponMib = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1))
zxAnGponMib = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 2))
zxAnPonProtection = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 3))
zxAnVlanTrans = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10))
zxAnTransceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 11))
zxPwCSC = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2))
zxPwCPSN = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3))
zxAnCesProtection = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 11))
zxPwCTDM = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1))
zxPwCETH = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1))
mibBuilder.exportSymbols("ZTE-MASTER-MIB", zxPwCTDM=zxPwCTDM, zxAnGponMib=zxAnGponMib, zxAnEponMib=zxAnEponMib, zxPwCETH=zxPwCETH, zxAnPonProtection=zxAnPonProtection, zxAnCesMib=zxAnCesMib, zxAnTransceiver=zxAnTransceiver, zxAnPonMib=zxAnPonMib, zxPwCPSN=zxPwCPSN, zxPwCSC=zxPwCSC, zxAnVlanTrans=zxAnVlanTrans, zxAnCesProtection=zxAnCesProtection)
