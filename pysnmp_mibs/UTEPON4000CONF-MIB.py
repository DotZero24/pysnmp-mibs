_Z='read-create'
_Y='utsMonitorSessionID'
_X='utsLedGEPortSlotLedDispSlotId'
_W='utsLedPonSlotLedDispSlotId'
_V='abnormal'
_U='normal'
_T='disable'
_S='enable'
_R='active'
_Q='utsEponModuleBoardPhyId'
_P='installed-and-work'
_O='installed-not-work'
_N='empty'
_M='UTEPON4000CONF-MIB'
_L='yellow-off'
_K='yellow-on'
_J='red-off'
_I='red-on'
_H='DisplayString'
_G='flashing'
_F='read-write'
_E='green-off'
_D='green-on'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,MacAddress,Timeout=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId','MacAddress','Timeout')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention','TruthValue')
utsGeponBBS4000,=mibBuilder.importSymbols('UTS-BBS-COMMON-MIB','utsGeponBBS4000')
utsGeponBBS4000Configuration=ModuleIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2))
class UtsSyslogServerityLevelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergencies',1),('alerts',2),('critical',3),('errors',4),('warnings',5),('notifications',6),('informational',7),('debugging',8)))
class UtsConfStationIdType(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
class UtsConfStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('success',1),('failure',2),('busy',3)))
_UtsSystemConfExt_ObjectIdentity=ObjectIdentity
utsSystemConfExt=_UtsSystemConfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1))
_UtsSystemExtObjects_ObjectIdentity=ObjectIdentity
utsSystemExtObjects=_UtsSystemExtObjects_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1))
_UtsEponModuleBoardTable_Object=MibTable
utsEponModuleBoardTable=_UtsEponModuleBoardTable_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1))
if mibBuilder.loadTexts:utsEponModuleBoardTable.setStatus(_A)
_UtsEponModuleBoardEntry_Object=MibTableRow
utsEponModuleBoardEntry=_UtsEponModuleBoardEntry_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1))
utsEponModuleBoardEntry.setIndexNames((0,_M,_Q))
if mibBuilder.loadTexts:utsEponModuleBoardEntry.setStatus(_A)
class _UtsEponModuleBoardPhyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_UtsEponModuleBoardPhyId_Type.__name__=_C
_UtsEponModuleBoardPhyId_Object=MibTableColumn
utsEponModuleBoardPhyId=_UtsEponModuleBoardPhyId_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,1),_UtsEponModuleBoardPhyId_Type())
utsEponModuleBoardPhyId.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardPhyId.setStatus(_A)
class _UtsEponModuleBoardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('csm',2),('epm04a',3),('epm04b',4),('epm04c',5),('gem04a',6),('gem04b',7),('xgm01a',8),('osm04a',9),('gpm02a',10)))
_UtsEponModuleBoardType_Type.__name__=_C
_UtsEponModuleBoardType_Object=MibTableColumn
utsEponModuleBoardType=_UtsEponModuleBoardType_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,2),_UtsEponModuleBoardType_Type())
utsEponModuleBoardType.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardType.setStatus(_A)
class _UtsEponModulePhyPresenceStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('installed',1),('not-installed',2)))
_UtsEponModulePhyPresenceStat_Type.__name__=_C
_UtsEponModulePhyPresenceStat_Object=MibTableColumn
utsEponModulePhyPresenceStat=_UtsEponModulePhyPresenceStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,3),_UtsEponModulePhyPresenceStat_Type())
utsEponModulePhyPresenceStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModulePhyPresenceStat.setStatus(_A)
class _UtsEponModuleAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,8)));namedValues=NamedValues(*(('locked',1),('unlocked',2),('reset',8)))
_UtsEponModuleAdminState_Type.__name__=_C
_UtsEponModuleAdminState_Object=MibTableColumn
utsEponModuleAdminState=_UtsEponModuleAdminState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,4),_UtsEponModuleAdminState_Type())
utsEponModuleAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:utsEponModuleAdminState.setStatus(_A)
class _UtsEponModuleOperationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('inactive',2),(_R,3)))
_UtsEponModuleOperationState_Type.__name__=_C
_UtsEponModuleOperationState_Object=MibTableColumn
utsEponModuleOperationState=_UtsEponModuleOperationState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,5),_UtsEponModuleOperationState_Type())
utsEponModuleOperationState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleOperationState.setStatus(_A)
class _UtsEponModuleRedundancyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),(_R,2),('standby',3)))
_UtsEponModuleRedundancyState_Type.__name__=_C
_UtsEponModuleRedundancyState_Object=MibTableColumn
utsEponModuleRedundancyState=_UtsEponModuleRedundancyState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,6),_UtsEponModuleRedundancyState_Type())
utsEponModuleRedundancyState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleRedundancyState.setStatus(_A)
_UtsEponModulePhyicalUptime_Type=TimeTicks
_UtsEponModulePhyicalUptime_Object=MibTableColumn
utsEponModulePhyicalUptime=_UtsEponModulePhyicalUptime_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,8),_UtsEponModulePhyicalUptime_Type())
utsEponModulePhyicalUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModulePhyicalUptime.setStatus(_A)
_UtsEponOpStateUptime_Type=TimeTicks
_UtsEponOpStateUptime_Object=MibTableColumn
utsEponOpStateUptime=_UtsEponOpStateUptime_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,9),_UtsEponOpStateUptime_Type())
utsEponOpStateUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponOpStateUptime.setStatus(_A)
_UtsEponModuleCSMSwitchtime_Type=TimeTicks
_UtsEponModuleCSMSwitchtime_Object=MibTableColumn
utsEponModuleCSMSwitchtime=_UtsEponModuleCSMSwitchtime_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,11),_UtsEponModuleCSMSwitchtime_Type())
utsEponModuleCSMSwitchtime.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleCSMSwitchtime.setStatus(_A)
class _UtsEponModuleBoardSwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UtsEponModuleBoardSwVer_Type.__name__=_H
_UtsEponModuleBoardSwVer_Object=MibTableColumn
utsEponModuleBoardSwVer=_UtsEponModuleBoardSwVer_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,12),_UtsEponModuleBoardSwVer_Type())
utsEponModuleBoardSwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardSwVer.setStatus(_A)
class _UtsEponModuleBoardBootromVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UtsEponModuleBoardBootromVer_Type.__name__=_H
_UtsEponModuleBoardBootromVer_Object=MibTableColumn
utsEponModuleBoardBootromVer=_UtsEponModuleBoardBootromVer_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,13),_UtsEponModuleBoardBootromVer_Type())
utsEponModuleBoardBootromVer.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardBootromVer.setStatus(_A)
class _UtsEponModuleBoardPassaveVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UtsEponModuleBoardPassaveVer_Type.__name__=_H
_UtsEponModuleBoardPassaveVer_Object=MibTableColumn
utsEponModuleBoardPassaveVer=_UtsEponModuleBoardPassaveVer_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,14),_UtsEponModuleBoardPassaveVer_Type())
utsEponModuleBoardPassaveVer.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardPassaveVer.setStatus(_A)
_UtsEponModuleBoardCurTemp_Type=Integer32
_UtsEponModuleBoardCurTemp_Object=MibTableColumn
utsEponModuleBoardCurTemp=_UtsEponModuleBoardCurTemp_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,15),_UtsEponModuleBoardCurTemp_Type())
utsEponModuleBoardCurTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardCurTemp.setStatus(_A)
class _UtsEponModuleBoardTempUpLimit_Type(Integer32):defaultValue=70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,70))
_UtsEponModuleBoardTempUpLimit_Type.__name__=_C
_UtsEponModuleBoardTempUpLimit_Object=MibTableColumn
utsEponModuleBoardTempUpLimit=_UtsEponModuleBoardTempUpLimit_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,16),_UtsEponModuleBoardTempUpLimit_Type())
utsEponModuleBoardTempUpLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:utsEponModuleBoardTempUpLimit.setStatus(_A)
class _UtsEponModuleBoardTempUpClearLimit_Type(Integer32):defaultValue=65;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,70))
_UtsEponModuleBoardTempUpClearLimit_Type.__name__=_C
_UtsEponModuleBoardTempUpClearLimit_Object=MibTableColumn
utsEponModuleBoardTempUpClearLimit=_UtsEponModuleBoardTempUpClearLimit_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,17),_UtsEponModuleBoardTempUpClearLimit_Type())
utsEponModuleBoardTempUpClearLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:utsEponModuleBoardTempUpClearLimit.setStatus(_A)
_UtsEponModuleBoardLastAdminStateChangetime_Type=TimeTicks
_UtsEponModuleBoardLastAdminStateChangetime_Object=MibTableColumn
utsEponModuleBoardLastAdminStateChangetime=_UtsEponModuleBoardLastAdminStateChangetime_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,18),_UtsEponModuleBoardLastAdminStateChangetime_Type())
utsEponModuleBoardLastAdminStateChangetime.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardLastAdminStateChangetime.setStatus(_A)
_UtsEponModuleBoardLastOperationStateChangetime_Type=TimeTicks
_UtsEponModuleBoardLastOperationStateChangetime_Object=MibTableColumn
utsEponModuleBoardLastOperationStateChangetime=_UtsEponModuleBoardLastOperationStateChangetime_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,19),_UtsEponModuleBoardLastOperationStateChangetime_Type())
utsEponModuleBoardLastOperationStateChangetime.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardLastOperationStateChangetime.setStatus(_A)
class _UtsEponModuleBoardDisableCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('adminlock',1),('lostcurrentstate',2),('serviceunavailable',3)))
_UtsEponModuleBoardDisableCause_Type.__name__=_C
_UtsEponModuleBoardDisableCause_Object=MibTableColumn
utsEponModuleBoardDisableCause=_UtsEponModuleBoardDisableCause_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,20),_UtsEponModuleBoardDisableCause_Type())
utsEponModuleBoardDisableCause.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardDisableCause.setStatus(_A)
class _UtsEponModuleBoardHwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UtsEponModuleBoardHwVer_Type.__name__=_H
_UtsEponModuleBoardHwVer_Object=MibTableColumn
utsEponModuleBoardHwVer=_UtsEponModuleBoardHwVer_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,21),_UtsEponModuleBoardHwVer_Type())
utsEponModuleBoardHwVer.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardHwVer.setStatus(_A)
class _UtsEponModuleBoardCpldVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UtsEponModuleBoardCpldVer_Type.__name__=_H
_UtsEponModuleBoardCpldVer_Object=MibTableColumn
utsEponModuleBoardCpldVer=_UtsEponModuleBoardCpldVer_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,22),_UtsEponModuleBoardCpldVer_Type())
utsEponModuleBoardCpldVer.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardCpldVer.setStatus(_A)
class _UtsEponModuleBoardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UtsEponModuleBoardSerialNumber_Type.__name__=_H
_UtsEponModuleBoardSerialNumber_Object=MibTableColumn
utsEponModuleBoardSerialNumber=_UtsEponModuleBoardSerialNumber_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,23),_UtsEponModuleBoardSerialNumber_Type())
utsEponModuleBoardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardSerialNumber.setStatus(_A)
class _UtsEponModuleBoard2424Information_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UtsEponModuleBoard2424Information_Type.__name__=_H
_UtsEponModuleBoard2424Information_Object=MibTableColumn
utsEponModuleBoard2424Information=_UtsEponModuleBoard2424Information_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,24),_UtsEponModuleBoard2424Information_Type())
utsEponModuleBoard2424Information.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoard2424Information.setStatus(_A)
class _UtsEponModuleBoardHASyncStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notstart',1),('syncing',2),('syncover',3),('syncfail',4)))
_UtsEponModuleBoardHASyncStatus_Type.__name__=_C
_UtsEponModuleBoardHASyncStatus_Object=MibTableColumn
utsEponModuleBoardHASyncStatus=_UtsEponModuleBoardHASyncStatus_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,26),_UtsEponModuleBoardHASyncStatus_Type())
utsEponModuleBoardHASyncStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardHASyncStatus.setStatus(_A)
_UtsEponModuleBoardCpuUtil_Type=Integer32
_UtsEponModuleBoardCpuUtil_Object=MibTableColumn
utsEponModuleBoardCpuUtil=_UtsEponModuleBoardCpuUtil_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,27),_UtsEponModuleBoardCpuUtil_Type())
utsEponModuleBoardCpuUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardCpuUtil.setStatus(_A)
_UtsEponModuleBoardMemUtil_Type=Integer32
_UtsEponModuleBoardMemUtil_Object=MibTableColumn
utsEponModuleBoardMemUtil=_UtsEponModuleBoardMemUtil_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,1,1,28),_UtsEponModuleBoardMemUtil_Type())
utsEponModuleBoardMemUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:utsEponModuleBoardMemUtil.setStatus(_A)
_UtsManagementConfExt_ObjectIdentity=ObjectIdentity
utsManagementConfExt=_UtsManagementConfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4))
_UtsSystemConfGroup_ObjectIdentity=ObjectIdentity
utsSystemConfGroup=_UtsSystemConfGroup_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,1))
class _UtsBBSVlanVPNTPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UtsBBSVlanVPNTPID_Type.__name__=_C
_UtsBBSVlanVPNTPID_Object=MibScalar
utsBBSVlanVPNTPID=_UtsBBSVlanVPNTPID_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,1,1),_UtsBBSVlanVPNTPID_Type())
utsBBSVlanVPNTPID.setMaxAccess(_F)
if mibBuilder.loadTexts:utsBBSVlanVPNTPID.setStatus(_A)
class _UtsBBSVlanVPNTunnel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_UtsBBSVlanVPNTunnel_Type.__name__=_C
_UtsBBSVlanVPNTunnel_Object=MibScalar
utsBBSVlanVPNTunnel=_UtsBBSVlanVPNTunnel_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,1,2),_UtsBBSVlanVPNTunnel_Type())
utsBBSVlanVPNTunnel.setMaxAccess(_F)
if mibBuilder.loadTexts:utsBBSVlanVPNTunnel.setStatus(_A)
class _UtsBBSVlanVPNPRISource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('customertag',1),('llid',2)))
_UtsBBSVlanVPNPRISource_Type.__name__=_C
_UtsBBSVlanVPNPRISource_Object=MibScalar
utsBBSVlanVPNPRISource=_UtsBBSVlanVPNPRISource_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,1,3),_UtsBBSVlanVPNPRISource_Type())
utsBBSVlanVPNPRISource.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSVlanVPNPRISource.setStatus(_A)
class _UtsBBSMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,16368))
_UtsBBSMaxFrameSize_Type.__name__=_C
_UtsBBSMaxFrameSize_Object=MibScalar
utsBBSMaxFrameSize=_UtsBBSMaxFrameSize_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,1,4),_UtsBBSMaxFrameSize_Type())
utsBBSMaxFrameSize.setMaxAccess(_F)
if mibBuilder.loadTexts:utsBBSMaxFrameSize.setStatus(_A)
_UtsFTPConfGroup_ObjectIdentity=ObjectIdentity
utsFTPConfGroup=_UtsFTPConfGroup_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,2))
_UtsFileSystemGroup_ObjectIdentity=ObjectIdentity
utsFileSystemGroup=_UtsFileSystemGroup_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,3))
_UtsChassisConfGroup_ObjectIdentity=ObjectIdentity
utsChassisConfGroup=_UtsChassisConfGroup_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,4))
class _UtsBBSChassisPwrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ac',1),('dc',2)))
_UtsBBSChassisPwrType_Type.__name__=_C
_UtsBBSChassisPwrType_Object=MibScalar
utsBBSChassisPwrType=_UtsBBSChassisPwrType_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,4,1),_UtsBBSChassisPwrType_Type())
utsBBSChassisPwrType.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSChassisPwrType.setStatus(_A)
class _UtsBBSChassisPwrLowSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_UtsBBSChassisPwrLowSlot_Type.__name__=_C
_UtsBBSChassisPwrLowSlot_Object=MibScalar
utsBBSChassisPwrLowSlot=_UtsBBSChassisPwrLowSlot_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,4,2),_UtsBBSChassisPwrLowSlot_Type())
utsBBSChassisPwrLowSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSChassisPwrLowSlot.setStatus(_A)
class _UtsBBSChassisPwrHighSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_UtsBBSChassisPwrHighSlot_Type.__name__=_C
_UtsBBSChassisPwrHighSlot_Object=MibScalar
utsBBSChassisPwrHighSlot=_UtsBBSChassisPwrHighSlot_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,4,3),_UtsBBSChassisPwrHighSlot_Type())
utsBBSChassisPwrHighSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSChassisPwrHighSlot.setStatus(_A)
class _UtsBBSChassisInternalPowerStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_UtsBBSChassisInternalPowerStat_Type.__name__=_C
_UtsBBSChassisInternalPowerStat_Object=MibScalar
utsBBSChassisInternalPowerStat=_UtsBBSChassisInternalPowerStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,4,4),_UtsBBSChassisInternalPowerStat_Type())
utsBBSChassisInternalPowerStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSChassisInternalPowerStat.setStatus(_A)
class _UtsBBSChassisFanTrayStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_UtsBBSChassisFanTrayStat_Type.__name__=_C
_UtsBBSChassisFanTrayStat_Object=MibScalar
utsBBSChassisFanTrayStat=_UtsBBSChassisFanTrayStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,4,5),_UtsBBSChassisFanTrayStat_Type())
utsBBSChassisFanTrayStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSChassisFanTrayStat.setStatus(_A)
class _UtsBBSChassisLeftFanTrayStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_UtsBBSChassisLeftFanTrayStat_Type.__name__=_C
_UtsBBSChassisLeftFanTrayStat_Object=MibScalar
utsBBSChassisLeftFanTrayStat=_UtsBBSChassisLeftFanTrayStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,4,8),_UtsBBSChassisLeftFanTrayStat_Type())
utsBBSChassisLeftFanTrayStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSChassisLeftFanTrayStat.setStatus(_A)
class _UtsBBSChassisMiddleFanTrayStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_UtsBBSChassisMiddleFanTrayStat_Type.__name__=_C
_UtsBBSChassisMiddleFanTrayStat_Object=MibScalar
utsBBSChassisMiddleFanTrayStat=_UtsBBSChassisMiddleFanTrayStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,4,9),_UtsBBSChassisMiddleFanTrayStat_Type())
utsBBSChassisMiddleFanTrayStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSChassisMiddleFanTrayStat.setStatus(_A)
class _UtsBBSChassisRightFanTrayStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_UtsBBSChassisRightFanTrayStat_Type.__name__=_C
_UtsBBSChassisRightFanTrayStat_Object=MibScalar
utsBBSChassisRightFanTrayStat=_UtsBBSChassisRightFanTrayStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,4,10),_UtsBBSChassisRightFanTrayStat_Type())
utsBBSChassisRightFanTrayStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSChassisRightFanTrayStat.setStatus(_A)
_UtsTFTPConfGroup_ObjectIdentity=ObjectIdentity
utsTFTPConfGroup=_UtsTFTPConfGroup_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,5))
_UtsLedMgmtConfExt_ObjectIdentity=ObjectIdentity
utsLedMgmtConfExt=_UtsLedMgmtConfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6))
_UtsLedCSMLedDispGroup_ObjectIdentity=ObjectIdentity
utsLedCSMLedDispGroup=_UtsLedCSMLedDispGroup_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1))
class _UtsBBSLEDCSMAPowerLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_UtsBBSLEDCSMAPowerLedState_Type.__name__=_C
_UtsBBSLEDCSMAPowerLedState_Object=MibScalar
utsBBSLEDCSMAPowerLedState=_UtsBBSLEDCSMAPowerLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,1),_UtsBBSLEDCSMAPowerLedState_Type())
utsBBSLEDCSMAPowerLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMAPowerLedState.setStatus(_A)
class _UtsBBSLEDCSMAActiveLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_UtsBBSLEDCSMAActiveLedState_Type.__name__=_C
_UtsBBSLEDCSMAActiveLedState_Object=MibScalar
utsBBSLEDCSMAActiveLedState=_UtsBBSLEDCSMAActiveLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,2),_UtsBBSLEDCSMAActiveLedState_Type())
utsBBSLEDCSMAActiveLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMAActiveLedState.setStatus(_A)
class _UtsBBSLEDCSMARunLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_G,3)))
_UtsBBSLEDCSMARunLedState_Type.__name__=_C
_UtsBBSLEDCSMARunLedState_Object=MibScalar
utsBBSLEDCSMARunLedState=_UtsBBSLEDCSMARunLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,3),_UtsBBSLEDCSMARunLedState_Type())
utsBBSLEDCSMARunLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMARunLedState.setStatus(_A)
class _UtsBBSLEDCSMACriticalAlarmLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_UtsBBSLEDCSMACriticalAlarmLedState_Type.__name__=_C
_UtsBBSLEDCSMACriticalAlarmLedState_Object=MibScalar
utsBBSLEDCSMACriticalAlarmLedState=_UtsBBSLEDCSMACriticalAlarmLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,4),_UtsBBSLEDCSMACriticalAlarmLedState_Type())
utsBBSLEDCSMACriticalAlarmLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMACriticalAlarmLedState.setStatus(_A)
class _UtsBBSLEDCSMAMajorAlarmLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_UtsBBSLEDCSMAMajorAlarmLedState_Type.__name__=_C
_UtsBBSLEDCSMAMajorAlarmLedState_Object=MibScalar
utsBBSLEDCSMAMajorAlarmLedState=_UtsBBSLEDCSMAMajorAlarmLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,5),_UtsBBSLEDCSMAMajorAlarmLedState_Type())
utsBBSLEDCSMAMajorAlarmLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMAMajorAlarmLedState.setStatus(_A)
class _UtsBBSLEDCSMAMinorAlarmLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_UtsBBSLEDCSMAMinorAlarmLedState_Type.__name__=_C
_UtsBBSLEDCSMAMinorAlarmLedState_Object=MibScalar
utsBBSLEDCSMAMinorAlarmLedState=_UtsBBSLEDCSMAMinorAlarmLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,6),_UtsBBSLEDCSMAMinorAlarmLedState_Type())
utsBBSLEDCSMAMinorAlarmLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMAMinorAlarmLedState.setStatus(_A)
class _UtsBBSLEDCSMAHotSwapLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_G,3)))
_UtsBBSLEDCSMAHotSwapLedState_Type.__name__=_C
_UtsBBSLEDCSMAHotSwapLedState_Object=MibScalar
utsBBSLEDCSMAHotSwapLedState=_UtsBBSLEDCSMAHotSwapLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,7),_UtsBBSLEDCSMAHotSwapLedState_Type())
utsBBSLEDCSMAHotSwapLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMAHotSwapLedState.setStatus(_A)
class _UtsBBSLEDCSMAEmsPortLinkLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_G,3)))
_UtsBBSLEDCSMAEmsPortLinkLedState_Type.__name__=_C
_UtsBBSLEDCSMAEmsPortLinkLedState_Object=MibScalar
utsBBSLEDCSMAEmsPortLinkLedState=_UtsBBSLEDCSMAEmsPortLinkLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,8),_UtsBBSLEDCSMAEmsPortLinkLedState_Type())
utsBBSLEDCSMAEmsPortLinkLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMAEmsPortLinkLedState.setStatus(_A)
class _UtsBBSLEDCSMAEmsPortSpeedLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_UtsBBSLEDCSMAEmsPortSpeedLedState_Type.__name__=_C
_UtsBBSLEDCSMAEmsPortSpeedLedState_Object=MibScalar
utsBBSLEDCSMAEmsPortSpeedLedState=_UtsBBSLEDCSMAEmsPortSpeedLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,9),_UtsBBSLEDCSMAEmsPortSpeedLedState_Type())
utsBBSLEDCSMAEmsPortSpeedLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMAEmsPortSpeedLedState.setStatus(_A)
class _UtsBBSLEDCSMBPowerLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_UtsBBSLEDCSMBPowerLedState_Type.__name__=_C
_UtsBBSLEDCSMBPowerLedState_Object=MibScalar
utsBBSLEDCSMBPowerLedState=_UtsBBSLEDCSMBPowerLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,10),_UtsBBSLEDCSMBPowerLedState_Type())
utsBBSLEDCSMBPowerLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMBPowerLedState.setStatus(_A)
class _UtsBBSLEDCSMBActiveLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_UtsBBSLEDCSMBActiveLedState_Type.__name__=_C
_UtsBBSLEDCSMBActiveLedState_Object=MibScalar
utsBBSLEDCSMBActiveLedState=_UtsBBSLEDCSMBActiveLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,11),_UtsBBSLEDCSMBActiveLedState_Type())
utsBBSLEDCSMBActiveLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMBActiveLedState.setStatus(_A)
class _UtsBBSLEDCSMBRunLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_G,3)))
_UtsBBSLEDCSMBRunLedState_Type.__name__=_C
_UtsBBSLEDCSMBRunLedState_Object=MibScalar
utsBBSLEDCSMBRunLedState=_UtsBBSLEDCSMBRunLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,12),_UtsBBSLEDCSMBRunLedState_Type())
utsBBSLEDCSMBRunLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMBRunLedState.setStatus(_A)
class _UtsBBSLEDCSMBCriticalAlarmLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_UtsBBSLEDCSMBCriticalAlarmLedState_Type.__name__=_C
_UtsBBSLEDCSMBCriticalAlarmLedState_Object=MibScalar
utsBBSLEDCSMBCriticalAlarmLedState=_UtsBBSLEDCSMBCriticalAlarmLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,13),_UtsBBSLEDCSMBCriticalAlarmLedState_Type())
utsBBSLEDCSMBCriticalAlarmLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMBCriticalAlarmLedState.setStatus(_A)
class _UtsBBSLEDCSMBMajorAlarmLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_UtsBBSLEDCSMBMajorAlarmLedState_Type.__name__=_C
_UtsBBSLEDCSMBMajorAlarmLedState_Object=MibScalar
utsBBSLEDCSMBMajorAlarmLedState=_UtsBBSLEDCSMBMajorAlarmLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,14),_UtsBBSLEDCSMBMajorAlarmLedState_Type())
utsBBSLEDCSMBMajorAlarmLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMBMajorAlarmLedState.setStatus(_A)
class _UtsBBSLEDCSMBMinorAlarmLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_UtsBBSLEDCSMBMinorAlarmLedState_Type.__name__=_C
_UtsBBSLEDCSMBMinorAlarmLedState_Object=MibScalar
utsBBSLEDCSMBMinorAlarmLedState=_UtsBBSLEDCSMBMinorAlarmLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,15),_UtsBBSLEDCSMBMinorAlarmLedState_Type())
utsBBSLEDCSMBMinorAlarmLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMBMinorAlarmLedState.setStatus(_A)
class _UtsBBSLEDCSMBHotSwapLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_G,3)))
_UtsBBSLEDCSMBHotSwapLedState_Type.__name__=_C
_UtsBBSLEDCSMBHotSwapLedState_Object=MibScalar
utsBBSLEDCSMBHotSwapLedState=_UtsBBSLEDCSMBHotSwapLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,16),_UtsBBSLEDCSMBHotSwapLedState_Type())
utsBBSLEDCSMBHotSwapLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMBHotSwapLedState.setStatus(_A)
class _UtsBBSLEDCSMBEmsPortLinkLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_G,3)))
_UtsBBSLEDCSMBEmsPortLinkLedState_Type.__name__=_C
_UtsBBSLEDCSMBEmsPortLinkLedState_Object=MibScalar
utsBBSLEDCSMBEmsPortLinkLedState=_UtsBBSLEDCSMBEmsPortLinkLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,17),_UtsBBSLEDCSMBEmsPortLinkLedState_Type())
utsBBSLEDCSMBEmsPortLinkLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMBEmsPortLinkLedState.setStatus(_A)
class _UtsBBSLEDCSMBEmsPortSpeedLedState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_UtsBBSLEDCSMBEmsPortSpeedLedState_Type.__name__=_C
_UtsBBSLEDCSMBEmsPortSpeedLedState_Object=MibScalar
utsBBSLEDCSMBEmsPortSpeedLedState=_UtsBBSLEDCSMBEmsPortSpeedLedState_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,1,18),_UtsBBSLEDCSMBEmsPortSpeedLedState_Type())
utsBBSLEDCSMBEmsPortSpeedLedState.setMaxAccess(_B)
if mibBuilder.loadTexts:utsBBSLEDCSMBEmsPortSpeedLedState.setStatus(_A)
_UtsLedPonSlotLedDispObjs_ObjectIdentity=ObjectIdentity
utsLedPonSlotLedDispObjs=_UtsLedPonSlotLedDispObjs_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2))
_UtsLedPonSlotLedDispTable_Object=MibTable
utsLedPonSlotLedDispTable=_UtsLedPonSlotLedDispTable_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1))
if mibBuilder.loadTexts:utsLedPonSlotLedDispTable.setStatus(_A)
_UtsLedPonSlotLedDispEntry_Object=MibTableRow
utsLedPonSlotLedDispEntry=_UtsLedPonSlotLedDispEntry_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1))
utsLedPonSlotLedDispEntry.setIndexNames((0,_M,_W))
if mibBuilder.loadTexts:utsLedPonSlotLedDispEntry.setStatus(_A)
_UtsLedPonSlotLedDispSlotId_Type=Integer32
_UtsLedPonSlotLedDispSlotId_Object=MibTableColumn
utsLedPonSlotLedDispSlotId=_UtsLedPonSlotLedDispSlotId_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,1),_UtsLedPonSlotLedDispSlotId_Type())
utsLedPonSlotLedDispSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispSlotId.setStatus(_A)
class _UtsLedPonSlotLedDispPowLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_UtsLedPonSlotLedDispPowLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispPowLedStat_Object=MibTableColumn
utsLedPonSlotLedDispPowLedStat=_UtsLedPonSlotLedDispPowLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,2),_UtsLedPonSlotLedDispPowLedStat_Type())
utsLedPonSlotLedDispPowLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispPowLedStat.setStatus(_A)
class _UtsLedPonSlotLedDispRunLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_G,3)))
_UtsLedPonSlotLedDispRunLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispRunLedStat_Object=MibTableColumn
utsLedPonSlotLedDispRunLedStat=_UtsLedPonSlotLedDispRunLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,3),_UtsLedPonSlotLedDispRunLedStat_Type())
utsLedPonSlotLedDispRunLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispRunLedStat.setStatus(_A)
class _UtsLedPonSlotLedDispFaultLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_UtsLedPonSlotLedDispFaultLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispFaultLedStat_Object=MibTableColumn
utsLedPonSlotLedDispFaultLedStat=_UtsLedPonSlotLedDispFaultLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,4),_UtsLedPonSlotLedDispFaultLedStat_Type())
utsLedPonSlotLedDispFaultLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispFaultLedStat.setStatus(_A)
class _UtsLedPonSlotLedDispSwapLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_G,3)))
_UtsLedPonSlotLedDispSwapLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispSwapLedStat_Object=MibTableColumn
utsLedPonSlotLedDispSwapLedStat=_UtsLedPonSlotLedDispSwapLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,5),_UtsLedPonSlotLedDispSwapLedStat_Type())
utsLedPonSlotLedDispSwapLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispSwapLedStat.setStatus(_A)
class _UtsLedPonSlotLedDispPonPort1OprLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_G,3)))
_UtsLedPonSlotLedDispPonPort1OprLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispPonPort1OprLedStat_Object=MibTableColumn
utsLedPonSlotLedDispPonPort1OprLedStat=_UtsLedPonSlotLedDispPonPort1OprLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,6),_UtsLedPonSlotLedDispPonPort1OprLedStat_Type())
utsLedPonSlotLedDispPonPort1OprLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispPonPort1OprLedStat.setStatus(_A)
class _UtsLedPonSlotLedDispPonPort1FaultLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_UtsLedPonSlotLedDispPonPort1FaultLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispPonPort1FaultLedStat_Object=MibTableColumn
utsLedPonSlotLedDispPonPort1FaultLedStat=_UtsLedPonSlotLedDispPonPort1FaultLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,7),_UtsLedPonSlotLedDispPonPort1FaultLedStat_Type())
utsLedPonSlotLedDispPonPort1FaultLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispPonPort1FaultLedStat.setStatus(_A)
class _UtsLedPonSlotLedDispPonPort2OprLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_G,3)))
_UtsLedPonSlotLedDispPonPort2OprLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispPonPort2OprLedStat_Object=MibTableColumn
utsLedPonSlotLedDispPonPort2OprLedStat=_UtsLedPonSlotLedDispPonPort2OprLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,8),_UtsLedPonSlotLedDispPonPort2OprLedStat_Type())
utsLedPonSlotLedDispPonPort2OprLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispPonPort2OprLedStat.setStatus(_A)
class _UtsLedPonSlotLedDispPonPort2FaultLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_UtsLedPonSlotLedDispPonPort2FaultLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispPonPort2FaultLedStat_Object=MibTableColumn
utsLedPonSlotLedDispPonPort2FaultLedStat=_UtsLedPonSlotLedDispPonPort2FaultLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,9),_UtsLedPonSlotLedDispPonPort2FaultLedStat_Type())
utsLedPonSlotLedDispPonPort2FaultLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispPonPort2FaultLedStat.setStatus(_A)
class _UtsLedPonSlotLedDispPonPort3OprLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_G,3)))
_UtsLedPonSlotLedDispPonPort3OprLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispPonPort3OprLedStat_Object=MibTableColumn
utsLedPonSlotLedDispPonPort3OprLedStat=_UtsLedPonSlotLedDispPonPort3OprLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,10),_UtsLedPonSlotLedDispPonPort3OprLedStat_Type())
utsLedPonSlotLedDispPonPort3OprLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispPonPort3OprLedStat.setStatus(_A)
class _UtsLedPonSlotLedDispPonPort3FaultLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_UtsLedPonSlotLedDispPonPort3FaultLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispPonPort3FaultLedStat_Object=MibTableColumn
utsLedPonSlotLedDispPonPort3FaultLedStat=_UtsLedPonSlotLedDispPonPort3FaultLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,11),_UtsLedPonSlotLedDispPonPort3FaultLedStat_Type())
utsLedPonSlotLedDispPonPort3FaultLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispPonPort3FaultLedStat.setStatus(_A)
class _UtsLedPonSlotLedDispPonPort4OprLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_G,3)))
_UtsLedPonSlotLedDispPonPort4OprLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispPonPort4OprLedStat_Object=MibTableColumn
utsLedPonSlotLedDispPonPort4OprLedStat=_UtsLedPonSlotLedDispPonPort4OprLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,12),_UtsLedPonSlotLedDispPonPort4OprLedStat_Type())
utsLedPonSlotLedDispPonPort4OprLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispPonPort4OprLedStat.setStatus(_A)
class _UtsLedPonSlotLedDispPonPort4FaultLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_UtsLedPonSlotLedDispPonPort4FaultLedStat_Type.__name__=_C
_UtsLedPonSlotLedDispPonPort4FaultLedStat_Object=MibTableColumn
utsLedPonSlotLedDispPonPort4FaultLedStat=_UtsLedPonSlotLedDispPonPort4FaultLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,2,1,1,13),_UtsLedPonSlotLedDispPonPort4FaultLedStat_Type())
utsLedPonSlotLedDispPonPort4FaultLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedPonSlotLedDispPonPort4FaultLedStat.setStatus(_A)
_UtsLedGEPortSlotLedDispObjs_ObjectIdentity=ObjectIdentity
utsLedGEPortSlotLedDispObjs=_UtsLedGEPortSlotLedDispObjs_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3))
_UtsLedGEPortSlotLedDispTable_Object=MibTable
utsLedGEPortSlotLedDispTable=_UtsLedGEPortSlotLedDispTable_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3,1))
if mibBuilder.loadTexts:utsLedGEPortSlotLedDispTable.setStatus(_A)
_UtsLedGEPortSlotLedDispEntry_Object=MibTableRow
utsLedGEPortSlotLedDispEntry=_UtsLedGEPortSlotLedDispEntry_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3,1,1))
utsLedGEPortSlotLedDispEntry.setIndexNames((0,_M,_X))
if mibBuilder.loadTexts:utsLedGEPortSlotLedDispEntry.setStatus(_A)
_UtsLedGEPortSlotLedDispSlotId_Type=Integer32
_UtsLedGEPortSlotLedDispSlotId_Object=MibTableColumn
utsLedGEPortSlotLedDispSlotId=_UtsLedGEPortSlotLedDispSlotId_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3,1,1,1),_UtsLedGEPortSlotLedDispSlotId_Type())
utsLedGEPortSlotLedDispSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedGEPortSlotLedDispSlotId.setStatus(_A)
class _UtsLedGEPortSlotLedDispPowLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_UtsLedGEPortSlotLedDispPowLedStat_Type.__name__=_C
_UtsLedGEPortSlotLedDispPowLedStat_Object=MibTableColumn
utsLedGEPortSlotLedDispPowLedStat=_UtsLedGEPortSlotLedDispPowLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3,1,1,2),_UtsLedGEPortSlotLedDispPowLedStat_Type())
utsLedGEPortSlotLedDispPowLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedGEPortSlotLedDispPowLedStat.setStatus(_A)
class _UtsLedGEPortSlotLedDispRunLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_G,3)))
_UtsLedGEPortSlotLedDispRunLedStat_Type.__name__=_C
_UtsLedGEPortSlotLedDispRunLedStat_Object=MibTableColumn
utsLedGEPortSlotLedDispRunLedStat=_UtsLedGEPortSlotLedDispRunLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3,1,1,3),_UtsLedGEPortSlotLedDispRunLedStat_Type())
utsLedGEPortSlotLedDispRunLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedGEPortSlotLedDispRunLedStat.setStatus(_A)
class _UtsLedGEPortSlotLedDispFaultLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_UtsLedGEPortSlotLedDispFaultLedStat_Type.__name__=_C
_UtsLedGEPortSlotLedDispFaultLedStat_Object=MibTableColumn
utsLedGEPortSlotLedDispFaultLedStat=_UtsLedGEPortSlotLedDispFaultLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3,1,1,4),_UtsLedGEPortSlotLedDispFaultLedStat_Type())
utsLedGEPortSlotLedDispFaultLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedGEPortSlotLedDispFaultLedStat.setStatus(_A)
class _UtsLedGEPortSlotLedDispSwapLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_L,2),(_G,3)))
_UtsLedGEPortSlotLedDispSwapLedStat_Type.__name__=_C
_UtsLedGEPortSlotLedDispSwapLedStat_Object=MibTableColumn
utsLedGEPortSlotLedDispSwapLedStat=_UtsLedGEPortSlotLedDispSwapLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3,1,1,5),_UtsLedGEPortSlotLedDispSwapLedStat_Type())
utsLedGEPortSlotLedDispSwapLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedGEPortSlotLedDispSwapLedStat.setStatus(_A)
class _UtsLedGEPortSlotLedDispPort1LinkLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_UtsLedGEPortSlotLedDispPort1LinkLedStat_Type.__name__=_C
_UtsLedGEPortSlotLedDispPort1LinkLedStat_Object=MibTableColumn
utsLedGEPortSlotLedDispPort1LinkLedStat=_UtsLedGEPortSlotLedDispPort1LinkLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3,1,1,6),_UtsLedGEPortSlotLedDispPort1LinkLedStat_Type())
utsLedGEPortSlotLedDispPort1LinkLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedGEPortSlotLedDispPort1LinkLedStat.setStatus(_A)
class _UtsLedGEPortSlotLedDispPort2LinkLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_UtsLedGEPortSlotLedDispPort2LinkLedStat_Type.__name__=_C
_UtsLedGEPortSlotLedDispPort2LinkLedStat_Object=MibTableColumn
utsLedGEPortSlotLedDispPort2LinkLedStat=_UtsLedGEPortSlotLedDispPort2LinkLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3,1,1,8),_UtsLedGEPortSlotLedDispPort2LinkLedStat_Type())
utsLedGEPortSlotLedDispPort2LinkLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedGEPortSlotLedDispPort2LinkLedStat.setStatus(_A)
class _UtsLedGEPortSlotLedDispPort3LinkLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_UtsLedGEPortSlotLedDispPort3LinkLedStat_Type.__name__=_C
_UtsLedGEPortSlotLedDispPort3LinkLedStat_Object=MibTableColumn
utsLedGEPortSlotLedDispPort3LinkLedStat=_UtsLedGEPortSlotLedDispPort3LinkLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3,1,1,10),_UtsLedGEPortSlotLedDispPort3LinkLedStat_Type())
utsLedGEPortSlotLedDispPort3LinkLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedGEPortSlotLedDispPort3LinkLedStat.setStatus(_A)
class _UtsLedGEPortSlotLedDispPort4LinkLedStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_UtsLedGEPortSlotLedDispPort4LinkLedStat_Type.__name__=_C
_UtsLedGEPortSlotLedDispPort4LinkLedStat_Object=MibTableColumn
utsLedGEPortSlotLedDispPort4LinkLedStat=_UtsLedGEPortSlotLedDispPort4LinkLedStat_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,6,3,1,1,12),_UtsLedGEPortSlotLedDispPort4LinkLedStat_Type())
utsLedGEPortSlotLedDispPort4LinkLedStat.setMaxAccess(_B)
if mibBuilder.loadTexts:utsLedGEPortSlotLedDispPort4LinkLedStat.setStatus(_A)
_UtsHAMgmtConfExt_ObjectIdentity=ObjectIdentity
utsHAMgmtConfExt=_UtsHAMgmtConfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,8))
_UtsHAMgmtConfObjs_ObjectIdentity=ObjectIdentity
utsHAMgmtConfObjs=_UtsHAMgmtConfObjs_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,8,1))
_UtsHAMgmtConfGroup_ObjectIdentity=ObjectIdentity
utsHAMgmtConfGroup=_UtsHAMgmtConfGroup_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,8,1,1))
class _UtsHAMgmtManualSwitchOver_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('switch',1))
_UtsHAMgmtManualSwitchOver_Type.__name__=_C
_UtsHAMgmtManualSwitchOver_Object=MibScalar
utsHAMgmtManualSwitchOver=_UtsHAMgmtManualSwitchOver_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,8,1,1,1),_UtsHAMgmtManualSwitchOver_Type())
utsHAMgmtManualSwitchOver.setMaxAccess(_F)
if mibBuilder.loadTexts:utsHAMgmtManualSwitchOver.setStatus(_A)
class _UtsHAMgmtRebootWholeSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reboot',1))
_UtsHAMgmtRebootWholeSystem_Type.__name__=_C
_UtsHAMgmtRebootWholeSystem_Object=MibScalar
utsHAMgmtRebootWholeSystem=_UtsHAMgmtRebootWholeSystem_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,8,1,1,2),_UtsHAMgmtRebootWholeSystem_Type())
utsHAMgmtRebootWholeSystem.setMaxAccess(_F)
if mibBuilder.loadTexts:utsHAMgmtRebootWholeSystem.setStatus(_A)
class _UtsHAMgmtMasterBoardBootFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UtsHAMgmtMasterBoardBootFileName_Type.__name__=_H
_UtsHAMgmtMasterBoardBootFileName_Object=MibScalar
utsHAMgmtMasterBoardBootFileName=_UtsHAMgmtMasterBoardBootFileName_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,8,1,1,3),_UtsHAMgmtMasterBoardBootFileName_Type())
utsHAMgmtMasterBoardBootFileName.setMaxAccess(_F)
if mibBuilder.loadTexts:utsHAMgmtMasterBoardBootFileName.setStatus(_A)
class _UtsHAMgmtSlaveBoardBootFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_UtsHAMgmtSlaveBoardBootFileName_Type.__name__=_H
_UtsHAMgmtSlaveBoardBootFileName_Object=MibScalar
utsHAMgmtSlaveBoardBootFileName=_UtsHAMgmtSlaveBoardBootFileName_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,1,4,8,1,1,4),_UtsHAMgmtSlaveBoardBootFileName_Type())
utsHAMgmtSlaveBoardBootFileName.setMaxAccess(_F)
if mibBuilder.loadTexts:utsHAMgmtSlaveBoardBootFileName.setStatus(_A)
_EponOamInitAlm_ObjectIdentity=ObjectIdentity
eponOamInitAlm=_EponOamInitAlm_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,1,2))
_UtsEthIfConfExt_ObjectIdentity=ObjectIdentity
utsEthIfConfExt=_UtsEthIfConfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,2))
_UtsEthIfExtObjects_ObjectIdentity=ObjectIdentity
utsEthIfExtObjects=_UtsEthIfExtObjects_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1))
_UtsLayer2ConfExt_ObjectIdentity=ObjectIdentity
utsLayer2ConfExt=_UtsLayer2ConfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1,5))
_UtsMonitorSessionObjects_ObjectIdentity=ObjectIdentity
utsMonitorSessionObjects=_UtsMonitorSessionObjects_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1,5,3))
_UtsMonitorSessionControlTable_Object=MibTable
utsMonitorSessionControlTable=_UtsMonitorSessionControlTable_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1,5,3,1))
if mibBuilder.loadTexts:utsMonitorSessionControlTable.setStatus(_A)
_UtsMonitorSessionControlEntry_Object=MibTableRow
utsMonitorSessionControlEntry=_UtsMonitorSessionControlEntry_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1,5,3,1,1))
utsMonitorSessionControlEntry.setIndexNames((0,_M,_Y))
if mibBuilder.loadTexts:utsMonitorSessionControlEntry.setStatus(_A)
class _UtsMonitorSessionID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_UtsMonitorSessionID_Type.__name__=_C
_UtsMonitorSessionID_Object=MibTableColumn
utsMonitorSessionID=_UtsMonitorSessionID_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1,5,3,1,1,1),_UtsMonitorSessionID_Type())
utsMonitorSessionID.setMaxAccess(_Z)
if mibBuilder.loadTexts:utsMonitorSessionID.setStatus(_A)
_UtsMonitorSessionModule_Type=Integer32
_UtsMonitorSessionModule_Object=MibTableColumn
utsMonitorSessionModule=_UtsMonitorSessionModule_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1,5,3,1,1,2),_UtsMonitorSessionModule_Type())
utsMonitorSessionModule.setMaxAccess(_F)
if mibBuilder.loadTexts:utsMonitorSessionModule.setStatus(_A)
_UtsMonitorSessionPort_Type=Integer32
_UtsMonitorSessionPort_Object=MibTableColumn
utsMonitorSessionPort=_UtsMonitorSessionPort_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1,5,3,1,1,3),_UtsMonitorSessionPort_Type())
utsMonitorSessionPort.setMaxAccess(_F)
if mibBuilder.loadTexts:utsMonitorSessionPort.setStatus(_A)
_UtsMonitorSessionIngressPortBitLists_Type=OctetString
_UtsMonitorSessionIngressPortBitLists_Object=MibTableColumn
utsMonitorSessionIngressPortBitLists=_UtsMonitorSessionIngressPortBitLists_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1,5,3,1,1,4),_UtsMonitorSessionIngressPortBitLists_Type())
utsMonitorSessionIngressPortBitLists.setMaxAccess(_F)
if mibBuilder.loadTexts:utsMonitorSessionIngressPortBitLists.setStatus(_A)
_UtsMonitorSessionEngressPortBitLists_Type=OctetString
_UtsMonitorSessionEngressPortBitLists_Object=MibTableColumn
utsMonitorSessionEngressPortBitLists=_UtsMonitorSessionEngressPortBitLists_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1,5,3,1,1,5),_UtsMonitorSessionEngressPortBitLists_Type())
utsMonitorSessionEngressPortBitLists.setMaxAccess(_F)
if mibBuilder.loadTexts:utsMonitorSessionEngressPortBitLists.setStatus(_A)
class _UtsMonitorSessionActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_UtsMonitorSessionActive_Type.__name__=_C
_UtsMonitorSessionActive_Object=MibTableColumn
utsMonitorSessionActive=_UtsMonitorSessionActive_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1,5,3,1,1,6),_UtsMonitorSessionActive_Type())
utsMonitorSessionActive.setMaxAccess(_F)
if mibBuilder.loadTexts:utsMonitorSessionActive.setStatus(_A)
_UtsMonitorSessionRowStatus_Type=RowStatus
_UtsMonitorSessionRowStatus_Object=MibTableColumn
utsMonitorSessionRowStatus=_UtsMonitorSessionRowStatus_Object((1,3,6,1,4,1,1949,1,3,10,200,6,2,2,1,5,3,1,1,7),_UtsMonitorSessionRowStatus_Type())
utsMonitorSessionRowStatus.setMaxAccess(_Z)
if mibBuilder.loadTexts:utsMonitorSessionRowStatus.setStatus(_A)
_UtsEfmPonConfExt_ObjectIdentity=ObjectIdentity
utsEfmPonConfExt=_UtsEfmPonConfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,3))
_UtsServiceConfExt_ObjectIdentity=ObjectIdentity
utsServiceConfExt=_UtsServiceConfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,4))
_UtsAclExt_ObjectIdentity=ObjectIdentity
utsAclExt=_UtsAclExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,2,4,2))
mibBuilder.exportSymbols(_M,**{'UtsSyslogServerityLevelType':UtsSyslogServerityLevelType,'UtsConfStationIdType':UtsConfStationIdType,'UtsConfStatusType':UtsConfStatusType,'utsGeponBBS4000Configuration':utsGeponBBS4000Configuration,'utsSystemConfExt':utsSystemConfExt,'utsSystemExtObjects':utsSystemExtObjects,'utsEponModuleBoardTable':utsEponModuleBoardTable,'utsEponModuleBoardEntry':utsEponModuleBoardEntry,_Q:utsEponModuleBoardPhyId,'utsEponModuleBoardType':utsEponModuleBoardType,'utsEponModulePhyPresenceStat':utsEponModulePhyPresenceStat,'utsEponModuleAdminState':utsEponModuleAdminState,'utsEponModuleOperationState':utsEponModuleOperationState,'utsEponModuleRedundancyState':utsEponModuleRedundancyState,'utsEponModulePhyicalUptime':utsEponModulePhyicalUptime,'utsEponOpStateUptime':utsEponOpStateUptime,'utsEponModuleCSMSwitchtime':utsEponModuleCSMSwitchtime,'utsEponModuleBoardSwVer':utsEponModuleBoardSwVer,'utsEponModuleBoardBootromVer':utsEponModuleBoardBootromVer,'utsEponModuleBoardPassaveVer':utsEponModuleBoardPassaveVer,'utsEponModuleBoardCurTemp':utsEponModuleBoardCurTemp,'utsEponModuleBoardTempUpLimit':utsEponModuleBoardTempUpLimit,'utsEponModuleBoardTempUpClearLimit':utsEponModuleBoardTempUpClearLimit,'utsEponModuleBoardLastAdminStateChangetime':utsEponModuleBoardLastAdminStateChangetime,'utsEponModuleBoardLastOperationStateChangetime':utsEponModuleBoardLastOperationStateChangetime,'utsEponModuleBoardDisableCause':utsEponModuleBoardDisableCause,'utsEponModuleBoardHwVer':utsEponModuleBoardHwVer,'utsEponModuleBoardCpldVer':utsEponModuleBoardCpldVer,'utsEponModuleBoardSerialNumber':utsEponModuleBoardSerialNumber,'utsEponModuleBoard2424Information':utsEponModuleBoard2424Information,'utsEponModuleBoardHASyncStatus':utsEponModuleBoardHASyncStatus,'utsEponModuleBoardCpuUtil':utsEponModuleBoardCpuUtil,'utsEponModuleBoardMemUtil':utsEponModuleBoardMemUtil,'utsManagementConfExt':utsManagementConfExt,'utsSystemConfGroup':utsSystemConfGroup,'utsBBSVlanVPNTPID':utsBBSVlanVPNTPID,'utsBBSVlanVPNTunnel':utsBBSVlanVPNTunnel,'utsBBSVlanVPNPRISource':utsBBSVlanVPNPRISource,'utsBBSMaxFrameSize':utsBBSMaxFrameSize,'utsFTPConfGroup':utsFTPConfGroup,'utsFileSystemGroup':utsFileSystemGroup,'utsChassisConfGroup':utsChassisConfGroup,'utsBBSChassisPwrType':utsBBSChassisPwrType,'utsBBSChassisPwrLowSlot':utsBBSChassisPwrLowSlot,'utsBBSChassisPwrHighSlot':utsBBSChassisPwrHighSlot,'utsBBSChassisInternalPowerStat':utsBBSChassisInternalPowerStat,'utsBBSChassisFanTrayStat':utsBBSChassisFanTrayStat,'utsBBSChassisLeftFanTrayStat':utsBBSChassisLeftFanTrayStat,'utsBBSChassisMiddleFanTrayStat':utsBBSChassisMiddleFanTrayStat,'utsBBSChassisRightFanTrayStat':utsBBSChassisRightFanTrayStat,'utsTFTPConfGroup':utsTFTPConfGroup,'utsLedMgmtConfExt':utsLedMgmtConfExt,'utsLedCSMLedDispGroup':utsLedCSMLedDispGroup,'utsBBSLEDCSMAPowerLedState':utsBBSLEDCSMAPowerLedState,'utsBBSLEDCSMAActiveLedState':utsBBSLEDCSMAActiveLedState,'utsBBSLEDCSMARunLedState':utsBBSLEDCSMARunLedState,'utsBBSLEDCSMACriticalAlarmLedState':utsBBSLEDCSMACriticalAlarmLedState,'utsBBSLEDCSMAMajorAlarmLedState':utsBBSLEDCSMAMajorAlarmLedState,'utsBBSLEDCSMAMinorAlarmLedState':utsBBSLEDCSMAMinorAlarmLedState,'utsBBSLEDCSMAHotSwapLedState':utsBBSLEDCSMAHotSwapLedState,'utsBBSLEDCSMAEmsPortLinkLedState':utsBBSLEDCSMAEmsPortLinkLedState,'utsBBSLEDCSMAEmsPortSpeedLedState':utsBBSLEDCSMAEmsPortSpeedLedState,'utsBBSLEDCSMBPowerLedState':utsBBSLEDCSMBPowerLedState,'utsBBSLEDCSMBActiveLedState':utsBBSLEDCSMBActiveLedState,'utsBBSLEDCSMBRunLedState':utsBBSLEDCSMBRunLedState,'utsBBSLEDCSMBCriticalAlarmLedState':utsBBSLEDCSMBCriticalAlarmLedState,'utsBBSLEDCSMBMajorAlarmLedState':utsBBSLEDCSMBMajorAlarmLedState,'utsBBSLEDCSMBMinorAlarmLedState':utsBBSLEDCSMBMinorAlarmLedState,'utsBBSLEDCSMBHotSwapLedState':utsBBSLEDCSMBHotSwapLedState,'utsBBSLEDCSMBEmsPortLinkLedState':utsBBSLEDCSMBEmsPortLinkLedState,'utsBBSLEDCSMBEmsPortSpeedLedState':utsBBSLEDCSMBEmsPortSpeedLedState,'utsLedPonSlotLedDispObjs':utsLedPonSlotLedDispObjs,'utsLedPonSlotLedDispTable':utsLedPonSlotLedDispTable,'utsLedPonSlotLedDispEntry':utsLedPonSlotLedDispEntry,_W:utsLedPonSlotLedDispSlotId,'utsLedPonSlotLedDispPowLedStat':utsLedPonSlotLedDispPowLedStat,'utsLedPonSlotLedDispRunLedStat':utsLedPonSlotLedDispRunLedStat,'utsLedPonSlotLedDispFaultLedStat':utsLedPonSlotLedDispFaultLedStat,'utsLedPonSlotLedDispSwapLedStat':utsLedPonSlotLedDispSwapLedStat,'utsLedPonSlotLedDispPonPort1OprLedStat':utsLedPonSlotLedDispPonPort1OprLedStat,'utsLedPonSlotLedDispPonPort1FaultLedStat':utsLedPonSlotLedDispPonPort1FaultLedStat,'utsLedPonSlotLedDispPonPort2OprLedStat':utsLedPonSlotLedDispPonPort2OprLedStat,'utsLedPonSlotLedDispPonPort2FaultLedStat':utsLedPonSlotLedDispPonPort2FaultLedStat,'utsLedPonSlotLedDispPonPort3OprLedStat':utsLedPonSlotLedDispPonPort3OprLedStat,'utsLedPonSlotLedDispPonPort3FaultLedStat':utsLedPonSlotLedDispPonPort3FaultLedStat,'utsLedPonSlotLedDispPonPort4OprLedStat':utsLedPonSlotLedDispPonPort4OprLedStat,'utsLedPonSlotLedDispPonPort4FaultLedStat':utsLedPonSlotLedDispPonPort4FaultLedStat,'utsLedGEPortSlotLedDispObjs':utsLedGEPortSlotLedDispObjs,'utsLedGEPortSlotLedDispTable':utsLedGEPortSlotLedDispTable,'utsLedGEPortSlotLedDispEntry':utsLedGEPortSlotLedDispEntry,_X:utsLedGEPortSlotLedDispSlotId,'utsLedGEPortSlotLedDispPowLedStat':utsLedGEPortSlotLedDispPowLedStat,'utsLedGEPortSlotLedDispRunLedStat':utsLedGEPortSlotLedDispRunLedStat,'utsLedGEPortSlotLedDispFaultLedStat':utsLedGEPortSlotLedDispFaultLedStat,'utsLedGEPortSlotLedDispSwapLedStat':utsLedGEPortSlotLedDispSwapLedStat,'utsLedGEPortSlotLedDispPort1LinkLedStat':utsLedGEPortSlotLedDispPort1LinkLedStat,'utsLedGEPortSlotLedDispPort2LinkLedStat':utsLedGEPortSlotLedDispPort2LinkLedStat,'utsLedGEPortSlotLedDispPort3LinkLedStat':utsLedGEPortSlotLedDispPort3LinkLedStat,'utsLedGEPortSlotLedDispPort4LinkLedStat':utsLedGEPortSlotLedDispPort4LinkLedStat,'utsHAMgmtConfExt':utsHAMgmtConfExt,'utsHAMgmtConfObjs':utsHAMgmtConfObjs,'utsHAMgmtConfGroup':utsHAMgmtConfGroup,'utsHAMgmtManualSwitchOver':utsHAMgmtManualSwitchOver,'utsHAMgmtRebootWholeSystem':utsHAMgmtRebootWholeSystem,'utsHAMgmtMasterBoardBootFileName':utsHAMgmtMasterBoardBootFileName,'utsHAMgmtSlaveBoardBootFileName':utsHAMgmtSlaveBoardBootFileName,'eponOamInitAlm':eponOamInitAlm,'utsEthIfConfExt':utsEthIfConfExt,'utsEthIfExtObjects':utsEthIfExtObjects,'utsLayer2ConfExt':utsLayer2ConfExt,'utsMonitorSessionObjects':utsMonitorSessionObjects,'utsMonitorSessionControlTable':utsMonitorSessionControlTable,'utsMonitorSessionControlEntry':utsMonitorSessionControlEntry,_Y:utsMonitorSessionID,'utsMonitorSessionModule':utsMonitorSessionModule,'utsMonitorSessionPort':utsMonitorSessionPort,'utsMonitorSessionIngressPortBitLists':utsMonitorSessionIngressPortBitLists,'utsMonitorSessionEngressPortBitLists':utsMonitorSessionEngressPortBitLists,'utsMonitorSessionActive':utsMonitorSessionActive,'utsMonitorSessionRowStatus':utsMonitorSessionRowStatus,'utsEfmPonConfExt':utsEfmPonConfExt,'utsServiceConfExt':utsServiceConfExt,'utsAclExt':utsAclExt})