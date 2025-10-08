#
# PySNMP MIB module HPN-ICF-NPV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPN-ICF-NPV-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
HpnicfFcVsanIndex, = mibBuilder.importSymbols("HPN-ICF-FC-TC-MIB", "HpnicfFcVsanIndex")
hpnicfVsanIndex, hpnicfSan = mibBuilder.importSymbols("HPN-ICF-VSAN-MIB", "hpnicfVsanIndex", "hpnicfSan")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TimeStamp", "TextualConvention")
hpnicfNpv = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6))
hpnicfNpv.setRevisions(('2013-04-02 00:00',))
if mibBuilder.loadTexts: hpnicfNpv.setLastUpdated('201304020000Z')
if mibBuilder.loadTexts: hpnicfNpv.setOrganization('')
class HpnicfNpvIfIndexList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 65535)

hpnicfNpvMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1))
hpnicfNpvConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1))
hpnicfNpvGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 1))
hpnicfNpvLoadbalanceVsan = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 1, 1), HpnicfFcVsanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfNpvLoadbalanceVsan.setStatus('current')
hpnicfNpvTrafficMapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2), )
if mibBuilder.loadTexts: hpnicfNpvTrafficMapConfigTable.setStatus('current')
hpnicfNpvTrafficMapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"))
if mibBuilder.loadTexts: hpnicfNpvTrafficMapConfigEntry.setStatus('current')
hpnicfNpvTrafficMapExternalIfIndexList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1, 1), HpnicfNpvIfIndexList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNpvTrafficMapExternalIfIndexList.setStatus('current')
hpnicfNpvTrafficMapLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNpvTrafficMapLastChange.setStatus('current')
hpnicfNpvTrafficMapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfNpvTrafficMapRowStatus.setStatus('current')
hpnicfNpvServerIfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 3), )
if mibBuilder.loadTexts: hpnicfNpvServerIfTable.setStatus('current')
hpnicfNpvServerIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-VSAN-MIB", "hpnicfVsanIndex"))
if mibBuilder.loadTexts: hpnicfNpvServerIfEntry.setStatus('current')
hpnicfNpvExternalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 6, 1, 1, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfNpvExternalIfIndex.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-NPV-MIB", hpnicfNpvMibObjects=hpnicfNpvMibObjects, hpnicfNpvTrafficMapConfigEntry=hpnicfNpvTrafficMapConfigEntry, PYSNMP_MODULE_ID=hpnicfNpv, hpnicfNpvServerIfEntry=hpnicfNpvServerIfEntry, hpnicfNpvExternalIfIndex=hpnicfNpvExternalIfIndex, hpnicfNpvGlobalObjects=hpnicfNpvGlobalObjects, hpnicfNpvTrafficMapLastChange=hpnicfNpvTrafficMapLastChange, hpnicfNpvTrafficMapConfigTable=hpnicfNpvTrafficMapConfigTable, hpnicfNpvLoadbalanceVsan=hpnicfNpvLoadbalanceVsan, HpnicfNpvIfIndexList=HpnicfNpvIfIndexList, hpnicfNpvTrafficMapRowStatus=hpnicfNpvTrafficMapRowStatus, hpnicfNpvConfiguration=hpnicfNpvConfiguration, hpnicfNpvServerIfTable=hpnicfNpvServerIfTable, hpnicfNpvTrafficMapExternalIfIndexList=hpnicfNpvTrafficMapExternalIfIndexList, hpnicfNpv=hpnicfNpv)
