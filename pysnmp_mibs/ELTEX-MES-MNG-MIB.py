#
# PySNMP MIB module ELTEX-MES-MNG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-MNG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesMng, = mibBuilder.importSymbols("ELTEX-MES", "eltMesMng")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltMesFtp = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 2))
eltMesAAAStatMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3))
eltMesSnmpCommExtMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 4))
eltMesMacNotificationMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7))
eltMesCountersMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8))
eltMesCpuTasksUtilMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9))
eltMesSystemExtMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 10))
eltMesIfExtensionMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276))
eltMesBridgeExtMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401))
eltMesSwitchRateLimiterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773))
mibBuilder.exportSymbols("ELTEX-MES-MNG-MIB", eltMesSnmpCommExtMIB=eltMesSnmpCommExtMIB, eltMesBridgeExtMIB=eltMesBridgeExtMIB, eltMesAAAStatMIB=eltMesAAAStatMIB, eltMesSwitchRateLimiterMIB=eltMesSwitchRateLimiterMIB, eltMesCountersMIB=eltMesCountersMIB, eltMesMacNotificationMIB=eltMesMacNotificationMIB, eltMesFtp=eltMesFtp, eltMesSystemExtMIB=eltMesSystemExtMIB, eltMesIfExtensionMIB=eltMesIfExtensionMIB, eltMesCpuTasksUtilMIB=eltMesCpuTasksUtilMIB)
