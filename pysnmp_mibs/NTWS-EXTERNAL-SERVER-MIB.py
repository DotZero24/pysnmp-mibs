#
# PySNMP MIB module NTWS-EXTERNAL-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/NTWS-EXTERNAL-SERVER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NtwsIpPort, = mibBuilder.importSymbols("NTWS-BASIC-TC", "NtwsIpPort")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsExternalServerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7))
ntwsExternalServerMib.setRevisions(('2008-10-24 00:10', '2007-08-16 00:05', '2006-07-31 00:04',))
if mibBuilder.loadTexts: ntwsExternalServerMib.setLastUpdated('200810240010Z')
if mibBuilder.loadTexts: ntwsExternalServerMib.setOrganization('Nortel Networks')
class NtwsSyslogServerEnable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

ntwsExternalServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1))
ntwsExternalServerDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1))
ntwsExtServerSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1), )
if mibBuilder.loadTexts: ntwsExtServerSyslogTable.setStatus('current')
ntwsExtServerSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1), ).setIndexNames((0, "NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogIndex"))
if mibBuilder.loadTexts: ntwsExtServerSyslogEntry.setStatus('current')
ntwsExtServerSyslogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ntwsExtServerSyslogIndex.setStatus('current')
ntwsExtServerSyslogAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsExtServerSyslogAddress.setStatus('current')
ntwsExtServerSyslogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 3), NtwsIpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsExtServerSyslogPort.setStatus('current')
ntwsExtServerSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 4), NtwsSyslogServerEnable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsExtServerSyslogEnable.setStatus('current')
ntwsExternalServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2))
ntwsExternalServerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 1))
ntwsExternalServerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 2))
ntwsExternalServerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 1, 1)).setObjects(("NTWS-EXTERNAL-SERVER-MIB", "ntwsExternalServerConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsExternalServerCompliance = ntwsExternalServerCompliance.setStatus('current')
ntwsExternalServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 2, 1)).setObjects(("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogAddress"), ("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogPort"), ("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsExternalServerConfigGroup = ntwsExternalServerConfigGroup.setStatus('current')
mibBuilder.exportSymbols("NTWS-EXTERNAL-SERVER-MIB", NtwsSyslogServerEnable=NtwsSyslogServerEnable, ntwsExternalServerMib=ntwsExternalServerMib, ntwsExternalServerGroups=ntwsExternalServerGroups, ntwsExtServerSyslogTable=ntwsExtServerSyslogTable, ntwsExtServerSyslogIndex=ntwsExtServerSyslogIndex, ntwsExtServerSyslogAddress=ntwsExtServerSyslogAddress, ntwsExternalServerConfigGroup=ntwsExternalServerConfigGroup, ntwsExternalServerCompliances=ntwsExternalServerCompliances, ntwsExternalServerObjects=ntwsExternalServerObjects, ntwsExtServerSyslogPort=ntwsExtServerSyslogPort, ntwsExtServerSyslogEnable=ntwsExtServerSyslogEnable, ntwsExternalServerConformance=ntwsExternalServerConformance, ntwsExternalServerDataObjects=ntwsExternalServerDataObjects, ntwsExternalServerCompliance=ntwsExternalServerCompliance, PYSNMP_MODULE_ID=ntwsExternalServerMib, ntwsExtServerSyslogEntry=ntwsExtServerSyslogEntry)
