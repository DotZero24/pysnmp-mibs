_A9='apsEventFEPLF'
_A8='apsEventPSBF'
_A7='apsEventChannelMismatch'
_A6='apsEventModeMismatch'
_A5='apsEventSwitchover'
_A4='apsMapChanNumber'
_A3='apsMapGroupName'
_A2='apsChanLTEs'
_A1='apsConfigGroups'
_A0='apsChanConfigPriority'
_z='apsChanStatusDiscontinuityTime'
_y='apsChanStatusSwitchoverSeconds'
_x='apsChanStatusLastSwitchover'
_w='apsChanStatusSignalFailures'
_v='apsChanStatusSignalDegrades'
_u='apsChanConfigStorageType'
_t='apsChanConfigRowStatus'
_s='apsChanConfigIfIndex'
_r='apsStatusDiscontinuityTime'
_q='apsStatusSwitchedChannel'
_p='apsStatusK1K2Trans'
_o='apsStatusK1K2Rcv'
_n='apsCommandControl'
_m='apsConfigWaitToRestore'
_l='apsNotificationEnable'
_k='apsConfigStorageType'
_j='apsConfigRowStatus'
_i='apsConfigCreationTime'
_h='apsConfigSfBerThreshold'
_g='apsConfigSdBerThreshold'
_f='apsConfigExtraTraffic'
_e='apsConfigDirection'
_d='apsConfigRevert'
_c='apsConfigMode'
_b='apsChanStatusEntry'
_a='apsStatusEntry'
_Z='channelMismatch'
_Y='modeMismatch'
_X='apsConfigName'
_W='ifIndex'
_V='IF-MIB'
_U='apsChanGeneral'
_T='apsStatusGeneral'
_S='apsConfigGeneral'
_R='apsChanStatusSwitchovers'
_Q='apsChanStatusCurrent'
_P='apsStatusFEPLFs'
_O='apsStatusPSBFs'
_N='apsStatusChannelMismatches'
_M='apsStatusModeMismatches'
_L='apsCommandSwitch'
_K='apsChanConfigNumber'
_J='apsChanConfigGroupName'
_I='not-accessible'
_H='StorageType'
_G='Bits'
_F='SnmpAdminString'
_E='apsStatusCurrent'
_D='Integer32'
_C='read-only'
_B='JNX-APS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_V,'InterfaceIndex',_W)
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI',_G,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_H,'TextualConvention','TimeStamp')
apsMIB=ModuleIdentity((1,3,6,1,4,1,2636,3,24))
if mibBuilder.loadTexts:apsMIB.setRevisions(('2002-05-08 23:00',))
class ApsK1K2(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class ApsSwitchCommand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noCmd',1),('clear',2),('lockoutOfProtection',3),('forcedSwitchWorkToProtect',4),('forcedSwitchProtectToWork',5),('manualSwitchWorkToProtect',6),('manualSwitchProtectToWork',7),('exercise',8)))
class ApsControlCommand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noCmd',1),('lockoutWorkingChannel',2),('clearLockoutWorkingChannel',3)))
_ApsMIBObjects_ObjectIdentity=ObjectIdentity
apsMIBObjects=_ApsMIBObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,24,1))
_ApsConfig_ObjectIdentity=ObjectIdentity
apsConfig=_ApsConfig_ObjectIdentity((1,3,6,1,4,1,2636,3,24,1,1))
_ApsConfigGroups_Type=Gauge32
_ApsConfigGroups_Object=MibScalar
apsConfigGroups=_ApsConfigGroups_Object((1,3,6,1,4,1,2636,3,24,1,1,1),_ApsConfigGroups_Type())
apsConfigGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigGroups.setStatus(_A)
_ApsConfigTable_Object=MibTable
apsConfigTable=_ApsConfigTable_Object((1,3,6,1,4,1,2636,3,24,1,1,2))
if mibBuilder.loadTexts:apsConfigTable.setStatus(_A)
_ApsConfigEntry_Object=MibTableRow
apsConfigEntry=_ApsConfigEntry_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1))
apsConfigEntry.setIndexNames((1,_B,_X))
if mibBuilder.loadTexts:apsConfigEntry.setStatus(_A)
class _ApsConfigName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApsConfigName_Type.__name__=_F
_ApsConfigName_Object=MibTableColumn
apsConfigName=_ApsConfigName_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1,1),_ApsConfigName_Type())
apsConfigName.setMaxAccess(_I)
if mibBuilder.loadTexts:apsConfigName.setStatus(_A)
_ApsConfigRowStatus_Type=RowStatus
_ApsConfigRowStatus_Object=MibTableColumn
apsConfigRowStatus=_ApsConfigRowStatus_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1,2),_ApsConfigRowStatus_Type())
apsConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigRowStatus.setStatus(_A)
class _ApsConfigMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('onePlusOne',1),('oneToN',2),('onePlusOneCompatible',3),('onePlusOneOptimized',4)))
_ApsConfigMode_Type.__name__=_D
_ApsConfigMode_Object=MibTableColumn
apsConfigMode=_ApsConfigMode_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1,3),_ApsConfigMode_Type())
apsConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigMode.setStatus(_A)
class _ApsConfigRevert_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonrevertive',1),('revertive',2)))
_ApsConfigRevert_Type.__name__=_D
_ApsConfigRevert_Object=MibTableColumn
apsConfigRevert=_ApsConfigRevert_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1,4),_ApsConfigRevert_Type())
apsConfigRevert.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigRevert.setStatus(_A)
class _ApsConfigDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
_ApsConfigDirection_Type.__name__=_D
_ApsConfigDirection_Object=MibTableColumn
apsConfigDirection=_ApsConfigDirection_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1,5),_ApsConfigDirection_Type())
apsConfigDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigDirection.setStatus(_A)
class _ApsConfigExtraTraffic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ApsConfigExtraTraffic_Type.__name__=_D
_ApsConfigExtraTraffic_Object=MibTableColumn
apsConfigExtraTraffic=_ApsConfigExtraTraffic_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1,6),_ApsConfigExtraTraffic_Type())
apsConfigExtraTraffic.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigExtraTraffic.setStatus(_A)
class _ApsConfigSdBerThreshold_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,9))
_ApsConfigSdBerThreshold_Type.__name__=_D
_ApsConfigSdBerThreshold_Object=MibTableColumn
apsConfigSdBerThreshold=_ApsConfigSdBerThreshold_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1,7),_ApsConfigSdBerThreshold_Type())
apsConfigSdBerThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigSdBerThreshold.setStatus(_A)
class _ApsConfigSfBerThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,5))
_ApsConfigSfBerThreshold_Type.__name__=_D
_ApsConfigSfBerThreshold_Object=MibTableColumn
apsConfigSfBerThreshold=_ApsConfigSfBerThreshold_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1,8),_ApsConfigSfBerThreshold_Type())
apsConfigSfBerThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigSfBerThreshold.setStatus(_A)
class _ApsConfigWaitToRestore_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_ApsConfigWaitToRestore_Type.__name__=_D
_ApsConfigWaitToRestore_Object=MibTableColumn
apsConfigWaitToRestore=_ApsConfigWaitToRestore_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1,9),_ApsConfigWaitToRestore_Type())
apsConfigWaitToRestore.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:apsConfigWaitToRestore.setUnits('seconds')
_ApsConfigCreationTime_Type=TimeStamp
_ApsConfigCreationTime_Object=MibTableColumn
apsConfigCreationTime=_ApsConfigCreationTime_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1,10),_ApsConfigCreationTime_Type())
apsConfigCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigCreationTime.setStatus(_A)
class _ApsConfigStorageType_Type(StorageType):defaultValue=3
_ApsConfigStorageType_Type.__name__=_H
_ApsConfigStorageType_Object=MibTableColumn
apsConfigStorageType=_ApsConfigStorageType_Object((1,3,6,1,4,1,2636,3,24,1,1,2,1,11),_ApsConfigStorageType_Type())
apsConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigStorageType.setStatus(_A)
_ApsStatusTable_Object=MibTable
apsStatusTable=_ApsStatusTable_Object((1,3,6,1,4,1,2636,3,24,1,2))
if mibBuilder.loadTexts:apsStatusTable.setStatus(_A)
_ApsStatusEntry_Object=MibTableRow
apsStatusEntry=_ApsStatusEntry_Object((1,3,6,1,4,1,2636,3,24,1,2,1))
if mibBuilder.loadTexts:apsStatusEntry.setStatus(_A)
_ApsStatusK1K2Rcv_Type=ApsK1K2
_ApsStatusK1K2Rcv_Object=MibTableColumn
apsStatusK1K2Rcv=_ApsStatusK1K2Rcv_Object((1,3,6,1,4,1,2636,3,24,1,2,1,1),_ApsStatusK1K2Rcv_Type())
apsStatusK1K2Rcv.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusK1K2Rcv.setStatus(_A)
_ApsStatusK1K2Trans_Type=ApsK1K2
_ApsStatusK1K2Trans_Object=MibTableColumn
apsStatusK1K2Trans=_ApsStatusK1K2Trans_Object((1,3,6,1,4,1,2636,3,24,1,2,1,2),_ApsStatusK1K2Trans_Type())
apsStatusK1K2Trans.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusK1K2Trans.setStatus(_A)
class _ApsStatusCurrent_Type(Bits):namedValues=NamedValues(*((_Y,0),(_Z,1),('psbf',2),('feplf',3),('extraTraffic',4)))
_ApsStatusCurrent_Type.__name__=_G
_ApsStatusCurrent_Object=MibTableColumn
apsStatusCurrent=_ApsStatusCurrent_Object((1,3,6,1,4,1,2636,3,24,1,2,1,3),_ApsStatusCurrent_Type())
apsStatusCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusCurrent.setStatus(_A)
_ApsStatusModeMismatches_Type=Counter32
_ApsStatusModeMismatches_Object=MibTableColumn
apsStatusModeMismatches=_ApsStatusModeMismatches_Object((1,3,6,1,4,1,2636,3,24,1,2,1,4),_ApsStatusModeMismatches_Type())
apsStatusModeMismatches.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusModeMismatches.setStatus(_A)
_ApsStatusChannelMismatches_Type=Counter32
_ApsStatusChannelMismatches_Object=MibTableColumn
apsStatusChannelMismatches=_ApsStatusChannelMismatches_Object((1,3,6,1,4,1,2636,3,24,1,2,1,5),_ApsStatusChannelMismatches_Type())
apsStatusChannelMismatches.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusChannelMismatches.setStatus(_A)
_ApsStatusPSBFs_Type=Counter32
_ApsStatusPSBFs_Object=MibTableColumn
apsStatusPSBFs=_ApsStatusPSBFs_Object((1,3,6,1,4,1,2636,3,24,1,2,1,6),_ApsStatusPSBFs_Type())
apsStatusPSBFs.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusPSBFs.setStatus(_A)
_ApsStatusFEPLFs_Type=Counter32
_ApsStatusFEPLFs_Object=MibTableColumn
apsStatusFEPLFs=_ApsStatusFEPLFs_Object((1,3,6,1,4,1,2636,3,24,1,2,1,7),_ApsStatusFEPLFs_Type())
apsStatusFEPLFs.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusFEPLFs.setStatus(_A)
_ApsStatusSwitchedChannel_Type=Integer32
_ApsStatusSwitchedChannel_Object=MibTableColumn
apsStatusSwitchedChannel=_ApsStatusSwitchedChannel_Object((1,3,6,1,4,1,2636,3,24,1,2,1,8),_ApsStatusSwitchedChannel_Type())
apsStatusSwitchedChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusSwitchedChannel.setStatus(_A)
_ApsStatusDiscontinuityTime_Type=TimeStamp
_ApsStatusDiscontinuityTime_Object=MibTableColumn
apsStatusDiscontinuityTime=_ApsStatusDiscontinuityTime_Object((1,3,6,1,4,1,2636,3,24,1,2,1,9),_ApsStatusDiscontinuityTime_Type())
apsStatusDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusDiscontinuityTime.setStatus(_A)
_ApsMap_ObjectIdentity=ObjectIdentity
apsMap=_ApsMap_ObjectIdentity((1,3,6,1,4,1,2636,3,24,1,3))
_ApsChanLTEs_Type=Gauge32
_ApsChanLTEs_Object=MibScalar
apsChanLTEs=_ApsChanLTEs_Object((1,3,6,1,4,1,2636,3,24,1,3,1),_ApsChanLTEs_Type())
apsChanLTEs.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanLTEs.setStatus(_A)
_ApsMapTable_Object=MibTable
apsMapTable=_ApsMapTable_Object((1,3,6,1,4,1,2636,3,24,1,3,2))
if mibBuilder.loadTexts:apsMapTable.setStatus(_A)
_ApsMapEntry_Object=MibTableRow
apsMapEntry=_ApsMapEntry_Object((1,3,6,1,4,1,2636,3,24,1,3,2,1))
apsMapEntry.setIndexNames((0,_V,_W))
if mibBuilder.loadTexts:apsMapEntry.setStatus(_A)
class _ApsMapGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ApsMapGroupName_Type.__name__=_F
_ApsMapGroupName_Object=MibTableColumn
apsMapGroupName=_ApsMapGroupName_Object((1,3,6,1,4,1,2636,3,24,1,3,2,1,2),_ApsMapGroupName_Type())
apsMapGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:apsMapGroupName.setStatus(_A)
class _ApsMapChanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,14))
_ApsMapChanNumber_Type.__name__=_D
_ApsMapChanNumber_Object=MibTableColumn
apsMapChanNumber=_ApsMapChanNumber_Object((1,3,6,1,4,1,2636,3,24,1,3,2,1,3),_ApsMapChanNumber_Type())
apsMapChanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:apsMapChanNumber.setStatus(_A)
_ApsChanConfigTable_Object=MibTable
apsChanConfigTable=_ApsChanConfigTable_Object((1,3,6,1,4,1,2636,3,24,1,4))
if mibBuilder.loadTexts:apsChanConfigTable.setStatus(_A)
_ApsChanConfigEntry_Object=MibTableRow
apsChanConfigEntry=_ApsChanConfigEntry_Object((1,3,6,1,4,1,2636,3,24,1,4,1))
apsChanConfigEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:apsChanConfigEntry.setStatus(_A)
class _ApsChanConfigGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApsChanConfigGroupName_Type.__name__=_F
_ApsChanConfigGroupName_Object=MibTableColumn
apsChanConfigGroupName=_ApsChanConfigGroupName_Object((1,3,6,1,4,1,2636,3,24,1,4,1,1),_ApsChanConfigGroupName_Type())
apsChanConfigGroupName.setMaxAccess(_I)
if mibBuilder.loadTexts:apsChanConfigGroupName.setStatus(_A)
class _ApsChanConfigNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_ApsChanConfigNumber_Type.__name__=_D
_ApsChanConfigNumber_Object=MibTableColumn
apsChanConfigNumber=_ApsChanConfigNumber_Object((1,3,6,1,4,1,2636,3,24,1,4,1,2),_ApsChanConfigNumber_Type())
apsChanConfigNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:apsChanConfigNumber.setStatus(_A)
_ApsChanConfigRowStatus_Type=RowStatus
_ApsChanConfigRowStatus_Object=MibTableColumn
apsChanConfigRowStatus=_ApsChanConfigRowStatus_Object((1,3,6,1,4,1,2636,3,24,1,4,1,3),_ApsChanConfigRowStatus_Type())
apsChanConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanConfigRowStatus.setStatus(_A)
_ApsChanConfigIfIndex_Type=InterfaceIndex
_ApsChanConfigIfIndex_Object=MibTableColumn
apsChanConfigIfIndex=_ApsChanConfigIfIndex_Object((1,3,6,1,4,1,2636,3,24,1,4,1,4),_ApsChanConfigIfIndex_Type())
apsChanConfigIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanConfigIfIndex.setStatus(_A)
class _ApsChanConfigPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_ApsChanConfigPriority_Type.__name__=_D
_ApsChanConfigPriority_Object=MibTableColumn
apsChanConfigPriority=_ApsChanConfigPriority_Object((1,3,6,1,4,1,2636,3,24,1,4,1,5),_ApsChanConfigPriority_Type())
apsChanConfigPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanConfigPriority.setStatus(_A)
class _ApsChanConfigStorageType_Type(StorageType):defaultValue=3
_ApsChanConfigStorageType_Type.__name__=_H
_ApsChanConfigStorageType_Object=MibTableColumn
apsChanConfigStorageType=_ApsChanConfigStorageType_Object((1,3,6,1,4,1,2636,3,24,1,4,1,6),_ApsChanConfigStorageType_Type())
apsChanConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanConfigStorageType.setStatus(_A)
_ApsCommandTable_Object=MibTable
apsCommandTable=_ApsCommandTable_Object((1,3,6,1,4,1,2636,3,24,1,5))
if mibBuilder.loadTexts:apsCommandTable.setStatus(_A)
_ApsCommandEntry_Object=MibTableRow
apsCommandEntry=_ApsCommandEntry_Object((1,3,6,1,4,1,2636,3,24,1,5,1))
apsCommandEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:apsCommandEntry.setStatus(_A)
_ApsCommandSwitch_Type=ApsSwitchCommand
_ApsCommandSwitch_Object=MibTableColumn
apsCommandSwitch=_ApsCommandSwitch_Object((1,3,6,1,4,1,2636,3,24,1,5,1,1),_ApsCommandSwitch_Type())
apsCommandSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:apsCommandSwitch.setStatus(_A)
_ApsCommandControl_Type=ApsControlCommand
_ApsCommandControl_Object=MibTableColumn
apsCommandControl=_ApsCommandControl_Object((1,3,6,1,4,1,2636,3,24,1,5,1,2),_ApsCommandControl_Type())
apsCommandControl.setMaxAccess(_C)
if mibBuilder.loadTexts:apsCommandControl.setStatus(_A)
_ApsChanStatusTable_Object=MibTable
apsChanStatusTable=_ApsChanStatusTable_Object((1,3,6,1,4,1,2636,3,24,1,6))
if mibBuilder.loadTexts:apsChanStatusTable.setStatus(_A)
_ApsChanStatusEntry_Object=MibTableRow
apsChanStatusEntry=_ApsChanStatusEntry_Object((1,3,6,1,4,1,2636,3,24,1,6,1))
if mibBuilder.loadTexts:apsChanStatusEntry.setStatus(_A)
class _ApsChanStatusCurrent_Type(Bits):namedValues=NamedValues(*(('lockedOut',0),('sd',1),('sf',2),('switched',3),('wtr',4)))
_ApsChanStatusCurrent_Type.__name__=_G
_ApsChanStatusCurrent_Object=MibTableColumn
apsChanStatusCurrent=_ApsChanStatusCurrent_Object((1,3,6,1,4,1,2636,3,24,1,6,1,1),_ApsChanStatusCurrent_Type())
apsChanStatusCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusCurrent.setStatus(_A)
_ApsChanStatusSignalDegrades_Type=Counter32
_ApsChanStatusSignalDegrades_Object=MibTableColumn
apsChanStatusSignalDegrades=_ApsChanStatusSignalDegrades_Object((1,3,6,1,4,1,2636,3,24,1,6,1,2),_ApsChanStatusSignalDegrades_Type())
apsChanStatusSignalDegrades.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusSignalDegrades.setStatus(_A)
_ApsChanStatusSignalFailures_Type=Counter32
_ApsChanStatusSignalFailures_Object=MibTableColumn
apsChanStatusSignalFailures=_ApsChanStatusSignalFailures_Object((1,3,6,1,4,1,2636,3,24,1,6,1,3),_ApsChanStatusSignalFailures_Type())
apsChanStatusSignalFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusSignalFailures.setStatus(_A)
_ApsChanStatusSwitchovers_Type=Counter32
_ApsChanStatusSwitchovers_Object=MibTableColumn
apsChanStatusSwitchovers=_ApsChanStatusSwitchovers_Object((1,3,6,1,4,1,2636,3,24,1,6,1,4),_ApsChanStatusSwitchovers_Type())
apsChanStatusSwitchovers.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusSwitchovers.setStatus(_A)
_ApsChanStatusLastSwitchover_Type=TimeStamp
_ApsChanStatusLastSwitchover_Object=MibTableColumn
apsChanStatusLastSwitchover=_ApsChanStatusLastSwitchover_Object((1,3,6,1,4,1,2636,3,24,1,6,1,5),_ApsChanStatusLastSwitchover_Type())
apsChanStatusLastSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusLastSwitchover.setStatus(_A)
_ApsChanStatusSwitchoverSeconds_Type=Counter32
_ApsChanStatusSwitchoverSeconds_Object=MibTableColumn
apsChanStatusSwitchoverSeconds=_ApsChanStatusSwitchoverSeconds_Object((1,3,6,1,4,1,2636,3,24,1,6,1,6),_ApsChanStatusSwitchoverSeconds_Type())
apsChanStatusSwitchoverSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusSwitchoverSeconds.setStatus(_A)
_ApsChanStatusDiscontinuityTime_Type=TimeStamp
_ApsChanStatusDiscontinuityTime_Object=MibTableColumn
apsChanStatusDiscontinuityTime=_ApsChanStatusDiscontinuityTime_Object((1,3,6,1,4,1,2636,3,24,1,6,1,7),_ApsChanStatusDiscontinuityTime_Type())
apsChanStatusDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusDiscontinuityTime.setStatus(_A)
class _ApsNotificationEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('switchover',0),(_Y,1),(_Z,2),('psbf',3),('feplf',4)))
_ApsNotificationEnable_Type.__name__=_G
_ApsNotificationEnable_Object=MibScalar
apsNotificationEnable=_ApsNotificationEnable_Object((1,3,6,1,4,1,2636,3,24,1,7),_ApsNotificationEnable_Type())
apsNotificationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:apsNotificationEnable.setStatus(_A)
_ApsMIBNotifications_ObjectIdentity=ObjectIdentity
apsMIBNotifications=_ApsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2636,3,24,2))
_ApsNotificationsPrefix_ObjectIdentity=ObjectIdentity
apsNotificationsPrefix=_ApsNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,2636,3,24,2,0))
_ApsMIBConformance_ObjectIdentity=ObjectIdentity
apsMIBConformance=_ApsMIBConformance_ObjectIdentity((1,3,6,1,4,1,2636,3,24,3))
_ApsGroups_ObjectIdentity=ObjectIdentity
apsGroups=_ApsGroups_ObjectIdentity((1,3,6,1,4,1,2636,3,24,3,1))
_ApsCompliances_ObjectIdentity=ObjectIdentity
apsCompliances=_ApsCompliances_ObjectIdentity((1,3,6,1,4,1,2636,3,24,3,2))
apsConfigEntry.registerAugmentions((_B,_a))
apsStatusEntry.setIndexNames(*apsConfigEntry.getIndexNames())
apsChanConfigEntry.registerAugmentions((_B,_b))
apsChanStatusEntry.setIndexNames(*apsChanConfigEntry.getIndexNames())
apsConfigGeneral=ObjectGroup((1,3,6,1,4,1,2636,3,24,3,1,1))
apsConfigGeneral.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:apsConfigGeneral.setStatus(_A)
apsConfigWtr=ObjectGroup((1,3,6,1,4,1,2636,3,24,3,1,2))
apsConfigWtr.setObjects((_B,_m))
if mibBuilder.loadTexts:apsConfigWtr.setStatus(_A)
apsCommandOnePlusOne=ObjectGroup((1,3,6,1,4,1,2636,3,24,3,1,3))
apsCommandOnePlusOne.setObjects((_B,_L))
if mibBuilder.loadTexts:apsCommandOnePlusOne.setStatus(_A)
apsCommandOneToN=ObjectGroup((1,3,6,1,4,1,2636,3,24,3,1,4))
apsCommandOneToN.setObjects(*((_B,_L),(_B,_n)))
if mibBuilder.loadTexts:apsCommandOneToN.setStatus(_A)
apsStatusGeneral=ObjectGroup((1,3,6,1,4,1,2636,3,24,3,1,5))
apsStatusGeneral.setObjects(*((_B,_o),(_B,_p),(_B,_E),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:apsStatusGeneral.setStatus(_A)
apsChanGeneral=ObjectGroup((1,3,6,1,4,1,2636,3,24,3,1,6))
apsChanGeneral.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_Q),(_B,_v),(_B,_w),(_B,_R),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:apsChanGeneral.setStatus(_A)
apsChanOneToN=ObjectGroup((1,3,6,1,4,1,2636,3,24,3,1,7))
apsChanOneToN.setObjects((_B,_A0))
if mibBuilder.loadTexts:apsChanOneToN.setStatus(_A)
apsTotalsGroup=ObjectGroup((1,3,6,1,4,1,2636,3,24,3,1,8))
apsTotalsGroup.setObjects(*((_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:apsTotalsGroup.setStatus(_A)
apsMapGroup=ObjectGroup((1,3,6,1,4,1,2636,3,24,3,1,9))
apsMapGroup.setObjects(*((_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:apsMapGroup.setStatus(_A)
apsEventSwitchover=NotificationType((1,3,6,1,4,1,2636,3,24,2,0,1))
apsEventSwitchover.setObjects(*((_B,_R),(_B,_Q)))
if mibBuilder.loadTexts:apsEventSwitchover.setStatus(_A)
apsEventModeMismatch=NotificationType((1,3,6,1,4,1,2636,3,24,2,0,2))
apsEventModeMismatch.setObjects(*((_B,_M),(_B,_E)))
if mibBuilder.loadTexts:apsEventModeMismatch.setStatus(_A)
apsEventChannelMismatch=NotificationType((1,3,6,1,4,1,2636,3,24,2,0,3))
apsEventChannelMismatch.setObjects(*((_B,_N),(_B,_E)))
if mibBuilder.loadTexts:apsEventChannelMismatch.setStatus(_A)
apsEventPSBF=NotificationType((1,3,6,1,4,1,2636,3,24,2,0,4))
apsEventPSBF.setObjects(*((_B,_O),(_B,_E)))
if mibBuilder.loadTexts:apsEventPSBF.setStatus(_A)
apsEventFEPLF=NotificationType((1,3,6,1,4,1,2636,3,24,2,0,5))
apsEventFEPLF.setObjects(*((_B,_P),(_B,_E)))
if mibBuilder.loadTexts:apsEventFEPLF.setStatus(_A)
apsEventGroup=NotificationGroup((1,3,6,1,4,1,2636,3,24,3,1,10))
apsEventGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:apsEventGroup.setStatus(_A)
apsFullCompliance=ModuleCompliance((1,3,6,1,4,1,2636,3,24,3,2,1))
apsFullCompliance.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:apsFullCompliance.setStatus(_A)
apsReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,2636,3,24,3,2,2))
apsReadOnlyCompliance.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:apsReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ApsK1K2':ApsK1K2,'ApsSwitchCommand':ApsSwitchCommand,'ApsControlCommand':ApsControlCommand,'apsMIB':apsMIB,'apsMIBObjects':apsMIBObjects,'apsConfig':apsConfig,_A1:apsConfigGroups,'apsConfigTable':apsConfigTable,'apsConfigEntry':apsConfigEntry,_X:apsConfigName,_j:apsConfigRowStatus,_c:apsConfigMode,_d:apsConfigRevert,_e:apsConfigDirection,_f:apsConfigExtraTraffic,_g:apsConfigSdBerThreshold,_h:apsConfigSfBerThreshold,_m:apsConfigWaitToRestore,_i:apsConfigCreationTime,_k:apsConfigStorageType,'apsStatusTable':apsStatusTable,_a:apsStatusEntry,_o:apsStatusK1K2Rcv,_p:apsStatusK1K2Trans,_E:apsStatusCurrent,_M:apsStatusModeMismatches,_N:apsStatusChannelMismatches,_O:apsStatusPSBFs,_P:apsStatusFEPLFs,_q:apsStatusSwitchedChannel,_r:apsStatusDiscontinuityTime,'apsMap':apsMap,_A2:apsChanLTEs,'apsMapTable':apsMapTable,'apsMapEntry':apsMapEntry,_A3:apsMapGroupName,_A4:apsMapChanNumber,'apsChanConfigTable':apsChanConfigTable,'apsChanConfigEntry':apsChanConfigEntry,_J:apsChanConfigGroupName,_K:apsChanConfigNumber,_t:apsChanConfigRowStatus,_s:apsChanConfigIfIndex,_A0:apsChanConfigPriority,_u:apsChanConfigStorageType,'apsCommandTable':apsCommandTable,'apsCommandEntry':apsCommandEntry,_L:apsCommandSwitch,_n:apsCommandControl,'apsChanStatusTable':apsChanStatusTable,_b:apsChanStatusEntry,_Q:apsChanStatusCurrent,_v:apsChanStatusSignalDegrades,_w:apsChanStatusSignalFailures,_R:apsChanStatusSwitchovers,_x:apsChanStatusLastSwitchover,_y:apsChanStatusSwitchoverSeconds,_z:apsChanStatusDiscontinuityTime,_l:apsNotificationEnable,'apsMIBNotifications':apsMIBNotifications,'apsNotificationsPrefix':apsNotificationsPrefix,_A5:apsEventSwitchover,_A6:apsEventModeMismatch,_A7:apsEventChannelMismatch,_A8:apsEventPSBF,_A9:apsEventFEPLF,'apsMIBConformance':apsMIBConformance,'apsGroups':apsGroups,_S:apsConfigGeneral,'apsConfigWtr':apsConfigWtr,'apsCommandOnePlusOne':apsCommandOnePlusOne,'apsCommandOneToN':apsCommandOneToN,_T:apsStatusGeneral,_U:apsChanGeneral,'apsChanOneToN':apsChanOneToN,'apsTotalsGroup':apsTotalsGroup,'apsMapGroup':apsMapGroup,'apsEventGroup':apsEventGroup,'apsCompliances':apsCompliances,'apsFullCompliance':apsFullCompliance,'apsReadOnlyCompliance':apsReadOnlyCompliance})