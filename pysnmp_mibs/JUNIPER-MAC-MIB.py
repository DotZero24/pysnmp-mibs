#
# PySNMP MIB module JUNIPER-MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/juniper/JUNIPER-MAC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
jnxMac = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 23))
jnxMac.setRevisions(('2002-10-10 00:00',))
if mibBuilder.loadTexts: jnxMac.setLastUpdated('200307182153Z')
if mibBuilder.loadTexts: jnxMac.setOrganization('Juniper Networks, Inc.')
class JnxVlanIndex(TextualConvention, Unsigned32):
    status = 'current'

jnxMacStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1))
jnxMacStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1), )
if mibBuilder.loadTexts: jnxMacStatsTable.setStatus('current')
jnxMacStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-MAC-MIB", "jnxVlanIndex"), (0, "JUNIPER-MAC-MIB", "jnxSourceMacAddress"))
if mibBuilder.loadTexts: jnxMacStatsEntry.setStatus('current')
jnxVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 1), JnxVlanIndex())
if mibBuilder.loadTexts: jnxVlanIndex.setStatus('current')
jnxSourceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: jnxSourceMacAddress.setStatus('current')
jnxMacHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCInOctets.setStatus('current')
jnxMacHCInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCInFrames.setStatus('current')
jnxMacHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCOutOctets.setStatus('current')
jnxMacHCOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCOutFrames.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-MAC-MIB", jnxMac=jnxMac, jnxSourceMacAddress=jnxSourceMacAddress, jnxMacHCOutOctets=jnxMacHCOutOctets, jnxMacHCOutFrames=jnxMacHCOutFrames, JnxVlanIndex=JnxVlanIndex, jnxMacHCInFrames=jnxMacHCInFrames, PYSNMP_MODULE_ID=jnxMac, jnxMacHCInOctets=jnxMacHCInOctets, jnxMacStats=jnxMacStats, jnxVlanIndex=jnxVlanIndex, jnxMacStatsEntry=jnxMacStatsEntry, jnxMacStatsTable=jnxMacStatsTable)
