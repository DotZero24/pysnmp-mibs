#
# PySNMP MIB module JUNIPER-IPv4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/juniper/JUNIPER-IPv4-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("JUNIPER-IPv4-MIB", jnxIpv4AdEntReasmMaxSize=jnxIpv4AdEntReasmMaxSize, jnxIpv4=jnxIpv4, jnxIpv4Config=jnxIpv4Config, jnxIpv4AddrEntry=jnxIpv4AddrEntry, jnxIpv4AddrTable=jnxIpv4AddrTable, jnxIpv4AdEntNetMask=jnxIpv4AdEntNetMask, jnxIpv4AdEntIfIndex=jnxIpv4AdEntIfIndex, PYSNMP_MODULE_ID=jnxIpv4, jnxIpv4AdEntBcastAddr=jnxIpv4AdEntBcastAddr, jnxIpv4AdEntAddr=jnxIpv4AdEntAddr)
