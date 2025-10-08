#
# PySNMP MIB module Juniper-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/Juniper-DNS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, = mibBuilder.importSymbols("Juniper-TC", "JuniEnable")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("Juniper-DNS-MIB", juniDnsLocalDomainNameListNextIndex=juniDnsLocalDomainNameListNextIndex, juniDnsGeneral=juniDnsGeneral, juniDnsLocalDomainNameListTable=juniDnsLocalDomainNameListTable, juniDnsCompliances=juniDnsCompliances, juniDnsServerListTable=juniDnsServerListTable, LocalDomainName=LocalDomainName, juniDnsV4V6ServerListGroup=juniDnsV4V6ServerListGroup, juniDnsLocalDomainNameListRowStatus=juniDnsLocalDomainNameListRowStatus, juniDnsMIB=juniDnsMIB, juniDnsServerListRowStatus=juniDnsServerListRowStatus, juniDnsServerListEntry=juniDnsServerListEntry, juniDnsLocalDomainNameList=juniDnsLocalDomainNameList, juniDnsCompliance=juniDnsCompliance, juniDnsObjects=juniDnsObjects, juniDnsServerListIndex=juniDnsServerListIndex, LocalDomainNameListIndex=LocalDomainNameListIndex, JuniNextLocalDomainNameListIndex=JuniNextLocalDomainNameListIndex, juniDnsServerListAddress=juniDnsServerListAddress, juniDnsEnableGroup=juniDnsEnableGroup, ServerListIndex=ServerListIndex, PYSNMP_MODULE_ID=juniDnsMIB, juniDnsLocalDomainNameListName=juniDnsLocalDomainNameListName, juniDnsV4V6ServerListAddressType=juniDnsV4V6ServerListAddressType, juniDnsConformance=juniDnsConformance, juniDnsServerListGroup=juniDnsServerListGroup, juniDnsEnable=juniDnsEnable, JuniNextServerListIndex=JuniNextServerListIndex, juniDnsServerListNextIndex=juniDnsServerListNextIndex, juniDnsLocalDomainNameListEntry=juniDnsLocalDomainNameListEntry, juniDnsLocalDomainNameListIndex=juniDnsLocalDomainNameListIndex, juniDnsLocalDomainNameListGroup=juniDnsLocalDomainNameListGroup, juniDnsGroups=juniDnsGroups, juniDnsServerList=juniDnsServerList, juniDnsV4V6ServerListAddress=juniDnsV4V6ServerListAddress)
