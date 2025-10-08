#
# PySNMP MIB module ZYXEL-SYS-MEMORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-SYS-MEMORY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:13 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelSysMemory = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50))
if mibBuilder.loadTexts: zyxelSysMemory.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelSysMemory.setOrganization('Enterprise Solution ZyXEL')
zyxelSysMemoryPoolStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1))
zyxelSysMemoryPoolTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1), )
if mibBuilder.loadTexts: zyxelSysMemoryPoolTable.setStatus('current')
zyxelSysMemoryPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1), ).setIndexNames((0, "ZYXEL-SYS-MEMORY-MIB", "zySysMemoryPoolId"))
if mibBuilder.loadTexts: zyxelSysMemoryPoolEntry.setStatus('current')
zySysMemoryPoolId = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: zySysMemoryPoolId.setStatus('current')
zySysMemoryPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMemoryPoolName.setStatus('current')
zySysMemoryPoolTotalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMemoryPoolTotalSize.setStatus('current')
zySysMemoryPoolUsedSize = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMemoryPoolUsedSize.setStatus('current')
zySysMemoryPoolUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 50, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zySysMemoryPoolUtilization.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-SYS-MEMORY-MIB", zySysMemoryPoolUsedSize=zySysMemoryPoolUsedSize, zySysMemoryPoolId=zySysMemoryPoolId, zyxelSysMemoryPoolStatus=zyxelSysMemoryPoolStatus, zyxelSysMemory=zyxelSysMemory, zySysMemoryPoolUtilization=zySysMemoryPoolUtilization, zyxelSysMemoryPoolEntry=zyxelSysMemoryPoolEntry, zySysMemoryPoolName=zySysMemoryPoolName, zyxelSysMemoryPoolTable=zyxelSysMemoryPoolTable, zySysMemoryPoolTotalSize=zySysMemoryPoolTotalSize, PYSNMP_MODULE_ID=zyxelSysMemory)
