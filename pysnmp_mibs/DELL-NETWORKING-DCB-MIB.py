_Ak='dellNetDcbObjectGroup'
_Aj='dellNetDCBNotificationsGroup'
_Ai='dellNetDCBNotificationObjectsGroup'
_Ah='dellNetPFCPortTableGroup'
_Ag='dellNetPFCScalarsGroup'
_Af='dellNetETSPortTableGroup'
_Ae='dellNetETSScalarsGroup'
_Ad='dellNetDCBXPortTableGroup'
_Ac='dellNetDcbxScalarsGroup'
_Ab='dellNetDcbSystemObjectGroup'
_Aa='dellNetPFCPortDcbxOperStateTrap'
_AZ='dellNetPFCPortPeerStatusTrap'
_AY='dellNetPFCPortAdminStatusTrap'
_AX='dellNetPFCModuleStatusTrap'
_AW='dellNetETSPortDcbxOperStateTrap'
_AV='dellNetETSPortPeerStatusTrap'
_AU='dellNetETSPortAdminStatusTrap'
_AT='dellNetETSModuleStatusTrap'
_AS='dellNetPFCRxTLVErrors'
_AR='dellNetPFCRxTLVCounter'
_AQ='dellNetPFCTxTLVCounter'
_AP='dellNetPFCClearTLVCounters'
_AO='dellNetPFCOperStatus'
_AN='dellNetPFCDcbxStateMachine'
_AM='dellNetPFCGlobalEnableTrap'
_AL='dellNetPFCClearCounters'
_AK='dellNetPFCSystemControl'
_AJ='dellNetETSRecoRxTLVErrors'
_AI='dellNetETSRecoRxTLVCounter'
_AH='dellNetETSRecoTxTLVCounter'
_AG='dellNetETSConfRxTLVErrors'
_AF='dellNetETSConfRxTLVCounter'
_AE='dellNetETSConfTxTLVCounter'
_AD='dellNetETSClearTLVCounters'
_AC='dellNetETSOperStatus'
_AB='dellNetETSDcbxStateMachine'
_AA='dellNetETSGlobalEnableTrap'
_A9='dellNetETSClearCounters'
_A8='dellNetETSSystemControl'
_A7='dellNetDCBXPortErrorFramesCount'
_A6='dellNetDCBXPortRxCount'
_A5='dellNetDCBXPortTxCount'
_A4='dellNetDCBXPortPeerRcvdAckNum'
_A3='dellNetDCBXPortAckNum'
_A2='dellNetDCBXPortSeqNum'
_A1='dellNetDCBXPortPeerMaxVersion'
_A0='dellNetDCBXPortPeerOperVersionNum'
_z='dellNetDCBXPortPeerRemovedCount'
_y='dellNetDCBXPortMultiplePeerCount'
_x='dellNetDCBXOperStatus'
_w='dellNetDCBXPortCfgSource'
_v='dellNetDCBXPortPeerMACaddress'
_u='dellNetDCBXPortOperVersion'
_t='dellNetDCBXPortConfigTLVsTxEnable'
_s='dellNetDCBXPortSupportedTLVs'
_r='dellNetDCBXPortVersion'
_q='dellNetDCBXAutoCfgPortRole'
_p='dellNetDCBXAdminStatus'
_o='dellNetDCBXGlobalVersion'
_n='dellNetDcbxGlobalTraceLevel'
_m='dellNetDcbPFCAdminStatus'
_l='dellNetDcbETSAdminStatus'
_k='dellNetDcbMaxPfcProfiles'
_j='dellNetDcbPfcMaxThreshold'
_i='dellNetDcbPfcMinThreshold'
_h='dellNetDCBXPortStatusEntry'
_g='accessible-for-notify'
_f='dellNetPFCPortNumber'
_e='dellNetETSPortNumber'
_d='shutdown'
_c='running'
_b='applicationPriorityISCSI'
_a='applicationPriorityFCOE'
_Z='etsRecom'
_Y='etsConfig'
_X='DcbxPortRole'
_W='dellNetDCBXPortNumber'
_V='dellNetDcbPortNumber'
_U='dellNetPFCDcbxOperState'
_T='dellNetPFCAdminMode'
_S='dellNetPFCModuleStatus'
_R='dellNetETSDcbxOperState'
_Q='dellNetETSAdminMode'
_P='dellNetETSModuleStatus'
_O='DcbAdminMode'
_N='Bits'
_M='dellNetDcbPeerUpStatus'
_L='DcbxVersion'
_K='not-accessible'
_J='Unsigned32'
_I='TruthValue'
_H='EnabledStatus'
_G='Integer32'
_F='obsolete'
_E='dellNetDcbTrapPortNumber'
_D='read-write'
_C='read-only'
_B='current'
_A='DELL-NETWORKING-DCB-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_N,'Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_I)
dellNetDcb=ModuleIdentity((1,3,6,1,4,1,6027,3,15))
if mibBuilder.loadTexts:dellNetDcb.setRevisions(('2012-04-16 00:00','2011-11-24 00:00','2010-09-25 00:00'))
class EnabledStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
class DcbAdminMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
class DcbState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off',0),('init',1),('rxrecommended',2),('internallypropagated',3)))
class DcbStateMachineType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('asymmetric',1),('symmetric',2),('feature',3)))
class DcbxPortRole(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('manual',1),('autoup',2),('autodown',3),('configSource',4)))
class DcbxVersion(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),('ieee',2),('cin',3),('cee',4)))
_DellNetDcbSystem_ObjectIdentity=ObjectIdentity
dellNetDcbSystem=_DellNetDcbSystem_ObjectIdentity((1,3,6,1,4,1,6027,3,15,1))
class _DellNetDcbPfcMinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DellNetDcbPfcMinThreshold_Type.__name__=_J
_DellNetDcbPfcMinThreshold_Object=MibScalar
dellNetDcbPfcMinThreshold=_DellNetDcbPfcMinThreshold_Object((1,3,6,1,4,1,6027,3,15,1,1),_DellNetDcbPfcMinThreshold_Type())
dellNetDcbPfcMinThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDcbPfcMinThreshold.setStatus(_B)
class _DellNetDcbPfcMaxThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DellNetDcbPfcMaxThreshold_Type.__name__=_J
_DellNetDcbPfcMaxThreshold_Object=MibScalar
dellNetDcbPfcMaxThreshold=_DellNetDcbPfcMaxThreshold_Object((1,3,6,1,4,1,6027,3,15,1,2),_DellNetDcbPfcMaxThreshold_Type())
dellNetDcbPfcMaxThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDcbPfcMaxThreshold.setStatus(_B)
class _DellNetDcbMaxPfcProfiles_Type(Unsigned32):defaultValue=256;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_DellNetDcbMaxPfcProfiles_Type.__name__=_J
_DellNetDcbMaxPfcProfiles_Object=MibScalar
dellNetDcbMaxPfcProfiles=_DellNetDcbMaxPfcProfiles_Object((1,3,6,1,4,1,6027,3,15,1,3),_DellNetDcbMaxPfcProfiles_Type())
dellNetDcbMaxPfcProfiles.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDcbMaxPfcProfiles.setStatus(_B)
_DellNetDcbObjects_ObjectIdentity=ObjectIdentity
dellNetDcbObjects=_DellNetDcbObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,2))
_DellNetDcbPortTable_Object=MibTable
dellNetDcbPortTable=_DellNetDcbPortTable_Object((1,3,6,1,4,1,6027,3,15,2,1))
if mibBuilder.loadTexts:dellNetDcbPortTable.setStatus(_F)
_DellNetDcbPortEntry_Object=MibTableRow
dellNetDcbPortEntry=_DellNetDcbPortEntry_Object((1,3,6,1,4,1,6027,3,15,2,1,1))
dellNetDcbPortEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:dellNetDcbPortEntry.setStatus(_F)
_DellNetDcbPortNumber_Type=InterfaceIndex
_DellNetDcbPortNumber_Object=MibTableColumn
dellNetDcbPortNumber=_DellNetDcbPortNumber_Object((1,3,6,1,4,1,6027,3,15,2,1,1,1),_DellNetDcbPortNumber_Type())
dellNetDcbPortNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:dellNetDcbPortNumber.setStatus(_F)
class _DellNetDcbETSAdminStatus_Type(EnabledStatus):defaultValue=1
_DellNetDcbETSAdminStatus_Type.__name__=_H
_DellNetDcbETSAdminStatus_Object=MibTableColumn
dellNetDcbETSAdminStatus=_DellNetDcbETSAdminStatus_Object((1,3,6,1,4,1,6027,3,15,2,1,1,2),_DellNetDcbETSAdminStatus_Type())
dellNetDcbETSAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDcbETSAdminStatus.setStatus(_F)
class _DellNetDcbPFCAdminStatus_Type(EnabledStatus):defaultValue=1
_DellNetDcbPFCAdminStatus_Type.__name__=_H
_DellNetDcbPFCAdminStatus_Object=MibTableColumn
dellNetDcbPFCAdminStatus=_DellNetDcbPFCAdminStatus_Object((1,3,6,1,4,1,6027,3,15,2,1,1,3),_DellNetDcbPFCAdminStatus_Type())
dellNetDcbPFCAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDcbPFCAdminStatus.setStatus(_F)
_DellNetDcbApplicationObjects_ObjectIdentity=ObjectIdentity
dellNetDcbApplicationObjects=_DellNetDcbApplicationObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3))
_DellNetDCBXObjects_ObjectIdentity=ObjectIdentity
dellNetDCBXObjects=_DellNetDCBXObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,1))
_DellNetDCBXScalars_ObjectIdentity=ObjectIdentity
dellNetDCBXScalars=_DellNetDCBXScalars_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,1,1))
_DellNetDcbxGlobalTraceLevel_Type=Integer32
_DellNetDcbxGlobalTraceLevel_Object=MibScalar
dellNetDcbxGlobalTraceLevel=_DellNetDcbxGlobalTraceLevel_Object((1,3,6,1,4,1,6027,3,15,3,1,1,1),_DellNetDcbxGlobalTraceLevel_Type())
dellNetDcbxGlobalTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetDcbxGlobalTraceLevel.setStatus(_B)
class _DellNetDCBXGlobalVersion_Type(DcbxVersion):defaultValue=1
_DellNetDCBXGlobalVersion_Type.__name__=_L
_DellNetDCBXGlobalVersion_Object=MibScalar
dellNetDCBXGlobalVersion=_DellNetDCBXGlobalVersion_Object((1,3,6,1,4,1,6027,3,15,3,1,1,2),_DellNetDCBXGlobalVersion_Type())
dellNetDCBXGlobalVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetDCBXGlobalVersion.setStatus(_B)
_DellNetDCBXPortTable_Object=MibTable
dellNetDCBXPortTable=_DellNetDCBXPortTable_Object((1,3,6,1,4,1,6027,3,15,3,1,2))
if mibBuilder.loadTexts:dellNetDCBXPortTable.setStatus(_B)
_DellNetDCBXPortEntry_Object=MibTableRow
dellNetDCBXPortEntry=_DellNetDCBXPortEntry_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1))
dellNetDCBXPortEntry.setIndexNames((0,_A,_W))
if mibBuilder.loadTexts:dellNetDCBXPortEntry.setStatus(_B)
_DellNetDCBXPortNumber_Type=InterfaceIndex
_DellNetDCBXPortNumber_Object=MibTableColumn
dellNetDCBXPortNumber=_DellNetDCBXPortNumber_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,1),_DellNetDCBXPortNumber_Type())
dellNetDCBXPortNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:dellNetDCBXPortNumber.setStatus(_B)
class _DellNetDCBXAdminStatus_Type(EnabledStatus):defaultValue=1
_DellNetDCBXAdminStatus_Type.__name__=_H
_DellNetDCBXAdminStatus_Object=MibTableColumn
dellNetDCBXAdminStatus=_DellNetDCBXAdminStatus_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,2),_DellNetDCBXAdminStatus_Type())
dellNetDCBXAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXAdminStatus.setStatus(_B)
class _DellNetDCBXAutoCfgPortRole_Type(DcbxPortRole):defaultValue=1
_DellNetDCBXAutoCfgPortRole_Type.__name__=_X
_DellNetDCBXAutoCfgPortRole_Object=MibTableColumn
dellNetDCBXAutoCfgPortRole=_DellNetDCBXAutoCfgPortRole_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,3),_DellNetDCBXAutoCfgPortRole_Type())
dellNetDCBXAutoCfgPortRole.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetDCBXAutoCfgPortRole.setStatus(_B)
class _DellNetDCBXPortVersion_Type(DcbxVersion):defaultValue=1
_DellNetDCBXPortVersion_Type.__name__=_L
_DellNetDCBXPortVersion_Object=MibTableColumn
dellNetDCBXPortVersion=_DellNetDCBXPortVersion_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,4),_DellNetDCBXPortVersion_Type())
dellNetDCBXPortVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetDCBXPortVersion.setStatus(_B)
class _DellNetDCBXPortSupportedTLVs_Type(Bits):namedValues=NamedValues(*(('pfc',0),(_Y,1),(_Z,2),(_a,3),(_b,4)))
_DellNetDCBXPortSupportedTLVs_Type.__name__=_N
_DellNetDCBXPortSupportedTLVs_Object=MibTableColumn
dellNetDCBXPortSupportedTLVs=_DellNetDCBXPortSupportedTLVs_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,5),_DellNetDCBXPortSupportedTLVs_Type())
dellNetDCBXPortSupportedTLVs.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortSupportedTLVs.setStatus(_B)
class _DellNetDCBXPortConfigTLVsTxEnable_Type(Bits):namedValues=NamedValues(*(('pfc',0),(_Y,1),(_Z,2),(_a,3),(_b,4)))
_DellNetDCBXPortConfigTLVsTxEnable_Type.__name__=_N
_DellNetDCBXPortConfigTLVsTxEnable_Object=MibTableColumn
dellNetDCBXPortConfigTLVsTxEnable=_DellNetDCBXPortConfigTLVsTxEnable_Object((1,3,6,1,4,1,6027,3,15,3,1,2,1,6),_DellNetDCBXPortConfigTLVsTxEnable_Type())
dellNetDCBXPortConfigTLVsTxEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetDCBXPortConfigTLVsTxEnable.setStatus(_B)
_DellNetDCBXPortStatusTable_Object=MibTable
dellNetDCBXPortStatusTable=_DellNetDCBXPortStatusTable_Object((1,3,6,1,4,1,6027,3,15,3,1,3))
if mibBuilder.loadTexts:dellNetDCBXPortStatusTable.setStatus(_B)
_DellNetDCBXPortStatusEntry_Object=MibTableRow
dellNetDCBXPortStatusEntry=_DellNetDCBXPortStatusEntry_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1))
if mibBuilder.loadTexts:dellNetDCBXPortStatusEntry.setStatus(_B)
class _DellNetDCBXPortOperVersion_Type(DcbxVersion):defaultValue=1
_DellNetDCBXPortOperVersion_Type.__name__=_L
_DellNetDCBXPortOperVersion_Object=MibTableColumn
dellNetDCBXPortOperVersion=_DellNetDCBXPortOperVersion_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,2),_DellNetDCBXPortOperVersion_Type())
dellNetDCBXPortOperVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortOperVersion.setStatus(_B)
_DellNetDCBXPortPeerMACaddress_Type=MacAddress
_DellNetDCBXPortPeerMACaddress_Object=MibTableColumn
dellNetDCBXPortPeerMACaddress=_DellNetDCBXPortPeerMACaddress_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,3),_DellNetDCBXPortPeerMACaddress_Type())
dellNetDCBXPortPeerMACaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortPeerMACaddress.setStatus(_B)
class _DellNetDCBXPortCfgSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_DellNetDCBXPortCfgSource_Type.__name__=_G
_DellNetDCBXPortCfgSource_Object=MibTableColumn
dellNetDCBXPortCfgSource=_DellNetDCBXPortCfgSource_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,4),_DellNetDCBXPortCfgSource_Type())
dellNetDCBXPortCfgSource.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortCfgSource.setStatus(_B)
_DellNetDCBXOperStatus_Type=EnabledStatus
_DellNetDCBXOperStatus_Object=MibTableColumn
dellNetDCBXOperStatus=_DellNetDCBXOperStatus_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,5),_DellNetDCBXOperStatus_Type())
dellNetDCBXOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXOperStatus.setStatus(_B)
_DellNetDCBXPortMultiplePeerCount_Type=Counter32
_DellNetDCBXPortMultiplePeerCount_Object=MibTableColumn
dellNetDCBXPortMultiplePeerCount=_DellNetDCBXPortMultiplePeerCount_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,6),_DellNetDCBXPortMultiplePeerCount_Type())
dellNetDCBXPortMultiplePeerCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortMultiplePeerCount.setStatus(_B)
_DellNetDCBXPortPeerRemovedCount_Type=Counter32
_DellNetDCBXPortPeerRemovedCount_Object=MibTableColumn
dellNetDCBXPortPeerRemovedCount=_DellNetDCBXPortPeerRemovedCount_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,7),_DellNetDCBXPortPeerRemovedCount_Type())
dellNetDCBXPortPeerRemovedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortPeerRemovedCount.setStatus(_B)
_DellNetDCBXPortPeerOperVersionNum_Type=Unsigned32
_DellNetDCBXPortPeerOperVersionNum_Object=MibTableColumn
dellNetDCBXPortPeerOperVersionNum=_DellNetDCBXPortPeerOperVersionNum_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,8),_DellNetDCBXPortPeerOperVersionNum_Type())
dellNetDCBXPortPeerOperVersionNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortPeerOperVersionNum.setStatus(_B)
_DellNetDCBXPortPeerMaxVersion_Type=Unsigned32
_DellNetDCBXPortPeerMaxVersion_Object=MibTableColumn
dellNetDCBXPortPeerMaxVersion=_DellNetDCBXPortPeerMaxVersion_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,9),_DellNetDCBXPortPeerMaxVersion_Type())
dellNetDCBXPortPeerMaxVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortPeerMaxVersion.setStatus(_B)
_DellNetDCBXPortSeqNum_Type=Unsigned32
_DellNetDCBXPortSeqNum_Object=MibTableColumn
dellNetDCBXPortSeqNum=_DellNetDCBXPortSeqNum_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,10),_DellNetDCBXPortSeqNum_Type())
dellNetDCBXPortSeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortSeqNum.setStatus(_B)
_DellNetDCBXPortAckNum_Type=Unsigned32
_DellNetDCBXPortAckNum_Object=MibTableColumn
dellNetDCBXPortAckNum=_DellNetDCBXPortAckNum_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,11),_DellNetDCBXPortAckNum_Type())
dellNetDCBXPortAckNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortAckNum.setStatus(_B)
_DellNetDCBXPortPeerRcvdAckNum_Type=Unsigned32
_DellNetDCBXPortPeerRcvdAckNum_Object=MibTableColumn
dellNetDCBXPortPeerRcvdAckNum=_DellNetDCBXPortPeerRcvdAckNum_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,12),_DellNetDCBXPortPeerRcvdAckNum_Type())
dellNetDCBXPortPeerRcvdAckNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortPeerRcvdAckNum.setStatus(_B)
_DellNetDCBXPortTxCount_Type=Counter32
_DellNetDCBXPortTxCount_Object=MibTableColumn
dellNetDCBXPortTxCount=_DellNetDCBXPortTxCount_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,13),_DellNetDCBXPortTxCount_Type())
dellNetDCBXPortTxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortTxCount.setStatus(_B)
_DellNetDCBXPortRxCount_Type=Counter32
_DellNetDCBXPortRxCount_Object=MibTableColumn
dellNetDCBXPortRxCount=_DellNetDCBXPortRxCount_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,14),_DellNetDCBXPortRxCount_Type())
dellNetDCBXPortRxCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortRxCount.setStatus(_B)
_DellNetDCBXPortErrorFramesCount_Type=Counter32
_DellNetDCBXPortErrorFramesCount_Object=MibTableColumn
dellNetDCBXPortErrorFramesCount=_DellNetDCBXPortErrorFramesCount_Object((1,3,6,1,4,1,6027,3,15,3,1,3,1,15),_DellNetDCBXPortErrorFramesCount_Type())
dellNetDCBXPortErrorFramesCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetDCBXPortErrorFramesCount.setStatus(_B)
_DellNetETSObjects_ObjectIdentity=ObjectIdentity
dellNetETSObjects=_DellNetETSObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,2))
_DellNetETSScalars_ObjectIdentity=ObjectIdentity
dellNetETSScalars=_DellNetETSScalars_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,2,1))
class _DellNetETSSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_DellNetETSSystemControl_Type.__name__=_G
_DellNetETSSystemControl_Object=MibScalar
dellNetETSSystemControl=_DellNetETSSystemControl_Object((1,3,6,1,4,1,6027,3,15,3,2,1,1),_DellNetETSSystemControl_Type())
dellNetETSSystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSSystemControl.setStatus(_B)
class _DellNetETSModuleStatus_Type(EnabledStatus):defaultValue=1
_DellNetETSModuleStatus_Type.__name__=_H
_DellNetETSModuleStatus_Object=MibScalar
dellNetETSModuleStatus=_DellNetETSModuleStatus_Object((1,3,6,1,4,1,6027,3,15,3,2,1,2),_DellNetETSModuleStatus_Type())
dellNetETSModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSModuleStatus.setStatus(_B)
class _DellNetETSClearCounters_Type(TruthValue):defaultValue=2
_DellNetETSClearCounters_Type.__name__=_I
_DellNetETSClearCounters_Object=MibScalar
dellNetETSClearCounters=_DellNetETSClearCounters_Object((1,3,6,1,4,1,6027,3,15,3,2,1,3),_DellNetETSClearCounters_Type())
dellNetETSClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetETSClearCounters.setStatus(_B)
class _DellNetETSGlobalEnableTrap_Type(Integer32):defaultValue=0
_DellNetETSGlobalEnableTrap_Type.__name__=_G
_DellNetETSGlobalEnableTrap_Object=MibScalar
dellNetETSGlobalEnableTrap=_DellNetETSGlobalEnableTrap_Object((1,3,6,1,4,1,6027,3,15,3,2,1,4),_DellNetETSGlobalEnableTrap_Type())
dellNetETSGlobalEnableTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSGlobalEnableTrap.setStatus(_B)
_DellNetETSPortTable_Object=MibTable
dellNetETSPortTable=_DellNetETSPortTable_Object((1,3,6,1,4,1,6027,3,15,3,2,2))
if mibBuilder.loadTexts:dellNetETSPortTable.setStatus(_B)
_DellNetETSPortEntry_Object=MibTableRow
dellNetETSPortEntry=_DellNetETSPortEntry_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1))
dellNetETSPortEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:dellNetETSPortEntry.setStatus(_B)
_DellNetETSPortNumber_Type=InterfaceIndex
_DellNetETSPortNumber_Object=MibTableColumn
dellNetETSPortNumber=_DellNetETSPortNumber_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,1),_DellNetETSPortNumber_Type())
dellNetETSPortNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:dellNetETSPortNumber.setStatus(_B)
class _DellNetETSAdminMode_Type(DcbAdminMode):defaultValue=1
_DellNetETSAdminMode_Type.__name__=_O
_DellNetETSAdminMode_Object=MibTableColumn
dellNetETSAdminMode=_DellNetETSAdminMode_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,2),_DellNetETSAdminMode_Type())
dellNetETSAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSAdminMode.setStatus(_B)
_DellNetETSDcbxOperState_Type=DcbState
_DellNetETSDcbxOperState_Object=MibTableColumn
dellNetETSDcbxOperState=_DellNetETSDcbxOperState_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,3),_DellNetETSDcbxOperState_Type())
dellNetETSDcbxOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSDcbxOperState.setStatus(_B)
_DellNetETSDcbxStateMachine_Type=DcbStateMachineType
_DellNetETSDcbxStateMachine_Object=MibTableColumn
dellNetETSDcbxStateMachine=_DellNetETSDcbxStateMachine_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,4),_DellNetETSDcbxStateMachine_Type())
dellNetETSDcbxStateMachine.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSDcbxStateMachine.setStatus(_B)
_DellNetETSOperStatus_Type=EnabledStatus
_DellNetETSOperStatus_Object=MibTableColumn
dellNetETSOperStatus=_DellNetETSOperStatus_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,5),_DellNetETSOperStatus_Type())
dellNetETSOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSOperStatus.setStatus(_B)
class _DellNetETSClearTLVCounters_Type(TruthValue):defaultValue=2
_DellNetETSClearTLVCounters_Type.__name__=_I
_DellNetETSClearTLVCounters_Object=MibTableColumn
dellNetETSClearTLVCounters=_DellNetETSClearTLVCounters_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,6),_DellNetETSClearTLVCounters_Type())
dellNetETSClearTLVCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetETSClearTLVCounters.setStatus(_B)
_DellNetETSConfTxTLVCounter_Type=Counter32
_DellNetETSConfTxTLVCounter_Object=MibTableColumn
dellNetETSConfTxTLVCounter=_DellNetETSConfTxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,7),_DellNetETSConfTxTLVCounter_Type())
dellNetETSConfTxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSConfTxTLVCounter.setStatus(_B)
_DellNetETSConfRxTLVCounter_Type=Counter32
_DellNetETSConfRxTLVCounter_Object=MibTableColumn
dellNetETSConfRxTLVCounter=_DellNetETSConfRxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,8),_DellNetETSConfRxTLVCounter_Type())
dellNetETSConfRxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSConfRxTLVCounter.setStatus(_B)
_DellNetETSConfRxTLVErrors_Type=Counter32
_DellNetETSConfRxTLVErrors_Object=MibTableColumn
dellNetETSConfRxTLVErrors=_DellNetETSConfRxTLVErrors_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,9),_DellNetETSConfRxTLVErrors_Type())
dellNetETSConfRxTLVErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSConfRxTLVErrors.setStatus(_B)
_DellNetETSRecoTxTLVCounter_Type=Counter32
_DellNetETSRecoTxTLVCounter_Object=MibTableColumn
dellNetETSRecoTxTLVCounter=_DellNetETSRecoTxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,10),_DellNetETSRecoTxTLVCounter_Type())
dellNetETSRecoTxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSRecoTxTLVCounter.setStatus(_B)
_DellNetETSRecoRxTLVCounter_Type=Counter32
_DellNetETSRecoRxTLVCounter_Object=MibTableColumn
dellNetETSRecoRxTLVCounter=_DellNetETSRecoRxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,11),_DellNetETSRecoRxTLVCounter_Type())
dellNetETSRecoRxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSRecoRxTLVCounter.setStatus(_B)
_DellNetETSRecoRxTLVErrors_Type=Counter32
_DellNetETSRecoRxTLVErrors_Object=MibTableColumn
dellNetETSRecoRxTLVErrors=_DellNetETSRecoRxTLVErrors_Object((1,3,6,1,4,1,6027,3,15,3,2,2,1,12),_DellNetETSRecoRxTLVErrors_Type())
dellNetETSRecoRxTLVErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetETSRecoRxTLVErrors.setStatus(_B)
_DellNetPFCObjects_ObjectIdentity=ObjectIdentity
dellNetPFCObjects=_DellNetPFCObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,3))
_DellNetPFCScalars_ObjectIdentity=ObjectIdentity
dellNetPFCScalars=_DellNetPFCScalars_ObjectIdentity((1,3,6,1,4,1,6027,3,15,3,3,1))
class _DellNetPFCSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_DellNetPFCSystemControl_Type.__name__=_G
_DellNetPFCSystemControl_Object=MibScalar
dellNetPFCSystemControl=_DellNetPFCSystemControl_Object((1,3,6,1,4,1,6027,3,15,3,3,1,1),_DellNetPFCSystemControl_Type())
dellNetPFCSystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPFCSystemControl.setStatus(_B)
class _DellNetPFCModuleStatus_Type(EnabledStatus):defaultValue=1
_DellNetPFCModuleStatus_Type.__name__=_H
_DellNetPFCModuleStatus_Object=MibScalar
dellNetPFCModuleStatus=_DellNetPFCModuleStatus_Object((1,3,6,1,4,1,6027,3,15,3,3,1,2),_DellNetPFCModuleStatus_Type())
dellNetPFCModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPFCModuleStatus.setStatus(_B)
class _DellNetPFCClearCounters_Type(TruthValue):defaultValue=2
_DellNetPFCClearCounters_Type.__name__=_I
_DellNetPFCClearCounters_Object=MibScalar
dellNetPFCClearCounters=_DellNetPFCClearCounters_Object((1,3,6,1,4,1,6027,3,15,3,3,1,3),_DellNetPFCClearCounters_Type())
dellNetPFCClearCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetPFCClearCounters.setStatus(_B)
class _DellNetPFCGlobalEnableTrap_Type(Integer32):defaultValue=0
_DellNetPFCGlobalEnableTrap_Type.__name__=_G
_DellNetPFCGlobalEnableTrap_Object=MibScalar
dellNetPFCGlobalEnableTrap=_DellNetPFCGlobalEnableTrap_Object((1,3,6,1,4,1,6027,3,15,3,3,1,4),_DellNetPFCGlobalEnableTrap_Type())
dellNetPFCGlobalEnableTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPFCGlobalEnableTrap.setStatus(_B)
_DellNetPFCPortTable_Object=MibTable
dellNetPFCPortTable=_DellNetPFCPortTable_Object((1,3,6,1,4,1,6027,3,15,3,3,2))
if mibBuilder.loadTexts:dellNetPFCPortTable.setStatus(_B)
_DellNetPFCPortEntry_Object=MibTableRow
dellNetPFCPortEntry=_DellNetPFCPortEntry_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1))
dellNetPFCPortEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:dellNetPFCPortEntry.setStatus(_B)
_DellNetPFCPortNumber_Type=InterfaceIndex
_DellNetPFCPortNumber_Object=MibTableColumn
dellNetPFCPortNumber=_DellNetPFCPortNumber_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,1),_DellNetPFCPortNumber_Type())
dellNetPFCPortNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:dellNetPFCPortNumber.setStatus(_B)
class _DellNetPFCAdminMode_Type(DcbAdminMode):defaultValue=1
_DellNetPFCAdminMode_Type.__name__=_O
_DellNetPFCAdminMode_Object=MibTableColumn
dellNetPFCAdminMode=_DellNetPFCAdminMode_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,2),_DellNetPFCAdminMode_Type())
dellNetPFCAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPFCAdminMode.setStatus(_B)
_DellNetPFCDcbxOperState_Type=DcbState
_DellNetPFCDcbxOperState_Object=MibTableColumn
dellNetPFCDcbxOperState=_DellNetPFCDcbxOperState_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,3),_DellNetPFCDcbxOperState_Type())
dellNetPFCDcbxOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPFCDcbxOperState.setStatus(_B)
_DellNetPFCDcbxStateMachine_Type=DcbStateMachineType
_DellNetPFCDcbxStateMachine_Object=MibTableColumn
dellNetPFCDcbxStateMachine=_DellNetPFCDcbxStateMachine_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,4),_DellNetPFCDcbxStateMachine_Type())
dellNetPFCDcbxStateMachine.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPFCDcbxStateMachine.setStatus(_B)
_DellNetPFCOperStatus_Type=EnabledStatus
_DellNetPFCOperStatus_Object=MibTableColumn
dellNetPFCOperStatus=_DellNetPFCOperStatus_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,5),_DellNetPFCOperStatus_Type())
dellNetPFCOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPFCOperStatus.setStatus(_B)
class _DellNetPFCClearTLVCounters_Type(TruthValue):defaultValue=2
_DellNetPFCClearTLVCounters_Type.__name__=_I
_DellNetPFCClearTLVCounters_Object=MibTableColumn
dellNetPFCClearTLVCounters=_DellNetPFCClearTLVCounters_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,6),_DellNetPFCClearTLVCounters_Type())
dellNetPFCClearTLVCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetPFCClearTLVCounters.setStatus(_B)
_DellNetPFCTxTLVCounter_Type=Counter32
_DellNetPFCTxTLVCounter_Object=MibTableColumn
dellNetPFCTxTLVCounter=_DellNetPFCTxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,7),_DellNetPFCTxTLVCounter_Type())
dellNetPFCTxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPFCTxTLVCounter.setStatus(_B)
_DellNetPFCRxTLVCounter_Type=Counter32
_DellNetPFCRxTLVCounter_Object=MibTableColumn
dellNetPFCRxTLVCounter=_DellNetPFCRxTLVCounter_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,8),_DellNetPFCRxTLVCounter_Type())
dellNetPFCRxTLVCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPFCRxTLVCounter.setStatus(_B)
_DellNetPFCRxTLVErrors_Type=Counter32
_DellNetPFCRxTLVErrors_Object=MibTableColumn
dellNetPFCRxTLVErrors=_DellNetPFCRxTLVErrors_Object((1,3,6,1,4,1,6027,3,15,3,3,2,1,9),_DellNetPFCRxTLVErrors_Type())
dellNetPFCRxTLVErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetPFCRxTLVErrors.setStatus(_B)
_DellNetDcbNotificationObjects_ObjectIdentity=ObjectIdentity
dellNetDcbNotificationObjects=_DellNetDcbNotificationObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,4))
_DellNetDCBTraps_ObjectIdentity=ObjectIdentity
dellNetDCBTraps=_DellNetDCBTraps_ObjectIdentity((1,3,6,1,4,1,6027,3,15,4,0))
_DellNetDCBTrapObjects_ObjectIdentity=ObjectIdentity
dellNetDCBTrapObjects=_DellNetDCBTrapObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,15,4,1))
_DellNetDcbTrapPortNumber_Type=TruthValue
_DellNetDcbTrapPortNumber_Object=MibScalar
dellNetDcbTrapPortNumber=_DellNetDcbTrapPortNumber_Object((1,3,6,1,4,1,6027,3,15,4,1,1),_DellNetDcbTrapPortNumber_Type())
dellNetDcbTrapPortNumber.setMaxAccess(_g)
if mibBuilder.loadTexts:dellNetDcbTrapPortNumber.setStatus(_B)
_DellNetDcbPeerUpStatus_Type=TruthValue
_DellNetDcbPeerUpStatus_Object=MibScalar
dellNetDcbPeerUpStatus=_DellNetDcbPeerUpStatus_Object((1,3,6,1,4,1,6027,3,15,4,1,2),_DellNetDcbPeerUpStatus_Type())
dellNetDcbPeerUpStatus.setMaxAccess(_g)
if mibBuilder.loadTexts:dellNetDcbPeerUpStatus.setStatus(_B)
_DellNetDCBMibConformance_ObjectIdentity=ObjectIdentity
dellNetDCBMibConformance=_DellNetDCBMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,15,5))
_DellNetDCBMibCompliances_ObjectIdentity=ObjectIdentity
dellNetDCBMibCompliances=_DellNetDCBMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,15,5,1))
_DellNetDCBMibGroups_ObjectIdentity=ObjectIdentity
dellNetDCBMibGroups=_DellNetDCBMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,15,5,2))
dellNetDCBXPortEntry.registerAugmentions((_A,_h))
dellNetDCBXPortStatusEntry.setIndexNames(*dellNetDCBXPortEntry.getIndexNames())
dellNetDcbSystemObjectGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,1))
dellNetDcbSystemObjectGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:dellNetDcbSystemObjectGroup.setStatus(_B)
dellNetDcbObjectGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,2))
dellNetDcbObjectGroup.setObjects(*((_A,_l),(_A,_m)))
if mibBuilder.loadTexts:dellNetDcbObjectGroup.setStatus(_F)
dellNetDcbxScalarsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,3))
dellNetDcbxScalarsGroup.setObjects(*((_A,_n),(_A,_o)))
if mibBuilder.loadTexts:dellNetDcbxScalarsGroup.setStatus(_B)
dellNetDCBXPortTableGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,4))
dellNetDCBXPortTableGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:dellNetDCBXPortTableGroup.setStatus(_B)
dellNetETSScalarsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,5))
dellNetETSScalarsGroup.setObjects(*((_A,_A8),(_A,_P),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:dellNetETSScalarsGroup.setStatus(_B)
dellNetETSPortTableGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,6))
dellNetETSPortTableGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:dellNetETSPortTableGroup.setStatus(_B)
dellNetPFCScalarsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,7))
dellNetPFCScalarsGroup.setObjects(*((_A,_AK),(_A,_S),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:dellNetPFCScalarsGroup.setStatus(_B)
dellNetPFCPortTableGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,8))
dellNetPFCPortTableGroup.setObjects(*((_A,_T),(_A,_U),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:dellNetPFCPortTableGroup.setStatus(_B)
dellNetDCBNotificationObjectsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,15,5,2,9))
dellNetDCBNotificationObjectsGroup.setObjects(*((_A,_E),(_A,_M)))
if mibBuilder.loadTexts:dellNetDCBNotificationObjectsGroup.setStatus(_B)
dellNetETSModuleStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,1))
dellNetETSModuleStatusTrap.setObjects((_A,_P))
if mibBuilder.loadTexts:dellNetETSModuleStatusTrap.setStatus(_B)
dellNetETSPortAdminStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,2))
dellNetETSPortAdminStatusTrap.setObjects(*((_A,_E),(_A,_Q)))
if mibBuilder.loadTexts:dellNetETSPortAdminStatusTrap.setStatus(_B)
dellNetETSPortPeerStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,3))
dellNetETSPortPeerStatusTrap.setObjects(*((_A,_E),(_A,_M)))
if mibBuilder.loadTexts:dellNetETSPortPeerStatusTrap.setStatus(_B)
dellNetETSPortDcbxOperStateTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,4))
dellNetETSPortDcbxOperStateTrap.setObjects(*((_A,_E),(_A,_R)))
if mibBuilder.loadTexts:dellNetETSPortDcbxOperStateTrap.setStatus(_B)
dellNetPFCModuleStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,5))
dellNetPFCModuleStatusTrap.setObjects((_A,_S))
if mibBuilder.loadTexts:dellNetPFCModuleStatusTrap.setStatus(_B)
dellNetPFCPortAdminStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,6))
dellNetPFCPortAdminStatusTrap.setObjects(*((_A,_E),(_A,_T)))
if mibBuilder.loadTexts:dellNetPFCPortAdminStatusTrap.setStatus(_B)
dellNetPFCPortPeerStatusTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,7))
dellNetPFCPortPeerStatusTrap.setObjects(*((_A,_E),(_A,_M)))
if mibBuilder.loadTexts:dellNetPFCPortPeerStatusTrap.setStatus(_B)
dellNetPFCPortDcbxOperStateTrap=NotificationType((1,3,6,1,4,1,6027,3,15,4,0,8))
dellNetPFCPortDcbxOperStateTrap.setObjects(*((_A,_E),(_A,_U)))
if mibBuilder.loadTexts:dellNetPFCPortDcbxOperStateTrap.setStatus(_B)
dellNetDCBNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6027,3,15,5,2,10))
dellNetDCBNotificationsGroup.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:dellNetDCBNotificationsGroup.setStatus(_B)
dellNetDCBMibComplianceRev1=ModuleCompliance((1,3,6,1,4,1,6027,3,15,5,1,1))
dellNetDCBMibComplianceRev1.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:dellNetDCBMibComplianceRev1.setStatus(_B)
dellNetDCBMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,15,5,1,2))
dellNetDCBMibCompliance.setObjects((_A,_Ak))
if mibBuilder.loadTexts:dellNetDCBMibCompliance.setStatus(_F)
mibBuilder.exportSymbols(_A,**{_H:EnabledStatus,_O:DcbAdminMode,'DcbState':DcbState,'DcbStateMachineType':DcbStateMachineType,_X:DcbxPortRole,_L:DcbxVersion,'dellNetDcb':dellNetDcb,'dellNetDcbSystem':dellNetDcbSystem,_i:dellNetDcbPfcMinThreshold,_j:dellNetDcbPfcMaxThreshold,_k:dellNetDcbMaxPfcProfiles,'dellNetDcbObjects':dellNetDcbObjects,'dellNetDcbPortTable':dellNetDcbPortTable,'dellNetDcbPortEntry':dellNetDcbPortEntry,_V:dellNetDcbPortNumber,_l:dellNetDcbETSAdminStatus,_m:dellNetDcbPFCAdminStatus,'dellNetDcbApplicationObjects':dellNetDcbApplicationObjects,'dellNetDCBXObjects':dellNetDCBXObjects,'dellNetDCBXScalars':dellNetDCBXScalars,_n:dellNetDcbxGlobalTraceLevel,_o:dellNetDCBXGlobalVersion,'dellNetDCBXPortTable':dellNetDCBXPortTable,'dellNetDCBXPortEntry':dellNetDCBXPortEntry,_W:dellNetDCBXPortNumber,_p:dellNetDCBXAdminStatus,_q:dellNetDCBXAutoCfgPortRole,_r:dellNetDCBXPortVersion,_s:dellNetDCBXPortSupportedTLVs,_t:dellNetDCBXPortConfigTLVsTxEnable,'dellNetDCBXPortStatusTable':dellNetDCBXPortStatusTable,_h:dellNetDCBXPortStatusEntry,_u:dellNetDCBXPortOperVersion,_v:dellNetDCBXPortPeerMACaddress,_w:dellNetDCBXPortCfgSource,_x:dellNetDCBXOperStatus,_y:dellNetDCBXPortMultiplePeerCount,_z:dellNetDCBXPortPeerRemovedCount,_A0:dellNetDCBXPortPeerOperVersionNum,_A1:dellNetDCBXPortPeerMaxVersion,_A2:dellNetDCBXPortSeqNum,_A3:dellNetDCBXPortAckNum,_A4:dellNetDCBXPortPeerRcvdAckNum,_A5:dellNetDCBXPortTxCount,_A6:dellNetDCBXPortRxCount,_A7:dellNetDCBXPortErrorFramesCount,'dellNetETSObjects':dellNetETSObjects,'dellNetETSScalars':dellNetETSScalars,_A8:dellNetETSSystemControl,_P:dellNetETSModuleStatus,_A9:dellNetETSClearCounters,_AA:dellNetETSGlobalEnableTrap,'dellNetETSPortTable':dellNetETSPortTable,'dellNetETSPortEntry':dellNetETSPortEntry,_e:dellNetETSPortNumber,_Q:dellNetETSAdminMode,_R:dellNetETSDcbxOperState,_AB:dellNetETSDcbxStateMachine,_AC:dellNetETSOperStatus,_AD:dellNetETSClearTLVCounters,_AE:dellNetETSConfTxTLVCounter,_AF:dellNetETSConfRxTLVCounter,_AG:dellNetETSConfRxTLVErrors,_AH:dellNetETSRecoTxTLVCounter,_AI:dellNetETSRecoRxTLVCounter,_AJ:dellNetETSRecoRxTLVErrors,'dellNetPFCObjects':dellNetPFCObjects,'dellNetPFCScalars':dellNetPFCScalars,_AK:dellNetPFCSystemControl,_S:dellNetPFCModuleStatus,_AL:dellNetPFCClearCounters,_AM:dellNetPFCGlobalEnableTrap,'dellNetPFCPortTable':dellNetPFCPortTable,'dellNetPFCPortEntry':dellNetPFCPortEntry,_f:dellNetPFCPortNumber,_T:dellNetPFCAdminMode,_U:dellNetPFCDcbxOperState,_AN:dellNetPFCDcbxStateMachine,_AO:dellNetPFCOperStatus,_AP:dellNetPFCClearTLVCounters,_AQ:dellNetPFCTxTLVCounter,_AR:dellNetPFCRxTLVCounter,_AS:dellNetPFCRxTLVErrors,'dellNetDcbNotificationObjects':dellNetDcbNotificationObjects,'dellNetDCBTraps':dellNetDCBTraps,_AT:dellNetETSModuleStatusTrap,_AU:dellNetETSPortAdminStatusTrap,_AV:dellNetETSPortPeerStatusTrap,_AW:dellNetETSPortDcbxOperStateTrap,_AX:dellNetPFCModuleStatusTrap,_AY:dellNetPFCPortAdminStatusTrap,_AZ:dellNetPFCPortPeerStatusTrap,_Aa:dellNetPFCPortDcbxOperStateTrap,'dellNetDCBTrapObjects':dellNetDCBTrapObjects,_E:dellNetDcbTrapPortNumber,_M:dellNetDcbPeerUpStatus,'dellNetDCBMibConformance':dellNetDCBMibConformance,'dellNetDCBMibCompliances':dellNetDCBMibCompliances,'dellNetDCBMibComplianceRev1':dellNetDCBMibComplianceRev1,'dellNetDCBMibCompliance':dellNetDCBMibCompliance,'dellNetDCBMibGroups':dellNetDCBMibGroups,_Ab:dellNetDcbSystemObjectGroup,_Ak:dellNetDcbObjectGroup,_Ac:dellNetDcbxScalarsGroup,_Ad:dellNetDCBXPortTableGroup,_Ae:dellNetETSScalarsGroup,_Af:dellNetETSPortTableGroup,_Ag:dellNetPFCScalarsGroup,_Ah:dellNetPFCPortTableGroup,_Ai:dellNetDCBNotificationObjectsGroup,_Aj:dellNetDCBNotificationsGroup})