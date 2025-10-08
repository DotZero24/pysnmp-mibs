#
# PySNMP MIB module MPSYSPERF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/maipu/MPSYSPERF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:19:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mpMgmt, = mibBuilder.importSymbols("MAIPU-SMI", "mpMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectSyntax, Counter32, ModuleIdentity, TimeTicks, Counter64, ObjectIdentity, Gauge32, ObjectName = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectSyntax", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "ObjectIdentity", "Gauge32", "ObjectName")
RowStatus, DateAndTime, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
mpSysPerfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5651, 3, 901))
if mibBuilder.loadTexts: mpSysPerfMib.setLastUpdated('0707311414Z')
if mibBuilder.loadTexts: mpSysPerfMib.setOrganization('Maipu (Sichuan) Communication Technology Co. LTD.')
mpSysRamUsage = MibScalar((1, 3, 6, 1, 4, 1, 5651, 3, 901, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpSysRamUsage.setStatus('current')
mpSysCpuUsage = MibScalar((1, 3, 6, 1, 4, 1, 5651, 3, 901, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpSysCpuUsage.setStatus('current')
mpSysCpuPeakLoad = MibScalar((1, 3, 6, 1, 4, 1, 5651, 3, 901, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mpSysCpuPeakLoad.setStatus('current')
mibBuilder.exportSymbols("MPSYSPERF-MIB", mpSysRamUsage=mpSysRamUsage, PYSNMP_MODULE_ID=mpSysPerfMib, mpSysCpuUsage=mpSysCpuUsage, mpSysPerfMib=mpSysPerfMib, mpSysCpuPeakLoad=mpSysCpuPeakLoad)
