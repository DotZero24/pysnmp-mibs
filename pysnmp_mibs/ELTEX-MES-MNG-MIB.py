#
# PySNMP MIB module ELTEX-MES-MNG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-MNG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:51 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesMng, = mibBuilder.importSymbols("ELTEX-MES", "eltMesMng")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ELTEX-MES-MNG-MIB", eltMesSnmpCommExtMIB=eltMesSnmpCommExtMIB, eltMesAAAStatMIB=eltMesAAAStatMIB, eltMesBridgeExtMIB=eltMesBridgeExtMIB, eltMesCpuTasksUtilMIB=eltMesCpuTasksUtilMIB, eltMesFtp=eltMesFtp, eltMesSystemExtMIB=eltMesSystemExtMIB, eltMesSwitchRateLimiterMIB=eltMesSwitchRateLimiterMIB, eltMesMacNotificationMIB=eltMesMacNotificationMIB, eltMesCountersMIB=eltMesCountersMIB, eltMesIfExtensionMIB=eltMesIfExtensionMIB)
