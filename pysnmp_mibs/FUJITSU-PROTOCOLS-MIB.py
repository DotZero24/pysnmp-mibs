#
# PySNMP MIB module FUJITSU-PROTOCOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fujitsu/FUJITSU-PROTOCOLS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fssProtocols, = mibBuilder.importSymbols("FSS-COMMON-SMI", "fssProtocols")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowStatus, DateAndTime, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "TruthValue", "DisplayString")
fUJITSU_PROTOCOLS_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000)).setLabel("fUJITSU-PROTOCOLS-MIB")
fUJITSU_PROTOCOLS_MIB.setRevisions(('2016-04-01 00:00',))
if mibBuilder.loadTexts: fUJITSU_PROTOCOLS_MIB.setLastUpdated('201604010000Z')
if mibBuilder.loadTexts: fUJITSU_PROTOCOLS_MIB.setOrganization('@ORGANIZATION')
class ConfdString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

protocols = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1))
protocolsProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1, 1), )
if mibBuilder.loadTexts: protocolsProtocolTable.setStatus('current')
protocolsProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1, 1, 1), ).setIndexNames((1, "FUJITSU-PROTOCOLS-MIB", "protocolsProtocolName"))
if mibBuilder.loadTexts: protocolsProtocolEntry.setStatus('current')
protocolsProtocolName = MibTableColumn((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1, 1, 1, 1), String())
if mibBuilder.loadTexts: protocolsProtocolName.setStatus('current')
protocolsProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1, 1, 1, 2), ConfdString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: protocolsProtocolType.setStatus('current')
protocolsProtocolRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: protocolsProtocolRowstatus.setStatus('current')
mibBuilder.exportSymbols("FUJITSU-PROTOCOLS-MIB", protocolsProtocolTable=protocolsProtocolTable, protocolsProtocolType=protocolsProtocolType, protocolsProtocolRowstatus=protocolsProtocolRowstatus, protocolsProtocolEntry=protocolsProtocolEntry, fUJITSU_PROTOCOLS_MIB=fUJITSU_PROTOCOLS_MIB, protocolsProtocolName=protocolsProtocolName, protocols=protocols, ConfdString=ConfdString, String=String, PYSNMP_MODULE_ID=fUJITSU_PROTOCOLS_MIB)
