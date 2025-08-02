_AN='cpwVcPeformanceGroup'
_AM='cpwVcGroup'
_AL='cpwVcDown'
_AK='cpwVcPerfTotalErrorPackets'
_AJ='cpwVcPerfTotalDiscontinuityTime'
_AI='cpwVcPerfTotalOutHCBytes'
_AH='cpwVcPerfTotalOutHCPackets'
_AG='cpwVcPerfTotalInHCBytes'
_AF='cpwVcPerfTotalInHCPackets'
_AE='cpwVcPerfIntervalOutHCBytes'
_AD='cpwVcPerfIntervalOutHCPackets'
_AC='cpwVcPerfIntervalInHCBytes'
_AB='cpwVcPerfIntervalInHCPackets'
_AA='cpwVcPerfIntervalTimeElapsed'
_A9='cpwVcPerfIntervalValidData'
_A8='cpwVcPerfCurrentOutHCBytes'
_A7='cpwVcPerfCurrentOutHCPackets'
_A6='cpwVcPerfCurrentInHCBytes'
_A5='cpwVcPerfCurrentInHCPackets'
_A4='cpwVcNotifRate'
_A3='cpwVcUpDownNotifEnable'
_A2='cpwVcStorageType'
_A1='cpwVcRowStatus'
_A0='cpwVcValidIntervals'
_z='cpwVcTimeElapsed'
_y='cpwVcInboundOperStatus'
_x='cpwVcOutboundOperStatus'
_w='cpwVcAdminStatus'
_v='cpwVcUpTime'
_u='cpwVcCreateTime'
_t='cpwVcDescr'
_s='cpwVcName'
_r='cpwVcInboundVcLabel'
_q='cpwVcOutboundVcLabel'
_p='cpwVcRemoteIfString'
_o='cpwVcRemoteIfMtu'
_n='cpwVcRemoteControlWord'
_m='cpwVcRemoteGroupID'
_l='cpwVcLocalIfString'
_k='cpwVcLocalIfMtu'
_j='cpwVcControlWord'
_i='cpwVcLocalGroupID'
_h='cpwVcID'
_g='cpwVcPeerAddr'
_f='cpwVcPeerAddrType'
_e='cpwVcInboundMode'
_d='cpwVcHoldingPriority'
_c='cpwVcSetUpPriority'
_b='cpwVcPsnType'
_a='cpwVcOwner'
_Z='cpwVcType'
_Y='cpwVcIndexNext'
_X='read-write'
_W='cpwVcPeerMappingVcID'
_V='cpwVcPeerMappingVcType'
_U='cpwVcPeerMappingPeerAddr'
_T='cpwVcPeerMappingPeerAddrType'
_S='cpwVcIdMappingPeerAddr'
_R='cpwVcIdMappingPeerAddrType'
_Q='cpwVcIdMappingVcID'
_P='cpwVcIdMappingVcType'
_O='cpwVcPerfIntervalNumber'
_N='Unsigned32'
_M='SnmpAdminString'
_L='InetAddressType'
_K='cpwVcPeerMappingVcIndex'
_J='cpwVcIdMappingVcIndex'
_I='TruthValue'
_H='cpwVcIndex'
_G='cpwVcOperStatus'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='CISCO-IETF-PW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CpwGroupID,CpwOperStatus,CpwVcIDType,CpwVcIndexType,CpwVcType=mibBuilder.importSymbols('CISCO-IETF-PW-TC-MIB','CpwGroupID','CpwOperStatus','CpwVcIDType','CpwVcIndexType','CpwVcType')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'experimental','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention','TimeStamp',_I)
cpwVcMIB=ModuleIdentity((1,3,6,1,4,1,9,10,106))
if mibBuilder.loadTexts:cpwVcMIB.setRevisions(('2004-03-17 12:00','2003-02-26 12:00','2002-05-26 12:00','2002-01-30 12:00','2001-11-07 12:00','2001-07-11 12:00'))
_CpwVcObjects_ObjectIdentity=ObjectIdentity
cpwVcObjects=_CpwVcObjects_ObjectIdentity((1,3,6,1,4,1,9,10,106,1))
_CpwVcIndexNext_Type=Unsigned32
_CpwVcIndexNext_Object=MibScalar
cpwVcIndexNext=_CpwVcIndexNext_Object((1,3,6,1,4,1,9,10,106,1,1),_CpwVcIndexNext_Type())
cpwVcIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcIndexNext.setStatus(_A)
_CpwVcTable_Object=MibTable
cpwVcTable=_CpwVcTable_Object((1,3,6,1,4,1,9,10,106,1,2))
if mibBuilder.loadTexts:cpwVcTable.setStatus(_A)
_CpwVcEntry_Object=MibTableRow
cpwVcEntry=_CpwVcEntry_Object((1,3,6,1,4,1,9,10,106,1,2,1))
cpwVcEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cpwVcEntry.setStatus(_A)
_CpwVcIndex_Type=CpwVcIndexType
_CpwVcIndex_Object=MibTableColumn
cpwVcIndex=_CpwVcIndex_Object((1,3,6,1,4,1,9,10,106,1,2,1,1),_CpwVcIndex_Type())
cpwVcIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcIndex.setStatus(_A)
_CpwVcType_Type=CpwVcType
_CpwVcType_Object=MibTableColumn
cpwVcType=_CpwVcType_Object((1,3,6,1,4,1,9,10,106,1,2,1,2),_CpwVcType_Type())
cpwVcType.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcType.setStatus(_A)
class _CpwVcOwner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('maintenanceProtocol',2),('other',3)))
_CpwVcOwner_Type.__name__=_E
_CpwVcOwner_Object=MibTableColumn
cpwVcOwner=_CpwVcOwner_Object((1,3,6,1,4,1,9,10,106,1,2,1,3),_CpwVcOwner_Type())
cpwVcOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcOwner.setStatus(_A)
class _CpwVcPsnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('mpls',1),('l2tp',2),('ip',3),('mplsOverIp',4),('gre',5),('other',6)))
_CpwVcPsnType_Type.__name__=_E
_CpwVcPsnType_Object=MibTableColumn
cpwVcPsnType=_CpwVcPsnType_Object((1,3,6,1,4,1,9,10,106,1,2,1,4),_CpwVcPsnType_Type())
cpwVcPsnType.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcPsnType.setStatus(_A)
class _CpwVcSetUpPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CpwVcSetUpPriority_Type.__name__=_E
_CpwVcSetUpPriority_Object=MibTableColumn
cpwVcSetUpPriority=_CpwVcSetUpPriority_Object((1,3,6,1,4,1,9,10,106,1,2,1,5),_CpwVcSetUpPriority_Type())
cpwVcSetUpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcSetUpPriority.setStatus(_A)
class _CpwVcHoldingPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CpwVcHoldingPriority_Type.__name__=_E
_CpwVcHoldingPriority_Object=MibTableColumn
cpwVcHoldingPriority=_CpwVcHoldingPriority_Object((1,3,6,1,4,1,9,10,106,1,2,1,6),_CpwVcHoldingPriority_Type())
cpwVcHoldingPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcHoldingPriority.setStatus(_A)
class _CpwVcInboundMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loose',1),('strict',2)))
_CpwVcInboundMode_Type.__name__=_E
_CpwVcInboundMode_Object=MibTableColumn
cpwVcInboundMode=_CpwVcInboundMode_Object((1,3,6,1,4,1,9,10,106,1,2,1,7),_CpwVcInboundMode_Type())
cpwVcInboundMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcInboundMode.setStatus(_A)
class _CpwVcPeerAddrType_Type(InetAddressType):defaultValue=1
_CpwVcPeerAddrType_Type.__name__=_L
_CpwVcPeerAddrType_Object=MibTableColumn
cpwVcPeerAddrType=_CpwVcPeerAddrType_Object((1,3,6,1,4,1,9,10,106,1,2,1,8),_CpwVcPeerAddrType_Type())
cpwVcPeerAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcPeerAddrType.setStatus(_A)
_CpwVcPeerAddr_Type=InetAddress
_CpwVcPeerAddr_Object=MibTableColumn
cpwVcPeerAddr=_CpwVcPeerAddr_Object((1,3,6,1,4,1,9,10,106,1,2,1,9),_CpwVcPeerAddr_Type())
cpwVcPeerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcPeerAddr.setStatus(_A)
_CpwVcID_Type=CpwVcIDType
_CpwVcID_Object=MibTableColumn
cpwVcID=_CpwVcID_Object((1,3,6,1,4,1,9,10,106,1,2,1,10),_CpwVcID_Type())
cpwVcID.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcID.setStatus(_A)
_CpwVcLocalGroupID_Type=CpwGroupID
_CpwVcLocalGroupID_Object=MibTableColumn
cpwVcLocalGroupID=_CpwVcLocalGroupID_Object((1,3,6,1,4,1,9,10,106,1,2,1,11),_CpwVcLocalGroupID_Type())
cpwVcLocalGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcLocalGroupID.setStatus(_A)
class _CpwVcControlWord_Type(TruthValue):defaultValue=2
_CpwVcControlWord_Type.__name__=_I
_CpwVcControlWord_Object=MibTableColumn
cpwVcControlWord=_CpwVcControlWord_Object((1,3,6,1,4,1,9,10,106,1,2,1,12),_CpwVcControlWord_Type())
cpwVcControlWord.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcControlWord.setStatus(_A)
class _CpwVcLocalIfMtu_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpwVcLocalIfMtu_Type.__name__=_N
_CpwVcLocalIfMtu_Object=MibTableColumn
cpwVcLocalIfMtu=_CpwVcLocalIfMtu_Object((1,3,6,1,4,1,9,10,106,1,2,1,13),_CpwVcLocalIfMtu_Type())
cpwVcLocalIfMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcLocalIfMtu.setStatus(_A)
class _CpwVcLocalIfString_Type(TruthValue):defaultValue=2
_CpwVcLocalIfString_Type.__name__=_I
_CpwVcLocalIfString_Object=MibTableColumn
cpwVcLocalIfString=_CpwVcLocalIfString_Object((1,3,6,1,4,1,9,10,106,1,2,1,14),_CpwVcLocalIfString_Type())
cpwVcLocalIfString.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcLocalIfString.setStatus(_A)
_CpwVcRemoteGroupID_Type=CpwGroupID
_CpwVcRemoteGroupID_Object=MibTableColumn
cpwVcRemoteGroupID=_CpwVcRemoteGroupID_Object((1,3,6,1,4,1,9,10,106,1,2,1,15),_CpwVcRemoteGroupID_Type())
cpwVcRemoteGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcRemoteGroupID.setStatus(_A)
class _CpwVcRemoteControlWord_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noControlWord',1),('withControlWord',2),('notYetKnown',3)))
_CpwVcRemoteControlWord_Type.__name__=_E
_CpwVcRemoteControlWord_Object=MibTableColumn
cpwVcRemoteControlWord=_CpwVcRemoteControlWord_Object((1,3,6,1,4,1,9,10,106,1,2,1,16),_CpwVcRemoteControlWord_Type())
cpwVcRemoteControlWord.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcRemoteControlWord.setStatus(_A)
_CpwVcRemoteIfMtu_Type=Unsigned32
_CpwVcRemoteIfMtu_Object=MibTableColumn
cpwVcRemoteIfMtu=_CpwVcRemoteIfMtu_Object((1,3,6,1,4,1,9,10,106,1,2,1,17),_CpwVcRemoteIfMtu_Type())
cpwVcRemoteIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcRemoteIfMtu.setStatus(_A)
class _CpwVcRemoteIfString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpwVcRemoteIfString_Type.__name__=_M
_CpwVcRemoteIfString_Object=MibTableColumn
cpwVcRemoteIfString=_CpwVcRemoteIfString_Object((1,3,6,1,4,1,9,10,106,1,2,1,18),_CpwVcRemoteIfString_Type())
cpwVcRemoteIfString.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcRemoteIfString.setStatus(_A)
_CpwVcOutboundVcLabel_Type=Unsigned32
_CpwVcOutboundVcLabel_Object=MibTableColumn
cpwVcOutboundVcLabel=_CpwVcOutboundVcLabel_Object((1,3,6,1,4,1,9,10,106,1,2,1,19),_CpwVcOutboundVcLabel_Type())
cpwVcOutboundVcLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcOutboundVcLabel.setStatus(_A)
_CpwVcInboundVcLabel_Type=Unsigned32
_CpwVcInboundVcLabel_Object=MibTableColumn
cpwVcInboundVcLabel=_CpwVcInboundVcLabel_Object((1,3,6,1,4,1,9,10,106,1,2,1,20),_CpwVcInboundVcLabel_Type())
cpwVcInboundVcLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcInboundVcLabel.setStatus(_A)
_CpwVcName_Type=SnmpAdminString
_CpwVcName_Object=MibTableColumn
cpwVcName=_CpwVcName_Object((1,3,6,1,4,1,9,10,106,1,2,1,21),_CpwVcName_Type())
cpwVcName.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcName.setStatus(_A)
_CpwVcDescr_Type=SnmpAdminString
_CpwVcDescr_Object=MibTableColumn
cpwVcDescr=_CpwVcDescr_Object((1,3,6,1,4,1,9,10,106,1,2,1,22),_CpwVcDescr_Type())
cpwVcDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcDescr.setStatus(_A)
_CpwVcCreateTime_Type=TimeStamp
_CpwVcCreateTime_Object=MibTableColumn
cpwVcCreateTime=_CpwVcCreateTime_Object((1,3,6,1,4,1,9,10,106,1,2,1,23),_CpwVcCreateTime_Type())
cpwVcCreateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcCreateTime.setStatus(_A)
_CpwVcUpTime_Type=TimeTicks
_CpwVcUpTime_Object=MibTableColumn
cpwVcUpTime=_CpwVcUpTime_Object((1,3,6,1,4,1,9,10,106,1,2,1,24),_CpwVcUpTime_Type())
cpwVcUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcUpTime.setStatus(_A)
class _CpwVcAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_CpwVcAdminStatus_Type.__name__=_E
_CpwVcAdminStatus_Object=MibTableColumn
cpwVcAdminStatus=_CpwVcAdminStatus_Object((1,3,6,1,4,1,9,10,106,1,2,1,25),_CpwVcAdminStatus_Type())
cpwVcAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcAdminStatus.setStatus(_A)
_CpwVcOperStatus_Type=CpwOperStatus
_CpwVcOperStatus_Object=MibTableColumn
cpwVcOperStatus=_CpwVcOperStatus_Object((1,3,6,1,4,1,9,10,106,1,2,1,26),_CpwVcOperStatus_Type())
cpwVcOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcOperStatus.setStatus(_A)
_CpwVcInboundOperStatus_Type=CpwOperStatus
_CpwVcInboundOperStatus_Object=MibTableColumn
cpwVcInboundOperStatus=_CpwVcInboundOperStatus_Object((1,3,6,1,4,1,9,10,106,1,2,1,27),_CpwVcInboundOperStatus_Type())
cpwVcInboundOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcInboundOperStatus.setStatus(_A)
_CpwVcOutboundOperStatus_Type=CpwOperStatus
_CpwVcOutboundOperStatus_Object=MibTableColumn
cpwVcOutboundOperStatus=_CpwVcOutboundOperStatus_Object((1,3,6,1,4,1,9,10,106,1,2,1,28),_CpwVcOutboundOperStatus_Type())
cpwVcOutboundOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcOutboundOperStatus.setStatus(_A)
class _CpwVcTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_CpwVcTimeElapsed_Type.__name__=_E
_CpwVcTimeElapsed_Object=MibTableColumn
cpwVcTimeElapsed=_CpwVcTimeElapsed_Object((1,3,6,1,4,1,9,10,106,1,2,1,29),_CpwVcTimeElapsed_Type())
cpwVcTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcTimeElapsed.setStatus(_A)
class _CpwVcValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_CpwVcValidIntervals_Type.__name__=_E
_CpwVcValidIntervals_Object=MibTableColumn
cpwVcValidIntervals=_CpwVcValidIntervals_Object((1,3,6,1,4,1,9,10,106,1,2,1,30),_CpwVcValidIntervals_Type())
cpwVcValidIntervals.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcValidIntervals.setStatus(_A)
_CpwVcRowStatus_Type=RowStatus
_CpwVcRowStatus_Object=MibTableColumn
cpwVcRowStatus=_CpwVcRowStatus_Object((1,3,6,1,4,1,9,10,106,1,2,1,31),_CpwVcRowStatus_Type())
cpwVcRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcRowStatus.setStatus(_A)
_CpwVcStorageType_Type=StorageType
_CpwVcStorageType_Object=MibTableColumn
cpwVcStorageType=_CpwVcStorageType_Object((1,3,6,1,4,1,9,10,106,1,2,1,32),_CpwVcStorageType_Type())
cpwVcStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cpwVcStorageType.setStatus(_A)
_CpwVcPerfCurrentTable_Object=MibTable
cpwVcPerfCurrentTable=_CpwVcPerfCurrentTable_Object((1,3,6,1,4,1,9,10,106,1,3))
if mibBuilder.loadTexts:cpwVcPerfCurrentTable.setStatus(_A)
_CpwVcPerfCurrentEntry_Object=MibTableRow
cpwVcPerfCurrentEntry=_CpwVcPerfCurrentEntry_Object((1,3,6,1,4,1,9,10,106,1,3,1))
cpwVcPerfCurrentEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cpwVcPerfCurrentEntry.setStatus(_A)
_CpwVcPerfCurrentInHCPackets_Type=Counter64
_CpwVcPerfCurrentInHCPackets_Object=MibTableColumn
cpwVcPerfCurrentInHCPackets=_CpwVcPerfCurrentInHCPackets_Object((1,3,6,1,4,1,9,10,106,1,3,1,1),_CpwVcPerfCurrentInHCPackets_Type())
cpwVcPerfCurrentInHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfCurrentInHCPackets.setStatus(_A)
_CpwVcPerfCurrentInHCBytes_Type=Counter64
_CpwVcPerfCurrentInHCBytes_Object=MibTableColumn
cpwVcPerfCurrentInHCBytes=_CpwVcPerfCurrentInHCBytes_Object((1,3,6,1,4,1,9,10,106,1,3,1,2),_CpwVcPerfCurrentInHCBytes_Type())
cpwVcPerfCurrentInHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfCurrentInHCBytes.setStatus(_A)
_CpwVcPerfCurrentOutHCPackets_Type=Counter64
_CpwVcPerfCurrentOutHCPackets_Object=MibTableColumn
cpwVcPerfCurrentOutHCPackets=_CpwVcPerfCurrentOutHCPackets_Object((1,3,6,1,4,1,9,10,106,1,3,1,3),_CpwVcPerfCurrentOutHCPackets_Type())
cpwVcPerfCurrentOutHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfCurrentOutHCPackets.setStatus(_A)
_CpwVcPerfCurrentOutHCBytes_Type=Counter64
_CpwVcPerfCurrentOutHCBytes_Object=MibTableColumn
cpwVcPerfCurrentOutHCBytes=_CpwVcPerfCurrentOutHCBytes_Object((1,3,6,1,4,1,9,10,106,1,3,1,4),_CpwVcPerfCurrentOutHCBytes_Type())
cpwVcPerfCurrentOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfCurrentOutHCBytes.setStatus(_A)
_CpwVcPerfIntervalTable_Object=MibTable
cpwVcPerfIntervalTable=_CpwVcPerfIntervalTable_Object((1,3,6,1,4,1,9,10,106,1,4))
if mibBuilder.loadTexts:cpwVcPerfIntervalTable.setStatus(_A)
_CpwVcPerfIntervalEntry_Object=MibTableRow
cpwVcPerfIntervalEntry=_CpwVcPerfIntervalEntry_Object((1,3,6,1,4,1,9,10,106,1,4,1))
cpwVcPerfIntervalEntry.setIndexNames((0,_B,_H),(0,_B,_O))
if mibBuilder.loadTexts:cpwVcPerfIntervalEntry.setStatus(_A)
class _CpwVcPerfIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_CpwVcPerfIntervalNumber_Type.__name__=_E
_CpwVcPerfIntervalNumber_Object=MibTableColumn
cpwVcPerfIntervalNumber=_CpwVcPerfIntervalNumber_Object((1,3,6,1,4,1,9,10,106,1,4,1,1),_CpwVcPerfIntervalNumber_Type())
cpwVcPerfIntervalNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcPerfIntervalNumber.setStatus(_A)
_CpwVcPerfIntervalValidData_Type=TruthValue
_CpwVcPerfIntervalValidData_Object=MibTableColumn
cpwVcPerfIntervalValidData=_CpwVcPerfIntervalValidData_Object((1,3,6,1,4,1,9,10,106,1,4,1,2),_CpwVcPerfIntervalValidData_Type())
cpwVcPerfIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfIntervalValidData.setStatus(_A)
_CpwVcPerfIntervalTimeElapsed_Type=Integer32
_CpwVcPerfIntervalTimeElapsed_Object=MibTableColumn
cpwVcPerfIntervalTimeElapsed=_CpwVcPerfIntervalTimeElapsed_Object((1,3,6,1,4,1,9,10,106,1,4,1,3),_CpwVcPerfIntervalTimeElapsed_Type())
cpwVcPerfIntervalTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfIntervalTimeElapsed.setStatus(_A)
_CpwVcPerfIntervalInHCPackets_Type=Counter64
_CpwVcPerfIntervalInHCPackets_Object=MibTableColumn
cpwVcPerfIntervalInHCPackets=_CpwVcPerfIntervalInHCPackets_Object((1,3,6,1,4,1,9,10,106,1,4,1,4),_CpwVcPerfIntervalInHCPackets_Type())
cpwVcPerfIntervalInHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfIntervalInHCPackets.setStatus(_A)
_CpwVcPerfIntervalInHCBytes_Type=Counter64
_CpwVcPerfIntervalInHCBytes_Object=MibTableColumn
cpwVcPerfIntervalInHCBytes=_CpwVcPerfIntervalInHCBytes_Object((1,3,6,1,4,1,9,10,106,1,4,1,5),_CpwVcPerfIntervalInHCBytes_Type())
cpwVcPerfIntervalInHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfIntervalInHCBytes.setStatus(_A)
_CpwVcPerfIntervalOutHCPackets_Type=Counter64
_CpwVcPerfIntervalOutHCPackets_Object=MibTableColumn
cpwVcPerfIntervalOutHCPackets=_CpwVcPerfIntervalOutHCPackets_Object((1,3,6,1,4,1,9,10,106,1,4,1,6),_CpwVcPerfIntervalOutHCPackets_Type())
cpwVcPerfIntervalOutHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfIntervalOutHCPackets.setStatus(_A)
_CpwVcPerfIntervalOutHCBytes_Type=Counter64
_CpwVcPerfIntervalOutHCBytes_Object=MibTableColumn
cpwVcPerfIntervalOutHCBytes=_CpwVcPerfIntervalOutHCBytes_Object((1,3,6,1,4,1,9,10,106,1,4,1,7),_CpwVcPerfIntervalOutHCBytes_Type())
cpwVcPerfIntervalOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfIntervalOutHCBytes.setStatus(_A)
_CpwVcPerfTotalTable_Object=MibTable
cpwVcPerfTotalTable=_CpwVcPerfTotalTable_Object((1,3,6,1,4,1,9,10,106,1,5))
if mibBuilder.loadTexts:cpwVcPerfTotalTable.setStatus(_A)
_CpwVcPerfTotalEntry_Object=MibTableRow
cpwVcPerfTotalEntry=_CpwVcPerfTotalEntry_Object((1,3,6,1,4,1,9,10,106,1,5,1))
cpwVcPerfTotalEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cpwVcPerfTotalEntry.setStatus(_A)
_CpwVcPerfTotalInHCPackets_Type=Counter64
_CpwVcPerfTotalInHCPackets_Object=MibTableColumn
cpwVcPerfTotalInHCPackets=_CpwVcPerfTotalInHCPackets_Object((1,3,6,1,4,1,9,10,106,1,5,1,1),_CpwVcPerfTotalInHCPackets_Type())
cpwVcPerfTotalInHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfTotalInHCPackets.setStatus(_A)
_CpwVcPerfTotalInHCBytes_Type=Counter64
_CpwVcPerfTotalInHCBytes_Object=MibTableColumn
cpwVcPerfTotalInHCBytes=_CpwVcPerfTotalInHCBytes_Object((1,3,6,1,4,1,9,10,106,1,5,1,2),_CpwVcPerfTotalInHCBytes_Type())
cpwVcPerfTotalInHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfTotalInHCBytes.setStatus(_A)
_CpwVcPerfTotalOutHCPackets_Type=Counter64
_CpwVcPerfTotalOutHCPackets_Object=MibTableColumn
cpwVcPerfTotalOutHCPackets=_CpwVcPerfTotalOutHCPackets_Object((1,3,6,1,4,1,9,10,106,1,5,1,3),_CpwVcPerfTotalOutHCPackets_Type())
cpwVcPerfTotalOutHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfTotalOutHCPackets.setStatus(_A)
_CpwVcPerfTotalOutHCBytes_Type=Counter64
_CpwVcPerfTotalOutHCBytes_Object=MibTableColumn
cpwVcPerfTotalOutHCBytes=_CpwVcPerfTotalOutHCBytes_Object((1,3,6,1,4,1,9,10,106,1,5,1,4),_CpwVcPerfTotalOutHCBytes_Type())
cpwVcPerfTotalOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfTotalOutHCBytes.setStatus(_A)
_CpwVcPerfTotalDiscontinuityTime_Type=TimeStamp
_CpwVcPerfTotalDiscontinuityTime_Object=MibTableColumn
cpwVcPerfTotalDiscontinuityTime=_CpwVcPerfTotalDiscontinuityTime_Object((1,3,6,1,4,1,9,10,106,1,5,1,5),_CpwVcPerfTotalDiscontinuityTime_Type())
cpwVcPerfTotalDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfTotalDiscontinuityTime.setStatus(_A)
_CpwVcPerfTotalErrorPackets_Type=Counter64
_CpwVcPerfTotalErrorPackets_Object=MibScalar
cpwVcPerfTotalErrorPackets=_CpwVcPerfTotalErrorPackets_Object((1,3,6,1,4,1,9,10,106,1,6),_CpwVcPerfTotalErrorPackets_Type())
cpwVcPerfTotalErrorPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPerfTotalErrorPackets.setStatus(_A)
_CpwVcIdMappingTable_Object=MibTable
cpwVcIdMappingTable=_CpwVcIdMappingTable_Object((1,3,6,1,4,1,9,10,106,1,7))
if mibBuilder.loadTexts:cpwVcIdMappingTable.setStatus(_A)
_CpwVcIdMappingEntry_Object=MibTableRow
cpwVcIdMappingEntry=_CpwVcIdMappingEntry_Object((1,3,6,1,4,1,9,10,106,1,7,1))
cpwVcIdMappingEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S),(0,_B,_J))
if mibBuilder.loadTexts:cpwVcIdMappingEntry.setStatus(_A)
_CpwVcIdMappingVcType_Type=CpwVcType
_CpwVcIdMappingVcType_Object=MibTableColumn
cpwVcIdMappingVcType=_CpwVcIdMappingVcType_Object((1,3,6,1,4,1,9,10,106,1,7,1,1),_CpwVcIdMappingVcType_Type())
cpwVcIdMappingVcType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcIdMappingVcType.setStatus(_A)
_CpwVcIdMappingVcID_Type=CpwVcIDType
_CpwVcIdMappingVcID_Object=MibTableColumn
cpwVcIdMappingVcID=_CpwVcIdMappingVcID_Object((1,3,6,1,4,1,9,10,106,1,7,1,2),_CpwVcIdMappingVcID_Type())
cpwVcIdMappingVcID.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcIdMappingVcID.setStatus(_A)
_CpwVcIdMappingPeerAddrType_Type=InetAddressType
_CpwVcIdMappingPeerAddrType_Object=MibTableColumn
cpwVcIdMappingPeerAddrType=_CpwVcIdMappingPeerAddrType_Object((1,3,6,1,4,1,9,10,106,1,7,1,3),_CpwVcIdMappingPeerAddrType_Type())
cpwVcIdMappingPeerAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcIdMappingPeerAddrType.setStatus(_A)
_CpwVcIdMappingPeerAddr_Type=InetAddress
_CpwVcIdMappingPeerAddr_Object=MibTableColumn
cpwVcIdMappingPeerAddr=_CpwVcIdMappingPeerAddr_Object((1,3,6,1,4,1,9,10,106,1,7,1,4),_CpwVcIdMappingPeerAddr_Type())
cpwVcIdMappingPeerAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcIdMappingPeerAddr.setStatus(_A)
_CpwVcIdMappingVcIndex_Type=CpwVcIndexType
_CpwVcIdMappingVcIndex_Object=MibTableColumn
cpwVcIdMappingVcIndex=_CpwVcIdMappingVcIndex_Object((1,3,6,1,4,1,9,10,106,1,7,1,5),_CpwVcIdMappingVcIndex_Type())
cpwVcIdMappingVcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcIdMappingVcIndex.setStatus(_A)
_CpwVcPeerMappingTable_Object=MibTable
cpwVcPeerMappingTable=_CpwVcPeerMappingTable_Object((1,3,6,1,4,1,9,10,106,1,8))
if mibBuilder.loadTexts:cpwVcPeerMappingTable.setStatus(_A)
_CpwVcPeerMappingEntry_Object=MibTableRow
cpwVcPeerMappingEntry=_CpwVcPeerMappingEntry_Object((1,3,6,1,4,1,9,10,106,1,8,1))
cpwVcPeerMappingEntry.setIndexNames((0,_B,_T),(0,_B,_U),(0,_B,_V),(0,_B,_W),(0,_B,_K))
if mibBuilder.loadTexts:cpwVcPeerMappingEntry.setStatus(_A)
_CpwVcPeerMappingPeerAddrType_Type=InetAddressType
_CpwVcPeerMappingPeerAddrType_Object=MibTableColumn
cpwVcPeerMappingPeerAddrType=_CpwVcPeerMappingPeerAddrType_Object((1,3,6,1,4,1,9,10,106,1,8,1,1),_CpwVcPeerMappingPeerAddrType_Type())
cpwVcPeerMappingPeerAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcPeerMappingPeerAddrType.setStatus(_A)
_CpwVcPeerMappingPeerAddr_Type=InetAddress
_CpwVcPeerMappingPeerAddr_Object=MibTableColumn
cpwVcPeerMappingPeerAddr=_CpwVcPeerMappingPeerAddr_Object((1,3,6,1,4,1,9,10,106,1,8,1,2),_CpwVcPeerMappingPeerAddr_Type())
cpwVcPeerMappingPeerAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcPeerMappingPeerAddr.setStatus(_A)
_CpwVcPeerMappingVcType_Type=CpwVcType
_CpwVcPeerMappingVcType_Object=MibTableColumn
cpwVcPeerMappingVcType=_CpwVcPeerMappingVcType_Object((1,3,6,1,4,1,9,10,106,1,8,1,3),_CpwVcPeerMappingVcType_Type())
cpwVcPeerMappingVcType.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcPeerMappingVcType.setStatus(_A)
_CpwVcPeerMappingVcID_Type=CpwVcIDType
_CpwVcPeerMappingVcID_Object=MibTableColumn
cpwVcPeerMappingVcID=_CpwVcPeerMappingVcID_Object((1,3,6,1,4,1,9,10,106,1,8,1,4),_CpwVcPeerMappingVcID_Type())
cpwVcPeerMappingVcID.setMaxAccess(_F)
if mibBuilder.loadTexts:cpwVcPeerMappingVcID.setStatus(_A)
_CpwVcPeerMappingVcIndex_Type=CpwVcIndexType
_CpwVcPeerMappingVcIndex_Object=MibTableColumn
cpwVcPeerMappingVcIndex=_CpwVcPeerMappingVcIndex_Object((1,3,6,1,4,1,9,10,106,1,8,1,5),_CpwVcPeerMappingVcIndex_Type())
cpwVcPeerMappingVcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcPeerMappingVcIndex.setStatus(_A)
class _CpwVcUpDownNotifEnable_Type(TruthValue):defaultValue=2
_CpwVcUpDownNotifEnable_Type.__name__=_I
_CpwVcUpDownNotifEnable_Object=MibScalar
cpwVcUpDownNotifEnable=_CpwVcUpDownNotifEnable_Object((1,3,6,1,4,1,9,10,106,1,9),_CpwVcUpDownNotifEnable_Type())
cpwVcUpDownNotifEnable.setMaxAccess(_X)
if mibBuilder.loadTexts:cpwVcUpDownNotifEnable.setStatus(_A)
_CpwVcNotifRate_Type=Unsigned32
_CpwVcNotifRate_Object=MibScalar
cpwVcNotifRate=_CpwVcNotifRate_Object((1,3,6,1,4,1,9,10,106,1,10),_CpwVcNotifRate_Type())
cpwVcNotifRate.setMaxAccess(_X)
if mibBuilder.loadTexts:cpwVcNotifRate.setStatus(_A)
_CpwVcNotifications_ObjectIdentity=ObjectIdentity
cpwVcNotifications=_CpwVcNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,106,2))
_CpwVcConformance_ObjectIdentity=ObjectIdentity
cpwVcConformance=_CpwVcConformance_ObjectIdentity((1,3,6,1,4,1,9,10,106,3))
_CpwVcGroups_ObjectIdentity=ObjectIdentity
cpwVcGroups=_CpwVcGroups_ObjectIdentity((1,3,6,1,4,1,9,10,106,3,1))
_CpwVcCompliances_ObjectIdentity=ObjectIdentity
cpwVcCompliances=_CpwVcCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,106,3,2))
cpwVcGroup=ObjectGroup((1,3,6,1,4,1,9,10,106,3,1,1))
cpwVcGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_G),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:cpwVcGroup.setStatus(_A)
cpwVcPeformanceGroup=ObjectGroup((1,3,6,1,4,1,9,10,106,3,1,2))
cpwVcPeformanceGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:cpwVcPeformanceGroup.setStatus(_A)
cpwVcMappingTablesGroup=ObjectGroup((1,3,6,1,4,1,9,10,106,3,1,3))
cpwVcMappingTablesGroup.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cpwVcMappingTablesGroup.setStatus(_A)
cpwVcDown=NotificationType((1,3,6,1,4,1,9,10,106,2,1))
cpwVcDown.setObjects(*((_B,_G),(_B,_G)))
if mibBuilder.loadTexts:cpwVcDown.setStatus(_A)
cpwVcUp=NotificationType((1,3,6,1,4,1,9,10,106,2,2))
cpwVcUp.setObjects(*((_B,_G),(_B,_G)))
if mibBuilder.loadTexts:cpwVcUp.setStatus(_A)
cpwVcNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,10,106,3,1,4))
cpwVcNotificationsGroup.setObjects(*((_B,'cpwVcUp'),(_B,_AL)))
if mibBuilder.loadTexts:cpwVcNotificationsGroup.setStatus(_A)
cpwModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,106,3,2,1))
cpwModuleCompliance.setObjects(*((_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:cpwModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cpwVcMIB':cpwVcMIB,'cpwVcObjects':cpwVcObjects,_Y:cpwVcIndexNext,'cpwVcTable':cpwVcTable,'cpwVcEntry':cpwVcEntry,_H:cpwVcIndex,_Z:cpwVcType,_a:cpwVcOwner,_b:cpwVcPsnType,_c:cpwVcSetUpPriority,_d:cpwVcHoldingPriority,_e:cpwVcInboundMode,_f:cpwVcPeerAddrType,_g:cpwVcPeerAddr,_h:cpwVcID,_i:cpwVcLocalGroupID,_j:cpwVcControlWord,_k:cpwVcLocalIfMtu,_l:cpwVcLocalIfString,_m:cpwVcRemoteGroupID,_n:cpwVcRemoteControlWord,_o:cpwVcRemoteIfMtu,_p:cpwVcRemoteIfString,_q:cpwVcOutboundVcLabel,_r:cpwVcInboundVcLabel,_s:cpwVcName,_t:cpwVcDescr,_u:cpwVcCreateTime,_v:cpwVcUpTime,_w:cpwVcAdminStatus,_G:cpwVcOperStatus,_y:cpwVcInboundOperStatus,_x:cpwVcOutboundOperStatus,_z:cpwVcTimeElapsed,_A0:cpwVcValidIntervals,_A1:cpwVcRowStatus,_A2:cpwVcStorageType,'cpwVcPerfCurrentTable':cpwVcPerfCurrentTable,'cpwVcPerfCurrentEntry':cpwVcPerfCurrentEntry,_A5:cpwVcPerfCurrentInHCPackets,_A6:cpwVcPerfCurrentInHCBytes,_A7:cpwVcPerfCurrentOutHCPackets,_A8:cpwVcPerfCurrentOutHCBytes,'cpwVcPerfIntervalTable':cpwVcPerfIntervalTable,'cpwVcPerfIntervalEntry':cpwVcPerfIntervalEntry,_O:cpwVcPerfIntervalNumber,_A9:cpwVcPerfIntervalValidData,_AA:cpwVcPerfIntervalTimeElapsed,_AB:cpwVcPerfIntervalInHCPackets,_AC:cpwVcPerfIntervalInHCBytes,_AD:cpwVcPerfIntervalOutHCPackets,_AE:cpwVcPerfIntervalOutHCBytes,'cpwVcPerfTotalTable':cpwVcPerfTotalTable,'cpwVcPerfTotalEntry':cpwVcPerfTotalEntry,_AF:cpwVcPerfTotalInHCPackets,_AG:cpwVcPerfTotalInHCBytes,_AH:cpwVcPerfTotalOutHCPackets,_AI:cpwVcPerfTotalOutHCBytes,_AJ:cpwVcPerfTotalDiscontinuityTime,_AK:cpwVcPerfTotalErrorPackets,'cpwVcIdMappingTable':cpwVcIdMappingTable,'cpwVcIdMappingEntry':cpwVcIdMappingEntry,_P:cpwVcIdMappingVcType,_Q:cpwVcIdMappingVcID,_R:cpwVcIdMappingPeerAddrType,_S:cpwVcIdMappingPeerAddr,_J:cpwVcIdMappingVcIndex,'cpwVcPeerMappingTable':cpwVcPeerMappingTable,'cpwVcPeerMappingEntry':cpwVcPeerMappingEntry,_T:cpwVcPeerMappingPeerAddrType,_U:cpwVcPeerMappingPeerAddr,_V:cpwVcPeerMappingVcType,_W:cpwVcPeerMappingVcID,_K:cpwVcPeerMappingVcIndex,_A3:cpwVcUpDownNotifEnable,_A4:cpwVcNotifRate,'cpwVcNotifications':cpwVcNotifications,_AL:cpwVcDown,'cpwVcUp':cpwVcUp,'cpwVcConformance':cpwVcConformance,'cpwVcGroups':cpwVcGroups,_AM:cpwVcGroup,_AN:cpwVcPeformanceGroup,'cpwVcMappingTablesGroup':cpwVcMappingTablesGroup,'cpwVcNotificationsGroup':cpwVcNotificationsGroup,'cpwVcCompliances':cpwVcCompliances,'cpwModuleCompliance':cpwModuleCompliance})