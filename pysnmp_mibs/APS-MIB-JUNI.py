_A0='junidApsChanGeneral'
_z='junidApsStatusGeneral'
_y='junidApsConfigGeneral'
_x='junidApsEventFEPLF'
_w='junidApsEventPSBF'
_v='junidApsEventChannelMismatch'
_u='junidApsEventModeMismatch'
_t='junidApsEventSwitchover'
_s='junidApsMapChanNumber'
_r='junidApsMapGroupName'
_q='junidApsChanLTEs'
_p='junidApsConfigGroups'
_o='junidApsChanConfigPriority'
_n='junidApsChanStatusSwitchoverSeconds'
_m='junidApsChanStatusLastSwitchover'
_l='junidApsChanStatusSignalFailures'
_k='junidApsChanStatusSignalDegrades'
_j='junidApsChanConfigRowStatus'
_i='junidApsChanConfigIfIndex'
_h='junidApsStatusSwitchedChannel'
_g='junidApsStatusK1K2Trans'
_f='junidApsStatusK1K2Rcv'
_e='junidApsCommandControl'
_d='junidApsConfigWaitToRestore'
_c='junidApsConfigRowStatus'
_b='junidApsConfigCreationTime'
_a='junidApsConfigSfBerThreshold'
_Z='junidApsConfigSdBerThreshold'
_Y='junidApsConfigExtraTraffic'
_X='junidApsConfigDirection'
_W='junidApsConfigRevert'
_V='junidApsConfigMode'
_U='read-write'
_T='junidApsMapIfIndex'
_S='junidApsChanStatusSwitchovers'
_R='junidApsChanStatusCurrent'
_Q='junidApsStatusFEPLFs'
_P='junidApsStatusPSBFs'
_O='junidApsStatusChannelMismatches'
_N='junidApsStatusModeMismatches'
_M='junidApsCommandSwitch'
_L='junidApsConfigName'
_K='Bits'
_J='junidApsChanConfigNumber'
_I='junidApsChanConfigGroupName'
_H='not-accessible'
_G='SnmpAdminString'
_F='junidApsStatusCurrent'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='APS-MIB-JUNI'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniSonetApsExperiment,=mibBuilder.importSymbols('Juniper-Experiment','juniSonetApsExperiment')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
junidApsMIB=ModuleIdentity((1,3,6,1,4,1,4874,3,2,2,1))
if mibBuilder.loadTexts:junidApsMIB.setRevisions(('2001-05-24 23:00',))
class JunidApsK1K2(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class JunidApsSwitchCommand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noCmd',1),('clear',2),('lockoutOfProtection',3),('forcedSwitchWorkToProtect',4),('forcedSwitchProtectToWork',5),('manualSwitchWorkToProtect',6),('manualSwitchProtectToWork',7),('exercise',8)))
class JunidApsControlCommand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noCmd',1),('lockoutWorkingChannel',2),('clearLockoutWorkingChannel',3)))
_JunidApsMIBObjects_ObjectIdentity=ObjectIdentity
junidApsMIBObjects=_JunidApsMIBObjects_ObjectIdentity((1,3,6,1,4,1,4874,3,2,2,1,1))
_JunidApsConfig_ObjectIdentity=ObjectIdentity
junidApsConfig=_JunidApsConfig_ObjectIdentity((1,3,6,1,4,1,4874,3,2,2,1,1,1))
_JunidApsConfigGroups_Type=Gauge32
_JunidApsConfigGroups_Object=MibScalar
junidApsConfigGroups=_JunidApsConfigGroups_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,1),_JunidApsConfigGroups_Type())
junidApsConfigGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsConfigGroups.setStatus(_A)
_JunidApsConfigTable_Object=MibTable
junidApsConfigTable=_JunidApsConfigTable_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2))
if mibBuilder.loadTexts:junidApsConfigTable.setStatus(_A)
_JunidApsConfigEntry_Object=MibTableRow
junidApsConfigEntry=_JunidApsConfigEntry_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2,1))
junidApsConfigEntry.setIndexNames((1,_B,_L))
if mibBuilder.loadTexts:junidApsConfigEntry.setStatus(_A)
class _JunidApsConfigName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_JunidApsConfigName_Type.__name__=_G
_JunidApsConfigName_Object=MibTableColumn
junidApsConfigName=_JunidApsConfigName_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2,1,1),_JunidApsConfigName_Type())
junidApsConfigName.setMaxAccess(_H)
if mibBuilder.loadTexts:junidApsConfigName.setStatus(_A)
_JunidApsConfigRowStatus_Type=RowStatus
_JunidApsConfigRowStatus_Object=MibTableColumn
junidApsConfigRowStatus=_JunidApsConfigRowStatus_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2,1,2),_JunidApsConfigRowStatus_Type())
junidApsConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:junidApsConfigRowStatus.setStatus(_A)
class _JunidApsConfigMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('onePlusOne',1),('oneToN',2),('onePlusOneCompatible',3),('onePlusOneOptimized',4)))
_JunidApsConfigMode_Type.__name__=_D
_JunidApsConfigMode_Object=MibTableColumn
junidApsConfigMode=_JunidApsConfigMode_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2,1,3),_JunidApsConfigMode_Type())
junidApsConfigMode.setMaxAccess(_E)
if mibBuilder.loadTexts:junidApsConfigMode.setStatus(_A)
class _JunidApsConfigRevert_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonrevertive',1),('revertive',2)))
_JunidApsConfigRevert_Type.__name__=_D
_JunidApsConfigRevert_Object=MibTableColumn
junidApsConfigRevert=_JunidApsConfigRevert_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2,1,4),_JunidApsConfigRevert_Type())
junidApsConfigRevert.setMaxAccess(_E)
if mibBuilder.loadTexts:junidApsConfigRevert.setStatus(_A)
class _JunidApsConfigDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
_JunidApsConfigDirection_Type.__name__=_D
_JunidApsConfigDirection_Object=MibTableColumn
junidApsConfigDirection=_JunidApsConfigDirection_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2,1,5),_JunidApsConfigDirection_Type())
junidApsConfigDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:junidApsConfigDirection.setStatus(_A)
class _JunidApsConfigExtraTraffic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_JunidApsConfigExtraTraffic_Type.__name__=_D
_JunidApsConfigExtraTraffic_Object=MibTableColumn
junidApsConfigExtraTraffic=_JunidApsConfigExtraTraffic_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2,1,6),_JunidApsConfigExtraTraffic_Type())
junidApsConfigExtraTraffic.setMaxAccess(_E)
if mibBuilder.loadTexts:junidApsConfigExtraTraffic.setStatus(_A)
class _JunidApsConfigSdBerThreshold_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,9))
_JunidApsConfigSdBerThreshold_Type.__name__=_D
_JunidApsConfigSdBerThreshold_Object=MibTableColumn
junidApsConfigSdBerThreshold=_JunidApsConfigSdBerThreshold_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2,1,7),_JunidApsConfigSdBerThreshold_Type())
junidApsConfigSdBerThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:junidApsConfigSdBerThreshold.setStatus(_A)
class _JunidApsConfigSfBerThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,5))
_JunidApsConfigSfBerThreshold_Type.__name__=_D
_JunidApsConfigSfBerThreshold_Object=MibTableColumn
junidApsConfigSfBerThreshold=_JunidApsConfigSfBerThreshold_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2,1,8),_JunidApsConfigSfBerThreshold_Type())
junidApsConfigSfBerThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:junidApsConfigSfBerThreshold.setStatus(_A)
class _JunidApsConfigWaitToRestore_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_JunidApsConfigWaitToRestore_Type.__name__=_D
_JunidApsConfigWaitToRestore_Object=MibTableColumn
junidApsConfigWaitToRestore=_JunidApsConfigWaitToRestore_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2,1,9),_JunidApsConfigWaitToRestore_Type())
junidApsConfigWaitToRestore.setMaxAccess(_E)
if mibBuilder.loadTexts:junidApsConfigWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:junidApsConfigWaitToRestore.setUnits('seconds')
_JunidApsConfigCreationTime_Type=TimeStamp
_JunidApsConfigCreationTime_Object=MibTableColumn
junidApsConfigCreationTime=_JunidApsConfigCreationTime_Object((1,3,6,1,4,1,4874,3,2,2,1,1,1,2,1,10),_JunidApsConfigCreationTime_Type())
junidApsConfigCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsConfigCreationTime.setStatus(_A)
_JunidApsStatusTable_Object=MibTable
junidApsStatusTable=_JunidApsStatusTable_Object((1,3,6,1,4,1,4874,3,2,2,1,1,2))
if mibBuilder.loadTexts:junidApsStatusTable.setStatus(_A)
_JunidApsStatusEntry_Object=MibTableRow
junidApsStatusEntry=_JunidApsStatusEntry_Object((1,3,6,1,4,1,4874,3,2,2,1,1,2,1))
junidApsStatusEntry.setIndexNames((1,_B,_L))
if mibBuilder.loadTexts:junidApsStatusEntry.setStatus(_A)
_JunidApsStatusK1K2Rcv_Type=JunidApsK1K2
_JunidApsStatusK1K2Rcv_Object=MibTableColumn
junidApsStatusK1K2Rcv=_JunidApsStatusK1K2Rcv_Object((1,3,6,1,4,1,4874,3,2,2,1,1,2,1,1),_JunidApsStatusK1K2Rcv_Type())
junidApsStatusK1K2Rcv.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsStatusK1K2Rcv.setStatus(_A)
_JunidApsStatusK1K2Trans_Type=JunidApsK1K2
_JunidApsStatusK1K2Trans_Object=MibTableColumn
junidApsStatusK1K2Trans=_JunidApsStatusK1K2Trans_Object((1,3,6,1,4,1,4874,3,2,2,1,1,2,1,2),_JunidApsStatusK1K2Trans_Type())
junidApsStatusK1K2Trans.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsStatusK1K2Trans.setStatus(_A)
class _JunidApsStatusCurrent_Type(Bits):namedValues=NamedValues(*(('modeMismatch',0),('channelMismatch',1),('psbf',2),('feplf',3),('extraTraffic',4)))
_JunidApsStatusCurrent_Type.__name__=_K
_JunidApsStatusCurrent_Object=MibTableColumn
junidApsStatusCurrent=_JunidApsStatusCurrent_Object((1,3,6,1,4,1,4874,3,2,2,1,1,2,1,3),_JunidApsStatusCurrent_Type())
junidApsStatusCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsStatusCurrent.setStatus(_A)
_JunidApsStatusModeMismatches_Type=Counter32
_JunidApsStatusModeMismatches_Object=MibTableColumn
junidApsStatusModeMismatches=_JunidApsStatusModeMismatches_Object((1,3,6,1,4,1,4874,3,2,2,1,1,2,1,4),_JunidApsStatusModeMismatches_Type())
junidApsStatusModeMismatches.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsStatusModeMismatches.setStatus(_A)
_JunidApsStatusChannelMismatches_Type=Counter32
_JunidApsStatusChannelMismatches_Object=MibTableColumn
junidApsStatusChannelMismatches=_JunidApsStatusChannelMismatches_Object((1,3,6,1,4,1,4874,3,2,2,1,1,2,1,5),_JunidApsStatusChannelMismatches_Type())
junidApsStatusChannelMismatches.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsStatusChannelMismatches.setStatus(_A)
_JunidApsStatusPSBFs_Type=Counter32
_JunidApsStatusPSBFs_Object=MibTableColumn
junidApsStatusPSBFs=_JunidApsStatusPSBFs_Object((1,3,6,1,4,1,4874,3,2,2,1,1,2,1,6),_JunidApsStatusPSBFs_Type())
junidApsStatusPSBFs.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsStatusPSBFs.setStatus(_A)
_JunidApsStatusFEPLFs_Type=Counter32
_JunidApsStatusFEPLFs_Object=MibTableColumn
junidApsStatusFEPLFs=_JunidApsStatusFEPLFs_Object((1,3,6,1,4,1,4874,3,2,2,1,1,2,1,7),_JunidApsStatusFEPLFs_Type())
junidApsStatusFEPLFs.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsStatusFEPLFs.setStatus(_A)
_JunidApsStatusSwitchedChannel_Type=Integer32
_JunidApsStatusSwitchedChannel_Object=MibTableColumn
junidApsStatusSwitchedChannel=_JunidApsStatusSwitchedChannel_Object((1,3,6,1,4,1,4874,3,2,2,1,1,2,1,8),_JunidApsStatusSwitchedChannel_Type())
junidApsStatusSwitchedChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsStatusSwitchedChannel.setStatus(_A)
_JunidApsMap_ObjectIdentity=ObjectIdentity
junidApsMap=_JunidApsMap_ObjectIdentity((1,3,6,1,4,1,4874,3,2,2,1,1,3))
_JunidApsChanLTEs_Type=Gauge32
_JunidApsChanLTEs_Object=MibScalar
junidApsChanLTEs=_JunidApsChanLTEs_Object((1,3,6,1,4,1,4874,3,2,2,1,1,3,1),_JunidApsChanLTEs_Type())
junidApsChanLTEs.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsChanLTEs.setStatus(_A)
_JunidApsMapTable_Object=MibTable
junidApsMapTable=_JunidApsMapTable_Object((1,3,6,1,4,1,4874,3,2,2,1,1,3,2))
if mibBuilder.loadTexts:junidApsMapTable.setStatus(_A)
_JunidApsMapEntry_Object=MibTableRow
junidApsMapEntry=_JunidApsMapEntry_Object((1,3,6,1,4,1,4874,3,2,2,1,1,3,2,1))
junidApsMapEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:junidApsMapEntry.setStatus(_A)
_JunidApsMapIfIndex_Type=InterfaceIndex
_JunidApsMapIfIndex_Object=MibTableColumn
junidApsMapIfIndex=_JunidApsMapIfIndex_Object((1,3,6,1,4,1,4874,3,2,2,1,1,3,2,1,1),_JunidApsMapIfIndex_Type())
junidApsMapIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:junidApsMapIfIndex.setStatus(_A)
class _JunidApsMapGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JunidApsMapGroupName_Type.__name__=_G
_JunidApsMapGroupName_Object=MibTableColumn
junidApsMapGroupName=_JunidApsMapGroupName_Object((1,3,6,1,4,1,4874,3,2,2,1,1,3,2,1,2),_JunidApsMapGroupName_Type())
junidApsMapGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsMapGroupName.setStatus(_A)
class _JunidApsMapChanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,14))
_JunidApsMapChanNumber_Type.__name__=_D
_JunidApsMapChanNumber_Object=MibTableColumn
junidApsMapChanNumber=_JunidApsMapChanNumber_Object((1,3,6,1,4,1,4874,3,2,2,1,1,3,2,1,3),_JunidApsMapChanNumber_Type())
junidApsMapChanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsMapChanNumber.setStatus(_A)
_JunidApsChanConfigTable_Object=MibTable
junidApsChanConfigTable=_JunidApsChanConfigTable_Object((1,3,6,1,4,1,4874,3,2,2,1,1,4))
if mibBuilder.loadTexts:junidApsChanConfigTable.setStatus(_A)
_JunidApsChanConfigEntry_Object=MibTableRow
junidApsChanConfigEntry=_JunidApsChanConfigEntry_Object((1,3,6,1,4,1,4874,3,2,2,1,1,4,1))
junidApsChanConfigEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:junidApsChanConfigEntry.setStatus(_A)
class _JunidApsChanConfigGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_JunidApsChanConfigGroupName_Type.__name__=_G
_JunidApsChanConfigGroupName_Object=MibTableColumn
junidApsChanConfigGroupName=_JunidApsChanConfigGroupName_Object((1,3,6,1,4,1,4874,3,2,2,1,1,4,1,1),_JunidApsChanConfigGroupName_Type())
junidApsChanConfigGroupName.setMaxAccess(_H)
if mibBuilder.loadTexts:junidApsChanConfigGroupName.setStatus(_A)
class _JunidApsChanConfigNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_JunidApsChanConfigNumber_Type.__name__=_D
_JunidApsChanConfigNumber_Object=MibTableColumn
junidApsChanConfigNumber=_JunidApsChanConfigNumber_Object((1,3,6,1,4,1,4874,3,2,2,1,1,4,1,2),_JunidApsChanConfigNumber_Type())
junidApsChanConfigNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:junidApsChanConfigNumber.setStatus(_A)
_JunidApsChanConfigRowStatus_Type=RowStatus
_JunidApsChanConfigRowStatus_Object=MibTableColumn
junidApsChanConfigRowStatus=_JunidApsChanConfigRowStatus_Object((1,3,6,1,4,1,4874,3,2,2,1,1,4,1,3),_JunidApsChanConfigRowStatus_Type())
junidApsChanConfigRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:junidApsChanConfigRowStatus.setStatus(_A)
_JunidApsChanConfigIfIndex_Type=InterfaceIndex
_JunidApsChanConfigIfIndex_Object=MibTableColumn
junidApsChanConfigIfIndex=_JunidApsChanConfigIfIndex_Object((1,3,6,1,4,1,4874,3,2,2,1,1,4,1,4),_JunidApsChanConfigIfIndex_Type())
junidApsChanConfigIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:junidApsChanConfigIfIndex.setStatus(_A)
class _JunidApsChanConfigPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_JunidApsChanConfigPriority_Type.__name__=_D
_JunidApsChanConfigPriority_Object=MibTableColumn
junidApsChanConfigPriority=_JunidApsChanConfigPriority_Object((1,3,6,1,4,1,4874,3,2,2,1,1,4,1,5),_JunidApsChanConfigPriority_Type())
junidApsChanConfigPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:junidApsChanConfigPriority.setStatus(_A)
_JunidApsCommandTable_Object=MibTable
junidApsCommandTable=_JunidApsCommandTable_Object((1,3,6,1,4,1,4874,3,2,2,1,1,5))
if mibBuilder.loadTexts:junidApsCommandTable.setStatus(_A)
_JunidApsCommandEntry_Object=MibTableRow
junidApsCommandEntry=_JunidApsCommandEntry_Object((1,3,6,1,4,1,4874,3,2,2,1,1,5,1))
junidApsCommandEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:junidApsCommandEntry.setStatus(_A)
_JunidApsCommandSwitch_Type=JunidApsSwitchCommand
_JunidApsCommandSwitch_Object=MibTableColumn
junidApsCommandSwitch=_JunidApsCommandSwitch_Object((1,3,6,1,4,1,4874,3,2,2,1,1,5,1,1),_JunidApsCommandSwitch_Type())
junidApsCommandSwitch.setMaxAccess(_U)
if mibBuilder.loadTexts:junidApsCommandSwitch.setStatus(_A)
_JunidApsCommandControl_Type=JunidApsControlCommand
_JunidApsCommandControl_Object=MibTableColumn
junidApsCommandControl=_JunidApsCommandControl_Object((1,3,6,1,4,1,4874,3,2,2,1,1,5,1,2),_JunidApsCommandControl_Type())
junidApsCommandControl.setMaxAccess(_U)
if mibBuilder.loadTexts:junidApsCommandControl.setStatus(_A)
_JunidApsChanStatusTable_Object=MibTable
junidApsChanStatusTable=_JunidApsChanStatusTable_Object((1,3,6,1,4,1,4874,3,2,2,1,1,6))
if mibBuilder.loadTexts:junidApsChanStatusTable.setStatus(_A)
_JunidApsChanStatusEntry_Object=MibTableRow
junidApsChanStatusEntry=_JunidApsChanStatusEntry_Object((1,3,6,1,4,1,4874,3,2,2,1,1,6,1))
junidApsChanStatusEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:junidApsChanStatusEntry.setStatus(_A)
class _JunidApsChanStatusCurrent_Type(Bits):namedValues=NamedValues(*(('lockedOut',0),('sd',1),('sf',2),('switched',3)))
_JunidApsChanStatusCurrent_Type.__name__=_K
_JunidApsChanStatusCurrent_Object=MibTableColumn
junidApsChanStatusCurrent=_JunidApsChanStatusCurrent_Object((1,3,6,1,4,1,4874,3,2,2,1,1,6,1,1),_JunidApsChanStatusCurrent_Type())
junidApsChanStatusCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsChanStatusCurrent.setStatus(_A)
_JunidApsChanStatusSignalDegrades_Type=Counter32
_JunidApsChanStatusSignalDegrades_Object=MibTableColumn
junidApsChanStatusSignalDegrades=_JunidApsChanStatusSignalDegrades_Object((1,3,6,1,4,1,4874,3,2,2,1,1,6,1,2),_JunidApsChanStatusSignalDegrades_Type())
junidApsChanStatusSignalDegrades.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsChanStatusSignalDegrades.setStatus(_A)
_JunidApsChanStatusSignalFailures_Type=Counter32
_JunidApsChanStatusSignalFailures_Object=MibTableColumn
junidApsChanStatusSignalFailures=_JunidApsChanStatusSignalFailures_Object((1,3,6,1,4,1,4874,3,2,2,1,1,6,1,3),_JunidApsChanStatusSignalFailures_Type())
junidApsChanStatusSignalFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsChanStatusSignalFailures.setStatus(_A)
_JunidApsChanStatusSwitchovers_Type=Counter32
_JunidApsChanStatusSwitchovers_Object=MibTableColumn
junidApsChanStatusSwitchovers=_JunidApsChanStatusSwitchovers_Object((1,3,6,1,4,1,4874,3,2,2,1,1,6,1,4),_JunidApsChanStatusSwitchovers_Type())
junidApsChanStatusSwitchovers.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsChanStatusSwitchovers.setStatus(_A)
_JunidApsChanStatusLastSwitchover_Type=TimeStamp
_JunidApsChanStatusLastSwitchover_Object=MibTableColumn
junidApsChanStatusLastSwitchover=_JunidApsChanStatusLastSwitchover_Object((1,3,6,1,4,1,4874,3,2,2,1,1,6,1,5),_JunidApsChanStatusLastSwitchover_Type())
junidApsChanStatusLastSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsChanStatusLastSwitchover.setStatus(_A)
_JunidApsChanStatusSwitchoverSeconds_Type=Counter32
_JunidApsChanStatusSwitchoverSeconds_Object=MibTableColumn
junidApsChanStatusSwitchoverSeconds=_JunidApsChanStatusSwitchoverSeconds_Object((1,3,6,1,4,1,4874,3,2,2,1,1,6,1,6),_JunidApsChanStatusSwitchoverSeconds_Type())
junidApsChanStatusSwitchoverSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:junidApsChanStatusSwitchoverSeconds.setStatus(_A)
_JunidApsMIBNotifications_ObjectIdentity=ObjectIdentity
junidApsMIBNotifications=_JunidApsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,4874,3,2,2,1,2))
_JunidApsNotificationsPrefix_ObjectIdentity=ObjectIdentity
junidApsNotificationsPrefix=_JunidApsNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,4874,3,2,2,1,2,0))
_JunidApsMIBConformance_ObjectIdentity=ObjectIdentity
junidApsMIBConformance=_JunidApsMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,3,2,2,1,3))
_JunidApsGroups_ObjectIdentity=ObjectIdentity
junidApsGroups=_JunidApsGroups_ObjectIdentity((1,3,6,1,4,1,4874,3,2,2,1,3,1))
_JunidApsCompliances_ObjectIdentity=ObjectIdentity
junidApsCompliances=_JunidApsCompliances_ObjectIdentity((1,3,6,1,4,1,4874,3,2,2,1,3,2))
junidApsConfigGeneral=ObjectGroup((1,3,6,1,4,1,4874,3,2,2,1,3,1,1))
junidApsConfigGeneral.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:junidApsConfigGeneral.setStatus(_A)
junidApsConfigWtr=ObjectGroup((1,3,6,1,4,1,4874,3,2,2,1,3,1,2))
junidApsConfigWtr.setObjects((_B,_d))
if mibBuilder.loadTexts:junidApsConfigWtr.setStatus(_A)
junidApsCommandOnePlusOne=ObjectGroup((1,3,6,1,4,1,4874,3,2,2,1,3,1,3))
junidApsCommandOnePlusOne.setObjects((_B,_M))
if mibBuilder.loadTexts:junidApsCommandOnePlusOne.setStatus(_A)
junidApsCommandOneToN=ObjectGroup((1,3,6,1,4,1,4874,3,2,2,1,3,1,4))
junidApsCommandOneToN.setObjects(*((_B,_M),(_B,_e)))
if mibBuilder.loadTexts:junidApsCommandOneToN.setStatus(_A)
junidApsStatusGeneral=ObjectGroup((1,3,6,1,4,1,4874,3,2,2,1,3,1,5))
junidApsStatusGeneral.setObjects(*((_B,_f),(_B,_g),(_B,_F),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_h)))
if mibBuilder.loadTexts:junidApsStatusGeneral.setStatus(_A)
junidApsChanGeneral=ObjectGroup((1,3,6,1,4,1,4874,3,2,2,1,3,1,6))
junidApsChanGeneral.setObjects(*((_B,_i),(_B,_j),(_B,_R),(_B,_k),(_B,_l),(_B,_S),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:junidApsChanGeneral.setStatus(_A)
junidApsChanOneToN=ObjectGroup((1,3,6,1,4,1,4874,3,2,2,1,3,1,7))
junidApsChanOneToN.setObjects((_B,_o))
if mibBuilder.loadTexts:junidApsChanOneToN.setStatus(_A)
junidApsTotalsGroup=ObjectGroup((1,3,6,1,4,1,4874,3,2,2,1,3,1,8))
junidApsTotalsGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:junidApsTotalsGroup.setStatus(_A)
junidApsMapGroup=ObjectGroup((1,3,6,1,4,1,4874,3,2,2,1,3,1,9))
junidApsMapGroup.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:junidApsMapGroup.setStatus(_A)
junidApsEventSwitchover=NotificationType((1,3,6,1,4,1,4874,3,2,2,1,2,0,1))
junidApsEventSwitchover.setObjects(*((_B,_S),(_B,_R)))
if mibBuilder.loadTexts:junidApsEventSwitchover.setStatus(_A)
junidApsEventModeMismatch=NotificationType((1,3,6,1,4,1,4874,3,2,2,1,2,0,2))
junidApsEventModeMismatch.setObjects(*((_B,_N),(_B,_F)))
if mibBuilder.loadTexts:junidApsEventModeMismatch.setStatus(_A)
junidApsEventChannelMismatch=NotificationType((1,3,6,1,4,1,4874,3,2,2,1,2,0,3))
junidApsEventChannelMismatch.setObjects(*((_B,_O),(_B,_F)))
if mibBuilder.loadTexts:junidApsEventChannelMismatch.setStatus(_A)
junidApsEventPSBF=NotificationType((1,3,6,1,4,1,4874,3,2,2,1,2,0,4))
junidApsEventPSBF.setObjects(*((_B,_P),(_B,_F)))
if mibBuilder.loadTexts:junidApsEventPSBF.setStatus(_A)
junidApsEventFEPLF=NotificationType((1,3,6,1,4,1,4874,3,2,2,1,2,0,5))
junidApsEventFEPLF.setObjects(*((_B,_Q),(_B,_F)))
if mibBuilder.loadTexts:junidApsEventFEPLF.setStatus(_A)
junidApsEventOptional=NotificationGroup((1,3,6,1,4,1,4874,3,2,2,1,3,1,10))
junidApsEventOptional.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:junidApsEventOptional.setStatus(_A)
junidApsCompliance=ModuleCompliance((1,3,6,1,4,1,4874,3,2,2,1,3,2,1))
junidApsCompliance.setObjects(*((_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:junidApsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'JunidApsK1K2':JunidApsK1K2,'JunidApsSwitchCommand':JunidApsSwitchCommand,'JunidApsControlCommand':JunidApsControlCommand,'junidApsMIB':junidApsMIB,'junidApsMIBObjects':junidApsMIBObjects,'junidApsConfig':junidApsConfig,_p:junidApsConfigGroups,'junidApsConfigTable':junidApsConfigTable,'junidApsConfigEntry':junidApsConfigEntry,_L:junidApsConfigName,_c:junidApsConfigRowStatus,_V:junidApsConfigMode,_W:junidApsConfigRevert,_X:junidApsConfigDirection,_Y:junidApsConfigExtraTraffic,_Z:junidApsConfigSdBerThreshold,_a:junidApsConfigSfBerThreshold,_d:junidApsConfigWaitToRestore,_b:junidApsConfigCreationTime,'junidApsStatusTable':junidApsStatusTable,'junidApsStatusEntry':junidApsStatusEntry,_f:junidApsStatusK1K2Rcv,_g:junidApsStatusK1K2Trans,_F:junidApsStatusCurrent,_N:junidApsStatusModeMismatches,_O:junidApsStatusChannelMismatches,_P:junidApsStatusPSBFs,_Q:junidApsStatusFEPLFs,_h:junidApsStatusSwitchedChannel,'junidApsMap':junidApsMap,_q:junidApsChanLTEs,'junidApsMapTable':junidApsMapTable,'junidApsMapEntry':junidApsMapEntry,_T:junidApsMapIfIndex,_r:junidApsMapGroupName,_s:junidApsMapChanNumber,'junidApsChanConfigTable':junidApsChanConfigTable,'junidApsChanConfigEntry':junidApsChanConfigEntry,_I:junidApsChanConfigGroupName,_J:junidApsChanConfigNumber,_j:junidApsChanConfigRowStatus,_i:junidApsChanConfigIfIndex,_o:junidApsChanConfigPriority,'junidApsCommandTable':junidApsCommandTable,'junidApsCommandEntry':junidApsCommandEntry,_M:junidApsCommandSwitch,_e:junidApsCommandControl,'junidApsChanStatusTable':junidApsChanStatusTable,'junidApsChanStatusEntry':junidApsChanStatusEntry,_R:junidApsChanStatusCurrent,_k:junidApsChanStatusSignalDegrades,_l:junidApsChanStatusSignalFailures,_S:junidApsChanStatusSwitchovers,_m:junidApsChanStatusLastSwitchover,_n:junidApsChanStatusSwitchoverSeconds,'junidApsMIBNotifications':junidApsMIBNotifications,'junidApsNotificationsPrefix':junidApsNotificationsPrefix,_t:junidApsEventSwitchover,_u:junidApsEventModeMismatch,_v:junidApsEventChannelMismatch,_w:junidApsEventPSBF,_x:junidApsEventFEPLF,'junidApsMIBConformance':junidApsMIBConformance,'junidApsGroups':junidApsGroups,_y:junidApsConfigGeneral,'junidApsConfigWtr':junidApsConfigWtr,'junidApsCommandOnePlusOne':junidApsCommandOnePlusOne,'junidApsCommandOneToN':junidApsCommandOneToN,_z:junidApsStatusGeneral,_A0:junidApsChanGeneral,'junidApsChanOneToN':junidApsChanOneToN,'junidApsTotalsGroup':junidApsTotalsGroup,'junidApsMapGroup':junidApsMapGroup,'junidApsEventOptional':junidApsEventOptional,'junidApsCompliances':junidApsCompliances,'junidApsCompliance':junidApsCompliance})