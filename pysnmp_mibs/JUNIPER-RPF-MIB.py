#
# PySNMP MIB module JUNIPER-RPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/juniper/JUNIPER-RPF-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxRpf = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 17))
jnxRpf.setRevisions(('2002-02-25 00:00',))
if mibBuilder.loadTexts: jnxRpf.setLastUpdated('200307182153Z')
if mibBuilder.loadTexts: jnxRpf.setOrganization('Juniper Networks, Inc.')
jnxRpfStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1))
jnxRpfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1), )
if mibBuilder.loadTexts: jnxRpfStatsTable.setStatus('current')
jnxRpfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1), ).setIndexNames((0, "JUNIPER-RPF-MIB", "jnxRpfStatsIfIndex"), (0, "JUNIPER-RPF-MIB", "jnxRpfStatsAddrFamily"))
if mibBuilder.loadTexts: jnxRpfStatsEntry.setStatus('current')
jnxRpfStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: jnxRpfStatsIfIndex.setStatus('current')
jnxRpfStatsAddrFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: jnxRpfStatsAddrFamily.setStatus('current')
jnxRpfStatsPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRpfStatsPackets.setStatus('current')
jnxRpfStatsBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 17, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRpfStatsBytes.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-RPF-MIB", jnxRpfStatsBytes=jnxRpfStatsBytes, jnxRpfStatsAddrFamily=jnxRpfStatsAddrFamily, jnxRpfStatsIfIndex=jnxRpfStatsIfIndex, jnxRpf=jnxRpf, jnxRpfStatsPackets=jnxRpfStatsPackets, jnxRpfStatsEntry=jnxRpfStatsEntry, PYSNMP_MODULE_ID=jnxRpf, jnxRpfStats=jnxRpfStats, jnxRpfStatsTable=jnxRpfStatsTable)
