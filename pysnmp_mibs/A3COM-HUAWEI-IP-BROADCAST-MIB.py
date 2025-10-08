#
# PySNMP MIB module A3COM-HUAWEI-IP-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/a3com/A3COM-HUAWEI-IP-BROADCAST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("A3COM-HUAWEI-IP-BROADCAST-MIB", h3cIpBdstGroup=h3cIpBdstGroup, PYSNMP_MODULE_ID=h3cIpBroadcast, h3cIpReceiveBroadcast=h3cIpReceiveBroadcast, h3cIpBroadcast=h3cIpBroadcast, h3cIpBdstScalarGroup=h3cIpBdstScalarGroup, h3cIpBdstTrapPrex=h3cIpBdstTrapPrex, h3cIpBdstTrap=h3cIpBdstTrap, h3cIpBdstForwardBroadcast=h3cIpBdstForwardBroadcast)
