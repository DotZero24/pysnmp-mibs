#
# PySNMP MIB module Juniper-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/junose/Juniper-DNS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, = mibBuilder.importSymbols("Juniper-TC", "JuniEnable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
juniDnsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47))
juniDnsMIB.setRevisions(('2006-09-15 08:32', '2003-09-11 15:50', '2002-09-16 21:44', '2001-03-22 19:29',))
if mibBuilder.loadTexts: juniDnsMIB.setLastUpdated('200609150832Z')
if mibBuilder.loadTexts: juniDnsMIB.setOrganization('Juniper Networks, Inc.')
class JuniNextServerListIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ServerListIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class JuniNextLocalDomainNameListIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class LocalDomainNameListIndex(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class LocalDomainName(TextualConvention, OctetString):
    reference = 'RFC 854: NVT ASCII character set. See SNMPv2-TC.DisplayString DESCRIPTION for a summary.'
    status = 'current'
    displayHint = '1025a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1025)

juniDnsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1))
juniDnsGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1))
juniDnsServerList = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2))
juniDnsLocalDomainNameList = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3))
juniDnsEnable = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1, 1), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDnsEnable.setStatus('current')
juniDnsServerListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 1), JuniNextServerListIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDnsServerListNextIndex.setStatus('current')
juniDnsServerListTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2), )
if mibBuilder.loadTexts: juniDnsServerListTable.setStatus('current')
juniDnsServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1), ).setIndexNames((0, "Juniper-DNS-MIB", "juniDnsServerListIndex"))
if mibBuilder.loadTexts: juniDnsServerListEntry.setStatus('current')
juniDnsServerListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 1), ServerListIndex())
if mibBuilder.loadTexts: juniDnsServerListIndex.setStatus('current')
juniDnsServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsServerListAddress.setStatus('obsolete')
juniDnsServerListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsServerListRowStatus.setStatus('current')
juniDnsV4V6ServerListAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 4), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsV4V6ServerListAddressType.setStatus('current')
juniDnsV4V6ServerListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsV4V6ServerListAddress.setStatus('current')
juniDnsLocalDomainNameListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 1), JuniNextLocalDomainNameListIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDnsLocalDomainNameListNextIndex.setStatus('current')
juniDnsLocalDomainNameListTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2), )
if mibBuilder.loadTexts: juniDnsLocalDomainNameListTable.setStatus('current')
juniDnsLocalDomainNameListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1), ).setIndexNames((0, "Juniper-DNS-MIB", "juniDnsLocalDomainNameListIndex"))
if mibBuilder.loadTexts: juniDnsLocalDomainNameListEntry.setStatus('current')
juniDnsLocalDomainNameListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 1), LocalDomainNameListIndex())
if mibBuilder.loadTexts: juniDnsLocalDomainNameListIndex.setStatus('current')
juniDnsLocalDomainNameListName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 2), LocalDomainName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsLocalDomainNameListName.setStatus('current')
juniDnsLocalDomainNameListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDnsLocalDomainNameListRowStatus.setStatus('current')
juniDnsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2))
juniDnsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1))
juniDnsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2))
juniDnsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1, 1)).setObjects(("Juniper-DNS-MIB", "juniDnsEnableGroup"), ("Juniper-DNS-MIB", "juniDnsServerListGroup"), ("Juniper-DNS-MIB", "juniDnsV4V6ServerListGroup"), ("Juniper-DNS-MIB", "juniDnsLocalDomainNameListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsCompliance = juniDnsCompliance.setStatus('current')
juniDnsEnableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 1)).setObjects(("Juniper-DNS-MIB", "juniDnsEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsEnableGroup = juniDnsEnableGroup.setStatus('current')
juniDnsServerListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 2)).setObjects(("Juniper-DNS-MIB", "juniDnsServerListNextIndex"), ("Juniper-DNS-MIB", "juniDnsServerListAddress"), ("Juniper-DNS-MIB", "juniDnsServerListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsServerListGroup = juniDnsServerListGroup.setStatus('obsolete')
juniDnsLocalDomainNameListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 3)).setObjects(("Juniper-DNS-MIB", "juniDnsLocalDomainNameListNextIndex"), ("Juniper-DNS-MIB", "juniDnsLocalDomainNameListName"), ("Juniper-DNS-MIB", "juniDnsLocalDomainNameListRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsLocalDomainNameListGroup = juniDnsLocalDomainNameListGroup.setStatus('current')
juniDnsV4V6ServerListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 4)).setObjects(("Juniper-DNS-MIB", "juniDnsServerListNextIndex"), ("Juniper-DNS-MIB", "juniDnsServerListRowStatus"), ("Juniper-DNS-MIB", "juniDnsV4V6ServerListAddress"), ("Juniper-DNS-MIB", "juniDnsV4V6ServerListAddressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDnsV4V6ServerListGroup = juniDnsV4V6ServerListGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-DNS-MIB", JuniNextServerListIndex=JuniNextServerListIndex, juniDnsV4V6ServerListAddress=juniDnsV4V6ServerListAddress, juniDnsLocalDomainNameListIndex=juniDnsLocalDomainNameListIndex, juniDnsLocalDomainNameList=juniDnsLocalDomainNameList, juniDnsLocalDomainNameListRowStatus=juniDnsLocalDomainNameListRowStatus, juniDnsV4V6ServerListAddressType=juniDnsV4V6ServerListAddressType, juniDnsGroups=juniDnsGroups, juniDnsCompliance=juniDnsCompliance, LocalDomainNameListIndex=LocalDomainNameListIndex, juniDnsServerListGroup=juniDnsServerListGroup, juniDnsLocalDomainNameListGroup=juniDnsLocalDomainNameListGroup, juniDnsServerListNextIndex=juniDnsServerListNextIndex, juniDnsMIB=juniDnsMIB, juniDnsServerListAddress=juniDnsServerListAddress, juniDnsServerListIndex=juniDnsServerListIndex, juniDnsLocalDomainNameListTable=juniDnsLocalDomainNameListTable, juniDnsServerListRowStatus=juniDnsServerListRowStatus, JuniNextLocalDomainNameListIndex=JuniNextLocalDomainNameListIndex, juniDnsCompliances=juniDnsCompliances, juniDnsEnableGroup=juniDnsEnableGroup, LocalDomainName=LocalDomainName, juniDnsObjects=juniDnsObjects, ServerListIndex=ServerListIndex, juniDnsV4V6ServerListGroup=juniDnsV4V6ServerListGroup, juniDnsServerListEntry=juniDnsServerListEntry, juniDnsLocalDomainNameListNextIndex=juniDnsLocalDomainNameListNextIndex, juniDnsServerList=juniDnsServerList, juniDnsEnable=juniDnsEnable, PYSNMP_MODULE_ID=juniDnsMIB, juniDnsConformance=juniDnsConformance, juniDnsLocalDomainNameListEntry=juniDnsLocalDomainNameListEntry, juniDnsServerListTable=juniDnsServerListTable, juniDnsLocalDomainNameListName=juniDnsLocalDomainNameListName, juniDnsGeneral=juniDnsGeneral)
