#
# PySNMP MIB module JUNIPER-IPv4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/juniper/JUNIPER-IPv4-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxIpv4 = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 12))
jnxIpv4.setRevisions(('2001-08-31 00:00',))
if mibBuilder.loadTexts: jnxIpv4.setLastUpdated('200307182153Z')
if mibBuilder.loadTexts: jnxIpv4.setOrganization('Juniper Networks, Inc.')
jnxIpv4Config = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 12, 1))
jnxIpv4AddrTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1), )
if mibBuilder.loadTexts: jnxIpv4AddrTable.setStatus('current')
jnxIpv4AddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1), ).setIndexNames((0, "JUNIPER-IPv4-MIB", "jnxIpv4AdEntIfIndex"), (0, "JUNIPER-IPv4-MIB", "jnxIpv4AdEntAddr"))
if mibBuilder.loadTexts: jnxIpv4AddrEntry.setStatus('current')
jnxIpv4AdEntIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: jnxIpv4AdEntIfIndex.setStatus('current')
jnxIpv4AdEntAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1, 2), IpAddress())
if mibBuilder.loadTexts: jnxIpv4AdEntAddr.setStatus('current')
jnxIpv4AdEntNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv4AdEntNetMask.setStatus('current')
jnxIpv4AdEntBcastAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv4AdEntBcastAddr.setStatus('current')
jnxIpv4AdEntReasmMaxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 12, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpv4AdEntReasmMaxSize.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-IPv4-MIB", jnxIpv4AdEntAddr=jnxIpv4AdEntAddr, jnxIpv4AdEntNetMask=jnxIpv4AdEntNetMask, PYSNMP_MODULE_ID=jnxIpv4, jnxIpv4AddrTable=jnxIpv4AddrTable, jnxIpv4AdEntIfIndex=jnxIpv4AdEntIfIndex, jnxIpv4AdEntReasmMaxSize=jnxIpv4AdEntReasmMaxSize, jnxIpv4Config=jnxIpv4Config, jnxIpv4AdEntBcastAddr=jnxIpv4AdEntBcastAddr, jnxIpv4AddrEntry=jnxIpv4AddrEntry, jnxIpv4=jnxIpv4)
