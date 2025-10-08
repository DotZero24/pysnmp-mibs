#
# PySNMP MIB module FASTPATH-QOS-AUTOVOIP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/FASTPATH-QOS-AUTOVOIP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fastPathQOS, = mibBuilder.importSymbols("FASTPATH-QOS-MIB", "fastPathQOS")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
fastPathQOSAUTOVOIP = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4))
fastPathQOSAUTOVOIP.setRevisions(('2007-11-23 00:00', '2007-11-23 00:00',))
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setLastUpdated('200711230000Z')
if mibBuilder.loadTexts: fastPathQOSAUTOVOIP.setOrganization('Broadcom Corporation')
class PercentByFives(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 5), ValueRangeConstraint(10, 10), ValueRangeConstraint(15, 15), ValueRangeConstraint(20, 20), ValueRangeConstraint(25, 25), ValueRangeConstraint(30, 30), ValueRangeConstraint(35, 35), ValueRangeConstraint(40, 40), ValueRangeConstraint(45, 45), ValueRangeConstraint(50, 50), ValueRangeConstraint(55, 55), ValueRangeConstraint(60, 60), ValueRangeConstraint(65, 65), ValueRangeConstraint(70, 70), ValueRangeConstraint(75, 75), ValueRangeConstraint(80, 80), ValueRangeConstraint(85, 85), ValueRangeConstraint(90, 90), ValueRangeConstraint(95, 95), ValueRangeConstraint(100, 100), )
class Sixteenths(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

agentAutoVoIPCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1))
agentAutoVoIPTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1), )
if mibBuilder.loadTexts: agentAutoVoIPTable.setStatus('current')
agentAutoVoIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1, 1), ).setIndexNames((0, "FASTPATH-QOS-AUTOVOIP-MIB", "agentAutoVoIPIntfIndex"))
if mibBuilder.loadTexts: agentAutoVoIPEntry.setStatus('current')
agentAutoVoIPIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: agentAutoVoIPIntfIndex.setStatus('current')
agentAutoVoIPMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentAutoVoIPMode.setStatus('current')
agentAutoVoIPCosQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 3, 4, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentAutoVoIPCosQueue.setStatus('current')
mibBuilder.exportSymbols("FASTPATH-QOS-AUTOVOIP-MIB", agentAutoVoIPIntfIndex=agentAutoVoIPIntfIndex, agentAutoVoIPMode=agentAutoVoIPMode, PYSNMP_MODULE_ID=fastPathQOSAUTOVOIP, agentAutoVoIPCosQueue=agentAutoVoIPCosQueue, Sixteenths=Sixteenths, fastPathQOSAUTOVOIP=fastPathQOSAUTOVOIP, agentAutoVoIPTable=agentAutoVoIPTable, agentAutoVoIPEntry=agentAutoVoIPEntry, PercentByFives=PercentByFives, agentAutoVoIPCfgGroup=agentAutoVoIPCfgGroup)
