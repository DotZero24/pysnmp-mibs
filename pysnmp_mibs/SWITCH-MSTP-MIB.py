_d='rcMstpPortBpduGuardStatus'
_c='rcMstpPortBpduGuardEnable'
_b='rcMstpXstPortLoopGuardState'
_a='rcMstpXstPortRootGuardState'
_Z='rcMstpXstPortState'
_Y='rcMstpXstPortCfgIndex'
_X='rcMstpXstPortCfgXstId'
_W='disabled'
_V='rcMstpCfgXstId'
_U='read-create'
_T='rcMstpXstInstanceEditId'
_S='rcMstpXstInstanceId'
_R='OctetString'
_Q='rcMstpXstId'
_P='yes'
_O='disable'
_N='enable'
_M='rcMstpPortIndex'
_L='DisplayString'
_K='Unsigned32'
_J='unknown'
_I='TruthValue'
_H='rcMstpXstPortIndex'
_G='rcMstpXstPortXstId'
_F='not-accessible'
_E='read-write'
_D='SWITCH-MSTP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_I)
Vlanset,=mibBuilder.importSymbols('SWITCH-TC','Vlanset')
rcMstp=ModuleIdentity((1,3,6,1,4,1,8886,6,1,24))
if mibBuilder.loadTexts:rcMstp.setRevisions(('2007-01-15 00:00',))
_RcMstpTraps_ObjectIdentity=ObjectIdentity
rcMstpTraps=_RcMstpTraps_ObjectIdentity((1,3,6,1,4,1,8886,6,1,24,1))
_RcMstpBridge_ObjectIdentity=ObjectIdentity
rcMstpBridge=_RcMstpBridge_ObjectIdentity((1,3,6,1,4,1,8886,6,1,24,2))
class _RcMstpBridgeAdminStp_Type(TruthValue):defaultValue=2
_RcMstpBridgeAdminStp_Type.__name__=_I
_RcMstpBridgeAdminStp_Object=MibScalar
rcMstpBridgeAdminStp=_RcMstpBridgeAdminStp_Object((1,3,6,1,4,1,8886,6,1,24,2,1),_RcMstpBridgeAdminStp_Type())
rcMstpBridgeAdminStp.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpBridgeAdminStp.setStatus(_A)
class _RcMstpBridgeMaxHops_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_RcMstpBridgeMaxHops_Type.__name__=_C
_RcMstpBridgeMaxHops_Object=MibScalar
rcMstpBridgeMaxHops=_RcMstpBridgeMaxHops_Object((1,3,6,1,4,1,8886,6,1,24,2,2),_RcMstpBridgeMaxHops_Type())
rcMstpBridgeMaxHops.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpBridgeMaxHops.setStatus(_A)
class _RcMstpBridgeVersionSupported_Type(Bits):namedValues=NamedValues(*(('nonStp',0),('dot1d1998',1),('dot1w',2),('dot1d2004',3),('dot1s',4),('dot1q',5),(_J,15)))
_RcMstpBridgeVersionSupported_Type.__name__='Bits'
_RcMstpBridgeVersionSupported_Object=MibScalar
rcMstpBridgeVersionSupported=_RcMstpBridgeVersionSupported_Object((1,3,6,1,4,1,8886,6,1,24,2,3),_RcMstpBridgeVersionSupported_Type())
rcMstpBridgeVersionSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpBridgeVersionSupported.setStatus(_A)
class _RcMstpBridgeProtocolVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,15)));namedValues=NamedValues(*(('forceNonStp',0),('forceLegacyDot1d',1),('forceDot1w',2),('autoDot1s',3),(_J,15)))
_RcMstpBridgeProtocolVersion_Type.__name__=_C
_RcMstpBridgeProtocolVersion_Object=MibScalar
rcMstpBridgeProtocolVersion=_RcMstpBridgeProtocolVersion_Object((1,3,6,1,4,1,8886,6,1,24,2,4),_RcMstpBridgeProtocolVersion_Type())
rcMstpBridgeProtocolVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpBridgeProtocolVersion.setStatus(_A)
class _RcMstpBridgeRegionFormatSelector_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcMstpBridgeRegionFormatSelector_Type.__name__=_C
_RcMstpBridgeRegionFormatSelector_Object=MibScalar
rcMstpBridgeRegionFormatSelector=_RcMstpBridgeRegionFormatSelector_Object((1,3,6,1,4,1,8886,6,1,24,2,5),_RcMstpBridgeRegionFormatSelector_Type())
rcMstpBridgeRegionFormatSelector.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpBridgeRegionFormatSelector.setStatus(_A)
class _RcMstpBridgeRegionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcMstpBridgeRegionName_Type.__name__=_L
_RcMstpBridgeRegionName_Object=MibScalar
rcMstpBridgeRegionName=_RcMstpBridgeRegionName_Object((1,3,6,1,4,1,8886,6,1,24,2,6),_RcMstpBridgeRegionName_Type())
rcMstpBridgeRegionName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpBridgeRegionName.setStatus(_A)
class _RcMstpBridgeRegionEditName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RcMstpBridgeRegionEditName_Type.__name__=_L
_RcMstpBridgeRegionEditName_Object=MibScalar
rcMstpBridgeRegionEditName=_RcMstpBridgeRegionEditName_Object((1,3,6,1,4,1,8886,6,1,24,2,7),_RcMstpBridgeRegionEditName_Type())
rcMstpBridgeRegionEditName.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpBridgeRegionEditName.setStatus(_A)
class _RcMstpBridgeRegionRevLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcMstpBridgeRegionRevLevel_Type.__name__=_C
_RcMstpBridgeRegionRevLevel_Object=MibScalar
rcMstpBridgeRegionRevLevel=_RcMstpBridgeRegionRevLevel_Object((1,3,6,1,4,1,8886,6,1,24,2,8),_RcMstpBridgeRegionRevLevel_Type())
rcMstpBridgeRegionRevLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpBridgeRegionRevLevel.setStatus(_A)
class _RcMstpBridgeRegionEditRevLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcMstpBridgeRegionEditRevLevel_Type.__name__=_C
_RcMstpBridgeRegionEditRevLevel_Object=MibScalar
rcMstpBridgeRegionEditRevLevel=_RcMstpBridgeRegionEditRevLevel_Object((1,3,6,1,4,1,8886,6,1,24,2,9),_RcMstpBridgeRegionEditRevLevel_Type())
rcMstpBridgeRegionEditRevLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpBridgeRegionEditRevLevel.setStatus(_A)
class _RcMstpBridgeRegionDigest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_RcMstpBridgeRegionDigest_Type.__name__=_R
_RcMstpBridgeRegionDigest_Object=MibScalar
rcMstpBridgeRegionDigest=_RcMstpBridgeRegionDigest_Object((1,3,6,1,4,1,8886,6,1,24,2,10),_RcMstpBridgeRegionDigest_Type())
rcMstpBridgeRegionDigest.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpBridgeRegionDigest.setStatus(_A)
_RcMstpBridgeCistRoot_Type=BridgeId
_RcMstpBridgeCistRoot_Object=MibScalar
rcMstpBridgeCistRoot=_RcMstpBridgeCistRoot_Object((1,3,6,1,4,1,8886,6,1,24,2,11),_RcMstpBridgeCistRoot_Type())
rcMstpBridgeCistRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpBridgeCistRoot.setStatus(_A)
_RcMstpBridgeCistExternalRootCost_Type=Integer32
_RcMstpBridgeCistExternalRootCost_Object=MibScalar
rcMstpBridgeCistExternalRootCost=_RcMstpBridgeCistExternalRootCost_Object((1,3,6,1,4,1,8886,6,1,24,2,12),_RcMstpBridgeCistExternalRootCost_Type())
rcMstpBridgeCistExternalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpBridgeCistExternalRootCost.setStatus(_A)
class _RcMstpBridgeDiameter_Type(Unsigned32):defaultValue=7;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,7))
_RcMstpBridgeDiameter_Type.__name__=_K
_RcMstpBridgeDiameter_Object=MibScalar
rcMstpBridgeDiameter=_RcMstpBridgeDiameter_Object((1,3,6,1,4,1,8886,6,1,24,2,13),_RcMstpBridgeDiameter_Type())
rcMstpBridgeDiameter.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpBridgeDiameter.setStatus(_A)
class _RcMstpBridgeRegionEditBufferOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('active',2)))
_RcMstpBridgeRegionEditBufferOperation_Type.__name__=_C
_RcMstpBridgeRegionEditBufferOperation_Object=MibScalar
rcMstpBridgeRegionEditBufferOperation=_RcMstpBridgeRegionEditBufferOperation_Object((1,3,6,1,4,1,8886,6,1,24,2,14),_RcMstpBridgeRegionEditBufferOperation_Type())
rcMstpBridgeRegionEditBufferOperation.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpBridgeRegionEditBufferOperation.setStatus(_A)
_RcMstpPortTable_Object=MibTable
rcMstpPortTable=_RcMstpPortTable_Object((1,3,6,1,4,1,8886,6,1,24,3))
if mibBuilder.loadTexts:rcMstpPortTable.setStatus(_A)
_RcMstpPortEntry_Object=MibTableRow
rcMstpPortEntry=_RcMstpPortEntry_Object((1,3,6,1,4,1,8886,6,1,24,3,1))
rcMstpPortEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:rcMstpPortEntry.setStatus(_A)
class _RcMstpPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcMstpPortIndex_Type.__name__=_C
_RcMstpPortIndex_Object=MibTableColumn
rcMstpPortIndex=_RcMstpPortIndex_Object((1,3,6,1,4,1,8886,6,1,24,3,1,1),_RcMstpPortIndex_Type())
rcMstpPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMstpPortIndex.setStatus(_A)
_RcMstpPortAdminMACEnable_Type=TruthValue
_RcMstpPortAdminMACEnable_Object=MibTableColumn
rcMstpPortAdminMACEnable=_RcMstpPortAdminMACEnable_Object((1,3,6,1,4,1,8886,6,1,24,3,1,2),_RcMstpPortAdminMACEnable_Type())
rcMstpPortAdminMACEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpPortAdminMACEnable.setStatus(_A)
_RcMstpPortOperMACEnable_Type=TruthValue
_RcMstpPortOperMACEnable_Object=MibTableColumn
rcMstpPortOperMACEnable=_RcMstpPortOperMACEnable_Object((1,3,6,1,4,1,8886,6,1,24,3,1,3),_RcMstpPortOperMACEnable_Type())
rcMstpPortOperMACEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpPortOperMACEnable.setStatus(_A)
class _RcMstpPortAdminEdgePort_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_RcMstpPortAdminEdgePort_Type.__name__=_C
_RcMstpPortAdminEdgePort_Object=MibTableColumn
rcMstpPortAdminEdgePort=_RcMstpPortAdminEdgePort_Object((1,3,6,1,4,1,8886,6,1,24,3,1,4),_RcMstpPortAdminEdgePort_Type())
rcMstpPortAdminEdgePort.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpPortAdminEdgePort.setStatus(_A)
class _RcMstpPortAdminStp_Type(TruthValue):defaultValue=2
_RcMstpPortAdminStp_Type.__name__=_I
_RcMstpPortAdminStp_Object=MibTableColumn
rcMstpPortAdminStp=_RcMstpPortAdminStp_Object((1,3,6,1,4,1,8886,6,1,24,3,1,5),_RcMstpPortAdminStp_Type())
rcMstpPortAdminStp.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpPortAdminStp.setStatus(_A)
class _RcMstpPortOperStp_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcMstpPortOperStp_Type.__name__=_C
_RcMstpPortOperStp_Object=MibTableColumn
rcMstpPortOperStp=_RcMstpPortOperStp_Object((1,3,6,1,4,1,8886,6,1,24,3,1,6),_RcMstpPortOperStp_Type())
rcMstpPortOperStp.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpPortOperStp.setStatus(_A)
class _RcMstpPortRootGuard_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcMstpPortRootGuard_Type.__name__=_C
_RcMstpPortRootGuard_Object=MibTableColumn
rcMstpPortRootGuard=_RcMstpPortRootGuard_Object((1,3,6,1,4,1,8886,6,1,24,3,1,7),_RcMstpPortRootGuard_Type())
rcMstpPortRootGuard.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpPortRootGuard.setStatus(_A)
_RcMstpPortRxTcnBpduCounter_Type=Counter32
_RcMstpPortRxTcnBpduCounter_Object=MibTableColumn
rcMstpPortRxTcnBpduCounter=_RcMstpPortRxTcnBpduCounter_Object((1,3,6,1,4,1,8886,6,1,24,3,1,8),_RcMstpPortRxTcnBpduCounter_Type())
rcMstpPortRxTcnBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpPortRxTcnBpduCounter.setStatus(_A)
_RcMstpPortRxCfgBpduCounter_Type=Counter32
_RcMstpPortRxCfgBpduCounter_Object=MibTableColumn
rcMstpPortRxCfgBpduCounter=_RcMstpPortRxCfgBpduCounter_Object((1,3,6,1,4,1,8886,6,1,24,3,1,9),_RcMstpPortRxCfgBpduCounter_Type())
rcMstpPortRxCfgBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpPortRxCfgBpduCounter.setStatus(_A)
_RcMstpPortRxRstBpduCounter_Type=Counter32
_RcMstpPortRxRstBpduCounter_Object=MibTableColumn
rcMstpPortRxRstBpduCounter=_RcMstpPortRxRstBpduCounter_Object((1,3,6,1,4,1,8886,6,1,24,3,1,10),_RcMstpPortRxRstBpduCounter_Type())
rcMstpPortRxRstBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpPortRxRstBpduCounter.setStatus(_A)
_RcMstpPortRxMstBpduCounter_Type=Counter32
_RcMstpPortRxMstBpduCounter_Object=MibTableColumn
rcMstpPortRxMstBpduCounter=_RcMstpPortRxMstBpduCounter_Object((1,3,6,1,4,1,8886,6,1,24,3,1,11),_RcMstpPortRxMstBpduCounter_Type())
rcMstpPortRxMstBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpPortRxMstBpduCounter.setStatus(_A)
_RcMstpPortTxTcnBpduCounter_Type=Counter32
_RcMstpPortTxTcnBpduCounter_Object=MibTableColumn
rcMstpPortTxTcnBpduCounter=_RcMstpPortTxTcnBpduCounter_Object((1,3,6,1,4,1,8886,6,1,24,3,1,12),_RcMstpPortTxTcnBpduCounter_Type())
rcMstpPortTxTcnBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpPortTxTcnBpduCounter.setStatus(_A)
_RcMstpPortTxCfgBpduCounter_Type=Counter32
_RcMstpPortTxCfgBpduCounter_Object=MibTableColumn
rcMstpPortTxCfgBpduCounter=_RcMstpPortTxCfgBpduCounter_Object((1,3,6,1,4,1,8886,6,1,24,3,1,13),_RcMstpPortTxCfgBpduCounter_Type())
rcMstpPortTxCfgBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpPortTxCfgBpduCounter.setStatus(_A)
_RcMstpPortTxRstBpduCounter_Type=Counter32
_RcMstpPortTxRstBpduCounter_Object=MibTableColumn
rcMstpPortTxRstBpduCounter=_RcMstpPortTxRstBpduCounter_Object((1,3,6,1,4,1,8886,6,1,24,3,1,14),_RcMstpPortTxRstBpduCounter_Type())
rcMstpPortTxRstBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpPortTxRstBpduCounter.setStatus(_A)
_RcMstpPortTxMstBpduCounter_Type=Counter32
_RcMstpPortTxMstBpduCounter_Object=MibTableColumn
rcMstpPortTxMstBpduCounter=_RcMstpPortTxMstBpduCounter_Object((1,3,6,1,4,1,8886,6,1,24,3,1,15),_RcMstpPortTxMstBpduCounter_Type())
rcMstpPortTxMstBpduCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpPortTxMstBpduCounter.setStatus(_A)
_RcMstpPortStatisticsClear_Type=TruthValue
_RcMstpPortStatisticsClear_Object=MibTableColumn
rcMstpPortStatisticsClear=_RcMstpPortStatisticsClear_Object((1,3,6,1,4,1,8886,6,1,24,3,1,16),_RcMstpPortStatisticsClear_Type())
rcMstpPortStatisticsClear.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpPortStatisticsClear.setStatus(_A)
class _RcMstpPortLoopGuard_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_RcMstpPortLoopGuard_Type.__name__=_C
_RcMstpPortLoopGuard_Object=MibTableColumn
rcMstpPortLoopGuard=_RcMstpPortLoopGuard_Object((1,3,6,1,4,1,8886,6,1,24,3,1,17),_RcMstpPortLoopGuard_Type())
rcMstpPortLoopGuard.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpPortLoopGuard.setStatus(_A)
class _RcMstpBpduFilterEnable_Type(TruthValue):defaultValue=2
_RcMstpBpduFilterEnable_Type.__name__=_I
_RcMstpBpduFilterEnable_Object=MibTableColumn
rcMstpBpduFilterEnable=_RcMstpBpduFilterEnable_Object((1,3,6,1,4,1,8886,6,1,24,3,1,18),_RcMstpBpduFilterEnable_Type())
rcMstpBpduFilterEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpBpduFilterEnable.setStatus(_A)
class _RcMstpPortBpduGuardEnable_Type(TruthValue):defaultValue=2
_RcMstpPortBpduGuardEnable_Type.__name__=_I
_RcMstpPortBpduGuardEnable_Object=MibTableColumn
rcMstpPortBpduGuardEnable=_RcMstpPortBpduGuardEnable_Object((1,3,6,1,4,1,8886,6,1,24,3,1,19),_RcMstpPortBpduGuardEnable_Type())
rcMstpPortBpduGuardEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpPortBpduGuardEnable.setStatus(_A)
class _RcMstpPortBpduGuardStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),(_P,2)))
_RcMstpPortBpduGuardStatus_Type.__name__=_C
_RcMstpPortBpduGuardStatus_Object=MibTableColumn
rcMstpPortBpduGuardStatus=_RcMstpPortBpduGuardStatus_Object((1,3,6,1,4,1,8886,6,1,24,3,1,20),_RcMstpPortBpduGuardStatus_Type())
rcMstpPortBpduGuardStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpPortBpduGuardStatus.setStatus(_A)
_RcMstpXstInstanceTable_Object=MibTable
rcMstpXstInstanceTable=_RcMstpXstInstanceTable_Object((1,3,6,1,4,1,8886,6,1,24,4))
if mibBuilder.loadTexts:rcMstpXstInstanceTable.setStatus(_A)
_RcMstpXstInstanceEntry_Object=MibTableRow
rcMstpXstInstanceEntry=_RcMstpXstInstanceEntry_Object((1,3,6,1,4,1,8886,6,1,24,4,1))
rcMstpXstInstanceEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:rcMstpXstInstanceEntry.setStatus(_A)
class _RcMstpXstInstanceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RcMstpXstInstanceId_Type.__name__=_C
_RcMstpXstInstanceId_Object=MibTableColumn
rcMstpXstInstanceId=_RcMstpXstInstanceId_Object((1,3,6,1,4,1,8886,6,1,24,4,1,1),_RcMstpXstInstanceId_Type())
rcMstpXstInstanceId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMstpXstInstanceId.setStatus(_A)
_RcMstpXstInstanceVlansMapped_Type=Vlanset
_RcMstpXstInstanceVlansMapped_Object=MibTableColumn
rcMstpXstInstanceVlansMapped=_RcMstpXstInstanceVlansMapped_Object((1,3,6,1,4,1,8886,6,1,24,4,1,2),_RcMstpXstInstanceVlansMapped_Type())
rcMstpXstInstanceVlansMapped.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstInstanceVlansMapped.setStatus(_A)
_RcMstpXstInstanceEditTable_Object=MibTable
rcMstpXstInstanceEditTable=_RcMstpXstInstanceEditTable_Object((1,3,6,1,4,1,8886,6,1,24,5))
if mibBuilder.loadTexts:rcMstpXstInstanceEditTable.setStatus(_A)
_RcMstpXstInstanceEditEntry_Object=MibTableRow
rcMstpXstInstanceEditEntry=_RcMstpXstInstanceEditEntry_Object((1,3,6,1,4,1,8886,6,1,24,5,1))
rcMstpXstInstanceEditEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:rcMstpXstInstanceEditEntry.setStatus(_A)
class _RcMstpXstInstanceEditId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RcMstpXstInstanceEditId_Type.__name__=_K
_RcMstpXstInstanceEditId_Object=MibTableColumn
rcMstpXstInstanceEditId=_RcMstpXstInstanceEditId_Object((1,3,6,1,4,1,8886,6,1,24,5,1,1),_RcMstpXstInstanceEditId_Type())
rcMstpXstInstanceEditId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMstpXstInstanceEditId.setStatus(_A)
_RcMstpXstInstanceEditVlansMap_Type=Vlanset
_RcMstpXstInstanceEditVlansMap_Object=MibTableColumn
rcMstpXstInstanceEditVlansMap=_RcMstpXstInstanceEditVlansMap_Object((1,3,6,1,4,1,8886,6,1,24,5,1,2),_RcMstpXstInstanceEditVlansMap_Type())
rcMstpXstInstanceEditVlansMap.setMaxAccess(_U)
if mibBuilder.loadTexts:rcMstpXstInstanceEditVlansMap.setStatus(_A)
_RcMstpXstInstanceEditRowStatus_Type=RowStatus
_RcMstpXstInstanceEditRowStatus_Object=MibTableColumn
rcMstpXstInstanceEditRowStatus=_RcMstpXstInstanceEditRowStatus_Object((1,3,6,1,4,1,8886,6,1,24,5,1,3),_RcMstpXstInstanceEditRowStatus_Type())
rcMstpXstInstanceEditRowStatus.setMaxAccess(_U)
if mibBuilder.loadTexts:rcMstpXstInstanceEditRowStatus.setStatus(_A)
_RcMstpXstTable_Object=MibTable
rcMstpXstTable=_RcMstpXstTable_Object((1,3,6,1,4,1,8886,6,1,24,6))
if mibBuilder.loadTexts:rcMstpXstTable.setStatus(_A)
_RcMstpXstEntry_Object=MibTableRow
rcMstpXstEntry=_RcMstpXstEntry_Object((1,3,6,1,4,1,8886,6,1,24,6,1))
rcMstpXstEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:rcMstpXstEntry.setStatus(_A)
class _RcMstpXstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RcMstpXstId_Type.__name__=_C
_RcMstpXstId_Object=MibTableColumn
rcMstpXstId=_RcMstpXstId_Object((1,3,6,1,4,1,8886,6,1,24,6,1,1),_RcMstpXstId_Type())
rcMstpXstId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMstpXstId.setStatus(_A)
_RcMstpXstBridgeId_Type=BridgeId
_RcMstpXstBridgeId_Object=MibTableColumn
rcMstpXstBridgeId=_RcMstpXstBridgeId_Object((1,3,6,1,4,1,8886,6,1,24,6,1,2),_RcMstpXstBridgeId_Type())
rcMstpXstBridgeId.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstBridgeId.setStatus(_A)
_RcMstpXstDesignatedRoot_Type=BridgeId
_RcMstpXstDesignatedRoot_Object=MibTableColumn
rcMstpXstDesignatedRoot=_RcMstpXstDesignatedRoot_Object((1,3,6,1,4,1,8886,6,1,24,6,1,3),_RcMstpXstDesignatedRoot_Type())
rcMstpXstDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstDesignatedRoot.setStatus(_A)
_RcMstpXstInternalRootCost_Type=Integer32
_RcMstpXstInternalRootCost_Object=MibTableColumn
rcMstpXstInternalRootCost=_RcMstpXstInternalRootCost_Object((1,3,6,1,4,1,8886,6,1,24,6,1,4),_RcMstpXstInternalRootCost_Type())
rcMstpXstInternalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstInternalRootCost.setStatus(_A)
_RcMstpXstRootPort_Type=Unsigned32
_RcMstpXstRootPort_Object=MibTableColumn
rcMstpXstRootPort=_RcMstpXstRootPort_Object((1,3,6,1,4,1,8886,6,1,24,6,1,5),_RcMstpXstRootPort_Type())
rcMstpXstRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstRootPort.setStatus(_A)
_RcMstpXstMasterPort_Type=Unsigned32
_RcMstpXstMasterPort_Object=MibTableColumn
rcMstpXstMasterPort=_RcMstpXstMasterPort_Object((1,3,6,1,4,1,8886,6,1,24,6,1,6),_RcMstpXstMasterPort_Type())
rcMstpXstMasterPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstMasterPort.setStatus(_A)
_RcMstpXstTimeSinceTopologyChange_Type=TimeTicks
_RcMstpXstTimeSinceTopologyChange_Object=MibTableColumn
rcMstpXstTimeSinceTopologyChange=_RcMstpXstTimeSinceTopologyChange_Object((1,3,6,1,4,1,8886,6,1,24,6,1,7),_RcMstpXstTimeSinceTopologyChange_Type())
rcMstpXstTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstTimeSinceTopologyChange.setStatus(_A)
_RcMstpXstTopologyChangesCount_Type=Counter32
_RcMstpXstTopologyChangesCount_Object=MibTableColumn
rcMstpXstTopologyChangesCount=_RcMstpXstTopologyChangesCount_Object((1,3,6,1,4,1,8886,6,1,24,6,1,8),_RcMstpXstTopologyChangesCount_Type())
rcMstpXstTopologyChangesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstTopologyChangesCount.setStatus(_A)
_RcMstpXstTopologyChangeFlag_Type=TruthValue
_RcMstpXstTopologyChangeFlag_Object=MibTableColumn
rcMstpXstTopologyChangeFlag=_RcMstpXstTopologyChangeFlag_Object((1,3,6,1,4,1,8886,6,1,24,6,1,9),_RcMstpXstTopologyChangeFlag_Type())
rcMstpXstTopologyChangeFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstTopologyChangeFlag.setStatus(_A)
_RcMstpXstConfigTable_Object=MibTable
rcMstpXstConfigTable=_RcMstpXstConfigTable_Object((1,3,6,1,4,1,8886,6,1,24,7))
if mibBuilder.loadTexts:rcMstpXstConfigTable.setStatus(_A)
_RcMstpXstConfigEntry_Object=MibTableRow
rcMstpXstConfigEntry=_RcMstpXstConfigEntry_Object((1,3,6,1,4,1,8886,6,1,24,7,1))
rcMstpXstConfigEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:rcMstpXstConfigEntry.setStatus(_A)
class _RcMstpCfgXstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RcMstpCfgXstId_Type.__name__=_C
_RcMstpCfgXstId_Object=MibTableColumn
rcMstpCfgXstId=_RcMstpCfgXstId_Object((1,3,6,1,4,1,8886,6,1,24,7,1,1),_RcMstpCfgXstId_Type())
rcMstpCfgXstId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMstpCfgXstId.setStatus(_A)
class _RcMstpXstBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_RcMstpXstBridgePriority_Type.__name__=_C
_RcMstpXstBridgePriority_Object=MibTableColumn
rcMstpXstBridgePriority=_RcMstpXstBridgePriority_Object((1,3,6,1,4,1,8886,6,1,24,7,1,2),_RcMstpXstBridgePriority_Type())
rcMstpXstBridgePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpXstBridgePriority.setStatus(_A)
_RcMstpXstPrimaryRoot_Type=TruthValue
_RcMstpXstPrimaryRoot_Object=MibTableColumn
rcMstpXstPrimaryRoot=_RcMstpXstPrimaryRoot_Object((1,3,6,1,4,1,8886,6,1,24,7,1,3),_RcMstpXstPrimaryRoot_Type())
rcMstpXstPrimaryRoot.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpXstPrimaryRoot.setStatus(_A)
_RcMstpXstSecondaryRoot_Type=TruthValue
_RcMstpXstSecondaryRoot_Object=MibTableColumn
rcMstpXstSecondaryRoot=_RcMstpXstSecondaryRoot_Object((1,3,6,1,4,1,8886,6,1,24,7,1,4),_RcMstpXstSecondaryRoot_Type())
rcMstpXstSecondaryRoot.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpXstSecondaryRoot.setStatus(_A)
_RcMstpXstPortTable_Object=MibTable
rcMstpXstPortTable=_RcMstpXstPortTable_Object((1,3,6,1,4,1,8886,6,1,24,8))
if mibBuilder.loadTexts:rcMstpXstPortTable.setStatus(_A)
_RcMstpXstPortEntry_Object=MibTableRow
rcMstpXstPortEntry=_RcMstpXstPortEntry_Object((1,3,6,1,4,1,8886,6,1,24,8,1))
rcMstpXstPortEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:rcMstpXstPortEntry.setStatus(_A)
class _RcMstpXstPortXstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RcMstpXstPortXstId_Type.__name__=_C
_RcMstpXstPortXstId_Object=MibTableColumn
rcMstpXstPortXstId=_RcMstpXstPortXstId_Object((1,3,6,1,4,1,8886,6,1,24,8,1,1),_RcMstpXstPortXstId_Type())
rcMstpXstPortXstId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMstpXstPortXstId.setStatus(_A)
class _RcMstpXstPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcMstpXstPortIndex_Type.__name__=_C
_RcMstpXstPortIndex_Object=MibTableColumn
rcMstpXstPortIndex=_RcMstpXstPortIndex_Object((1,3,6,1,4,1,8886,6,1,24,8,1,2),_RcMstpXstPortIndex_Type())
rcMstpXstPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMstpXstPortIndex.setStatus(_A)
class _RcMstpXstPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_W,0),('discarding',1),('learning',2),('forwarding',3),(_J,4)))
_RcMstpXstPortState_Type.__name__=_C
_RcMstpXstPortState_Object=MibTableColumn
rcMstpXstPortState=_RcMstpXstPortState_Object((1,3,6,1,4,1,8886,6,1,24,8,1,3),_RcMstpXstPortState_Type())
rcMstpXstPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstPortState.setStatus(_A)
class _RcMstpXstPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_W,1),('alternate',2),('backup',3),('root',4),('designated',5),('master',6),(_J,7)))
_RcMstpXstPortRole_Type.__name__=_C
_RcMstpXstPortRole_Object=MibTableColumn
rcMstpXstPortRole=_RcMstpXstPortRole_Object((1,3,6,1,4,1,8886,6,1,24,8,1,4),_RcMstpXstPortRole_Type())
rcMstpXstPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstPortRole.setStatus(_A)
_RcMstpXstPortDesignatedRoot_Type=BridgeId
_RcMstpXstPortDesignatedRoot_Object=MibTableColumn
rcMstpXstPortDesignatedRoot=_RcMstpXstPortDesignatedRoot_Object((1,3,6,1,4,1,8886,6,1,24,8,1,5),_RcMstpXstPortDesignatedRoot_Type())
rcMstpXstPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstPortDesignatedRoot.setStatus(_A)
_RcMstpXstPortExternalRootCost_Type=Integer32
_RcMstpXstPortExternalRootCost_Object=MibTableColumn
rcMstpXstPortExternalRootCost=_RcMstpXstPortExternalRootCost_Object((1,3,6,1,4,1,8886,6,1,24,8,1,6),_RcMstpXstPortExternalRootCost_Type())
rcMstpXstPortExternalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstPortExternalRootCost.setStatus(_A)
_RcMstpXstPortRegionalRoot_Type=BridgeId
_RcMstpXstPortRegionalRoot_Object=MibTableColumn
rcMstpXstPortRegionalRoot=_RcMstpXstPortRegionalRoot_Object((1,3,6,1,4,1,8886,6,1,24,8,1,7),_RcMstpXstPortRegionalRoot_Type())
rcMstpXstPortRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstPortRegionalRoot.setStatus(_A)
_RcMstpXstPortInternalRootCost_Type=Integer32
_RcMstpXstPortInternalRootCost_Object=MibTableColumn
rcMstpXstPortInternalRootCost=_RcMstpXstPortInternalRootCost_Object((1,3,6,1,4,1,8886,6,1,24,8,1,8),_RcMstpXstPortInternalRootCost_Type())
rcMstpXstPortInternalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstPortInternalRootCost.setStatus(_A)
_RcMstpXstPortDesignatedBridge_Type=BridgeId
_RcMstpXstPortDesignatedBridge_Object=MibTableColumn
rcMstpXstPortDesignatedBridge=_RcMstpXstPortDesignatedBridge_Object((1,3,6,1,4,1,8886,6,1,24,8,1,9),_RcMstpXstPortDesignatedBridge_Type())
rcMstpXstPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstPortDesignatedBridge.setStatus(_A)
_RcMstpXstPortDesignatedPort_Type=Integer32
_RcMstpXstPortDesignatedPort_Object=MibTableColumn
rcMstpXstPortDesignatedPort=_RcMstpXstPortDesignatedPort_Object((1,3,6,1,4,1,8886,6,1,24,8,1,10),_RcMstpXstPortDesignatedPort_Type())
rcMstpXstPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstPortDesignatedPort.setStatus(_A)
_RcMstpXstPortOperInternalPathCost_Type=Integer32
_RcMstpXstPortOperInternalPathCost_Object=MibTableColumn
rcMstpXstPortOperInternalPathCost=_RcMstpXstPortOperInternalPathCost_Object((1,3,6,1,4,1,8886,6,1,24,8,1,11),_RcMstpXstPortOperInternalPathCost_Type())
rcMstpXstPortOperInternalPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstPortOperInternalPathCost.setStatus(_A)
class _RcMstpXstPortRootGuardState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),(_P,2)))
_RcMstpXstPortRootGuardState_Type.__name__=_C
_RcMstpXstPortRootGuardState_Object=MibTableColumn
rcMstpXstPortRootGuardState=_RcMstpXstPortRootGuardState_Object((1,3,6,1,4,1,8886,6,1,24,8,1,12),_RcMstpXstPortRootGuardState_Type())
rcMstpXstPortRootGuardState.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstPortRootGuardState.setStatus(_A)
class _RcMstpXstPortLoopGuardState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),(_P,2)))
_RcMstpXstPortLoopGuardState_Type.__name__=_C
_RcMstpXstPortLoopGuardState_Object=MibTableColumn
rcMstpXstPortLoopGuardState=_RcMstpXstPortLoopGuardState_Object((1,3,6,1,4,1,8886,6,1,24,8,1,13),_RcMstpXstPortLoopGuardState_Type())
rcMstpXstPortLoopGuardState.setMaxAccess(_B)
if mibBuilder.loadTexts:rcMstpXstPortLoopGuardState.setStatus(_A)
_RcMstpXstPortConfigTable_Object=MibTable
rcMstpXstPortConfigTable=_RcMstpXstPortConfigTable_Object((1,3,6,1,4,1,8886,6,1,24,9))
if mibBuilder.loadTexts:rcMstpXstPortConfigTable.setStatus(_A)
_RcMstpXstPortConfigEntry_Object=MibTableRow
rcMstpXstPortConfigEntry=_RcMstpXstPortConfigEntry_Object((1,3,6,1,4,1,8886,6,1,24,9,1))
rcMstpXstPortConfigEntry.setIndexNames((0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:rcMstpXstPortConfigEntry.setStatus(_A)
class _RcMstpXstPortCfgXstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RcMstpXstPortCfgXstId_Type.__name__=_C
_RcMstpXstPortCfgXstId_Object=MibTableColumn
rcMstpXstPortCfgXstId=_RcMstpXstPortCfgXstId_Object((1,3,6,1,4,1,8886,6,1,24,9,1,1),_RcMstpXstPortCfgXstId_Type())
rcMstpXstPortCfgXstId.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMstpXstPortCfgXstId.setStatus(_A)
class _RcMstpXstPortCfgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcMstpXstPortCfgIndex_Type.__name__=_C
_RcMstpXstPortCfgIndex_Object=MibTableColumn
rcMstpXstPortCfgIndex=_RcMstpXstPortCfgIndex_Object((1,3,6,1,4,1,8886,6,1,24,9,1,2),_RcMstpXstPortCfgIndex_Type())
rcMstpXstPortCfgIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rcMstpXstPortCfgIndex.setStatus(_A)
class _RcMstpXstPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RcMstpXstPortPriority_Type.__name__=_C
_RcMstpXstPortPriority_Object=MibTableColumn
rcMstpXstPortPriority=_RcMstpXstPortPriority_Object((1,3,6,1,4,1,8886,6,1,24,9,1,3),_RcMstpXstPortPriority_Type())
rcMstpXstPortPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpXstPortPriority.setStatus(_A)
class _RcMstpXstPortAdminInternalPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_RcMstpXstPortAdminInternalPathCost_Type.__name__=_C
_RcMstpXstPortAdminInternalPathCost_Object=MibTableColumn
rcMstpXstPortAdminInternalPathCost=_RcMstpXstPortAdminInternalPathCost_Object((1,3,6,1,4,1,8886,6,1,24,9,1,4),_RcMstpXstPortAdminInternalPathCost_Type())
rcMstpXstPortAdminInternalPathCost.setMaxAccess(_E)
if mibBuilder.loadTexts:rcMstpXstPortAdminInternalPathCost.setStatus(_A)
rcMstpNewRootBridge=NotificationType((1,3,6,1,4,1,8886,6,1,24,1,1))
rcMstpNewRootBridge.setObjects((_D,_Q))
if mibBuilder.loadTexts:rcMstpNewRootBridge.setStatus(_A)
rcMstpNewRootPort=NotificationType((1,3,6,1,4,1,8886,6,1,24,1,2))
rcMstpNewRootPort.setObjects(*((_D,_G),(_D,_H)))
if mibBuilder.loadTexts:rcMstpNewRootPort.setStatus(_A)
rcMstpTopologyChange=NotificationType((1,3,6,1,4,1,8886,6,1,24,1,3))
rcMstpTopologyChange.setObjects(*((_D,_G),(_D,_H),(_D,_Z)))
if mibBuilder.loadTexts:rcMstpTopologyChange.setStatus(_A)
rcMstpRootGuardStateChange=NotificationType((1,3,6,1,4,1,8886,6,1,24,1,4))
rcMstpRootGuardStateChange.setObjects(*((_D,_G),(_D,_H),(_D,_a)))
if mibBuilder.loadTexts:rcMstpRootGuardStateChange.setStatus(_A)
rcMstpLoopGuardStateChange=NotificationType((1,3,6,1,4,1,8886,6,1,24,1,5))
rcMstpLoopGuardStateChange.setObjects(*((_D,_G),(_D,_H),(_D,_b)))
if mibBuilder.loadTexts:rcMstpLoopGuardStateChange.setStatus(_A)
rcMstpBpduGuardStateChange=NotificationType((1,3,6,1,4,1,8886,6,1,24,1,6))
rcMstpBpduGuardStateChange.setObjects(*((_D,_M),(_D,_c),(_D,_d)))
if mibBuilder.loadTexts:rcMstpBpduGuardStateChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rcMstp':rcMstp,'rcMstpTraps':rcMstpTraps,'rcMstpNewRootBridge':rcMstpNewRootBridge,'rcMstpNewRootPort':rcMstpNewRootPort,'rcMstpTopologyChange':rcMstpTopologyChange,'rcMstpRootGuardStateChange':rcMstpRootGuardStateChange,'rcMstpLoopGuardStateChange':rcMstpLoopGuardStateChange,'rcMstpBpduGuardStateChange':rcMstpBpduGuardStateChange,'rcMstpBridge':rcMstpBridge,'rcMstpBridgeAdminStp':rcMstpBridgeAdminStp,'rcMstpBridgeMaxHops':rcMstpBridgeMaxHops,'rcMstpBridgeVersionSupported':rcMstpBridgeVersionSupported,'rcMstpBridgeProtocolVersion':rcMstpBridgeProtocolVersion,'rcMstpBridgeRegionFormatSelector':rcMstpBridgeRegionFormatSelector,'rcMstpBridgeRegionName':rcMstpBridgeRegionName,'rcMstpBridgeRegionEditName':rcMstpBridgeRegionEditName,'rcMstpBridgeRegionRevLevel':rcMstpBridgeRegionRevLevel,'rcMstpBridgeRegionEditRevLevel':rcMstpBridgeRegionEditRevLevel,'rcMstpBridgeRegionDigest':rcMstpBridgeRegionDigest,'rcMstpBridgeCistRoot':rcMstpBridgeCistRoot,'rcMstpBridgeCistExternalRootCost':rcMstpBridgeCistExternalRootCost,'rcMstpBridgeDiameter':rcMstpBridgeDiameter,'rcMstpBridgeRegionEditBufferOperation':rcMstpBridgeRegionEditBufferOperation,'rcMstpPortTable':rcMstpPortTable,'rcMstpPortEntry':rcMstpPortEntry,_M:rcMstpPortIndex,'rcMstpPortAdminMACEnable':rcMstpPortAdminMACEnable,'rcMstpPortOperMACEnable':rcMstpPortOperMACEnable,'rcMstpPortAdminEdgePort':rcMstpPortAdminEdgePort,'rcMstpPortAdminStp':rcMstpPortAdminStp,'rcMstpPortOperStp':rcMstpPortOperStp,'rcMstpPortRootGuard':rcMstpPortRootGuard,'rcMstpPortRxTcnBpduCounter':rcMstpPortRxTcnBpduCounter,'rcMstpPortRxCfgBpduCounter':rcMstpPortRxCfgBpduCounter,'rcMstpPortRxRstBpduCounter':rcMstpPortRxRstBpduCounter,'rcMstpPortRxMstBpduCounter':rcMstpPortRxMstBpduCounter,'rcMstpPortTxTcnBpduCounter':rcMstpPortTxTcnBpduCounter,'rcMstpPortTxCfgBpduCounter':rcMstpPortTxCfgBpduCounter,'rcMstpPortTxRstBpduCounter':rcMstpPortTxRstBpduCounter,'rcMstpPortTxMstBpduCounter':rcMstpPortTxMstBpduCounter,'rcMstpPortStatisticsClear':rcMstpPortStatisticsClear,'rcMstpPortLoopGuard':rcMstpPortLoopGuard,'rcMstpBpduFilterEnable':rcMstpBpduFilterEnable,_c:rcMstpPortBpduGuardEnable,_d:rcMstpPortBpduGuardStatus,'rcMstpXstInstanceTable':rcMstpXstInstanceTable,'rcMstpXstInstanceEntry':rcMstpXstInstanceEntry,_S:rcMstpXstInstanceId,'rcMstpXstInstanceVlansMapped':rcMstpXstInstanceVlansMapped,'rcMstpXstInstanceEditTable':rcMstpXstInstanceEditTable,'rcMstpXstInstanceEditEntry':rcMstpXstInstanceEditEntry,_T:rcMstpXstInstanceEditId,'rcMstpXstInstanceEditVlansMap':rcMstpXstInstanceEditVlansMap,'rcMstpXstInstanceEditRowStatus':rcMstpXstInstanceEditRowStatus,'rcMstpXstTable':rcMstpXstTable,'rcMstpXstEntry':rcMstpXstEntry,_Q:rcMstpXstId,'rcMstpXstBridgeId':rcMstpXstBridgeId,'rcMstpXstDesignatedRoot':rcMstpXstDesignatedRoot,'rcMstpXstInternalRootCost':rcMstpXstInternalRootCost,'rcMstpXstRootPort':rcMstpXstRootPort,'rcMstpXstMasterPort':rcMstpXstMasterPort,'rcMstpXstTimeSinceTopologyChange':rcMstpXstTimeSinceTopologyChange,'rcMstpXstTopologyChangesCount':rcMstpXstTopologyChangesCount,'rcMstpXstTopologyChangeFlag':rcMstpXstTopologyChangeFlag,'rcMstpXstConfigTable':rcMstpXstConfigTable,'rcMstpXstConfigEntry':rcMstpXstConfigEntry,_V:rcMstpCfgXstId,'rcMstpXstBridgePriority':rcMstpXstBridgePriority,'rcMstpXstPrimaryRoot':rcMstpXstPrimaryRoot,'rcMstpXstSecondaryRoot':rcMstpXstSecondaryRoot,'rcMstpXstPortTable':rcMstpXstPortTable,'rcMstpXstPortEntry':rcMstpXstPortEntry,_G:rcMstpXstPortXstId,_H:rcMstpXstPortIndex,_Z:rcMstpXstPortState,'rcMstpXstPortRole':rcMstpXstPortRole,'rcMstpXstPortDesignatedRoot':rcMstpXstPortDesignatedRoot,'rcMstpXstPortExternalRootCost':rcMstpXstPortExternalRootCost,'rcMstpXstPortRegionalRoot':rcMstpXstPortRegionalRoot,'rcMstpXstPortInternalRootCost':rcMstpXstPortInternalRootCost,'rcMstpXstPortDesignatedBridge':rcMstpXstPortDesignatedBridge,'rcMstpXstPortDesignatedPort':rcMstpXstPortDesignatedPort,'rcMstpXstPortOperInternalPathCost':rcMstpXstPortOperInternalPathCost,_a:rcMstpXstPortRootGuardState,_b:rcMstpXstPortLoopGuardState,'rcMstpXstPortConfigTable':rcMstpXstPortConfigTable,'rcMstpXstPortConfigEntry':rcMstpXstPortConfigEntry,_X:rcMstpXstPortCfgXstId,_Y:rcMstpXstPortCfgIndex,'rcMstpXstPortPriority':rcMstpXstPortPriority,'rcMstpXstPortAdminInternalPathCost':rcMstpXstPortAdminInternalPathCost})