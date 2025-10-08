#
# PySNMP MIB module ZTE-MASTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zte/ZTE-MASTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZTE-MASTER-MIB", zxPwCTDM=zxPwCTDM, zxPwCETH=zxPwCETH, zxAnEponMib=zxAnEponMib, zxPwCSC=zxPwCSC, zxPwCPSN=zxPwCPSN, zxAnCesProtection=zxAnCesProtection, zxAnGponMib=zxAnGponMib, zxAnCesMib=zxAnCesMib, zxAnPonMib=zxAnPonMib, zxAnTransceiver=zxAnTransceiver, zxAnVlanTrans=zxAnVlanTrans, zxAnPonProtection=zxAnPonProtection)
