_q='fsDCBXMode'
_p='fsAppPriDcbxOperState'
_o='fsAppPriAdminMode'
_n='fsAppPriModuleStatus'
_m='fsPFCDcbxOperState'
_l='fsPFCAdminMode'
_k='fsPFCModuleStatus'
_j='fsETSDcbxOperState'
_i='fsETSAdminMode'
_h='fsETSModuleStatus'
_g='fslldpXdot1dcbxConfigTCSupportedEntry'
_f='fsAppPriXAppEntry'
_e='fsDcbxCEECtrlPortNumber'
_d='fsAppPriPortNumber'
_c='fsPFCPortNumber'
_b='fsETSPortNumber'
_a='DcbxVersion'
_Z='fsDCBXPortNumber'
_Y='fsDcbPortNumber'
_X='unknown'
_W='disabled'
_V='accessible-for-notify'
_U='shutdown'
_T='start'
_S='lldpV2RemTimeMark'
_R='lldpV2RemLocalIfIndex'
_Q='lldpV2RemLocalDestMACAddress'
_P='lldpV2RemIndex'
_O='fsDcbPeerUpStatus'
_N='DcbAdminMode'
_M='Unsigned32'
_L='fsDcbFeatureType'
_K='lldpV2LocPortIfIndex'
_J='not-accessible'
_I='EnabledStatus'
_H='Integer32'
_G='TruthValue'
_F='LLDP-V2-MIB'
_E='fsDcbTrapPortNumber'
_D='read-write'
_C='ARICENT-DCB-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
lldpXdot1dcbxAdminApplicationPriorityAppEntry,=mibBuilder.importSymbols('LLDP-EXT-DOT1-DCBX-MIB','lldpXdot1dcbxAdminApplicationPriorityAppEntry')
lldpV2LocPortIfIndex,lldpV2PortConfigEntry,lldpV2RemIndex,lldpV2RemLocalDestMACAddress,lldpV2RemLocalIfIndex,lldpV2RemTimeMark=mibBuilder.importSymbols(_F,_K,'lldpV2PortConfigEntry',_P,_Q,_R,_S)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_G)
fsDcbMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,22))
if mibBuilder.loadTexts:fsDcbMIB.setRevisions(('2012-09-05 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_W,2)))
class DcbAdminMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('auto',0),('on',1),('off',2)))
class DcbState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('off',0),('init',1),('rxrecommended',2),('ceedisabled',3),('uselocalcfg',4),('usepeercfg',5)))
class DcbxVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),('ieee',2),('cee',3),(_X,4)))
class DcbStateMachineType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('asymmetric',1),('symmetric',2),('feature',3)))
class FsLldpXdot1dcbxTCSupportedCapacity(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,7))
class DcbxStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('peerNotAdvFeat',1),('peerNotAdvDcbx',2),('notAdvertise',3),(_W,4),('peerDisabled',5),('peerInError',6),('peerNWillingCompatibleCfg',7),('cfgNotCompatible',8),('ok',9),(_X,10)))
_FsDcbSystem_ObjectIdentity=ObjectIdentity
fsDcbSystem=_FsDcbSystem_ObjectIdentity((1,3,6,1,4,1,29601,2,22,1))
class _FsDcbPfcMinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDcbPfcMinThreshold_Type.__name__=_M
_FsDcbPfcMinThreshold_Object=MibScalar
fsDcbPfcMinThreshold=_FsDcbPfcMinThreshold_Object((1,3,6,1,4,1,29601,2,22,1,1),_FsDcbPfcMinThreshold_Type())
fsDcbPfcMinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDcbPfcMinThreshold.setStatus(_A)
class _FsDcbPfcMaxThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsDcbPfcMaxThreshold_Type.__name__=_M
_FsDcbPfcMaxThreshold_Object=MibScalar
fsDcbPfcMaxThreshold=_FsDcbPfcMaxThreshold_Object((1,3,6,1,4,1,29601,2,22,1,2),_FsDcbPfcMaxThreshold_Type())
fsDcbPfcMaxThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDcbPfcMaxThreshold.setStatus(_A)
class _FsDcbMaxPfcProfiles_Type(Unsigned32):defaultValue=256;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_FsDcbMaxPfcProfiles_Type.__name__=_M
_FsDcbMaxPfcProfiles_Object=MibScalar
fsDcbMaxPfcProfiles=_FsDcbMaxPfcProfiles_Object((1,3,6,1,4,1,29601,2,22,1,3),_FsDcbMaxPfcProfiles_Type())
fsDcbMaxPfcProfiles.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbMaxPfcProfiles.setStatus(_A)
_FsDcbObjects_ObjectIdentity=ObjectIdentity
fsDcbObjects=_FsDcbObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,22,2))
_FsDcbPortTable_Object=MibTable
fsDcbPortTable=_FsDcbPortTable_Object((1,3,6,1,4,1,29601,2,22,2,1))
if mibBuilder.loadTexts:fsDcbPortTable.setStatus(_A)
_FsDcbPortEntry_Object=MibTableRow
fsDcbPortEntry=_FsDcbPortEntry_Object((1,3,6,1,4,1,29601,2,22,2,1,1))
fsDcbPortEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:fsDcbPortEntry.setStatus(_A)
_FsDcbPortNumber_Type=InterfaceIndex
_FsDcbPortNumber_Object=MibTableColumn
fsDcbPortNumber=_FsDcbPortNumber_Object((1,3,6,1,4,1,29601,2,22,2,1,1,1),_FsDcbPortNumber_Type())
fsDcbPortNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:fsDcbPortNumber.setStatus(_A)
class _FsDcbETSAdminStatus_Type(EnabledStatus):defaultValue=2
_FsDcbETSAdminStatus_Type.__name__=_I
_FsDcbETSAdminStatus_Object=MibTableColumn
fsDcbETSAdminStatus=_FsDcbETSAdminStatus_Object((1,3,6,1,4,1,29601,2,22,2,1,1,2),_FsDcbETSAdminStatus_Type())
fsDcbETSAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbETSAdminStatus.setStatus(_A)
class _FsDcbPFCAdminStatus_Type(EnabledStatus):defaultValue=2
_FsDcbPFCAdminStatus_Type.__name__=_I
_FsDcbPFCAdminStatus_Object=MibTableColumn
fsDcbPFCAdminStatus=_FsDcbPFCAdminStatus_Object((1,3,6,1,4,1,29601,2,22,2,1,1,3),_FsDcbPFCAdminStatus_Type())
fsDcbPFCAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbPFCAdminStatus.setStatus(_A)
_FsDcbRowStatus_Type=RowStatus
_FsDcbRowStatus_Object=MibTableColumn
fsDcbRowStatus=_FsDcbRowStatus_Object((1,3,6,1,4,1,29601,2,22,2,1,1,4),_FsDcbRowStatus_Type())
fsDcbRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDcbRowStatus.setStatus(_A)
class _FsDcbAppPriAdminStatus_Type(EnabledStatus):defaultValue=2
_FsDcbAppPriAdminStatus_Type.__name__=_I
_FsDcbAppPriAdminStatus_Object=MibTableColumn
fsDcbAppPriAdminStatus=_FsDcbAppPriAdminStatus_Object((1,3,6,1,4,1,29601,2,22,2,1,1,5),_FsDcbAppPriAdminStatus_Type())
fsDcbAppPriAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbAppPriAdminStatus.setStatus(_A)
_FsDcbOperVersion_Type=DcbxVersion
_FsDcbOperVersion_Object=MibTableColumn
fsDcbOperVersion=_FsDcbOperVersion_Object((1,3,6,1,4,1,29601,2,22,2,1,1,6),_FsDcbOperVersion_Type())
fsDcbOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbOperVersion.setStatus(_A)
_FsDcbMaxVersion_Type=DcbxVersion
_FsDcbMaxVersion_Object=MibTableColumn
fsDcbMaxVersion=_FsDcbMaxVersion_Object((1,3,6,1,4,1,29601,2,22,2,1,1,7),_FsDcbMaxVersion_Type())
fsDcbMaxVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbMaxVersion.setStatus(_A)
_FsDcbPeerOperVersion_Type=DcbxVersion
_FsDcbPeerOperVersion_Object=MibTableColumn
fsDcbPeerOperVersion=_FsDcbPeerOperVersion_Object((1,3,6,1,4,1,29601,2,22,2,1,1,8),_FsDcbPeerOperVersion_Type())
fsDcbPeerOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbPeerOperVersion.setStatus(_A)
_FsDcbPeerMaxVersion_Type=DcbxVersion
_FsDcbPeerMaxVersion_Object=MibTableColumn
fsDcbPeerMaxVersion=_FsDcbPeerMaxVersion_Object((1,3,6,1,4,1,29601,2,22,2,1,1,9),_FsDcbPeerMaxVersion_Type())
fsDcbPeerMaxVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbPeerMaxVersion.setStatus(_A)
_FsDcbApplicationObjects_ObjectIdentity=ObjectIdentity
fsDcbApplicationObjects=_FsDcbApplicationObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3))
_FsDCBXObjects_ObjectIdentity=ObjectIdentity
fsDCBXObjects=_FsDCBXObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3,1))
_FsDCBXScalars_ObjectIdentity=ObjectIdentity
fsDCBXScalars=_FsDCBXScalars_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3,1,1))
class _FsDcbxGlobalTraceLevel_Type(Integer32):defaultValue=256
_FsDcbxGlobalTraceLevel_Type.__name__=_H
_FsDcbxGlobalTraceLevel_Object=MibScalar
fsDcbxGlobalTraceLevel=_FsDcbxGlobalTraceLevel_Object((1,3,6,1,4,1,29601,2,22,3,1,1,1),_FsDcbxGlobalTraceLevel_Type())
fsDcbxGlobalTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDcbxGlobalTraceLevel.setStatus(_A)
_FsDCBXPortTable_Object=MibTable
fsDCBXPortTable=_FsDCBXPortTable_Object((1,3,6,1,4,1,29601,2,22,3,1,2))
if mibBuilder.loadTexts:fsDCBXPortTable.setStatus(_A)
_FsDCBXPortEntry_Object=MibTableRow
fsDCBXPortEntry=_FsDCBXPortEntry_Object((1,3,6,1,4,1,29601,2,22,3,1,2,1))
fsDCBXPortEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:fsDCBXPortEntry.setStatus(_A)
_FsDCBXPortNumber_Type=InterfaceIndex
_FsDCBXPortNumber_Object=MibTableColumn
fsDCBXPortNumber=_FsDCBXPortNumber_Object((1,3,6,1,4,1,29601,2,22,3,1,2,1,1),_FsDCBXPortNumber_Type())
fsDCBXPortNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:fsDCBXPortNumber.setStatus(_A)
class _FsDCBXAdminStatus_Type(EnabledStatus):defaultValue=1
_FsDCBXAdminStatus_Type.__name__=_I
_FsDCBXAdminStatus_Object=MibTableColumn
fsDCBXAdminStatus=_FsDCBXAdminStatus_Object((1,3,6,1,4,1,29601,2,22,3,1,2,1,2),_FsDCBXAdminStatus_Type())
fsDCBXAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDCBXAdminStatus.setStatus(_A)
class _FsDCBXMode_Type(DcbxVersion):defaultValue=1
_FsDCBXMode_Type.__name__=_a
_FsDCBXMode_Object=MibTableColumn
fsDCBXMode=_FsDCBXMode_Object((1,3,6,1,4,1,29601,2,22,3,1,2,1,3),_FsDCBXMode_Type())
fsDCBXMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDCBXMode.setStatus(_A)
_FsETSObjects_ObjectIdentity=ObjectIdentity
fsETSObjects=_FsETSObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3,2))
_FsETSScalars_ObjectIdentity=ObjectIdentity
fsETSScalars=_FsETSScalars_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3,2,1))
class _FsETSSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_FsETSSystemControl_Type.__name__=_H
_FsETSSystemControl_Object=MibScalar
fsETSSystemControl=_FsETSSystemControl_Object((1,3,6,1,4,1,29601,2,22,3,2,1,1),_FsETSSystemControl_Type())
fsETSSystemControl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsETSSystemControl.setStatus(_A)
class _FsETSModuleStatus_Type(EnabledStatus):defaultValue=1
_FsETSModuleStatus_Type.__name__=_I
_FsETSModuleStatus_Object=MibScalar
fsETSModuleStatus=_FsETSModuleStatus_Object((1,3,6,1,4,1,29601,2,22,3,2,1,2),_FsETSModuleStatus_Type())
fsETSModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsETSModuleStatus.setStatus(_A)
class _FsETSClearCounters_Type(TruthValue):defaultValue=2
_FsETSClearCounters_Type.__name__=_G
_FsETSClearCounters_Object=MibScalar
fsETSClearCounters=_FsETSClearCounters_Object((1,3,6,1,4,1,29601,2,22,3,2,1,3),_FsETSClearCounters_Type())
fsETSClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:fsETSClearCounters.setStatus(_A)
class _FsETSGlobalEnableTrap_Type(Integer32):defaultValue=3
_FsETSGlobalEnableTrap_Type.__name__=_H
_FsETSGlobalEnableTrap_Object=MibScalar
fsETSGlobalEnableTrap=_FsETSGlobalEnableTrap_Object((1,3,6,1,4,1,29601,2,22,3,2,1,4),_FsETSGlobalEnableTrap_Type())
fsETSGlobalEnableTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:fsETSGlobalEnableTrap.setStatus(_A)
_FsETSGeneratedTrapCount_Type=Unsigned32
_FsETSGeneratedTrapCount_Object=MibScalar
fsETSGeneratedTrapCount=_FsETSGeneratedTrapCount_Object((1,3,6,1,4,1,29601,2,22,3,2,1,5),_FsETSGeneratedTrapCount_Type())
fsETSGeneratedTrapCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsETSGeneratedTrapCount.setStatus(_A)
_FsETSPortTable_Object=MibTable
fsETSPortTable=_FsETSPortTable_Object((1,3,6,1,4,1,29601,2,22,3,2,2))
if mibBuilder.loadTexts:fsETSPortTable.setStatus(_A)
_FsETSPortEntry_Object=MibTableRow
fsETSPortEntry=_FsETSPortEntry_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1))
fsETSPortEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:fsETSPortEntry.setStatus(_A)
_FsETSPortNumber_Type=InterfaceIndex
_FsETSPortNumber_Object=MibTableColumn
fsETSPortNumber=_FsETSPortNumber_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,1),_FsETSPortNumber_Type())
fsETSPortNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:fsETSPortNumber.setStatus(_A)
class _FsETSAdminMode_Type(DcbAdminMode):defaultValue=2
_FsETSAdminMode_Type.__name__=_N
_FsETSAdminMode_Object=MibTableColumn
fsETSAdminMode=_FsETSAdminMode_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,2),_FsETSAdminMode_Type())
fsETSAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsETSAdminMode.setStatus(_A)
_FsETSDcbxOperState_Type=DcbState
_FsETSDcbxOperState_Object=MibTableColumn
fsETSDcbxOperState=_FsETSDcbxOperState_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,3),_FsETSDcbxOperState_Type())
fsETSDcbxOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSDcbxOperState.setStatus(_A)
_FsETSDcbxStateMachine_Type=DcbStateMachineType
_FsETSDcbxStateMachine_Object=MibTableColumn
fsETSDcbxStateMachine=_FsETSDcbxStateMachine_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,4),_FsETSDcbxStateMachine_Type())
fsETSDcbxStateMachine.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSDcbxStateMachine.setStatus(_A)
class _FsETSClearTLVCounters_Type(TruthValue):defaultValue=2
_FsETSClearTLVCounters_Type.__name__=_G
_FsETSClearTLVCounters_Object=MibTableColumn
fsETSClearTLVCounters=_FsETSClearTLVCounters_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,5),_FsETSClearTLVCounters_Type())
fsETSClearTLVCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:fsETSClearTLVCounters.setStatus(_A)
_FsETSConfTxTLVCounter_Type=Counter32
_FsETSConfTxTLVCounter_Object=MibTableColumn
fsETSConfTxTLVCounter=_FsETSConfTxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,6),_FsETSConfTxTLVCounter_Type())
fsETSConfTxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSConfTxTLVCounter.setStatus(_A)
_FsETSConfRxTLVCounter_Type=Counter32
_FsETSConfRxTLVCounter_Object=MibTableColumn
fsETSConfRxTLVCounter=_FsETSConfRxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,7),_FsETSConfRxTLVCounter_Type())
fsETSConfRxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSConfRxTLVCounter.setStatus(_A)
_FsETSConfRxTLVErrors_Type=Counter32
_FsETSConfRxTLVErrors_Object=MibTableColumn
fsETSConfRxTLVErrors=_FsETSConfRxTLVErrors_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,8),_FsETSConfRxTLVErrors_Type())
fsETSConfRxTLVErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSConfRxTLVErrors.setStatus(_A)
_FsETSRecoTxTLVCounter_Type=Counter32
_FsETSRecoTxTLVCounter_Object=MibTableColumn
fsETSRecoTxTLVCounter=_FsETSRecoTxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,9),_FsETSRecoTxTLVCounter_Type())
fsETSRecoTxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSRecoTxTLVCounter.setStatus(_A)
_FsETSRecoRxTLVCounter_Type=Counter32
_FsETSRecoRxTLVCounter_Object=MibTableColumn
fsETSRecoRxTLVCounter=_FsETSRecoRxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,10),_FsETSRecoRxTLVCounter_Type())
fsETSRecoRxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSRecoRxTLVCounter.setStatus(_A)
_FsETSRecoRxTLVErrors_Type=Counter32
_FsETSRecoRxTLVErrors_Object=MibTableColumn
fsETSRecoRxTLVErrors=_FsETSRecoRxTLVErrors_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,11),_FsETSRecoRxTLVErrors_Type())
fsETSRecoRxTLVErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSRecoRxTLVErrors.setStatus(_A)
_FsETSTcSuppTxTLVCounter_Type=Counter32
_FsETSTcSuppTxTLVCounter_Object=MibTableColumn
fsETSTcSuppTxTLVCounter=_FsETSTcSuppTxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,12),_FsETSTcSuppTxTLVCounter_Type())
fsETSTcSuppTxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSTcSuppTxTLVCounter.setStatus(_A)
_FsETSTcSuppRxTLVCounter_Type=Counter32
_FsETSTcSuppRxTLVCounter_Object=MibTableColumn
fsETSTcSuppRxTLVCounter=_FsETSTcSuppRxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,13),_FsETSTcSuppRxTLVCounter_Type())
fsETSTcSuppRxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSTcSuppRxTLVCounter.setStatus(_A)
_FsETSTcSuppRxTLVErrors_Type=Counter32
_FsETSTcSuppRxTLVErrors_Object=MibTableColumn
fsETSTcSuppRxTLVErrors=_FsETSTcSuppRxTLVErrors_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,14),_FsETSTcSuppRxTLVErrors_Type())
fsETSTcSuppRxTLVErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSTcSuppRxTLVErrors.setStatus(_A)
_FsETSRowStatus_Type=RowStatus
_FsETSRowStatus_Object=MibTableColumn
fsETSRowStatus=_FsETSRowStatus_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,15),_FsETSRowStatus_Type())
fsETSRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsETSRowStatus.setStatus(_A)
_FsETSSyncd_Type=TruthValue
_FsETSSyncd_Object=MibTableColumn
fsETSSyncd=_FsETSSyncd_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,16),_FsETSSyncd_Type())
fsETSSyncd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSSyncd.setStatus(_A)
_FsETSError_Type=TruthValue
_FsETSError_Object=MibTableColumn
fsETSError=_FsETSError_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,17),_FsETSError_Type())
fsETSError.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSError.setStatus(_A)
_FsETSDcbxStatus_Type=DcbxStatus
_FsETSDcbxStatus_Object=MibTableColumn
fsETSDcbxStatus=_FsETSDcbxStatus_Object((1,3,6,1,4,1,29601,2,22,3,2,2,1,18),_FsETSDcbxStatus_Type())
fsETSDcbxStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsETSDcbxStatus.setStatus(_A)
_FsPFCObjects_ObjectIdentity=ObjectIdentity
fsPFCObjects=_FsPFCObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3,3))
_FsPFCScalars_ObjectIdentity=ObjectIdentity
fsPFCScalars=_FsPFCScalars_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3,3,1))
class _FsPFCSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_FsPFCSystemControl_Type.__name__=_H
_FsPFCSystemControl_Object=MibScalar
fsPFCSystemControl=_FsPFCSystemControl_Object((1,3,6,1,4,1,29601,2,22,3,3,1,1),_FsPFCSystemControl_Type())
fsPFCSystemControl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPFCSystemControl.setStatus(_A)
class _FsPFCModuleStatus_Type(EnabledStatus):defaultValue=1
_FsPFCModuleStatus_Type.__name__=_I
_FsPFCModuleStatus_Object=MibScalar
fsPFCModuleStatus=_FsPFCModuleStatus_Object((1,3,6,1,4,1,29601,2,22,3,3,1,2),_FsPFCModuleStatus_Type())
fsPFCModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPFCModuleStatus.setStatus(_A)
class _FsPFCClearCounters_Type(TruthValue):defaultValue=2
_FsPFCClearCounters_Type.__name__=_G
_FsPFCClearCounters_Object=MibScalar
fsPFCClearCounters=_FsPFCClearCounters_Object((1,3,6,1,4,1,29601,2,22,3,3,1,3),_FsPFCClearCounters_Type())
fsPFCClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPFCClearCounters.setStatus(_A)
class _FsPFCGlobalEnableTrap_Type(Integer32):defaultValue=3
_FsPFCGlobalEnableTrap_Type.__name__=_H
_FsPFCGlobalEnableTrap_Object=MibScalar
fsPFCGlobalEnableTrap=_FsPFCGlobalEnableTrap_Object((1,3,6,1,4,1,29601,2,22,3,3,1,4),_FsPFCGlobalEnableTrap_Type())
fsPFCGlobalEnableTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPFCGlobalEnableTrap.setStatus(_A)
_FsPFCGeneratedTrapCount_Type=Unsigned32
_FsPFCGeneratedTrapCount_Object=MibScalar
fsPFCGeneratedTrapCount=_FsPFCGeneratedTrapCount_Object((1,3,6,1,4,1,29601,2,22,3,3,1,5),_FsPFCGeneratedTrapCount_Type())
fsPFCGeneratedTrapCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPFCGeneratedTrapCount.setStatus(_A)
_FsPFCPortTable_Object=MibTable
fsPFCPortTable=_FsPFCPortTable_Object((1,3,6,1,4,1,29601,2,22,3,3,2))
if mibBuilder.loadTexts:fsPFCPortTable.setStatus(_A)
_FsPFCPortEntry_Object=MibTableRow
fsPFCPortEntry=_FsPFCPortEntry_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1))
fsPFCPortEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:fsPFCPortEntry.setStatus(_A)
_FsPFCPortNumber_Type=InterfaceIndex
_FsPFCPortNumber_Object=MibTableColumn
fsPFCPortNumber=_FsPFCPortNumber_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,1),_FsPFCPortNumber_Type())
fsPFCPortNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:fsPFCPortNumber.setStatus(_A)
class _FsPFCAdminMode_Type(DcbAdminMode):defaultValue=2
_FsPFCAdminMode_Type.__name__=_N
_FsPFCAdminMode_Object=MibTableColumn
fsPFCAdminMode=_FsPFCAdminMode_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,2),_FsPFCAdminMode_Type())
fsPFCAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPFCAdminMode.setStatus(_A)
_FsPFCDcbxOperState_Type=DcbState
_FsPFCDcbxOperState_Object=MibTableColumn
fsPFCDcbxOperState=_FsPFCDcbxOperState_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,3),_FsPFCDcbxOperState_Type())
fsPFCDcbxOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCDcbxOperState.setStatus(_A)
_FsPFCDcbxStateMachine_Type=DcbStateMachineType
_FsPFCDcbxStateMachine_Object=MibTableColumn
fsPFCDcbxStateMachine=_FsPFCDcbxStateMachine_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,4),_FsPFCDcbxStateMachine_Type())
fsPFCDcbxStateMachine.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCDcbxStateMachine.setStatus(_A)
class _FsPFCClearTLVCounters_Type(TruthValue):defaultValue=2
_FsPFCClearTLVCounters_Type.__name__=_G
_FsPFCClearTLVCounters_Object=MibTableColumn
fsPFCClearTLVCounters=_FsPFCClearTLVCounters_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,5),_FsPFCClearTLVCounters_Type())
fsPFCClearTLVCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPFCClearTLVCounters.setStatus(_A)
_FsPFCTxTLVCounter_Type=Counter32
_FsPFCTxTLVCounter_Object=MibTableColumn
fsPFCTxTLVCounter=_FsPFCTxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,6),_FsPFCTxTLVCounter_Type())
fsPFCTxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCTxTLVCounter.setStatus(_A)
_FsPFCRxTLVCounter_Type=Counter32
_FsPFCRxTLVCounter_Object=MibTableColumn
fsPFCRxTLVCounter=_FsPFCRxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,7),_FsPFCRxTLVCounter_Type())
fsPFCRxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCRxTLVCounter.setStatus(_A)
_FsPFCRxTLVErrors_Type=Counter32
_FsPFCRxTLVErrors_Object=MibTableColumn
fsPFCRxTLVErrors=_FsPFCRxTLVErrors_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,8),_FsPFCRxTLVErrors_Type())
fsPFCRxTLVErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCRxTLVErrors.setStatus(_A)
_FsPFCRowStatus_Type=RowStatus
_FsPFCRowStatus_Object=MibTableColumn
fsPFCRowStatus=_FsPFCRowStatus_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,9),_FsPFCRowStatus_Type())
fsPFCRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPFCRowStatus.setStatus(_A)
_FsPFCSyncd_Type=TruthValue
_FsPFCSyncd_Object=MibTableColumn
fsPFCSyncd=_FsPFCSyncd_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,10),_FsPFCSyncd_Type())
fsPFCSyncd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCSyncd.setStatus(_A)
_FsPFCError_Type=TruthValue
_FsPFCError_Object=MibTableColumn
fsPFCError=_FsPFCError_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,11),_FsPFCError_Type())
fsPFCError.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCError.setStatus(_A)
_FsPFCDcbxStatus_Type=DcbxStatus
_FsPFCDcbxStatus_Object=MibTableColumn
fsPFCDcbxStatus=_FsPFCDcbxStatus_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,12),_FsPFCDcbxStatus_Type())
fsPFCDcbxStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCDcbxStatus.setStatus(_A)
_FsPFCRxPauseFrameCounter_Type=Counter32
_FsPFCRxPauseFrameCounter_Object=MibTableColumn
fsPFCRxPauseFrameCounter=_FsPFCRxPauseFrameCounter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,13),_FsPFCRxPauseFrameCounter_Type())
fsPFCRxPauseFrameCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCRxPauseFrameCounter.setStatus(_A)
_FsPFCTxPauseFrameCounter_Type=Counter32
_FsPFCTxPauseFrameCounter_Object=MibTableColumn
fsPFCTxPauseFrameCounter=_FsPFCTxPauseFrameCounter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,14),_FsPFCTxPauseFrameCounter_Type())
fsPFCTxPauseFrameCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCTxPauseFrameCounter.setStatus(_A)
_FsPFCRxPauseFrameP0Counter_Type=Counter32
_FsPFCRxPauseFrameP0Counter_Object=MibTableColumn
fsPFCRxPauseFrameP0Counter=_FsPFCRxPauseFrameP0Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,15),_FsPFCRxPauseFrameP0Counter_Type())
fsPFCRxPauseFrameP0Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCRxPauseFrameP0Counter.setStatus(_A)
_FsPFCRxPauseFrameP1Counter_Type=Counter32
_FsPFCRxPauseFrameP1Counter_Object=MibTableColumn
fsPFCRxPauseFrameP1Counter=_FsPFCRxPauseFrameP1Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,16),_FsPFCRxPauseFrameP1Counter_Type())
fsPFCRxPauseFrameP1Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCRxPauseFrameP1Counter.setStatus(_A)
_FsPFCRxPauseFrameP2Counter_Type=Counter32
_FsPFCRxPauseFrameP2Counter_Object=MibTableColumn
fsPFCRxPauseFrameP2Counter=_FsPFCRxPauseFrameP2Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,17),_FsPFCRxPauseFrameP2Counter_Type())
fsPFCRxPauseFrameP2Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCRxPauseFrameP2Counter.setStatus(_A)
_FsPFCRxPauseFrameP3Counter_Type=Counter32
_FsPFCRxPauseFrameP3Counter_Object=MibTableColumn
fsPFCRxPauseFrameP3Counter=_FsPFCRxPauseFrameP3Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,18),_FsPFCRxPauseFrameP3Counter_Type())
fsPFCRxPauseFrameP3Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCRxPauseFrameP3Counter.setStatus(_A)
_FsPFCRxPauseFrameP4Counter_Type=Counter32
_FsPFCRxPauseFrameP4Counter_Object=MibTableColumn
fsPFCRxPauseFrameP4Counter=_FsPFCRxPauseFrameP4Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,19),_FsPFCRxPauseFrameP4Counter_Type())
fsPFCRxPauseFrameP4Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCRxPauseFrameP4Counter.setStatus(_A)
_FsPFCRxPauseFrameP5Counter_Type=Counter32
_FsPFCRxPauseFrameP5Counter_Object=MibTableColumn
fsPFCRxPauseFrameP5Counter=_FsPFCRxPauseFrameP5Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,20),_FsPFCRxPauseFrameP5Counter_Type())
fsPFCRxPauseFrameP5Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCRxPauseFrameP5Counter.setStatus(_A)
_FsPFCRxPauseFrameP6Counter_Type=Counter32
_FsPFCRxPauseFrameP6Counter_Object=MibTableColumn
fsPFCRxPauseFrameP6Counter=_FsPFCRxPauseFrameP6Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,21),_FsPFCRxPauseFrameP6Counter_Type())
fsPFCRxPauseFrameP6Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCRxPauseFrameP6Counter.setStatus(_A)
_FsPFCRxPauseFrameP7Counter_Type=Counter32
_FsPFCRxPauseFrameP7Counter_Object=MibTableColumn
fsPFCRxPauseFrameP7Counter=_FsPFCRxPauseFrameP7Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,22),_FsPFCRxPauseFrameP7Counter_Type())
fsPFCRxPauseFrameP7Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCRxPauseFrameP7Counter.setStatus(_A)
_FsPFCTxPauseFrameP0Counter_Type=Counter32
_FsPFCTxPauseFrameP0Counter_Object=MibTableColumn
fsPFCTxPauseFrameP0Counter=_FsPFCTxPauseFrameP0Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,23),_FsPFCTxPauseFrameP0Counter_Type())
fsPFCTxPauseFrameP0Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCTxPauseFrameP0Counter.setStatus(_A)
_FsPFCTxPauseFrameP1Counter_Type=Counter32
_FsPFCTxPauseFrameP1Counter_Object=MibTableColumn
fsPFCTxPauseFrameP1Counter=_FsPFCTxPauseFrameP1Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,24),_FsPFCTxPauseFrameP1Counter_Type())
fsPFCTxPauseFrameP1Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCTxPauseFrameP1Counter.setStatus(_A)
_FsPFCTxPauseFrameP2Counter_Type=Counter32
_FsPFCTxPauseFrameP2Counter_Object=MibTableColumn
fsPFCTxPauseFrameP2Counter=_FsPFCTxPauseFrameP2Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,25),_FsPFCTxPauseFrameP2Counter_Type())
fsPFCTxPauseFrameP2Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCTxPauseFrameP2Counter.setStatus(_A)
_FsPFCTxPauseFrameP3Counter_Type=Counter32
_FsPFCTxPauseFrameP3Counter_Object=MibTableColumn
fsPFCTxPauseFrameP3Counter=_FsPFCTxPauseFrameP3Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,26),_FsPFCTxPauseFrameP3Counter_Type())
fsPFCTxPauseFrameP3Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCTxPauseFrameP3Counter.setStatus(_A)
_FsPFCTxPauseFrameP4Counter_Type=Counter32
_FsPFCTxPauseFrameP4Counter_Object=MibTableColumn
fsPFCTxPauseFrameP4Counter=_FsPFCTxPauseFrameP4Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,27),_FsPFCTxPauseFrameP4Counter_Type())
fsPFCTxPauseFrameP4Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCTxPauseFrameP4Counter.setStatus(_A)
_FsPFCTxPauseFrameP5Counter_Type=Counter32
_FsPFCTxPauseFrameP5Counter_Object=MibTableColumn
fsPFCTxPauseFrameP5Counter=_FsPFCTxPauseFrameP5Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,28),_FsPFCTxPauseFrameP5Counter_Type())
fsPFCTxPauseFrameP5Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCTxPauseFrameP5Counter.setStatus(_A)
_FsPFCTxPauseFrameP6Counter_Type=Counter32
_FsPFCTxPauseFrameP6Counter_Object=MibTableColumn
fsPFCTxPauseFrameP6Counter=_FsPFCTxPauseFrameP6Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,29),_FsPFCTxPauseFrameP6Counter_Type())
fsPFCTxPauseFrameP6Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCTxPauseFrameP6Counter.setStatus(_A)
_FsPFCTxPauseFrameP7Counter_Type=Counter32
_FsPFCTxPauseFrameP7Counter_Object=MibTableColumn
fsPFCTxPauseFrameP7Counter=_FsPFCTxPauseFrameP7Counter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,30),_FsPFCTxPauseFrameP7Counter_Type())
fsPFCTxPauseFrameP7Counter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCTxPauseFrameP7Counter.setStatus(_A)
_FsPFCDataFrameDiscardCounter_Type=Counter32
_FsPFCDataFrameDiscardCounter_Object=MibTableColumn
fsPFCDataFrameDiscardCounter=_FsPFCDataFrameDiscardCounter_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,31),_FsPFCDataFrameDiscardCounter_Type())
fsPFCDataFrameDiscardCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPFCDataFrameDiscardCounter.setStatus(_A)
class _FsPFCClearPauseFrameCounters_Type(TruthValue):defaultValue=2
_FsPFCClearPauseFrameCounters_Type.__name__=_G
_FsPFCClearPauseFrameCounters_Object=MibTableColumn
fsPFCClearPauseFrameCounters=_FsPFCClearPauseFrameCounters_Object((1,3,6,1,4,1,29601,2,22,3,3,2,1,32),_FsPFCClearPauseFrameCounters_Type())
fsPFCClearPauseFrameCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPFCClearPauseFrameCounters.setStatus(_A)
_FsAppPriObjects_ObjectIdentity=ObjectIdentity
fsAppPriObjects=_FsAppPriObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3,4))
_FsAppPriScalars_ObjectIdentity=ObjectIdentity
fsAppPriScalars=_FsAppPriScalars_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3,4,1))
class _FsAppPriSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_FsAppPriSystemControl_Type.__name__=_H
_FsAppPriSystemControl_Object=MibScalar
fsAppPriSystemControl=_FsAppPriSystemControl_Object((1,3,6,1,4,1,29601,2,22,3,4,1,1),_FsAppPriSystemControl_Type())
fsAppPriSystemControl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAppPriSystemControl.setStatus(_A)
class _FsAppPriModuleStatus_Type(EnabledStatus):defaultValue=1
_FsAppPriModuleStatus_Type.__name__=_I
_FsAppPriModuleStatus_Object=MibScalar
fsAppPriModuleStatus=_FsAppPriModuleStatus_Object((1,3,6,1,4,1,29601,2,22,3,4,1,2),_FsAppPriModuleStatus_Type())
fsAppPriModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAppPriModuleStatus.setStatus(_A)
class _FsAppPriClearCounters_Type(TruthValue):defaultValue=2
_FsAppPriClearCounters_Type.__name__=_G
_FsAppPriClearCounters_Object=MibScalar
fsAppPriClearCounters=_FsAppPriClearCounters_Object((1,3,6,1,4,1,29601,2,22,3,4,1,3),_FsAppPriClearCounters_Type())
fsAppPriClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAppPriClearCounters.setStatus(_A)
class _FsAppPriGlobalEnableTrap_Type(Integer32):defaultValue=3
_FsAppPriGlobalEnableTrap_Type.__name__=_H
_FsAppPriGlobalEnableTrap_Object=MibScalar
fsAppPriGlobalEnableTrap=_FsAppPriGlobalEnableTrap_Object((1,3,6,1,4,1,29601,2,22,3,4,1,4),_FsAppPriGlobalEnableTrap_Type())
fsAppPriGlobalEnableTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAppPriGlobalEnableTrap.setStatus(_A)
_FsAppPriGeneratedTrapCount_Type=Unsigned32
_FsAppPriGeneratedTrapCount_Object=MibScalar
fsAppPriGeneratedTrapCount=_FsAppPriGeneratedTrapCount_Object((1,3,6,1,4,1,29601,2,22,3,4,1,5),_FsAppPriGeneratedTrapCount_Type())
fsAppPriGeneratedTrapCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAppPriGeneratedTrapCount.setStatus(_A)
_FsAppPriPortTable_Object=MibTable
fsAppPriPortTable=_FsAppPriPortTable_Object((1,3,6,1,4,1,29601,2,22,3,4,2))
if mibBuilder.loadTexts:fsAppPriPortTable.setStatus(_A)
_FsAppPriPortEntry_Object=MibTableRow
fsAppPriPortEntry=_FsAppPriPortEntry_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1))
fsAppPriPortEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:fsAppPriPortEntry.setStatus(_A)
_FsAppPriPortNumber_Type=InterfaceIndex
_FsAppPriPortNumber_Object=MibTableColumn
fsAppPriPortNumber=_FsAppPriPortNumber_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,1),_FsAppPriPortNumber_Type())
fsAppPriPortNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:fsAppPriPortNumber.setStatus(_A)
class _FsAppPriAdminMode_Type(DcbAdminMode):defaultValue=2
_FsAppPriAdminMode_Type.__name__=_N
_FsAppPriAdminMode_Object=MibTableColumn
fsAppPriAdminMode=_FsAppPriAdminMode_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,2),_FsAppPriAdminMode_Type())
fsAppPriAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAppPriAdminMode.setStatus(_A)
_FsAppPriDcbxOperState_Type=DcbState
_FsAppPriDcbxOperState_Object=MibTableColumn
fsAppPriDcbxOperState=_FsAppPriDcbxOperState_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,3),_FsAppPriDcbxOperState_Type())
fsAppPriDcbxOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsAppPriDcbxOperState.setStatus(_A)
_FsAppPriDcbxStateMachine_Type=DcbStateMachineType
_FsAppPriDcbxStateMachine_Object=MibTableColumn
fsAppPriDcbxStateMachine=_FsAppPriDcbxStateMachine_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,4),_FsAppPriDcbxStateMachine_Type())
fsAppPriDcbxStateMachine.setMaxAccess(_B)
if mibBuilder.loadTexts:fsAppPriDcbxStateMachine.setStatus(_A)
class _FsAppPriClearTLVCounters_Type(TruthValue):defaultValue=2
_FsAppPriClearTLVCounters_Type.__name__=_G
_FsAppPriClearTLVCounters_Object=MibTableColumn
fsAppPriClearTLVCounters=_FsAppPriClearTLVCounters_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,5),_FsAppPriClearTLVCounters_Type())
fsAppPriClearTLVCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAppPriClearTLVCounters.setStatus(_A)
_FsAppPriTxTLVCounter_Type=Counter32
_FsAppPriTxTLVCounter_Object=MibTableColumn
fsAppPriTxTLVCounter=_FsAppPriTxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,6),_FsAppPriTxTLVCounter_Type())
fsAppPriTxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsAppPriTxTLVCounter.setStatus(_A)
_FsAppPriRxTLVCounter_Type=Counter32
_FsAppPriRxTLVCounter_Object=MibTableColumn
fsAppPriRxTLVCounter=_FsAppPriRxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,7),_FsAppPriRxTLVCounter_Type())
fsAppPriRxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsAppPriRxTLVCounter.setStatus(_A)
_FsAppPriRxTLVErrors_Type=Counter32
_FsAppPriRxTLVErrors_Object=MibTableColumn
fsAppPriRxTLVErrors=_FsAppPriRxTLVErrors_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,8),_FsAppPriRxTLVErrors_Type())
fsAppPriRxTLVErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fsAppPriRxTLVErrors.setStatus(_A)
_FsAppPriAppProtocols_Type=Unsigned32
_FsAppPriAppProtocols_Object=MibTableColumn
fsAppPriAppProtocols=_FsAppPriAppProtocols_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,9),_FsAppPriAppProtocols_Type())
fsAppPriAppProtocols.setMaxAccess(_B)
if mibBuilder.loadTexts:fsAppPriAppProtocols.setStatus(_A)
_FsAppPriRowStatus_Type=RowStatus
_FsAppPriRowStatus_Object=MibTableColumn
fsAppPriRowStatus=_FsAppPriRowStatus_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,10),_FsAppPriRowStatus_Type())
fsAppPriRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAppPriRowStatus.setStatus(_A)
_FsAppPriSyncd_Type=TruthValue
_FsAppPriSyncd_Object=MibTableColumn
fsAppPriSyncd=_FsAppPriSyncd_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,11),_FsAppPriSyncd_Type())
fsAppPriSyncd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsAppPriSyncd.setStatus(_A)
_FsAppPriError_Type=TruthValue
_FsAppPriError_Object=MibTableColumn
fsAppPriError=_FsAppPriError_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,12),_FsAppPriError_Type())
fsAppPriError.setMaxAccess(_B)
if mibBuilder.loadTexts:fsAppPriError.setStatus(_A)
_FsAppPriDcbxStatus_Type=DcbxStatus
_FsAppPriDcbxStatus_Object=MibTableColumn
fsAppPriDcbxStatus=_FsAppPriDcbxStatus_Object((1,3,6,1,4,1,29601,2,22,3,4,2,1,13),_FsAppPriDcbxStatus_Type())
fsAppPriDcbxStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsAppPriDcbxStatus.setStatus(_A)
_FsAppPriXAppTable_Object=MibTable
fsAppPriXAppTable=_FsAppPriXAppTable_Object((1,3,6,1,4,1,29601,2,22,3,4,3))
if mibBuilder.loadTexts:fsAppPriXAppTable.setStatus(_A)
_FsAppPriXAppEntry_Object=MibTableRow
fsAppPriXAppEntry=_FsAppPriXAppEntry_Object((1,3,6,1,4,1,29601,2,22,3,4,3,1))
if mibBuilder.loadTexts:fsAppPriXAppEntry.setStatus(_A)
_FsAppPriXAppRowStatus_Type=RowStatus
_FsAppPriXAppRowStatus_Object=MibTableColumn
fsAppPriXAppRowStatus=_FsAppPriXAppRowStatus_Object((1,3,6,1,4,1,29601,2,22,3,4,3,1,1),_FsAppPriXAppRowStatus_Type())
fsAppPriXAppRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAppPriXAppRowStatus.setStatus(_A)
_FslldpXdot1dcbxLocApplicationPriorityBasicTable_Object=MibTable
fslldpXdot1dcbxLocApplicationPriorityBasicTable=_FslldpXdot1dcbxLocApplicationPriorityBasicTable_Object((1,3,6,1,4,1,29601,2,22,3,4,4))
if mibBuilder.loadTexts:fslldpXdot1dcbxLocApplicationPriorityBasicTable.setStatus(_A)
_FslldpXdot1dcbxLocApplicationPriorityBasicEntry_Object=MibTableRow
fslldpXdot1dcbxLocApplicationPriorityBasicEntry=_FslldpXdot1dcbxLocApplicationPriorityBasicEntry_Object((1,3,6,1,4,1,29601,2,22,3,4,4,1))
fslldpXdot1dcbxLocApplicationPriorityBasicEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:fslldpXdot1dcbxLocApplicationPriorityBasicEntry.setStatus(_A)
_FslldpXdot1dcbxLocApplicationPriorityWilling_Type=TruthValue
_FslldpXdot1dcbxLocApplicationPriorityWilling_Object=MibTableColumn
fslldpXdot1dcbxLocApplicationPriorityWilling=_FslldpXdot1dcbxLocApplicationPriorityWilling_Object((1,3,6,1,4,1,29601,2,22,3,4,4,1,1),_FslldpXdot1dcbxLocApplicationPriorityWilling_Type())
fslldpXdot1dcbxLocApplicationPriorityWilling.setMaxAccess(_B)
if mibBuilder.loadTexts:fslldpXdot1dcbxLocApplicationPriorityWilling.setStatus(_A)
_FslldpXdot1dcbxAdminApplicationPriorityBasicTable_Object=MibTable
fslldpXdot1dcbxAdminApplicationPriorityBasicTable=_FslldpXdot1dcbxAdminApplicationPriorityBasicTable_Object((1,3,6,1,4,1,29601,2,22,3,4,5))
if mibBuilder.loadTexts:fslldpXdot1dcbxAdminApplicationPriorityBasicTable.setStatus(_A)
_FslldpXdot1dcbxAdminApplicationPriorityBasicEntry_Object=MibTableRow
fslldpXdot1dcbxAdminApplicationPriorityBasicEntry=_FslldpXdot1dcbxAdminApplicationPriorityBasicEntry_Object((1,3,6,1,4,1,29601,2,22,3,4,5,1))
fslldpXdot1dcbxAdminApplicationPriorityBasicEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:fslldpXdot1dcbxAdminApplicationPriorityBasicEntry.setStatus(_A)
class _FslldpXdot1dcbxAdminApplicationPriorityWilling_Type(TruthValue):defaultValue=2
_FslldpXdot1dcbxAdminApplicationPriorityWilling_Type.__name__=_G
_FslldpXdot1dcbxAdminApplicationPriorityWilling_Object=MibTableColumn
fslldpXdot1dcbxAdminApplicationPriorityWilling=_FslldpXdot1dcbxAdminApplicationPriorityWilling_Object((1,3,6,1,4,1,29601,2,22,3,4,5,1,1),_FslldpXdot1dcbxAdminApplicationPriorityWilling_Type())
fslldpXdot1dcbxAdminApplicationPriorityWilling.setMaxAccess(_D)
if mibBuilder.loadTexts:fslldpXdot1dcbxAdminApplicationPriorityWilling.setStatus(_A)
_FslldpXdot1dcbxRemApplicationPriorityBasicTable_Object=MibTable
fslldpXdot1dcbxRemApplicationPriorityBasicTable=_FslldpXdot1dcbxRemApplicationPriorityBasicTable_Object((1,3,6,1,4,1,29601,2,22,3,4,6))
if mibBuilder.loadTexts:fslldpXdot1dcbxRemApplicationPriorityBasicTable.setStatus(_A)
_FslldpXdot1dcbxRemApplicationPriorityBasicEntry_Object=MibTableRow
fslldpXdot1dcbxRemApplicationPriorityBasicEntry=_FslldpXdot1dcbxRemApplicationPriorityBasicEntry_Object((1,3,6,1,4,1,29601,2,22,3,4,6,1))
fslldpXdot1dcbxRemApplicationPriorityBasicEntry.setIndexNames((0,_F,_S),(0,_F,_R),(0,_F,_Q),(0,_F,_P))
if mibBuilder.loadTexts:fslldpXdot1dcbxRemApplicationPriorityBasicEntry.setStatus(_A)
_FslldpXdot1dcbxRemApplicationPriorityWilling_Type=TruthValue
_FslldpXdot1dcbxRemApplicationPriorityWilling_Object=MibTableColumn
fslldpXdot1dcbxRemApplicationPriorityWilling=_FslldpXdot1dcbxRemApplicationPriorityWilling_Object((1,3,6,1,4,1,29601,2,22,3,4,6,1,1),_FslldpXdot1dcbxRemApplicationPriorityWilling_Type())
fslldpXdot1dcbxRemApplicationPriorityWilling.setMaxAccess(_B)
if mibBuilder.loadTexts:fslldpXdot1dcbxRemApplicationPriorityWilling.setStatus(_A)
_FsTCSupportedObjects_ObjectIdentity=ObjectIdentity
fsTCSupportedObjects=_FsTCSupportedObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3,5))
_FslldpXdot1dcbxConfigTCSupportedTable_Object=MibTable
fslldpXdot1dcbxConfigTCSupportedTable=_FslldpXdot1dcbxConfigTCSupportedTable_Object((1,3,6,1,4,1,29601,2,22,3,5,1))
if mibBuilder.loadTexts:fslldpXdot1dcbxConfigTCSupportedTable.setStatus(_A)
_FslldpXdot1dcbxConfigTCSupportedEntry_Object=MibTableRow
fslldpXdot1dcbxConfigTCSupportedEntry=_FslldpXdot1dcbxConfigTCSupportedEntry_Object((1,3,6,1,4,1,29601,2,22,3,5,1,1))
if mibBuilder.loadTexts:fslldpXdot1dcbxConfigTCSupportedEntry.setStatus(_A)
class _FslldpXdot1dcbxConfigTCSupportedTxEnable_Type(TruthValue):defaultValue=2
_FslldpXdot1dcbxConfigTCSupportedTxEnable_Type.__name__=_G
_FslldpXdot1dcbxConfigTCSupportedTxEnable_Object=MibTableColumn
fslldpXdot1dcbxConfigTCSupportedTxEnable=_FslldpXdot1dcbxConfigTCSupportedTxEnable_Object((1,3,6,1,4,1,29601,2,22,3,5,1,1,1),_FslldpXdot1dcbxConfigTCSupportedTxEnable_Type())
fslldpXdot1dcbxConfigTCSupportedTxEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fslldpXdot1dcbxConfigTCSupportedTxEnable.setStatus(_A)
_FslldpXdot1dcbxLocTCSupportedTable_Object=MibTable
fslldpXdot1dcbxLocTCSupportedTable=_FslldpXdot1dcbxLocTCSupportedTable_Object((1,3,6,1,4,1,29601,2,22,3,5,2))
if mibBuilder.loadTexts:fslldpXdot1dcbxLocTCSupportedTable.setStatus(_A)
_FslldpXdot1dcbxLocTCSupportedEntry_Object=MibTableRow
fslldpXdot1dcbxLocTCSupportedEntry=_FslldpXdot1dcbxLocTCSupportedEntry_Object((1,3,6,1,4,1,29601,2,22,3,5,2,1))
fslldpXdot1dcbxLocTCSupportedEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:fslldpXdot1dcbxLocTCSupportedEntry.setStatus(_A)
_FslldpXdot1dcbxLocTCSupported_Type=FsLldpXdot1dcbxTCSupportedCapacity
_FslldpXdot1dcbxLocTCSupported_Object=MibTableColumn
fslldpXdot1dcbxLocTCSupported=_FslldpXdot1dcbxLocTCSupported_Object((1,3,6,1,4,1,29601,2,22,3,5,2,1,1),_FslldpXdot1dcbxLocTCSupported_Type())
fslldpXdot1dcbxLocTCSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:fslldpXdot1dcbxLocTCSupported.setStatus(_A)
_FslldpXdot1dcbxRemTCSupportedTable_Object=MibTable
fslldpXdot1dcbxRemTCSupportedTable=_FslldpXdot1dcbxRemTCSupportedTable_Object((1,3,6,1,4,1,29601,2,22,3,5,3))
if mibBuilder.loadTexts:fslldpXdot1dcbxRemTCSupportedTable.setStatus(_A)
_FslldpXdot1dcbxRemTCSupportedEntry_Object=MibTableRow
fslldpXdot1dcbxRemTCSupportedEntry=_FslldpXdot1dcbxRemTCSupportedEntry_Object((1,3,6,1,4,1,29601,2,22,3,5,3,1))
fslldpXdot1dcbxRemTCSupportedEntry.setIndexNames((0,_F,_S),(0,_F,_R),(0,_F,_Q),(0,_F,_P))
if mibBuilder.loadTexts:fslldpXdot1dcbxRemTCSupportedEntry.setStatus(_A)
_FslldpXdot1dcbxRemTCSupported_Type=FsLldpXdot1dcbxTCSupportedCapacity
_FslldpXdot1dcbxRemTCSupported_Object=MibTableColumn
fslldpXdot1dcbxRemTCSupported=_FslldpXdot1dcbxRemTCSupported_Object((1,3,6,1,4,1,29601,2,22,3,5,3,1,1),_FslldpXdot1dcbxRemTCSupported_Type())
fslldpXdot1dcbxRemTCSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:fslldpXdot1dcbxRemTCSupported.setStatus(_A)
_FslldpXdot1dcbxAdminTCSupportedTable_Object=MibTable
fslldpXdot1dcbxAdminTCSupportedTable=_FslldpXdot1dcbxAdminTCSupportedTable_Object((1,3,6,1,4,1,29601,2,22,3,5,4))
if mibBuilder.loadTexts:fslldpXdot1dcbxAdminTCSupportedTable.setStatus(_A)
_FslldpXdot1dcbxAdminTCSupportedEntry_Object=MibTableRow
fslldpXdot1dcbxAdminTCSupportedEntry=_FslldpXdot1dcbxAdminTCSupportedEntry_Object((1,3,6,1,4,1,29601,2,22,3,5,4,1))
fslldpXdot1dcbxAdminTCSupportedEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:fslldpXdot1dcbxAdminTCSupportedEntry.setStatus(_A)
_FslldpXdot1dcbxAdminTCSupported_Type=FsLldpXdot1dcbxTCSupportedCapacity
_FslldpXdot1dcbxAdminTCSupported_Object=MibTableColumn
fslldpXdot1dcbxAdminTCSupported=_FslldpXdot1dcbxAdminTCSupported_Object((1,3,6,1,4,1,29601,2,22,3,5,4,1,1),_FslldpXdot1dcbxAdminTCSupported_Type())
fslldpXdot1dcbxAdminTCSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:fslldpXdot1dcbxAdminTCSupported.setStatus(_A)
_FsDcbxCEEObjects_ObjectIdentity=ObjectIdentity
fsDcbxCEEObjects=_FsDcbxCEEObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3,6))
_FsDcbxCEEScalars_ObjectIdentity=ObjectIdentity
fsDcbxCEEScalars=_FsDcbxCEEScalars_ObjectIdentity((1,3,6,1,4,1,29601,2,22,3,6,1))
class _FsDcbxCEEGlobalEnableTrap_Type(Integer32):defaultValue=0
_FsDcbxCEEGlobalEnableTrap_Type.__name__=_H
_FsDcbxCEEGlobalEnableTrap_Object=MibScalar
fsDcbxCEEGlobalEnableTrap=_FsDcbxCEEGlobalEnableTrap_Object((1,3,6,1,4,1,29601,2,22,3,6,1,1),_FsDcbxCEEGlobalEnableTrap_Type())
fsDcbxCEEGlobalEnableTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDcbxCEEGlobalEnableTrap.setStatus(_A)
_FsDcbxCEEGeneratedTrapCount_Type=Unsigned32
_FsDcbxCEEGeneratedTrapCount_Object=MibScalar
fsDcbxCEEGeneratedTrapCount=_FsDcbxCEEGeneratedTrapCount_Object((1,3,6,1,4,1,29601,2,22,3,6,1,2),_FsDcbxCEEGeneratedTrapCount_Type())
fsDcbxCEEGeneratedTrapCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbxCEEGeneratedTrapCount.setStatus(_A)
class _FsDcbxCEEClearCounters_Type(TruthValue):defaultValue=2
_FsDcbxCEEClearCounters_Type.__name__=_G
_FsDcbxCEEClearCounters_Object=MibScalar
fsDcbxCEEClearCounters=_FsDcbxCEEClearCounters_Object((1,3,6,1,4,1,29601,2,22,3,6,1,3),_FsDcbxCEEClearCounters_Type())
fsDcbxCEEClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDcbxCEEClearCounters.setStatus(_A)
_FsDcbxCEECtrlTable_Object=MibTable
fsDcbxCEECtrlTable=_FsDcbxCEECtrlTable_Object((1,3,6,1,4,1,29601,2,22,3,6,2))
if mibBuilder.loadTexts:fsDcbxCEECtrlTable.setStatus(_A)
_FsDcbxCEECtrlEntry_Object=MibTableRow
fsDcbxCEECtrlEntry=_FsDcbxCEECtrlEntry_Object((1,3,6,1,4,1,29601,2,22,3,6,2,1))
fsDcbxCEECtrlEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:fsDcbxCEECtrlEntry.setStatus(_A)
_FsDcbxCEECtrlPortNumber_Type=InterfaceIndex
_FsDcbxCEECtrlPortNumber_Object=MibTableColumn
fsDcbxCEECtrlPortNumber=_FsDcbxCEECtrlPortNumber_Object((1,3,6,1,4,1,29601,2,22,3,6,2,1,1),_FsDcbxCEECtrlPortNumber_Type())
fsDcbxCEECtrlPortNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:fsDcbxCEECtrlPortNumber.setStatus(_A)
_FsDcbxCEECtrlSeqNo_Type=Unsigned32
_FsDcbxCEECtrlSeqNo_Object=MibTableColumn
fsDcbxCEECtrlSeqNo=_FsDcbxCEECtrlSeqNo_Object((1,3,6,1,4,1,29601,2,22,3,6,2,1,2),_FsDcbxCEECtrlSeqNo_Type())
fsDcbxCEECtrlSeqNo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbxCEECtrlSeqNo.setStatus(_A)
_FsDcbxCEECtrlAckNo_Type=Unsigned32
_FsDcbxCEECtrlAckNo_Object=MibTableColumn
fsDcbxCEECtrlAckNo=_FsDcbxCEECtrlAckNo_Object((1,3,6,1,4,1,29601,2,22,3,6,2,1,3),_FsDcbxCEECtrlAckNo_Type())
fsDcbxCEECtrlAckNo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbxCEECtrlAckNo.setStatus(_A)
_FsDcbxCEECtrlRcvdAckNo_Type=Unsigned32
_FsDcbxCEECtrlRcvdAckNo_Object=MibTableColumn
fsDcbxCEECtrlRcvdAckNo=_FsDcbxCEECtrlRcvdAckNo_Object((1,3,6,1,4,1,29601,2,22,3,6,2,1,4),_FsDcbxCEECtrlRcvdAckNo_Type())
fsDcbxCEECtrlRcvdAckNo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbxCEECtrlRcvdAckNo.setStatus(_A)
_FsDcbxCEECtrlTxTLVCounter_Type=Counter32
_FsDcbxCEECtrlTxTLVCounter_Object=MibTableColumn
fsDcbxCEECtrlTxTLVCounter=_FsDcbxCEECtrlTxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,6,2,1,5),_FsDcbxCEECtrlTxTLVCounter_Type())
fsDcbxCEECtrlTxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbxCEECtrlTxTLVCounter.setStatus(_A)
_FsDcbxCEECtrlRxTLVCounter_Type=Counter32
_FsDcbxCEECtrlRxTLVCounter_Object=MibTableColumn
fsDcbxCEECtrlRxTLVCounter=_FsDcbxCEECtrlRxTLVCounter_Object((1,3,6,1,4,1,29601,2,22,3,6,2,1,6),_FsDcbxCEECtrlRxTLVCounter_Type())
fsDcbxCEECtrlRxTLVCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbxCEECtrlRxTLVCounter.setStatus(_A)
_FsDcbxCEECtrlRxTLVErrorCounter_Type=Counter32
_FsDcbxCEECtrlRxTLVErrorCounter_Object=MibTableColumn
fsDcbxCEECtrlRxTLVErrorCounter=_FsDcbxCEECtrlRxTLVErrorCounter_Object((1,3,6,1,4,1,29601,2,22,3,6,2,1,7),_FsDcbxCEECtrlRxTLVErrorCounter_Type())
fsDcbxCEECtrlRxTLVErrorCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcbxCEECtrlRxTLVErrorCounter.setStatus(_A)
_FsDcbNotificationObjects_ObjectIdentity=ObjectIdentity
fsDcbNotificationObjects=_FsDcbNotificationObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,22,4))
_FsDCBTraps_ObjectIdentity=ObjectIdentity
fsDCBTraps=_FsDCBTraps_ObjectIdentity((1,3,6,1,4,1,29601,2,22,4,0))
_FsDCBTrapObjects_ObjectIdentity=ObjectIdentity
fsDCBTrapObjects=_FsDCBTrapObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,22,4,1))
_FsDcbTrapPortNumber_Type=InterfaceIndex
_FsDcbTrapPortNumber_Object=MibScalar
fsDcbTrapPortNumber=_FsDcbTrapPortNumber_Object((1,3,6,1,4,1,29601,2,22,4,1,1),_FsDcbTrapPortNumber_Type())
fsDcbTrapPortNumber.setMaxAccess(_V)
if mibBuilder.loadTexts:fsDcbTrapPortNumber.setStatus(_A)
_FsDcbPeerUpStatus_Type=TruthValue
_FsDcbPeerUpStatus_Object=MibScalar
fsDcbPeerUpStatus=_FsDcbPeerUpStatus_Object((1,3,6,1,4,1,29601,2,22,4,1,2),_FsDcbPeerUpStatus_Type())
fsDcbPeerUpStatus.setMaxAccess(_V)
if mibBuilder.loadTexts:fsDcbPeerUpStatus.setStatus(_A)
class _FsDcbFeatureType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('priorityGroup',1),('priorityFlowControl',2),('applicationPriority',3)))
_FsDcbFeatureType_Type.__name__=_H
_FsDcbFeatureType_Object=MibScalar
fsDcbFeatureType=_FsDcbFeatureType_Object((1,3,6,1,4,1,29601,2,22,4,1,3),_FsDcbFeatureType_Type())
fsDcbFeatureType.setMaxAccess(_V)
if mibBuilder.loadTexts:fsDcbFeatureType.setStatus(_A)
lldpXdot1dcbxAdminApplicationPriorityAppEntry.registerAugmentions((_C,_f))
fsAppPriXAppEntry.setIndexNames(*lldpXdot1dcbxAdminApplicationPriorityAppEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions((_C,_g))
fslldpXdot1dcbxConfigTCSupportedEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
fsETSModuleStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,1))
fsETSModuleStatusTrap.setObjects((_C,_h))
if mibBuilder.loadTexts:fsETSModuleStatusTrap.setStatus(_A)
fsETSPortAdminStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,2))
fsETSPortAdminStatusTrap.setObjects(*((_C,_E),(_C,_i)))
if mibBuilder.loadTexts:fsETSPortAdminStatusTrap.setStatus(_A)
fsETSPortPeerStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,3))
fsETSPortPeerStatusTrap.setObjects(*((_C,_E),(_C,_O)))
if mibBuilder.loadTexts:fsETSPortPeerStatusTrap.setStatus(_A)
fsETSPortDcbxOperStateTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,4))
fsETSPortDcbxOperStateTrap.setObjects(*((_C,_E),(_C,_j)))
if mibBuilder.loadTexts:fsETSPortDcbxOperStateTrap.setStatus(_A)
fsPFCModuleStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,5))
fsPFCModuleStatusTrap.setObjects((_C,_k))
if mibBuilder.loadTexts:fsPFCModuleStatusTrap.setStatus(_A)
fsPFCPortAdminStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,6))
fsPFCPortAdminStatusTrap.setObjects(*((_C,_E),(_C,_l)))
if mibBuilder.loadTexts:fsPFCPortAdminStatusTrap.setStatus(_A)
fsPFCPortPeerStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,7))
fsPFCPortPeerStatusTrap.setObjects(*((_C,_E),(_C,_O)))
if mibBuilder.loadTexts:fsPFCPortPeerStatusTrap.setStatus(_A)
fsPFCPortDcbxOperStateTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,8))
fsPFCPortDcbxOperStateTrap.setObjects(*((_C,_E),(_C,_m)))
if mibBuilder.loadTexts:fsPFCPortDcbxOperStateTrap.setStatus(_A)
fsAppPriModuleStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,9))
fsAppPriModuleStatusTrap.setObjects((_C,_n))
if mibBuilder.loadTexts:fsAppPriModuleStatusTrap.setStatus(_A)
fsAppPriPortAdminStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,10))
fsAppPriPortAdminStatusTrap.setObjects(*((_C,_E),(_C,_o)))
if mibBuilder.loadTexts:fsAppPriPortAdminStatusTrap.setStatus(_A)
fsAppPriPortPeerStatusTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,11))
fsAppPriPortPeerStatusTrap.setObjects(*((_C,_E),(_C,_O)))
if mibBuilder.loadTexts:fsAppPriPortPeerStatusTrap.setStatus(_A)
fsAppPriPortDcbxOperStateTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,12))
fsAppPriPortDcbxOperStateTrap.setObjects(*((_C,_E),(_C,_p)))
if mibBuilder.loadTexts:fsAppPriPortDcbxOperStateTrap.setStatus(_A)
fsDcbxCEELldpTxDisabledTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,13))
fsDcbxCEELldpTxDisabledTrap.setObjects((_C,_E))
if mibBuilder.loadTexts:fsDcbxCEELldpTxDisabledTrap.setStatus(_A)
fsDcbxCEELldpRxDisabledTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,14))
fsDcbxCEELldpRxDisabledTrap.setObjects((_C,_E))
if mibBuilder.loadTexts:fsDcbxCEELldpRxDisabledTrap.setStatus(_A)
fsDcbxCEEDupControlTlvTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,15))
fsDcbxCEEDupControlTlvTrap.setObjects((_C,_E))
if mibBuilder.loadTexts:fsDcbxCEEDupControlTlvTrap.setStatus(_A)
fsDcbxCEEPeerNoRespTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,16))
fsDcbxCEEPeerNoRespTrap.setObjects(*((_C,_E),(_C,_L)))
if mibBuilder.loadTexts:fsDcbxCEEPeerNoRespTrap.setStatus(_A)
fsDcbxCEEDupFeatureTlvTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,17))
fsDcbxCEEDupFeatureTlvTrap.setObjects(*((_C,_E),(_C,_L)))
if mibBuilder.loadTexts:fsDcbxCEEDupFeatureTlvTrap.setStatus(_A)
fsDcbxCEEPeerNoFeatureTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,18))
fsDcbxCEEPeerNoFeatureTrap.setObjects(*((_C,_E),(_C,_L)))
if mibBuilder.loadTexts:fsDcbxCEEPeerNoFeatureTrap.setStatus(_A)
fsDcbxCEEFeatureErrorTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,19))
fsDcbxCEEFeatureErrorTrap.setObjects(*((_C,_E),(_C,_L)))
if mibBuilder.loadTexts:fsDcbxCEEFeatureErrorTrap.setStatus(_A)
fsDcbxCEEAppPriProtocolNotSuppTrap=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,20))
fsDcbxCEEAppPriProtocolNotSuppTrap.setObjects((_C,_E))
if mibBuilder.loadTexts:fsDcbxCEEAppPriProtocolNotSuppTrap.setStatus(_A)
fsDcbxCEEVersionChanged=NotificationType((1,3,6,1,4,1,29601,2,22,4,0,21))
fsDcbxCEEVersionChanged.setObjects(*((_C,_E),(_C,_q)))
if mibBuilder.loadTexts:fsDcbxCEEVersionChanged.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_I:EnabledStatus,_N:DcbAdminMode,'DcbState':DcbState,_a:DcbxVersion,'DcbStateMachineType':DcbStateMachineType,'FsLldpXdot1dcbxTCSupportedCapacity':FsLldpXdot1dcbxTCSupportedCapacity,'DcbxStatus':DcbxStatus,'fsDcbMIB':fsDcbMIB,'fsDcbSystem':fsDcbSystem,'fsDcbPfcMinThreshold':fsDcbPfcMinThreshold,'fsDcbPfcMaxThreshold':fsDcbPfcMaxThreshold,'fsDcbMaxPfcProfiles':fsDcbMaxPfcProfiles,'fsDcbObjects':fsDcbObjects,'fsDcbPortTable':fsDcbPortTable,'fsDcbPortEntry':fsDcbPortEntry,_Y:fsDcbPortNumber,'fsDcbETSAdminStatus':fsDcbETSAdminStatus,'fsDcbPFCAdminStatus':fsDcbPFCAdminStatus,'fsDcbRowStatus':fsDcbRowStatus,'fsDcbAppPriAdminStatus':fsDcbAppPriAdminStatus,'fsDcbOperVersion':fsDcbOperVersion,'fsDcbMaxVersion':fsDcbMaxVersion,'fsDcbPeerOperVersion':fsDcbPeerOperVersion,'fsDcbPeerMaxVersion':fsDcbPeerMaxVersion,'fsDcbApplicationObjects':fsDcbApplicationObjects,'fsDCBXObjects':fsDCBXObjects,'fsDCBXScalars':fsDCBXScalars,'fsDcbxGlobalTraceLevel':fsDcbxGlobalTraceLevel,'fsDCBXPortTable':fsDCBXPortTable,'fsDCBXPortEntry':fsDCBXPortEntry,_Z:fsDCBXPortNumber,'fsDCBXAdminStatus':fsDCBXAdminStatus,_q:fsDCBXMode,'fsETSObjects':fsETSObjects,'fsETSScalars':fsETSScalars,'fsETSSystemControl':fsETSSystemControl,_h:fsETSModuleStatus,'fsETSClearCounters':fsETSClearCounters,'fsETSGlobalEnableTrap':fsETSGlobalEnableTrap,'fsETSGeneratedTrapCount':fsETSGeneratedTrapCount,'fsETSPortTable':fsETSPortTable,'fsETSPortEntry':fsETSPortEntry,_b:fsETSPortNumber,_i:fsETSAdminMode,_j:fsETSDcbxOperState,'fsETSDcbxStateMachine':fsETSDcbxStateMachine,'fsETSClearTLVCounters':fsETSClearTLVCounters,'fsETSConfTxTLVCounter':fsETSConfTxTLVCounter,'fsETSConfRxTLVCounter':fsETSConfRxTLVCounter,'fsETSConfRxTLVErrors':fsETSConfRxTLVErrors,'fsETSRecoTxTLVCounter':fsETSRecoTxTLVCounter,'fsETSRecoRxTLVCounter':fsETSRecoRxTLVCounter,'fsETSRecoRxTLVErrors':fsETSRecoRxTLVErrors,'fsETSTcSuppTxTLVCounter':fsETSTcSuppTxTLVCounter,'fsETSTcSuppRxTLVCounter':fsETSTcSuppRxTLVCounter,'fsETSTcSuppRxTLVErrors':fsETSTcSuppRxTLVErrors,'fsETSRowStatus':fsETSRowStatus,'fsETSSyncd':fsETSSyncd,'fsETSError':fsETSError,'fsETSDcbxStatus':fsETSDcbxStatus,'fsPFCObjects':fsPFCObjects,'fsPFCScalars':fsPFCScalars,'fsPFCSystemControl':fsPFCSystemControl,_k:fsPFCModuleStatus,'fsPFCClearCounters':fsPFCClearCounters,'fsPFCGlobalEnableTrap':fsPFCGlobalEnableTrap,'fsPFCGeneratedTrapCount':fsPFCGeneratedTrapCount,'fsPFCPortTable':fsPFCPortTable,'fsPFCPortEntry':fsPFCPortEntry,_c:fsPFCPortNumber,_l:fsPFCAdminMode,_m:fsPFCDcbxOperState,'fsPFCDcbxStateMachine':fsPFCDcbxStateMachine,'fsPFCClearTLVCounters':fsPFCClearTLVCounters,'fsPFCTxTLVCounter':fsPFCTxTLVCounter,'fsPFCRxTLVCounter':fsPFCRxTLVCounter,'fsPFCRxTLVErrors':fsPFCRxTLVErrors,'fsPFCRowStatus':fsPFCRowStatus,'fsPFCSyncd':fsPFCSyncd,'fsPFCError':fsPFCError,'fsPFCDcbxStatus':fsPFCDcbxStatus,'fsPFCRxPauseFrameCounter':fsPFCRxPauseFrameCounter,'fsPFCTxPauseFrameCounter':fsPFCTxPauseFrameCounter,'fsPFCRxPauseFrameP0Counter':fsPFCRxPauseFrameP0Counter,'fsPFCRxPauseFrameP1Counter':fsPFCRxPauseFrameP1Counter,'fsPFCRxPauseFrameP2Counter':fsPFCRxPauseFrameP2Counter,'fsPFCRxPauseFrameP3Counter':fsPFCRxPauseFrameP3Counter,'fsPFCRxPauseFrameP4Counter':fsPFCRxPauseFrameP4Counter,'fsPFCRxPauseFrameP5Counter':fsPFCRxPauseFrameP5Counter,'fsPFCRxPauseFrameP6Counter':fsPFCRxPauseFrameP6Counter,'fsPFCRxPauseFrameP7Counter':fsPFCRxPauseFrameP7Counter,'fsPFCTxPauseFrameP0Counter':fsPFCTxPauseFrameP0Counter,'fsPFCTxPauseFrameP1Counter':fsPFCTxPauseFrameP1Counter,'fsPFCTxPauseFrameP2Counter':fsPFCTxPauseFrameP2Counter,'fsPFCTxPauseFrameP3Counter':fsPFCTxPauseFrameP3Counter,'fsPFCTxPauseFrameP4Counter':fsPFCTxPauseFrameP4Counter,'fsPFCTxPauseFrameP5Counter':fsPFCTxPauseFrameP5Counter,'fsPFCTxPauseFrameP6Counter':fsPFCTxPauseFrameP6Counter,'fsPFCTxPauseFrameP7Counter':fsPFCTxPauseFrameP7Counter,'fsPFCDataFrameDiscardCounter':fsPFCDataFrameDiscardCounter,'fsPFCClearPauseFrameCounters':fsPFCClearPauseFrameCounters,'fsAppPriObjects':fsAppPriObjects,'fsAppPriScalars':fsAppPriScalars,'fsAppPriSystemControl':fsAppPriSystemControl,_n:fsAppPriModuleStatus,'fsAppPriClearCounters':fsAppPriClearCounters,'fsAppPriGlobalEnableTrap':fsAppPriGlobalEnableTrap,'fsAppPriGeneratedTrapCount':fsAppPriGeneratedTrapCount,'fsAppPriPortTable':fsAppPriPortTable,'fsAppPriPortEntry':fsAppPriPortEntry,_d:fsAppPriPortNumber,_o:fsAppPriAdminMode,_p:fsAppPriDcbxOperState,'fsAppPriDcbxStateMachine':fsAppPriDcbxStateMachine,'fsAppPriClearTLVCounters':fsAppPriClearTLVCounters,'fsAppPriTxTLVCounter':fsAppPriTxTLVCounter,'fsAppPriRxTLVCounter':fsAppPriRxTLVCounter,'fsAppPriRxTLVErrors':fsAppPriRxTLVErrors,'fsAppPriAppProtocols':fsAppPriAppProtocols,'fsAppPriRowStatus':fsAppPriRowStatus,'fsAppPriSyncd':fsAppPriSyncd,'fsAppPriError':fsAppPriError,'fsAppPriDcbxStatus':fsAppPriDcbxStatus,'fsAppPriXAppTable':fsAppPriXAppTable,_f:fsAppPriXAppEntry,'fsAppPriXAppRowStatus':fsAppPriXAppRowStatus,'fslldpXdot1dcbxLocApplicationPriorityBasicTable':fslldpXdot1dcbxLocApplicationPriorityBasicTable,'fslldpXdot1dcbxLocApplicationPriorityBasicEntry':fslldpXdot1dcbxLocApplicationPriorityBasicEntry,'fslldpXdot1dcbxLocApplicationPriorityWilling':fslldpXdot1dcbxLocApplicationPriorityWilling,'fslldpXdot1dcbxAdminApplicationPriorityBasicTable':fslldpXdot1dcbxAdminApplicationPriorityBasicTable,'fslldpXdot1dcbxAdminApplicationPriorityBasicEntry':fslldpXdot1dcbxAdminApplicationPriorityBasicEntry,'fslldpXdot1dcbxAdminApplicationPriorityWilling':fslldpXdot1dcbxAdminApplicationPriorityWilling,'fslldpXdot1dcbxRemApplicationPriorityBasicTable':fslldpXdot1dcbxRemApplicationPriorityBasicTable,'fslldpXdot1dcbxRemApplicationPriorityBasicEntry':fslldpXdot1dcbxRemApplicationPriorityBasicEntry,'fslldpXdot1dcbxRemApplicationPriorityWilling':fslldpXdot1dcbxRemApplicationPriorityWilling,'fsTCSupportedObjects':fsTCSupportedObjects,'fslldpXdot1dcbxConfigTCSupportedTable':fslldpXdot1dcbxConfigTCSupportedTable,_g:fslldpXdot1dcbxConfigTCSupportedEntry,'fslldpXdot1dcbxConfigTCSupportedTxEnable':fslldpXdot1dcbxConfigTCSupportedTxEnable,'fslldpXdot1dcbxLocTCSupportedTable':fslldpXdot1dcbxLocTCSupportedTable,'fslldpXdot1dcbxLocTCSupportedEntry':fslldpXdot1dcbxLocTCSupportedEntry,'fslldpXdot1dcbxLocTCSupported':fslldpXdot1dcbxLocTCSupported,'fslldpXdot1dcbxRemTCSupportedTable':fslldpXdot1dcbxRemTCSupportedTable,'fslldpXdot1dcbxRemTCSupportedEntry':fslldpXdot1dcbxRemTCSupportedEntry,'fslldpXdot1dcbxRemTCSupported':fslldpXdot1dcbxRemTCSupported,'fslldpXdot1dcbxAdminTCSupportedTable':fslldpXdot1dcbxAdminTCSupportedTable,'fslldpXdot1dcbxAdminTCSupportedEntry':fslldpXdot1dcbxAdminTCSupportedEntry,'fslldpXdot1dcbxAdminTCSupported':fslldpXdot1dcbxAdminTCSupported,'fsDcbxCEEObjects':fsDcbxCEEObjects,'fsDcbxCEEScalars':fsDcbxCEEScalars,'fsDcbxCEEGlobalEnableTrap':fsDcbxCEEGlobalEnableTrap,'fsDcbxCEEGeneratedTrapCount':fsDcbxCEEGeneratedTrapCount,'fsDcbxCEEClearCounters':fsDcbxCEEClearCounters,'fsDcbxCEECtrlTable':fsDcbxCEECtrlTable,'fsDcbxCEECtrlEntry':fsDcbxCEECtrlEntry,_e:fsDcbxCEECtrlPortNumber,'fsDcbxCEECtrlSeqNo':fsDcbxCEECtrlSeqNo,'fsDcbxCEECtrlAckNo':fsDcbxCEECtrlAckNo,'fsDcbxCEECtrlRcvdAckNo':fsDcbxCEECtrlRcvdAckNo,'fsDcbxCEECtrlTxTLVCounter':fsDcbxCEECtrlTxTLVCounter,'fsDcbxCEECtrlRxTLVCounter':fsDcbxCEECtrlRxTLVCounter,'fsDcbxCEECtrlRxTLVErrorCounter':fsDcbxCEECtrlRxTLVErrorCounter,'fsDcbNotificationObjects':fsDcbNotificationObjects,'fsDCBTraps':fsDCBTraps,'fsETSModuleStatusTrap':fsETSModuleStatusTrap,'fsETSPortAdminStatusTrap':fsETSPortAdminStatusTrap,'fsETSPortPeerStatusTrap':fsETSPortPeerStatusTrap,'fsETSPortDcbxOperStateTrap':fsETSPortDcbxOperStateTrap,'fsPFCModuleStatusTrap':fsPFCModuleStatusTrap,'fsPFCPortAdminStatusTrap':fsPFCPortAdminStatusTrap,'fsPFCPortPeerStatusTrap':fsPFCPortPeerStatusTrap,'fsPFCPortDcbxOperStateTrap':fsPFCPortDcbxOperStateTrap,'fsAppPriModuleStatusTrap':fsAppPriModuleStatusTrap,'fsAppPriPortAdminStatusTrap':fsAppPriPortAdminStatusTrap,'fsAppPriPortPeerStatusTrap':fsAppPriPortPeerStatusTrap,'fsAppPriPortDcbxOperStateTrap':fsAppPriPortDcbxOperStateTrap,'fsDcbxCEELldpTxDisabledTrap':fsDcbxCEELldpTxDisabledTrap,'fsDcbxCEELldpRxDisabledTrap':fsDcbxCEELldpRxDisabledTrap,'fsDcbxCEEDupControlTlvTrap':fsDcbxCEEDupControlTlvTrap,'fsDcbxCEEPeerNoRespTrap':fsDcbxCEEPeerNoRespTrap,'fsDcbxCEEDupFeatureTlvTrap':fsDcbxCEEDupFeatureTlvTrap,'fsDcbxCEEPeerNoFeatureTrap':fsDcbxCEEPeerNoFeatureTrap,'fsDcbxCEEFeatureErrorTrap':fsDcbxCEEFeatureErrorTrap,'fsDcbxCEEAppPriProtocolNotSuppTrap':fsDcbxCEEAppPriProtocolNotSuppTrap,'fsDcbxCEEVersionChanged':fsDcbxCEEVersionChanged,'fsDCBTrapObjects':fsDCBTrapObjects,_E:fsDcbTrapPortNumber,_O:fsDcbPeerUpStatus,_L:fsDcbFeatureType})