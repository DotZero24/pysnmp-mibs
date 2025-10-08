#
# PySNMP MIB module ELTEX-MES-SMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-SMON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:41 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
class EltPortCopyRemoteDirectionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eltPortCopyRemoteRx", 1), ("eltPortCopyRemoteTx", 2))

eltMesSmon = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84))
eltMesSmon.setRevisions(('2016-02-10 00:00',))
if mibBuilder.loadTexts: eltMesSmon.setLastUpdated('201602100000Z')
if mibBuilder.loadTexts: eltMesSmon.setOrganization('Eltex Enterprise, Ltd.')
eltPortCopyRemoteTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1), )
if mibBuilder.loadTexts: eltPortCopyRemoteTable.setStatus('current')
eltPortCopyRemoteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1), ).setIndexNames((0, "ELTEX-MES-SMON-MIB", "eltPortCopyRemoteDirection"))
if mibBuilder.loadTexts: eltPortCopyRemoteEntry.setStatus('current')
eltPortCopyRemoteDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 1), EltPortCopyRemoteDirectionType())
if mibBuilder.loadTexts: eltPortCopyRemoteDirection.setStatus('current')
eltPortCopyRemoteVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 2), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltPortCopyRemoteVlan.setStatus('current')
eltPortCopyRemotePrio = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltPortCopyRemotePrio.setStatus('current')
eltPortCopyRemoteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eltPortCopyRemoteStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-SMON-MIB", eltPortCopyRemoteDirection=eltPortCopyRemoteDirection, eltPortCopyRemoteEntry=eltPortCopyRemoteEntry, PYSNMP_MODULE_ID=eltMesSmon, eltPortCopyRemoteStatus=eltPortCopyRemoteStatus, EltPortCopyRemoteDirectionType=EltPortCopyRemoteDirectionType, eltPortCopyRemotePrio=eltPortCopyRemotePrio, eltPortCopyRemoteTable=eltPortCopyRemoteTable, eltPortCopyRemoteVlan=eltPortCopyRemoteVlan, eltMesSmon=eltMesSmon)
