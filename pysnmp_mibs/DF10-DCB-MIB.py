_Ak='dF10DcbObjectGroup'
_Aj='dF10DCBNotificationsGroup'
_Ai='dF10DCBNotificationObjectsGroup'
_Ah='dF10PFCPortTableGroup'
_Ag='dF10PFCScalarsGroup'
_Af='dF10ETSPortTableGroup'
_Ae='dF10ETSScalarsGroup'
_Ad='dF10DCBXPortTableGroup'
_Ac='dF10DcbxScalarsGroup'
_Ab='dF10DcbSystemObjectGroup'
_Aa='dF10PFCPortDcbxOperStateTrap'
_AZ='dF10PFCPortPeerStatusTrap'
_AY='dF10PFCPortAdminStatusTrap'
_AX='dF10PFCModuleStatusTrap'
_AW='dF10ETSPortDcbxOperStateTrap'
_AV='dF10ETSPortPeerStatusTrap'
_AU='dF10ETSPortAdminStatusTrap'
_AT='dF10ETSModuleStatusTrap'
_AS='dF10PFCRxTLVErrors'
_AR='dF10PFCRxTLVCounter'
_AQ='dF10PFCTxTLVCounter'
_AP='dF10PFCClearTLVCounters'
_AO='dF10PFCOperStatus'
_AN='dF10PFCDcbxStateMachine'
_AM='dF10PFCGlobalEnableTrap'
_AL='dF10PFCClearCounters'
_AK='dF10PFCSystemControl'
_AJ='dF10ETSRecoRxTLVErrors'
_AI='dF10ETSRecoRxTLVCounter'
_AH='dF10ETSRecoTxTLVCounter'
_AG='dF10ETSConfRxTLVErrors'
_AF='dF10ETSConfRxTLVCounter'
_AE='dF10ETSConfTxTLVCounter'
_AD='dF10ETSClearTLVCounters'
_AC='dF10ETSOperStatus'
_AB='dF10ETSDcbxStateMachine'
_AA='dF10ETSGlobalEnableTrap'
_A9='dF10ETSClearCounters'
_A8='dF10ETSSystemControl'
_A7='dF10DCBXPortErrorFramesCount'
_A6='dF10DCBXPortRxCount'
_A5='dF10DCBXPortTxCount'
_A4='dF10DCBXPortPeerRcvdAckNum'
_A3='dF10DCBXPortAckNum'
_A2='dF10DCBXPortSeqNum'
_A1='dF10DCBXPortPeerMaxVersion'
_A0='dF10DCBXPortPeerOperVersionNum'
_z='dF10DCBXPortPeerRemovedCount'
_y='dF10DCBXPortMultiplePeerCount'
_x='dF10DCBXOperStatus'
_w='dF10DCBXPortCfgSource'
_v='dF10DCBXPortPeerMACaddress'
_u='dF10DCBXPortOperVersion'
_t='dF10DCBXPortConfigTLVsTxEnable'
_s='dF10DCBXPortSupportedTLVs'
_r='dF10DCBXPortVersion'
_q='dF10DCBXAutoCfgPortRole'
_p='dF10DCBXAdminStatus'
_o='dF10DCBXGlobalVersion'
_n='dF10DcbxGlobalTraceLevel'
_m='dF10DcbPFCAdminStatus'
_l='dF10DcbETSAdminStatus'
_k='dF10DcbMaxPfcProfiles'
_j='dF10DcbPfcMaxThreshold'
_i='dF10DcbPfcMinThreshold'
_h='dF10DCBXPortStatusEntry'
_g='accessible-for-notify'
_f='dF10PFCPortNumber'
_e='dF10ETSPortNumber'
_d='shutdown'
_c='running'
_b='applicationPriorityISCSI'
_a='applicationPriorityFCOE'
_Z='etsRecom'
_Y='etsConfig'
_X='DcbxPortRole'
_W='dF10DCBXPortNumber'
_V='dF10DcbPortNumber'
_U='dF10PFCDcbxOperState'
_T='dF10PFCAdminMode'
_S='dF10PFCModuleStatus'
_R='dF10ETSDcbxOperState'
_Q='dF10ETSAdminMode'
_P='dF10ETSModuleStatus'
_O='DcbAdminMode'
_N='Bits'
_M='dF10DcbPeerUpStatus'
_L='DcbxVersion'
_K='not-accessible'
_J='Unsigned32'
_I='TruthValue'
_H='EnabledStatus'
_G='Integer32'
_F='obsolete'
_E='dF10DcbTrapPortNumber'
_D='read-write'
_C='read-only'
_B='current'
_A='DF10-DCB-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_N,'Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_I)
dF10Dcb=ModuleIdentity((1,3,6,1,4,1,6027,3,15))
if mibBuilder.loadTexts:dF10Dcb.setRevisions(('2012-04-16 00:00','2011-11-24 00:00','2010-09-25 00:00'))
class EnabledStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
class DcbAdminMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
class DcbState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off',0),('init',1),('rxrecommended',2),('internallypropagated',3)))
class DcbStateMachineType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('asymmetric',1),('symmetric',2),('feature',3)))
class DcbxPortRole(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('manual',1),('autoup',2),('autodown',3),('configSource',4)))
class DcbxVersion(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),('ieee',2),('cin',3),('cee',4)))
_DF10DcbSystem_ObjectIdentity=ObjectIdentity
dF10DcbSystem=_DF10DcbSystem_ObjectIdentity((1,3,6,1,4,1,6027,3,15,1))
class _DF10DcbPfcMinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DF10DcbPfcMinThreshold_Type.__name__=_J
_DF10DcbPfcMinThreshold_Object=MibScalar
dF10DcbPfcMinThreshold=_DF10DcbPfcMinThreshold_Object((1,3,6,1,4,1,6027,3,15,1,1),_DF10DcbPfcMinThreshold_Type())
dF10DcbPfcMinThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DcbPfcMinThreshold.setStatus(_B)
class _DF10DcbPfcMaxThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DF10DcbPfcMaxThreshold_Type.__name__=_J
_DF10DcbPfcMaxThreshold_Object=MibScalar
dF10DcbPfcMaxThreshold=_DF10DcbPfcMaxThreshold_Object((1,3,6,1,4,1,6027,3,15,1,2),_DF10DcbPfcMaxThreshold_Type())
dF10DcbPfcMaxThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DcbPfcMaxThreshold.setStatus(_B)
class _DF10DcbMaxPfcProfiles_Type(Unsigned32):defaultValue=256;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_DF10DcbMaxPfcProfiles_Type.__name__=_J
_DF10DcbMaxPfcProfiles_Object=MibScalar
dF10DcbMaxPfcProfiles=_DF10DcbMaxPfcProfiles_Object((1,3,6,1,4,1,6027,3,15,1,3),_DF10DcbMaxPfcProfiles_Type())
dF10DcbMaxPfcProfiles.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DcbMaxPfcProfiles.setStatus(_B)
_DF10DcbObjects_ObjectIdentity=ObjectIdentity
dF10DcbObjects=_DF10DcbObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,2))
_DF10DcbPortTable_Object=MibTable
dF10DcbPortTable=_DF10DcbPortTable_Object((1,3,6,1,4,1,6027,3,15,2,1))
if mibBuilder.loadTexts:dF10DcbPortTable.setStatus(_F)
_DF10DcbPortEntry_Object=MibTableRow
dF10DcbPortEntry=_DF10DcbPortEntry_Object((1,3,6,1,4,1,6027,3,15,2,1,1))
dF10DcbPortEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:dF10DcbPortEntry.setStatus(_F)
_DF10DcbPortNumber_Type=InterfaceIndex
_DF10DcbPortNumber_Object=MibTableColumn
dF10DcbPortNumber=_DF10DcbPortNumber_Object((1,3,6,1,4,1,6027,3,15,2,1,1,1),_DF10DcbPortNumber_Type())
dF10DcbPortNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:dF10DcbPortNumber.setStatus(_F)
class _DF10DcbETSAdminStatus_Type(EnabledStatus):defaultValue=1
_DF10DcbETSAdminStatus_Type.__name__=_H
_DF10DcbETSAdminStatus_Object=MibTableColumn
dF10DcbETSAdminStatus=_DF10DcbETSAdminStatus_Object((1,3,6,1,4,1,6027,3,15,2,1,1,2),_DF10DcbETSAdminStatus_Type())
dF10DcbETSAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DcbETSAdminStatus.setStatus(_F)
class _DF10DcbPFCAdminStatus_Type(EnabledStatus):defaultValue=1
_DF10DcbPFCAdminStatus_Type.__name__=_H
_DF10DcbPFCAdminStatus_Object=MibTableColumn
dF10DcbPFCAdminStatus=_DF10DcbPFCAdminStatus_Object((1,3,6,1,4,1,6027,3,15,2,1,1,3),_DF10DcbPFCAdminStatus_Type())
dF10DcbPFCAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DcbPFCAdminStatus.setStatus(_F)
_DF10DcbApplicationObjects_ObjectIdentity=ObjectIdentity
dF10DcbApplicationObjects=_DF10DcbApplicationObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3))
_DF10DCBXObjects_ObjectIdentity=ObjectIdentity
dF10DCBXObjects=_DF10DCBXObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,1))
_DF10DCBXScalars_ObjectIdentity=ObjectIdentity
dF10DCBXScalars=_DF10DCBXScalars_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,1,1))
_DF10DcbxGlobalTraceLevel_Type=Integer32
_DF10DcbxGlobalTraceLevel_Object=MibScalar
dF10DcbxGlobalTraceLevel=_DF10DcbxGlobalTraceLevel_Object((1,3,6,1,4,1,6027,3,15,3,1,1,1),_DF10DcbxGlobalTraceLevel_Type())
dF10DcbxGlobalTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:dF10DcbxGlobalTraceLevel.setStatus(_B)
class _DF10DCBXGlobalVersion_Type(DcbxVersion):defaultValue=1
_DF10DCBXGlobalVersion_Type.__name__=_L
_DF10DCBXGlobalVersion_Object=MibScalar
dF10DCBXGlobalVersion=_DF10DCBXGlobalVersion_Object((1,3,6,1,4,1,6027,3,15,3,1,1,2),_DF10DCBXGlobalVersion_Type())
dF10DCBXGlobalVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dF10DCBXGlobalVersion.setStatus(_B)
_DF10DCBXPortTable_Object=MibTable
dF10DCBXPortTable=_DF10DCBXPortTable_Object((1,3,6,1,4,1,6027,3,15,3,1,2))
if mibBuilder.loadTexts:dF10DCBXPortTable.setStatus(_B)
_DF10DCBXPortEntry_Object=MibTableRow
dF10DCBXPortEntry=_DF10DCBXPortEntry_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1))
dF10DCBXPortEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:dF10DCBXPortEntry.setStatus(_B)
_DF10DCBXPortNumber_Type=InterfaceIndex
_DF10DCBXPortNumber_Object=MibTableColumn
dF10DCBXPortNumber=_DF10DCBXPortNumber_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,1),_DF10DCBXPortNumber_Type())
dF10DCBXPortNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:dF10DCBXPortNumber.setStatus(_B)
class _DF10DCBXAdminStatus_Type(EnabledStatus):defaultValue=1
_DF10DCBXAdminStatus_Type.__name__=_H
_DF10DCBXAdminStatus_Object=MibTableColumn
dF10DCBXAdminStatus=_DF10DCBXAdminStatus_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,2),_DF10DCBXAdminStatus_Type())
dF10DCBXAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXAdminStatus.setStatus(_B)
class _DF10DCBXAutoCfgPortRole_Type(DcbxPortRole):defaultValue=1
_DF10DCBXAutoCfgPortRole_Type.__name__=_X
_DF10DCBXAutoCfgPortRole_Object=MibTableColumn
dF10DCBXAutoCfgPortRole=_DF10DCBXAutoCfgPortRole_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,3),_DF10DCBXAutoCfgPortRole_Type())
dF10DCBXAutoCfgPortRole.setMaxAccess(_D)
if mibBuilder.loadTexts:dF10DCBXAutoCfgPortRole.setStatus(_B)
class _DF10DCBXPortVersion_Type(DcbxVersion):defaultValue=1
_DF10DCBXPortVersion_Type.__name__=_L
_DF10DCBXPortVersion_Object=MibTableColumn
dF10DCBXPortVersion=_DF10DCBXPortVersion_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,4),_DF10DCBXPortVersion_Type())
dF10DCBXPortVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dF10DCBXPortVersion.setStatus(_B)
class _DF10DCBXPortSupportedTLVs_Type(Bits):namedValues=NamedValues(*(('pfc',0),(_Y,1),(_Z,2),(_a,3),(_b,4)))
_DF10DCBXPortSupportedTLVs_Type.__name__=_N
_DF10DCBXPortSupportedTLVs_Object=MibTableColumn
dF10DCBXPortSupportedTLVs=_DF10DCBXPortSupportedTLVs_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,5),_DF10DCBXPortSupportedTLVs_Type())
dF10DCBXPortSupportedTLVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortSupportedTLVs.setStatus(_B)
class _DF10DCBXPortConfigTLVsTxEnable_Type(Bits):namedValues=NamedValues(*(('pfc',0),(_Y,1),(_Z,2),(_a,3),(_b,4)))
_DF10DCBXPortConfigTLVsTxEnable_Type.__name__=_N
_DF10DCBXPortConfigTLVsTxEnable_Object=MibTableColumn
dF10DCBXPortConfigTLVsTxEnable=_DF10DCBXPortConfigTLVsTxEnable_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,6),_DF10DCBXPortConfigTLVsTxEnable_Type())
dF10DCBXPortConfigTLVsTxEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dF10DCBXPortConfigTLVsTxEnable.setStatus(_B)
_DF10DCBXPortStatusTable_Object=MibTable
dF10DCBXPortStatusTable=_DF10DCBXPortStatusTable_Object((1,3,6,1,4,1,6027,3,15,3,1,3))
if mibBuilder.loadTexts:dF10DCBXPortStatusTable.setStatus(_B)
_DF10DCBXPortStatusEntry_Object=MibTableRow
dF10DCBXPortStatusEntry=_DF10DCBXPortStatusEntry_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1))
if mibBuilder.loadTexts:dF10DCBXPortStatusEntry.setStatus(_B)
class _DF10DCBXPortOperVersion_Type(DcbxVersion):defaultValue=1
_DF10DCBXPortOperVersion_Type.__name__=_L
_DF10DCBXPortOperVersion_Object=MibTableColumn
dF10DCBXPortOperVersion=_DF10DCBXPortOperVersion_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,2),_DF10DCBXPortOperVersion_Type())
dF10DCBXPortOperVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortOperVersion.setStatus(_B)
_DF10DCBXPortPeerMACaddress_Type=MacAddress
_DF10DCBXPortPeerMACaddress_Object=MibTableColumn
dF10DCBXPortPeerMACaddress=_DF10DCBXPortPeerMACaddress_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,3),_DF10DCBXPortPeerMACaddress_Type())
dF10DCBXPortPeerMACaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortPeerMACaddress.setStatus(_B)
class _DF10DCBXPortCfgSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_DF10DCBXPortCfgSource_Type.__name__=_G
_DF10DCBXPortCfgSource_Object=MibTableColumn
dF10DCBXPortCfgSource=_DF10DCBXPortCfgSource_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,4),_DF10DCBXPortCfgSource_Type())
dF10DCBXPortCfgSource.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortCfgSource.setStatus(_B)
_DF10DCBXOperStatus_Type=EnabledStatus
_DF10DCBXOperStatus_Object=MibTableColumn
dF10DCBXOperStatus=_DF10DCBXOperStatus_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,5),_DF10DCBXOperStatus_Type())
dF10DCBXOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXOperStatus.setStatus(_B)
_DF10DCBXPortMultiplePeerCount_Type=Counter32
_DF10DCBXPortMultiplePeerCount_Object=MibTableColumn
dF10DCBXPortMultiplePeerCount=_DF10DCBXPortMultiplePeerCount_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,6),_DF10DCBXPortMultiplePeerCount_Type())
dF10DCBXPortMultiplePeerCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortMultiplePeerCount.setStatus(_B)
_DF10DCBXPortPeerRemovedCount_Type=Counter32
_DF10DCBXPortPeerRemovedCount_Object=MibTableColumn
dF10DCBXPortPeerRemovedCount=_DF10DCBXPortPeerRemovedCount_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,7),_DF10DCBXPortPeerRemovedCount_Type())
dF10DCBXPortPeerRemovedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortPeerRemovedCount.setStatus(_B)
_DF10DCBXPortPeerOperVersionNum_Type=Unsigned32
_DF10DCBXPortPeerOperVersionNum_Object=MibTableColumn
dF10DCBXPortPeerOperVersionNum=_DF10DCBXPortPeerOperVersionNum_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,8),_DF10DCBXPortPeerOperVersionNum_Type())
dF10DCBXPortPeerOperVersionNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortPeerOperVersionNum.setStatus(_B)
_DF10DCBXPortPeerMaxVersion_Type=Unsigned32
_DF10DCBXPortPeerMaxVersion_Object=MibTableColumn
dF10DCBXPortPeerMaxVersion=_DF10DCBXPortPeerMaxVersion_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,9),_DF10DCBXPortPeerMaxVersion_Type())
dF10DCBXPortPeerMaxVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortPeerMaxVersion.setStatus(_B)
_DF10DCBXPortSeqNum_Type=Unsigned32
_DF10DCBXPortSeqNum_Object=MibTableColumn
dF10DCBXPortSeqNum=_DF10DCBXPortSeqNum_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,10),_DF10DCBXPortSeqNum_Type())
dF10DCBXPortSeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortSeqNum.setStatus(_B)
_DF10DCBXPortAckNum_Type=Unsigned32
_DF10DCBXPortAckNum_Object=MibTableColumn
dF10DCBXPortAckNum=_DF10DCBXPortAckNum_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,11),_DF10DCBXPortAckNum_Type())
dF10DCBXPortAckNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortAckNum.setStatus(_B)
_DF10DCBXPortPeerRcvdAckNum_Type=Unsigned32
_DF10DCBXPortPeerRcvdAckNum_Object=MibTableColumn
dF10DCBXPortPeerRcvdAckNum=_DF10DCBXPortPeerRcvdAckNum_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,12),_DF10DCBXPortPeerRcvdAckNum_Type())
dF10DCBXPortPeerRcvdAckNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortPeerRcvdAckNum.setStatus(_B)
_DF10DCBXPortTxCount_Type=Counter32
_DF10DCBXPortTxCount_Object=MibTableColumn
dF10DCBXPortTxCount=_DF10DCBXPortTxCount_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,13),_DF10DCBXPortTxCount_Type())
dF10DCBXPortTxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortTxCount.setStatus(_B)
_DF10DCBXPortRxCount_Type=Counter32
_DF10DCBXPortRxCount_Object=MibTableColumn
dF10DCBXPortRxCount=_DF10DCBXPortRxCount_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,14),_DF10DCBXPortRxCount_Type())
dF10DCBXPortRxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortRxCount.setStatus(_B)
_DF10DCBXPortErrorFramesCount_Type=Counter32
_DF10DCBXPortErrorFramesCount_Object=MibTableColumn
dF10DCBXPortErrorFramesCount=_DF10DCBXPortErrorFramesCount_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,15),_DF10DCBXPortErrorFramesCount_Type())
dF10DCBXPortErrorFramesCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10DCBXPortErrorFramesCount.setStatus(_B)
_DF10ETSObjects_ObjectIdentity=ObjectIdentity
dF10ETSObjects=_DF10ETSObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,2))
_DF10ETSScalars_ObjectIdentity=ObjectIdentity
dF10ETSScalars=_DF10ETSScalars_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,2,1))
class _DF10ETSSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_DF10ETSSystemControl_Type.__name__=_G
_DF10ETSSystemControl_Object=MibScalar
dF10ETSSystemControl=_DF10ETSSystemControl_Object((1,3,6,1,4,1,6027,3,15,3,2,1,1),_DF10ETSSystemControl_Type())
dF10ETSSystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSSystemControl.setStatus(_B)
class _DF10ETSModuleStatus_Type(EnabledStatus):defaultValue=1
_DF10ETSModuleStatus_Type.__name__=_H
_DF10ETSModuleStatus_Object=MibScalar
dF10ETSModuleStatus=_DF10ETSModuleStatus_Object((1,3,6,1,4,1,6027,3,15,3,2,1,2),_DF10ETSModuleStatus_Type())
dF10ETSModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSModuleStatus.setStatus(_B)
class _DF10ETSClearCounters_Type(TruthValue):defaultValue=2
_DF10ETSClearCounters_Type.__name__=_I
_DF10ETSClearCounters_Object=MibScalar
dF10ETSClearCounters=_DF10ETSClearCounters_Object((1,3,6,1,4,1,6027,3,15,3,2,1,3),_DF10ETSClearCounters_Type())
dF10ETSClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:dF10ETSClearCounters.setStatus(_B)
class _DF10ETSGlobalEnableTrap_Type(Integer32):defaultValue=0
_DF10ETSGlobalEnableTrap_Type.__name__=_G
_DF10ETSGlobalEnableTrap_Object=MibScalar
dF10ETSGlobalEnableTrap=_DF10ETSGlobalEnableTrap_Object((1,3,6,1,4,1,6027,3,15,3,2,1,4),_DF10ETSGlobalEnableTrap_Type())
dF10ETSGlobalEnableTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSGlobalEnableTrap.setStatus(_B)
_DF10ETSPortTable_Object=MibTable
dF10ETSPortTable=_DF10ETSPortTable_Object((1,3,6,1,4,1,6027,3,15,3,2,2))
if mibBuilder.loadTexts:dF10ETSPortTable.setStatus(_B)
_DF10ETSPortEntry_Object=MibTableRow
dF10ETSPortEntry=_DF10ETSPortEntry_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1))
dF10ETSPortEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:dF10ETSPortEntry.setStatus(_B)
_DF10ETSPortNumber_Type=InterfaceIndex
_DF10ETSPortNumber_Object=MibTableColumn
dF10ETSPortNumber=_DF10ETSPortNumber_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,1),_DF10ETSPortNumber_Type())
dF10ETSPortNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:dF10ETSPortNumber.setStatus(_B)
class _DF10ETSAdminMode_Type(DcbAdminMode):defaultValue=1
_DF10ETSAdminMode_Type.__name__=_O
_DF10ETSAdminMode_Object=MibTableColumn
dF10ETSAdminMode=_DF10ETSAdminMode_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,2),_DF10ETSAdminMode_Type())
dF10ETSAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSAdminMode.setStatus(_B)
_DF10ETSDcbxOperState_Type=DcbState
_DF10ETSDcbxOperState_Object=MibTableColumn
dF10ETSDcbxOperState=_DF10ETSDcbxOperState_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,3),_DF10ETSDcbxOperState_Type())
dF10ETSDcbxOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSDcbxOperState.setStatus(_B)
_DF10ETSDcbxStateMachine_Type=DcbStateMachineType
_DF10ETSDcbxStateMachine_Object=MibTableColumn
dF10ETSDcbxStateMachine=_DF10ETSDcbxStateMachine_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,4),_DF10ETSDcbxStateMachine_Type())
dF10ETSDcbxStateMachine.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSDcbxStateMachine.setStatus(_B)
_DF10ETSOperStatus_Type=EnabledStatus
_DF10ETSOperStatus_Object=MibTableColumn
dF10ETSOperStatus=_DF10ETSOperStatus_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,5),_DF10ETSOperStatus_Type())
dF10ETSOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSOperStatus.setStatus(_B)
class _DF10ETSClearTLVCounters_Type(TruthValue):defaultValue=2
_DF10ETSClearTLVCounters_Type.__name__=_I
_DF10ETSClearTLVCounters_Object=MibTableColumn
dF10ETSClearTLVCounters=_DF10ETSClearTLVCounters_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,6),_DF10ETSClearTLVCounters_Type())
dF10ETSClearTLVCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:dF10ETSClearTLVCounters.setStatus(_B)
_DF10ETSConfTxTLVCounter_Type=Counter32
_DF10ETSConfTxTLVCounter_Object=MibTableColumn
dF10ETSConfTxTLVCounter=_DF10ETSConfTxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,7),_DF10ETSConfTxTLVCounter_Type())
dF10ETSConfTxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSConfTxTLVCounter.setStatus(_B)
_DF10ETSConfRxTLVCounter_Type=Counter32
_DF10ETSConfRxTLVCounter_Object=MibTableColumn
dF10ETSConfRxTLVCounter=_DF10ETSConfRxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,8),_DF10ETSConfRxTLVCounter_Type())
dF10ETSConfRxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSConfRxTLVCounter.setStatus(_B)
_DF10ETSConfRxTLVErrors_Type=Counter32
_DF10ETSConfRxTLVErrors_Object=MibTableColumn
dF10ETSConfRxTLVErrors=_DF10ETSConfRxTLVErrors_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,9),_DF10ETSConfRxTLVErrors_Type())
dF10ETSConfRxTLVErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSConfRxTLVErrors.setStatus(_B)
_DF10ETSRecoTxTLVCounter_Type=Counter32
_DF10ETSRecoTxTLVCounter_Object=MibTableColumn
dF10ETSRecoTxTLVCounter=_DF10ETSRecoTxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,10),_DF10ETSRecoTxTLVCounter_Type())
dF10ETSRecoTxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSRecoTxTLVCounter.setStatus(_B)
_DF10ETSRecoRxTLVCounter_Type=Counter32
_DF10ETSRecoRxTLVCounter_Object=MibTableColumn
dF10ETSRecoRxTLVCounter=_DF10ETSRecoRxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,11),_DF10ETSRecoRxTLVCounter_Type())
dF10ETSRecoRxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSRecoRxTLVCounter.setStatus(_B)
_DF10ETSRecoRxTLVErrors_Type=Counter32
_DF10ETSRecoRxTLVErrors_Object=MibTableColumn
dF10ETSRecoRxTLVErrors=_DF10ETSRecoRxTLVErrors_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,12),_DF10ETSRecoRxTLVErrors_Type())
dF10ETSRecoRxTLVErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10ETSRecoRxTLVErrors.setStatus(_B)
_DF10PFCObjects_ObjectIdentity=ObjectIdentity
dF10PFCObjects=_DF10PFCObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,3))
_DF10PFCScalars_ObjectIdentity=ObjectIdentity
dF10PFCScalars=_DF10PFCScalars_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,3,1))
class _DF10PFCSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_DF10PFCSystemControl_Type.__name__=_G
_DF10PFCSystemControl_Object=MibScalar
dF10PFCSystemControl=_DF10PFCSystemControl_Object((1,3,6,1,4,1,6027,3,15,3,3,1,1),_DF10PFCSystemControl_Type())
dF10PFCSystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10PFCSystemControl.setStatus(_B)
class _DF10PFCModuleStatus_Type(EnabledStatus):defaultValue=1
_DF10PFCModuleStatus_Type.__name__=_H
_DF10PFCModuleStatus_Object=MibScalar
dF10PFCModuleStatus=_DF10PFCModuleStatus_Object((1,3,6,1,4,1,6027,3,15,3,3,1,2),_DF10PFCModuleStatus_Type())
dF10PFCModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10PFCModuleStatus.setStatus(_B)
class _DF10PFCClearCounters_Type(TruthValue):defaultValue=2
_DF10PFCClearCounters_Type.__name__=_I
_DF10PFCClearCounters_Object=MibScalar
dF10PFCClearCounters=_DF10PFCClearCounters_Object((1,3,6,1,4,1,6027,3,15,3,3,1,3),_DF10PFCClearCounters_Type())
dF10PFCClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:dF10PFCClearCounters.setStatus(_B)
class _DF10PFCGlobalEnableTrap_Type(Integer32):defaultValue=0
_DF10PFCGlobalEnableTrap_Type.__name__=_G
_DF10PFCGlobalEnableTrap_Object=MibScalar
dF10PFCGlobalEnableTrap=_DF10PFCGlobalEnableTrap_Object((1,3,6,1,4,1,6027,3,15,3,3,1,4),_DF10PFCGlobalEnableTrap_Type())
dF10PFCGlobalEnableTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10PFCGlobalEnableTrap.setStatus(_B)
_DF10PFCPortTable_Object=MibTable
dF10PFCPortTable=_DF10PFCPortTable_Object((1,3,6,1,4,1,6027,3,15,3,3,2))
if mibBuilder.loadTexts:dF10PFCPortTable.setStatus(_B)
_DF10PFCPortEntry_Object=MibTableRow
dF10PFCPortEntry=_DF10PFCPortEntry_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1))
dF10PFCPortEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:dF10PFCPortEntry.setStatus(_B)
_DF10PFCPortNumber_Type=InterfaceIndex
_DF10PFCPortNumber_Object=MibTableColumn
dF10PFCPortNumber=_DF10PFCPortNumber_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,1),_DF10PFCPortNumber_Type())
dF10PFCPortNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:dF10PFCPortNumber.setStatus(_B)
class _DF10PFCAdminMode_Type(DcbAdminMode):defaultValue=1
_DF10PFCAdminMode_Type.__name__=_O
_DF10PFCAdminMode_Object=MibTableColumn
dF10PFCAdminMode=_DF10PFCAdminMode_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,2),_DF10PFCAdminMode_Type())
dF10PFCAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10PFCAdminMode.setStatus(_B)
_DF10PFCDcbxOperState_Type=DcbState
_DF10PFCDcbxOperState_Object=MibTableColumn
dF10PFCDcbxOperState=_DF10PFCDcbxOperState_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,3),_DF10PFCDcbxOperState_Type())
dF10PFCDcbxOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10PFCDcbxOperState.setStatus(_B)
_DF10PFCDcbxStateMachine_Type=DcbStateMachineType
_DF10PFCDcbxStateMachine_Object=MibTableColumn
dF10PFCDcbxStateMachine=_DF10PFCDcbxStateMachine_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,4),_DF10PFCDcbxStateMachine_Type())
dF10PFCDcbxStateMachine.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10PFCDcbxStateMachine.setStatus(_B)
_DF10PFCOperStatus_Type=EnabledStatus
_DF10PFCOperStatus_Object=MibTableColumn
dF10PFCOperStatus=_DF10PFCOperStatus_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,5),_DF10PFCOperStatus_Type())
dF10PFCOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10PFCOperStatus.setStatus(_B)
class _DF10PFCClearTLVCounters_Type(TruthValue):defaultValue=2
_DF10PFCClearTLVCounters_Type.__name__=_I
_DF10PFCClearTLVCounters_Object=MibTableColumn
dF10PFCClearTLVCounters=_DF10PFCClearTLVCounters_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,6),_DF10PFCClearTLVCounters_Type())
dF10PFCClearTLVCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:dF10PFCClearTLVCounters.setStatus(_B)
_DF10PFCTxTLVCounter_Type=Counter32
_DF10PFCTxTLVCounter_Object=MibTableColumn
dF10PFCTxTLVCounter=_DF10PFCTxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,7),_DF10PFCTxTLVCounter_Type())
dF10PFCTxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10PFCTxTLVCounter.setStatus(_B)
_DF10PFCRxTLVCounter_Type=Counter32
_DF10PFCRxTLVCounter_Object=MibTableColumn
dF10PFCRxTLVCounter=_DF10PFCRxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,8),_DF10PFCRxTLVCounter_Type())
dF10PFCRxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10PFCRxTLVCounter.setStatus(_B)
_DF10PFCRxTLVErrors_Type=Counter32
_DF10PFCRxTLVErrors_Object=MibTableColumn
dF10PFCRxTLVErrors=_DF10PFCRxTLVErrors_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,9),_DF10PFCRxTLVErrors_Type())
dF10PFCRxTLVErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dF10PFCRxTLVErrors.setStatus(_B)
_DF10DcbNotificationObjects_ObjectIdentity=ObjectIdentity
dF10DcbNotificationObjects=_DF10DcbNotificationObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,4))
_DF10DCBTraps_ObjectIdentity=ObjectIdentity
dF10DCBTraps=_DF10DCBTraps_ObjectIdentity((1,3,6,1,4,1,6027,3,15,4,0))
_DF10DCBTrapObjects_ObjectIdentity=ObjectIdentity
dF10DCBTrapObjects=_DF10DCBTrapObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,4,1))
_DF10DcbTrapPortNumber_Type=TruthValue
_DF10DcbTrapPortNumber_Object=MibScalar
dF10DcbTrapPortNumber=_DF10DcbTrapPortNumber_Object((1,3,6,1,4,1,6027,3,15,4,1,1),_DF10DcbTrapPortNumber_Type())
dF10DcbTrapPortNumber.setMaxAccess(_g)
if mibBuilder.loadTexts:dF10DcbTrapPortNumber.setStatus(_B)
_DF10DcbPeerUpStatus_Type=TruthValue
_DF10DcbPeerUpStatus_Object=MibScalar
dF10DcbPeerUpStatus=_DF10DcbPeerUpStatus_Object((1,3,6,1,4,1,6027,3,15,4,1,2),_DF10DcbPeerUpStatus_Type())
dF10DcbPeerUpStatus.setMaxAccess(_g)
if mibBuilder.loadTexts:dF10DcbPeerUpStatus.setStatus(_B)
_DF10DCBMibConformance_ObjectIdentity=ObjectIdentity
dF10DCBMibConformance=_DF10DCBMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,15,5))
_DF10DCBMibCompliances_ObjectIdentity=ObjectIdentity
dF10DCBMibCompliances=_DF10DCBMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,15,5,1))
_DF10DCBMibGroups_ObjectIdentity=ObjectIdentity
dF10DCBMibGroups=_DF10DCBMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,15,5,2))
dF10DCBXPortEntry.registerAugmentions((_A,_h))
dF10DCBXPortStatusEntry.setIndexNames(*dF10DCBXPortEntry.getIndexNames())
dF10DcbSystemObjectGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,1))
dF10DcbSystemObjectGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:dF10DcbSystemObjectGroup.setStatus(_B)
dF10DcbObjectGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,2))
dF10DcbObjectGroup.setObjects(*((_A,_l),(_A,_m)))
if mibBuilder.loadTexts:dF10DcbObjectGroup.setStatus(_F)
dF10DcbxScalarsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,3))
dF10DcbxScalarsGroup.setObjects(*((_A,_n),(_A,_o)))
if mibBuilder.loadTexts:dF10DcbxScalarsGroup.setStatus(_B)
dF10DCBXPortTableGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,4))
dF10DCBXPortTableGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:dF10DCBXPortTableGroup.setStatus(_B)
dF10ETSScalarsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,5))
dF10ETSScalarsGroup.setObjects(*((_A,_A8),(_A,_P),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:dF10ETSScalarsGroup.setStatus(_B)
dF10ETSPortTableGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,6))
dF10ETSPortTableGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:dF10ETSPortTableGroup.setStatus(_B)
dF10PFCScalarsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,7))
dF10PFCScalarsGroup.setObjects(*((_A,_AK),(_A,_S),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:dF10PFCScalarsGroup.setStatus(_B)
dF10PFCPortTableGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,8))
dF10PFCPortTableGroup.setObjects(*((_A,_T),(_A,_U),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:dF10PFCPortTableGroup.setStatus(_B)
dF10DCBNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,9))
dF10DCBNotificationObjectsGroup.setObjects(*((_A,_E),(_A,_M)))
if mibBuilder.loadTexts:dF10DCBNotificationObjectsGroup.setStatus(_B)
dF10ETSModuleStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,1))
dF10ETSModuleStatusTrap.setObjects((_A,_P))
if mibBuilder.loadTexts:dF10ETSModuleStatusTrap.setStatus(_B)
dF10ETSPortAdminStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,2))
dF10ETSPortAdminStatusTrap.setObjects(*((_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:dF10ETSPortAdminStatusTrap.setStatus(_B)
dF10ETSPortPeerStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,3))
dF10ETSPortPeerStatusTrap.setObjects(*((_A,_E),(_A,_M)))
if mibBuilder.loadTexts:dF10ETSPortPeerStatusTrap.setStatus(_B)
dF10ETSPortDcbxOperStateTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,4))
dF10ETSPortDcbxOperStateTrap.setObjects(*((_A,_E),(_A,_R)))
if mibBuilder.loadTexts:dF10ETSPortDcbxOperStateTrap.setStatus(_B)
dF10PFCModuleStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,5))
dF10PFCModuleStatusTrap.setObjects((_A,_S))
if mibBuilder.loadTexts:dF10PFCModuleStatusTrap.setStatus(_B)
dF10PFCPortAdminStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,6))
dF10PFCPortAdminStatusTrap.setObjects(*((_A,_E),(_A,_T)))
if mibBuilder.loadTexts:dF10PFCPortAdminStatusTrap.setStatus(_B)
dF10PFCPortPeerStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,7))
dF10PFCPortPeerStatusTrap.setObjects(*((_A,_E),(_A,_M)))
if mibBuilder.loadTexts:dF10PFCPortPeerStatusTrap.setStatus(_B)
dF10PFCPortDcbxOperStateTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,8))
dF10PFCPortDcbxOperStateTrap.setObjects(*((_A,_E),(_A,_U)))
if mibBuilder.loadTexts:dF10PFCPortDcbxOperStateTrap.setStatus(_B)
dF10DCBNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6027,3,15,5,2,10))
dF10DCBNotificationsGroup.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:dF10DCBNotificationsGroup.setStatus(_B)
dF10DCBMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,6027,3,15,5,1,1))
dF10DCBMibComplianceRev1.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:dF10DCBMibComplianceRev1.setStatus(_B)
dF10DCBMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,15,5,1,2))
dF10DCBMibCompliance.setObjects((_A,_Ak))
if mibBuilder.loadTexts:dF10DCBMibCompliance.setStatus(_F)
mibBuilder.exportSymbols(_A,**{_H:EnabledStatus,_O:DcbAdminMode,'DcbState':DcbState,'DcbStateMachineType':DcbStateMachineType,_X:DcbxPortRole,_L:DcbxVersion,'dF10Dcb':dF10Dcb,'dF10DcbSystem':dF10DcbSystem,_i:dF10DcbPfcMinThreshold,_j:dF10DcbPfcMaxThreshold,_k:dF10DcbMaxPfcProfiles,'dF10DcbObjects':dF10DcbObjects,'dF10DcbPortTable':dF10DcbPortTable,'dF10DcbPortEntry':dF10DcbPortEntry,_V:dF10DcbPortNumber,_l:dF10DcbETSAdminStatus,_m:dF10DcbPFCAdminStatus,'dF10DcbApplicationObjects':dF10DcbApplicationObjects,'dF10DCBXObjects':dF10DCBXObjects,'dF10DCBXScalars':dF10DCBXScalars,_n:dF10DcbxGlobalTraceLevel,_o:dF10DCBXGlobalVersion,'dF10DCBXPortTable':dF10DCBXPortTable,'dF10DCBXPortEntry':dF10DCBXPortEntry,_W:dF10DCBXPortNumber,_p:dF10DCBXAdminStatus,_q:dF10DCBXAutoCfgPortRole,_r:dF10DCBXPortVersion,_s:dF10DCBXPortSupportedTLVs,_t:dF10DCBXPortConfigTLVsTxEnable,'dF10DCBXPortStatusTable':dF10DCBXPortStatusTable,_h:dF10DCBXPortStatusEntry,_u:dF10DCBXPortOperVersion,_v:dF10DCBXPortPeerMACaddress,_w:dF10DCBXPortCfgSource,_x:dF10DCBXOperStatus,_y:dF10DCBXPortMultiplePeerCount,_z:dF10DCBXPortPeerRemovedCount,_A0:dF10DCBXPortPeerOperVersionNum,_A1:dF10DCBXPortPeerMaxVersion,_A2:dF10DCBXPortSeqNum,_A3:dF10DCBXPortAckNum,_A4:dF10DCBXPortPeerRcvdAckNum,_A5:dF10DCBXPortTxCount,_A6:dF10DCBXPortRxCount,_A7:dF10DCBXPortErrorFramesCount,'dF10ETSObjects':dF10ETSObjects,'dF10ETSScalars':dF10ETSScalars,_A8:dF10ETSSystemControl,_P:dF10ETSModuleStatus,_A9:dF10ETSClearCounters,_AA:dF10ETSGlobalEnableTrap,'dF10ETSPortTable':dF10ETSPortTable,'dF10ETSPortEntry':dF10ETSPortEntry,_e:dF10ETSPortNumber,_Q:dF10ETSAdminMode,_R:dF10ETSDcbxOperState,_AB:dF10ETSDcbxStateMachine,_AC:dF10ETSOperStatus,_AD:dF10ETSClearTLVCounters,_AE:dF10ETSConfTxTLVCounter,_AF:dF10ETSConfRxTLVCounter,_AG:dF10ETSConfRxTLVErrors,_AH:dF10ETSRecoTxTLVCounter,_AI:dF10ETSRecoRxTLVCounter,_AJ:dF10ETSRecoRxTLVErrors,'dF10PFCObjects':dF10PFCObjects,'dF10PFCScalars':dF10PFCScalars,_AK:dF10PFCSystemControl,_S:dF10PFCModuleStatus,_AL:dF10PFCClearCounters,_AM:dF10PFCGlobalEnableTrap,'dF10PFCPortTable':dF10PFCPortTable,'dF10PFCPortEntry':dF10PFCPortEntry,_f:dF10PFCPortNumber,_T:dF10PFCAdminMode,_U:dF10PFCDcbxOperState,_AN:dF10PFCDcbxStateMachine,_AO:dF10PFCOperStatus,_AP:dF10PFCClearTLVCounters,_AQ:dF10PFCTxTLVCounter,_AR:dF10PFCRxTLVCounter,_AS:dF10PFCRxTLVErrors,'dF10DcbNotificationObjects':dF10DcbNotificationObjects,'dF10DCBTraps':dF10DCBTraps,_AT:dF10ETSModuleStatusTrap,_AU:dF10ETSPortAdminStatusTrap,_AV:dF10ETSPortPeerStatusTrap,_AW:dF10ETSPortDcbxOperStateTrap,_AX:dF10PFCModuleStatusTrap,_AY:dF10PFCPortAdminStatusTrap,_AZ:dF10PFCPortPeerStatusTrap,_Aa:dF10PFCPortDcbxOperStateTrap,'dF10DCBTrapObjects':dF10DCBTrapObjects,_E:dF10DcbTrapPortNumber,_M:dF10DcbPeerUpStatus,'dF10DCBMibConformance':dF10DCBMibConformance,'dF10DCBMibCompliances':dF10DCBMibCompliances,'dF10DCBMibComplianceRev1':dF10DCBMibComplianceRev1,'dF10DCBMibCompliance':dF10DCBMibCompliance,'dF10DCBMibGroups':dF10DCBMibGroups,_Ab:dF10DcbSystemObjectGroup,_Ak:dF10DcbObjectGroup,_Ac:dF10DcbxScalarsGroup,_Ad:dF10DCBXPortTableGroup,_Ae:dF10ETSScalarsGroup,_Af:dF10ETSPortTableGroup,_Ag:dF10PFCScalarsGroup,_Ah:dF10PFCPortTableGroup,_Ai:dF10DCBNotificationObjectsGroup,_Aj:dF10DCBNotificationsGroup})