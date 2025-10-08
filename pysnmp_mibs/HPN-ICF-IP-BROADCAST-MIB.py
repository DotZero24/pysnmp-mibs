#
# PySNMP MIB module HPN-ICF-IP-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-IP-BROADCAST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:57 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfIpBroadcast = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33))
hpnicfIpBroadcast.setRevisions(('2004-12-13 19:36',))
if mibBuilder.loadTexts: hpnicfIpBroadcast.setLastUpdated('200412131936Z')
if mibBuilder.loadTexts: hpnicfIpBroadcast.setOrganization('')
hpnicfIpBdstScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1))
hpnicfIpBdstForwardBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpBdstForwardBroadcast.setStatus('current')
hpnicfIpReceiveBroadcast = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("receive", 1), ("notReceive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpReceiveBroadcast.setStatus('current')
hpnicfIpBdstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 2))
hpnicfIpBdstTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 3))
hpnicfIpBdstTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 3, 0))
mibBuilder.exportSymbols("HPN-ICF-IP-BROADCAST-MIB", hpnicfIpReceiveBroadcast=hpnicfIpReceiveBroadcast, hpnicfIpBroadcast=hpnicfIpBroadcast, hpnicfIpBdstForwardBroadcast=hpnicfIpBdstForwardBroadcast, hpnicfIpBdstTrap=hpnicfIpBdstTrap, hpnicfIpBdstTrapPrex=hpnicfIpBdstTrapPrex, hpnicfIpBdstGroup=hpnicfIpBdstGroup, PYSNMP_MODULE_ID=hpnicfIpBroadcast, hpnicfIpBdstScalarGroup=hpnicfIpBdstScalarGroup)
