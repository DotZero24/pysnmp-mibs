#
# PySNMP MIB module HP-AUTZ-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HP-AUTZ-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:08:18 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
VidList, = mibBuilder.importSymbols("HP-ICF-TC", "VidList")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
hpSwitchAuthorizationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32))
hpSwitchAuthorizationMIB.setRevisions(('2018-08-20 00:00', '2018-03-19 00:00', '2017-07-16 00:00', '2017-03-16 00:00', '2016-10-20 00:00', '2016-05-09 00:00', '2016-01-07 00:00', '2014-08-04 00:00', '2011-02-07 00:00', '2007-08-29 00:00', '2005-10-05 00:00',))
if mibBuilder.loadTexts: hpSwitchAuthorizationMIB.setLastUpdated('201808200000Z')
if mibBuilder.loadTexts: hpSwitchAuthorizationMIB.setOrganization('HP Networking')
class HpAutzUserRoleName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '63a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 63)

hpicfSwitchAuthorizationNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 0))
hpicfSwitchAuthServerFail = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 0, 1)).setObjects(("HP-AUTZ-MIB", "hpicfSwitchAuthServerType"), ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIPType"), ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIP"))
if mibBuilder.loadTexts: hpicfSwitchAuthServerFail.setStatus('current')
hpSwitchAuthorizationConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1))
hpSwitchAutzServiceTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1), )
if mibBuilder.loadTexts: hpSwitchAutzServiceTable.setStatus('current')
hpSwitchAutzServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1), ).setIndexNames((0, "HP-AUTZ-MIB", "hpSwitchAutzServiceType"))
if mibBuilder.loadTexts: hpSwitchAutzServiceEntry.setStatus('current')
hpSwitchAutzServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("commands", 1), ("exec", 2), ("network", 3), ("restUri", 4))))
if mibBuilder.loadTexts: hpSwitchAutzServiceType.setStatus('current')
hpSwitchAutzServicePrimaryMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("local", 1), ("tacacs", 2), ("radius", 3), ("none", 4), ("auto", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzServicePrimaryMethod.setStatus('current')
hpSwitchAutzServiceSecondaryMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("none", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzServiceSecondaryMethod.setStatus('current')
hpSwitchAutzServiceCommandsLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("all", 1), ("managerlevelonly", 2))).clone('all')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzServiceCommandsLevel.setStatus('current')
hpicfSwitchAuthObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2))
hpicfSwitchAuthServerType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 9))).clone(namedValues=NamedValues(("radius", 1), ("tacacs", 2), ("other", 9)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfSwitchAuthServerType.setStatus('current')
hpicfSwitchAuthServerIPType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfSwitchAuthServerIPType.setStatus('current')
hpicfSwitchAuthServerIP = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 2, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfSwitchAuthServerIP.setStatus('current')
hpSwitchAuthConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 3))
hpicfSwitchAuthServerNotifyEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSwitchAuthServerNotifyEnable.setStatus('current')
hpSwitchAuthLocalPrivConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4))
hpSwitchLocalMgmtPrivGroupsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1), )
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivGroupsTable.setStatus('current')
hpSwitchLocalMgmtPrivGroupsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1), ).setIndexNames((0, "HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupIndex"))
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivGroupsEntry.setStatus('current')
hpSwitchLocalMgmtPrivGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivGroupIndex.setStatus('current')
hpSwitchLocalMgmtPrivGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivGroupName.setStatus('current')
hpSwitchLocalMgmtPrivGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivGroupStatus.setStatus('current')
hpSwitchLocalMgmtPrivCommandsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2), )
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCommandsTable.setStatus('current')
hpSwitchLocalMgmtPrivCommandsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1), ).setIndexNames((0, "HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupIndex"), (0, "HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdSequenceIndex"))
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCommandsEntry.setStatus('current')
hpSwitchLocalMgmtPrivCmdSequenceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCmdSequenceIndex.setStatus('current')
hpSwitchLocalMgmtPrivCmdMatchStr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCmdMatchStr.setStatus('current')
hpSwitchLocalMgmtPrivCmdPriv = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCmdPriv.setStatus('current')
hpSwitchLocalMgmtPrivCmdSendLog = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCmdSendLog.setStatus('current')
hpSwitchLocalMgmtPrivCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 4, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchLocalMgmtPrivCmdStatus.setStatus('current')
hpSwitchAutzUserRole = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5))
hpSwitchAutzUserRoleEnabled = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleEnabled.setStatus('current')
hpSwitchAutzUserRoleInitialRoleName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 2), HpAutzUserRoleName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleInitialRoleName.setStatus('current')
hpSwitchAutzUserRoleDownloadedEnabled = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleDownloadedEnabled.setStatus('current')
hpSwitchAutzUserRoleTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3), )
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTable.setStatus('current')
hpSwitchAutzUserRoleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1), ).setIndexNames((0, "HP-AUTZ-MIB", "hpSwitchAutzUserRoleName"))
if mibBuilder.loadTexts: hpSwitchAutzUserRoleEntry.setStatus('current')
hpSwitchAutzUserRoleName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 1), HpAutzUserRoleName())
if mibBuilder.loadTexts: hpSwitchAutzUserRoleName.setStatus('current')
hpSwitchAutzUserRoleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleRowStatus.setStatus('current')
hpSwitchAutzUserRoleType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("predefined", 1), ("local", 2), ("downloaded", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleType.setStatus('current')
hpSwitchAutzUserRoleCaptivePortalProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleCaptivePortalProfileName.setStatus('current')
hpSwitchAutzUserRoleIngressUserPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleIngressUserPolicyName.setStatus('current')
hpSwitchAutzUserRoleReauthPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999999999))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleReauthPeriod.setStatus('current')
hpSwitchAutzUserRoleVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 7), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleVlanId.setStatus('current')
hpSwitchAutzUserRoleVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleVlanName.setStatus('current')
hpSwitchAutzUserRoleTunneledNodeServerRedirect = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTunneledNodeServerRedirect.setStatus('current')
hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole.setStatus('current')
hpSwitchAutzUserRoleTaggedVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 11), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTaggedVlanId.setStatus('deprecated')
hpSwitchAutzUserRoleTaggedVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 12), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTaggedVlanName.setStatus('current')
hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 13), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole.setStatus('current')
hpSwitchAutzUserRoleLogOffPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 9999999), )).clone(300)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleLogOffPeriod.setStatus('current')
hpSwitchAutzUserRoleCachedReauthPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 15), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(60, 2147483647), ))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleCachedReauthPeriod.setStatus('current')
hpSwitchAutzUserRoleTaggedVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 3, 1, 16), VidList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleTaggedVlanList.setStatus('current')
hpSwitchAutzUserRoleSubTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 5), )
if mibBuilder.loadTexts: hpSwitchAutzUserRoleSubTable.setStatus('current')
hpSwitchAutzUserRoleSubEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 5, 1), ).setIndexNames((0, "HP-AUTZ-MIB", "hpSwitchAutzUserRoleName"), (0, "HP-AUTZ-MIB", "hpSwitchAutzUserRoleSubType"))
if mibBuilder.loadTexts: hpSwitchAutzUserRoleSubEntry.setStatus('current')
hpSwitchAutzUserRoleSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("device", 1))))
if mibBuilder.loadTexts: hpSwitchAutzUserRoleSubType.setStatus('current')
hpSwitchAutzUserRoleAdminEdgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 5, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleAdminEdgePort.setStatus('current')
hpSwitchAutzUserRolePoePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("default", 0), ("critical", 1), ("high", 2), ("low", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRolePoePriority.setStatus('current')
hpSwitchAutzUserRolePoeAllocBy = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("usage", 1), ("class", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRolePoeAllocBy.setStatus('current')
hpSwitchAutzUserRoleSubTypeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRoleSubTypeRowStatus.setStatus('current')
hpSwitchAutzUserRolePortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 1, 5, 5, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpSwitchAutzUserRolePortMode.setStatus('current')
hpSwitchAuthorizationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2))
hpSwitchAuthorizationMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1))
hpSwitchAuthorizationMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 1)).setObjects(("HP-AUTZ-MIB", "hpSwitchAuthorizationConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAuthorizationMIBCompliance = hpSwitchAuthorizationMIBCompliance.setStatus('current')
hpSwitchLocalMgmtPrivGrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 2)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzLocalMgmtPrivGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchLocalMgmtPrivGrpMIBCompliance = hpSwitchLocalMgmtPrivGrpMIBCompliance.setStatus('deprecated')
hpSwitchLocalMgmtPrivGrpMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 3)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzLocalMgmtPrivGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchLocalMgmtPrivGrpMIBCompliance1 = hpSwitchLocalMgmtPrivGrpMIBCompliance1.setStatus('deprecated')
hpSwitchAuthorizationObjectsGrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 4)).setObjects(("HP-AUTZ-MIB", "hpicfSwitchAuthorizationObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAuthorizationObjectsGrpMIBCompliance = hpSwitchAuthorizationObjectsGrpMIBCompliance.setStatus('current')
hpSwitchAuthorizationNotificationGrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 5)).setObjects(("HP-AUTZ-MIB", "hpicfSwitchAuthorizationNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAuthorizationNotificationGrpMIBCompliance = hpSwitchAuthorizationNotificationGrpMIBCompliance.setStatus('current')
hpSwitchAutzRoleGrpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 6)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzRoleGrpCompliance = hpSwitchAutzRoleGrpCompliance.setStatus('deprecated')
hpSwitchAutzRoleGrpCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 7)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzRoleGrpCompliance1 = hpSwitchAutzRoleGrpCompliance1.setStatus('deprecated')
hpSwitchAutzRoleGrpCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 8)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzRoleGrpCompliance2 = hpSwitchAutzRoleGrpCompliance2.setStatus('deprecated')
hpSwitchAutzRoleGrpCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 9)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzRoleGrpCompliance3 = hpSwitchAutzRoleGrpCompliance3.setStatus('deprecated')
hpSwitchAutzRoleGrpCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 10)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleGroup4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzRoleGrpCompliance4 = hpSwitchAutzRoleGrpCompliance4.setStatus('deprecated')
hpSwitchLocalMgmtPrivGrpMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 11)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzLocalMgmtPrivGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchLocalMgmtPrivGrpMIBCompliance2 = hpSwitchLocalMgmtPrivGrpMIBCompliance2.setStatus('current')
hpSwitchLocalMgmtPrivGrpMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 12)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzLocalMgmtPrivGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchLocalMgmtPrivGrpMIBCompliance3 = hpSwitchLocalMgmtPrivGrpMIBCompliance3.setStatus('current')
hpSwitchAutzRoleGrpCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 13)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleGroup5"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzRoleGrpCompliance5 = hpSwitchAutzRoleGrpCompliance5.setStatus('deprecated')
hpSwitchAutzRoleGrpCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 1, 14)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleGroup6"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzRoleGrpCompliance6 = hpSwitchAutzRoleGrpCompliance6.setStatus('current')
hpSwitchAuthorizationMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2))
hpSwitchAuthorizationConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 1)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzServicePrimaryMethod"), ("HP-AUTZ-MIB", "hpSwitchAutzServiceSecondaryMethod"), ("HP-AUTZ-MIB", "hpSwitchAutzServiceCommandsLevel"), ("HP-AUTZ-MIB", "hpicfSwitchAuthServerNotifyEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAuthorizationConfigGroup = hpSwitchAuthorizationConfigGroup.setStatus('current')
hpicfSwitchAuthorizationNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 2)).setObjects(("HP-AUTZ-MIB", "hpicfSwitchAuthServerFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSwitchAuthorizationNotificationGroup = hpicfSwitchAuthorizationNotificationGroup.setStatus('current')
hpicfSwitchAuthorizationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 3)).setObjects(("HP-AUTZ-MIB", "hpicfSwitchAuthServerType"), ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIPType"), ("HP-AUTZ-MIB", "hpicfSwitchAuthServerIP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSwitchAuthorizationObjectsGroup = hpicfSwitchAuthorizationObjectsGroup.setStatus('current')
hpSwitchAutzLocalMgmtPrivGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 4)).setObjects(("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupName"), ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdMatchStr"), ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdPriv"), ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdSendLog"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzLocalMgmtPrivGroup = hpSwitchAutzLocalMgmtPrivGroup.setStatus('current')
hpSwitchAutzLocalMgmtPrivGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 5)).setObjects(("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivCmdStatus"), ("HP-AUTZ-MIB", "hpSwitchLocalMgmtPrivGroupStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzLocalMgmtPrivGroup1 = hpSwitchAutzLocalMgmtPrivGroup1.setStatus('current')
hpSwitchAutzUserRoleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 6)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzUserRoleGroup = hpSwitchAutzUserRoleGroup.setStatus('deprecated')
hpSwitchAutzUserRoleGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 7)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzUserRoleGroup1 = hpSwitchAutzUserRoleGroup1.setStatus('deprecated')
hpSwitchAutzUserRoleGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 8)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzUserRoleGroup2 = hpSwitchAutzUserRoleGroup2.setStatus('deprecated')
hpSwitchAutzUserRoleGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 9)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleDownloadedEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzUserRoleGroup3 = hpSwitchAutzUserRoleGroup3.setStatus('deprecated')
hpSwitchAutzUserRoleGroup4 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 10)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleDownloadedEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzUserRoleGroup4 = hpSwitchAutzUserRoleGroup4.setStatus('deprecated')
hpSwitchAutzUserRoleGroup5 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 13)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleDownloadedEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleLogOffPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzUserRoleGroup5 = hpSwitchAutzUserRoleGroup5.setStatus('deprecated')
hpSwitchAutzUserRoleGroup6 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32, 2, 2, 14)).setObjects(("HP-AUTZ-MIB", "hpSwitchAutzUserRoleEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleInitialRoleName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleType"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCaptivePortalProfileName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleIngressUserPolicyName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanId"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerRedirect"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanName"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleDownloadedEnabled"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleLogOffPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleSubTypeRowStatus"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleAdminEdgePort"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRolePoePriority"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleCachedReauthPeriod"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRolePoeAllocBy"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRoleTaggedVlanList"), ("HP-AUTZ-MIB", "hpSwitchAutzUserRolePortMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpSwitchAutzUserRoleGroup6 = hpSwitchAutzUserRoleGroup6.setStatus('current')
mibBuilder.exportSymbols("HP-AUTZ-MIB", hpSwitchLocalMgmtPrivGroupsEntry=hpSwitchLocalMgmtPrivGroupsEntry, hpSwitchAutzUserRoleTaggedVlanName=hpSwitchAutzUserRoleTaggedVlanName, hpSwitchAuthorizationMIBGroups=hpSwitchAuthorizationMIBGroups, hpSwitchLocalMgmtPrivGroupsTable=hpSwitchLocalMgmtPrivGroupsTable, hpSwitchLocalMgmtPrivCmdPriv=hpSwitchLocalMgmtPrivCmdPriv, hpSwitchAutzUserRoleType=hpSwitchAutzUserRoleType, hpSwitchLocalMgmtPrivCmdStatus=hpSwitchLocalMgmtPrivCmdStatus, hpSwitchAuthorizationMIB=hpSwitchAuthorizationMIB, hpSwitchAutzServiceEntry=hpSwitchAutzServiceEntry, hpicfSwitchAuthServerFail=hpicfSwitchAuthServerFail, hpSwitchAutzUserRole=hpSwitchAutzUserRole, hpSwitchAuthorizationConfigGroup=hpSwitchAuthorizationConfigGroup, hpSwitchAutzRoleGrpCompliance=hpSwitchAutzRoleGrpCompliance, hpSwitchAutzServiceSecondaryMethod=hpSwitchAutzServiceSecondaryMethod, hpSwitchAutzUserRoleGroup2=hpSwitchAutzUserRoleGroup2, hpSwitchAutzRoleGrpCompliance4=hpSwitchAutzRoleGrpCompliance4, hpSwitchAutzServicePrimaryMethod=hpSwitchAutzServicePrimaryMethod, hpSwitchAutzUserRoleRowStatus=hpSwitchAutzUserRoleRowStatus, hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole=hpSwitchAutzUserRoleTunneledNodeServerSecondaryRole, hpSwitchAutzUserRoleTable=hpSwitchAutzUserRoleTable, hpSwitchAuthorizationObjectsGrpMIBCompliance=hpSwitchAuthorizationObjectsGrpMIBCompliance, hpSwitchAutzUserRoleSubTypeRowStatus=hpSwitchAutzUserRoleSubTypeRowStatus, hpSwitchAutzUserRoleEntry=hpSwitchAutzUserRoleEntry, hpSwitchAutzUserRoleTaggedVlanId=hpSwitchAutzUserRoleTaggedVlanId, hpSwitchLocalMgmtPrivGrpMIBCompliance1=hpSwitchLocalMgmtPrivGrpMIBCompliance1, hpSwitchAutzUserRoleSubEntry=hpSwitchAutzUserRoleSubEntry, hpSwitchAutzRoleGrpCompliance3=hpSwitchAutzRoleGrpCompliance3, hpSwitchAutzUserRoleLogOffPeriod=hpSwitchAutzUserRoleLogOffPeriod, hpSwitchAuthorizationConfig=hpSwitchAuthorizationConfig, hpSwitchAuthorizationNotificationGrpMIBCompliance=hpSwitchAuthorizationNotificationGrpMIBCompliance, hpSwitchLocalMgmtPrivCommandsEntry=hpSwitchLocalMgmtPrivCommandsEntry, hpicfSwitchAuthServerIPType=hpicfSwitchAuthServerIPType, hpSwitchAutzUserRoleIngressUserPolicyName=hpSwitchAutzUserRoleIngressUserPolicyName, hpSwitchAutzUserRoleTaggedVlanList=hpSwitchAutzUserRoleTaggedVlanList, hpSwitchAutzUserRoleGroup1=hpSwitchAutzUserRoleGroup1, hpSwitchAutzUserRoleTunneledNodeServerRedirect=hpSwitchAutzUserRoleTunneledNodeServerRedirect, hpSwitchAutzRoleGrpCompliance1=hpSwitchAutzRoleGrpCompliance1, hpicfSwitchAuthorizationNotifications=hpicfSwitchAuthorizationNotifications, PYSNMP_MODULE_ID=hpSwitchAuthorizationMIB, hpSwitchAuthLocalPrivConfigObjects=hpSwitchAuthLocalPrivConfigObjects, hpSwitchAutzUserRoleName=hpSwitchAutzUserRoleName, hpSwitchAutzUserRoleCachedReauthPeriod=hpSwitchAutzUserRoleCachedReauthPeriod, hpSwitchAutzServiceType=hpSwitchAutzServiceType, hpicfSwitchAuthorizationNotificationGroup=hpicfSwitchAuthorizationNotificationGroup, hpSwitchLocalMgmtPrivGroupStatus=hpSwitchLocalMgmtPrivGroupStatus, hpSwitchAutzUserRoleDownloadedEnabled=hpSwitchAutzUserRoleDownloadedEnabled, hpSwitchLocalMgmtPrivGroupName=hpSwitchLocalMgmtPrivGroupName, hpSwitchLocalMgmtPrivGroupIndex=hpSwitchLocalMgmtPrivGroupIndex, hpSwitchAutzUserRoleGroup6=hpSwitchAutzUserRoleGroup6, hpSwitchAutzLocalMgmtPrivGroup1=hpSwitchAutzLocalMgmtPrivGroup1, hpSwitchAutzUserRoleEnabled=hpSwitchAutzUserRoleEnabled, hpSwitchAuthorizationMIBCompliances=hpSwitchAuthorizationMIBCompliances, hpSwitchAutzUserRoleVlanName=hpSwitchAutzUserRoleVlanName, hpSwitchAutzServiceCommandsLevel=hpSwitchAutzServiceCommandsLevel, hpSwitchAuthorizationMIBCompliance=hpSwitchAuthorizationMIBCompliance, hpSwitchLocalMgmtPrivCmdMatchStr=hpSwitchLocalMgmtPrivCmdMatchStr, hpicfSwitchAuthObjects=hpicfSwitchAuthObjects, hpicfSwitchAuthServerType=hpicfSwitchAuthServerType, hpSwitchAutzUserRoleGroup=hpSwitchAutzUserRoleGroup, HpAutzUserRoleName=HpAutzUserRoleName, hpSwitchAutzUserRolePoePriority=hpSwitchAutzUserRolePoePriority, hpSwitchAutzUserRoleGroup4=hpSwitchAutzUserRoleGroup4, hpSwitchLocalMgmtPrivGrpMIBCompliance=hpSwitchLocalMgmtPrivGrpMIBCompliance, hpSwitchAutzRoleGrpCompliance6=hpSwitchAutzRoleGrpCompliance6, hpSwitchAutzLocalMgmtPrivGroup=hpSwitchAutzLocalMgmtPrivGroup, hpSwitchAutzUserRoleGroup3=hpSwitchAutzUserRoleGroup3, hpSwitchAutzUserRoleReauthPeriod=hpSwitchAutzUserRoleReauthPeriod, hpSwitchAutzUserRoleGroup5=hpSwitchAutzUserRoleGroup5, hpSwitchLocalMgmtPrivCmdSendLog=hpSwitchLocalMgmtPrivCmdSendLog, hpSwitchAuthConfigObjects=hpSwitchAuthConfigObjects, hpSwitchAutzUserRoleInitialRoleName=hpSwitchAutzUserRoleInitialRoleName, hpSwitchAutzUserRoleSubType=hpSwitchAutzUserRoleSubType, hpSwitchAutzUserRoleVlanId=hpSwitchAutzUserRoleVlanId, hpicfSwitchAuthServerNotifyEnable=hpicfSwitchAuthServerNotifyEnable, hpSwitchAutzServiceTable=hpSwitchAutzServiceTable, hpSwitchAuthorizationConformance=hpSwitchAuthorizationConformance, hpSwitchAutzRoleGrpCompliance2=hpSwitchAutzRoleGrpCompliance2, hpSwitchLocalMgmtPrivGrpMIBCompliance3=hpSwitchLocalMgmtPrivGrpMIBCompliance3, hpSwitchAutzUserRolePoeAllocBy=hpSwitchAutzUserRolePoeAllocBy, hpSwitchAutzUserRolePortMode=hpSwitchAutzUserRolePortMode, hpSwitchAutzUserRoleCaptivePortalProfileName=hpSwitchAutzUserRoleCaptivePortalProfileName, hpSwitchLocalMgmtPrivCommandsTable=hpSwitchLocalMgmtPrivCommandsTable, hpSwitchAutzUserRoleSubTable=hpSwitchAutzUserRoleSubTable, hpSwitchLocalMgmtPrivGrpMIBCompliance2=hpSwitchLocalMgmtPrivGrpMIBCompliance2, hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole=hpSwitchAutzUserRoleTunneledNodeServerDownloadableRole, hpicfSwitchAuthorizationObjectsGroup=hpicfSwitchAuthorizationObjectsGroup, hpSwitchAutzUserRoleAdminEdgePort=hpSwitchAutzUserRoleAdminEdgePort, hpicfSwitchAuthServerIP=hpicfSwitchAuthServerIP, hpSwitchAutzRoleGrpCompliance5=hpSwitchAutzRoleGrpCompliance5, hpSwitchLocalMgmtPrivCmdSequenceIndex=hpSwitchLocalMgmtPrivCmdSequenceIndex)
