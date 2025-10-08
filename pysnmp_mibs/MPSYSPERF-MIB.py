#
# PySNMP MIB module MPSYSPERF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/maipu/MPSYSPERF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:58 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mpMgmt, = mibBuilder.importSymbols("MAIPU-SMI", "mpMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ObjectSyntax, iso, MibIdentifier, ObjectName, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ObjectSyntax", "iso", "MibIdentifier", "ObjectName", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
mpSysPerfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5651, 3, 901))
if mibBuilder.loadTexts: mpSysPerfMib.setLastUpdated('0707311414Z')
if mibBuilder.loadTexts: mpSysPerfMib.setOrganization('Maipu (Sichuan) Communication Technology Co. LTD.')
mpSysRamUsage = MibScalar((1, 3, 6, 1, 4, 1, 5651, 3, 901, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpSysRamUsage.setStatus('current')
mpSysCpuUsage = MibScalar((1, 3, 6, 1, 4, 1, 5651, 3, 901, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpSysCpuUsage.setStatus('current')
mpSysCpuPeakLoad = MibScalar((1, 3, 6, 1, 4, 1, 5651, 3, 901, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpSysCpuPeakLoad.setStatus('current')
mibBuilder.exportSymbols("MPSYSPERF-MIB", PYSNMP_MODULE_ID=mpSysPerfMib, mpSysCpuPeakLoad=mpSysCpuPeakLoad, mpSysCpuUsage=mpSysCpuUsage, mpSysRamUsage=mpSysRamUsage, mpSysPerfMib=mpSysPerfMib)
