_AZ='ciscoVsi2MasterNotificationGroup'
_AY='ciscoVsi2AlarmControlGroup'
_AX='ciscoVsi2MasterGroup'
_AW='vsiLcnExhaustionNotice'
_AV='vsiXCFailed'
_AU='vsiLogicalIfDown'
_AT='vsiLogicalIfUp'
_AS='vsiSessionDown'
_AR='vsiSessionUp'
_AQ='vsiControllerDeleted'
_AP='vsiControllerAdded'
_AO='vsiVSITrapEnable'
_AN='vsiXCTrapEnable'
_AM='vsiLogicalIfTrapEnable'
_AL='vsiSessionTrapEnable'
_AK='vsiControllerTrapEnable'
_AJ='vsiAvailableChnlAlarmThreshold'
_AI='vsiAvailableChnlWarnThreshold'
_AH='vsiControlIfIpAddress'
_AG='vsiXCVciHi'
_AF='vsiXCVpiHi'
_AE='vsiXCVciLow'
_AD='vsiXCVpiLow'
_AC='vsiXCState'
_AB='vsiLogicalIfSessionIndex'
_AA='vsiLogicalControlIfIndex'
_A9='vsiLogicalIfMaxVci'
_A8='vsiLogicalIfMinVci'
_A7='vsiLogicalIfMaxVpi'
_A6='vsiLogicalIfMinVpi'
_A5='vsiLogicalIfStrictSigRange'
_A4='vsiLogicalIfVpiTranslated'
_A3='vsiLogicalIfMulticastSupported'
_A2='vsiLogicalIfVcMergeSupported'
_A1='vsiLogicalIfMaxEgressCellRate'
_A0='vsiLogicalIfMaxIngressCellRate'
_z='vsiLogicalIfAvailEgressCellRate'
_y='vsiLogicalIfAvailIngressCellRate'
_x='vsiLogicalIfAvailEgressChnls'
_w='vsiLogicalIfAvailIngressChnls'
_v='vsiLogicalIfEndPointsInUse'
_u='vsiLogicalIfRxInvalidAddrs'
_t='vsiLogicalIfRxHeaderErrors'
_s='vsiLogicalIfTxCellsDiscarded'
_r='vsiLogicalIfRxCellsDiscarded'
_q='vsiLogicalIfTxCells'
_p='vsiLogicalIfRxCells'
_o='vsiLogicalIfAdminState'
_n='vsiLogicalIfName'
_m='vsiSessionPowerupId'
_l='vsiSessionActiveId'
_k='vsiSessionCmdsPending'
_j='vsiSessionWindowSize'
_i='vsiSessionSlaveId'
_h='vsiSessionSwitchName'
_g='vsiSessionSwitchId'
_f='vsiSessionVci'
_e='vsiSessionVpi'
_d='vsiLogicalControlInterface'
_c='vsiControlInterface'
_b='vsiSpecifiedVersion'
_a='vsiVersionInUse'
_Z='vsiTopVersionSupported'
_Y='vsiBaseVersionSupported'
_X='vsiCrossConnects'
_W='vsiControllerId'
_V='not-accessible'
_U='vsiSessionIndex'
_T='vsiSessionControllerIndex'
_S='Gauge32'
_R='ciscoVsiMasterGeneralGroup'
_Q='vsiAvailableChnlThresholdStatus'
_P='vsiXCIndex'
_O='vsiLogicalIfIndex'
_N='vsiLogicalIfControllerIndex'
_M='vsiLogicalIfOperState'
_L='vsiSessionState'
_K='vsiControllerType'
_J='vsiXCLogicalIfHi'
_I='vsiXCLogicalIfLow'
_H='vsiXCControllerIndex'
_G='vsiControllerIndex'
_F='TruthValue'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-VSIMASTER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_S,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
ciscoVsiMasterMIB=ModuleIdentity((1,3,6,1,4,1,9,9,162))
if mibBuilder.loadTexts:ciscoVsiMasterMIB.setRevisions(('2000-10-17 00:00','2000-06-01 00:00'))
class VsiControllerIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class VsiSessionIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class VsiLogicalIfIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class VsiXCIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CiscoVsiMasterObjects_ObjectIdentity=ObjectIdentity
ciscoVsiMasterObjects=_CiscoVsiMasterObjects_ObjectIdentity((1,3,6,1,4,1,9,9,162,1))
_VsiMasterControllerTable_Object=MibTable
vsiMasterControllerTable=_VsiMasterControllerTable_Object((1,3,6,1,4,1,9,9,162,1,1))
if mibBuilder.loadTexts:vsiMasterControllerTable.setStatus(_B)
_VsiMasterControllerEntry_Object=MibTableRow
vsiMasterControllerEntry=_VsiMasterControllerEntry_Object((1,3,6,1,4,1,9,9,162,1,1,1))
vsiMasterControllerEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:vsiMasterControllerEntry.setStatus(_B)
_VsiControllerIndex_Type=VsiControllerIndex
_VsiControllerIndex_Object=MibTableColumn
vsiControllerIndex=_VsiControllerIndex_Object((1,3,6,1,4,1,9,9,162,1,1,1,1),_VsiControllerIndex_Type())
vsiControllerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiControllerIndex.setStatus(_B)
class _VsiControllerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VsiControllerId_Type.__name__=_D
_VsiControllerId_Object=MibTableColumn
vsiControllerId=_VsiControllerId_Object((1,3,6,1,4,1,9,9,162,1,1,1,2),_VsiControllerId_Type())
vsiControllerId.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiControllerId.setStatus(_B)
class _VsiCrossConnects_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VsiCrossConnects_Type.__name__=_D
_VsiCrossConnects_Object=MibTableColumn
vsiCrossConnects=_VsiCrossConnects_Object((1,3,6,1,4,1,9,9,162,1,1,1,3),_VsiCrossConnects_Type())
vsiCrossConnects.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiCrossConnects.setStatus(_B)
class _VsiControllerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('mpls',2),('pnni',3),('par',4)))
_VsiControllerType_Type.__name__=_D
_VsiControllerType_Object=MibTableColumn
vsiControllerType=_VsiControllerType_Object((1,3,6,1,4,1,9,9,162,1,1,1,4),_VsiControllerType_Type())
vsiControllerType.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiControllerType.setStatus(_B)
class _VsiBaseVersionSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VsiBaseVersionSupported_Type.__name__=_D
_VsiBaseVersionSupported_Object=MibTableColumn
vsiBaseVersionSupported=_VsiBaseVersionSupported_Object((1,3,6,1,4,1,9,9,162,1,1,1,5),_VsiBaseVersionSupported_Type())
vsiBaseVersionSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiBaseVersionSupported.setStatus(_B)
class _VsiTopVersionSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VsiTopVersionSupported_Type.__name__=_D
_VsiTopVersionSupported_Object=MibTableColumn
vsiTopVersionSupported=_VsiTopVersionSupported_Object((1,3,6,1,4,1,9,9,162,1,1,1,6),_VsiTopVersionSupported_Type())
vsiTopVersionSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiTopVersionSupported.setStatus(_B)
class _VsiVersionInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VsiVersionInUse_Type.__name__=_D
_VsiVersionInUse_Object=MibTableColumn
vsiVersionInUse=_VsiVersionInUse_Object((1,3,6,1,4,1,9,9,162,1,1,1,7),_VsiVersionInUse_Type())
vsiVersionInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiVersionInUse.setStatus(_B)
class _VsiSpecifiedVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VsiSpecifiedVersion_Type.__name__=_D
_VsiSpecifiedVersion_Object=MibTableColumn
vsiSpecifiedVersion=_VsiSpecifiedVersion_Object((1,3,6,1,4,1,9,9,162,1,1,1,8),_VsiSpecifiedVersion_Type())
vsiSpecifiedVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:vsiSpecifiedVersion.setStatus(_B)
_VsiControlInterface_Type=InterfaceIndex
_VsiControlInterface_Object=MibTableColumn
vsiControlInterface=_VsiControlInterface_Object((1,3,6,1,4,1,9,9,162,1,1,1,9),_VsiControlInterface_Type())
vsiControlInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiControlInterface.setStatus(_B)
_VsiLogicalControlInterface_Type=VsiLogicalIfIndex
_VsiLogicalControlInterface_Object=MibTableColumn
vsiLogicalControlInterface=_VsiLogicalControlInterface_Object((1,3,6,1,4,1,9,9,162,1,1,1,10),_VsiLogicalControlInterface_Type())
vsiLogicalControlInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalControlInterface.setStatus(_B)
_VsiControlIfIpAddress_Type=IpAddress
_VsiControlIfIpAddress_Object=MibTableColumn
vsiControlIfIpAddress=_VsiControlIfIpAddress_Object((1,3,6,1,4,1,9,9,162,1,1,1,11),_VsiControlIfIpAddress_Type())
vsiControlIfIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiControlIfIpAddress.setStatus(_B)
class _VsiAvailableChnlWarnThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VsiAvailableChnlWarnThreshold_Type.__name__=_D
_VsiAvailableChnlWarnThreshold_Object=MibTableColumn
vsiAvailableChnlWarnThreshold=_VsiAvailableChnlWarnThreshold_Object((1,3,6,1,4,1,9,9,162,1,1,1,12),_VsiAvailableChnlWarnThreshold_Type())
vsiAvailableChnlWarnThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:vsiAvailableChnlWarnThreshold.setStatus(_B)
class _VsiAvailableChnlAlarmThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VsiAvailableChnlAlarmThreshold_Type.__name__=_D
_VsiAvailableChnlAlarmThreshold_Object=MibTableColumn
vsiAvailableChnlAlarmThreshold=_VsiAvailableChnlAlarmThreshold_Object((1,3,6,1,4,1,9,9,162,1,1,1,13),_VsiAvailableChnlAlarmThreshold_Type())
vsiAvailableChnlAlarmThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:vsiAvailableChnlAlarmThreshold.setStatus(_B)
class _VsiAvailableChnlThresholdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('warning',1),('alarm',2),('recovery',3),('normal',4)))
_VsiAvailableChnlThresholdStatus_Type.__name__=_D
_VsiAvailableChnlThresholdStatus_Object=MibTableColumn
vsiAvailableChnlThresholdStatus=_VsiAvailableChnlThresholdStatus_Object((1,3,6,1,4,1,9,9,162,1,1,1,14),_VsiAvailableChnlThresholdStatus_Type())
vsiAvailableChnlThresholdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiAvailableChnlThresholdStatus.setStatus(_B)
_VsiSessionTable_Object=MibTable
vsiSessionTable=_VsiSessionTable_Object((1,3,6,1,4,1,9,9,162,1,2))
if mibBuilder.loadTexts:vsiSessionTable.setStatus(_B)
_VsiSessionEntry_Object=MibTableRow
vsiSessionEntry=_VsiSessionEntry_Object((1,3,6,1,4,1,9,9,162,1,2,1))
vsiSessionEntry.setIndexNames((0,_A,_T),(0,_A,_U))
if mibBuilder.loadTexts:vsiSessionEntry.setStatus(_B)
_VsiSessionControllerIndex_Type=VsiControllerIndex
_VsiSessionControllerIndex_Object=MibTableColumn
vsiSessionControllerIndex=_VsiSessionControllerIndex_Object((1,3,6,1,4,1,9,9,162,1,2,1,1),_VsiSessionControllerIndex_Type())
vsiSessionControllerIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:vsiSessionControllerIndex.setStatus(_B)
_VsiSessionIndex_Type=VsiSessionIndex
_VsiSessionIndex_Object=MibTableColumn
vsiSessionIndex=_VsiSessionIndex_Object((1,3,6,1,4,1,9,9,162,1,2,1,2),_VsiSessionIndex_Type())
vsiSessionIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:vsiSessionIndex.setStatus(_B)
class _VsiSessionVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VsiSessionVpi_Type.__name__=_D
_VsiSessionVpi_Object=MibTableColumn
vsiSessionVpi=_VsiSessionVpi_Object((1,3,6,1,4,1,9,9,162,1,2,1,3),_VsiSessionVpi_Type())
vsiSessionVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiSessionVpi.setStatus(_B)
class _VsiSessionVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VsiSessionVci_Type.__name__=_D
_VsiSessionVci_Object=MibTableColumn
vsiSessionVci=_VsiSessionVci_Object((1,3,6,1,4,1,9,9,162,1,2,1,4),_VsiSessionVci_Type())
vsiSessionVci.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiSessionVci.setStatus(_B)
class _VsiSessionSwitchId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VsiSessionSwitchId_Type.__name__=_D
_VsiSessionSwitchId_Object=MibTableColumn
vsiSessionSwitchId=_VsiSessionSwitchId_Object((1,3,6,1,4,1,9,9,162,1,2,1,5),_VsiSessionSwitchId_Type())
vsiSessionSwitchId.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiSessionSwitchId.setStatus(_B)
_VsiSessionSwitchName_Type=SnmpAdminString
_VsiSessionSwitchName_Object=MibTableColumn
vsiSessionSwitchName=_VsiSessionSwitchName_Object((1,3,6,1,4,1,9,9,162,1,2,1,6),_VsiSessionSwitchName_Type())
vsiSessionSwitchName.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiSessionSwitchName.setStatus(_B)
class _VsiSessionSlaveId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VsiSessionSlaveId_Type.__name__=_D
_VsiSessionSlaveId_Object=MibTableColumn
vsiSessionSlaveId=_VsiSessionSlaveId_Object((1,3,6,1,4,1,9,9,162,1,2,1,7),_VsiSessionSlaveId_Type())
vsiSessionSlaveId.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiSessionSlaveId.setStatus(_B)
class _VsiSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('inactive',1),('unknown',2),('configuring',3),('resyncStarting',4),('resyncUnderway',5),('resyncEnding',6),('discovery',7),('established',8),('shutdownStarting',9)))
_VsiSessionState_Type.__name__=_D
_VsiSessionState_Object=MibTableColumn
vsiSessionState=_VsiSessionState_Object((1,3,6,1,4,1,9,9,162,1,2,1,8),_VsiSessionState_Type())
vsiSessionState.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiSessionState.setStatus(_B)
class _VsiSessionWindowSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VsiSessionWindowSize_Type.__name__=_D
_VsiSessionWindowSize_Object=MibTableColumn
vsiSessionWindowSize=_VsiSessionWindowSize_Object((1,3,6,1,4,1,9,9,162,1,2,1,9),_VsiSessionWindowSize_Type())
vsiSessionWindowSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiSessionWindowSize.setStatus(_B)
class _VsiSessionCmdsPending_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VsiSessionCmdsPending_Type.__name__=_S
_VsiSessionCmdsPending_Object=MibTableColumn
vsiSessionCmdsPending=_VsiSessionCmdsPending_Object((1,3,6,1,4,1,9,9,162,1,2,1,10),_VsiSessionCmdsPending_Type())
vsiSessionCmdsPending.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiSessionCmdsPending.setStatus(_B)
class _VsiSessionActiveId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VsiSessionActiveId_Type.__name__=_D
_VsiSessionActiveId_Object=MibTableColumn
vsiSessionActiveId=_VsiSessionActiveId_Object((1,3,6,1,4,1,9,9,162,1,2,1,11),_VsiSessionActiveId_Type())
vsiSessionActiveId.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiSessionActiveId.setStatus(_B)
class _VsiSessionPowerupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VsiSessionPowerupId_Type.__name__=_D
_VsiSessionPowerupId_Object=MibTableColumn
vsiSessionPowerupId=_VsiSessionPowerupId_Object((1,3,6,1,4,1,9,9,162,1,2,1,12),_VsiSessionPowerupId_Type())
vsiSessionPowerupId.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiSessionPowerupId.setStatus(_B)
_VsiLogicalIfTable_Object=MibTable
vsiLogicalIfTable=_VsiLogicalIfTable_Object((1,3,6,1,4,1,9,9,162,1,3))
if mibBuilder.loadTexts:vsiLogicalIfTable.setStatus(_B)
_VsiLogicalIfEntry_Object=MibTableRow
vsiLogicalIfEntry=_VsiLogicalIfEntry_Object((1,3,6,1,4,1,9,9,162,1,3,1))
vsiLogicalIfEntry.setIndexNames((0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:vsiLogicalIfEntry.setStatus(_B)
_VsiLogicalIfControllerIndex_Type=VsiControllerIndex
_VsiLogicalIfControllerIndex_Object=MibTableColumn
vsiLogicalIfControllerIndex=_VsiLogicalIfControllerIndex_Object((1,3,6,1,4,1,9,9,162,1,3,1,1),_VsiLogicalIfControllerIndex_Type())
vsiLogicalIfControllerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfControllerIndex.setStatus(_B)
_VsiLogicalIfIndex_Type=VsiLogicalIfIndex
_VsiLogicalIfIndex_Object=MibTableColumn
vsiLogicalIfIndex=_VsiLogicalIfIndex_Object((1,3,6,1,4,1,9,9,162,1,3,1,2),_VsiLogicalIfIndex_Type())
vsiLogicalIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfIndex.setStatus(_B)
_VsiLogicalIfName_Type=SnmpAdminString
_VsiLogicalIfName_Object=MibTableColumn
vsiLogicalIfName=_VsiLogicalIfName_Object((1,3,6,1,4,1,9,9,162,1,3,1,3),_VsiLogicalIfName_Type())
vsiLogicalIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfName.setStatus(_B)
class _VsiLogicalIfOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('removed',1),('active',2),('failedExternal',3),('failedInternal',4)))
_VsiLogicalIfOperState_Type.__name__=_D
_VsiLogicalIfOperState_Object=MibTableColumn
vsiLogicalIfOperState=_VsiLogicalIfOperState_Object((1,3,6,1,4,1,9,9,162,1,3,1,4),_VsiLogicalIfOperState_Type())
vsiLogicalIfOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfOperState.setStatus(_B)
class _VsiLogicalIfAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('up',2),('pendingDown',3)))
_VsiLogicalIfAdminState_Type.__name__=_D
_VsiLogicalIfAdminState_Object=MibTableColumn
vsiLogicalIfAdminState=_VsiLogicalIfAdminState_Object((1,3,6,1,4,1,9,9,162,1,3,1,5),_VsiLogicalIfAdminState_Type())
vsiLogicalIfAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfAdminState.setStatus(_B)
_VsiLogicalIfRxCells_Type=Counter32
_VsiLogicalIfRxCells_Object=MibTableColumn
vsiLogicalIfRxCells=_VsiLogicalIfRxCells_Object((1,3,6,1,4,1,9,9,162,1,3,1,6),_VsiLogicalIfRxCells_Type())
vsiLogicalIfRxCells.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfRxCells.setStatus(_B)
_VsiLogicalIfTxCells_Type=Counter32
_VsiLogicalIfTxCells_Object=MibTableColumn
vsiLogicalIfTxCells=_VsiLogicalIfTxCells_Object((1,3,6,1,4,1,9,9,162,1,3,1,7),_VsiLogicalIfTxCells_Type())
vsiLogicalIfTxCells.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfTxCells.setStatus(_B)
_VsiLogicalIfRxCellsDiscarded_Type=Counter32
_VsiLogicalIfRxCellsDiscarded_Object=MibTableColumn
vsiLogicalIfRxCellsDiscarded=_VsiLogicalIfRxCellsDiscarded_Object((1,3,6,1,4,1,9,9,162,1,3,1,8),_VsiLogicalIfRxCellsDiscarded_Type())
vsiLogicalIfRxCellsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfRxCellsDiscarded.setStatus(_B)
_VsiLogicalIfTxCellsDiscarded_Type=Counter32
_VsiLogicalIfTxCellsDiscarded_Object=MibTableColumn
vsiLogicalIfTxCellsDiscarded=_VsiLogicalIfTxCellsDiscarded_Object((1,3,6,1,4,1,9,9,162,1,3,1,9),_VsiLogicalIfTxCellsDiscarded_Type())
vsiLogicalIfTxCellsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfTxCellsDiscarded.setStatus(_B)
_VsiLogicalIfRxHeaderErrors_Type=Counter32
_VsiLogicalIfRxHeaderErrors_Object=MibTableColumn
vsiLogicalIfRxHeaderErrors=_VsiLogicalIfRxHeaderErrors_Object((1,3,6,1,4,1,9,9,162,1,3,1,10),_VsiLogicalIfRxHeaderErrors_Type())
vsiLogicalIfRxHeaderErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfRxHeaderErrors.setStatus(_B)
_VsiLogicalIfRxInvalidAddrs_Type=Counter32
_VsiLogicalIfRxInvalidAddrs_Object=MibTableColumn
vsiLogicalIfRxInvalidAddrs=_VsiLogicalIfRxInvalidAddrs_Object((1,3,6,1,4,1,9,9,162,1,3,1,11),_VsiLogicalIfRxInvalidAddrs_Type())
vsiLogicalIfRxInvalidAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfRxInvalidAddrs.setStatus(_B)
_VsiLogicalIfEndPointsInUse_Type=Gauge32
_VsiLogicalIfEndPointsInUse_Object=MibTableColumn
vsiLogicalIfEndPointsInUse=_VsiLogicalIfEndPointsInUse_Object((1,3,6,1,4,1,9,9,162,1,3,1,12),_VsiLogicalIfEndPointsInUse_Type())
vsiLogicalIfEndPointsInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfEndPointsInUse.setStatus(_B)
_VsiLogicalIfAvailIngressChnls_Type=Gauge32
_VsiLogicalIfAvailIngressChnls_Object=MibTableColumn
vsiLogicalIfAvailIngressChnls=_VsiLogicalIfAvailIngressChnls_Object((1,3,6,1,4,1,9,9,162,1,3,1,13),_VsiLogicalIfAvailIngressChnls_Type())
vsiLogicalIfAvailIngressChnls.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfAvailIngressChnls.setStatus(_B)
_VsiLogicalIfAvailEgressChnls_Type=Gauge32
_VsiLogicalIfAvailEgressChnls_Object=MibTableColumn
vsiLogicalIfAvailEgressChnls=_VsiLogicalIfAvailEgressChnls_Object((1,3,6,1,4,1,9,9,162,1,3,1,14),_VsiLogicalIfAvailEgressChnls_Type())
vsiLogicalIfAvailEgressChnls.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfAvailEgressChnls.setStatus(_B)
_VsiLogicalIfAvailIngressCellRate_Type=Gauge32
_VsiLogicalIfAvailIngressCellRate_Object=MibTableColumn
vsiLogicalIfAvailIngressCellRate=_VsiLogicalIfAvailIngressCellRate_Object((1,3,6,1,4,1,9,9,162,1,3,1,15),_VsiLogicalIfAvailIngressCellRate_Type())
vsiLogicalIfAvailIngressCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfAvailIngressCellRate.setStatus(_B)
_VsiLogicalIfAvailEgressCellRate_Type=Gauge32
_VsiLogicalIfAvailEgressCellRate_Object=MibTableColumn
vsiLogicalIfAvailEgressCellRate=_VsiLogicalIfAvailEgressCellRate_Object((1,3,6,1,4,1,9,9,162,1,3,1,16),_VsiLogicalIfAvailEgressCellRate_Type())
vsiLogicalIfAvailEgressCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfAvailEgressCellRate.setStatus(_B)
_VsiLogicalIfVcMergeSupported_Type=TruthValue
_VsiLogicalIfVcMergeSupported_Object=MibTableColumn
vsiLogicalIfVcMergeSupported=_VsiLogicalIfVcMergeSupported_Object((1,3,6,1,4,1,9,9,162,1,3,1,17),_VsiLogicalIfVcMergeSupported_Type())
vsiLogicalIfVcMergeSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfVcMergeSupported.setStatus(_B)
_VsiLogicalIfMulticastSupported_Type=TruthValue
_VsiLogicalIfMulticastSupported_Object=MibTableColumn
vsiLogicalIfMulticastSupported=_VsiLogicalIfMulticastSupported_Object((1,3,6,1,4,1,9,9,162,1,3,1,18),_VsiLogicalIfMulticastSupported_Type())
vsiLogicalIfMulticastSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfMulticastSupported.setStatus(_B)
_VsiLogicalIfVpiTranslated_Type=TruthValue
_VsiLogicalIfVpiTranslated_Object=MibTableColumn
vsiLogicalIfVpiTranslated=_VsiLogicalIfVpiTranslated_Object((1,3,6,1,4,1,9,9,162,1,3,1,19),_VsiLogicalIfVpiTranslated_Type())
vsiLogicalIfVpiTranslated.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfVpiTranslated.setStatus(_B)
_VsiLogicalIfStrictSigRange_Type=TruthValue
_VsiLogicalIfStrictSigRange_Object=MibTableColumn
vsiLogicalIfStrictSigRange=_VsiLogicalIfStrictSigRange_Object((1,3,6,1,4,1,9,9,162,1,3,1,20),_VsiLogicalIfStrictSigRange_Type())
vsiLogicalIfStrictSigRange.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfStrictSigRange.setStatus(_B)
class _VsiLogicalIfMaxIngressCellRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VsiLogicalIfMaxIngressCellRate_Type.__name__=_D
_VsiLogicalIfMaxIngressCellRate_Object=MibTableColumn
vsiLogicalIfMaxIngressCellRate=_VsiLogicalIfMaxIngressCellRate_Object((1,3,6,1,4,1,9,9,162,1,3,1,21),_VsiLogicalIfMaxIngressCellRate_Type())
vsiLogicalIfMaxIngressCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfMaxIngressCellRate.setStatus(_B)
class _VsiLogicalIfMaxEgressCellRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VsiLogicalIfMaxEgressCellRate_Type.__name__=_D
_VsiLogicalIfMaxEgressCellRate_Object=MibTableColumn
vsiLogicalIfMaxEgressCellRate=_VsiLogicalIfMaxEgressCellRate_Object((1,3,6,1,4,1,9,9,162,1,3,1,22),_VsiLogicalIfMaxEgressCellRate_Type())
vsiLogicalIfMaxEgressCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfMaxEgressCellRate.setStatus(_B)
class _VsiLogicalIfMinVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VsiLogicalIfMinVpi_Type.__name__=_D
_VsiLogicalIfMinVpi_Object=MibTableColumn
vsiLogicalIfMinVpi=_VsiLogicalIfMinVpi_Object((1,3,6,1,4,1,9,9,162,1,3,1,23),_VsiLogicalIfMinVpi_Type())
vsiLogicalIfMinVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfMinVpi.setStatus(_B)
class _VsiLogicalIfMaxVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VsiLogicalIfMaxVpi_Type.__name__=_D
_VsiLogicalIfMaxVpi_Object=MibTableColumn
vsiLogicalIfMaxVpi=_VsiLogicalIfMaxVpi_Object((1,3,6,1,4,1,9,9,162,1,3,1,24),_VsiLogicalIfMaxVpi_Type())
vsiLogicalIfMaxVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfMaxVpi.setStatus(_B)
class _VsiLogicalIfMinVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VsiLogicalIfMinVci_Type.__name__=_D
_VsiLogicalIfMinVci_Object=MibTableColumn
vsiLogicalIfMinVci=_VsiLogicalIfMinVci_Object((1,3,6,1,4,1,9,9,162,1,3,1,25),_VsiLogicalIfMinVci_Type())
vsiLogicalIfMinVci.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfMinVci.setStatus(_B)
class _VsiLogicalIfMaxVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VsiLogicalIfMaxVci_Type.__name__=_D
_VsiLogicalIfMaxVci_Object=MibTableColumn
vsiLogicalIfMaxVci=_VsiLogicalIfMaxVci_Object((1,3,6,1,4,1,9,9,162,1,3,1,26),_VsiLogicalIfMaxVci_Type())
vsiLogicalIfMaxVci.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfMaxVci.setStatus(_B)
_VsiLogicalControlIfIndex_Type=InterfaceIndex
_VsiLogicalControlIfIndex_Object=MibTableColumn
vsiLogicalControlIfIndex=_VsiLogicalControlIfIndex_Object((1,3,6,1,4,1,9,9,162,1,3,1,27),_VsiLogicalControlIfIndex_Type())
vsiLogicalControlIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalControlIfIndex.setStatus(_B)
_VsiLogicalIfSessionIndex_Type=VsiSessionIndex
_VsiLogicalIfSessionIndex_Object=MibTableColumn
vsiLogicalIfSessionIndex=_VsiLogicalIfSessionIndex_Object((1,3,6,1,4,1,9,9,162,1,3,1,28),_VsiLogicalIfSessionIndex_Type())
vsiLogicalIfSessionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiLogicalIfSessionIndex.setStatus(_B)
_VsiXCTable_Object=MibTable
vsiXCTable=_VsiXCTable_Object((1,3,6,1,4,1,9,9,162,1,4))
if mibBuilder.loadTexts:vsiXCTable.setStatus(_B)
_VsiXCEntry_Object=MibTableRow
vsiXCEntry=_VsiXCEntry_Object((1,3,6,1,4,1,9,9,162,1,4,1))
vsiXCEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_A,_J),(0,_A,_P))
if mibBuilder.loadTexts:vsiXCEntry.setStatus(_B)
_VsiXCControllerIndex_Type=VsiControllerIndex
_VsiXCControllerIndex_Object=MibTableColumn
vsiXCControllerIndex=_VsiXCControllerIndex_Object((1,3,6,1,4,1,9,9,162,1,4,1,1),_VsiXCControllerIndex_Type())
vsiXCControllerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiXCControllerIndex.setStatus(_B)
_VsiXCLogicalIfLow_Type=VsiLogicalIfIndex
_VsiXCLogicalIfLow_Object=MibTableColumn
vsiXCLogicalIfLow=_VsiXCLogicalIfLow_Object((1,3,6,1,4,1,9,9,162,1,4,1,2),_VsiXCLogicalIfLow_Type())
vsiXCLogicalIfLow.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiXCLogicalIfLow.setStatus(_B)
_VsiXCLogicalIfHi_Type=VsiLogicalIfIndex
_VsiXCLogicalIfHi_Object=MibTableColumn
vsiXCLogicalIfHi=_VsiXCLogicalIfHi_Object((1,3,6,1,4,1,9,9,162,1,4,1,3),_VsiXCLogicalIfHi_Type())
vsiXCLogicalIfHi.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiXCLogicalIfHi.setStatus(_B)
_VsiXCIndex_Type=VsiXCIndex
_VsiXCIndex_Object=MibTableColumn
vsiXCIndex=_VsiXCIndex_Object((1,3,6,1,4,1,9,9,162,1,4,1,4),_VsiXCIndex_Type())
vsiXCIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiXCIndex.setStatus(_B)
class _VsiXCState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('deleted',1),('reserved',2),('committed',3),('reservedFail',4)))
_VsiXCState_Type.__name__=_D
_VsiXCState_Object=MibTableColumn
vsiXCState=_VsiXCState_Object((1,3,6,1,4,1,9,9,162,1,4,1,5),_VsiXCState_Type())
vsiXCState.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiXCState.setStatus(_B)
class _VsiXCVpiLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VsiXCVpiLow_Type.__name__=_D
_VsiXCVpiLow_Object=MibTableColumn
vsiXCVpiLow=_VsiXCVpiLow_Object((1,3,6,1,4,1,9,9,162,1,4,1,6),_VsiXCVpiLow_Type())
vsiXCVpiLow.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiXCVpiLow.setStatus(_B)
class _VsiXCVciLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VsiXCVciLow_Type.__name__=_D
_VsiXCVciLow_Object=MibTableColumn
vsiXCVciLow=_VsiXCVciLow_Object((1,3,6,1,4,1,9,9,162,1,4,1,7),_VsiXCVciLow_Type())
vsiXCVciLow.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiXCVciLow.setStatus(_B)
class _VsiXCVpiHi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VsiXCVpiHi_Type.__name__=_D
_VsiXCVpiHi_Object=MibTableColumn
vsiXCVpiHi=_VsiXCVpiHi_Object((1,3,6,1,4,1,9,9,162,1,4,1,8),_VsiXCVpiHi_Type())
vsiXCVpiHi.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiXCVpiHi.setStatus(_B)
class _VsiXCVciHi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VsiXCVciHi_Type.__name__=_D
_VsiXCVciHi_Object=MibTableColumn
vsiXCVciHi=_VsiXCVciHi_Object((1,3,6,1,4,1,9,9,162,1,4,1,9),_VsiXCVciHi_Type())
vsiXCVciHi.setMaxAccess(_C)
if mibBuilder.loadTexts:vsiXCVciHi.setStatus(_B)
class _VsiControllerTrapEnable_Type(TruthValue):defaultValue=2
_VsiControllerTrapEnable_Type.__name__=_F
_VsiControllerTrapEnable_Object=MibScalar
vsiControllerTrapEnable=_VsiControllerTrapEnable_Object((1,3,6,1,4,1,9,9,162,1,5),_VsiControllerTrapEnable_Type())
vsiControllerTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:vsiControllerTrapEnable.setStatus(_B)
class _VsiSessionTrapEnable_Type(TruthValue):defaultValue=2
_VsiSessionTrapEnable_Type.__name__=_F
_VsiSessionTrapEnable_Object=MibScalar
vsiSessionTrapEnable=_VsiSessionTrapEnable_Object((1,3,6,1,4,1,9,9,162,1,6),_VsiSessionTrapEnable_Type())
vsiSessionTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:vsiSessionTrapEnable.setStatus(_B)
class _VsiLogicalIfTrapEnable_Type(TruthValue):defaultValue=2
_VsiLogicalIfTrapEnable_Type.__name__=_F
_VsiLogicalIfTrapEnable_Object=MibScalar
vsiLogicalIfTrapEnable=_VsiLogicalIfTrapEnable_Object((1,3,6,1,4,1,9,9,162,1,7),_VsiLogicalIfTrapEnable_Type())
vsiLogicalIfTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:vsiLogicalIfTrapEnable.setStatus(_B)
class _VsiXCTrapEnable_Type(TruthValue):defaultValue=2
_VsiXCTrapEnable_Type.__name__=_F
_VsiXCTrapEnable_Object=MibScalar
vsiXCTrapEnable=_VsiXCTrapEnable_Object((1,3,6,1,4,1,9,9,162,1,8),_VsiXCTrapEnable_Type())
vsiXCTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:vsiXCTrapEnable.setStatus(_B)
class _VsiVSITrapEnable_Type(TruthValue):defaultValue=2
_VsiVSITrapEnable_Type.__name__=_F
_VsiVSITrapEnable_Object=MibScalar
vsiVSITrapEnable=_VsiVSITrapEnable_Object((1,3,6,1,4,1,9,9,162,1,9),_VsiVSITrapEnable_Type())
vsiVSITrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:vsiVSITrapEnable.setStatus(_B)
_CiscoVsiMasterNotifications_ObjectIdentity=ObjectIdentity
ciscoVsiMasterNotifications=_CiscoVsiMasterNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,162,2))
_CiscoVsiMasterConformance_ObjectIdentity=ObjectIdentity
ciscoVsiMasterConformance=_CiscoVsiMasterConformance_ObjectIdentity((1,3,6,1,4,1,9,9,162,3))
_CiscoVsiMasterGroups_ObjectIdentity=ObjectIdentity
ciscoVsiMasterGroups=_CiscoVsiMasterGroups_ObjectIdentity((1,3,6,1,4,1,9,9,162,3,1))
_CiscoVsiMasterCompliances_ObjectIdentity=ObjectIdentity
ciscoVsiMasterCompliances=_CiscoVsiMasterCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,162,3,2))
ciscoVsiMasterGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,9,162,3,1,1))
ciscoVsiMasterGeneralGroup.setObjects(*((_A,_G),(_A,_W),(_A,_X),(_A,_K),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_L),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_N),(_A,_O),(_A,_n),(_A,_M),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_H),(_A,_I),(_A,_J),(_A,_P),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:ciscoVsiMasterGeneralGroup.setStatus(_B)
ciscoVsi2MasterGroup=ObjectGroup((1,3,6,1,4,1,9,9,162,3,1,2))
ciscoVsi2MasterGroup.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ),(_A,_Q)))
if mibBuilder.loadTexts:ciscoVsi2MasterGroup.setStatus(_B)
ciscoVsi2AlarmControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,162,3,1,3))
ciscoVsi2AlarmControlGroup.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:ciscoVsi2AlarmControlGroup.setStatus(_B)
vsiControllerAdded=NotificationType((1,3,6,1,4,1,9,9,162,2,1))
vsiControllerAdded.setObjects((_A,_K))
if mibBuilder.loadTexts:vsiControllerAdded.setStatus(_B)
vsiControllerDeleted=NotificationType((1,3,6,1,4,1,9,9,162,2,2))
vsiControllerDeleted.setObjects((_A,_K))
if mibBuilder.loadTexts:vsiControllerDeleted.setStatus(_B)
vsiSessionUp=NotificationType((1,3,6,1,4,1,9,9,162,2,3))
vsiSessionUp.setObjects((_A,_L))
if mibBuilder.loadTexts:vsiSessionUp.setStatus(_B)
vsiSessionDown=NotificationType((1,3,6,1,4,1,9,9,162,2,4))
vsiSessionDown.setObjects((_A,_L))
if mibBuilder.loadTexts:vsiSessionDown.setStatus(_B)
vsiLogicalIfUp=NotificationType((1,3,6,1,4,1,9,9,162,2,5))
vsiLogicalIfUp.setObjects((_A,_M))
if mibBuilder.loadTexts:vsiLogicalIfUp.setStatus(_B)
vsiLogicalIfDown=NotificationType((1,3,6,1,4,1,9,9,162,2,6))
vsiLogicalIfDown.setObjects((_A,_M))
if mibBuilder.loadTexts:vsiLogicalIfDown.setStatus(_B)
vsiXCFailed=NotificationType((1,3,6,1,4,1,9,9,162,2,7))
vsiXCFailed.setObjects(*((_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:vsiXCFailed.setStatus(_B)
vsiLcnExhaustionNotice=NotificationType((1,3,6,1,4,1,9,9,162,2,8))
vsiLcnExhaustionNotice.setObjects(*((_A,_G),(_A,_Q)))
if mibBuilder.loadTexts:vsiLcnExhaustionNotice.setStatus(_B)
ciscoVsi2MasterNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,162,3,1,4))
ciscoVsi2MasterNotificationGroup.setObjects(*((_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:ciscoVsi2MasterNotificationGroup.setStatus(_B)
ciscoVsiMasterModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,162,3,2,1))
ciscoVsiMasterModuleCompliance.setObjects((_A,_R))
if mibBuilder.loadTexts:ciscoVsiMasterModuleCompliance.setStatus('deprecated')
ciscoVsi2MasterModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,162,3,2,2))
ciscoVsi2MasterModuleCompliance.setObjects(*((_A,_R),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:ciscoVsi2MasterModuleCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VsiControllerIndex':VsiControllerIndex,'VsiSessionIndex':VsiSessionIndex,'VsiLogicalIfIndex':VsiLogicalIfIndex,'VsiXCIndex':VsiXCIndex,'ciscoVsiMasterMIB':ciscoVsiMasterMIB,'ciscoVsiMasterObjects':ciscoVsiMasterObjects,'vsiMasterControllerTable':vsiMasterControllerTable,'vsiMasterControllerEntry':vsiMasterControllerEntry,_G:vsiControllerIndex,_W:vsiControllerId,_X:vsiCrossConnects,_K:vsiControllerType,_Y:vsiBaseVersionSupported,_Z:vsiTopVersionSupported,_a:vsiVersionInUse,_b:vsiSpecifiedVersion,_c:vsiControlInterface,_d:vsiLogicalControlInterface,_AH:vsiControlIfIpAddress,_AI:vsiAvailableChnlWarnThreshold,_AJ:vsiAvailableChnlAlarmThreshold,_Q:vsiAvailableChnlThresholdStatus,'vsiSessionTable':vsiSessionTable,'vsiSessionEntry':vsiSessionEntry,_T:vsiSessionControllerIndex,_U:vsiSessionIndex,_e:vsiSessionVpi,_f:vsiSessionVci,_g:vsiSessionSwitchId,_h:vsiSessionSwitchName,_i:vsiSessionSlaveId,_L:vsiSessionState,_j:vsiSessionWindowSize,_k:vsiSessionCmdsPending,_l:vsiSessionActiveId,_m:vsiSessionPowerupId,'vsiLogicalIfTable':vsiLogicalIfTable,'vsiLogicalIfEntry':vsiLogicalIfEntry,_N:vsiLogicalIfControllerIndex,_O:vsiLogicalIfIndex,_n:vsiLogicalIfName,_M:vsiLogicalIfOperState,_o:vsiLogicalIfAdminState,_p:vsiLogicalIfRxCells,_q:vsiLogicalIfTxCells,_r:vsiLogicalIfRxCellsDiscarded,_s:vsiLogicalIfTxCellsDiscarded,_t:vsiLogicalIfRxHeaderErrors,_u:vsiLogicalIfRxInvalidAddrs,_v:vsiLogicalIfEndPointsInUse,_w:vsiLogicalIfAvailIngressChnls,_x:vsiLogicalIfAvailEgressChnls,_y:vsiLogicalIfAvailIngressCellRate,_z:vsiLogicalIfAvailEgressCellRate,_A2:vsiLogicalIfVcMergeSupported,_A3:vsiLogicalIfMulticastSupported,_A4:vsiLogicalIfVpiTranslated,_A5:vsiLogicalIfStrictSigRange,_A0:vsiLogicalIfMaxIngressCellRate,_A1:vsiLogicalIfMaxEgressCellRate,_A6:vsiLogicalIfMinVpi,_A7:vsiLogicalIfMaxVpi,_A8:vsiLogicalIfMinVci,_A9:vsiLogicalIfMaxVci,_AA:vsiLogicalControlIfIndex,_AB:vsiLogicalIfSessionIndex,'vsiXCTable':vsiXCTable,'vsiXCEntry':vsiXCEntry,_H:vsiXCControllerIndex,_I:vsiXCLogicalIfLow,_J:vsiXCLogicalIfHi,_P:vsiXCIndex,_AC:vsiXCState,_AD:vsiXCVpiLow,_AE:vsiXCVciLow,_AF:vsiXCVpiHi,_AG:vsiXCVciHi,_AK:vsiControllerTrapEnable,_AL:vsiSessionTrapEnable,_AM:vsiLogicalIfTrapEnable,_AN:vsiXCTrapEnable,_AO:vsiVSITrapEnable,'ciscoVsiMasterNotifications':ciscoVsiMasterNotifications,_AP:vsiControllerAdded,_AQ:vsiControllerDeleted,_AR:vsiSessionUp,_AS:vsiSessionDown,_AT:vsiLogicalIfUp,_AU:vsiLogicalIfDown,_AV:vsiXCFailed,_AW:vsiLcnExhaustionNotice,'ciscoVsiMasterConformance':ciscoVsiMasterConformance,'ciscoVsiMasterGroups':ciscoVsiMasterGroups,_R:ciscoVsiMasterGeneralGroup,_AX:ciscoVsi2MasterGroup,_AY:ciscoVsi2AlarmControlGroup,_AZ:ciscoVsi2MasterNotificationGroup,'ciscoVsiMasterCompliances':ciscoVsiMasterCompliances,'ciscoVsiMasterModuleCompliance':ciscoVsiMasterModuleCompliance,'ciscoVsi2MasterModuleCompliance':ciscoVsi2MasterModuleCompliance})