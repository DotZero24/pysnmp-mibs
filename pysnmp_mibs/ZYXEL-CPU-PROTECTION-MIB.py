#
# PySNMP MIB module ZYXEL-CPU-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-CPU-PROTECTION-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:08 2025
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
zyxelCpuProtection = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16))
if mibBuilder.loadTexts: zyxelCpuProtection.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelCpuProtection.setOrganization('Enterprise Solution ZyXEL')
zyxelCpuProtectionSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1))
zyxelCpuProtectionTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1), )
if mibBuilder.loadTexts: zyxelCpuProtectionTable.setStatus('current')
zyxelCpuProtectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1), ).setIndexNames((0, "ZYXEL-CPU-PROTECTION-MIB", "zyCpuProtectionPort"), (0, "ZYXEL-CPU-PROTECTION-MIB", "zyCpuProtectionReasonType"))
if mibBuilder.loadTexts: zyxelCpuProtectionEntry.setStatus('current')
zyCpuProtectionPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: zyCpuProtectionPort.setStatus('current')
zyCpuProtectionReasonType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("arp", 1), ("bpdu", 2), ("igmp", 3))))
if mibBuilder.loadTexts: zyCpuProtectionReasonType.setStatus('current')
zyCpuProtectionRateLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 16, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyCpuProtectionRateLimit.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-CPU-PROTECTION-MIB", zyxelCpuProtection=zyxelCpuProtection, zyxelCpuProtectionTable=zyxelCpuProtectionTable, zyCpuProtectionPort=zyCpuProtectionPort, zyxelCpuProtectionEntry=zyxelCpuProtectionEntry, zyxelCpuProtectionSetup=zyxelCpuProtectionSetup, zyCpuProtectionRateLimit=zyCpuProtectionRateLimit, zyCpuProtectionReasonType=zyCpuProtectionReasonType, PYSNMP_MODULE_ID=zyxelCpuProtection)
