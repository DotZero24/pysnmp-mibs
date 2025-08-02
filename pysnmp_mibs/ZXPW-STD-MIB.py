_N='zxPwIndex'
_M='ZXPW-STD-MIB'
_L='PwIndexType'
_K='PwFragSize'
_J='Unsigned32'
_I='SnmpAdminString'
_H='InetAddressType'
_G='InterfaceIndexOrZero'
_F='TruthValue'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HCPerfTimeElapsed,HCPerfValidIntervals=mibBuilder.importSymbols('HC-PerfHist-TC-MIB','HCPerfTimeElapsed','HCPerfValidIntervals')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','StorageType','TextualConvention',_F)
zxAnCesMib,=mibBuilder.importSymbols('ZTE-MASTER-MIB','zxAnCesMib')
IANAPwPsnTypeTC,IANAPwTypeTC=mibBuilder.importSymbols('ZX-PWE3-MIB','IANAPwPsnTypeTC','IANAPwTypeTC')
PwAttachmentIdentifierType,PwCapabilities,PwCwStatusTC,PwFragSize,PwFragStatus,PwGroupID,PwIDType,PwIndexType,PwOperStatusTC,PwStatus=mibBuilder.importSymbols('ZXPW-TC-STD-MIB','PwAttachmentIdentifierType','PwCapabilities','PwCwStatusTC',_K,'PwFragStatus','PwGroupID','PwIDType',_L,'PwOperStatusTC','PwStatus')
zxPwStdMIB=ModuleIdentity((1,3,6,1,4,1,3902,1015,1013,1))
_ZxPwObjects_ObjectIdentity=ObjectIdentity
zxPwObjects=_ZxPwObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1013,1,1))
_ZxPwIndexNext_Type=Unsigned32
_ZxPwIndexNext_Object=MibScalar
zxPwIndexNext=_ZxPwIndexNext_Object((1,3,6,1,4,1,3902,1015,1013,1,1,1),_ZxPwIndexNext_Type())
zxPwIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwIndexNext.setStatus(_A)
_ZxPwTable_Object=MibTable
zxPwTable=_ZxPwTable_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2))
if mibBuilder.loadTexts:zxPwTable.setStatus(_A)
_ZxPwEntry_Object=MibTableRow
zxPwEntry=_ZxPwEntry_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1))
zxPwEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:zxPwEntry.setStatus(_A)
_ZxPwIndex_Type=PwIndexType
_ZxPwIndex_Object=MibTableColumn
zxPwIndex=_ZxPwIndex_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,1),_ZxPwIndex_Type())
zxPwIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxPwIndex.setStatus(_A)
_ZxPwType_Type=IANAPwTypeTC
_ZxPwType_Object=MibTableColumn
zxPwType=_ZxPwType_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,2),_ZxPwType_Type())
zxPwType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwType.setStatus(_A)
class _ZxPwOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('manual',1),('pwIdFecSignaling',2),('genFecSignaling',3),('l2tpControlProtocol',4),('other',5)))
_ZxPwOwner_Type.__name__=_D
_ZxPwOwner_Object=MibTableColumn
zxPwOwner=_ZxPwOwner_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,3),_ZxPwOwner_Type())
zxPwOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwOwner.setStatus(_A)
_ZxPwPsnType_Type=IANAPwPsnTypeTC
_ZxPwPsnType_Object=MibTableColumn
zxPwPsnType=_ZxPwPsnType_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,4),_ZxPwPsnType_Type())
zxPwPsnType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwPsnType.setStatus(_A)
class _ZxPwSetUpPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxPwSetUpPriority_Type.__name__=_D
_ZxPwSetUpPriority_Object=MibTableColumn
zxPwSetUpPriority=_ZxPwSetUpPriority_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,5),_ZxPwSetUpPriority_Type())
zxPwSetUpPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwSetUpPriority.setStatus(_A)
class _ZxPwHoldingPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxPwHoldingPriority_Type.__name__=_D
_ZxPwHoldingPriority_Object=MibTableColumn
zxPwHoldingPriority=_ZxPwHoldingPriority_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,6),_ZxPwHoldingPriority_Type())
zxPwHoldingPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwHoldingPriority.setStatus(_A)
class _ZxPwPeerAddrType_Type(InetAddressType):defaultValue=1
_ZxPwPeerAddrType_Type.__name__=_H
_ZxPwPeerAddrType_Object=MibTableColumn
zxPwPeerAddrType=_ZxPwPeerAddrType_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,8),_ZxPwPeerAddrType_Type())
zxPwPeerAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwPeerAddrType.setStatus(_A)
_ZxPwPeerAddr_Type=InetAddress
_ZxPwPeerAddr_Object=MibTableColumn
zxPwPeerAddr=_ZxPwPeerAddr_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,9),_ZxPwPeerAddr_Type())
zxPwPeerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwPeerAddr.setStatus(_A)
class _ZxPwAttachedPwIndex_Type(PwIndexType):defaultValue=0
_ZxPwAttachedPwIndex_Type.__name__=_L
_ZxPwAttachedPwIndex_Object=MibTableColumn
zxPwAttachedPwIndex=_ZxPwAttachedPwIndex_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,10),_ZxPwAttachedPwIndex_Type())
zxPwAttachedPwIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwAttachedPwIndex.setStatus(_A)
class _ZxPwIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_ZxPwIfIndex_Type.__name__=_G
_ZxPwIfIndex_Object=MibTableColumn
zxPwIfIndex=_ZxPwIfIndex_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,11),_ZxPwIfIndex_Type())
zxPwIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwIfIndex.setStatus(_A)
_ZxPwID_Type=PwIDType
_ZxPwID_Object=MibTableColumn
zxPwID=_ZxPwID_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,12),_ZxPwID_Type())
zxPwID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwID.setStatus(_A)
_ZxPwLocalGroupID_Type=PwGroupID
_ZxPwLocalGroupID_Object=MibTableColumn
zxPwLocalGroupID=_ZxPwLocalGroupID_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,13),_ZxPwLocalGroupID_Type())
zxPwLocalGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwLocalGroupID.setStatus(_A)
_ZxPwGroupAttachmentID_Type=PwAttachmentIdentifierType
_ZxPwGroupAttachmentID_Object=MibTableColumn
zxPwGroupAttachmentID=_ZxPwGroupAttachmentID_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,14),_ZxPwGroupAttachmentID_Type())
zxPwGroupAttachmentID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwGroupAttachmentID.setStatus(_A)
_ZxPwLocalAttachmentID_Type=PwAttachmentIdentifierType
_ZxPwLocalAttachmentID_Object=MibTableColumn
zxPwLocalAttachmentID=_ZxPwLocalAttachmentID_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,15),_ZxPwLocalAttachmentID_Type())
zxPwLocalAttachmentID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwLocalAttachmentID.setStatus(_A)
_ZxPwPeerAttachmentID_Type=PwAttachmentIdentifierType
_ZxPwPeerAttachmentID_Object=MibTableColumn
zxPwPeerAttachmentID=_ZxPwPeerAttachmentID_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,16),_ZxPwPeerAttachmentID_Type())
zxPwPeerAttachmentID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwPeerAttachmentID.setStatus(_A)
class _ZxPwCwPreference_Type(TruthValue):defaultValue=2
_ZxPwCwPreference_Type.__name__=_F
_ZxPwCwPreference_Object=MibTableColumn
zxPwCwPreference=_ZxPwCwPreference_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,17),_ZxPwCwPreference_Type())
zxPwCwPreference.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwCwPreference.setStatus(_A)
class _ZxPwLocalIfMtu_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxPwLocalIfMtu_Type.__name__=_J
_ZxPwLocalIfMtu_Object=MibTableColumn
zxPwLocalIfMtu=_ZxPwLocalIfMtu_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,18),_ZxPwLocalIfMtu_Type())
zxPwLocalIfMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwLocalIfMtu.setStatus(_A)
class _ZxPwLocalIfString_Type(TruthValue):defaultValue=2
_ZxPwLocalIfString_Type.__name__=_F
_ZxPwLocalIfString_Object=MibTableColumn
zxPwLocalIfString=_ZxPwLocalIfString_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,19),_ZxPwLocalIfString_Type())
zxPwLocalIfString.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwLocalIfString.setStatus(_A)
_ZxPwLocalCapabAdvert_Type=PwCapabilities
_ZxPwLocalCapabAdvert_Object=MibTableColumn
zxPwLocalCapabAdvert=_ZxPwLocalCapabAdvert_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,20),_ZxPwLocalCapabAdvert_Type())
zxPwLocalCapabAdvert.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwLocalCapabAdvert.setStatus(_A)
_ZxPwRemoteGroupID_Type=PwGroupID
_ZxPwRemoteGroupID_Object=MibTableColumn
zxPwRemoteGroupID=_ZxPwRemoteGroupID_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,21),_ZxPwRemoteGroupID_Type())
zxPwRemoteGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwRemoteGroupID.setStatus(_A)
_ZxPwCwStatus_Type=PwCwStatusTC
_ZxPwCwStatus_Object=MibTableColumn
zxPwCwStatus=_ZxPwCwStatus_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,22),_ZxPwCwStatus_Type())
zxPwCwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCwStatus.setStatus(_A)
_ZxPwRemoteIfMtu_Type=Unsigned32
_ZxPwRemoteIfMtu_Object=MibTableColumn
zxPwRemoteIfMtu=_ZxPwRemoteIfMtu_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,23),_ZxPwRemoteIfMtu_Type())
zxPwRemoteIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwRemoteIfMtu.setStatus(_A)
class _ZxPwRemoteIfString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ZxPwRemoteIfString_Type.__name__=_I
_ZxPwRemoteIfString_Object=MibTableColumn
zxPwRemoteIfString=_ZxPwRemoteIfString_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,24),_ZxPwRemoteIfString_Type())
zxPwRemoteIfString.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwRemoteIfString.setStatus(_A)
_ZxPwRemoteCapabilities_Type=PwCapabilities
_ZxPwRemoteCapabilities_Object=MibTableColumn
zxPwRemoteCapabilities=_ZxPwRemoteCapabilities_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,25),_ZxPwRemoteCapabilities_Type())
zxPwRemoteCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwRemoteCapabilities.setStatus(_A)
class _ZxPwFragmentCfgSize_Type(PwFragSize):defaultValue=0
_ZxPwFragmentCfgSize_Type.__name__=_K
_ZxPwFragmentCfgSize_Object=MibTableColumn
zxPwFragmentCfgSize=_ZxPwFragmentCfgSize_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,26),_ZxPwFragmentCfgSize_Type())
zxPwFragmentCfgSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwFragmentCfgSize.setStatus(_A)
_ZxPwRmtFragCapability_Type=PwFragStatus
_ZxPwRmtFragCapability_Object=MibTableColumn
zxPwRmtFragCapability=_ZxPwRmtFragCapability_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,27),_ZxPwRmtFragCapability_Type())
zxPwRmtFragCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwRmtFragCapability.setStatus(_A)
class _ZxPwFcsRetentioncfg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fcsRetentionDisable',1),('fcsRetentionEnable',2)))
_ZxPwFcsRetentioncfg_Type.__name__=_D
_ZxPwFcsRetentioncfg_Object=MibTableColumn
zxPwFcsRetentioncfg=_ZxPwFcsRetentioncfg_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,28),_ZxPwFcsRetentioncfg_Type())
zxPwFcsRetentioncfg.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwFcsRetentioncfg.setStatus(_A)
class _ZxPwFcsRetentionStatus_Type(Bits):namedValues=NamedValues(*(('remoteIndicationUnknown',0),('remoteRequestFcsRetention',1),('fcsRetentionEnabled',2),('fcsRetentionDisabled',3),('localFcsRetentionCfgErr',4),('fcsRetentionFcsSizeMismatch',5)))
_ZxPwFcsRetentionStatus_Type.__name__='Bits'
_ZxPwFcsRetentionStatus_Object=MibTableColumn
zxPwFcsRetentionStatus=_ZxPwFcsRetentionStatus_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,29),_ZxPwFcsRetentionStatus_Type())
zxPwFcsRetentionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwFcsRetentionStatus.setStatus(_A)
_ZxPwOutboundLabel_Type=Unsigned32
_ZxPwOutboundLabel_Object=MibTableColumn
zxPwOutboundLabel=_ZxPwOutboundLabel_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,30),_ZxPwOutboundLabel_Type())
zxPwOutboundLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwOutboundLabel.setStatus(_A)
_ZxPwInboundLabel_Type=Unsigned32
_ZxPwInboundLabel_Object=MibTableColumn
zxPwInboundLabel=_ZxPwInboundLabel_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,31),_ZxPwInboundLabel_Type())
zxPwInboundLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwInboundLabel.setStatus(_A)
_ZxPwName_Type=SnmpAdminString
_ZxPwName_Object=MibTableColumn
zxPwName=_ZxPwName_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,32),_ZxPwName_Type())
zxPwName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwName.setStatus(_A)
_ZxPwDescr_Type=SnmpAdminString
_ZxPwDescr_Object=MibTableColumn
zxPwDescr=_ZxPwDescr_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,33),_ZxPwDescr_Type())
zxPwDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwDescr.setStatus(_A)
class _ZxPwCreateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_ZxPwCreateTime_Type.__name__=_E
_ZxPwCreateTime_Object=MibTableColumn
zxPwCreateTime=_ZxPwCreateTime_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,34),_ZxPwCreateTime_Type())
zxPwCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwCreateTime.setStatus(_A)
class _ZxPwUpTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_ZxPwUpTime_Type.__name__=_E
_ZxPwUpTime_Object=MibTableColumn
zxPwUpTime=_ZxPwUpTime_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,35),_ZxPwUpTime_Type())
zxPwUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwUpTime.setStatus(_A)
_ZxPwLastChange_Type=TimeTicks
_ZxPwLastChange_Object=MibTableColumn
zxPwLastChange=_ZxPwLastChange_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,36),_ZxPwLastChange_Type())
zxPwLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwLastChange.setStatus(_A)
class _ZxPwAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_ZxPwAdminStatus_Type.__name__=_D
_ZxPwAdminStatus_Object=MibTableColumn
zxPwAdminStatus=_ZxPwAdminStatus_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,37),_ZxPwAdminStatus_Type())
zxPwAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwAdminStatus.setStatus(_A)
_ZxPwOperStatus_Type=PwOperStatusTC
_ZxPwOperStatus_Object=MibTableColumn
zxPwOperStatus=_ZxPwOperStatus_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,38),_ZxPwOperStatus_Type())
zxPwOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwOperStatus.setStatus(_A)
_ZxPwLocalStatus_Type=PwStatus
_ZxPwLocalStatus_Object=MibTableColumn
zxPwLocalStatus=_ZxPwLocalStatus_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,39),_ZxPwLocalStatus_Type())
zxPwLocalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwLocalStatus.setStatus(_A)
class _ZxPwRemoteStatusCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notApplicable',1),('notYetKnown',2),('remoteCapable',3),('remoteNotCapable',4)))
_ZxPwRemoteStatusCapable_Type.__name__=_D
_ZxPwRemoteStatusCapable_Object=MibTableColumn
zxPwRemoteStatusCapable=_ZxPwRemoteStatusCapable_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,40),_ZxPwRemoteStatusCapable_Type())
zxPwRemoteStatusCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwRemoteStatusCapable.setStatus(_A)
_ZxPwRemoteStatus_Type=PwStatus
_ZxPwRemoteStatus_Object=MibTableColumn
zxPwRemoteStatus=_ZxPwRemoteStatus_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,41),_ZxPwRemoteStatus_Type())
zxPwRemoteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwRemoteStatus.setStatus(_A)
_ZxPwTimeElapsed_Type=HCPerfTimeElapsed
_ZxPwTimeElapsed_Object=MibTableColumn
zxPwTimeElapsed=_ZxPwTimeElapsed_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,42),_ZxPwTimeElapsed_Type())
zxPwTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwTimeElapsed.setStatus(_A)
_ZxPwValidIntervals_Type=HCPerfValidIntervals
_ZxPwValidIntervals_Object=MibTableColumn
zxPwValidIntervals=_ZxPwValidIntervals_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,43),_ZxPwValidIntervals_Type())
zxPwValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:zxPwValidIntervals.setStatus(_A)
_ZxPwRowStatus_Type=RowStatus
_ZxPwRowStatus_Object=MibTableColumn
zxPwRowStatus=_ZxPwRowStatus_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,44),_ZxPwRowStatus_Type())
zxPwRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwRowStatus.setStatus(_A)
_ZxPwStorageType_Type=StorageType
_ZxPwStorageType_Object=MibTableColumn
zxPwStorageType=_ZxPwStorageType_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,45),_ZxPwStorageType_Type())
zxPwStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwStorageType.setStatus(_A)
class _ZxPwPeerTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ZxPwPeerTos_Type.__name__=_D
_ZxPwPeerTos_Object=MibTableColumn
zxPwPeerTos=_ZxPwPeerTos_Object((1,3,6,1,4,1,3902,1015,1013,1,1,2,1,46),_ZxPwPeerTos_Type())
zxPwPeerTos.setMaxAccess(_B)
if mibBuilder.loadTexts:zxPwPeerTos.setStatus(_A)
mibBuilder.exportSymbols(_M,**{'zxPwStdMIB':zxPwStdMIB,'zxPwObjects':zxPwObjects,'zxPwIndexNext':zxPwIndexNext,'zxPwTable':zxPwTable,'zxPwEntry':zxPwEntry,_N:zxPwIndex,'zxPwType':zxPwType,'zxPwOwner':zxPwOwner,'zxPwPsnType':zxPwPsnType,'zxPwSetUpPriority':zxPwSetUpPriority,'zxPwHoldingPriority':zxPwHoldingPriority,'zxPwPeerAddrType':zxPwPeerAddrType,'zxPwPeerAddr':zxPwPeerAddr,'zxPwAttachedPwIndex':zxPwAttachedPwIndex,'zxPwIfIndex':zxPwIfIndex,'zxPwID':zxPwID,'zxPwLocalGroupID':zxPwLocalGroupID,'zxPwGroupAttachmentID':zxPwGroupAttachmentID,'zxPwLocalAttachmentID':zxPwLocalAttachmentID,'zxPwPeerAttachmentID':zxPwPeerAttachmentID,'zxPwCwPreference':zxPwCwPreference,'zxPwLocalIfMtu':zxPwLocalIfMtu,'zxPwLocalIfString':zxPwLocalIfString,'zxPwLocalCapabAdvert':zxPwLocalCapabAdvert,'zxPwRemoteGroupID':zxPwRemoteGroupID,'zxPwCwStatus':zxPwCwStatus,'zxPwRemoteIfMtu':zxPwRemoteIfMtu,'zxPwRemoteIfString':zxPwRemoteIfString,'zxPwRemoteCapabilities':zxPwRemoteCapabilities,'zxPwFragmentCfgSize':zxPwFragmentCfgSize,'zxPwRmtFragCapability':zxPwRmtFragCapability,'zxPwFcsRetentioncfg':zxPwFcsRetentioncfg,'zxPwFcsRetentionStatus':zxPwFcsRetentionStatus,'zxPwOutboundLabel':zxPwOutboundLabel,'zxPwInboundLabel':zxPwInboundLabel,'zxPwName':zxPwName,'zxPwDescr':zxPwDescr,'zxPwCreateTime':zxPwCreateTime,'zxPwUpTime':zxPwUpTime,'zxPwLastChange':zxPwLastChange,'zxPwAdminStatus':zxPwAdminStatus,'zxPwOperStatus':zxPwOperStatus,'zxPwLocalStatus':zxPwLocalStatus,'zxPwRemoteStatusCapable':zxPwRemoteStatusCapable,'zxPwRemoteStatus':zxPwRemoteStatus,'zxPwTimeElapsed':zxPwTimeElapsed,'zxPwValidIntervals':zxPwValidIntervals,'zxPwRowStatus':zxPwRowStatus,'zxPwStorageType':zxPwStorageType,'zxPwPeerTos':zxPwPeerTos})