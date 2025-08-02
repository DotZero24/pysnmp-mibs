_A0='cApsChanGeneral'
_z='cApsStatusGeneral'
_y='cApsConfigGeneral'
_x='cApsEventFEPLF'
_w='cApsEventPSBF'
_v='cApsEventChannelMismatch'
_u='cApsEventModeMismatch'
_t='cApsEventSwitchover'
_s='cApsMapChanNumber'
_r='cApsMapGroupName'
_q='cApsChanLTEs'
_p='cApsConfigGroups'
_o='cApsChanConfigPriority'
_n='cApsChanStatusSwitchoverSeconds'
_m='cApsChanStatusLastSwitchover'
_l='cApsChanStatusSignalFailures'
_k='cApsChanStatusSignalDegrades'
_j='cApsChanConfigRowStatus'
_i='cApsChanConfigIfIndex'
_h='cApsStatusSwitchedChannel'
_g='cApsStatusK1K2Trans'
_f='cApsStatusK1K2Rcv'
_e='cApsCommandControl'
_d='cApsConfigWaitToRestore'
_c='cApsConfigRowStatus'
_b='cApsConfigCreationTime'
_a='cApsConfigSfBerThreshold'
_Z='cApsConfigSdBerThreshold'
_Y='cApsConfigExtraTraffic'
_X='cApsConfigDirection'
_W='cApsConfigRevert'
_V='cApsConfigMode'
_U='read-write'
_T='cApsMapIfIndex'
_S='cApsChanStatusSwitchovers'
_R='cApsChanStatusCurrent'
_Q='cApsStatusFEPLFs'
_P='cApsStatusPSBFs'
_O='cApsStatusChannelMismatches'
_N='cApsStatusModeMismatches'
_M='cApsCommandSwitch'
_L='cApsConfigName'
_K='Bits'
_J='cApsChanConfigNumber'
_I='cApsChanConfigGroupName'
_H='not-accessible'
_G='SnmpAdminString'
_F='cApsStatusCurrent'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='CISCO-APS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
cApsMIB=ModuleIdentity((1,3,6,1,4,1,9,10,71))
if mibBuilder.loadTexts:cApsMIB.setRevisions(('2001-12-26 12:00','2001-04-29 00:00'))
class CApsK1K2(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class CApsSwitchCommand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noCmd',1),('clear',2),('lockoutOfProtection',3),('forcedSwitchWorkToProtect',4),('forcedSwitchProtectToWork',5),('manualSwitchWorkToProtect',6),('manualSwitchProtectToWork',7),('exercise',8)))
class CApsControlCommand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noCmd',1),('lockoutWorkingChannel',2),('clearLockoutWorkingChannel',3)))
_CApsMIBObjects_ObjectIdentity=ObjectIdentity
cApsMIBObjects=_CApsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,71,1))
_CApsConfig_ObjectIdentity=ObjectIdentity
cApsConfig=_CApsConfig_ObjectIdentity((1,3,6,1,4,1,9,10,71,1,1))
_CApsConfigGroups_Type=Gauge32
_CApsConfigGroups_Object=MibScalar
cApsConfigGroups=_CApsConfigGroups_Object((1,3,6,1,4,1,9,10,71,1,1,1),_CApsConfigGroups_Type())
cApsConfigGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigGroups.setStatus(_A)
_CApsConfigTable_Object=MibTable
cApsConfigTable=_CApsConfigTable_Object((1,3,6,1,4,1,9,10,71,1,1,2))
if mibBuilder.loadTexts:cApsConfigTable.setStatus(_A)
_CApsConfigEntry_Object=MibTableRow
cApsConfigEntry=_CApsConfigEntry_Object((1,3,6,1,4,1,9,10,71,1,1,2,1))
cApsConfigEntry.setIndexNames((1,_B,_L))
if mibBuilder.loadTexts:cApsConfigEntry.setStatus(_A)
class _CApsConfigName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CApsConfigName_Type.__name__=_G
_CApsConfigName_Object=MibTableColumn
cApsConfigName=_CApsConfigName_Object((1,3,6,1,4,1,9,10,71,1,1,2,1,1),_CApsConfigName_Type())
cApsConfigName.setMaxAccess(_H)
if mibBuilder.loadTexts:cApsConfigName.setStatus(_A)
_CApsConfigRowStatus_Type=RowStatus
_CApsConfigRowStatus_Object=MibTableColumn
cApsConfigRowStatus=_CApsConfigRowStatus_Object((1,3,6,1,4,1,9,10,71,1,1,2,1,2),_CApsConfigRowStatus_Type())
cApsConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsConfigRowStatus.setStatus(_A)
class _CApsConfigMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('onePlusOne',1),('oneToN',2),('onePlusOneCompatible',3),('onePlusOneOptimized',4)))
_CApsConfigMode_Type.__name__=_D
_CApsConfigMode_Object=MibTableColumn
cApsConfigMode=_CApsConfigMode_Object((1,3,6,1,4,1,9,10,71,1,1,2,1,3),_CApsConfigMode_Type())
cApsConfigMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsConfigMode.setStatus(_A)
class _CApsConfigRevert_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonrevertive',1),('revertive',2)))
_CApsConfigRevert_Type.__name__=_D
_CApsConfigRevert_Object=MibTableColumn
cApsConfigRevert=_CApsConfigRevert_Object((1,3,6,1,4,1,9,10,71,1,1,2,1,4),_CApsConfigRevert_Type())
cApsConfigRevert.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsConfigRevert.setStatus(_A)
class _CApsConfigDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
_CApsConfigDirection_Type.__name__=_D
_CApsConfigDirection_Object=MibTableColumn
cApsConfigDirection=_CApsConfigDirection_Object((1,3,6,1,4,1,9,10,71,1,1,2,1,5),_CApsConfigDirection_Type())
cApsConfigDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsConfigDirection.setStatus(_A)
class _CApsConfigExtraTraffic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CApsConfigExtraTraffic_Type.__name__=_D
_CApsConfigExtraTraffic_Object=MibTableColumn
cApsConfigExtraTraffic=_CApsConfigExtraTraffic_Object((1,3,6,1,4,1,9,10,71,1,1,2,1,6),_CApsConfigExtraTraffic_Type())
cApsConfigExtraTraffic.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsConfigExtraTraffic.setStatus(_A)
class _CApsConfigSdBerThreshold_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,9))
_CApsConfigSdBerThreshold_Type.__name__=_D
_CApsConfigSdBerThreshold_Object=MibTableColumn
cApsConfigSdBerThreshold=_CApsConfigSdBerThreshold_Object((1,3,6,1,4,1,9,10,71,1,1,2,1,7),_CApsConfigSdBerThreshold_Type())
cApsConfigSdBerThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsConfigSdBerThreshold.setStatus(_A)
class _CApsConfigSfBerThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,5))
_CApsConfigSfBerThreshold_Type.__name__=_D
_CApsConfigSfBerThreshold_Object=MibTableColumn
cApsConfigSfBerThreshold=_CApsConfigSfBerThreshold_Object((1,3,6,1,4,1,9,10,71,1,1,2,1,8),_CApsConfigSfBerThreshold_Type())
cApsConfigSfBerThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsConfigSfBerThreshold.setStatus(_A)
class _CApsConfigWaitToRestore_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_CApsConfigWaitToRestore_Type.__name__=_D
_CApsConfigWaitToRestore_Object=MibTableColumn
cApsConfigWaitToRestore=_CApsConfigWaitToRestore_Object((1,3,6,1,4,1,9,10,71,1,1,2,1,9),_CApsConfigWaitToRestore_Type())
cApsConfigWaitToRestore.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsConfigWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:cApsConfigWaitToRestore.setUnits('seconds')
_CApsConfigCreationTime_Type=TimeStamp
_CApsConfigCreationTime_Object=MibTableColumn
cApsConfigCreationTime=_CApsConfigCreationTime_Object((1,3,6,1,4,1,9,10,71,1,1,2,1,10),_CApsConfigCreationTime_Type())
cApsConfigCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsConfigCreationTime.setStatus(_A)
_CApsStatusTable_Object=MibTable
cApsStatusTable=_CApsStatusTable_Object((1,3,6,1,4,1,9,10,71,1,2))
if mibBuilder.loadTexts:cApsStatusTable.setStatus(_A)
_CApsStatusEntry_Object=MibTableRow
cApsStatusEntry=_CApsStatusEntry_Object((1,3,6,1,4,1,9,10,71,1,2,1))
cApsStatusEntry.setIndexNames((1,_B,_L))
if mibBuilder.loadTexts:cApsStatusEntry.setStatus(_A)
_CApsStatusK1K2Rcv_Type=CApsK1K2
_CApsStatusK1K2Rcv_Object=MibTableColumn
cApsStatusK1K2Rcv=_CApsStatusK1K2Rcv_Object((1,3,6,1,4,1,9,10,71,1,2,1,1),_CApsStatusK1K2Rcv_Type())
cApsStatusK1K2Rcv.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsStatusK1K2Rcv.setStatus(_A)
_CApsStatusK1K2Trans_Type=CApsK1K2
_CApsStatusK1K2Trans_Object=MibTableColumn
cApsStatusK1K2Trans=_CApsStatusK1K2Trans_Object((1,3,6,1,4,1,9,10,71,1,2,1,2),_CApsStatusK1K2Trans_Type())
cApsStatusK1K2Trans.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsStatusK1K2Trans.setStatus(_A)
class _CApsStatusCurrent_Type(Bits):namedValues=NamedValues(*(('modeMismatch',0),('channelMismatch',1),('psbf',2),('feplf',3),('extraTraffic',4)))
_CApsStatusCurrent_Type.__name__=_K
_CApsStatusCurrent_Object=MibTableColumn
cApsStatusCurrent=_CApsStatusCurrent_Object((1,3,6,1,4,1,9,10,71,1,2,1,3),_CApsStatusCurrent_Type())
cApsStatusCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsStatusCurrent.setStatus(_A)
_CApsStatusModeMismatches_Type=Counter32
_CApsStatusModeMismatches_Object=MibTableColumn
cApsStatusModeMismatches=_CApsStatusModeMismatches_Object((1,3,6,1,4,1,9,10,71,1,2,1,4),_CApsStatusModeMismatches_Type())
cApsStatusModeMismatches.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsStatusModeMismatches.setStatus(_A)
_CApsStatusChannelMismatches_Type=Counter32
_CApsStatusChannelMismatches_Object=MibTableColumn
cApsStatusChannelMismatches=_CApsStatusChannelMismatches_Object((1,3,6,1,4,1,9,10,71,1,2,1,5),_CApsStatusChannelMismatches_Type())
cApsStatusChannelMismatches.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsStatusChannelMismatches.setStatus(_A)
_CApsStatusPSBFs_Type=Counter32
_CApsStatusPSBFs_Object=MibTableColumn
cApsStatusPSBFs=_CApsStatusPSBFs_Object((1,3,6,1,4,1,9,10,71,1,2,1,6),_CApsStatusPSBFs_Type())
cApsStatusPSBFs.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsStatusPSBFs.setStatus(_A)
_CApsStatusFEPLFs_Type=Counter32
_CApsStatusFEPLFs_Object=MibTableColumn
cApsStatusFEPLFs=_CApsStatusFEPLFs_Object((1,3,6,1,4,1,9,10,71,1,2,1,7),_CApsStatusFEPLFs_Type())
cApsStatusFEPLFs.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsStatusFEPLFs.setStatus(_A)
_CApsStatusSwitchedChannel_Type=Integer32
_CApsStatusSwitchedChannel_Object=MibTableColumn
cApsStatusSwitchedChannel=_CApsStatusSwitchedChannel_Object((1,3,6,1,4,1,9,10,71,1,2,1,8),_CApsStatusSwitchedChannel_Type())
cApsStatusSwitchedChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsStatusSwitchedChannel.setStatus(_A)
_CApsMap_ObjectIdentity=ObjectIdentity
cApsMap=_CApsMap_ObjectIdentity((1,3,6,1,4,1,9,10,71,1,3))
_CApsChanLTEs_Type=Gauge32
_CApsChanLTEs_Object=MibScalar
cApsChanLTEs=_CApsChanLTEs_Object((1,3,6,1,4,1,9,10,71,1,3,1),_CApsChanLTEs_Type())
cApsChanLTEs.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsChanLTEs.setStatus(_A)
_CApsMapTable_Object=MibTable
cApsMapTable=_CApsMapTable_Object((1,3,6,1,4,1,9,10,71,1,3,2))
if mibBuilder.loadTexts:cApsMapTable.setStatus(_A)
_CApsMapEntry_Object=MibTableRow
cApsMapEntry=_CApsMapEntry_Object((1,3,6,1,4,1,9,10,71,1,3,2,1))
cApsMapEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:cApsMapEntry.setStatus(_A)
_CApsMapIfIndex_Type=InterfaceIndex
_CApsMapIfIndex_Object=MibTableColumn
cApsMapIfIndex=_CApsMapIfIndex_Object((1,3,6,1,4,1,9,10,71,1,3,2,1,1),_CApsMapIfIndex_Type())
cApsMapIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:cApsMapIfIndex.setStatus(_A)
class _CApsMapGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CApsMapGroupName_Type.__name__=_G
_CApsMapGroupName_Object=MibTableColumn
cApsMapGroupName=_CApsMapGroupName_Object((1,3,6,1,4,1,9,10,71,1,3,2,1,2),_CApsMapGroupName_Type())
cApsMapGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsMapGroupName.setStatus(_A)
class _CApsMapChanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,14))
_CApsMapChanNumber_Type.__name__=_D
_CApsMapChanNumber_Object=MibTableColumn
cApsMapChanNumber=_CApsMapChanNumber_Object((1,3,6,1,4,1,9,10,71,1,3,2,1,3),_CApsMapChanNumber_Type())
cApsMapChanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsMapChanNumber.setStatus(_A)
_CApsChanConfigTable_Object=MibTable
cApsChanConfigTable=_CApsChanConfigTable_Object((1,3,6,1,4,1,9,10,71,1,4))
if mibBuilder.loadTexts:cApsChanConfigTable.setStatus(_A)
_CApsChanConfigEntry_Object=MibTableRow
cApsChanConfigEntry=_CApsChanConfigEntry_Object((1,3,6,1,4,1,9,10,71,1,4,1))
cApsChanConfigEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:cApsChanConfigEntry.setStatus(_A)
class _CApsChanConfigGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CApsChanConfigGroupName_Type.__name__=_G
_CApsChanConfigGroupName_Object=MibTableColumn
cApsChanConfigGroupName=_CApsChanConfigGroupName_Object((1,3,6,1,4,1,9,10,71,1,4,1,1),_CApsChanConfigGroupName_Type())
cApsChanConfigGroupName.setMaxAccess(_H)
if mibBuilder.loadTexts:cApsChanConfigGroupName.setStatus(_A)
class _CApsChanConfigNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_CApsChanConfigNumber_Type.__name__=_D
_CApsChanConfigNumber_Object=MibTableColumn
cApsChanConfigNumber=_CApsChanConfigNumber_Object((1,3,6,1,4,1,9,10,71,1,4,1,2),_CApsChanConfigNumber_Type())
cApsChanConfigNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:cApsChanConfigNumber.setStatus(_A)
_CApsChanConfigRowStatus_Type=RowStatus
_CApsChanConfigRowStatus_Object=MibTableColumn
cApsChanConfigRowStatus=_CApsChanConfigRowStatus_Object((1,3,6,1,4,1,9,10,71,1,4,1,3),_CApsChanConfigRowStatus_Type())
cApsChanConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsChanConfigRowStatus.setStatus(_A)
_CApsChanConfigIfIndex_Type=InterfaceIndex
_CApsChanConfigIfIndex_Object=MibTableColumn
cApsChanConfigIfIndex=_CApsChanConfigIfIndex_Object((1,3,6,1,4,1,9,10,71,1,4,1,4),_CApsChanConfigIfIndex_Type())
cApsChanConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsChanConfigIfIndex.setStatus(_A)
class _CApsChanConfigPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_CApsChanConfigPriority_Type.__name__=_D
_CApsChanConfigPriority_Object=MibTableColumn
cApsChanConfigPriority=_CApsChanConfigPriority_Object((1,3,6,1,4,1,9,10,71,1,4,1,5),_CApsChanConfigPriority_Type())
cApsChanConfigPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:cApsChanConfigPriority.setStatus(_A)
_CApsCommandTable_Object=MibTable
cApsCommandTable=_CApsCommandTable_Object((1,3,6,1,4,1,9,10,71,1,5))
if mibBuilder.loadTexts:cApsCommandTable.setStatus(_A)
_CApsCommandEntry_Object=MibTableRow
cApsCommandEntry=_CApsCommandEntry_Object((1,3,6,1,4,1,9,10,71,1,5,1))
cApsCommandEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:cApsCommandEntry.setStatus(_A)
_CApsCommandSwitch_Type=CApsSwitchCommand
_CApsCommandSwitch_Object=MibTableColumn
cApsCommandSwitch=_CApsCommandSwitch_Object((1,3,6,1,4,1,9,10,71,1,5,1,1),_CApsCommandSwitch_Type())
cApsCommandSwitch.setMaxAccess(_U)
if mibBuilder.loadTexts:cApsCommandSwitch.setStatus(_A)
_CApsCommandControl_Type=CApsControlCommand
_CApsCommandControl_Object=MibTableColumn
cApsCommandControl=_CApsCommandControl_Object((1,3,6,1,4,1,9,10,71,1,5,1,2),_CApsCommandControl_Type())
cApsCommandControl.setMaxAccess(_U)
if mibBuilder.loadTexts:cApsCommandControl.setStatus(_A)
_CApsChanStatusTable_Object=MibTable
cApsChanStatusTable=_CApsChanStatusTable_Object((1,3,6,1,4,1,9,10,71,1,6))
if mibBuilder.loadTexts:cApsChanStatusTable.setStatus(_A)
_CApsChanStatusEntry_Object=MibTableRow
cApsChanStatusEntry=_CApsChanStatusEntry_Object((1,3,6,1,4,1,9,10,71,1,6,1))
cApsChanStatusEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:cApsChanStatusEntry.setStatus(_A)
class _CApsChanStatusCurrent_Type(Bits):namedValues=NamedValues(*(('lockedOut',0),('sd',1),('sf',2),('switched',3)))
_CApsChanStatusCurrent_Type.__name__=_K
_CApsChanStatusCurrent_Object=MibTableColumn
cApsChanStatusCurrent=_CApsChanStatusCurrent_Object((1,3,6,1,4,1,9,10,71,1,6,1,1),_CApsChanStatusCurrent_Type())
cApsChanStatusCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsChanStatusCurrent.setStatus(_A)
_CApsChanStatusSignalDegrades_Type=Counter32
_CApsChanStatusSignalDegrades_Object=MibTableColumn
cApsChanStatusSignalDegrades=_CApsChanStatusSignalDegrades_Object((1,3,6,1,4,1,9,10,71,1,6,1,2),_CApsChanStatusSignalDegrades_Type())
cApsChanStatusSignalDegrades.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsChanStatusSignalDegrades.setStatus(_A)
_CApsChanStatusSignalFailures_Type=Counter32
_CApsChanStatusSignalFailures_Object=MibTableColumn
cApsChanStatusSignalFailures=_CApsChanStatusSignalFailures_Object((1,3,6,1,4,1,9,10,71,1,6,1,3),_CApsChanStatusSignalFailures_Type())
cApsChanStatusSignalFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsChanStatusSignalFailures.setStatus(_A)
_CApsChanStatusSwitchovers_Type=Counter32
_CApsChanStatusSwitchovers_Object=MibTableColumn
cApsChanStatusSwitchovers=_CApsChanStatusSwitchovers_Object((1,3,6,1,4,1,9,10,71,1,6,1,4),_CApsChanStatusSwitchovers_Type())
cApsChanStatusSwitchovers.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsChanStatusSwitchovers.setStatus(_A)
_CApsChanStatusLastSwitchover_Type=TimeStamp
_CApsChanStatusLastSwitchover_Object=MibTableColumn
cApsChanStatusLastSwitchover=_CApsChanStatusLastSwitchover_Object((1,3,6,1,4,1,9,10,71,1,6,1,5),_CApsChanStatusLastSwitchover_Type())
cApsChanStatusLastSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsChanStatusLastSwitchover.setStatus(_A)
_CApsChanStatusSwitchoverSeconds_Type=Counter32
_CApsChanStatusSwitchoverSeconds_Object=MibTableColumn
cApsChanStatusSwitchoverSeconds=_CApsChanStatusSwitchoverSeconds_Object((1,3,6,1,4,1,9,10,71,1,6,1,6),_CApsChanStatusSwitchoverSeconds_Type())
cApsChanStatusSwitchoverSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:cApsChanStatusSwitchoverSeconds.setStatus(_A)
_CApsMIBNotifications_ObjectIdentity=ObjectIdentity
cApsMIBNotifications=_CApsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,71,2))
_CApsNotificationsPrefix_ObjectIdentity=ObjectIdentity
cApsNotificationsPrefix=_CApsNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,71,2,0))
_CApsMIBConformance_ObjectIdentity=ObjectIdentity
cApsMIBConformance=_CApsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,71,3))
_CApsGroups_ObjectIdentity=ObjectIdentity
cApsGroups=_CApsGroups_ObjectIdentity((1,3,6,1,4,1,9,10,71,3,1))
_CApsCompliances_ObjectIdentity=ObjectIdentity
cApsCompliances=_CApsCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,71,3,2))
cApsConfigGeneral=ObjectGroup((1,3,6,1,4,1,9,10,71,3,1,1))
cApsConfigGeneral.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:cApsConfigGeneral.setStatus(_A)
cApsConfigWtr=ObjectGroup((1,3,6,1,4,1,9,10,71,3,1,2))
cApsConfigWtr.setObjects((_B,_d))
if mibBuilder.loadTexts:cApsConfigWtr.setStatus(_A)
cApsCommandOnePlusOne=ObjectGroup((1,3,6,1,4,1,9,10,71,3,1,3))
cApsCommandOnePlusOne.setObjects((_B,_M))
if mibBuilder.loadTexts:cApsCommandOnePlusOne.setStatus(_A)
cApsCommandOneToN=ObjectGroup((1,3,6,1,4,1,9,10,71,3,1,4))
cApsCommandOneToN.setObjects(*((_B,_M),(_B,_e)))
if mibBuilder.loadTexts:cApsCommandOneToN.setStatus(_A)
cApsStatusGeneral=ObjectGroup((1,3,6,1,4,1,9,10,71,3,1,5))
cApsStatusGeneral.setObjects(*((_B,_f),(_B,_g),(_B,_F),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_h)))
if mibBuilder.loadTexts:cApsStatusGeneral.setStatus(_A)
cApsChanGeneral=ObjectGroup((1,3,6,1,4,1,9,10,71,3,1,6))
cApsChanGeneral.setObjects(*((_B,_i),(_B,_j),(_B,_R),(_B,_k),(_B,_l),(_B,_S),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:cApsChanGeneral.setStatus(_A)
cApsChanOneToN=ObjectGroup((1,3,6,1,4,1,9,10,71,3,1,7))
cApsChanOneToN.setObjects((_B,_o))
if mibBuilder.loadTexts:cApsChanOneToN.setStatus(_A)
cApsTotalsGroup=ObjectGroup((1,3,6,1,4,1,9,10,71,3,1,8))
cApsTotalsGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cApsTotalsGroup.setStatus(_A)
cApsMapGroup=ObjectGroup((1,3,6,1,4,1,9,10,71,3,1,9))
cApsMapGroup.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:cApsMapGroup.setStatus(_A)
cApsEventSwitchover=NotificationType((1,3,6,1,4,1,9,10,71,2,0,1))
cApsEventSwitchover.setObjects(*((_B,_S),(_B,_R)))
if mibBuilder.loadTexts:cApsEventSwitchover.setStatus(_A)
cApsEventModeMismatch=NotificationType((1,3,6,1,4,1,9,10,71,2,0,2))
cApsEventModeMismatch.setObjects(*((_B,_N),(_B,_F)))
if mibBuilder.loadTexts:cApsEventModeMismatch.setStatus(_A)
cApsEventChannelMismatch=NotificationType((1,3,6,1,4,1,9,10,71,2,0,3))
cApsEventChannelMismatch.setObjects(*((_B,_O),(_B,_F)))
if mibBuilder.loadTexts:cApsEventChannelMismatch.setStatus(_A)
cApsEventPSBF=NotificationType((1,3,6,1,4,1,9,10,71,2,0,4))
cApsEventPSBF.setObjects(*((_B,_P),(_B,_F)))
if mibBuilder.loadTexts:cApsEventPSBF.setStatus(_A)
cApsEventFEPLF=NotificationType((1,3,6,1,4,1,9,10,71,2,0,5))
cApsEventFEPLF.setObjects(*((_B,_Q),(_B,_F)))
if mibBuilder.loadTexts:cApsEventFEPLF.setStatus(_A)
cApsEventOptional=NotificationGroup((1,3,6,1,4,1,9,10,71,3,1,10))
cApsEventOptional.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:cApsEventOptional.setStatus(_A)
cApsCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,71,3,2,1))
cApsCompliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:cApsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CApsK1K2':CApsK1K2,'CApsSwitchCommand':CApsSwitchCommand,'CApsControlCommand':CApsControlCommand,'cApsMIB':cApsMIB,'cApsMIBObjects':cApsMIBObjects,'cApsConfig':cApsConfig,_p:cApsConfigGroups,'cApsConfigTable':cApsConfigTable,'cApsConfigEntry':cApsConfigEntry,_L:cApsConfigName,_c:cApsConfigRowStatus,_V:cApsConfigMode,_W:cApsConfigRevert,_X:cApsConfigDirection,_Y:cApsConfigExtraTraffic,_Z:cApsConfigSdBerThreshold,_a:cApsConfigSfBerThreshold,_d:cApsConfigWaitToRestore,_b:cApsConfigCreationTime,'cApsStatusTable':cApsStatusTable,'cApsStatusEntry':cApsStatusEntry,_f:cApsStatusK1K2Rcv,_g:cApsStatusK1K2Trans,_F:cApsStatusCurrent,_N:cApsStatusModeMismatches,_O:cApsStatusChannelMismatches,_P:cApsStatusPSBFs,_Q:cApsStatusFEPLFs,_h:cApsStatusSwitchedChannel,'cApsMap':cApsMap,_q:cApsChanLTEs,'cApsMapTable':cApsMapTable,'cApsMapEntry':cApsMapEntry,_T:cApsMapIfIndex,_r:cApsMapGroupName,_s:cApsMapChanNumber,'cApsChanConfigTable':cApsChanConfigTable,'cApsChanConfigEntry':cApsChanConfigEntry,_I:cApsChanConfigGroupName,_J:cApsChanConfigNumber,_j:cApsChanConfigRowStatus,_i:cApsChanConfigIfIndex,_o:cApsChanConfigPriority,'cApsCommandTable':cApsCommandTable,'cApsCommandEntry':cApsCommandEntry,_M:cApsCommandSwitch,_e:cApsCommandControl,'cApsChanStatusTable':cApsChanStatusTable,'cApsChanStatusEntry':cApsChanStatusEntry,_R:cApsChanStatusCurrent,_k:cApsChanStatusSignalDegrades,_l:cApsChanStatusSignalFailures,_S:cApsChanStatusSwitchovers,_m:cApsChanStatusLastSwitchover,_n:cApsChanStatusSwitchoverSeconds,'cApsMIBNotifications':cApsMIBNotifications,'cApsNotificationsPrefix':cApsNotificationsPrefix,_t:cApsEventSwitchover,_u:cApsEventModeMismatch,_v:cApsEventChannelMismatch,_w:cApsEventPSBF,_x:cApsEventFEPLF,'cApsMIBConformance':cApsMIBConformance,'cApsGroups':cApsGroups,_y:cApsConfigGeneral,'cApsConfigWtr':cApsConfigWtr,'cApsCommandOnePlusOne':cApsCommandOnePlusOne,'cApsCommandOneToN':cApsCommandOneToN,_z:cApsStatusGeneral,_A0:cApsChanGeneral,'cApsChanOneToN':cApsChanOneToN,'cApsTotalsGroup':cApsTotalsGroup,'cApsMapGroup':cApsMapGroup,'cApsEventOptional':cApsEventOptional,'cApsCompliances':cApsCompliances,'cApsCompliance':cApsCompliance})