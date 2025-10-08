#
# PySNMP MIB module JUNIPER-MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/juniper/JUNIPER-MAC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:18 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
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
mibBuilder.exportSymbols("JUNIPER-MAC-MIB", jnxMacHCInFrames=jnxMacHCInFrames, jnxMacStats=jnxMacStats, jnxVlanIndex=jnxVlanIndex, jnxMacStatsTable=jnxMacStatsTable, jnxMac=jnxMac, jnxMacHCInOctets=jnxMacHCInOctets, jnxMacStatsEntry=jnxMacStatsEntry, jnxSourceMacAddress=jnxSourceMacAddress, JnxVlanIndex=JnxVlanIndex, jnxMacHCOutOctets=jnxMacHCOutOctets, jnxMacHCOutFrames=jnxMacHCOutFrames, PYSNMP_MODULE_ID=jnxMac)
