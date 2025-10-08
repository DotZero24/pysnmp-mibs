#
# PySNMP MIB module JUNIPER-RPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/juniper/JUNIPER-RPF-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("JUNIPER-RPF-MIB", jnxRpfStats=jnxRpfStats, PYSNMP_MODULE_ID=jnxRpf, jnxRpf=jnxRpf, jnxRpfStatsPackets=jnxRpfStatsPackets, jnxRpfStatsBytes=jnxRpfStatsBytes, jnxRpfStatsTable=jnxRpfStatsTable, jnxRpfStatsEntry=jnxRpfStatsEntry, jnxRpfStatsAddrFamily=jnxRpfStatsAddrFamily, jnxRpfStatsIfIndex=jnxRpfStatsIfIndex)
