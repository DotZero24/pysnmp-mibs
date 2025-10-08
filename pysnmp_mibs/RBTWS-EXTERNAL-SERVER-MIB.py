#
# PySNMP MIB module RBTWS-EXTERNAL-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/RBTWS-EXTERNAL-SERVER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsExternalServerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7))
rbtwsExternalServerMib.setRevisions(('2006-07-31 00:04',))
if mibBuilder.loadTexts: rbtwsExternalServerMib.setLastUpdated('200609271237Z')
if mibBuilder.loadTexts: rbtwsExternalServerMib.setOrganization('Enterasys Networks')
class RbtwsIpPort(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class RbtwsSyslogServerEnable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

rbtwsExternalServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1))
rbtwsExternalServerDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1))
rbtwsExtServerSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1), )
if mibBuilder.loadTexts: rbtwsExtServerSyslogTable.setStatus('current')
rbtwsExtServerSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1), ).setIndexNames((0, "RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogIndex"))
if mibBuilder.loadTexts: rbtwsExtServerSyslogEntry.setStatus('current')
rbtwsExtServerSyslogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: rbtwsExtServerSyslogIndex.setStatus('current')
rbtwsExtServerSyslogAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsExtServerSyslogAddress.setStatus('current')
rbtwsExtServerSyslogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 3), RbtwsIpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsExtServerSyslogPort.setStatus('current')
rbtwsExtServerSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 4), RbtwsSyslogServerEnable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsExtServerSyslogEnable.setStatus('current')
rbtwsExternalServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2))
rbtwsExternalServerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 1))
rbtwsExternalServerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 2))
rbtwsExternalServerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 1, 1)).setObjects(("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExternalServerConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsExternalServerCompliance = rbtwsExternalServerCompliance.setStatus('current')
rbtwsExternalServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 2, 1)).setObjects(("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogAddress"), ("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogPort"), ("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsExternalServerConfigGroup = rbtwsExternalServerConfigGroup.setStatus('current')
mibBuilder.exportSymbols("RBTWS-EXTERNAL-SERVER-MIB", PYSNMP_MODULE_ID=rbtwsExternalServerMib, rbtwsExtServerSyslogTable=rbtwsExtServerSyslogTable, RbtwsIpPort=RbtwsIpPort, rbtwsExtServerSyslogPort=rbtwsExtServerSyslogPort, rbtwsExternalServerConfigGroup=rbtwsExternalServerConfigGroup, rbtwsExtServerSyslogAddress=rbtwsExtServerSyslogAddress, rbtwsExtServerSyslogEnable=rbtwsExtServerSyslogEnable, RbtwsSyslogServerEnable=RbtwsSyslogServerEnable, rbtwsExternalServerCompliances=rbtwsExternalServerCompliances, rbtwsExternalServerMib=rbtwsExternalServerMib, rbtwsExtServerSyslogEntry=rbtwsExtServerSyslogEntry, rbtwsExternalServerGroups=rbtwsExternalServerGroups, rbtwsExternalServerCompliance=rbtwsExternalServerCompliance, rbtwsExtServerSyslogIndex=rbtwsExtServerSyslogIndex, rbtwsExternalServerConformance=rbtwsExternalServerConformance, rbtwsExternalServerObjects=rbtwsExternalServerObjects, rbtwsExternalServerDataObjects=rbtwsExternalServerDataObjects)
