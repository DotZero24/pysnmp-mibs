_A2='apsChanGeneral'
_A1='apsStatusGeneral'
_A0='apsConfigGeneral'
_z='apsEventFEPLF'
_y='apsEventPSBF'
_x='apsEventChannelMismatch'
_w='apsEventModeMismatch'
_v='apsEventSwitchover'
_u='apsMapChanNumber'
_t='apsMapGroupName'
_s='apsChanLTEs'
_r='apsConfigGroups'
_q='apsChanConfigPriority'
_p='apsChanStatusSwitchoverSeconds'
_o='apsChanStatusLastSwitchover'
_n='apsChanStatusSignalFailures'
_m='apsChanStatusSignalDegrades'
_l='apsChanConfigRowStatus'
_k='apsChanConfigIfIndex'
_j='apsStatusSwitchedChannel'
_i='apsStatusK1K2Trans'
_h='apsStatusK1K2Rcv'
_g='apsCommandControl'
_f='apsConfigWaitToRestore'
_e='apsConfigRowStatus'
_d='apsConfigCreationTime'
_c='apsConfigSfBerThreshold'
_b='apsConfigSdBerThreshold'
_a='apsConfigExtraTraffic'
_Z='apsConfigDirection'
_Y='apsConfigRevert'
_X='apsConfigMode'
_W='read-write'
_V='apsMapIfIndex'
_U='outOfService'
_T='inService'
_S='apsChanStatusSwitchovers'
_R='apsChanStatusCurrent'
_Q='apsStatusFEPLFs'
_P='apsStatusPSBFs'
_O='apsStatusChannelMismatches'
_N='apsStatusModeMismatches'
_M='apsCommandSwitch'
_L='apsConfigName'
_K='Bits'
_J='apsChanConfigNumber'
_I='apsChanConfigGroupName'
_H='not-accessible'
_G='SnmpAdminString'
_F='apsStatusCurrent'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='APS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
ietfDrafts,=mibBuilder.importSymbols('Zhone','ietfDrafts')
apsMIB=ModuleIdentity((1,3,6,1,4,1,5504,10,1,1))
if mibBuilder.loadTexts:apsMIB.setRevisions(('2001-05-24 23:00',))
class ApsK1K2(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class ApsSwitchCommand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noCmd',1),('clear',2),('lockoutOfProtection',3),('forcedSwitchWorkToProtect',4),('forcedSwitchProtectToWork',5),('manualSwitchWorkToProtect',6),('manualSwitchProtectToWork',7),('exercise',8)))
class ApsControlCommand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noCmd',1),('lockoutWorkingChannel',2),('clearLockoutWorkingChannel',3)))
_ApsMIBObjects_ObjectIdentity=ObjectIdentity
apsMIBObjects=_ApsMIBObjects_ObjectIdentity((1,3,6,1,4,1,5504,10,1,1,1))
_ApsConfig_ObjectIdentity=ObjectIdentity
apsConfig=_ApsConfig_ObjectIdentity((1,3,6,1,4,1,5504,10,1,1,1,1))
_ApsConfigGroups_Type=Gauge32
_ApsConfigGroups_Object=MibScalar
apsConfigGroups=_ApsConfigGroups_Object((1,3,6,1,4,1,5504,10,1,1,1,1,1),_ApsConfigGroups_Type())
apsConfigGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigGroups.setStatus(_A)
_ApsConfigTable_Object=MibTable
apsConfigTable=_ApsConfigTable_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2))
if mibBuilder.loadTexts:apsConfigTable.setStatus(_A)
_ApsConfigEntry_Object=MibTableRow
apsConfigEntry=_ApsConfigEntry_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1))
apsConfigEntry.setIndexNames((1,_B,_L))
if mibBuilder.loadTexts:apsConfigEntry.setStatus(_A)
class _ApsConfigName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApsConfigName_Type.__name__=_G
_ApsConfigName_Object=MibTableColumn
apsConfigName=_ApsConfigName_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1,1),_ApsConfigName_Type())
apsConfigName.setMaxAccess(_H)
if mibBuilder.loadTexts:apsConfigName.setStatus(_A)
_ApsConfigRowStatus_Type=RowStatus
_ApsConfigRowStatus_Object=MibTableColumn
apsConfigRowStatus=_ApsConfigRowStatus_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1,2),_ApsConfigRowStatus_Type())
apsConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:apsConfigRowStatus.setStatus(_A)
class _ApsConfigMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('onePlusOne',1),('oneToN',2),('onePlusOneCompatible',3),('onePlusOneOptimized',4)))
_ApsConfigMode_Type.__name__=_D
_ApsConfigMode_Object=MibTableColumn
apsConfigMode=_ApsConfigMode_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1,3),_ApsConfigMode_Type())
apsConfigMode.setMaxAccess(_E)
if mibBuilder.loadTexts:apsConfigMode.setStatus(_A)
class _ApsConfigRevert_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonrevertive',1),('revertive',2)))
_ApsConfigRevert_Type.__name__=_D
_ApsConfigRevert_Object=MibTableColumn
apsConfigRevert=_ApsConfigRevert_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1,4),_ApsConfigRevert_Type())
apsConfigRevert.setMaxAccess(_E)
if mibBuilder.loadTexts:apsConfigRevert.setStatus(_A)
class _ApsConfigDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
_ApsConfigDirection_Type.__name__=_D
_ApsConfigDirection_Object=MibTableColumn
apsConfigDirection=_ApsConfigDirection_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1,5),_ApsConfigDirection_Type())
apsConfigDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:apsConfigDirection.setStatus(_A)
class _ApsConfigExtraTraffic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ApsConfigExtraTraffic_Type.__name__=_D
_ApsConfigExtraTraffic_Object=MibTableColumn
apsConfigExtraTraffic=_ApsConfigExtraTraffic_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1,6),_ApsConfigExtraTraffic_Type())
apsConfigExtraTraffic.setMaxAccess(_E)
if mibBuilder.loadTexts:apsConfigExtraTraffic.setStatus(_A)
class _ApsConfigSdBerThreshold_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,9))
_ApsConfigSdBerThreshold_Type.__name__=_D
_ApsConfigSdBerThreshold_Object=MibTableColumn
apsConfigSdBerThreshold=_ApsConfigSdBerThreshold_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1,7),_ApsConfigSdBerThreshold_Type())
apsConfigSdBerThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:apsConfigSdBerThreshold.setStatus(_A)
class _ApsConfigSfBerThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,5))
_ApsConfigSfBerThreshold_Type.__name__=_D
_ApsConfigSfBerThreshold_Object=MibTableColumn
apsConfigSfBerThreshold=_ApsConfigSfBerThreshold_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1,8),_ApsConfigSfBerThreshold_Type())
apsConfigSfBerThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:apsConfigSfBerThreshold.setStatus(_A)
class _ApsConfigWaitToRestore_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_ApsConfigWaitToRestore_Type.__name__=_D
_ApsConfigWaitToRestore_Object=MibTableColumn
apsConfigWaitToRestore=_ApsConfigWaitToRestore_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1,9),_ApsConfigWaitToRestore_Type())
apsConfigWaitToRestore.setMaxAccess(_E)
if mibBuilder.loadTexts:apsConfigWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:apsConfigWaitToRestore.setUnits('seconds')
_ApsConfigCreationTime_Type=TimeStamp
_ApsConfigCreationTime_Object=MibTableColumn
apsConfigCreationTime=_ApsConfigCreationTime_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1,10),_ApsConfigCreationTime_Type())
apsConfigCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigCreationTime.setStatus(_A)
class _ApsConfigAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_ApsConfigAdminStatus_Type.__name__=_D
_ApsConfigAdminStatus_Object=MibTableColumn
apsConfigAdminStatus=_ApsConfigAdminStatus_Object((1,3,6,1,4,1,5504,10,1,1,1,1,2,1,11),_ApsConfigAdminStatus_Type())
apsConfigAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:apsConfigAdminStatus.setStatus(_A)
_ApsStatusTable_Object=MibTable
apsStatusTable=_ApsStatusTable_Object((1,3,6,1,4,1,5504,10,1,1,1,2))
if mibBuilder.loadTexts:apsStatusTable.setStatus(_A)
_ApsStatusEntry_Object=MibTableRow
apsStatusEntry=_ApsStatusEntry_Object((1,3,6,1,4,1,5504,10,1,1,1,2,1))
apsStatusEntry.setIndexNames((1,_B,_L))
if mibBuilder.loadTexts:apsStatusEntry.setStatus(_A)
_ApsStatusK1K2Rcv_Type=ApsK1K2
_ApsStatusK1K2Rcv_Object=MibTableColumn
apsStatusK1K2Rcv=_ApsStatusK1K2Rcv_Object((1,3,6,1,4,1,5504,10,1,1,1,2,1,1),_ApsStatusK1K2Rcv_Type())
apsStatusK1K2Rcv.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusK1K2Rcv.setStatus(_A)
_ApsStatusK1K2Trans_Type=ApsK1K2
_ApsStatusK1K2Trans_Object=MibTableColumn
apsStatusK1K2Trans=_ApsStatusK1K2Trans_Object((1,3,6,1,4,1,5504,10,1,1,1,2,1,2),_ApsStatusK1K2Trans_Type())
apsStatusK1K2Trans.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusK1K2Trans.setStatus(_A)
class _ApsStatusCurrent_Type(Bits):namedValues=NamedValues(*(('modeMismatch',0),('channelMismatch',1),('psbf',2),('feplf',3),('extraTraffic',4)))
_ApsStatusCurrent_Type.__name__=_K
_ApsStatusCurrent_Object=MibTableColumn
apsStatusCurrent=_ApsStatusCurrent_Object((1,3,6,1,4,1,5504,10,1,1,1,2,1,3),_ApsStatusCurrent_Type())
apsStatusCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusCurrent.setStatus(_A)
_ApsStatusModeMismatches_Type=Counter32
_ApsStatusModeMismatches_Object=MibTableColumn
apsStatusModeMismatches=_ApsStatusModeMismatches_Object((1,3,6,1,4,1,5504,10,1,1,1,2,1,4),_ApsStatusModeMismatches_Type())
apsStatusModeMismatches.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusModeMismatches.setStatus(_A)
_ApsStatusChannelMismatches_Type=Counter32
_ApsStatusChannelMismatches_Object=MibTableColumn
apsStatusChannelMismatches=_ApsStatusChannelMismatches_Object((1,3,6,1,4,1,5504,10,1,1,1,2,1,5),_ApsStatusChannelMismatches_Type())
apsStatusChannelMismatches.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusChannelMismatches.setStatus(_A)
_ApsStatusPSBFs_Type=Counter32
_ApsStatusPSBFs_Object=MibTableColumn
apsStatusPSBFs=_ApsStatusPSBFs_Object((1,3,6,1,4,1,5504,10,1,1,1,2,1,6),_ApsStatusPSBFs_Type())
apsStatusPSBFs.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusPSBFs.setStatus(_A)
_ApsStatusFEPLFs_Type=Counter32
_ApsStatusFEPLFs_Object=MibTableColumn
apsStatusFEPLFs=_ApsStatusFEPLFs_Object((1,3,6,1,4,1,5504,10,1,1,1,2,1,7),_ApsStatusFEPLFs_Type())
apsStatusFEPLFs.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusFEPLFs.setStatus(_A)
_ApsStatusSwitchedChannel_Type=Integer32
_ApsStatusSwitchedChannel_Object=MibTableColumn
apsStatusSwitchedChannel=_ApsStatusSwitchedChannel_Object((1,3,6,1,4,1,5504,10,1,1,1,2,1,8),_ApsStatusSwitchedChannel_Type())
apsStatusSwitchedChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusSwitchedChannel.setStatus(_A)
_ApsMap_ObjectIdentity=ObjectIdentity
apsMap=_ApsMap_ObjectIdentity((1,3,6,1,4,1,5504,10,1,1,1,3))
_ApsChanLTEs_Type=Gauge32
_ApsChanLTEs_Object=MibScalar
apsChanLTEs=_ApsChanLTEs_Object((1,3,6,1,4,1,5504,10,1,1,1,3,1),_ApsChanLTEs_Type())
apsChanLTEs.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanLTEs.setStatus(_A)
_ApsMapTable_Object=MibTable
apsMapTable=_ApsMapTable_Object((1,3,6,1,4,1,5504,10,1,1,1,3,2))
if mibBuilder.loadTexts:apsMapTable.setStatus(_A)
_ApsMapEntry_Object=MibTableRow
apsMapEntry=_ApsMapEntry_Object((1,3,6,1,4,1,5504,10,1,1,1,3,2,1))
apsMapEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:apsMapEntry.setStatus(_A)
_ApsMapIfIndex_Type=InterfaceIndex
_ApsMapIfIndex_Object=MibTableColumn
apsMapIfIndex=_ApsMapIfIndex_Object((1,3,6,1,4,1,5504,10,1,1,1,3,2,1,1),_ApsMapIfIndex_Type())
apsMapIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:apsMapIfIndex.setStatus(_A)
class _ApsMapGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ApsMapGroupName_Type.__name__=_G
_ApsMapGroupName_Object=MibTableColumn
apsMapGroupName=_ApsMapGroupName_Object((1,3,6,1,4,1,5504,10,1,1,1,3,2,1,2),_ApsMapGroupName_Type())
apsMapGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:apsMapGroupName.setStatus(_A)
class _ApsMapChanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,14))
_ApsMapChanNumber_Type.__name__=_D
_ApsMapChanNumber_Object=MibTableColumn
apsMapChanNumber=_ApsMapChanNumber_Object((1,3,6,1,4,1,5504,10,1,1,1,3,2,1,3),_ApsMapChanNumber_Type())
apsMapChanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:apsMapChanNumber.setStatus(_A)
_ApsChanConfigTable_Object=MibTable
apsChanConfigTable=_ApsChanConfigTable_Object((1,3,6,1,4,1,5504,10,1,1,1,4))
if mibBuilder.loadTexts:apsChanConfigTable.setStatus(_A)
_ApsChanConfigEntry_Object=MibTableRow
apsChanConfigEntry=_ApsChanConfigEntry_Object((1,3,6,1,4,1,5504,10,1,1,1,4,1))
apsChanConfigEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:apsChanConfigEntry.setStatus(_A)
class _ApsChanConfigGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApsChanConfigGroupName_Type.__name__=_G
_ApsChanConfigGroupName_Object=MibTableColumn
apsChanConfigGroupName=_ApsChanConfigGroupName_Object((1,3,6,1,4,1,5504,10,1,1,1,4,1,1),_ApsChanConfigGroupName_Type())
apsChanConfigGroupName.setMaxAccess(_H)
if mibBuilder.loadTexts:apsChanConfigGroupName.setStatus(_A)
class _ApsChanConfigNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_ApsChanConfigNumber_Type.__name__=_D
_ApsChanConfigNumber_Object=MibTableColumn
apsChanConfigNumber=_ApsChanConfigNumber_Object((1,3,6,1,4,1,5504,10,1,1,1,4,1,2),_ApsChanConfigNumber_Type())
apsChanConfigNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:apsChanConfigNumber.setStatus(_A)
_ApsChanConfigRowStatus_Type=RowStatus
_ApsChanConfigRowStatus_Object=MibTableColumn
apsChanConfigRowStatus=_ApsChanConfigRowStatus_Object((1,3,6,1,4,1,5504,10,1,1,1,4,1,3),_ApsChanConfigRowStatus_Type())
apsChanConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:apsChanConfigRowStatus.setStatus(_A)
_ApsChanConfigIfIndex_Type=InterfaceIndex
_ApsChanConfigIfIndex_Object=MibTableColumn
apsChanConfigIfIndex=_ApsChanConfigIfIndex_Object((1,3,6,1,4,1,5504,10,1,1,1,4,1,4),_ApsChanConfigIfIndex_Type())
apsChanConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:apsChanConfigIfIndex.setStatus(_A)
class _ApsChanConfigPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_ApsChanConfigPriority_Type.__name__=_D
_ApsChanConfigPriority_Object=MibTableColumn
apsChanConfigPriority=_ApsChanConfigPriority_Object((1,3,6,1,4,1,5504,10,1,1,1,4,1,5),_ApsChanConfigPriority_Type())
apsChanConfigPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:apsChanConfigPriority.setStatus(_A)
class _ApsChanConfigAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_ApsChanConfigAdminStatus_Type.__name__=_D
_ApsChanConfigAdminStatus_Object=MibTableColumn
apsChanConfigAdminStatus=_ApsChanConfigAdminStatus_Object((1,3,6,1,4,1,5504,10,1,1,1,4,1,6),_ApsChanConfigAdminStatus_Type())
apsChanConfigAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:apsChanConfigAdminStatus.setStatus(_A)
_ApsCommandTable_Object=MibTable
apsCommandTable=_ApsCommandTable_Object((1,3,6,1,4,1,5504,10,1,1,1,5))
if mibBuilder.loadTexts:apsCommandTable.setStatus(_A)
_ApsCommandEntry_Object=MibTableRow
apsCommandEntry=_ApsCommandEntry_Object((1,3,6,1,4,1,5504,10,1,1,1,5,1))
apsCommandEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:apsCommandEntry.setStatus(_A)
_ApsCommandSwitch_Type=ApsSwitchCommand
_ApsCommandSwitch_Object=MibTableColumn
apsCommandSwitch=_ApsCommandSwitch_Object((1,3,6,1,4,1,5504,10,1,1,1,5,1,1),_ApsCommandSwitch_Type())
apsCommandSwitch.setMaxAccess(_W)
if mibBuilder.loadTexts:apsCommandSwitch.setStatus(_A)
_ApsCommandControl_Type=ApsControlCommand
_ApsCommandControl_Object=MibTableColumn
apsCommandControl=_ApsCommandControl_Object((1,3,6,1,4,1,5504,10,1,1,1,5,1,2),_ApsCommandControl_Type())
apsCommandControl.setMaxAccess(_W)
if mibBuilder.loadTexts:apsCommandControl.setStatus(_A)
_ApsChanStatusTable_Object=MibTable
apsChanStatusTable=_ApsChanStatusTable_Object((1,3,6,1,4,1,5504,10,1,1,1,6))
if mibBuilder.loadTexts:apsChanStatusTable.setStatus(_A)
_ApsChanStatusEntry_Object=MibTableRow
apsChanStatusEntry=_ApsChanStatusEntry_Object((1,3,6,1,4,1,5504,10,1,1,1,6,1))
apsChanStatusEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:apsChanStatusEntry.setStatus(_A)
class _ApsChanStatusCurrent_Type(Bits):namedValues=NamedValues(*(('lockedOut',0),('sd',1),('sf',2),('switched',3)))
_ApsChanStatusCurrent_Type.__name__=_K
_ApsChanStatusCurrent_Object=MibTableColumn
apsChanStatusCurrent=_ApsChanStatusCurrent_Object((1,3,6,1,4,1,5504,10,1,1,1,6,1,1),_ApsChanStatusCurrent_Type())
apsChanStatusCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusCurrent.setStatus(_A)
_ApsChanStatusSignalDegrades_Type=Counter32
_ApsChanStatusSignalDegrades_Object=MibTableColumn
apsChanStatusSignalDegrades=_ApsChanStatusSignalDegrades_Object((1,3,6,1,4,1,5504,10,1,1,1,6,1,2),_ApsChanStatusSignalDegrades_Type())
apsChanStatusSignalDegrades.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusSignalDegrades.setStatus(_A)
_ApsChanStatusSignalFailures_Type=Counter32
_ApsChanStatusSignalFailures_Object=MibTableColumn
apsChanStatusSignalFailures=_ApsChanStatusSignalFailures_Object((1,3,6,1,4,1,5504,10,1,1,1,6,1,3),_ApsChanStatusSignalFailures_Type())
apsChanStatusSignalFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusSignalFailures.setStatus(_A)
_ApsChanStatusSwitchovers_Type=Counter32
_ApsChanStatusSwitchovers_Object=MibTableColumn
apsChanStatusSwitchovers=_ApsChanStatusSwitchovers_Object((1,3,6,1,4,1,5504,10,1,1,1,6,1,4),_ApsChanStatusSwitchovers_Type())
apsChanStatusSwitchovers.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusSwitchovers.setStatus(_A)
_ApsChanStatusLastSwitchover_Type=TimeStamp
_ApsChanStatusLastSwitchover_Object=MibTableColumn
apsChanStatusLastSwitchover=_ApsChanStatusLastSwitchover_Object((1,3,6,1,4,1,5504,10,1,1,1,6,1,5),_ApsChanStatusLastSwitchover_Type())
apsChanStatusLastSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusLastSwitchover.setStatus(_A)
_ApsChanStatusSwitchoverSeconds_Type=Counter32
_ApsChanStatusSwitchoverSeconds_Object=MibTableColumn
apsChanStatusSwitchoverSeconds=_ApsChanStatusSwitchoverSeconds_Object((1,3,6,1,4,1,5504,10,1,1,1,6,1,6),_ApsChanStatusSwitchoverSeconds_Type())
apsChanStatusSwitchoverSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusSwitchoverSeconds.setStatus(_A)
_ApsMIBNotifications_ObjectIdentity=ObjectIdentity
apsMIBNotifications=_ApsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,5504,10,1,1,2))
_ApsNotificationsPrefix_ObjectIdentity=ObjectIdentity
apsNotificationsPrefix=_ApsNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,5504,10,1,1,2,0))
_ApsMIBConformance_ObjectIdentity=ObjectIdentity
apsMIBConformance=_ApsMIBConformance_ObjectIdentity((1,3,6,1,4,1,5504,10,1,1,3))
_ApsGroups_ObjectIdentity=ObjectIdentity
apsGroups=_ApsGroups_ObjectIdentity((1,3,6,1,4,1,5504,10,1,1,3,1))
_ApsCompliances_ObjectIdentity=ObjectIdentity
apsCompliances=_ApsCompliances_ObjectIdentity((1,3,6,1,4,1,5504,10,1,1,3,2))
apsConfigGeneral=ObjectGroup((1,3,6,1,4,1,5504,10,1,1,3,1,1))
apsConfigGeneral.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:apsConfigGeneral.setStatus(_A)
apsConfigWtr=ObjectGroup((1,3,6,1,4,1,5504,10,1,1,3,1,2))
apsConfigWtr.setObjects((_B,_f))
if mibBuilder.loadTexts:apsConfigWtr.setStatus(_A)
apsCommandOnePlusOne=ObjectGroup((1,3,6,1,4,1,5504,10,1,1,3,1,3))
apsCommandOnePlusOne.setObjects((_B,_M))
if mibBuilder.loadTexts:apsCommandOnePlusOne.setStatus(_A)
apsCommandOneToN=ObjectGroup((1,3,6,1,4,1,5504,10,1,1,3,1,4))
apsCommandOneToN.setObjects(*((_B,_M),(_B,_g)))
if mibBuilder.loadTexts:apsCommandOneToN.setStatus(_A)
apsStatusGeneral=ObjectGroup((1,3,6,1,4,1,5504,10,1,1,3,1,5))
apsStatusGeneral.setObjects(*((_B,_h),(_B,_i),(_B,_F),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_j)))
if mibBuilder.loadTexts:apsStatusGeneral.setStatus(_A)
apsChanGeneral=ObjectGroup((1,3,6,1,4,1,5504,10,1,1,3,1,6))
apsChanGeneral.setObjects(*((_B,_k),(_B,_l),(_B,_R),(_B,_m),(_B,_n),(_B,_S),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:apsChanGeneral.setStatus(_A)
apsChanOneToN=ObjectGroup((1,3,6,1,4,1,5504,10,1,1,3,1,7))
apsChanOneToN.setObjects((_B,_q))
if mibBuilder.loadTexts:apsChanOneToN.setStatus(_A)
apsTotalsGroup=ObjectGroup((1,3,6,1,4,1,5504,10,1,1,3,1,8))
apsTotalsGroup.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:apsTotalsGroup.setStatus(_A)
apsMapGroup=ObjectGroup((1,3,6,1,4,1,5504,10,1,1,3,1,9))
apsMapGroup.setObjects(*((_B,_t),(_B,_u)))
if mibBuilder.loadTexts:apsMapGroup.setStatus(_A)
apsEventSwitchover=NotificationType((1,3,6,1,4,1,5504,10,1,1,2,0,1))
apsEventSwitchover.setObjects(*((_B,_S),(_B,_R)))
if mibBuilder.loadTexts:apsEventSwitchover.setStatus(_A)
apsEventModeMismatch=NotificationType((1,3,6,1,4,1,5504,10,1,1,2,0,2))
apsEventModeMismatch.setObjects(*((_B,_N),(_B,_F)))
if mibBuilder.loadTexts:apsEventModeMismatch.setStatus(_A)
apsEventChannelMismatch=NotificationType((1,3,6,1,4,1,5504,10,1,1,2,0,3))
apsEventChannelMismatch.setObjects(*((_B,_O),(_B,_F)))
if mibBuilder.loadTexts:apsEventChannelMismatch.setStatus(_A)
apsEventPSBF=NotificationType((1,3,6,1,4,1,5504,10,1,1,2,0,4))
apsEventPSBF.setObjects(*((_B,_P),(_B,_F)))
if mibBuilder.loadTexts:apsEventPSBF.setStatus(_A)
apsEventFEPLF=NotificationType((1,3,6,1,4,1,5504,10,1,1,2,0,5))
apsEventFEPLF.setObjects(*((_B,_Q),(_B,_F)))
if mibBuilder.loadTexts:apsEventFEPLF.setStatus(_A)
apsEventOptional=NotificationGroup((1,3,6,1,4,1,5504,10,1,1,3,1,10))
apsEventOptional.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:apsEventOptional.setStatus(_A)
apsCompliance=ModuleCompliance((1,3,6,1,4,1,5504,10,1,1,3,2,1))
apsCompliance.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:apsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ApsK1K2':ApsK1K2,'ApsSwitchCommand':ApsSwitchCommand,'ApsControlCommand':ApsControlCommand,'apsMIB':apsMIB,'apsMIBObjects':apsMIBObjects,'apsConfig':apsConfig,_r:apsConfigGroups,'apsConfigTable':apsConfigTable,'apsConfigEntry':apsConfigEntry,_L:apsConfigName,_e:apsConfigRowStatus,_X:apsConfigMode,_Y:apsConfigRevert,_Z:apsConfigDirection,_a:apsConfigExtraTraffic,_b:apsConfigSdBerThreshold,_c:apsConfigSfBerThreshold,_f:apsConfigWaitToRestore,_d:apsConfigCreationTime,'apsConfigAdminStatus':apsConfigAdminStatus,'apsStatusTable':apsStatusTable,'apsStatusEntry':apsStatusEntry,_h:apsStatusK1K2Rcv,_i:apsStatusK1K2Trans,_F:apsStatusCurrent,_N:apsStatusModeMismatches,_O:apsStatusChannelMismatches,_P:apsStatusPSBFs,_Q:apsStatusFEPLFs,_j:apsStatusSwitchedChannel,'apsMap':apsMap,_s:apsChanLTEs,'apsMapTable':apsMapTable,'apsMapEntry':apsMapEntry,_V:apsMapIfIndex,_t:apsMapGroupName,_u:apsMapChanNumber,'apsChanConfigTable':apsChanConfigTable,'apsChanConfigEntry':apsChanConfigEntry,_I:apsChanConfigGroupName,_J:apsChanConfigNumber,_l:apsChanConfigRowStatus,_k:apsChanConfigIfIndex,_q:apsChanConfigPriority,'apsChanConfigAdminStatus':apsChanConfigAdminStatus,'apsCommandTable':apsCommandTable,'apsCommandEntry':apsCommandEntry,_M:apsCommandSwitch,_g:apsCommandControl,'apsChanStatusTable':apsChanStatusTable,'apsChanStatusEntry':apsChanStatusEntry,_R:apsChanStatusCurrent,_m:apsChanStatusSignalDegrades,_n:apsChanStatusSignalFailures,_S:apsChanStatusSwitchovers,_o:apsChanStatusLastSwitchover,_p:apsChanStatusSwitchoverSeconds,'apsMIBNotifications':apsMIBNotifications,'apsNotificationsPrefix':apsNotificationsPrefix,_v:apsEventSwitchover,_w:apsEventModeMismatch,_x:apsEventChannelMismatch,_y:apsEventPSBF,_z:apsEventFEPLF,'apsMIBConformance':apsMIBConformance,'apsGroups':apsGroups,_A0:apsConfigGeneral,'apsConfigWtr':apsConfigWtr,'apsCommandOnePlusOne':apsCommandOnePlusOne,'apsCommandOneToN':apsCommandOneToN,_A1:apsStatusGeneral,_A2:apsChanGeneral,'apsChanOneToN':apsChanOneToN,'apsTotalsGroup':apsTotalsGroup,'apsMapGroup':apsMapGroup,'apsEventOptional':apsEventOptional,'apsCompliances':apsCompliances,'apsCompliance':apsCompliance})