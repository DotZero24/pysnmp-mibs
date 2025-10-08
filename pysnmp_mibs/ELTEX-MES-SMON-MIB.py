#
# PySNMP MIB module ELTEX-MES-SMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-SMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("ELTEX-MES-SMON-MIB", EltPortCopyRemoteDirectionType=EltPortCopyRemoteDirectionType, eltMesSmon=eltMesSmon, eltPortCopyRemoteVlan=eltPortCopyRemoteVlan, eltPortCopyRemoteDirection=eltPortCopyRemoteDirection, eltPortCopyRemoteStatus=eltPortCopyRemoteStatus, PYSNMP_MODULE_ID=eltMesSmon, eltPortCopyRemoteTable=eltPortCopyRemoteTable, eltPortCopyRemoteEntry=eltPortCopyRemoteEntry, eltPortCopyRemotePrio=eltPortCopyRemotePrio)
