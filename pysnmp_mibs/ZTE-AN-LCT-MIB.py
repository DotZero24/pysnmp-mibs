_S='zxAnLctAccessTrapsGroup'
_R='zxAnLctAccessGroup'
_Q='zxAnLctGlobalGroup'
_P='zxAnLctAccessLogoutTrap'
_O='zxAnLctAccessLoginTrap'
_N='zxAnLctAccessRowStatus'
_M='zxAnLctAccessHeartbeatTimeOut'
_L='zxAnLctAccessHeartbeatAction'
_K='read-only'
_J='read-create'
_I='zxAnLctAccessSessionId'
_H='read-write'
_G='zxAnLctAccessUserName'
_F='zxAnLctAccessSourceIpAddress'
_E='zxAnLctAccessDetailInfo'
_D='DisplayString'
_C='Integer32'
_B='current'
_A='ZTE-AN-LCT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
zxAnSysObjects,=mibBuilder.importSymbols('ZTE-AN-SYS-MIB','zxAnSysObjects')
zxAnLctMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,1,1,150))
if mibBuilder.loadTexts:zxAnLctMib.setRevisions(('2011-08-23 00:00',))
_ZxAnLctGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnLctGlobalObjects=_ZxAnLctGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1,1,150,1))
class _ZxAnLctAccessHeartbeatAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('heartbeat',1))
_ZxAnLctAccessHeartbeatAction_Type.__name__=_C
_ZxAnLctAccessHeartbeatAction_Object=MibScalar
zxAnLctAccessHeartbeatAction=_ZxAnLctAccessHeartbeatAction_Object((1,3,6,1,4,1,3902,1015,1,1,150,1,1),_ZxAnLctAccessHeartbeatAction_Type())
zxAnLctAccessHeartbeatAction.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnLctAccessHeartbeatAction.setStatus(_B)
class _ZxAnLctAccessHeartbeatTimeOut_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_ZxAnLctAccessHeartbeatTimeOut_Type.__name__=_C
_ZxAnLctAccessHeartbeatTimeOut_Object=MibScalar
zxAnLctAccessHeartbeatTimeOut=_ZxAnLctAccessHeartbeatTimeOut_Object((1,3,6,1,4,1,3902,1015,1,1,150,1,2),_ZxAnLctAccessHeartbeatTimeOut_Type())
zxAnLctAccessHeartbeatTimeOut.setMaxAccess(_H)
if mibBuilder.loadTexts:zxAnLctAccessHeartbeatTimeOut.setStatus(_B)
if mibBuilder.loadTexts:zxAnLctAccessHeartbeatTimeOut.setUnits('seconds')
_ZxAnLctObjects_ObjectIdentity=ObjectIdentity
zxAnLctObjects=_ZxAnLctObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1,1,150,2))
_ZxAnLctAccessObjects_ObjectIdentity=ObjectIdentity
zxAnLctAccessObjects=_ZxAnLctAccessObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1,1,150,2,1))
_ZxAnLctAccessTable_Object=MibTable
zxAnLctAccessTable=_ZxAnLctAccessTable_Object((1,3,6,1,4,1,3902,1015,1,1,150,2,1,1))
if mibBuilder.loadTexts:zxAnLctAccessTable.setStatus(_B)
_ZxAnLctAccessEntry_Object=MibTableRow
zxAnLctAccessEntry=_ZxAnLctAccessEntry_Object((1,3,6,1,4,1,3902,1015,1,1,150,2,1,1,1))
zxAnLctAccessEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:zxAnLctAccessEntry.setStatus(_B)
class _ZxAnLctAccessSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ZxAnLctAccessSessionId_Type.__name__=_C
_ZxAnLctAccessSessionId_Object=MibTableColumn
zxAnLctAccessSessionId=_ZxAnLctAccessSessionId_Object((1,3,6,1,4,1,3902,1015,1,1,150,2,1,1,1,1),_ZxAnLctAccessSessionId_Type())
zxAnLctAccessSessionId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxAnLctAccessSessionId.setStatus(_B)
class _ZxAnLctAccessDetailInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_ZxAnLctAccessDetailInfo_Type.__name__=_D
_ZxAnLctAccessDetailInfo_Object=MibTableColumn
zxAnLctAccessDetailInfo=_ZxAnLctAccessDetailInfo_Object((1,3,6,1,4,1,3902,1015,1,1,150,2,1,1,1,2),_ZxAnLctAccessDetailInfo_Type())
zxAnLctAccessDetailInfo.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnLctAccessDetailInfo.setStatus(_B)
class _ZxAnLctAccessSourceIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_ZxAnLctAccessSourceIpAddress_Type.__name__=_D
_ZxAnLctAccessSourceIpAddress_Object=MibTableColumn
zxAnLctAccessSourceIpAddress=_ZxAnLctAccessSourceIpAddress_Object((1,3,6,1,4,1,3902,1015,1,1,150,2,1,1,1,3),_ZxAnLctAccessSourceIpAddress_Type())
zxAnLctAccessSourceIpAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnLctAccessSourceIpAddress.setStatus(_B)
class _ZxAnLctAccessUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxAnLctAccessUserName_Type.__name__=_D
_ZxAnLctAccessUserName_Object=MibTableColumn
zxAnLctAccessUserName=_ZxAnLctAccessUserName_Object((1,3,6,1,4,1,3902,1015,1,1,150,2,1,1,1,4),_ZxAnLctAccessUserName_Type())
zxAnLctAccessUserName.setMaxAccess(_K)
if mibBuilder.loadTexts:zxAnLctAccessUserName.setStatus(_B)
_ZxAnLctAccessRowStatus_Type=RowStatus
_ZxAnLctAccessRowStatus_Object=MibTableColumn
zxAnLctAccessRowStatus=_ZxAnLctAccessRowStatus_Object((1,3,6,1,4,1,3902,1015,1,1,150,2,1,1,1,50),_ZxAnLctAccessRowStatus_Type())
zxAnLctAccessRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnLctAccessRowStatus.setStatus(_B)
_ZxAnLctNotifications_ObjectIdentity=ObjectIdentity
zxAnLctNotifications=_ZxAnLctNotifications_ObjectIdentity((1,3,6,1,4,1,3902,1015,1,1,150,3))
_ZxAnLctAccessTraps_ObjectIdentity=ObjectIdentity
zxAnLctAccessTraps=_ZxAnLctAccessTraps_ObjectIdentity((1,3,6,1,4,1,3902,1015,1,1,150,3,1))
_ZxAnLctConformance_ObjectIdentity=ObjectIdentity
zxAnLctConformance=_ZxAnLctConformance_ObjectIdentity((1,3,6,1,4,1,3902,1015,1,1,150,4))
_ZxAnLctCompliances_ObjectIdentity=ObjectIdentity
zxAnLctCompliances=_ZxAnLctCompliances_ObjectIdentity((1,3,6,1,4,1,3902,1015,1,1,150,4,1))
_ZxAnLctGroups_ObjectIdentity=ObjectIdentity
zxAnLctGroups=_ZxAnLctGroups_ObjectIdentity((1,3,6,1,4,1,3902,1015,1,1,150,4,2))
zxAnLctGlobalGroup=ObjectGroup((1,3,6,1,4,1,3902,1015,1,1,150,4,2,1))
zxAnLctGlobalGroup.setObjects(*((_A,_L),(_A,_M)))
if mibBuilder.loadTexts:zxAnLctGlobalGroup.setStatus(_B)
zxAnLctAccessGroup=ObjectGroup((1,3,6,1,4,1,3902,1015,1,1,150,4,2,2))
zxAnLctAccessGroup.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_N)))
if mibBuilder.loadTexts:zxAnLctAccessGroup.setStatus(_B)
zxAnLctAccessTrapsGroup=ObjectGroup((1,3,6,1,4,1,3902,1015,1,1,150,4,2,3))
zxAnLctAccessTrapsGroup.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:zxAnLctAccessTrapsGroup.setStatus(_B)
zxAnLctAccessLoginTrap=NotificationType((1,3,6,1,4,1,3902,1015,1,1,150,3,1,1))
zxAnLctAccessLoginTrap.setObjects(*((_A,_F),(_A,_G),(_A,_E)))
if mibBuilder.loadTexts:zxAnLctAccessLoginTrap.setStatus(_B)
zxAnLctAccessLogoutTrap=NotificationType((1,3,6,1,4,1,3902,1015,1,1,150,3,1,2))
zxAnLctAccessLogoutTrap.setObjects(*((_A,_F),(_A,_G),(_A,_E)))
if mibBuilder.loadTexts:zxAnLctAccessLogoutTrap.setStatus(_B)
zxAnLctCompliance=ModuleCompliance((1,3,6,1,4,1,3902,1015,1,1,150,4,1,1))
zxAnLctCompliance.setObjects(*((_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:zxAnLctCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'zxAnLctMib':zxAnLctMib,'zxAnLctGlobalObjects':zxAnLctGlobalObjects,_L:zxAnLctAccessHeartbeatAction,_M:zxAnLctAccessHeartbeatTimeOut,'zxAnLctObjects':zxAnLctObjects,'zxAnLctAccessObjects':zxAnLctAccessObjects,'zxAnLctAccessTable':zxAnLctAccessTable,'zxAnLctAccessEntry':zxAnLctAccessEntry,_I:zxAnLctAccessSessionId,_E:zxAnLctAccessDetailInfo,_F:zxAnLctAccessSourceIpAddress,_G:zxAnLctAccessUserName,_N:zxAnLctAccessRowStatus,'zxAnLctNotifications':zxAnLctNotifications,'zxAnLctAccessTraps':zxAnLctAccessTraps,_O:zxAnLctAccessLoginTrap,_P:zxAnLctAccessLogoutTrap,'zxAnLctConformance':zxAnLctConformance,'zxAnLctCompliances':zxAnLctCompliances,'zxAnLctCompliance':zxAnLctCompliance,'zxAnLctGroups':zxAnLctGroups,_Q:zxAnLctGlobalGroup,_R:zxAnLctAccessGroup,_S:zxAnLctAccessTrapsGroup})