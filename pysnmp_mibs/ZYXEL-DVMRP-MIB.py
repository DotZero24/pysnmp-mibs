#
# PySNMP MIB module ZYXEL-DVMRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zyxel/ZYXEL-DVMRP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyRouteDomainIpMaskBits, zyRouteDomainIpAddress = mibBuilder.importSymbols("ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits", "zyRouteDomainIpAddress")
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
mibBuilder.exportSymbols("ZYXEL-DVMRP-MIB", zyDvmrpState=zyDvmrpState, zyxelDvmrp=zyxelDvmrp, zyxelDvmrpRouteDomainEntry=zyxelDvmrpRouteDomainEntry, zyDvmrpRouteDomainState=zyDvmrpRouteDomainState, zyxelDvmrpSetup=zyxelDvmrpSetup, PYSNMP_MODULE_ID=zyxelDvmrp, zyxelDvmrpRouteDomainTable=zyxelDvmrpRouteDomainTable, zyDvmrpThreshold=zyDvmrpThreshold)
