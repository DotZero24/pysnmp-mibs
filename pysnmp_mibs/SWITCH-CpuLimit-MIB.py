#
# PySNMP MIB module SWITCH-CpuLimit-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/raisecom/SWITCH-CpuLimit-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
iscomSwitch, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "iscomSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
EnableVar, = mibBuilder.importSymbols("SWITCH-TC", "EnableVar")
rcCpuLimit = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 6, 1, 61))
rcCpuLimit.setRevisions(('2010-04-01 00:00',))
if mibBuilder.loadTexts: rcCpuLimit.setLastUpdated('201004010000Z')
if mibBuilder.loadTexts: rcCpuLimit.setOrganization('Raisecom Technology Co., Ltd.')
rcCpuLimitGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8886, 6, 1, 61, 1))
rcCpuLimitEnable = MibScalar((1, 3, 6, 1, 4, 1, 8886, 6, 1, 61, 1, 1), EnableVar()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcCpuLimitEnable.setStatus('current')
mibBuilder.exportSymbols("SWITCH-CpuLimit-MIB", PYSNMP_MODULE_ID=rcCpuLimit, rcCpuLimitGroup=rcCpuLimitGroup, rcCpuLimit=rcCpuLimit, rcCpuLimitEnable=rcCpuLimitEnable)
