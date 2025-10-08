#
# PySNMP MIB module NMS-L2-PROTOCOL-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/bdcom/NMS-L2-PROTOCOL-TUNNEL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nmsMgmt, = mibBuilder.importSymbols("NMS-SMI", "nmsMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nmsL2ProtocolTunnelMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3320, 9, 357))
if mibBuilder.loadTexts: nmsL2ProtocolTunnelMIB.setLastUpdated('201302210000Z')
if mibBuilder.loadTexts: nmsL2ProtocolTunnelMIB.setOrganization('')
l2ptMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 357, 1))
l2ptGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 9, 357, 1, 1))
l2ptIntfTable = MibTable((1, 3, 6, 1, 4, 1, 3320, 9, 357, 1, 2), )
if mibBuilder.loadTexts: l2ptIntfTable.setStatus('current')
l2ptIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3320, 9, 357, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: l2ptIntfEntry.setStatus('current')
l2ptIntfStpTnl = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 9, 357, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2ptIntfStpTnl.setStatus('current')
mibBuilder.exportSymbols("NMS-L2-PROTOCOL-TUNNEL-MIB", l2ptIntfTable=l2ptIntfTable, l2ptGlobal=l2ptGlobal, l2ptIntfStpTnl=l2ptIntfStpTnl, l2ptIntfEntry=l2ptIntfEntry, PYSNMP_MODULE_ID=nmsL2ProtocolTunnelMIB, l2ptMIBObjects=l2ptMIBObjects, nmsL2ProtocolTunnelMIB=nmsL2ProtocolTunnelMIB)
