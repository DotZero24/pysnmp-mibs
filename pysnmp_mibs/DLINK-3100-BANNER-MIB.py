_G='not-accessible'
_F='rlBannerMessageIndex'
_E='Integer32'
_D='rlBannerMessageType'
_C='DLINK-3100-BANNER-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('DLINK-3100-MIB','rnd')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rlBanner=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,133))
if mibBuilder.loadTexts:rlBanner.setRevisions(('2007-12-16 00:00',))
class BannerMessageType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rlBannerMOTD',1),('rlBannerLogin',2),('rlBannerExec',3)))
_RlBannerMessageTable_Object=MibTable
rlBannerMessageTable=_RlBannerMessageTable_Object((1,3,6,1,4,1,171,10,94,89,89,133,1))
if mibBuilder.loadTexts:rlBannerMessageTable.setStatus(_A)
_RlBannerMessageEntry_Object=MibTableRow
rlBannerMessageEntry=_RlBannerMessageEntry_Object((1,3,6,1,4,1,171,10,94,89,89,133,1,1))
rlBannerMessageEntry.setIndexNames((0,_C,_D),(0,_C,_F))
if mibBuilder.loadTexts:rlBannerMessageEntry.setStatus(_A)
_RlBannerMessageType_Type=BannerMessageType
_RlBannerMessageType_Object=MibTableColumn
rlBannerMessageType=_RlBannerMessageType_Object((1,3,6,1,4,1,171,10,94,89,89,133,1,1,1),_RlBannerMessageType_Type())
rlBannerMessageType.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBannerMessageType.setStatus(_A)
class _RlBannerMessageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,13))
_RlBannerMessageIndex_Type.__name__=_E
_RlBannerMessageIndex_Object=MibTableColumn
rlBannerMessageIndex=_RlBannerMessageIndex_Object((1,3,6,1,4,1,171,10,94,89,89,133,1,1,2),_RlBannerMessageIndex_Type())
rlBannerMessageIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rlBannerMessageIndex.setStatus(_A)
_RlBannerMessageText_Type=SnmpAdminString
_RlBannerMessageText_Object=MibTableColumn
rlBannerMessageText=_RlBannerMessageText_Object((1,3,6,1,4,1,171,10,94,89,89,133,1,1,3),_RlBannerMessageText_Type())
rlBannerMessageText.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBannerMessageText.setStatus(_A)
_RlBannerManageTable_Object=MibTable
rlBannerManageTable=_RlBannerManageTable_Object((1,3,6,1,4,1,171,10,94,89,89,133,2))
if mibBuilder.loadTexts:rlBannerManageTable.setStatus(_A)
_RlBannerManageEntry_Object=MibTableRow
rlBannerManageEntry=_RlBannerManageEntry_Object((1,3,6,1,4,1,171,10,94,89,89,133,2,1))
rlBannerManageEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:rlBannerManageEntry.setStatus(_A)
_RlBannerManageSSH_Type=EnabledStatus
_RlBannerManageSSH_Object=MibTableColumn
rlBannerManageSSH=_RlBannerManageSSH_Object((1,3,6,1,4,1,171,10,94,89,89,133,2,1,1),_RlBannerManageSSH_Type())
rlBannerManageSSH.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBannerManageSSH.setStatus(_A)
_RlBannerManageTelnet_Type=EnabledStatus
_RlBannerManageTelnet_Object=MibTableColumn
rlBannerManageTelnet=_RlBannerManageTelnet_Object((1,3,6,1,4,1,171,10,94,89,89,133,2,1,2),_RlBannerManageTelnet_Type())
rlBannerManageTelnet.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBannerManageTelnet.setStatus(_A)
_RlBannerManageConsole_Type=EnabledStatus
_RlBannerManageConsole_Object=MibTableColumn
rlBannerManageConsole=_RlBannerManageConsole_Object((1,3,6,1,4,1,171,10,94,89,89,133,2,1,3),_RlBannerManageConsole_Type())
rlBannerManageConsole.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBannerManageConsole.setStatus(_A)
_RlBannerMessageClear_Type=BannerMessageType
_RlBannerMessageClear_Object=MibScalar
rlBannerMessageClear=_RlBannerMessageClear_Object((1,3,6,1,4,1,171,10,94,89,89,133,3),_RlBannerMessageClear_Type())
rlBannerMessageClear.setMaxAccess(_B)
if mibBuilder.loadTexts:rlBannerMessageClear.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'BannerMessageType':BannerMessageType,'rlBanner':rlBanner,'rlBannerMessageTable':rlBannerMessageTable,'rlBannerMessageEntry':rlBannerMessageEntry,_D:rlBannerMessageType,_F:rlBannerMessageIndex,'rlBannerMessageText':rlBannerMessageText,'rlBannerManageTable':rlBannerManageTable,'rlBannerManageEntry':rlBannerManageEntry,'rlBannerManageSSH':rlBannerManageSSH,'rlBannerManageTelnet':rlBannerManageTelnet,'rlBannerManageConsole':rlBannerManageConsole,'rlBannerMessageClear':rlBannerMessageClear})