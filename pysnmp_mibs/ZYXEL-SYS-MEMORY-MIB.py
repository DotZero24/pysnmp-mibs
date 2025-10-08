#
# PySNMP MIB module ZYXEL-SYS-MEMORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-SYS-MEMORY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ZYXEL-SYS-MEMORY-MIB", zySysMemoryPoolTotalSize=zySysMemoryPoolTotalSize, PYSNMP_MODULE_ID=zyxelSysMemory, zyxelSysMemoryPoolEntry=zyxelSysMemoryPoolEntry, zyxelSysMemoryPoolTable=zyxelSysMemoryPoolTable, zyxelSysMemory=zyxelSysMemory, zySysMemoryPoolUsedSize=zySysMemoryPoolUsedSize, zySysMemoryPoolName=zySysMemoryPoolName, zySysMemoryPoolUtilization=zySysMemoryPoolUtilization, zyxelSysMemoryPoolStatus=zyxelSysMemoryPoolStatus, zySysMemoryPoolId=zySysMemoryPoolId)
