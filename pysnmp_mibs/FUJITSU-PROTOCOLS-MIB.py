#
# PySNMP MIB module FUJITSU-PROTOCOLS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fujitsu/FUJITSU-PROTOCOLS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fssProtocols, = mibBuilder.importSymbols("FSS-COMMON-SMI", "fssProtocols")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, DateAndTime, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "DateAndTime", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("FUJITSU-PROTOCOLS-MIB", fUJITSU_PROTOCOLS_MIB=fUJITSU_PROTOCOLS_MIB, protocolsProtocolTable=protocolsProtocolTable, protocolsProtocolType=protocolsProtocolType, protocolsProtocolRowstatus=protocolsProtocolRowstatus, protocols=protocols, protocolsProtocolEntry=protocolsProtocolEntry, PYSNMP_MODULE_ID=fUJITSU_PROTOCOLS_MIB, String=String, protocolsProtocolName=protocolsProtocolName, ConfdString=ConfdString)
