#
# PySNMP MIB module QTECH-NMS-L2-PROTOCOL-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-NMS-L2-PROTOCOL-TUNNEL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:09 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
nmsMgmt, = mibBuilder.importSymbols("QTECH-NMS-SMI", "nmsMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nmsL2ProtocolTunnelMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 34751, 9, 357))
if mibBuilder.loadTexts: nmsL2ProtocolTunnelMIB.setLastUpdated('201302210000Z')
if mibBuilder.loadTexts: nmsL2ProtocolTunnelMIB.setOrganization('')
l2ptMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 34751, 9, 357, 1))
l2ptGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 34751, 9, 357, 1, 1))
l2ptIntfTable = MibTable((1, 3, 6, 1, 4, 1, 34751, 9, 357, 1, 2), )
if mibBuilder.loadTexts: l2ptIntfTable.setStatus('current')
l2ptIntfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 34751, 9, 357, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: l2ptIntfEntry.setStatus('current')
l2ptIntfStpTnl = MibTableColumn((1, 3, 6, 1, 4, 1, 34751, 9, 357, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: l2ptIntfStpTnl.setStatus('current')
mibBuilder.exportSymbols("QTECH-NMS-L2-PROTOCOL-TUNNEL-MIB", l2ptIntfStpTnl=l2ptIntfStpTnl, nmsL2ProtocolTunnelMIB=nmsL2ProtocolTunnelMIB, l2ptMIBObjects=l2ptMIBObjects, l2ptIntfTable=l2ptIntfTable, l2ptGlobal=l2ptGlobal, PYSNMP_MODULE_ID=nmsL2ProtocolTunnelMIB, l2ptIntfEntry=l2ptIntfEntry)
