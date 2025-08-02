_O='cienaCesExtAggRedundancyState'
_N='cienaCesExtAggIndex'
_M='cienaCesLagProtectionPort'
_L='DisplayString'
_K='Unsigned32'
_J='cienaGlobalSeverity'
_I='cienaGlobalMacAddress'
_H='down'
_G='cienaCesExtAggId'
_F='CIENA-GLOBAL-MIB'
_E='none'
_D='CIENA-CES-EXT-LAG-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaGlobalMacAddress,cienaGlobalSeverity=mibBuilder.importSymbols(_F,_I,_J)
cienaCesConfig,cienaCesNotifications=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'MacAddress','PhysAddress','RowStatus','TextualConvention')
cienaCesExtLagMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,3))
if mibBuilder.loadTexts:cienaCesExtLagMIB.setRevisions(('2018-02-13 00:00','2017-06-07 00:00','2016-09-28 00:00','2016-09-16 00:00','2016-09-14 00:00','2016-09-07 00:00','2016-08-10 00:00'))
_CienaCesExtLagMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesExtLagMIBObjects=_CienaCesExtLagMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,3,1))
_CienaCesExtLag_ObjectIdentity=ObjectIdentity
cienaCesExtLag=_CienaCesExtLag_ObjectIdentity((1,3,6,1,4,1,1271,2,1,3,1,1))
_CienaCesMaxLags_Type=Unsigned32
_CienaCesMaxLags_Object=MibScalar
cienaCesMaxLags=_CienaCesMaxLags_Object((1,3,6,1,4,1,1271,2,1,3,1,1,1),_CienaCesMaxLags_Type())
cienaCesMaxLags.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesMaxLags.setStatus(_A)
_CienaCesNumLags_Type=Unsigned32
_CienaCesNumLags_Object=MibScalar
cienaCesNumLags=_CienaCesNumLags_Object((1,3,6,1,4,1,1271,2,1,3,1,1,2),_CienaCesNumLags_Type())
cienaCesNumLags.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesNumLags.setStatus(_A)
_CienaCesExtLagTable_Object=MibTable
cienaCesExtLagTable=_CienaCesExtLagTable_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3))
if mibBuilder.loadTexts:cienaCesExtLagTable.setStatus(_A)
_CienaCesExtLagEntry_Object=MibTableRow
cienaCesExtLagEntry=_CienaCesExtLagEntry_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1))
cienaCesExtLagEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:cienaCesExtLagEntry.setStatus(_A)
class _CienaCesExtAggId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CienaCesExtAggId_Type.__name__=_C
_CienaCesExtAggId_Object=MibTableColumn
cienaCesExtAggId=_CienaCesExtAggId_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,1),_CienaCesExtAggId_Type())
cienaCesExtAggId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggId.setStatus(_A)
class _CienaCesExtAggName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CienaCesExtAggName_Type.__name__=_L
_CienaCesExtAggName_Object=MibTableColumn
cienaCesExtAggName=_CienaCesExtAggName_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,2),_CienaCesExtAggName_Type())
cienaCesExtAggName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggName.setStatus(_A)
class _CienaCesExtAggIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CienaCesExtAggIndex_Type.__name__=_C
_CienaCesExtAggIndex_Object=MibTableColumn
cienaCesExtAggIndex=_CienaCesExtAggIndex_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,3),_CienaCesExtAggIndex_Type())
cienaCesExtAggIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggIndex.setStatus(_A)
class _CienaCesExtAggMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lacp',1),('manual',2)))
_CienaCesExtAggMode_Type.__name__=_C
_CienaCesExtAggMode_Object=MibTableColumn
cienaCesExtAggMode=_CienaCesExtAggMode_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,4),_CienaCesExtAggMode_Type())
cienaCesExtAggMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggMode.setStatus(_A)
class _CienaCesExtLagProtectionRevertState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CienaCesExtLagProtectionRevertState_Type.__name__=_C
_CienaCesExtLagProtectionRevertState_Object=MibTableColumn
cienaCesExtLagProtectionRevertState=_CienaCesExtLagProtectionRevertState_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,5),_CienaCesExtLagProtectionRevertState_Type())
cienaCesExtLagProtectionRevertState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtLagProtectionRevertState.setStatus(_A)
class _CienaCesExtLagProtectionRevertTimer_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_CienaCesExtLagProtectionRevertTimer_Type.__name__=_C
_CienaCesExtLagProtectionRevertTimer_Object=MibTableColumn
cienaCesExtLagProtectionRevertTimer=_CienaCesExtLagProtectionRevertTimer_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,6),_CienaCesExtLagProtectionRevertTimer_Type())
cienaCesExtLagProtectionRevertTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtLagProtectionRevertTimer.setStatus(_A)
if mibBuilder.loadTexts:cienaCesExtLagProtectionRevertTimer.setUnits('msec')
_CienaCesExtAggTotalAddedPorts_Type=Unsigned32
_CienaCesExtAggTotalAddedPorts_Object=MibTableColumn
cienaCesExtAggTotalAddedPorts=_CienaCesExtAggTotalAddedPorts_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,7),_CienaCesExtAggTotalAddedPorts_Type())
cienaCesExtAggTotalAddedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggTotalAddedPorts.setStatus(_A)
_CienaCesExtAggTotalProtectionPorts_Type=Unsigned32
_CienaCesExtAggTotalProtectionPorts_Object=MibTableColumn
cienaCesExtAggTotalProtectionPorts=_CienaCesExtAggTotalProtectionPorts_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,8),_CienaCesExtAggTotalProtectionPorts_Type())
cienaCesExtAggTotalProtectionPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggTotalProtectionPorts.setStatus(_A)
class _CienaCesExtLagProtectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('proprietary',1),('standard',2),(_E,3)))
_CienaCesExtLagProtectionMode_Type.__name__=_C
_CienaCesExtLagProtectionMode_Object=MibTableColumn
cienaCesExtLagProtectionMode=_CienaCesExtLagProtectionMode_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,9),_CienaCesExtLagProtectionMode_Type())
cienaCesExtLagProtectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtLagProtectionMode.setStatus(_A)
_CienaCesExtAggICL_Type=DisplayString
_CienaCesExtAggICL_Object=MibTableColumn
cienaCesExtAggICL=_CienaCesExtAggICL_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,10),_CienaCesExtAggICL_Type())
cienaCesExtAggICL.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggICL.setStatus(_A)
class _CienaCesExtAggRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('backup',2),(_E,3)))
_CienaCesExtAggRole_Type.__name__=_C
_CienaCesExtAggRole_Object=MibTableColumn
cienaCesExtAggRole=_CienaCesExtAggRole_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,11),_CienaCesExtAggRole_Type())
cienaCesExtAggRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggRole.setStatus(_A)
_CienaCesExtAggRgNodeId_Type=Unsigned32
_CienaCesExtAggRgNodeId_Object=MibTableColumn
cienaCesExtAggRgNodeId=_CienaCesExtAggRgNodeId_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,12),_CienaCesExtAggRgNodeId_Type())
cienaCesExtAggRgNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggRgNodeId.setStatus(_A)
_CienaCesExtAggRgDynamicPriority_Type=Unsigned32
_CienaCesExtAggRgDynamicPriority_Object=MibTableColumn
cienaCesExtAggRgDynamicPriority=_CienaCesExtAggRgDynamicPriority_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,13),_CienaCesExtAggRgDynamicPriority_Type())
cienaCesExtAggRgDynamicPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggRgDynamicPriority.setStatus(_A)
_CienaCesExtAggRgOperKey_Type=Unsigned32
_CienaCesExtAggRgOperKey_Object=MibTableColumn
cienaCesExtAggRgOperKey=_CienaCesExtAggRgOperKey_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,14),_CienaCesExtAggRgOperKey_Type())
cienaCesExtAggRgOperKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggRgOperKey.setStatus(_A)
class _CienaCesExtAggRedundancyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),('unavailable',2),('active',3),('standby',4),('standalone',5),(_E,6)))
_CienaCesExtAggRedundancyState_Type.__name__=_C
_CienaCesExtAggRedundancyState_Object=MibTableColumn
cienaCesExtAggRedundancyState=_CienaCesExtAggRedundancyState_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,15),_CienaCesExtAggRedundancyState_Type())
cienaCesExtAggRedundancyState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggRedundancyState.setStatus(_A)
class _CienaCesExtAggConnectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('init',1),('disconnected',2),('connected',3),('mismatch',4),(_E,5)))
_CienaCesExtAggConnectState_Type.__name__=_C
_CienaCesExtAggConnectState_Object=MibTableColumn
cienaCesExtAggConnectState=_CienaCesExtAggConnectState_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,16),_CienaCesExtAggConnectState_Type())
cienaCesExtAggConnectState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggConnectState.setStatus(_A)
class _CienaCesExtAggRgMismatchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('no',1),('rgpeer',2),('partner',3),('version',4),(_E,5)))
_CienaCesExtAggRgMismatchStatus_Type.__name__=_C
_CienaCesExtAggRgMismatchStatus_Object=MibTableColumn
cienaCesExtAggRgMismatchStatus=_CienaCesExtAggRgMismatchStatus_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,17),_CienaCesExtAggRgMismatchStatus_Type())
cienaCesExtAggRgMismatchStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggRgMismatchStatus.setStatus(_A)
_CienaCesExtAggPeerSystemMac_Type=MacAddress
_CienaCesExtAggPeerSystemMac_Object=MibTableColumn
cienaCesExtAggPeerSystemMac=_CienaCesExtAggPeerSystemMac_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,18),_CienaCesExtAggPeerSystemMac_Type())
cienaCesExtAggPeerSystemMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggPeerSystemMac.setStatus(_A)
_CienaCesExtAggPeerRgNodeId_Type=Unsigned32
_CienaCesExtAggPeerRgNodeId_Object=MibTableColumn
cienaCesExtAggPeerRgNodeId=_CienaCesExtAggPeerRgNodeId_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,19),_CienaCesExtAggPeerRgNodeId_Type())
cienaCesExtAggPeerRgNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggPeerRgNodeId.setStatus(_A)
_CienaCesExtAggPeerRgDynamicPriority_Type=Unsigned32
_CienaCesExtAggPeerRgDynamicPriority_Object=MibTableColumn
cienaCesExtAggPeerRgDynamicPriority=_CienaCesExtAggPeerRgDynamicPriority_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,20),_CienaCesExtAggPeerRgDynamicPriority_Type())
cienaCesExtAggPeerRgDynamicPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggPeerRgDynamicPriority.setStatus(_A)
_CienaCesExtAggPeerRgOperKey_Type=Unsigned32
_CienaCesExtAggPeerRgOperKey_Object=MibTableColumn
cienaCesExtAggPeerRgOperKey=_CienaCesExtAggPeerRgOperKey_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,21),_CienaCesExtAggPeerRgOperKey_Type())
cienaCesExtAggPeerRgOperKey.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggPeerRgOperKey.setStatus(_A)
_CienaCesExtAggPeerRgNumAddedPorts_Type=Unsigned32
_CienaCesExtAggPeerRgNumAddedPorts_Object=MibTableColumn
cienaCesExtAggPeerRgNumAddedPorts=_CienaCesExtAggPeerRgNumAddedPorts_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,22),_CienaCesExtAggPeerRgNumAddedPorts_Type())
cienaCesExtAggPeerRgNumAddedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggPeerRgNumAddedPorts.setStatus(_A)
_CienaCesExtAggPeerRgNumAvailablePorts_Type=Unsigned32
_CienaCesExtAggPeerRgNumAvailablePorts_Object=MibTableColumn
cienaCesExtAggPeerRgNumAvailablePorts=_CienaCesExtAggPeerRgNumAvailablePorts_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,23),_CienaCesExtAggPeerRgNumAvailablePorts_Type())
cienaCesExtAggPeerRgNumAvailablePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggPeerRgNumAvailablePorts.setStatus(_A)
_CienaCesExtAggDisconnectRx_Type=Counter32
_CienaCesExtAggDisconnectRx_Object=MibTableColumn
cienaCesExtAggDisconnectRx=_CienaCesExtAggDisconnectRx_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,24),_CienaCesExtAggDisconnectRx_Type())
cienaCesExtAggDisconnectRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggDisconnectRx.setStatus(_A)
_CienaCesExtAggDisconnectTx_Type=Counter32
_CienaCesExtAggDisconnectTx_Object=MibTableColumn
cienaCesExtAggDisconnectTx=_CienaCesExtAggDisconnectTx_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,25),_CienaCesExtAggDisconnectTx_Type())
cienaCesExtAggDisconnectTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggDisconnectTx.setStatus(_A)
_CienaCesExtAggConfigMismatchRx_Type=Counter32
_CienaCesExtAggConfigMismatchRx_Object=MibTableColumn
cienaCesExtAggConfigMismatchRx=_CienaCesExtAggConfigMismatchRx_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,26),_CienaCesExtAggConfigMismatchRx_Type())
cienaCesExtAggConfigMismatchRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggConfigMismatchRx.setStatus(_A)
_CienaCesExtAggKeyMismatchCount_Type=Counter32
_CienaCesExtAggKeyMismatchCount_Object=MibTableColumn
cienaCesExtAggKeyMismatchCount=_CienaCesExtAggKeyMismatchCount_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,27),_CienaCesExtAggKeyMismatchCount_Type())
cienaCesExtAggKeyMismatchCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggKeyMismatchCount.setStatus(_A)
_CienaCesExtAggOutOfSequenceRx_Type=Counter32
_CienaCesExtAggOutOfSequenceRx_Object=MibTableColumn
cienaCesExtAggOutOfSequenceRx=_CienaCesExtAggOutOfSequenceRx_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,28),_CienaCesExtAggOutOfSequenceRx_Type())
cienaCesExtAggOutOfSequenceRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggOutOfSequenceRx.setStatus(_A)
_CienaCesExtAggPeerUnreachableCount_Type=Counter32
_CienaCesExtAggPeerUnreachableCount_Object=MibTableColumn
cienaCesExtAggPeerUnreachableCount=_CienaCesExtAggPeerUnreachableCount_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,29),_CienaCesExtAggPeerUnreachableCount_Type())
cienaCesExtAggPeerUnreachableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggPeerUnreachableCount.setStatus(_A)
_CienaCesExtAggUnknownRx_Type=Counter32
_CienaCesExtAggUnknownRx_Object=MibTableColumn
cienaCesExtAggUnknownRx=_CienaCesExtAggUnknownRx_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,30),_CienaCesExtAggUnknownRx_Type())
cienaCesExtAggUnknownRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggUnknownRx.setStatus(_A)
_CienaCesExtAggTotalRx_Type=Counter32
_CienaCesExtAggTotalRx_Object=MibTableColumn
cienaCesExtAggTotalRx=_CienaCesExtAggTotalRx_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,31),_CienaCesExtAggTotalRx_Type())
cienaCesExtAggTotalRx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggTotalRx.setStatus(_A)
_CienaCesExtAggTotalTx_Type=Counter32
_CienaCesExtAggTotalTx_Object=MibTableColumn
cienaCesExtAggTotalTx=_CienaCesExtAggTotalTx_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,32),_CienaCesExtAggTotalTx_Type())
cienaCesExtAggTotalTx.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggTotalTx.setStatus(_A)
_CienaCesExtAggTotalDownTime_Type=Unsigned32
_CienaCesExtAggTotalDownTime_Object=MibTableColumn
cienaCesExtAggTotalDownTime=_CienaCesExtAggTotalDownTime_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,33),_CienaCesExtAggTotalDownTime_Type())
cienaCesExtAggTotalDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggTotalDownTime.setStatus(_A)
_CienaCesExtAggUpTime_Type=Unsigned32
_CienaCesExtAggUpTime_Object=MibTableColumn
cienaCesExtAggUpTime=_CienaCesExtAggUpTime_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,34),_CienaCesExtAggUpTime_Type())
cienaCesExtAggUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggUpTime.setStatus(_A)
_CienaCesExtAggTimeInProtectState_Type=Unsigned32
_CienaCesExtAggTimeInProtectState_Object=MibTableColumn
cienaCesExtAggTimeInProtectState=_CienaCesExtAggTimeInProtectState_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,35),_CienaCesExtAggTimeInProtectState_Type())
cienaCesExtAggTimeInProtectState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggTimeInProtectState.setStatus(_A)
_CienaCesExtAggLastTimeProtected_Type=Unsigned32
_CienaCesExtAggLastTimeProtected_Object=MibTableColumn
cienaCesExtAggLastTimeProtected=_CienaCesExtAggLastTimeProtected_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,36),_CienaCesExtAggLastTimeProtected_Type())
cienaCesExtAggLastTimeProtected.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggLastTimeProtected.setStatus(_A)
_CienaCesExtAggNumberOfSwitchovers_Type=Counter32
_CienaCesExtAggNumberOfSwitchovers_Object=MibTableColumn
cienaCesExtAggNumberOfSwitchovers=_CienaCesExtAggNumberOfSwitchovers_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,37),_CienaCesExtAggNumberOfSwitchovers_Type())
cienaCesExtAggNumberOfSwitchovers.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggNumberOfSwitchovers.setStatus(_A)
class _CienaCesExtAggMultiChassis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_CienaCesExtAggMultiChassis_Type.__name__=_C
_CienaCesExtAggMultiChassis_Object=MibTableColumn
cienaCesExtAggMultiChassis=_CienaCesExtAggMultiChassis_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,38),_CienaCesExtAggMultiChassis_Type())
cienaCesExtAggMultiChassis.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggMultiChassis.setStatus(_A)
class _CienaCesExtAggMinimumLinkAggregation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CienaCesExtAggMinimumLinkAggregation_Type.__name__=_C
_CienaCesExtAggMinimumLinkAggregation_Object=MibTableColumn
cienaCesExtAggMinimumLinkAggregation=_CienaCesExtAggMinimumLinkAggregation_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,39),_CienaCesExtAggMinimumLinkAggregation_Type())
cienaCesExtAggMinimumLinkAggregation.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggMinimumLinkAggregation.setStatus(_A)
class _CienaCesExtAggMinimumLinkThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CienaCesExtAggMinimumLinkThreshold_Type.__name__=_C
_CienaCesExtAggMinimumLinkThreshold_Object=MibTableColumn
cienaCesExtAggMinimumLinkThreshold=_CienaCesExtAggMinimumLinkThreshold_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,40),_CienaCesExtAggMinimumLinkThreshold_Type())
cienaCesExtAggMinimumLinkThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggMinimumLinkThreshold.setStatus(_A)
class _CienaCesExtAggAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_H,2)))
_CienaCesExtAggAdminState_Type.__name__=_C
_CienaCesExtAggAdminState_Object=MibTableColumn
cienaCesExtAggAdminState=_CienaCesExtAggAdminState_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,41),_CienaCesExtAggAdminState_Type())
cienaCesExtAggAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggAdminState.setStatus(_A)
class _CienaCesExtAggOperState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_H,2)))
_CienaCesExtAggOperState_Type.__name__=_C
_CienaCesExtAggOperState_Object=MibTableColumn
cienaCesExtAggOperState=_CienaCesExtAggOperState_Object((1,3,6,1,4,1,1271,2,1,3,1,1,3,1,42),_CienaCesExtAggOperState_Type())
cienaCesExtAggOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggOperState.setStatus(_A)
_CienaCesLagProtectionTable_Object=MibTable
cienaCesLagProtectionTable=_CienaCesLagProtectionTable_Object((1,3,6,1,4,1,1271,2,1,3,1,1,4))
if mibBuilder.loadTexts:cienaCesLagProtectionTable.setStatus(_A)
_CienaCesLagProtectionEntry_Object=MibTableRow
cienaCesLagProtectionEntry=_CienaCesLagProtectionEntry_Object((1,3,6,1,4,1,1271,2,1,3,1,1,4,1))
cienaCesLagProtectionEntry.setIndexNames((0,_D,_G),(0,_D,_M))
if mibBuilder.loadTexts:cienaCesLagProtectionEntry.setStatus(_A)
class _CienaCesLagProtectionPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CienaCesLagProtectionPort_Type.__name__=_C
_CienaCesLagProtectionPort_Object=MibTableColumn
cienaCesLagProtectionPort=_CienaCesLagProtectionPort_Object((1,3,6,1,4,1,1271,2,1,3,1,1,4,1,1),_CienaCesLagProtectionPort_Type())
cienaCesLagProtectionPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesLagProtectionPort.setStatus(_A)
class _CienaCesExtAggMarkerTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CienaCesExtAggMarkerTimeout_Type.__name__=_K
_CienaCesExtAggMarkerTimeout_Object=MibScalar
cienaCesExtAggMarkerTimeout=_CienaCesExtAggMarkerTimeout_Object((1,3,6,1,4,1,1271,2,1,3,1,1,5),_CienaCesExtAggMarkerTimeout_Type())
cienaCesExtAggMarkerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesExtAggMarkerTimeout.setStatus(_A)
if mibBuilder.loadTexts:cienaCesExtAggMarkerTimeout.setUnits('msec')
_CienaCesExtLagMIBConformance_ObjectIdentity=ObjectIdentity
cienaCesExtLagMIBConformance=_CienaCesExtLagMIBConformance_ObjectIdentity((1,3,6,1,4,1,1271,2,1,3,2))
_CienaCesExtLagMIBCompliances_ObjectIdentity=ObjectIdentity
cienaCesExtLagMIBCompliances=_CienaCesExtLagMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1271,2,1,3,2,1))
_CienaCesExtLagMIBGroups_ObjectIdentity=ObjectIdentity
cienaCesExtLagMIBGroups=_CienaCesExtLagMIBGroups_ObjectIdentity((1,3,6,1,4,1,1271,2,1,3,2,2))
_CienaCesExtLagMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cienaCesExtLagMIBNotificationPrefix=_CienaCesExtLagMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,2,21))
_CienaCesExtLagMIBNotifications_ObjectIdentity=ObjectIdentity
cienaCesExtLagMIBNotifications=_CienaCesExtLagMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,2,21,0))
cienaCesExtLagMclagStateChange=NotificationType((1,3,6,1,4,1,1271,2,2,21,0,1))
cienaCesExtLagMclagStateChange.setObjects(*((_F,_J),(_F,_I),(_D,_N),(_D,_O)))
if mibBuilder.loadTexts:cienaCesExtLagMclagStateChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cienaCesExtLagMIB':cienaCesExtLagMIB,'cienaCesExtLagMIBObjects':cienaCesExtLagMIBObjects,'cienaCesExtLag':cienaCesExtLag,'cienaCesMaxLags':cienaCesMaxLags,'cienaCesNumLags':cienaCesNumLags,'cienaCesExtLagTable':cienaCesExtLagTable,'cienaCesExtLagEntry':cienaCesExtLagEntry,_G:cienaCesExtAggId,'cienaCesExtAggName':cienaCesExtAggName,_N:cienaCesExtAggIndex,'cienaCesExtAggMode':cienaCesExtAggMode,'cienaCesExtLagProtectionRevertState':cienaCesExtLagProtectionRevertState,'cienaCesExtLagProtectionRevertTimer':cienaCesExtLagProtectionRevertTimer,'cienaCesExtAggTotalAddedPorts':cienaCesExtAggTotalAddedPorts,'cienaCesExtAggTotalProtectionPorts':cienaCesExtAggTotalProtectionPorts,'cienaCesExtLagProtectionMode':cienaCesExtLagProtectionMode,'cienaCesExtAggICL':cienaCesExtAggICL,'cienaCesExtAggRole':cienaCesExtAggRole,'cienaCesExtAggRgNodeId':cienaCesExtAggRgNodeId,'cienaCesExtAggRgDynamicPriority':cienaCesExtAggRgDynamicPriority,'cienaCesExtAggRgOperKey':cienaCesExtAggRgOperKey,_O:cienaCesExtAggRedundancyState,'cienaCesExtAggConnectState':cienaCesExtAggConnectState,'cienaCesExtAggRgMismatchStatus':cienaCesExtAggRgMismatchStatus,'cienaCesExtAggPeerSystemMac':cienaCesExtAggPeerSystemMac,'cienaCesExtAggPeerRgNodeId':cienaCesExtAggPeerRgNodeId,'cienaCesExtAggPeerRgDynamicPriority':cienaCesExtAggPeerRgDynamicPriority,'cienaCesExtAggPeerRgOperKey':cienaCesExtAggPeerRgOperKey,'cienaCesExtAggPeerRgNumAddedPorts':cienaCesExtAggPeerRgNumAddedPorts,'cienaCesExtAggPeerRgNumAvailablePorts':cienaCesExtAggPeerRgNumAvailablePorts,'cienaCesExtAggDisconnectRx':cienaCesExtAggDisconnectRx,'cienaCesExtAggDisconnectTx':cienaCesExtAggDisconnectTx,'cienaCesExtAggConfigMismatchRx':cienaCesExtAggConfigMismatchRx,'cienaCesExtAggKeyMismatchCount':cienaCesExtAggKeyMismatchCount,'cienaCesExtAggOutOfSequenceRx':cienaCesExtAggOutOfSequenceRx,'cienaCesExtAggPeerUnreachableCount':cienaCesExtAggPeerUnreachableCount,'cienaCesExtAggUnknownRx':cienaCesExtAggUnknownRx,'cienaCesExtAggTotalRx':cienaCesExtAggTotalRx,'cienaCesExtAggTotalTx':cienaCesExtAggTotalTx,'cienaCesExtAggTotalDownTime':cienaCesExtAggTotalDownTime,'cienaCesExtAggUpTime':cienaCesExtAggUpTime,'cienaCesExtAggTimeInProtectState':cienaCesExtAggTimeInProtectState,'cienaCesExtAggLastTimeProtected':cienaCesExtAggLastTimeProtected,'cienaCesExtAggNumberOfSwitchovers':cienaCesExtAggNumberOfSwitchovers,'cienaCesExtAggMultiChassis':cienaCesExtAggMultiChassis,'cienaCesExtAggMinimumLinkAggregation':cienaCesExtAggMinimumLinkAggregation,'cienaCesExtAggMinimumLinkThreshold':cienaCesExtAggMinimumLinkThreshold,'cienaCesExtAggAdminState':cienaCesExtAggAdminState,'cienaCesExtAggOperState':cienaCesExtAggOperState,'cienaCesLagProtectionTable':cienaCesLagProtectionTable,'cienaCesLagProtectionEntry':cienaCesLagProtectionEntry,_M:cienaCesLagProtectionPort,'cienaCesExtAggMarkerTimeout':cienaCesExtAggMarkerTimeout,'cienaCesExtLagMIBConformance':cienaCesExtLagMIBConformance,'cienaCesExtLagMIBCompliances':cienaCesExtLagMIBCompliances,'cienaCesExtLagMIBGroups':cienaCesExtLagMIBGroups,'cienaCesExtLagMIBNotificationPrefix':cienaCesExtLagMIBNotificationPrefix,'cienaCesExtLagMIBNotifications':cienaCesExtLagMIBNotifications,'cienaCesExtLagMclagStateChange':cienaCesExtLagMclagStateChange})