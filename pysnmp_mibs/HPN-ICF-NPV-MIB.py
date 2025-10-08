#
# PySNMP MIB module HPN-ICF-NPV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPN-ICF-NPV-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
HpnicfFcVsanIndex, = mibBuilder.importSymbols("HPN-ICF-FC-TC-MIB", "HpnicfFcVsanIndex")
hpnicfSan, hpnicfVsanIndex = mibBuilder.importSymbols("HPN-ICF-VSAN-MIB", "hpnicfSan", "hpnicfVsanIndex")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
TimeStamp, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("HPN-ICF-NPV-MIB", hpnicfNpvTrafficMapConfigTable=hpnicfNpvTrafficMapConfigTable, hpnicfNpvMibObjects=hpnicfNpvMibObjects, HpnicfNpvIfIndexList=HpnicfNpvIfIndexList, hpnicfNpvServerIfEntry=hpnicfNpvServerIfEntry, PYSNMP_MODULE_ID=hpnicfNpv, hpnicfNpvTrafficMapRowStatus=hpnicfNpvTrafficMapRowStatus, hpnicfNpvTrafficMapConfigEntry=hpnicfNpvTrafficMapConfigEntry, hpnicfNpvConfiguration=hpnicfNpvConfiguration, hpnicfNpvServerIfTable=hpnicfNpvServerIfTable, hpnicfNpv=hpnicfNpv, hpnicfNpvTrafficMapLastChange=hpnicfNpvTrafficMapLastChange, hpnicfNpvTrafficMapExternalIfIndexList=hpnicfNpvTrafficMapExternalIfIndexList, hpnicfNpvExternalIfIndex=hpnicfNpvExternalIfIndex, hpnicfNpvLoadbalanceVsan=hpnicfNpvLoadbalanceVsan, hpnicfNpvGlobalObjects=hpnicfNpvGlobalObjects)
