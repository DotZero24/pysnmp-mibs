_A7='alaErpNotificationGroup'
_A6='alaErpRingAttributesGroup'
_A5='alaErpGlobalGroup'
_A4='alaErpRingPortStatusChanged'
_A3='alaErpRingRemoved'
_A2='alaErpRingMultipleRpl'
_A1='alaErpRingStateChanged'
_A0='alaErpRingResetVersionFallback'
_z='alaErpRingActiveVersion'
_y='alaErpStatsPDUErr'
_x='alaErpStatsRPLBlockPDUDrop'
_w='alaErpStatsRPLBlockPDURx'
_v='alaErpStatsRPLBlockPDUTx'
_u='alaErpStatsNoRequestPduDrop'
_t='alaErpStatsNoRequestPduRx'
_s='alaErpStatsNoRequestPduTx'
_r='alaErpStatsSignalFailPduDrop'
_q='alaErpStatsSignalFailPduRx'
_p='alaErpStatsSignalFailPduTx'
_o='alaErpRingVlanRowStatus'
_n='alaErpRingPortRmepId'
_m='alaErpRingPortClearStats'
_l='alaErpRingPortEthOAMEvent'
_k='alaErpRingPortType'
_j='alaErpRingClearAction'
_i='alaErpRingRevertive'
_h='alaErpRingVirtualChannel'
_g='alaErpRingRowStatus'
_f='alaErpRingTimeToRevert'
_e='alaErpRingLastStateChange'
_d='alaErpRingClearStats'
_c='alaErpRingGuardTimer'
_b='alaErpRingWaitToRestoreTimer'
_a='alaErpRingStatus'
_Z='alaErpRingPort2'
_Y='alaErpRingPort1'
_X='alaErpRingMEGLevel'
_W='alaErpRingServiceVid'
_V='alaErpClearStats'
_U='alaErpStatsEntry'
_T='alaErpRingVlanProtectedVid'
_S='AlaErpRingPortType'
_R='AlaErpRingPortStatus'
_Q='accessible-for-notify'
_P='TruthValue'
_O='alaErpRingPortStatus'
_N='alaErpRingState'
_M='alaErpRingPortIfIndex'
_L='disabled'
_K='enabled'
_J='Unsigned32'
_I='read-write'
_H='reset'
_G='default'
_F='alaErpRingId'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='ALCATEL-IND1-ERP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Erp,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1Erp')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_P)
alcatelIND1ERPMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,46,1))
if mibBuilder.loadTexts:alcatelIND1ERPMIB.setRevisions(('2008-07-10 00:00',))
class AlaErpRingPortStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('blocking',2)))
class AlaErpRingPortType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonRpl',1),('rpl',2)))
class AlaErpRingMepId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
class AlaErpRingMEGLevel(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AlcatelIND1ERPMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1ERPMIBObjects=_AlcatelIND1ERPMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,46,1,1))
if mibBuilder.loadTexts:alcatelIND1ERPMIBObjects.setStatus(_A)
_AlaErpGlobal_ObjectIdentity=ObjectIdentity
alaErpGlobal=_AlaErpGlobal_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,1))
class _AlaErpClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_AlaErpClearStats_Type.__name__=_E
_AlaErpClearStats_Object=MibScalar
alaErpClearStats=_AlaErpClearStats_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,1,1),_AlaErpClearStats_Type())
alaErpClearStats.setMaxAccess(_I)
if mibBuilder.loadTexts:alaErpClearStats.setStatus(_A)
_AlaErpRingAttributes_ObjectIdentity=ObjectIdentity
alaErpRingAttributes=_AlaErpRingAttributes_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2))
_AlaErpRingTable_Object=MibTable
alaErpRingTable=_AlaErpRingTable_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1))
if mibBuilder.loadTexts:alaErpRingTable.setStatus(_A)
_AlaErpRingEntry_Object=MibTableRow
alaErpRingEntry=_AlaErpRingEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1))
alaErpRingEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:alaErpRingEntry.setStatus(_A)
class _AlaErpRingId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaErpRingId_Type.__name__=_E
_AlaErpRingId_Object=MibTableColumn
alaErpRingId=_AlaErpRingId_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,1),_AlaErpRingId_Type())
alaErpRingId.setMaxAccess(_Q)
if mibBuilder.loadTexts:alaErpRingId.setStatus(_A)
_AlaErpRingServiceVid_Type=VlanId
_AlaErpRingServiceVid_Object=MibTableColumn
alaErpRingServiceVid=_AlaErpRingServiceVid_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,2),_AlaErpRingServiceVid_Type())
alaErpRingServiceVid.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingServiceVid.setStatus(_A)
_AlaErpRingMEGLevel_Type=AlaErpRingMEGLevel
_AlaErpRingMEGLevel_Object=MibTableColumn
alaErpRingMEGLevel=_AlaErpRingMEGLevel_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,3),_AlaErpRingMEGLevel_Type())
alaErpRingMEGLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingMEGLevel.setStatus(_A)
_AlaErpRingPort1_Type=InterfaceIndex
_AlaErpRingPort1_Object=MibTableColumn
alaErpRingPort1=_AlaErpRingPort1_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,4),_AlaErpRingPort1_Type())
alaErpRingPort1.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingPort1.setStatus(_A)
_AlaErpRingPort2_Type=InterfaceIndexOrZero
_AlaErpRingPort2_Object=MibTableColumn
alaErpRingPort2=_AlaErpRingPort2_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,5),_AlaErpRingPort2_Type())
alaErpRingPort2.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingPort2.setStatus(_A)
class _AlaErpRingStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AlaErpRingStatus_Type.__name__=_E
_AlaErpRingStatus_Object=MibTableColumn
alaErpRingStatus=_AlaErpRingStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,6),_AlaErpRingStatus_Type())
alaErpRingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingStatus.setStatus(_A)
class _AlaErpRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('idle',0),('protection',1)))
_AlaErpRingState_Type.__name__=_E
_AlaErpRingState_Object=MibTableColumn
alaErpRingState=_AlaErpRingState_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,7),_AlaErpRingState_Type())
alaErpRingState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpRingState.setStatus(_A)
class _AlaErpRingWaitToRestoreTimer_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_AlaErpRingWaitToRestoreTimer_Type.__name__=_J
_AlaErpRingWaitToRestoreTimer_Object=MibTableColumn
alaErpRingWaitToRestoreTimer=_AlaErpRingWaitToRestoreTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,8),_AlaErpRingWaitToRestoreTimer_Type())
alaErpRingWaitToRestoreTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingWaitToRestoreTimer.setStatus(_A)
class _AlaErpRingGuardTimer_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_AlaErpRingGuardTimer_Type.__name__=_E
_AlaErpRingGuardTimer_Object=MibTableColumn
alaErpRingGuardTimer=_AlaErpRingGuardTimer_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,9),_AlaErpRingGuardTimer_Type())
alaErpRingGuardTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingGuardTimer.setStatus(_A)
if mibBuilder.loadTexts:alaErpRingGuardTimer.setUnits('10 milliseconds')
class _AlaErpRingClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_AlaErpRingClearStats_Type.__name__=_E
_AlaErpRingClearStats_Object=MibTableColumn
alaErpRingClearStats=_AlaErpRingClearStats_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,10),_AlaErpRingClearStats_Type())
alaErpRingClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingClearStats.setStatus(_A)
_AlaErpRingLastStateChange_Type=TimeStamp
_AlaErpRingLastStateChange_Object=MibTableColumn
alaErpRingLastStateChange=_AlaErpRingLastStateChange_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,11),_AlaErpRingLastStateChange_Type())
alaErpRingLastStateChange.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpRingLastStateChange.setStatus(_A)
_AlaErpRingTimeToRevert_Type=TimeTicks
_AlaErpRingTimeToRevert_Object=MibTableColumn
alaErpRingTimeToRevert=_AlaErpRingTimeToRevert_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,12),_AlaErpRingTimeToRevert_Type())
alaErpRingTimeToRevert.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpRingTimeToRevert.setStatus(_A)
_AlaErpRingRowStatus_Type=RowStatus
_AlaErpRingRowStatus_Object=MibTableColumn
alaErpRingRowStatus=_AlaErpRingRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,13),_AlaErpRingRowStatus_Type())
alaErpRingRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingRowStatus.setStatus(_A)
class _AlaErpRingVirtualChannel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AlaErpRingVirtualChannel_Type.__name__=_E
_AlaErpRingVirtualChannel_Object=MibTableColumn
alaErpRingVirtualChannel=_AlaErpRingVirtualChannel_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,14),_AlaErpRingVirtualChannel_Type())
alaErpRingVirtualChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingVirtualChannel.setStatus(_A)
class _AlaErpRingRevertive_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AlaErpRingRevertive_Type.__name__=_E
_AlaErpRingRevertive_Object=MibTableColumn
alaErpRingRevertive=_AlaErpRingRevertive_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,15),_AlaErpRingRevertive_Type())
alaErpRingRevertive.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingRevertive.setStatus(_A)
class _AlaErpRingClearAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_AlaErpRingClearAction_Type.__name__=_E
_AlaErpRingClearAction_Object=MibTableColumn
alaErpRingClearAction=_AlaErpRingClearAction_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,16),_AlaErpRingClearAction_Type())
alaErpRingClearAction.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingClearAction.setStatus(_A)
class _AlaErpRingActiveVersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AlaErpRingActiveVersion_Type.__name__=_J
_AlaErpRingActiveVersion_Object=MibTableColumn
alaErpRingActiveVersion=_AlaErpRingActiveVersion_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,17),_AlaErpRingActiveVersion_Type())
alaErpRingActiveVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpRingActiveVersion.setStatus(_A)
class _AlaErpRingResetVersionFallback_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_AlaErpRingResetVersionFallback_Type.__name__=_E
_AlaErpRingResetVersionFallback_Object=MibTableColumn
alaErpRingResetVersionFallback=_AlaErpRingResetVersionFallback_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,1,1,18),_AlaErpRingResetVersionFallback_Type())
alaErpRingResetVersionFallback.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingResetVersionFallback.setStatus(_A)
_AlaErpRingPortTable_Object=MibTable
alaErpRingPortTable=_AlaErpRingPortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,2))
if mibBuilder.loadTexts:alaErpRingPortTable.setStatus(_A)
_AlaErpRingPortEntry_Object=MibTableRow
alaErpRingPortEntry=_AlaErpRingPortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,2,1))
alaErpRingPortEntry.setIndexNames((0,_B,_F),(0,_B,_M))
if mibBuilder.loadTexts:alaErpRingPortEntry.setStatus(_A)
_AlaErpRingPortIfIndex_Type=InterfaceIndex
_AlaErpRingPortIfIndex_Object=MibTableColumn
alaErpRingPortIfIndex=_AlaErpRingPortIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,2,1,1),_AlaErpRingPortIfIndex_Type())
alaErpRingPortIfIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:alaErpRingPortIfIndex.setStatus(_A)
class _AlaErpRingPortStatus_Type(AlaErpRingPortStatus):defaultValue=2
_AlaErpRingPortStatus_Type.__name__=_R
_AlaErpRingPortStatus_Object=MibTableColumn
alaErpRingPortStatus=_AlaErpRingPortStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,2,1,2),_AlaErpRingPortStatus_Type())
alaErpRingPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpRingPortStatus.setStatus(_A)
class _AlaErpRingPortType_Type(AlaErpRingPortType):defaultValue=1
_AlaErpRingPortType_Type.__name__=_S
_AlaErpRingPortType_Object=MibTableColumn
alaErpRingPortType=_AlaErpRingPortType_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,2,1,3),_AlaErpRingPortType_Type())
alaErpRingPortType.setMaxAccess(_I)
if mibBuilder.loadTexts:alaErpRingPortType.setStatus(_A)
class _AlaErpRingPortEthOAMEvent_Type(TruthValue):defaultValue=2
_AlaErpRingPortEthOAMEvent_Type.__name__=_P
_AlaErpRingPortEthOAMEvent_Object=MibTableColumn
alaErpRingPortEthOAMEvent=_AlaErpRingPortEthOAMEvent_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,2,1,4),_AlaErpRingPortEthOAMEvent_Type())
alaErpRingPortEthOAMEvent.setMaxAccess(_I)
if mibBuilder.loadTexts:alaErpRingPortEthOAMEvent.setStatus(_A)
class _AlaErpRingPortClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_AlaErpRingPortClearStats_Type.__name__=_E
_AlaErpRingPortClearStats_Object=MibTableColumn
alaErpRingPortClearStats=_AlaErpRingPortClearStats_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,2,1,5),_AlaErpRingPortClearStats_Type())
alaErpRingPortClearStats.setMaxAccess(_I)
if mibBuilder.loadTexts:alaErpRingPortClearStats.setStatus(_A)
_AlaErpRingPortRmepId_Type=AlaErpRingMepId
_AlaErpRingPortRmepId_Object=MibTableColumn
alaErpRingPortRmepId=_AlaErpRingPortRmepId_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,2,1,6),_AlaErpRingPortRmepId_Type())
alaErpRingPortRmepId.setMaxAccess(_I)
if mibBuilder.loadTexts:alaErpRingPortRmepId.setStatus(_A)
_AlaErpRingVlanTable_Object=MibTable
alaErpRingVlanTable=_AlaErpRingVlanTable_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,3))
if mibBuilder.loadTexts:alaErpRingVlanTable.setStatus(_A)
_AlaErpRingVlanEntry_Object=MibTableRow
alaErpRingVlanEntry=_AlaErpRingVlanEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,3,1))
alaErpRingVlanEntry.setIndexNames((0,_B,_F),(0,_B,_T))
if mibBuilder.loadTexts:alaErpRingVlanEntry.setStatus(_A)
_AlaErpRingVlanProtectedVid_Type=VlanId
_AlaErpRingVlanProtectedVid_Object=MibTableColumn
alaErpRingVlanProtectedVid=_AlaErpRingVlanProtectedVid_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,3,1,1),_AlaErpRingVlanProtectedVid_Type())
alaErpRingVlanProtectedVid.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:alaErpRingVlanProtectedVid.setStatus(_A)
_AlaErpRingVlanRowStatus_Type=RowStatus
_AlaErpRingVlanRowStatus_Object=MibTableColumn
alaErpRingVlanRowStatus=_AlaErpRingVlanRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,3,1,2),_AlaErpRingVlanRowStatus_Type())
alaErpRingVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaErpRingVlanRowStatus.setStatus(_A)
_AlaErpStatsTable_Object=MibTable
alaErpStatsTable=_AlaErpStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4))
if mibBuilder.loadTexts:alaErpStatsTable.setStatus(_A)
_AlaErpStatsEntry_Object=MibTableRow
alaErpStatsEntry=_AlaErpStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4,1))
if mibBuilder.loadTexts:alaErpStatsEntry.setStatus(_A)
_AlaErpStatsSignalFailPduTx_Type=Counter32
_AlaErpStatsSignalFailPduTx_Object=MibTableColumn
alaErpStatsSignalFailPduTx=_AlaErpStatsSignalFailPduTx_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4,1,1),_AlaErpStatsSignalFailPduTx_Type())
alaErpStatsSignalFailPduTx.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpStatsSignalFailPduTx.setStatus(_A)
_AlaErpStatsSignalFailPduRx_Type=Counter32
_AlaErpStatsSignalFailPduRx_Object=MibTableColumn
alaErpStatsSignalFailPduRx=_AlaErpStatsSignalFailPduRx_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4,1,2),_AlaErpStatsSignalFailPduRx_Type())
alaErpStatsSignalFailPduRx.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpStatsSignalFailPduRx.setStatus(_A)
_AlaErpStatsSignalFailPduDrop_Type=Counter32
_AlaErpStatsSignalFailPduDrop_Object=MibTableColumn
alaErpStatsSignalFailPduDrop=_AlaErpStatsSignalFailPduDrop_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4,1,3),_AlaErpStatsSignalFailPduDrop_Type())
alaErpStatsSignalFailPduDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpStatsSignalFailPduDrop.setStatus(_A)
_AlaErpStatsNoRequestPduTx_Type=Counter32
_AlaErpStatsNoRequestPduTx_Object=MibTableColumn
alaErpStatsNoRequestPduTx=_AlaErpStatsNoRequestPduTx_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4,1,4),_AlaErpStatsNoRequestPduTx_Type())
alaErpStatsNoRequestPduTx.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpStatsNoRequestPduTx.setStatus(_A)
_AlaErpStatsNoRequestPduRx_Type=Counter32
_AlaErpStatsNoRequestPduRx_Object=MibTableColumn
alaErpStatsNoRequestPduRx=_AlaErpStatsNoRequestPduRx_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4,1,5),_AlaErpStatsNoRequestPduRx_Type())
alaErpStatsNoRequestPduRx.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpStatsNoRequestPduRx.setStatus(_A)
_AlaErpStatsNoRequestPduDrop_Type=Counter32
_AlaErpStatsNoRequestPduDrop_Object=MibTableColumn
alaErpStatsNoRequestPduDrop=_AlaErpStatsNoRequestPduDrop_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4,1,6),_AlaErpStatsNoRequestPduDrop_Type())
alaErpStatsNoRequestPduDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpStatsNoRequestPduDrop.setStatus(_A)
_AlaErpStatsRPLBlockPDUTx_Type=Counter32
_AlaErpStatsRPLBlockPDUTx_Object=MibTableColumn
alaErpStatsRPLBlockPDUTx=_AlaErpStatsRPLBlockPDUTx_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4,1,7),_AlaErpStatsRPLBlockPDUTx_Type())
alaErpStatsRPLBlockPDUTx.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpStatsRPLBlockPDUTx.setStatus(_A)
_AlaErpStatsRPLBlockPDURx_Type=Counter32
_AlaErpStatsRPLBlockPDURx_Object=MibTableColumn
alaErpStatsRPLBlockPDURx=_AlaErpStatsRPLBlockPDURx_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4,1,8),_AlaErpStatsRPLBlockPDURx_Type())
alaErpStatsRPLBlockPDURx.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpStatsRPLBlockPDURx.setStatus(_A)
_AlaErpStatsRPLBlockPDUDrop_Type=Counter32
_AlaErpStatsRPLBlockPDUDrop_Object=MibTableColumn
alaErpStatsRPLBlockPDUDrop=_AlaErpStatsRPLBlockPDUDrop_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4,1,9),_AlaErpStatsRPLBlockPDUDrop_Type())
alaErpStatsRPLBlockPDUDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpStatsRPLBlockPDUDrop.setStatus(_A)
_AlaErpStatsPDUErr_Type=Counter32
_AlaErpStatsPDUErr_Object=MibTableColumn
alaErpStatsPDUErr=_AlaErpStatsPDUErr_Object((1,3,6,1,4,1,6486,800,1,2,1,46,1,1,2,4,1,10),_AlaErpStatsPDUErr_Type())
alaErpStatsPDUErr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaErpStatsPDUErr.setStatus(_A)
_AlaErpNotifications_ObjectIdentity=ObjectIdentity
alaErpNotifications=_AlaErpNotifications_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,46,1,2))
_AlaErpNotificationsRoot_ObjectIdentity=ObjectIdentity
alaErpNotificationsRoot=_AlaErpNotificationsRoot_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,46,1,2,0))
_AlcatelIND1ERPMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1ERPMIBConformance=_AlcatelIND1ERPMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,46,1,3))
_AlcatelIND1ERPMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1ERPMIBCompliances=_AlcatelIND1ERPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,46,1,3,1))
_AlcatelIND1ERPMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1ERPMIBGroups=_AlcatelIND1ERPMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,46,1,3,2))
alaErpRingPortEntry.registerAugmentions((_B,_U))
alaErpStatsEntry.setIndexNames(*alaErpRingPortEntry.getIndexNames())
alaErpGlobalGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,46,1,3,2,1))
alaErpGlobalGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:alaErpGlobalGroup.setStatus(_A)
alaErpRingAttributesGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,46,1,3,2,2))
alaErpRingAttributesGroup.setObjects(*((_B,_F),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_N),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_O),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:alaErpRingAttributesGroup.setStatus(_A)
alaErpRingStateChanged=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,46,1,2,0,1))
alaErpRingStateChanged.setObjects(*((_B,_F),(_B,_N)))
if mibBuilder.loadTexts:alaErpRingStateChanged.setStatus(_A)
alaErpRingMultipleRpl=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,46,1,2,0,2))
alaErpRingMultipleRpl.setObjects((_B,_F))
if mibBuilder.loadTexts:alaErpRingMultipleRpl.setStatus(_A)
alaErpRingRemoved=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,46,1,2,0,3))
alaErpRingRemoved.setObjects((_B,_F))
if mibBuilder.loadTexts:alaErpRingRemoved.setStatus(_A)
alaErpRingPortStatusChanged=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,46,1,2,0,4))
alaErpRingPortStatusChanged.setObjects(*((_B,_F),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:alaErpRingPortStatusChanged.setStatus(_A)
alaErpNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,46,1,3,2,3))
alaErpNotificationGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:alaErpNotificationGroup.setStatus(_A)
alcatelIND1ERPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,46,1,3,1,1))
alcatelIND1ERPMIBCompliance.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:alcatelIND1ERPMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_R:AlaErpRingPortStatus,_S:AlaErpRingPortType,'AlaErpRingMepId':AlaErpRingMepId,'AlaErpRingMEGLevel':AlaErpRingMEGLevel,'alcatelIND1ERPMIB':alcatelIND1ERPMIB,'alcatelIND1ERPMIBObjects':alcatelIND1ERPMIBObjects,'alaErpGlobal':alaErpGlobal,_V:alaErpClearStats,'alaErpRingAttributes':alaErpRingAttributes,'alaErpRingTable':alaErpRingTable,'alaErpRingEntry':alaErpRingEntry,_F:alaErpRingId,_W:alaErpRingServiceVid,_X:alaErpRingMEGLevel,_Y:alaErpRingPort1,_Z:alaErpRingPort2,_a:alaErpRingStatus,_N:alaErpRingState,_b:alaErpRingWaitToRestoreTimer,_c:alaErpRingGuardTimer,_d:alaErpRingClearStats,_e:alaErpRingLastStateChange,_f:alaErpRingTimeToRevert,_g:alaErpRingRowStatus,_h:alaErpRingVirtualChannel,_i:alaErpRingRevertive,_j:alaErpRingClearAction,_z:alaErpRingActiveVersion,_A0:alaErpRingResetVersionFallback,'alaErpRingPortTable':alaErpRingPortTable,'alaErpRingPortEntry':alaErpRingPortEntry,_M:alaErpRingPortIfIndex,_O:alaErpRingPortStatus,_k:alaErpRingPortType,_l:alaErpRingPortEthOAMEvent,_m:alaErpRingPortClearStats,_n:alaErpRingPortRmepId,'alaErpRingVlanTable':alaErpRingVlanTable,'alaErpRingVlanEntry':alaErpRingVlanEntry,_T:alaErpRingVlanProtectedVid,_o:alaErpRingVlanRowStatus,'alaErpStatsTable':alaErpStatsTable,_U:alaErpStatsEntry,_p:alaErpStatsSignalFailPduTx,_q:alaErpStatsSignalFailPduRx,_r:alaErpStatsSignalFailPduDrop,_s:alaErpStatsNoRequestPduTx,_t:alaErpStatsNoRequestPduRx,_u:alaErpStatsNoRequestPduDrop,_v:alaErpStatsRPLBlockPDUTx,_w:alaErpStatsRPLBlockPDURx,_x:alaErpStatsRPLBlockPDUDrop,_y:alaErpStatsPDUErr,'alaErpNotifications':alaErpNotifications,'alaErpNotificationsRoot':alaErpNotificationsRoot,_A1:alaErpRingStateChanged,_A2:alaErpRingMultipleRpl,_A3:alaErpRingRemoved,_A4:alaErpRingPortStatusChanged,'alcatelIND1ERPMIBConformance':alcatelIND1ERPMIBConformance,'alcatelIND1ERPMIBCompliances':alcatelIND1ERPMIBCompliances,'alcatelIND1ERPMIBCompliance':alcatelIND1ERPMIBCompliance,'alcatelIND1ERPMIBGroups':alcatelIND1ERPMIBGroups,_A5:alaErpGlobalGroup,_A6:alaErpRingAttributesGroup,_A7:alaErpNotificationGroup})