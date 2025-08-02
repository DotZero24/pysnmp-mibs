_Q='not-accessible'
_P='classC'
_O='classB'
_N='classA'
_M='DisplayString'
_L='nnfrAvcId'
_K='nnfrPvcDlci'
_J='bps'
_I='nnbundleId'
_H='BUNDLE-MIB'
_G='FR-MIB'
_F='TruthValue'
_E='read-create'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nnbundleId,=mibBuilder.importSymbols(_H,_I)
ntEnterpriseDataTasmanMgmt,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention',_F)
nnfrMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,1,16))
if mibBuilder.loadTexts:nnfrMib.setRevisions(('1999-04-23 00:00',))
_NnfrTable_Object=MibTable
nnfrTable=_NnfrTable_Object((1,3,6,1,4,1,562,73,1,1,1,16,1))
if mibBuilder.loadTexts:nnfrTable.setStatus(_A)
_NnfrTableEntry_Object=MibTableRow
nnfrTableEntry=_NnfrTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1))
nnfrTableEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:nnfrTableEntry.setStatus(_A)
class _NnfrIfEnable_Type(TruthValue):defaultValue=1
_NnfrIfEnable_Type.__name__=_F
_NnfrIfEnable_Object=MibTableColumn
nnfrIfEnable=_NnfrIfEnable_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,1),_NnfrIfEnable_Type())
nnfrIfEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrIfEnable.setStatus(_A)
class _NnfrEnablePvcAll_Type(TruthValue):defaultValue=2
_NnfrEnablePvcAll_Type.__name__=_F
_NnfrEnablePvcAll_Object=MibTableColumn
nnfrEnablePvcAll=_NnfrEnablePvcAll_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,2),_NnfrEnablePvcAll_Type())
nnfrEnablePvcAll.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrEnablePvcAll.setStatus(_A)
class _NnfrFrameSize_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(56,4096))
_NnfrFrameSize_Type.__name__=_C
_NnfrFrameSize_Object=MibTableColumn
nnfrFrameSize=_NnfrFrameSize_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,3),_NnfrFrameSize_Type())
nnfrFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrFrameSize.setStatus(_A)
if mibBuilder.loadTexts:nnfrFrameSize.setUnits('bytes')
class _NnfrIfType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dce',1),('dte',2),('nni',3)))
_NnfrIfType_Type.__name__=_C
_NnfrIfType_Object=MibTableColumn
nnfrIfType=_NnfrIfType_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,4),_NnfrIfType_Type())
nnfrIfType.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrIfType.setStatus(_A)
class _NnfrLmiType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4)));namedValues=NamedValues(*(('none',0),('cisco',2),('ansi',3),('q933a',4)))
_NnfrLmiType_Type.__name__=_C
_NnfrLmiType_Object=MibTableColumn
nnfrLmiType=_NnfrLmiType_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,5),_NnfrLmiType_Type())
nnfrLmiType.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrLmiType.setStatus(_A)
class _NnfrLmiDceN392_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_NnfrLmiDceN392_Type.__name__=_C
_NnfrLmiDceN392_Object=MibTableColumn
nnfrLmiDceN392=_NnfrLmiDceN392_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,6),_NnfrLmiDceN392_Type())
nnfrLmiDceN392.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrLmiDceN392.setStatus(_A)
class _NnfrLmiDceN393_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_NnfrLmiDceN393_Type.__name__=_C
_NnfrLmiDceN393_Object=MibTableColumn
nnfrLmiDceN393=_NnfrLmiDceN393_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,7),_NnfrLmiDceN393_Type())
nnfrLmiDceN393.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrLmiDceN393.setStatus(_A)
class _NnfrLmiDteN392_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_NnfrLmiDteN392_Type.__name__=_C
_NnfrLmiDteN392_Object=MibTableColumn
nnfrLmiDteN392=_NnfrLmiDteN392_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,8),_NnfrLmiDteN392_Type())
nnfrLmiDteN392.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrLmiDteN392.setStatus(_A)
class _NnfrLmiDteN393_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_NnfrLmiDteN393_Type.__name__=_C
_NnfrLmiDteN393_Object=MibTableColumn
nnfrLmiDteN393=_NnfrLmiDteN393_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,9),_NnfrLmiDteN393_Type())
nnfrLmiDteN393.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrLmiDteN393.setStatus(_A)
class _NnfrLmiDteN391_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_NnfrLmiDteN391_Type.__name__=_C
_NnfrLmiDteN391_Object=MibTableColumn
nnfrLmiDteN391=_NnfrLmiDteN391_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,10),_NnfrLmiDteN391_Type())
nnfrLmiDteN391.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrLmiDteN391.setStatus(_A)
class _NnfrLmiKeepalive_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,255))
_NnfrLmiKeepalive_Type.__name__=_C
_NnfrLmiKeepalive_Object=MibTableColumn
nnfrLmiKeepalive=_NnfrLmiKeepalive_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,11),_NnfrLmiKeepalive_Type())
nnfrLmiKeepalive.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrLmiKeepalive.setStatus(_A)
class _NnmfrAckMsgTimer_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_NnmfrAckMsgTimer_Type.__name__=_C
_NnmfrAckMsgTimer_Object=MibTableColumn
nnmfrAckMsgTimer=_NnmfrAckMsgTimer_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,12),_NnmfrAckMsgTimer_Type())
nnmfrAckMsgTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nnmfrAckMsgTimer.setStatus(_A)
class _NnmfrAckMsgMaxRetry_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_NnmfrAckMsgMaxRetry_Type.__name__=_C
_NnmfrAckMsgMaxRetry_Object=MibTableColumn
nnmfrAckMsgMaxRetry=_NnmfrAckMsgMaxRetry_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,13),_NnmfrAckMsgMaxRetry_Type())
nnmfrAckMsgMaxRetry.setMaxAccess(_D)
if mibBuilder.loadTexts:nnmfrAckMsgMaxRetry.setStatus(_A)
class _NnmfrClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_NnmfrClass_Type.__name__=_C
_NnmfrClass_Object=MibTableColumn
nnmfrClass=_NnmfrClass_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,14),_NnmfrClass_Type())
nnmfrClass.setMaxAccess(_D)
if mibBuilder.loadTexts:nnmfrClass.setStatus(_A)
class _NnmfrClassThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_NnmfrClassThreshold_Type.__name__=_C
_NnmfrClassThreshold_Object=MibTableColumn
nnmfrClassThreshold=_NnmfrClassThreshold_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,15),_NnmfrClassThreshold_Type())
nnmfrClassThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:nnmfrClassThreshold.setStatus(_A)
class _NnmfrFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(56,4096))
_NnmfrFrameSize_Type.__name__=_C
_NnmfrFrameSize_Object=MibTableColumn
nnmfrFrameSize=_NnmfrFrameSize_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,16),_NnmfrFrameSize_Type())
nnmfrFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nnmfrFrameSize.setStatus(_A)
class _NnmfrHelloTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,180))
_NnmfrHelloTimer_Type.__name__=_C
_NnmfrHelloTimer_Object=MibTableColumn
nnmfrHelloTimer=_NnmfrHelloTimer_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,17),_NnmfrHelloTimer_Type())
nnmfrHelloTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nnmfrHelloTimer.setStatus(_A)
class _NnmfrSegThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(56,4096))
_NnmfrSegThreshold_Type.__name__=_C
_NnmfrSegThreshold_Object=MibTableColumn
nnmfrSegThreshold=_NnmfrSegThreshold_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,18),_NnmfrSegThreshold_Type())
nnmfrSegThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:nnmfrSegThreshold.setStatus(_A)
class _NnmfrDiffDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,128))
_NnmfrDiffDelay_Type.__name__=_C
_NnmfrDiffDelay_Object=MibTableColumn
nnmfrDiffDelay=_NnmfrDiffDelay_Object((1,3,6,1,4,1,562,73,1,1,1,16,1,1,19),_NnmfrDiffDelay_Type())
nnmfrDiffDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nnmfrDiffDelay.setStatus(_A)
_NnfrPvcTable_Object=MibTable
nnfrPvcTable=_NnfrPvcTable_Object((1,3,6,1,4,1,562,73,1,1,1,16,2))
if mibBuilder.loadTexts:nnfrPvcTable.setStatus(_A)
_NnfrPvcTableEntry_Object=MibTableRow
nnfrPvcTableEntry=_NnfrPvcTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1))
nnfrPvcTableEntry.setIndexNames((0,_H,_I),(0,_G,_K))
if mibBuilder.loadTexts:nnfrPvcTableEntry.setStatus(_A)
class _NnfrPvcDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,991))
_NnfrPvcDlci_Type.__name__=_C
_NnfrPvcDlci_Object=MibTableColumn
nnfrPvcDlci=_NnfrPvcDlci_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,1),_NnfrPvcDlci_Type())
nnfrPvcDlci.setMaxAccess(_Q)
if mibBuilder.loadTexts:nnfrPvcDlci.setStatus(_A)
class _NnfrPvcEnable_Type(TruthValue):defaultValue=1
_NnfrPvcEnable_Type.__name__=_F
_NnfrPvcEnable_Object=MibTableColumn
nnfrPvcEnable=_NnfrPvcEnable_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,2),_NnfrPvcEnable_Type())
nnfrPvcEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcEnable.setStatus(_A)
class _NnfrPvcDescr_Type(DisplayString):defaultValue=OctetString('')
_NnfrPvcDescr_Type.__name__=_M
_NnfrPvcDescr_Object=MibTableColumn
nnfrPvcDescr=_NnfrPvcDescr_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,3),_NnfrPvcDescr_Type())
nnfrPvcDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcDescr.setStatus(_A)
_NnfrPvcIpAddr_Type=IpAddress
_NnfrPvcIpAddr_Object=MibTableColumn
nnfrPvcIpAddr=_NnfrPvcIpAddr_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,4),_NnfrPvcIpAddr_Type())
nnfrPvcIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcIpAddr.setStatus(_A)
_NnfrPvcIpSubnetMask_Type=IpAddress
_NnfrPvcIpSubnetMask_Object=MibTableColumn
nnfrPvcIpSubnetMask=_NnfrPvcIpSubnetMask_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,5),_NnfrPvcIpSubnetMask_Type())
nnfrPvcIpSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcIpSubnetMask.setStatus(_A)
_NnfrPvcRemoteIpAddr_Type=IpAddress
_NnfrPvcRemoteIpAddr_Object=MibTableColumn
nnfrPvcRemoteIpAddr=_NnfrPvcRemoteIpAddr_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,6),_NnfrPvcRemoteIpAddr_Type())
nnfrPvcRemoteIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcRemoteIpAddr.setStatus(_A)
class _NnfrPvcPolicingEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('none',0),('standard',2)))
_NnfrPvcPolicingEnable_Type.__name__=_C
_NnfrPvcPolicingEnable_Object=MibTableColumn
nnfrPvcPolicingEnable=_NnfrPvcPolicingEnable_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,7),_NnfrPvcPolicingEnable_Type())
nnfrPvcPolicingEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcPolicingEnable.setStatus(_A)
class _NnfrPvcPolicingDe_Type(TruthValue):defaultValue=1
_NnfrPvcPolicingDe_Type.__name__=_F
_NnfrPvcPolicingDe_Object=MibTableColumn
nnfrPvcPolicingDe=_NnfrPvcPolicingDe_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,8),_NnfrPvcPolicingDe_Type())
nnfrPvcPolicingDe.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcPolicingDe.setStatus(_A)
_NnfrPvcPolicingCir_Type=Integer32
_NnfrPvcPolicingCir_Object=MibTableColumn
nnfrPvcPolicingCir=_NnfrPvcPolicingCir_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,9),_NnfrPvcPolicingCir_Type())
nnfrPvcPolicingCir.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcPolicingCir.setStatus(_A)
if mibBuilder.loadTexts:nnfrPvcPolicingCir.setUnits(_J)
_NnfrPvcPolicingBc_Type=Integer32
_NnfrPvcPolicingBc_Object=MibTableColumn
nnfrPvcPolicingBc=_NnfrPvcPolicingBc_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,10),_NnfrPvcPolicingBc_Type())
nnfrPvcPolicingBc.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcPolicingBc.setStatus(_A)
if mibBuilder.loadTexts:nnfrPvcPolicingBc.setUnits(_J)
class _NnfrPvcPolicingBe_Type(Integer32):defaultValue=0
_NnfrPvcPolicingBe_Type.__name__=_C
_NnfrPvcPolicingBe_Object=MibTableColumn
nnfrPvcPolicingBe=_NnfrPvcPolicingBe_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,11),_NnfrPvcPolicingBe_Type())
nnfrPvcPolicingBe.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcPolicingBe.setStatus(_A)
_NnfrPvcShapingCir_Type=Integer32
_NnfrPvcShapingCir_Object=MibTableColumn
nnfrPvcShapingCir=_NnfrPvcShapingCir_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,12),_NnfrPvcShapingCir_Type())
nnfrPvcShapingCir.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcShapingCir.setStatus(_A)
if mibBuilder.loadTexts:nnfrPvcShapingCir.setUnits(_J)
_NnfrPvcShapingBcMax_Type=Integer32
_NnfrPvcShapingBcMax_Object=MibTableColumn
nnfrPvcShapingBcMax=_NnfrPvcShapingBcMax_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,13),_NnfrPvcShapingBcMax_Type())
nnfrPvcShapingBcMax.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcShapingBcMax.setStatus(_A)
if mibBuilder.loadTexts:nnfrPvcShapingBcMax.setUnits(_J)
_NnfrPvcShapingBcMin_Type=Integer32
_NnfrPvcShapingBcMin_Object=MibTableColumn
nnfrPvcShapingBcMin=_NnfrPvcShapingBcMin_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,14),_NnfrPvcShapingBcMin_Type())
nnfrPvcShapingBcMin.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcShapingBcMin.setStatus(_A)
if mibBuilder.loadTexts:nnfrPvcShapingBcMin.setUnits(_J)
class _NnfrPvcShapingBe_Type(Integer32):defaultValue=0
_NnfrPvcShapingBe_Type.__name__=_C
_NnfrPvcShapingBe_Object=MibTableColumn
nnfrPvcShapingBe=_NnfrPvcShapingBe_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,15),_NnfrPvcShapingBe_Type())
nnfrPvcShapingBe.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcShapingBe.setStatus(_A)
_NnfrPvcDlciForSwitching_Type=Integer32
_NnfrPvcDlciForSwitching_Object=MibTableColumn
nnfrPvcDlciForSwitching=_NnfrPvcDlciForSwitching_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,16),_NnfrPvcDlciForSwitching_Type())
nnfrPvcDlciForSwitching.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcDlciForSwitching.setStatus(_A)
_NnfrPvcBundleNameForSwitching_Type=DisplayString
_NnfrPvcBundleNameForSwitching_Object=MibTableColumn
nnfrPvcBundleNameForSwitching=_NnfrPvcBundleNameForSwitching_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,17),_NnfrPvcBundleNameForSwitching_Type())
nnfrPvcBundleNameForSwitching.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcBundleNameForSwitching.setStatus(_A)
_NnfrPvcRowStatus_Type=RowStatus
_NnfrPvcRowStatus_Object=MibTableColumn
nnfrPvcRowStatus=_NnfrPvcRowStatus_Object((1,3,6,1,4,1,562,73,1,1,1,16,2,1,18),_NnfrPvcRowStatus_Type())
nnfrPvcRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrPvcRowStatus.setStatus(_A)
_NnfrStatsTable_Object=MibTable
nnfrStatsTable=_NnfrStatsTable_Object((1,3,6,1,4,1,562,73,1,1,1,16,3))
if mibBuilder.loadTexts:nnfrStatsTable.setStatus(_A)
_NnfrStatsTableEntry_Object=MibTableRow
nnfrStatsTableEntry=_NnfrStatsTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,16,3,1))
nnfrStatsTableEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:nnfrStatsTableEntry.setStatus(_A)
_NnfrStatsFramesRx_Type=Counter32
_NnfrStatsFramesRx_Object=MibTableColumn
nnfrStatsFramesRx=_NnfrStatsFramesRx_Object((1,3,6,1,4,1,562,73,1,1,1,16,3,1,1),_NnfrStatsFramesRx_Type())
nnfrStatsFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrStatsFramesRx.setStatus(_A)
_NnfrStatsInvFramesRx_Type=Counter32
_NnfrStatsInvFramesRx_Object=MibTableColumn
nnfrStatsInvFramesRx=_NnfrStatsInvFramesRx_Object((1,3,6,1,4,1,562,73,1,1,1,16,3,1,2),_NnfrStatsInvFramesRx_Type())
nnfrStatsInvFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrStatsInvFramesRx.setStatus(_A)
_NnfrStatsFECNsRx_Type=Counter32
_NnfrStatsFECNsRx_Object=MibTableColumn
nnfrStatsFECNsRx=_NnfrStatsFECNsRx_Object((1,3,6,1,4,1,562,73,1,1,1,16,3,1,3),_NnfrStatsFECNsRx_Type())
nnfrStatsFECNsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrStatsFECNsRx.setStatus(_A)
_NnfrStatsBECNsRx_Type=Counter32
_NnfrStatsBECNsRx_Object=MibTableColumn
nnfrStatsBECNsRx=_NnfrStatsBECNsRx_Object((1,3,6,1,4,1,562,73,1,1,1,16,3,1,4),_NnfrStatsBECNsRx_Type())
nnfrStatsBECNsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrStatsBECNsRx.setStatus(_A)
_NnfrStatsShortFramesRx_Type=Counter32
_NnfrStatsShortFramesRx_Object=MibTableColumn
nnfrStatsShortFramesRx=_NnfrStatsShortFramesRx_Object((1,3,6,1,4,1,562,73,1,1,1,16,3,1,5),_NnfrStatsShortFramesRx_Type())
nnfrStatsShortFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrStatsShortFramesRx.setStatus(_A)
_NnfrStatsLongFramesRx_Type=Counter32
_NnfrStatsLongFramesRx_Object=MibTableColumn
nnfrStatsLongFramesRx=_NnfrStatsLongFramesRx_Object((1,3,6,1,4,1,562,73,1,1,1,16,3,1,6),_NnfrStatsLongFramesRx_Type())
nnfrStatsLongFramesRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrStatsLongFramesRx.setStatus(_A)
_NnfrStatsInvDLCIsRx_Type=Counter32
_NnfrStatsInvDLCIsRx_Object=MibTableColumn
nnfrStatsInvDLCIsRx=_NnfrStatsInvDLCIsRx_Object((1,3,6,1,4,1,562,73,1,1,1,16,3,1,7),_NnfrStatsInvDLCIsRx_Type())
nnfrStatsInvDLCIsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrStatsInvDLCIsRx.setStatus(_A)
_NnfrStatsUnknownDLCIsRx_Type=Counter32
_NnfrStatsUnknownDLCIsRx_Object=MibTableColumn
nnfrStatsUnknownDLCIsRx=_NnfrStatsUnknownDLCIsRx_Object((1,3,6,1,4,1,562,73,1,1,1,16,3,1,8),_NnfrStatsUnknownDLCIsRx_Type())
nnfrStatsUnknownDLCIsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrStatsUnknownDLCIsRx.setStatus(_A)
_NnfrStatsFramesTx_Type=Counter32
_NnfrStatsFramesTx_Object=MibTableColumn
nnfrStatsFramesTx=_NnfrStatsFramesTx_Object((1,3,6,1,4,1,562,73,1,1,1,16,3,1,9),_NnfrStatsFramesTx_Type())
nnfrStatsFramesTx.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrStatsFramesTx.setStatus(_A)
_NnfrPvcStatsTable_Object=MibTable
nnfrPvcStatsTable=_NnfrPvcStatsTable_Object((1,3,6,1,4,1,562,73,1,1,1,16,4))
if mibBuilder.loadTexts:nnfrPvcStatsTable.setStatus(_A)
_NnfrPvcStatsTableEntry_Object=MibTableRow
nnfrPvcStatsTableEntry=_NnfrPvcStatsTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1))
nnfrPvcStatsTableEntry.setIndexNames((0,_H,_I),(0,_G,_K))
if mibBuilder.loadTexts:nnfrPvcStatsTableEntry.setStatus(_A)
_NnfrPvcStatsBytesRxLastBootOrClear_Type=Counter32
_NnfrPvcStatsBytesRxLastBootOrClear_Object=MibTableColumn
nnfrPvcStatsBytesRxLastBootOrClear=_NnfrPvcStatsBytesRxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,1),_NnfrPvcStatsBytesRxLastBootOrClear_Type())
nnfrPvcStatsBytesRxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsBytesRxLastBootOrClear.setStatus(_A)
_NnfrPvcStatsBytesTxLastBootOrClear_Type=Counter32
_NnfrPvcStatsBytesTxLastBootOrClear_Object=MibTableColumn
nnfrPvcStatsBytesTxLastBootOrClear=_NnfrPvcStatsBytesTxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,2),_NnfrPvcStatsBytesTxLastBootOrClear_Type())
nnfrPvcStatsBytesTxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsBytesTxLastBootOrClear.setStatus(_A)
_NnfrPvcStatsPktsRxLastBootOrClear_Type=Counter32
_NnfrPvcStatsPktsRxLastBootOrClear_Object=MibTableColumn
nnfrPvcStatsPktsRxLastBootOrClear=_NnfrPvcStatsPktsRxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,3),_NnfrPvcStatsPktsRxLastBootOrClear_Type())
nnfrPvcStatsPktsRxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsPktsRxLastBootOrClear.setStatus(_A)
_NnfrPvcStatsPktsTxLastBootOrClear_Type=Counter32
_NnfrPvcStatsPktsTxLastBootOrClear_Object=MibTableColumn
nnfrPvcStatsPktsTxLastBootOrClear=_NnfrPvcStatsPktsTxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,4),_NnfrPvcStatsPktsTxLastBootOrClear_Type())
nnfrPvcStatsPktsTxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsPktsTxLastBootOrClear.setStatus(_A)
_NnfrPvcStatsErrPktsRxLastBootOrClear_Type=Counter32
_NnfrPvcStatsErrPktsRxLastBootOrClear_Object=MibTableColumn
nnfrPvcStatsErrPktsRxLastBootOrClear=_NnfrPvcStatsErrPktsRxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,5),_NnfrPvcStatsErrPktsRxLastBootOrClear_Type())
nnfrPvcStatsErrPktsRxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsErrPktsRxLastBootOrClear.setStatus(_A)
_NnfrPvcStatsUpDownStatesLastBootOrClear_Type=Counter32
_NnfrPvcStatsUpDownStatesLastBootOrClear_Object=MibTableColumn
nnfrPvcStatsUpDownStatesLastBootOrClear=_NnfrPvcStatsUpDownStatesLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,6),_NnfrPvcStatsUpDownStatesLastBootOrClear_Type())
nnfrPvcStatsUpDownStatesLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsUpDownStatesLastBootOrClear.setStatus(_A)
_NnfrPvcStatsBytesRxLastFiveMins_Type=Counter32
_NnfrPvcStatsBytesRxLastFiveMins_Object=MibTableColumn
nnfrPvcStatsBytesRxLastFiveMins=_NnfrPvcStatsBytesRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,7),_NnfrPvcStatsBytesRxLastFiveMins_Type())
nnfrPvcStatsBytesRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsBytesRxLastFiveMins.setStatus(_A)
_NnfrPvcStatsBytesTxLastFiveMins_Type=Counter32
_NnfrPvcStatsBytesTxLastFiveMins_Object=MibTableColumn
nnfrPvcStatsBytesTxLastFiveMins=_NnfrPvcStatsBytesTxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,8),_NnfrPvcStatsBytesTxLastFiveMins_Type())
nnfrPvcStatsBytesTxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsBytesTxLastFiveMins.setStatus(_A)
_NnfrPvcStatsPktsRxLastFiveMins_Type=Counter32
_NnfrPvcStatsPktsRxLastFiveMins_Object=MibTableColumn
nnfrPvcStatsPktsRxLastFiveMins=_NnfrPvcStatsPktsRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,9),_NnfrPvcStatsPktsRxLastFiveMins_Type())
nnfrPvcStatsPktsRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsPktsRxLastFiveMins.setStatus(_A)
_NnfrPvcStatsPktsTxLastFiveMins_Type=Counter32
_NnfrPvcStatsPktsTxLastFiveMins_Object=MibTableColumn
nnfrPvcStatsPktsTxLastFiveMins=_NnfrPvcStatsPktsTxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,10),_NnfrPvcStatsPktsTxLastFiveMins_Type())
nnfrPvcStatsPktsTxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsPktsTxLastFiveMins.setStatus(_A)
_NnfrPvcStatsErrPktsRxLastFiveMins_Type=Counter32
_NnfrPvcStatsErrPktsRxLastFiveMins_Object=MibTableColumn
nnfrPvcStatsErrPktsRxLastFiveMins=_NnfrPvcStatsErrPktsRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,11),_NnfrPvcStatsErrPktsRxLastFiveMins_Type())
nnfrPvcStatsErrPktsRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsErrPktsRxLastFiveMins.setStatus(_A)
_NnfrPvcStatsUpDownStatesLastFiveMins_Type=Counter32
_NnfrPvcStatsUpDownStatesLastFiveMins_Object=MibTableColumn
nnfrPvcStatsUpDownStatesLastFiveMins=_NnfrPvcStatsUpDownStatesLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,4,1,12),_NnfrPvcStatsUpDownStatesLastFiveMins_Type())
nnfrPvcStatsUpDownStatesLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrPvcStatsUpDownStatesLastFiveMins.setStatus(_A)
_NnfrAvcTable_Object=MibTable
nnfrAvcTable=_NnfrAvcTable_Object((1,3,6,1,4,1,562,73,1,1,1,16,5))
if mibBuilder.loadTexts:nnfrAvcTable.setStatus(_A)
_NnfrAvcTableEntry_Object=MibTableRow
nnfrAvcTableEntry=_NnfrAvcTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1))
nnfrAvcTableEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:nnfrAvcTableEntry.setStatus(_A)
_NnfrAvcId_Type=Integer32
_NnfrAvcId_Object=MibTableColumn
nnfrAvcId=_NnfrAvcId_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,1),_NnfrAvcId_Type())
nnfrAvcId.setMaxAccess(_Q)
if mibBuilder.loadTexts:nnfrAvcId.setStatus(_A)
class _NnfrAvcDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,991))
_NnfrAvcDlci_Type.__name__=_C
_NnfrAvcDlci_Object=MibTableColumn
nnfrAvcDlci=_NnfrAvcDlci_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,2),_NnfrAvcDlci_Type())
nnfrAvcDlci.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrAvcDlci.setStatus(_A)
class _NnfrAvcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NnfrAvcName_Type.__name__=_M
_NnfrAvcName_Object=MibTableColumn
nnfrAvcName=_NnfrAvcName_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,3),_NnfrAvcName_Type())
nnfrAvcName.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrAvcName.setStatus(_A)
_NnfrAvcIpAddr_Type=IpAddress
_NnfrAvcIpAddr_Object=MibTableColumn
nnfrAvcIpAddr=_NnfrAvcIpAddr_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,4),_NnfrAvcIpAddr_Type())
nnfrAvcIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrAvcIpAddr.setStatus(_A)
_NnfrAvcIpSubnetMask_Type=IpAddress
_NnfrAvcIpSubnetMask_Object=MibTableColumn
nnfrAvcIpSubnetMask=_NnfrAvcIpSubnetMask_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,5),_NnfrAvcIpSubnetMask_Type())
nnfrAvcIpSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrAvcIpSubnetMask.setStatus(_A)
_NnfrAvcRemoteIpAddr_Type=IpAddress
_NnfrAvcRemoteIpAddr_Object=MibTableColumn
nnfrAvcRemoteIpAddr=_NnfrAvcRemoteIpAddr_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,6),_NnfrAvcRemoteIpAddr_Type())
nnfrAvcRemoteIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrAvcRemoteIpAddr.setStatus(_A)
class _NnfrAvcClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3),('classD',4),('classE',5)))
_NnfrAvcClass_Type.__name__=_C
_NnfrAvcClass_Object=MibTableColumn
nnfrAvcClass=_NnfrAvcClass_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,7),_NnfrAvcClass_Type())
nnfrAvcClass.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrAvcClass.setStatus(_A)
_NnfrAvcClassThreshold_Type=Integer32
_NnfrAvcClassThreshold_Object=MibTableColumn
nnfrAvcClassThreshold=_NnfrAvcClassThreshold_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,8),_NnfrAvcClassThreshold_Type())
nnfrAvcClassThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrAvcClassThreshold.setStatus(_A)
class _NnfrAvcFragmentSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(56,4096))
_NnfrAvcFragmentSize_Type.__name__=_C
_NnfrAvcFragmentSize_Object=MibTableColumn
nnfrAvcFragmentSize=_NnfrAvcFragmentSize_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,9),_NnfrAvcFragmentSize_Type())
nnfrAvcFragmentSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrAvcFragmentSize.setStatus(_A)
class _NnfrAvcSegThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(56,4096))
_NnfrAvcSegThreshold_Type.__name__=_C
_NnfrAvcSegThreshold_Object=MibTableColumn
nnfrAvcSegThreshold=_NnfrAvcSegThreshold_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,10),_NnfrAvcSegThreshold_Type())
nnfrAvcSegThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrAvcSegThreshold.setStatus(_A)
class _NnfrAvcSequence_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('short',1),('long',2)))
_NnfrAvcSequence_Type.__name__=_C
_NnfrAvcSequence_Object=MibTableColumn
nnfrAvcSequence=_NnfrAvcSequence_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,11),_NnfrAvcSequence_Type())
nnfrAvcSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrAvcSequence.setStatus(_A)
class _NnfrAvcDiffDelay_Type(Integer32):defaultValue=80
_NnfrAvcDiffDelay_Type.__name__=_C
_NnfrAvcDiffDelay_Object=MibTableColumn
nnfrAvcDiffDelay=_NnfrAvcDiffDelay_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,12),_NnfrAvcDiffDelay_Type())
nnfrAvcDiffDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrAvcDiffDelay.setStatus(_A)
class _NnfrAvcEnhancedMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_NnfrAvcEnhancedMode_Type.__name__=_C
_NnfrAvcEnhancedMode_Object=MibTableColumn
nnfrAvcEnhancedMode=_NnfrAvcEnhancedMode_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,13),_NnfrAvcEnhancedMode_Type())
nnfrAvcEnhancedMode.setMaxAccess(_D)
if mibBuilder.loadTexts:nnfrAvcEnhancedMode.setStatus(_A)
_NnfrAvcNoOfCvcs_Type=Integer32
_NnfrAvcNoOfCvcs_Object=MibTableColumn
nnfrAvcNoOfCvcs=_NnfrAvcNoOfCvcs_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,14),_NnfrAvcNoOfCvcs_Type())
nnfrAvcNoOfCvcs.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcNoOfCvcs.setStatus(_A)
_NnfrAvcTotalBw_Type=Integer32
_NnfrAvcTotalBw_Object=MibTableColumn
nnfrAvcTotalBw=_NnfrAvcTotalBw_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,15),_NnfrAvcTotalBw_Type())
nnfrAvcTotalBw.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcTotalBw.setStatus(_A)
if mibBuilder.loadTexts:nnfrAvcTotalBw.setUnits('kbps')
class _NnfrAvcEnable_Type(TruthValue):defaultValue=1
_NnfrAvcEnable_Type.__name__=_F
_NnfrAvcEnable_Object=MibTableColumn
nnfrAvcEnable=_NnfrAvcEnable_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,16),_NnfrAvcEnable_Type())
nnfrAvcEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrAvcEnable.setStatus(_A)
_NnfrAvcRowStatus_Type=RowStatus
_NnfrAvcRowStatus_Object=MibTableColumn
nnfrAvcRowStatus=_NnfrAvcRowStatus_Object((1,3,6,1,4,1,562,73,1,1,1,16,5,1,17),_NnfrAvcRowStatus_Type())
nnfrAvcRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrAvcRowStatus.setStatus(_A)
_NnfrCvcTable_Object=MibTable
nnfrCvcTable=_NnfrCvcTable_Object((1,3,6,1,4,1,562,73,1,1,1,16,6))
if mibBuilder.loadTexts:nnfrCvcTable.setStatus(_A)
_NnfrCvcTableEntry_Object=MibTableRow
nnfrCvcTableEntry=_NnfrCvcTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,16,6,1))
nnfrCvcTableEntry.setIndexNames((0,_G,_L),(0,_H,_I),(0,_G,_K))
if mibBuilder.loadTexts:nnfrCvcTableEntry.setStatus(_A)
_NnfrCvcBundleName_Type=DisplayString
_NnfrCvcBundleName_Object=MibTableColumn
nnfrCvcBundleName=_NnfrCvcBundleName_Object((1,3,6,1,4,1,562,73,1,1,1,16,6,1,1),_NnfrCvcBundleName_Type())
nnfrCvcBundleName.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrCvcBundleName.setStatus(_A)
class _NnfrCvcEnable_Type(TruthValue):defaultValue=1
_NnfrCvcEnable_Type.__name__=_F
_NnfrCvcEnable_Object=MibTableColumn
nnfrCvcEnable=_NnfrCvcEnable_Object((1,3,6,1,4,1,562,73,1,1,1,16,6,1,2),_NnfrCvcEnable_Type())
nnfrCvcEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrCvcEnable.setStatus(_A)
_NnfrCvcRowStatus_Type=RowStatus
_NnfrCvcRowStatus_Object=MibTableColumn
nnfrCvcRowStatus=_NnfrCvcRowStatus_Object((1,3,6,1,4,1,562,73,1,1,1,16,6,1,3),_NnfrCvcRowStatus_Type())
nnfrCvcRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:nnfrCvcRowStatus.setStatus(_A)
_NnfrAvcStatsTable_Object=MibTable
nnfrAvcStatsTable=_NnfrAvcStatsTable_Object((1,3,6,1,4,1,562,73,1,1,1,16,7))
if mibBuilder.loadTexts:nnfrAvcStatsTable.setStatus(_A)
_NnfrAvcStatsTableEntry_Object=MibTableRow
nnfrAvcStatsTableEntry=_NnfrAvcStatsTableEntry_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1))
nnfrAvcStatsTableEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:nnfrAvcStatsTableEntry.setStatus(_A)
_NnfrAvcStatsBytesRxLastBootOrClear_Type=Counter32
_NnfrAvcStatsBytesRxLastBootOrClear_Object=MibTableColumn
nnfrAvcStatsBytesRxLastBootOrClear=_NnfrAvcStatsBytesRxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,1),_NnfrAvcStatsBytesRxLastBootOrClear_Type())
nnfrAvcStatsBytesRxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsBytesRxLastBootOrClear.setStatus(_A)
_NnfrAvcStatsBytesTxLastBootOrClear_Type=Counter32
_NnfrAvcStatsBytesTxLastBootOrClear_Object=MibTableColumn
nnfrAvcStatsBytesTxLastBootOrClear=_NnfrAvcStatsBytesTxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,2),_NnfrAvcStatsBytesTxLastBootOrClear_Type())
nnfrAvcStatsBytesTxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsBytesTxLastBootOrClear.setStatus(_A)
_NnfrAvcStatsPktsRxLastBootOrClear_Type=Counter32
_NnfrAvcStatsPktsRxLastBootOrClear_Object=MibTableColumn
nnfrAvcStatsPktsRxLastBootOrClear=_NnfrAvcStatsPktsRxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,3),_NnfrAvcStatsPktsRxLastBootOrClear_Type())
nnfrAvcStatsPktsRxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsPktsRxLastBootOrClear.setStatus(_A)
_NnfrAvcStatsPktsTxLastBootOrClear_Type=Counter32
_NnfrAvcStatsPktsTxLastBootOrClear_Object=MibTableColumn
nnfrAvcStatsPktsTxLastBootOrClear=_NnfrAvcStatsPktsTxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,4),_NnfrAvcStatsPktsTxLastBootOrClear_Type())
nnfrAvcStatsPktsTxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsPktsTxLastBootOrClear.setStatus(_A)
_NnfrAvcStatsErrPktsRxLastBootOrClear_Type=Counter32
_NnfrAvcStatsErrPktsRxLastBootOrClear_Object=MibTableColumn
nnfrAvcStatsErrPktsRxLastBootOrClear=_NnfrAvcStatsErrPktsRxLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,5),_NnfrAvcStatsErrPktsRxLastBootOrClear_Type())
nnfrAvcStatsErrPktsRxLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsErrPktsRxLastBootOrClear.setStatus(_A)
_NnfrAvcStatsUpDownStatesLastBootOrClear_Type=Counter32
_NnfrAvcStatsUpDownStatesLastBootOrClear_Object=MibTableColumn
nnfrAvcStatsUpDownStatesLastBootOrClear=_NnfrAvcStatsUpDownStatesLastBootOrClear_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,6),_NnfrAvcStatsUpDownStatesLastBootOrClear_Type())
nnfrAvcStatsUpDownStatesLastBootOrClear.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsUpDownStatesLastBootOrClear.setStatus(_A)
_NnfrAvcStatsBytesRxLastFiveMins_Type=Counter32
_NnfrAvcStatsBytesRxLastFiveMins_Object=MibTableColumn
nnfrAvcStatsBytesRxLastFiveMins=_NnfrAvcStatsBytesRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,7),_NnfrAvcStatsBytesRxLastFiveMins_Type())
nnfrAvcStatsBytesRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsBytesRxLastFiveMins.setStatus(_A)
_NnfrAvcStatsBytesTxLastFiveMins_Type=Counter32
_NnfrAvcStatsBytesTxLastFiveMins_Object=MibTableColumn
nnfrAvcStatsBytesTxLastFiveMins=_NnfrAvcStatsBytesTxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,8),_NnfrAvcStatsBytesTxLastFiveMins_Type())
nnfrAvcStatsBytesTxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsBytesTxLastFiveMins.setStatus(_A)
_NnfrAvcStatsPktsRxLastFiveMins_Type=Counter32
_NnfrAvcStatsPktsRxLastFiveMins_Object=MibTableColumn
nnfrAvcStatsPktsRxLastFiveMins=_NnfrAvcStatsPktsRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,9),_NnfrAvcStatsPktsRxLastFiveMins_Type())
nnfrAvcStatsPktsRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsPktsRxLastFiveMins.setStatus(_A)
_NnfrAvcStatsPktsTxLastFiveMins_Type=Counter32
_NnfrAvcStatsPktsTxLastFiveMins_Object=MibTableColumn
nnfrAvcStatsPktsTxLastFiveMins=_NnfrAvcStatsPktsTxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,10),_NnfrAvcStatsPktsTxLastFiveMins_Type())
nnfrAvcStatsPktsTxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsPktsTxLastFiveMins.setStatus(_A)
_NnfrAvcStatsErrPktsRxLastFiveMins_Type=Counter32
_NnfrAvcStatsErrPktsRxLastFiveMins_Object=MibTableColumn
nnfrAvcStatsErrPktsRxLastFiveMins=_NnfrAvcStatsErrPktsRxLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,11),_NnfrAvcStatsErrPktsRxLastFiveMins_Type())
nnfrAvcStatsErrPktsRxLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsErrPktsRxLastFiveMins.setStatus(_A)
_NnfrAvcStatsUpDownStatesLastFiveMins_Type=Counter32
_NnfrAvcStatsUpDownStatesLastFiveMins_Object=MibTableColumn
nnfrAvcStatsUpDownStatesLastFiveMins=_NnfrAvcStatsUpDownStatesLastFiveMins_Object((1,3,6,1,4,1,562,73,1,1,1,16,7,1,12),_NnfrAvcStatsUpDownStatesLastFiveMins_Type())
nnfrAvcStatsUpDownStatesLastFiveMins.setMaxAccess(_B)
if mibBuilder.loadTexts:nnfrAvcStatsUpDownStatesLastFiveMins.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'nnfrMib':nnfrMib,'nnfrTable':nnfrTable,'nnfrTableEntry':nnfrTableEntry,'nnfrIfEnable':nnfrIfEnable,'nnfrEnablePvcAll':nnfrEnablePvcAll,'nnfrFrameSize':nnfrFrameSize,'nnfrIfType':nnfrIfType,'nnfrLmiType':nnfrLmiType,'nnfrLmiDceN392':nnfrLmiDceN392,'nnfrLmiDceN393':nnfrLmiDceN393,'nnfrLmiDteN392':nnfrLmiDteN392,'nnfrLmiDteN393':nnfrLmiDteN393,'nnfrLmiDteN391':nnfrLmiDteN391,'nnfrLmiKeepalive':nnfrLmiKeepalive,'nnmfrAckMsgTimer':nnmfrAckMsgTimer,'nnmfrAckMsgMaxRetry':nnmfrAckMsgMaxRetry,'nnmfrClass':nnmfrClass,'nnmfrClassThreshold':nnmfrClassThreshold,'nnmfrFrameSize':nnmfrFrameSize,'nnmfrHelloTimer':nnmfrHelloTimer,'nnmfrSegThreshold':nnmfrSegThreshold,'nnmfrDiffDelay':nnmfrDiffDelay,'nnfrPvcTable':nnfrPvcTable,'nnfrPvcTableEntry':nnfrPvcTableEntry,_K:nnfrPvcDlci,'nnfrPvcEnable':nnfrPvcEnable,'nnfrPvcDescr':nnfrPvcDescr,'nnfrPvcIpAddr':nnfrPvcIpAddr,'nnfrPvcIpSubnetMask':nnfrPvcIpSubnetMask,'nnfrPvcRemoteIpAddr':nnfrPvcRemoteIpAddr,'nnfrPvcPolicingEnable':nnfrPvcPolicingEnable,'nnfrPvcPolicingDe':nnfrPvcPolicingDe,'nnfrPvcPolicingCir':nnfrPvcPolicingCir,'nnfrPvcPolicingBc':nnfrPvcPolicingBc,'nnfrPvcPolicingBe':nnfrPvcPolicingBe,'nnfrPvcShapingCir':nnfrPvcShapingCir,'nnfrPvcShapingBcMax':nnfrPvcShapingBcMax,'nnfrPvcShapingBcMin':nnfrPvcShapingBcMin,'nnfrPvcShapingBe':nnfrPvcShapingBe,'nnfrPvcDlciForSwitching':nnfrPvcDlciForSwitching,'nnfrPvcBundleNameForSwitching':nnfrPvcBundleNameForSwitching,'nnfrPvcRowStatus':nnfrPvcRowStatus,'nnfrStatsTable':nnfrStatsTable,'nnfrStatsTableEntry':nnfrStatsTableEntry,'nnfrStatsFramesRx':nnfrStatsFramesRx,'nnfrStatsInvFramesRx':nnfrStatsInvFramesRx,'nnfrStatsFECNsRx':nnfrStatsFECNsRx,'nnfrStatsBECNsRx':nnfrStatsBECNsRx,'nnfrStatsShortFramesRx':nnfrStatsShortFramesRx,'nnfrStatsLongFramesRx':nnfrStatsLongFramesRx,'nnfrStatsInvDLCIsRx':nnfrStatsInvDLCIsRx,'nnfrStatsUnknownDLCIsRx':nnfrStatsUnknownDLCIsRx,'nnfrStatsFramesTx':nnfrStatsFramesTx,'nnfrPvcStatsTable':nnfrPvcStatsTable,'nnfrPvcStatsTableEntry':nnfrPvcStatsTableEntry,'nnfrPvcStatsBytesRxLastBootOrClear':nnfrPvcStatsBytesRxLastBootOrClear,'nnfrPvcStatsBytesTxLastBootOrClear':nnfrPvcStatsBytesTxLastBootOrClear,'nnfrPvcStatsPktsRxLastBootOrClear':nnfrPvcStatsPktsRxLastBootOrClear,'nnfrPvcStatsPktsTxLastBootOrClear':nnfrPvcStatsPktsTxLastBootOrClear,'nnfrPvcStatsErrPktsRxLastBootOrClear':nnfrPvcStatsErrPktsRxLastBootOrClear,'nnfrPvcStatsUpDownStatesLastBootOrClear':nnfrPvcStatsUpDownStatesLastBootOrClear,'nnfrPvcStatsBytesRxLastFiveMins':nnfrPvcStatsBytesRxLastFiveMins,'nnfrPvcStatsBytesTxLastFiveMins':nnfrPvcStatsBytesTxLastFiveMins,'nnfrPvcStatsPktsRxLastFiveMins':nnfrPvcStatsPktsRxLastFiveMins,'nnfrPvcStatsPktsTxLastFiveMins':nnfrPvcStatsPktsTxLastFiveMins,'nnfrPvcStatsErrPktsRxLastFiveMins':nnfrPvcStatsErrPktsRxLastFiveMins,'nnfrPvcStatsUpDownStatesLastFiveMins':nnfrPvcStatsUpDownStatesLastFiveMins,'nnfrAvcTable':nnfrAvcTable,'nnfrAvcTableEntry':nnfrAvcTableEntry,_L:nnfrAvcId,'nnfrAvcDlci':nnfrAvcDlci,'nnfrAvcName':nnfrAvcName,'nnfrAvcIpAddr':nnfrAvcIpAddr,'nnfrAvcIpSubnetMask':nnfrAvcIpSubnetMask,'nnfrAvcRemoteIpAddr':nnfrAvcRemoteIpAddr,'nnfrAvcClass':nnfrAvcClass,'nnfrAvcClassThreshold':nnfrAvcClassThreshold,'nnfrAvcFragmentSize':nnfrAvcFragmentSize,'nnfrAvcSegThreshold':nnfrAvcSegThreshold,'nnfrAvcSequence':nnfrAvcSequence,'nnfrAvcDiffDelay':nnfrAvcDiffDelay,'nnfrAvcEnhancedMode':nnfrAvcEnhancedMode,'nnfrAvcNoOfCvcs':nnfrAvcNoOfCvcs,'nnfrAvcTotalBw':nnfrAvcTotalBw,'nnfrAvcEnable':nnfrAvcEnable,'nnfrAvcRowStatus':nnfrAvcRowStatus,'nnfrCvcTable':nnfrCvcTable,'nnfrCvcTableEntry':nnfrCvcTableEntry,'nnfrCvcBundleName':nnfrCvcBundleName,'nnfrCvcEnable':nnfrCvcEnable,'nnfrCvcRowStatus':nnfrCvcRowStatus,'nnfrAvcStatsTable':nnfrAvcStatsTable,'nnfrAvcStatsTableEntry':nnfrAvcStatsTableEntry,'nnfrAvcStatsBytesRxLastBootOrClear':nnfrAvcStatsBytesRxLastBootOrClear,'nnfrAvcStatsBytesTxLastBootOrClear':nnfrAvcStatsBytesTxLastBootOrClear,'nnfrAvcStatsPktsRxLastBootOrClear':nnfrAvcStatsPktsRxLastBootOrClear,'nnfrAvcStatsPktsTxLastBootOrClear':nnfrAvcStatsPktsTxLastBootOrClear,'nnfrAvcStatsErrPktsRxLastBootOrClear':nnfrAvcStatsErrPktsRxLastBootOrClear,'nnfrAvcStatsUpDownStatesLastBootOrClear':nnfrAvcStatsUpDownStatesLastBootOrClear,'nnfrAvcStatsBytesRxLastFiveMins':nnfrAvcStatsBytesRxLastFiveMins,'nnfrAvcStatsBytesTxLastFiveMins':nnfrAvcStatsBytesTxLastFiveMins,'nnfrAvcStatsPktsRxLastFiveMins':nnfrAvcStatsPktsRxLastFiveMins,'nnfrAvcStatsPktsTxLastFiveMins':nnfrAvcStatsPktsTxLastFiveMins,'nnfrAvcStatsErrPktsRxLastFiveMins':nnfrAvcStatsErrPktsRxLastFiveMins,'nnfrAvcStatsUpDownStatesLastFiveMins':nnfrAvcStatsUpDownStatesLastFiveMins})