#
# PySNMP MIB module CPQRECOV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/CPQRECOV-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cpqHoTrapFlags, compaq = mibBuilder.importSymbols("CPQHOST-MIB", "cpqHoTrapFlags", "compaq")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cpqRecovery = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 13))
cpqRsPartnerFailed = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13001)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
cpqRsStandbyCableFailure = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13002)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
cpqRsStandbyFailure = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13003)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
cpqRsOnlineCableFailure = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13004)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
cpqRsFailoverFailed = NotificationType((1, 3, 6, 1, 4, 1, 232) + (0,13005)).setObjects(("SNMPv2-MIB", "sysName"), ("CPQHOST-MIB", "cpqHoTrapFlags"))
mibBuilder.exportSymbols("CPQRECOV-MIB", cpqRsStandbyFailure=cpqRsStandbyFailure, cpqRsOnlineCableFailure=cpqRsOnlineCableFailure, cpqRecovery=cpqRecovery, cpqRsPartnerFailed=cpqRsPartnerFailed, cpqRsStandbyCableFailure=cpqRsStandbyCableFailure, cpqRsFailoverFailed=cpqRsFailoverFailed)
