#
# PySNMP MIB module RADLAN-BANNER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/radlan/RADLAN-BANNER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
rlBanner = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 133))
rlBanner.setRevisions(('2007-12-16 00:00',))
if mibBuilder.loadTexts: rlBanner.setLastUpdated('200803160000Z')
if mibBuilder.loadTexts: rlBanner.setOrganization('Marvell Computer Communications Ltd.')
class BannerMessageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rlBannerMOTD", 1), ("rlBannerLogin", 2), ("rlBannerExec", 3))

rlBannerMessageTable = MibTable((1, 3, 6, 1, 4, 1, 89, 133, 1), )
if mibBuilder.loadTexts: rlBannerMessageTable.setStatus('current')
rlBannerMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 133, 1, 1), ).setIndexNames((0, "RADLAN-BANNER-MIB", "rlBannerMessageType"), (0, "RADLAN-BANNER-MIB", "rlBannerMessageIndex"))
if mibBuilder.loadTexts: rlBannerMessageEntry.setStatus('current')
rlBannerMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 1, 1, 1), BannerMessageType())
if mibBuilder.loadTexts: rlBannerMessageType.setStatus('current')
rlBannerMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13)))
if mibBuilder.loadTexts: rlBannerMessageIndex.setStatus('current')
rlBannerMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 1, 1, 3), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerMessageText.setStatus('current')
rlBannerManageTable = MibTable((1, 3, 6, 1, 4, 1, 89, 133, 2), )
if mibBuilder.loadTexts: rlBannerManageTable.setStatus('current')
rlBannerManageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 133, 2, 1), ).setIndexNames((0, "RADLAN-BANNER-MIB", "rlBannerMessageType"))
if mibBuilder.loadTexts: rlBannerManageEntry.setStatus('current')
rlBannerManageSSH = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageSSH.setStatus('current')
rlBannerManageTelnet = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 2, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageTelnet.setStatus('current')
rlBannerManageConsole = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 133, 2, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageConsole.setStatus('current')
rlBannerMessageClear = MibScalar((1, 3, 6, 1, 4, 1, 89, 133, 3), BannerMessageType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerMessageClear.setStatus('current')
mibBuilder.exportSymbols("RADLAN-BANNER-MIB", rlBannerManageSSH=rlBannerManageSSH, rlBannerManageEntry=rlBannerManageEntry, BannerMessageType=BannerMessageType, rlBannerMessageType=rlBannerMessageType, rlBannerMessageEntry=rlBannerMessageEntry, rlBannerMessageText=rlBannerMessageText, rlBannerManageTable=rlBannerManageTable, rlBannerMessageIndex=rlBannerMessageIndex, PYSNMP_MODULE_ID=rlBanner, rlBannerManageConsole=rlBannerManageConsole, rlBannerMessageClear=rlBannerMessageClear, rlBanner=rlBanner, rlBannerManageTelnet=rlBannerManageTelnet, rlBannerMessageTable=rlBannerMessageTable)
