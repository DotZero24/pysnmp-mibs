#
# PySNMP MIB module CISCOSB-BANNER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciscosb/CISCOSB-BANNER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:32:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rlBanner = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133))
rlBanner.setRevisions(('2007-12-16 00:00',))
if mibBuilder.loadTexts: rlBanner.setLastUpdated('200803160000Z')
if mibBuilder.loadTexts: rlBanner.setOrganization('Cisco Systems, Inc.')
class BannerMessageType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rlBannerMOTD", 1), ("rlBannerLogin", 2), ("rlBannerExec", 3))

rlBannerMessageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 1), )
if mibBuilder.loadTexts: rlBannerMessageTable.setStatus('current')
rlBannerMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 1, 1), ).setIndexNames((0, "CISCOSB-BANNER-MIB", "rlBannerMessageType"), (0, "CISCOSB-BANNER-MIB", "rlBannerMessageIndex"))
if mibBuilder.loadTexts: rlBannerMessageEntry.setStatus('current')
rlBannerMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 1, 1, 1), BannerMessageType())
if mibBuilder.loadTexts: rlBannerMessageType.setStatus('current')
rlBannerMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13)))
if mibBuilder.loadTexts: rlBannerMessageIndex.setStatus('current')
rlBannerMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 1, 1, 3), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerMessageText.setStatus('current')
rlBannerManageTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 2), )
if mibBuilder.loadTexts: rlBannerManageTable.setStatus('current')
rlBannerManageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 2, 1), ).setIndexNames((0, "CISCOSB-BANNER-MIB", "rlBannerMessageType"))
if mibBuilder.loadTexts: rlBannerManageEntry.setStatus('current')
rlBannerManageSSH = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 2, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageSSH.setStatus('current')
rlBannerManageTelnet = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 2, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageTelnet.setStatus('current')
rlBannerManageConsole = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 2, 1, 3), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerManageConsole.setStatus('current')
rlBannerMessageClear = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 133, 3), BannerMessageType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBannerMessageClear.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-BANNER-MIB", rlBannerManageSSH=rlBannerManageSSH, rlBanner=rlBanner, rlBannerMessageClear=rlBannerMessageClear, rlBannerMessageType=rlBannerMessageType, rlBannerMessageTable=rlBannerMessageTable, rlBannerManageEntry=rlBannerManageEntry, PYSNMP_MODULE_ID=rlBanner, BannerMessageType=BannerMessageType, rlBannerMessageIndex=rlBannerMessageIndex, rlBannerManageTelnet=rlBannerManageTelnet, rlBannerManageTable=rlBannerManageTable, rlBannerManageConsole=rlBannerManageConsole, rlBannerMessageText=rlBannerMessageText, rlBannerMessageEntry=rlBannerMessageEntry)
