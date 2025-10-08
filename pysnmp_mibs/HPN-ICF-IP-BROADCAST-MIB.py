#
# PySNMP MIB module HPN-ICF-IP-BROADCAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-IP-BROADCAST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("HPN-ICF-IP-BROADCAST-MIB", hpnicfIpBdstForwardBroadcast=hpnicfIpBdstForwardBroadcast, hpnicfIpBdstTrap=hpnicfIpBdstTrap, PYSNMP_MODULE_ID=hpnicfIpBroadcast, hpnicfIpReceiveBroadcast=hpnicfIpReceiveBroadcast, hpnicfIpBdstScalarGroup=hpnicfIpBdstScalarGroup, hpnicfIpBdstTrapPrex=hpnicfIpBdstTrapPrex, hpnicfIpBroadcast=hpnicfIpBroadcast, hpnicfIpBdstGroup=hpnicfIpBdstGroup)
