#
# PySNMP MIB module SWITCH-CpuLimit-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/raisecom/SWITCH-CpuLimit-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:54:39 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
EnableVar, = mibBuilder.importSymbols("SWITCH-TC", "EnableVar")
rcCpuLimit = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 6, 1, 61))
rcCpuLimit.setRevisions(('2010-04-01 00:00',))
if mibBuilder.loadTexts: rcCpuLimit.setLastUpdated('201004010000Z')
if mibBuilder.loadTexts: rcCpuLimit.setOrganization('Raisecom Technology Co., Ltd.')
rcCpuLimitGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 61, 1))
rcCpuLimitEnable = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 61, 1, 1), EnableVar()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcCpuLimitEnable.setStatus('current')
mibBuilder.exportSymbols("SWITCH-CpuLimit-MIB", rcCpuLimitGroup=rcCpuLimitGroup, rcCpuLimitEnable=rcCpuLimitEnable, PYSNMP_MODULE_ID=rcCpuLimit, rcCpuLimit=rcCpuLimit)
