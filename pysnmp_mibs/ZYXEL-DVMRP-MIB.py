#
# PySNMP MIB module ZYXEL-DVMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/zyxel/ZYXEL-DVMRP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:03 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyRouteDomainIpAddress, zyRouteDomainIpMaskBits = mibBuilder.importSymbols("ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress", "zyRouteDomainIpMaskBits")
zyxelDvmrp = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23))
if mibBuilder.loadTexts: zyxelDvmrp.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelDvmrp.setOrganization('Enterprise Solution ZyXEL')
zyxelDvmrpSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1))
zyDvmrpState = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDvmrpState.setStatus('current')
zyDvmrpThreshold = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDvmrpThreshold.setStatus('current')
zyxelDvmrpRouteDomainTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3), )
if mibBuilder.loadTexts: zyxelDvmrpRouteDomainTable.setStatus('current')
zyxelDvmrpRouteDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3, 1), ).setIndexNames((0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress"), (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits"))
if mibBuilder.loadTexts: zyxelDvmrpRouteDomainEntry.setStatus('current')
zyDvmrpRouteDomainState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDvmrpRouteDomainState.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-DVMRP-MIB", zyDvmrpState=zyDvmrpState, zyxelDvmrpSetup=zyxelDvmrpSetup, zyxelDvmrp=zyxelDvmrp, zyxelDvmrpRouteDomainEntry=zyxelDvmrpRouteDomainEntry, zyxelDvmrpRouteDomainTable=zyxelDvmrpRouteDomainTable, PYSNMP_MODULE_ID=zyxelDvmrp, zyDvmrpThreshold=zyDvmrpThreshold, zyDvmrpRouteDomainState=zyDvmrpRouteDomainState)
