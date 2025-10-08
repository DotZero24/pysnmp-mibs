#
# PySNMP MIB module A3COM-HUAWEI-IP-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-IP-BROADCAST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:33:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cIpBroadcast = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33))
h3cIpBroadcast.setRevisions(('2004-12-13 19:36',))
if mibBuilder.loadTexts: h3cIpBroadcast.setLastUpdated('200412131936Z')
if mibBuilder.loadTexts: h3cIpBroadcast.setOrganization('Huawei 3Com Technologies Co., Ltd.')
h3cIpBdstScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 1))
h3cIpBdstForwardBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpBdstForwardBroadcast.setStatus('current')
h3cIpReceiveBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receive", 1), ("notReceive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIpReceiveBroadcast.setStatus('current')
h3cIpBdstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 2))
h3cIpBdstTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 3))
h3cIpBdstTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 33, 3, 0))
mibBuilder.exportSymbols("A3COM-HUAWEI-IP-BROADCAST-MIB", PYSNMP_MODULE_ID=h3cIpBroadcast, h3cIpReceiveBroadcast=h3cIpReceiveBroadcast, h3cIpBdstTrap=h3cIpBdstTrap, h3cIpBdstForwardBroadcast=h3cIpBdstForwardBroadcast, h3cIpBdstGroup=h3cIpBdstGroup, h3cIpBroadcast=h3cIpBroadcast, h3cIpBdstTrapPrex=h3cIpBdstTrapPrex, h3cIpBdstScalarGroup=h3cIpBdstScalarGroup)
