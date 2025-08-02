_Aa='juniIpsecTunnelSystemStatsGroup'
_AZ='juniIpsecSummaryStatsOperStatusNotPresent'
_AY='juniIpsecSummaryStatsOperStatusDown'
_AX='juniIpsecSummaryStatsOperStatusUp'
_AW='juniIpsecSummaryStatsAdminStatusDisabled'
_AV='juniIpsecSummaryStatsAdminStatusEnabled'
_AU='juniIpsecSummaryStatsTotalTunnels'
_AT='juniIpsecTunnelGlobalLocalEndpointRowStatus'
_AS='juniIpsecTunnelGlobalLocalEndpoint'
_AR='juniIpsecTunnelTransformSetRowStatus'
_AQ='juniIpsecTunnelTransform6'
_AP='juniIpsecTunnelTransform5'
_AO='juniIpsecTunnelTransform4'
_AN='juniIpsecTunnelTransform3'
_AM='juniIpsecTunnelTransform2'
_AL='juniIpsecTunnelTransform1'
_AK='juniIpsecTunnelOutbPolicyErrs'
_AJ='juniIpsecTunnelOutbOtherTxErrs'
_AI='juniIpsecTunnelStatOutbAccRecvOctets'
_AH='juniIpsecTunnelStatOutbAccRecvPkts'
_AG='juniIpsecTunnelStatOutbUserRecvOctets'
_AF='juniIpsecTunnelStatOutbUserRecvPkts'
_AE='juniIpsecTunnelStatInbPadErrs'
_AD='juniIpsecTunnelStatInbDecryptErrs'
_AC='juniIpsecTunnelStatInbOtherRecvErrs'
_AB='juniIpsecTunnelStatInbPolicyErrs'
_AA='juniIpsecTunnelStatInbReplayErrs'
_A9='juniIpsecTunnelStatInbAuthErrs'
_A8='juniIpsecTunnelStatInbAccRecvOctets'
_A7='juniIpsecTunnelStatInbAccRecvPkts'
_A6='juniIpsecTunnelStatInbUserRecvOctets'
_A5='juniIpsecTunnelStatInbUserRecvPkts'
_A4='juniIpsecTunnelRowStatus'
_A3='juniIpsecTunnelOutboundTransform'
_A2='juniIpsecTunnelOutboundSpi'
_A1='juniIpsecTunnelInboundTransform4'
_A0='juniIpsecTunnelInboundSpi4'
_z='juniIpsecTunnelInboundTransform3'
_y='juniIpsecTunnelInboundSpi3'
_x='juniIpsecTunnelInboundTransform2'
_w='juniIpsecTunnelInboundSpi2'
_v='juniIpsecTunnelInboundTransform1'
_u='juniIpsecTunnelInboundSpi1'
_t='juniIpsecTunnelMtu'
_s='juniIpsecTunnelPfsGroup'
_r='juniIpsecTunnelLifeTimeKBs'
_q='juniIpsecTunnelLifeTimeSecs'
_p='juniIpsecTunnelRemoteIdAddr2'
_o='juniIpsecTunnelRemoteIdAddr1'
_n='juniIpsecTunnelRemoteIdType'
_m='juniIpsecTunnelLocalIdAddr2'
_l='juniIpsecTunnelLocalIdAddr1'
_k='juniIpsecTunnelLocalIdType'
_j='juniIpsecTunnelBackupDstName'
_i='juniIpsecTunnelBackupDstAddr'
_h='juniIpsecTunnelBackupDstType'
_g='juniIpsecTunnelDstName'
_f='juniIpsecTunnelDstAddr'
_e='juniIpsecTunnelDstType'
_d='juniIpsecTunnelSrcName'
_c='juniIpsecTunnelSrcAddr'
_b='juniIpsecTunnelSrcType'
_a='juniIpsecTunnelTransformSet'
_Z='juniIpsecTunnelRemoteEndPt'
_Y='juniIpsecTunnelLocalEndPt'
_X='juniIpsecTunnelTransportVirtualRouter'
_W='juniIpsecTunnelType'
_V='juniIpsecTunnelName'
_U='juniIpsecTunnelNextIfIndex'
_T='juniIpsecTunnelTransportVrRouterIdx'
_S='juniIpsecTunnelTransformSetName'
_R='juniIpsecTunnelStatIfIndex'
_Q='JuniIpsecTunnelType'
_P='juniIpsecTunnelIfIndex'
_O='reserved'
_N='JuniName'
_M='juniIpsecGlobalLocalEndpointGroup'
_L='juniIpsecTransformSetGroup'
_K='juniIpsecTunnelStatsGroup'
_J='juniIpsecTunnelConfigGroup'
_I='not-accessible'
_H='Unsigned32'
_G='JuniIpsecTransformType'
_F='JuniIpsecIdentityType'
_E='DisplayString'
_D='read-create'
_C='read-only'
_B='Juniper-IPsec-Tunnel-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniName,JuniNextIfIndex=mibBuilder.importSymbols('Juniper-TC',_N,'JuniNextIfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
juniIpsecTunnelMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,70))
if mibBuilder.loadTexts:juniIpsecTunnelMIB.setRevisions(('2004-04-06 22:26',))
class JuniIpsecIdentityType(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_O,0),('idIpv4Addr',1),('idFqdn',2),('idUserFqdn',3),('idIpv4AddrSubnet',4),('idIpv6Addr',5),('idIpv6AddrSubnet',6),('idIpv4AddrRange',7),('idIpv6AddrRange',8),('idDn',9),('idDerAsn1Gn',10),('idKeyId',11)))
class JuniIpsecTransformType(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_O,0),('ahMd5',1),('ahSha',2),('espDesMd5',3),('esp3DesMd5',4),('espDesSha',5),('esp3DesSha',6),('espNullMd5',7),('espNullSha',8),('espDesNullAuth',9),('esp3DesNullAuth',10)))
class JuniIpsecPfsGroup(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,5)));namedValues=NamedValues(*(('noGroup',0),('group1',1),('group2',2),('group5',5)))
class JuniIpsecTunnelType(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('signaledTunnel',0),('manualTunnel',1)))
class Spi(TextualConvention,Unsigned32):status=_A;displayHint='x';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_JuniIpsecObjects_ObjectIdentity=ObjectIdentity
juniIpsecObjects=_JuniIpsecObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,70,1))
_JuniIpsecTunnel_ObjectIdentity=ObjectIdentity
juniIpsecTunnel=_JuniIpsecTunnel_ObjectIdentity((1,3,6,1,4,1,4874,2,2,70,1,1))
_JuniIpsecTunnelNextIfIndex_Type=JuniNextIfIndex
_JuniIpsecTunnelNextIfIndex_Object=MibScalar
juniIpsecTunnelNextIfIndex=_JuniIpsecTunnelNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,70,1,1,1),_JuniIpsecTunnelNextIfIndex_Type())
juniIpsecTunnelNextIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelNextIfIndex.setStatus(_A)
_JuniIpsecTunnelInterfaceTable_Object=MibTable
juniIpsecTunnelInterfaceTable=_JuniIpsecTunnelInterfaceTable_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2))
if mibBuilder.loadTexts:juniIpsecTunnelInterfaceTable.setStatus(_A)
_JuniIpsecTunnelInterfaceEntry_Object=MibTableRow
juniIpsecTunnelInterfaceEntry=_JuniIpsecTunnelInterfaceEntry_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1))
juniIpsecTunnelInterfaceEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:juniIpsecTunnelInterfaceEntry.setStatus(_A)
_JuniIpsecTunnelIfIndex_Type=InterfaceIndex
_JuniIpsecTunnelIfIndex_Object=MibTableColumn
juniIpsecTunnelIfIndex=_JuniIpsecTunnelIfIndex_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,1),_JuniIpsecTunnelIfIndex_Type())
juniIpsecTunnelIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:juniIpsecTunnelIfIndex.setStatus(_A)
class _JuniIpsecTunnelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_JuniIpsecTunnelName_Type.__name__=_E
_JuniIpsecTunnelName_Object=MibTableColumn
juniIpsecTunnelName=_JuniIpsecTunnelName_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,2),_JuniIpsecTunnelName_Type())
juniIpsecTunnelName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelName.setStatus(_A)
class _JuniIpsecTunnelType_Type(JuniIpsecTunnelType):defaultValue=0
_JuniIpsecTunnelType_Type.__name__=_Q
_JuniIpsecTunnelType_Object=MibTableColumn
juniIpsecTunnelType=_JuniIpsecTunnelType_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,3),_JuniIpsecTunnelType_Type())
juniIpsecTunnelType.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelType.setStatus(_A)
class _JuniIpsecTunnelTransportVirtualRouter_Type(JuniName):defaultValue=OctetString('default')
_JuniIpsecTunnelTransportVirtualRouter_Type.__name__=_N
_JuniIpsecTunnelTransportVirtualRouter_Object=MibTableColumn
juniIpsecTunnelTransportVirtualRouter=_JuniIpsecTunnelTransportVirtualRouter_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,4),_JuniIpsecTunnelTransportVirtualRouter_Type())
juniIpsecTunnelTransportVirtualRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelTransportVirtualRouter.setStatus(_A)
_JuniIpsecTunnelLocalEndPt_Type=IpAddress
_JuniIpsecTunnelLocalEndPt_Object=MibTableColumn
juniIpsecTunnelLocalEndPt=_JuniIpsecTunnelLocalEndPt_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,5),_JuniIpsecTunnelLocalEndPt_Type())
juniIpsecTunnelLocalEndPt.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelLocalEndPt.setStatus(_A)
_JuniIpsecTunnelRemoteEndPt_Type=IpAddress
_JuniIpsecTunnelRemoteEndPt_Object=MibTableColumn
juniIpsecTunnelRemoteEndPt=_JuniIpsecTunnelRemoteEndPt_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,6),_JuniIpsecTunnelRemoteEndPt_Type())
juniIpsecTunnelRemoteEndPt.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelRemoteEndPt.setStatus(_A)
class _JuniIpsecTunnelTransformSet_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_JuniIpsecTunnelTransformSet_Type.__name__=_E
_JuniIpsecTunnelTransformSet_Object=MibTableColumn
juniIpsecTunnelTransformSet=_JuniIpsecTunnelTransformSet_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,7),_JuniIpsecTunnelTransformSet_Type())
juniIpsecTunnelTransformSet.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelTransformSet.setStatus(_A)
class _JuniIpsecTunnelSrcType_Type(JuniIpsecIdentityType):defaultValue=1
_JuniIpsecTunnelSrcType_Type.__name__=_F
_JuniIpsecTunnelSrcType_Object=MibTableColumn
juniIpsecTunnelSrcType=_JuniIpsecTunnelSrcType_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,8),_JuniIpsecTunnelSrcType_Type())
juniIpsecTunnelSrcType.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelSrcType.setStatus(_A)
_JuniIpsecTunnelSrcAddr_Type=IpAddress
_JuniIpsecTunnelSrcAddr_Object=MibTableColumn
juniIpsecTunnelSrcAddr=_JuniIpsecTunnelSrcAddr_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,9),_JuniIpsecTunnelSrcAddr_Type())
juniIpsecTunnelSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelSrcAddr.setStatus(_A)
class _JuniIpsecTunnelSrcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_JuniIpsecTunnelSrcName_Type.__name__=_E
_JuniIpsecTunnelSrcName_Object=MibTableColumn
juniIpsecTunnelSrcName=_JuniIpsecTunnelSrcName_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,10),_JuniIpsecTunnelSrcName_Type())
juniIpsecTunnelSrcName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelSrcName.setStatus(_A)
class _JuniIpsecTunnelDstType_Type(JuniIpsecIdentityType):defaultValue=1
_JuniIpsecTunnelDstType_Type.__name__=_F
_JuniIpsecTunnelDstType_Object=MibTableColumn
juniIpsecTunnelDstType=_JuniIpsecTunnelDstType_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,11),_JuniIpsecTunnelDstType_Type())
juniIpsecTunnelDstType.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelDstType.setStatus(_A)
_JuniIpsecTunnelDstAddr_Type=IpAddress
_JuniIpsecTunnelDstAddr_Object=MibTableColumn
juniIpsecTunnelDstAddr=_JuniIpsecTunnelDstAddr_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,12),_JuniIpsecTunnelDstAddr_Type())
juniIpsecTunnelDstAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelDstAddr.setStatus(_A)
class _JuniIpsecTunnelDstName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_JuniIpsecTunnelDstName_Type.__name__=_E
_JuniIpsecTunnelDstName_Object=MibTableColumn
juniIpsecTunnelDstName=_JuniIpsecTunnelDstName_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,13),_JuniIpsecTunnelDstName_Type())
juniIpsecTunnelDstName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelDstName.setStatus(_A)
class _JuniIpsecTunnelBackupDstType_Type(JuniIpsecIdentityType):defaultValue=1
_JuniIpsecTunnelBackupDstType_Type.__name__=_F
_JuniIpsecTunnelBackupDstType_Object=MibTableColumn
juniIpsecTunnelBackupDstType=_JuniIpsecTunnelBackupDstType_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,14),_JuniIpsecTunnelBackupDstType_Type())
juniIpsecTunnelBackupDstType.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelBackupDstType.setStatus(_A)
_JuniIpsecTunnelBackupDstAddr_Type=IpAddress
_JuniIpsecTunnelBackupDstAddr_Object=MibTableColumn
juniIpsecTunnelBackupDstAddr=_JuniIpsecTunnelBackupDstAddr_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,15),_JuniIpsecTunnelBackupDstAddr_Type())
juniIpsecTunnelBackupDstAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelBackupDstAddr.setStatus(_A)
class _JuniIpsecTunnelBackupDstName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_JuniIpsecTunnelBackupDstName_Type.__name__=_E
_JuniIpsecTunnelBackupDstName_Object=MibTableColumn
juniIpsecTunnelBackupDstName=_JuniIpsecTunnelBackupDstName_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,16),_JuniIpsecTunnelBackupDstName_Type())
juniIpsecTunnelBackupDstName.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelBackupDstName.setStatus(_A)
class _JuniIpsecTunnelLocalIdType_Type(JuniIpsecIdentityType):defaultValue=1
_JuniIpsecTunnelLocalIdType_Type.__name__=_F
_JuniIpsecTunnelLocalIdType_Object=MibTableColumn
juniIpsecTunnelLocalIdType=_JuniIpsecTunnelLocalIdType_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,17),_JuniIpsecTunnelLocalIdType_Type())
juniIpsecTunnelLocalIdType.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelLocalIdType.setStatus(_A)
_JuniIpsecTunnelLocalIdAddr1_Type=IpAddress
_JuniIpsecTunnelLocalIdAddr1_Object=MibTableColumn
juniIpsecTunnelLocalIdAddr1=_JuniIpsecTunnelLocalIdAddr1_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,18),_JuniIpsecTunnelLocalIdAddr1_Type())
juniIpsecTunnelLocalIdAddr1.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelLocalIdAddr1.setStatus(_A)
_JuniIpsecTunnelLocalIdAddr2_Type=IpAddress
_JuniIpsecTunnelLocalIdAddr2_Object=MibTableColumn
juniIpsecTunnelLocalIdAddr2=_JuniIpsecTunnelLocalIdAddr2_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,19),_JuniIpsecTunnelLocalIdAddr2_Type())
juniIpsecTunnelLocalIdAddr2.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelLocalIdAddr2.setStatus(_A)
class _JuniIpsecTunnelRemoteIdType_Type(JuniIpsecIdentityType):defaultValue=1
_JuniIpsecTunnelRemoteIdType_Type.__name__=_F
_JuniIpsecTunnelRemoteIdType_Object=MibTableColumn
juniIpsecTunnelRemoteIdType=_JuniIpsecTunnelRemoteIdType_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,20),_JuniIpsecTunnelRemoteIdType_Type())
juniIpsecTunnelRemoteIdType.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelRemoteIdType.setStatus(_A)
_JuniIpsecTunnelRemoteIdAddr1_Type=IpAddress
_JuniIpsecTunnelRemoteIdAddr1_Object=MibTableColumn
juniIpsecTunnelRemoteIdAddr1=_JuniIpsecTunnelRemoteIdAddr1_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,21),_JuniIpsecTunnelRemoteIdAddr1_Type())
juniIpsecTunnelRemoteIdAddr1.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelRemoteIdAddr1.setStatus(_A)
_JuniIpsecTunnelRemoteIdAddr2_Type=IpAddress
_JuniIpsecTunnelRemoteIdAddr2_Object=MibTableColumn
juniIpsecTunnelRemoteIdAddr2=_JuniIpsecTunnelRemoteIdAddr2_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,22),_JuniIpsecTunnelRemoteIdAddr2_Type())
juniIpsecTunnelRemoteIdAddr2.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelRemoteIdAddr2.setStatus(_A)
class _JuniIpsecTunnelLifeTimeSecs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1800,864000))
_JuniIpsecTunnelLifeTimeSecs_Type.__name__=_H
_JuniIpsecTunnelLifeTimeSecs_Object=MibTableColumn
juniIpsecTunnelLifeTimeSecs=_JuniIpsecTunnelLifeTimeSecs_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,23),_JuniIpsecTunnelLifeTimeSecs_Type())
juniIpsecTunnelLifeTimeSecs.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelLifeTimeSecs.setStatus(_A)
if mibBuilder.loadTexts:juniIpsecTunnelLifeTimeSecs.setUnits('seconds')
class _JuniIpsecTunnelLifeTimeKBs_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(102400,4294967295))
_JuniIpsecTunnelLifeTimeKBs_Type.__name__=_H
_JuniIpsecTunnelLifeTimeKBs_Object=MibTableColumn
juniIpsecTunnelLifeTimeKBs=_JuniIpsecTunnelLifeTimeKBs_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,24),_JuniIpsecTunnelLifeTimeKBs_Type())
juniIpsecTunnelLifeTimeKBs.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelLifeTimeKBs.setStatus(_A)
if mibBuilder.loadTexts:juniIpsecTunnelLifeTimeKBs.setUnits('kilobytes')
_JuniIpsecTunnelPfsGroup_Type=JuniIpsecPfsGroup
_JuniIpsecTunnelPfsGroup_Object=MibTableColumn
juniIpsecTunnelPfsGroup=_JuniIpsecTunnelPfsGroup_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,25),_JuniIpsecTunnelPfsGroup_Type())
juniIpsecTunnelPfsGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelPfsGroup.setStatus(_A)
class _JuniIpsecTunnelMtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(160,9000))
_JuniIpsecTunnelMtu_Type.__name__=_H
_JuniIpsecTunnelMtu_Object=MibTableColumn
juniIpsecTunnelMtu=_JuniIpsecTunnelMtu_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,26),_JuniIpsecTunnelMtu_Type())
juniIpsecTunnelMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelMtu.setStatus(_A)
_JuniIpsecTunnelInboundSpi1_Type=Spi
_JuniIpsecTunnelInboundSpi1_Object=MibTableColumn
juniIpsecTunnelInboundSpi1=_JuniIpsecTunnelInboundSpi1_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,27),_JuniIpsecTunnelInboundSpi1_Type())
juniIpsecTunnelInboundSpi1.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelInboundSpi1.setStatus(_A)
_JuniIpsecTunnelInboundTransform1_Type=JuniIpsecTransformType
_JuniIpsecTunnelInboundTransform1_Object=MibTableColumn
juniIpsecTunnelInboundTransform1=_JuniIpsecTunnelInboundTransform1_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,28),_JuniIpsecTunnelInboundTransform1_Type())
juniIpsecTunnelInboundTransform1.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelInboundTransform1.setStatus(_A)
_JuniIpsecTunnelInboundSpi2_Type=Spi
_JuniIpsecTunnelInboundSpi2_Object=MibTableColumn
juniIpsecTunnelInboundSpi2=_JuniIpsecTunnelInboundSpi2_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,29),_JuniIpsecTunnelInboundSpi2_Type())
juniIpsecTunnelInboundSpi2.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelInboundSpi2.setStatus(_A)
_JuniIpsecTunnelInboundTransform2_Type=JuniIpsecTransformType
_JuniIpsecTunnelInboundTransform2_Object=MibTableColumn
juniIpsecTunnelInboundTransform2=_JuniIpsecTunnelInboundTransform2_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,30),_JuniIpsecTunnelInboundTransform2_Type())
juniIpsecTunnelInboundTransform2.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelInboundTransform2.setStatus(_A)
_JuniIpsecTunnelInboundSpi3_Type=Spi
_JuniIpsecTunnelInboundSpi3_Object=MibTableColumn
juniIpsecTunnelInboundSpi3=_JuniIpsecTunnelInboundSpi3_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,31),_JuniIpsecTunnelInboundSpi3_Type())
juniIpsecTunnelInboundSpi3.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelInboundSpi3.setStatus(_A)
_JuniIpsecTunnelInboundTransform3_Type=JuniIpsecTransformType
_JuniIpsecTunnelInboundTransform3_Object=MibTableColumn
juniIpsecTunnelInboundTransform3=_JuniIpsecTunnelInboundTransform3_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,32),_JuniIpsecTunnelInboundTransform3_Type())
juniIpsecTunnelInboundTransform3.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelInboundTransform3.setStatus(_A)
_JuniIpsecTunnelInboundSpi4_Type=Spi
_JuniIpsecTunnelInboundSpi4_Object=MibTableColumn
juniIpsecTunnelInboundSpi4=_JuniIpsecTunnelInboundSpi4_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,33),_JuniIpsecTunnelInboundSpi4_Type())
juniIpsecTunnelInboundSpi4.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelInboundSpi4.setStatus(_A)
_JuniIpsecTunnelInboundTransform4_Type=JuniIpsecTransformType
_JuniIpsecTunnelInboundTransform4_Object=MibTableColumn
juniIpsecTunnelInboundTransform4=_JuniIpsecTunnelInboundTransform4_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,34),_JuniIpsecTunnelInboundTransform4_Type())
juniIpsecTunnelInboundTransform4.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelInboundTransform4.setStatus(_A)
_JuniIpsecTunnelOutboundSpi_Type=Spi
_JuniIpsecTunnelOutboundSpi_Object=MibTableColumn
juniIpsecTunnelOutboundSpi=_JuniIpsecTunnelOutboundSpi_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,35),_JuniIpsecTunnelOutboundSpi_Type())
juniIpsecTunnelOutboundSpi.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelOutboundSpi.setStatus(_A)
_JuniIpsecTunnelOutboundTransform_Type=JuniIpsecTransformType
_JuniIpsecTunnelOutboundTransform_Object=MibTableColumn
juniIpsecTunnelOutboundTransform=_JuniIpsecTunnelOutboundTransform_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,36),_JuniIpsecTunnelOutboundTransform_Type())
juniIpsecTunnelOutboundTransform.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelOutboundTransform.setStatus(_A)
_JuniIpsecTunnelRowStatus_Type=RowStatus
_JuniIpsecTunnelRowStatus_Object=MibTableColumn
juniIpsecTunnelRowStatus=_JuniIpsecTunnelRowStatus_Object((1,3,6,1,4,1,4874,2,2,70,1,1,2,1,37),_JuniIpsecTunnelRowStatus_Type())
juniIpsecTunnelRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelRowStatus.setStatus(_A)
_JuniIpsecTunnelStatTable_Object=MibTable
juniIpsecTunnelStatTable=_JuniIpsecTunnelStatTable_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3))
if mibBuilder.loadTexts:juniIpsecTunnelStatTable.setStatus(_A)
_JuniIpsecTunnelStatEntry_Object=MibTableRow
juniIpsecTunnelStatEntry=_JuniIpsecTunnelStatEntry_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1))
juniIpsecTunnelStatEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:juniIpsecTunnelStatEntry.setStatus(_A)
_JuniIpsecTunnelStatIfIndex_Type=InterfaceIndex
_JuniIpsecTunnelStatIfIndex_Object=MibTableColumn
juniIpsecTunnelStatIfIndex=_JuniIpsecTunnelStatIfIndex_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,1),_JuniIpsecTunnelStatIfIndex_Type())
juniIpsecTunnelStatIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:juniIpsecTunnelStatIfIndex.setStatus(_A)
_JuniIpsecTunnelStatInbUserRecvPkts_Type=Counter64
_JuniIpsecTunnelStatInbUserRecvPkts_Object=MibTableColumn
juniIpsecTunnelStatInbUserRecvPkts=_JuniIpsecTunnelStatInbUserRecvPkts_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,2),_JuniIpsecTunnelStatInbUserRecvPkts_Type())
juniIpsecTunnelStatInbUserRecvPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatInbUserRecvPkts.setStatus(_A)
_JuniIpsecTunnelStatInbUserRecvOctets_Type=Counter64
_JuniIpsecTunnelStatInbUserRecvOctets_Object=MibTableColumn
juniIpsecTunnelStatInbUserRecvOctets=_JuniIpsecTunnelStatInbUserRecvOctets_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,3),_JuniIpsecTunnelStatInbUserRecvOctets_Type())
juniIpsecTunnelStatInbUserRecvOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatInbUserRecvOctets.setStatus(_A)
_JuniIpsecTunnelStatInbAccRecvPkts_Type=Counter64
_JuniIpsecTunnelStatInbAccRecvPkts_Object=MibTableColumn
juniIpsecTunnelStatInbAccRecvPkts=_JuniIpsecTunnelStatInbAccRecvPkts_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,4),_JuniIpsecTunnelStatInbAccRecvPkts_Type())
juniIpsecTunnelStatInbAccRecvPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatInbAccRecvPkts.setStatus(_A)
_JuniIpsecTunnelStatInbAccRecvOctets_Type=Counter64
_JuniIpsecTunnelStatInbAccRecvOctets_Object=MibTableColumn
juniIpsecTunnelStatInbAccRecvOctets=_JuniIpsecTunnelStatInbAccRecvOctets_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,5),_JuniIpsecTunnelStatInbAccRecvOctets_Type())
juniIpsecTunnelStatInbAccRecvOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatInbAccRecvOctets.setStatus(_A)
_JuniIpsecTunnelStatInbAuthErrs_Type=Counter32
_JuniIpsecTunnelStatInbAuthErrs_Object=MibTableColumn
juniIpsecTunnelStatInbAuthErrs=_JuniIpsecTunnelStatInbAuthErrs_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,6),_JuniIpsecTunnelStatInbAuthErrs_Type())
juniIpsecTunnelStatInbAuthErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatInbAuthErrs.setStatus(_A)
_JuniIpsecTunnelStatInbReplayErrs_Type=Counter32
_JuniIpsecTunnelStatInbReplayErrs_Object=MibTableColumn
juniIpsecTunnelStatInbReplayErrs=_JuniIpsecTunnelStatInbReplayErrs_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,7),_JuniIpsecTunnelStatInbReplayErrs_Type())
juniIpsecTunnelStatInbReplayErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatInbReplayErrs.setStatus(_A)
_JuniIpsecTunnelStatInbPolicyErrs_Type=Counter32
_JuniIpsecTunnelStatInbPolicyErrs_Object=MibTableColumn
juniIpsecTunnelStatInbPolicyErrs=_JuniIpsecTunnelStatInbPolicyErrs_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,8),_JuniIpsecTunnelStatInbPolicyErrs_Type())
juniIpsecTunnelStatInbPolicyErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatInbPolicyErrs.setStatus(_A)
_JuniIpsecTunnelStatInbOtherRecvErrs_Type=Counter32
_JuniIpsecTunnelStatInbOtherRecvErrs_Object=MibTableColumn
juniIpsecTunnelStatInbOtherRecvErrs=_JuniIpsecTunnelStatInbOtherRecvErrs_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,9),_JuniIpsecTunnelStatInbOtherRecvErrs_Type())
juniIpsecTunnelStatInbOtherRecvErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatInbOtherRecvErrs.setStatus(_A)
_JuniIpsecTunnelStatInbDecryptErrs_Type=Counter32
_JuniIpsecTunnelStatInbDecryptErrs_Object=MibTableColumn
juniIpsecTunnelStatInbDecryptErrs=_JuniIpsecTunnelStatInbDecryptErrs_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,10),_JuniIpsecTunnelStatInbDecryptErrs_Type())
juniIpsecTunnelStatInbDecryptErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatInbDecryptErrs.setStatus(_A)
_JuniIpsecTunnelStatInbPadErrs_Type=Counter32
_JuniIpsecTunnelStatInbPadErrs_Object=MibTableColumn
juniIpsecTunnelStatInbPadErrs=_JuniIpsecTunnelStatInbPadErrs_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,11),_JuniIpsecTunnelStatInbPadErrs_Type())
juniIpsecTunnelStatInbPadErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatInbPadErrs.setStatus(_A)
_JuniIpsecTunnelStatOutbUserRecvPkts_Type=Counter64
_JuniIpsecTunnelStatOutbUserRecvPkts_Object=MibTableColumn
juniIpsecTunnelStatOutbUserRecvPkts=_JuniIpsecTunnelStatOutbUserRecvPkts_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,12),_JuniIpsecTunnelStatOutbUserRecvPkts_Type())
juniIpsecTunnelStatOutbUserRecvPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatOutbUserRecvPkts.setStatus(_A)
_JuniIpsecTunnelStatOutbUserRecvOctets_Type=Counter64
_JuniIpsecTunnelStatOutbUserRecvOctets_Object=MibTableColumn
juniIpsecTunnelStatOutbUserRecvOctets=_JuniIpsecTunnelStatOutbUserRecvOctets_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,13),_JuniIpsecTunnelStatOutbUserRecvOctets_Type())
juniIpsecTunnelStatOutbUserRecvOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatOutbUserRecvOctets.setStatus(_A)
_JuniIpsecTunnelStatOutbAccRecvPkts_Type=Counter64
_JuniIpsecTunnelStatOutbAccRecvPkts_Object=MibTableColumn
juniIpsecTunnelStatOutbAccRecvPkts=_JuniIpsecTunnelStatOutbAccRecvPkts_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,14),_JuniIpsecTunnelStatOutbAccRecvPkts_Type())
juniIpsecTunnelStatOutbAccRecvPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatOutbAccRecvPkts.setStatus(_A)
_JuniIpsecTunnelStatOutbAccRecvOctets_Type=Counter64
_JuniIpsecTunnelStatOutbAccRecvOctets_Object=MibTableColumn
juniIpsecTunnelStatOutbAccRecvOctets=_JuniIpsecTunnelStatOutbAccRecvOctets_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,15),_JuniIpsecTunnelStatOutbAccRecvOctets_Type())
juniIpsecTunnelStatOutbAccRecvOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelStatOutbAccRecvOctets.setStatus(_A)
_JuniIpsecTunnelOutbOtherTxErrs_Type=Counter32
_JuniIpsecTunnelOutbOtherTxErrs_Object=MibTableColumn
juniIpsecTunnelOutbOtherTxErrs=_JuniIpsecTunnelOutbOtherTxErrs_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,16),_JuniIpsecTunnelOutbOtherTxErrs_Type())
juniIpsecTunnelOutbOtherTxErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelOutbOtherTxErrs.setStatus(_A)
_JuniIpsecTunnelOutbPolicyErrs_Type=Counter32
_JuniIpsecTunnelOutbPolicyErrs_Object=MibTableColumn
juniIpsecTunnelOutbPolicyErrs=_JuniIpsecTunnelOutbPolicyErrs_Object((1,3,6,1,4,1,4874,2,2,70,1,1,3,1,17),_JuniIpsecTunnelOutbPolicyErrs_Type())
juniIpsecTunnelOutbPolicyErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecTunnelOutbPolicyErrs.setStatus(_A)
_JuniIpsecTunnelTransformSetTable_Object=MibTable
juniIpsecTunnelTransformSetTable=_JuniIpsecTunnelTransformSetTable_Object((1,3,6,1,4,1,4874,2,2,70,1,1,4))
if mibBuilder.loadTexts:juniIpsecTunnelTransformSetTable.setStatus(_A)
_JuniIpsecTunnelTransformSetEntry_Object=MibTableRow
juniIpsecTunnelTransformSetEntry=_JuniIpsecTunnelTransformSetEntry_Object((1,3,6,1,4,1,4874,2,2,70,1,1,4,1))
juniIpsecTunnelTransformSetEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:juniIpsecTunnelTransformSetEntry.setStatus(_A)
class _JuniIpsecTunnelTransformSetName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_JuniIpsecTunnelTransformSetName_Type.__name__=_E
_JuniIpsecTunnelTransformSetName_Object=MibTableColumn
juniIpsecTunnelTransformSetName=_JuniIpsecTunnelTransformSetName_Object((1,3,6,1,4,1,4874,2,2,70,1,1,4,1,1),_JuniIpsecTunnelTransformSetName_Type())
juniIpsecTunnelTransformSetName.setMaxAccess(_I)
if mibBuilder.loadTexts:juniIpsecTunnelTransformSetName.setStatus(_A)
class _JuniIpsecTunnelTransform1_Type(JuniIpsecTransformType):defaultValue=0
_JuniIpsecTunnelTransform1_Type.__name__=_G
_JuniIpsecTunnelTransform1_Object=MibTableColumn
juniIpsecTunnelTransform1=_JuniIpsecTunnelTransform1_Object((1,3,6,1,4,1,4874,2,2,70,1,1,4,1,2),_JuniIpsecTunnelTransform1_Type())
juniIpsecTunnelTransform1.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelTransform1.setStatus(_A)
class _JuniIpsecTunnelTransform2_Type(JuniIpsecTransformType):defaultValue=0
_JuniIpsecTunnelTransform2_Type.__name__=_G
_JuniIpsecTunnelTransform2_Object=MibTableColumn
juniIpsecTunnelTransform2=_JuniIpsecTunnelTransform2_Object((1,3,6,1,4,1,4874,2,2,70,1,1,4,1,3),_JuniIpsecTunnelTransform2_Type())
juniIpsecTunnelTransform2.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelTransform2.setStatus(_A)
class _JuniIpsecTunnelTransform3_Type(JuniIpsecTransformType):defaultValue=0
_JuniIpsecTunnelTransform3_Type.__name__=_G
_JuniIpsecTunnelTransform3_Object=MibTableColumn
juniIpsecTunnelTransform3=_JuniIpsecTunnelTransform3_Object((1,3,6,1,4,1,4874,2,2,70,1,1,4,1,4),_JuniIpsecTunnelTransform3_Type())
juniIpsecTunnelTransform3.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelTransform3.setStatus(_A)
_JuniIpsecTunnelTransform4_Type=JuniIpsecTransformType
_JuniIpsecTunnelTransform4_Object=MibTableColumn
juniIpsecTunnelTransform4=_JuniIpsecTunnelTransform4_Object((1,3,6,1,4,1,4874,2,2,70,1,1,4,1,5),_JuniIpsecTunnelTransform4_Type())
juniIpsecTunnelTransform4.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelTransform4.setStatus(_A)
class _JuniIpsecTunnelTransform5_Type(JuniIpsecTransformType):defaultValue=0
_JuniIpsecTunnelTransform5_Type.__name__=_G
_JuniIpsecTunnelTransform5_Object=MibTableColumn
juniIpsecTunnelTransform5=_JuniIpsecTunnelTransform5_Object((1,3,6,1,4,1,4874,2,2,70,1,1,4,1,6),_JuniIpsecTunnelTransform5_Type())
juniIpsecTunnelTransform5.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelTransform5.setStatus(_A)
class _JuniIpsecTunnelTransform6_Type(JuniIpsecTransformType):defaultValue=0
_JuniIpsecTunnelTransform6_Type.__name__=_G
_JuniIpsecTunnelTransform6_Object=MibTableColumn
juniIpsecTunnelTransform6=_JuniIpsecTunnelTransform6_Object((1,3,6,1,4,1,4874,2,2,70,1,1,4,1,7),_JuniIpsecTunnelTransform6_Type())
juniIpsecTunnelTransform6.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelTransform6.setStatus(_A)
_JuniIpsecTunnelTransformSetRowStatus_Type=RowStatus
_JuniIpsecTunnelTransformSetRowStatus_Object=MibTableColumn
juniIpsecTunnelTransformSetRowStatus=_JuniIpsecTunnelTransformSetRowStatus_Object((1,3,6,1,4,1,4874,2,2,70,1,1,4,1,8),_JuniIpsecTunnelTransformSetRowStatus_Type())
juniIpsecTunnelTransformSetRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelTransformSetRowStatus.setStatus(_A)
_JuniIpsecTunnelGlobalLocalEndpointTable_Object=MibTable
juniIpsecTunnelGlobalLocalEndpointTable=_JuniIpsecTunnelGlobalLocalEndpointTable_Object((1,3,6,1,4,1,4874,2,2,70,1,1,5))
if mibBuilder.loadTexts:juniIpsecTunnelGlobalLocalEndpointTable.setStatus(_A)
_JuniIpsecTunnelGlobalLocalEndpointEntry_Object=MibTableRow
juniIpsecTunnelGlobalLocalEndpointEntry=_JuniIpsecTunnelGlobalLocalEndpointEntry_Object((1,3,6,1,4,1,4874,2,2,70,1,1,5,1))
juniIpsecTunnelGlobalLocalEndpointEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:juniIpsecTunnelGlobalLocalEndpointEntry.setStatus(_A)
_JuniIpsecTunnelTransportVrRouterIdx_Type=Unsigned32
_JuniIpsecTunnelTransportVrRouterIdx_Object=MibTableColumn
juniIpsecTunnelTransportVrRouterIdx=_JuniIpsecTunnelTransportVrRouterIdx_Object((1,3,6,1,4,1,4874,2,2,70,1,1,5,1,1),_JuniIpsecTunnelTransportVrRouterIdx_Type())
juniIpsecTunnelTransportVrRouterIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:juniIpsecTunnelTransportVrRouterIdx.setStatus(_A)
_JuniIpsecTunnelGlobalLocalEndpoint_Type=IpAddress
_JuniIpsecTunnelGlobalLocalEndpoint_Object=MibTableColumn
juniIpsecTunnelGlobalLocalEndpoint=_JuniIpsecTunnelGlobalLocalEndpoint_Object((1,3,6,1,4,1,4874,2,2,70,1,1,5,1,2),_JuniIpsecTunnelGlobalLocalEndpoint_Type())
juniIpsecTunnelGlobalLocalEndpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelGlobalLocalEndpoint.setStatus(_A)
_JuniIpsecTunnelGlobalLocalEndpointRowStatus_Type=RowStatus
_JuniIpsecTunnelGlobalLocalEndpointRowStatus_Object=MibTableColumn
juniIpsecTunnelGlobalLocalEndpointRowStatus=_JuniIpsecTunnelGlobalLocalEndpointRowStatus_Object((1,3,6,1,4,1,4874,2,2,70,1,1,5,1,3),_JuniIpsecTunnelGlobalLocalEndpointRowStatus_Type())
juniIpsecTunnelGlobalLocalEndpointRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIpsecTunnelGlobalLocalEndpointRowStatus.setStatus(_A)
_JuniIpsecSystem_ObjectIdentity=ObjectIdentity
juniIpsecSystem=_JuniIpsecSystem_ObjectIdentity((1,3,6,1,4,1,4874,2,2,70,1,2))
_JuniIpsecTunnelSystemStats_ObjectIdentity=ObjectIdentity
juniIpsecTunnelSystemStats=_JuniIpsecTunnelSystemStats_ObjectIdentity((1,3,6,1,4,1,4874,2,2,70,1,2,1))
_JuniIpsecSummaryStatsTotalTunnels_Type=Counter32
_JuniIpsecSummaryStatsTotalTunnels_Object=MibScalar
juniIpsecSummaryStatsTotalTunnels=_JuniIpsecSummaryStatsTotalTunnels_Object((1,3,6,1,4,1,4874,2,2,70,1,2,1,1),_JuniIpsecSummaryStatsTotalTunnels_Type())
juniIpsecSummaryStatsTotalTunnels.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecSummaryStatsTotalTunnels.setStatus(_A)
_JuniIpsecSummaryStatsAdminStatusEnabled_Type=Counter32
_JuniIpsecSummaryStatsAdminStatusEnabled_Object=MibScalar
juniIpsecSummaryStatsAdminStatusEnabled=_JuniIpsecSummaryStatsAdminStatusEnabled_Object((1,3,6,1,4,1,4874,2,2,70,1,2,1,2),_JuniIpsecSummaryStatsAdminStatusEnabled_Type())
juniIpsecSummaryStatsAdminStatusEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecSummaryStatsAdminStatusEnabled.setStatus(_A)
_JuniIpsecSummaryStatsAdminStatusDisabled_Type=Counter32
_JuniIpsecSummaryStatsAdminStatusDisabled_Object=MibScalar
juniIpsecSummaryStatsAdminStatusDisabled=_JuniIpsecSummaryStatsAdminStatusDisabled_Object((1,3,6,1,4,1,4874,2,2,70,1,2,1,3),_JuniIpsecSummaryStatsAdminStatusDisabled_Type())
juniIpsecSummaryStatsAdminStatusDisabled.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecSummaryStatsAdminStatusDisabled.setStatus(_A)
_JuniIpsecSummaryStatsOperStatusUp_Type=Counter32
_JuniIpsecSummaryStatsOperStatusUp_Object=MibScalar
juniIpsecSummaryStatsOperStatusUp=_JuniIpsecSummaryStatsOperStatusUp_Object((1,3,6,1,4,1,4874,2,2,70,1,2,1,4),_JuniIpsecSummaryStatsOperStatusUp_Type())
juniIpsecSummaryStatsOperStatusUp.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecSummaryStatsOperStatusUp.setStatus(_A)
_JuniIpsecSummaryStatsOperStatusDown_Type=Counter32
_JuniIpsecSummaryStatsOperStatusDown_Object=MibScalar
juniIpsecSummaryStatsOperStatusDown=_JuniIpsecSummaryStatsOperStatusDown_Object((1,3,6,1,4,1,4874,2,2,70,1,2,1,5),_JuniIpsecSummaryStatsOperStatusDown_Type())
juniIpsecSummaryStatsOperStatusDown.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecSummaryStatsOperStatusDown.setStatus(_A)
_JuniIpsecSummaryStatsOperStatusNotPresent_Type=Counter32
_JuniIpsecSummaryStatsOperStatusNotPresent_Object=MibScalar
juniIpsecSummaryStatsOperStatusNotPresent=_JuniIpsecSummaryStatsOperStatusNotPresent_Object((1,3,6,1,4,1,4874,2,2,70,1,2,1,6),_JuniIpsecSummaryStatsOperStatusNotPresent_Type())
juniIpsecSummaryStatsOperStatusNotPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:juniIpsecSummaryStatsOperStatusNotPresent.setStatus(_A)
_JuniIpsecTunnelMIBConformance_ObjectIdentity=ObjectIdentity
juniIpsecTunnelMIBConformance=_JuniIpsecTunnelMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,70,2))
_JuniIpsecTunnelMIBCompliances_ObjectIdentity=ObjectIdentity
juniIpsecTunnelMIBCompliances=_JuniIpsecTunnelMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,70,2,1))
_JuniIpsecTunnelMIBGroups_ObjectIdentity=ObjectIdentity
juniIpsecTunnelMIBGroups=_JuniIpsecTunnelMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,70,2,2))
juniIpsecTunnelConfigGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,70,2,2,1))
juniIpsecTunnelConfigGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:juniIpsecTunnelConfigGroup.setStatus(_A)
juniIpsecTunnelStatsGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,70,2,2,2))
juniIpsecTunnelStatsGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:juniIpsecTunnelStatsGroup.setStatus(_A)
juniIpsecTransformSetGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,70,2,2,3))
juniIpsecTransformSetGroup.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:juniIpsecTransformSetGroup.setStatus(_A)
juniIpsecGlobalLocalEndpointGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,70,2,2,4))
juniIpsecGlobalLocalEndpointGroup.setObjects(*((_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:juniIpsecGlobalLocalEndpointGroup.setStatus(_A)
juniIpsecTunnelSystemStatsGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,70,2,2,5))
juniIpsecTunnelSystemStatsGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:juniIpsecTunnelSystemStatsGroup.setStatus(_A)
juniIpsecTunnelCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,70,2,1,1))
juniIpsecTunnelCompliance.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:juniIpsecTunnelCompliance.setStatus('obsolete')
juniIpsecTunnelCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,70,2,1,2))
juniIpsecTunnelCompliance2.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_Aa)))
if mibBuilder.loadTexts:juniIpsecTunnelCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:JuniIpsecIdentityType,_G:JuniIpsecTransformType,'JuniIpsecPfsGroup':JuniIpsecPfsGroup,_Q:JuniIpsecTunnelType,'Spi':Spi,'juniIpsecTunnelMIB':juniIpsecTunnelMIB,'juniIpsecObjects':juniIpsecObjects,'juniIpsecTunnel':juniIpsecTunnel,_U:juniIpsecTunnelNextIfIndex,'juniIpsecTunnelInterfaceTable':juniIpsecTunnelInterfaceTable,'juniIpsecTunnelInterfaceEntry':juniIpsecTunnelInterfaceEntry,_P:juniIpsecTunnelIfIndex,_V:juniIpsecTunnelName,_W:juniIpsecTunnelType,_X:juniIpsecTunnelTransportVirtualRouter,_Y:juniIpsecTunnelLocalEndPt,_Z:juniIpsecTunnelRemoteEndPt,_a:juniIpsecTunnelTransformSet,_b:juniIpsecTunnelSrcType,_c:juniIpsecTunnelSrcAddr,_d:juniIpsecTunnelSrcName,_e:juniIpsecTunnelDstType,_f:juniIpsecTunnelDstAddr,_g:juniIpsecTunnelDstName,_h:juniIpsecTunnelBackupDstType,_i:juniIpsecTunnelBackupDstAddr,_j:juniIpsecTunnelBackupDstName,_k:juniIpsecTunnelLocalIdType,_l:juniIpsecTunnelLocalIdAddr1,_m:juniIpsecTunnelLocalIdAddr2,_n:juniIpsecTunnelRemoteIdType,_o:juniIpsecTunnelRemoteIdAddr1,_p:juniIpsecTunnelRemoteIdAddr2,_q:juniIpsecTunnelLifeTimeSecs,_r:juniIpsecTunnelLifeTimeKBs,_s:juniIpsecTunnelPfsGroup,_t:juniIpsecTunnelMtu,_u:juniIpsecTunnelInboundSpi1,_v:juniIpsecTunnelInboundTransform1,_w:juniIpsecTunnelInboundSpi2,_x:juniIpsecTunnelInboundTransform2,_y:juniIpsecTunnelInboundSpi3,_z:juniIpsecTunnelInboundTransform3,_A0:juniIpsecTunnelInboundSpi4,_A1:juniIpsecTunnelInboundTransform4,_A2:juniIpsecTunnelOutboundSpi,_A3:juniIpsecTunnelOutboundTransform,_A4:juniIpsecTunnelRowStatus,'juniIpsecTunnelStatTable':juniIpsecTunnelStatTable,'juniIpsecTunnelStatEntry':juniIpsecTunnelStatEntry,_R:juniIpsecTunnelStatIfIndex,_A5:juniIpsecTunnelStatInbUserRecvPkts,_A6:juniIpsecTunnelStatInbUserRecvOctets,_A7:juniIpsecTunnelStatInbAccRecvPkts,_A8:juniIpsecTunnelStatInbAccRecvOctets,_A9:juniIpsecTunnelStatInbAuthErrs,_AA:juniIpsecTunnelStatInbReplayErrs,_AB:juniIpsecTunnelStatInbPolicyErrs,_AC:juniIpsecTunnelStatInbOtherRecvErrs,_AD:juniIpsecTunnelStatInbDecryptErrs,_AE:juniIpsecTunnelStatInbPadErrs,_AF:juniIpsecTunnelStatOutbUserRecvPkts,_AG:juniIpsecTunnelStatOutbUserRecvOctets,_AH:juniIpsecTunnelStatOutbAccRecvPkts,_AI:juniIpsecTunnelStatOutbAccRecvOctets,_AJ:juniIpsecTunnelOutbOtherTxErrs,_AK:juniIpsecTunnelOutbPolicyErrs,'juniIpsecTunnelTransformSetTable':juniIpsecTunnelTransformSetTable,'juniIpsecTunnelTransformSetEntry':juniIpsecTunnelTransformSetEntry,_S:juniIpsecTunnelTransformSetName,_AL:juniIpsecTunnelTransform1,_AM:juniIpsecTunnelTransform2,_AN:juniIpsecTunnelTransform3,_AO:juniIpsecTunnelTransform4,_AP:juniIpsecTunnelTransform5,_AQ:juniIpsecTunnelTransform6,_AR:juniIpsecTunnelTransformSetRowStatus,'juniIpsecTunnelGlobalLocalEndpointTable':juniIpsecTunnelGlobalLocalEndpointTable,'juniIpsecTunnelGlobalLocalEndpointEntry':juniIpsecTunnelGlobalLocalEndpointEntry,_T:juniIpsecTunnelTransportVrRouterIdx,_AS:juniIpsecTunnelGlobalLocalEndpoint,_AT:juniIpsecTunnelGlobalLocalEndpointRowStatus,'juniIpsecSystem':juniIpsecSystem,'juniIpsecTunnelSystemStats':juniIpsecTunnelSystemStats,_AU:juniIpsecSummaryStatsTotalTunnels,_AV:juniIpsecSummaryStatsAdminStatusEnabled,_AW:juniIpsecSummaryStatsAdminStatusDisabled,_AX:juniIpsecSummaryStatsOperStatusUp,_AY:juniIpsecSummaryStatsOperStatusDown,_AZ:juniIpsecSummaryStatsOperStatusNotPresent,'juniIpsecTunnelMIBConformance':juniIpsecTunnelMIBConformance,'juniIpsecTunnelMIBCompliances':juniIpsecTunnelMIBCompliances,'juniIpsecTunnelCompliance':juniIpsecTunnelCompliance,'juniIpsecTunnelCompliance2':juniIpsecTunnelCompliance2,'juniIpsecTunnelMIBGroups':juniIpsecTunnelMIBGroups,_J:juniIpsecTunnelConfigGroup,_K:juniIpsecTunnelStatsGroup,_L:juniIpsecTransformSetGroup,_M:juniIpsecGlobalLocalEndpointGroup,_Aa:juniIpsecTunnelSystemStatsGroup})