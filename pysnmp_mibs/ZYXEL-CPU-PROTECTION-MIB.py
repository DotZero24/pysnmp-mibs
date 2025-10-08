#
# PySNMP MIB module ZYXEL-CPU-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-CPU-PROTECTION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ZYXEL-CPU-PROTECTION-MIB", zyxelCpuProtectionEntry=zyxelCpuProtectionEntry, zyxelCpuProtection=zyxelCpuProtection, zyCpuProtectionReasonType=zyCpuProtectionReasonType, zyxelCpuProtectionTable=zyxelCpuProtectionTable, zyxelCpuProtectionSetup=zyxelCpuProtectionSetup, PYSNMP_MODULE_ID=zyxelCpuProtection, zyCpuProtectionPort=zyCpuProtectionPort, zyCpuProtectionRateLimit=zyCpuProtectionRateLimit)
