_Ab='mplsL3VpnNumVrfRouteMaxThreshCleared'
_Aa='mplsL3VpnNumVrfSecIllglLblThrshExcd'
_AZ='mplsL3VpnVrfNumVrfRouteMaxThreshExceeded'
_AY='mplsL3VpnVrfRouteMidThreshExceeded'
_AX='mplsL3VpnVrfDown'
_AW='mplsL3VpnVrfUp'
_AV='mplsL3VpnVrfRTStorageType'
_AU='mplsL3VpnVrfRTRowStatus'
_AT='mplsL3VpnVrfRT'
_AS='mplsL3VpnVrfRTDescr'
_AR='mplsL3VpnVrfRteInetCidrStatus'
_AQ='mplsL3VpnVrfRteXCPointer'
_AP='mplsL3VpnVrfRteInetCidrMetric5'
_AO='mplsL3VpnVrfRteInetCidrMetric4'
_AN='mplsL3VpnVrfRteInetCidrMetric3'
_AM='mplsL3VpnVrfRteInetCidrMetric2'
_AL='mplsL3VpnVrfRteInetCidrMetric1'
_AK='mplsL3VpnVrfRteInetCidrNextHopAS'
_AJ='mplsL3VpnVrfRteInetCidrAge'
_AI='mplsL3VpnVrfRteInetCidrProto'
_AH='mplsL3VpnVrfRteInetCidrType'
_AG='mplsL3VpnVrfRteInetCidrIfIndex'
_AF='mplsL3VpnVrfSecDiscontinuityTime'
_AE='mplsL3VpnVrfPerfDiscTime'
_AD='mplsL3VpnVrfPerfRoutesDropped'
_AC='mplsL3VpnVrfPerfRoutesDeleted'
_AB='mplsL3VpnVrfPerfRoutesAdded'
_AA='mplsL3VpnIfConfStorageType'
_A9='mplsL3VpnIfVpnRouteDistProtocol'
_A8='mplsL3VpnIfVpnClassification'
_A7='mplsL3VpnVrfConfStorageType'
_A6='mplsL3VpnVrfConfAdminStatus'
_A5='mplsL3VpnVrfConfRowStatus'
_A4='mplsL3VpnVrfConfLastChanged'
_A3='mplsL3VpnVrfConfMaxRoutes'
_A2='mplsL3VpnVrfAssociatedInterfaces'
_A1='mplsL3VpnVrfActiveInterfaces'
_A0='mplsL3VpnVrfCreationTime'
_z='mplsL3VpnVrfRD'
_y='mplsL3VpnVrfDescription'
_x='mplsL3VpnVrfVpnId'
_w='mplsL3VpnIllLblRcvThrsh'
_v='mplsL3VpnVrfConfRteMxThrshTime'
_u='mplsL3VpnVrfConfMaxPossRts'
_t='mplsL3VpnNotificationEnable'
_s='mplsL3VpnConnectedInterfaces'
_r='mplsL3VpnActiveVrfs'
_q='mplsL3VpnConfiguredVrfs'
_p='mplsL3VpnVrfPerfEntry'
_o='mplsL3VpnVrfSecEntry'
_n='mplsL3VpnVrfRteInetCidrNextHop'
_m='mplsL3VpnVrfRteInetCidrNHopType'
_l='mplsL3VpnVrfRteInetCidrPolicy'
_k='mplsL3VpnVrfRteInetCidrPfxLen'
_j='mplsL3VpnVrfRteInetCidrDest'
_i='mplsL3VpnVrfRteInetCidrDestType'
_h='mplsL3VpnVrfRTType'
_g='mplsL3VpnVrfRTIndex'
_f='mplsL3VpnIfConfIndex'
_e='read-write'
_d='TruthValue'
_c='InetAutonomousSystemNumber'
_b='InetAddressPrefixLength'
_a='InterfaceIndexOrZero'
_Z='mplsL3VpnPerfRouteGroup'
_Y='mplsL3VpnNotificationGroup'
_X='mplsL3VpnSecGroup'
_W='mplsL3VpnVrfRTGroup'
_V='mplsL3VpnVrfRteGroup'
_U='mplsL3VpnPerfGroup'
_T='mplsL3VpnIfGroup'
_S='mplsL3VpnVrfGroup'
_R='mplsL3VpnScalarGroup'
_Q='mplsL3VpnVrfSecIllegalLblVltns'
_P='mplsL3VpnVrfConfMidRteThresh'
_O='MplsL3VpnRouteDistinguisher'
_N='SnmpAdminString'
_M='mplsL3VpnIfConfRowStatus'
_L='mplsL3VpnVrfConfHighRteThresh'
_K='mplsL3VpnVrfOperStatus'
_J='StorageType'
_I='mplsL3VpnVrfPerfCurrNumRoutes'
_H='mplsL3VpnVrfName'
_G='Unsigned32'
_F='not-accessible'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='current'
_A='MPLS-L3VPN-STD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAipRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipRouteProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_a)
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_b,'InetAddressType',_c)
MplsIndexType,=mibBuilder.importSymbols('MPLS-LSR-STD-MIB','MplsIndexType')
mplsStdMIB,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','mplsStdMIB')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_J,'TextualConvention','TimeStamp',_d)
VPNIdOrZero,=mibBuilder.importSymbols('VPN-TC-STD-MIB','VPNIdOrZero')
mplsL3VpnMIB=ModuleIdentity((1,3,6,1,2,1,10,166,11))
if mibBuilder.loadTexts:mplsL3VpnMIB.setRevisions(('2006-01-23 00:00',))
class MplsL3VpnName(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
class MplsL3VpnRouteDistinguisher(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class MplsL3VpnRtType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('import',1),('export',2),('both',3)))
_MplsL3VpnNotifications_ObjectIdentity=ObjectIdentity
mplsL3VpnNotifications=_MplsL3VpnNotifications_ObjectIdentity((1,3,6,1,2,1,10,166,11,0))
_MplsL3VpnObjects_ObjectIdentity=ObjectIdentity
mplsL3VpnObjects=_MplsL3VpnObjects_ObjectIdentity((1,3,6,1,2,1,10,166,11,1))
_MplsL3VpnScalars_ObjectIdentity=ObjectIdentity
mplsL3VpnScalars=_MplsL3VpnScalars_ObjectIdentity((1,3,6,1,2,1,10,166,11,1,1))
_MplsL3VpnConfiguredVrfs_Type=Unsigned32
_MplsL3VpnConfiguredVrfs_Object=MibScalar
mplsL3VpnConfiguredVrfs=_MplsL3VpnConfiguredVrfs_Object((1,3,6,1,2,1,10,166,11,1,1,1),_MplsL3VpnConfiguredVrfs_Type())
mplsL3VpnConfiguredVrfs.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnConfiguredVrfs.setStatus(_B)
_MplsL3VpnActiveVrfs_Type=Gauge32
_MplsL3VpnActiveVrfs_Object=MibScalar
mplsL3VpnActiveVrfs=_MplsL3VpnActiveVrfs_Object((1,3,6,1,2,1,10,166,11,1,1,2),_MplsL3VpnActiveVrfs_Type())
mplsL3VpnActiveVrfs.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnActiveVrfs.setStatus(_B)
_MplsL3VpnConnectedInterfaces_Type=Gauge32
_MplsL3VpnConnectedInterfaces_Object=MibScalar
mplsL3VpnConnectedInterfaces=_MplsL3VpnConnectedInterfaces_Object((1,3,6,1,2,1,10,166,11,1,1,3),_MplsL3VpnConnectedInterfaces_Type())
mplsL3VpnConnectedInterfaces.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnConnectedInterfaces.setStatus(_B)
class _MplsL3VpnNotificationEnable_Type(TruthValue):defaultValue=2
_MplsL3VpnNotificationEnable_Type.__name__=_d
_MplsL3VpnNotificationEnable_Object=MibScalar
mplsL3VpnNotificationEnable=_MplsL3VpnNotificationEnable_Object((1,3,6,1,2,1,10,166,11,1,1,4),_MplsL3VpnNotificationEnable_Type())
mplsL3VpnNotificationEnable.setMaxAccess(_e)
if mibBuilder.loadTexts:mplsL3VpnNotificationEnable.setStatus(_B)
_MplsL3VpnVrfConfMaxPossRts_Type=Unsigned32
_MplsL3VpnVrfConfMaxPossRts_Object=MibScalar
mplsL3VpnVrfConfMaxPossRts=_MplsL3VpnVrfConfMaxPossRts_Object((1,3,6,1,2,1,10,166,11,1,1,5),_MplsL3VpnVrfConfMaxPossRts_Type())
mplsL3VpnVrfConfMaxPossRts.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfConfMaxPossRts.setStatus(_B)
class _MplsL3VpnVrfConfRteMxThrshTime_Type(Unsigned32):defaultValue=0
_MplsL3VpnVrfConfRteMxThrshTime_Type.__name__=_G
_MplsL3VpnVrfConfRteMxThrshTime_Object=MibScalar
mplsL3VpnVrfConfRteMxThrshTime=_MplsL3VpnVrfConfRteMxThrshTime_Object((1,3,6,1,2,1,10,166,11,1,1,6),_MplsL3VpnVrfConfRteMxThrshTime_Type())
mplsL3VpnVrfConfRteMxThrshTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfConfRteMxThrshTime.setStatus(_B)
if mibBuilder.loadTexts:mplsL3VpnVrfConfRteMxThrshTime.setUnits('seconds')
_MplsL3VpnIllLblRcvThrsh_Type=Unsigned32
_MplsL3VpnIllLblRcvThrsh_Object=MibScalar
mplsL3VpnIllLblRcvThrsh=_MplsL3VpnIllLblRcvThrsh_Object((1,3,6,1,2,1,10,166,11,1,1,7),_MplsL3VpnIllLblRcvThrsh_Type())
mplsL3VpnIllLblRcvThrsh.setMaxAccess(_e)
if mibBuilder.loadTexts:mplsL3VpnIllLblRcvThrsh.setStatus(_B)
_MplsL3VpnConf_ObjectIdentity=ObjectIdentity
mplsL3VpnConf=_MplsL3VpnConf_ObjectIdentity((1,3,6,1,2,1,10,166,11,1,2))
_MplsL3VpnIfConfTable_Object=MibTable
mplsL3VpnIfConfTable=_MplsL3VpnIfConfTable_Object((1,3,6,1,2,1,10,166,11,1,2,1))
if mibBuilder.loadTexts:mplsL3VpnIfConfTable.setStatus(_B)
_MplsL3VpnIfConfEntry_Object=MibTableRow
mplsL3VpnIfConfEntry=_MplsL3VpnIfConfEntry_Object((1,3,6,1,2,1,10,166,11,1,2,1,1))
mplsL3VpnIfConfEntry.setIndexNames((0,_A,_H),(0,_A,_f))
if mibBuilder.loadTexts:mplsL3VpnIfConfEntry.setStatus(_B)
_MplsL3VpnIfConfIndex_Type=InterfaceIndex
_MplsL3VpnIfConfIndex_Object=MibTableColumn
mplsL3VpnIfConfIndex=_MplsL3VpnIfConfIndex_Object((1,3,6,1,2,1,10,166,11,1,2,1,1,1),_MplsL3VpnIfConfIndex_Type())
mplsL3VpnIfConfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsL3VpnIfConfIndex.setStatus(_B)
class _MplsL3VpnIfVpnClassification_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('carrierOfCarrier',1),('enterprise',2),('interProvider',3)))
_MplsL3VpnIfVpnClassification_Type.__name__=_E
_MplsL3VpnIfVpnClassification_Object=MibTableColumn
mplsL3VpnIfVpnClassification=_MplsL3VpnIfVpnClassification_Object((1,3,6,1,2,1,10,166,11,1,2,1,1,2),_MplsL3VpnIfVpnClassification_Type())
mplsL3VpnIfVpnClassification.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnIfVpnClassification.setStatus(_B)
class _MplsL3VpnIfVpnRouteDistProtocol_Type(Bits):namedValues=NamedValues(*(('none',0),('bgp',1),('ospf',2),('rip',3),('isis',4),('static',5),('other',6)))
_MplsL3VpnIfVpnRouteDistProtocol_Type.__name__='Bits'
_MplsL3VpnIfVpnRouteDistProtocol_Object=MibTableColumn
mplsL3VpnIfVpnRouteDistProtocol=_MplsL3VpnIfVpnRouteDistProtocol_Object((1,3,6,1,2,1,10,166,11,1,2,1,1,3),_MplsL3VpnIfVpnRouteDistProtocol_Type())
mplsL3VpnIfVpnRouteDistProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnIfVpnRouteDistProtocol.setStatus(_B)
class _MplsL3VpnIfConfStorageType_Type(StorageType):defaultValue=2
_MplsL3VpnIfConfStorageType_Type.__name__=_J
_MplsL3VpnIfConfStorageType_Object=MibTableColumn
mplsL3VpnIfConfStorageType=_MplsL3VpnIfConfStorageType_Object((1,3,6,1,2,1,10,166,11,1,2,1,1,4),_MplsL3VpnIfConfStorageType_Type())
mplsL3VpnIfConfStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnIfConfStorageType.setStatus(_B)
_MplsL3VpnIfConfRowStatus_Type=RowStatus
_MplsL3VpnIfConfRowStatus_Object=MibTableColumn
mplsL3VpnIfConfRowStatus=_MplsL3VpnIfConfRowStatus_Object((1,3,6,1,2,1,10,166,11,1,2,1,1,5),_MplsL3VpnIfConfRowStatus_Type())
mplsL3VpnIfConfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnIfConfRowStatus.setStatus(_B)
_MplsL3VpnVrfTable_Object=MibTable
mplsL3VpnVrfTable=_MplsL3VpnVrfTable_Object((1,3,6,1,2,1,10,166,11,1,2,2))
if mibBuilder.loadTexts:mplsL3VpnVrfTable.setStatus(_B)
_MplsL3VpnVrfEntry_Object=MibTableRow
mplsL3VpnVrfEntry=_MplsL3VpnVrfEntry_Object((1,3,6,1,2,1,10,166,11,1,2,2,1))
mplsL3VpnVrfEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:mplsL3VpnVrfEntry.setStatus(_B)
_MplsL3VpnVrfName_Type=MplsL3VpnName
_MplsL3VpnVrfName_Object=MibTableColumn
mplsL3VpnVrfName=_MplsL3VpnVrfName_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,1),_MplsL3VpnVrfName_Type())
mplsL3VpnVrfName.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsL3VpnVrfName.setStatus(_B)
_MplsL3VpnVrfVpnId_Type=VPNIdOrZero
_MplsL3VpnVrfVpnId_Object=MibTableColumn
mplsL3VpnVrfVpnId=_MplsL3VpnVrfVpnId_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,2),_MplsL3VpnVrfVpnId_Type())
mplsL3VpnVrfVpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfVpnId.setStatus(_B)
class _MplsL3VpnVrfDescription_Type(SnmpAdminString):defaultValue=OctetString('')
_MplsL3VpnVrfDescription_Type.__name__=_N
_MplsL3VpnVrfDescription_Object=MibTableColumn
mplsL3VpnVrfDescription=_MplsL3VpnVrfDescription_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,3),_MplsL3VpnVrfDescription_Type())
mplsL3VpnVrfDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfDescription.setStatus(_B)
class _MplsL3VpnVrfRD_Type(MplsL3VpnRouteDistinguisher):defaultValue=OctetString('')
_MplsL3VpnVrfRD_Type.__name__=_O
_MplsL3VpnVrfRD_Object=MibTableColumn
mplsL3VpnVrfRD=_MplsL3VpnVrfRD_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,4),_MplsL3VpnVrfRD_Type())
mplsL3VpnVrfRD.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRD.setStatus(_B)
_MplsL3VpnVrfCreationTime_Type=TimeStamp
_MplsL3VpnVrfCreationTime_Object=MibTableColumn
mplsL3VpnVrfCreationTime=_MplsL3VpnVrfCreationTime_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,5),_MplsL3VpnVrfCreationTime_Type())
mplsL3VpnVrfCreationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfCreationTime.setStatus(_B)
class _MplsL3VpnVrfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_MplsL3VpnVrfOperStatus_Type.__name__=_E
_MplsL3VpnVrfOperStatus_Object=MibTableColumn
mplsL3VpnVrfOperStatus=_MplsL3VpnVrfOperStatus_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,6),_MplsL3VpnVrfOperStatus_Type())
mplsL3VpnVrfOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfOperStatus.setStatus(_B)
_MplsL3VpnVrfActiveInterfaces_Type=Gauge32
_MplsL3VpnVrfActiveInterfaces_Object=MibTableColumn
mplsL3VpnVrfActiveInterfaces=_MplsL3VpnVrfActiveInterfaces_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,7),_MplsL3VpnVrfActiveInterfaces_Type())
mplsL3VpnVrfActiveInterfaces.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfActiveInterfaces.setStatus(_B)
_MplsL3VpnVrfAssociatedInterfaces_Type=Unsigned32
_MplsL3VpnVrfAssociatedInterfaces_Object=MibTableColumn
mplsL3VpnVrfAssociatedInterfaces=_MplsL3VpnVrfAssociatedInterfaces_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,8),_MplsL3VpnVrfAssociatedInterfaces_Type())
mplsL3VpnVrfAssociatedInterfaces.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfAssociatedInterfaces.setStatus(_B)
class _MplsL3VpnVrfConfMidRteThresh_Type(Unsigned32):defaultValue=0
_MplsL3VpnVrfConfMidRteThresh_Type.__name__=_G
_MplsL3VpnVrfConfMidRteThresh_Object=MibTableColumn
mplsL3VpnVrfConfMidRteThresh=_MplsL3VpnVrfConfMidRteThresh_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,9),_MplsL3VpnVrfConfMidRteThresh_Type())
mplsL3VpnVrfConfMidRteThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfConfMidRteThresh.setStatus(_B)
class _MplsL3VpnVrfConfHighRteThresh_Type(Unsigned32):defaultValue=0
_MplsL3VpnVrfConfHighRteThresh_Type.__name__=_G
_MplsL3VpnVrfConfHighRteThresh_Object=MibTableColumn
mplsL3VpnVrfConfHighRteThresh=_MplsL3VpnVrfConfHighRteThresh_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,10),_MplsL3VpnVrfConfHighRteThresh_Type())
mplsL3VpnVrfConfHighRteThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfConfHighRteThresh.setStatus(_B)
class _MplsL3VpnVrfConfMaxRoutes_Type(Unsigned32):defaultValue=0
_MplsL3VpnVrfConfMaxRoutes_Type.__name__=_G
_MplsL3VpnVrfConfMaxRoutes_Object=MibTableColumn
mplsL3VpnVrfConfMaxRoutes=_MplsL3VpnVrfConfMaxRoutes_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,11),_MplsL3VpnVrfConfMaxRoutes_Type())
mplsL3VpnVrfConfMaxRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfConfMaxRoutes.setStatus(_B)
_MplsL3VpnVrfConfLastChanged_Type=TimeStamp
_MplsL3VpnVrfConfLastChanged_Object=MibTableColumn
mplsL3VpnVrfConfLastChanged=_MplsL3VpnVrfConfLastChanged_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,12),_MplsL3VpnVrfConfLastChanged_Type())
mplsL3VpnVrfConfLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfConfLastChanged.setStatus(_B)
_MplsL3VpnVrfConfRowStatus_Type=RowStatus
_MplsL3VpnVrfConfRowStatus_Object=MibTableColumn
mplsL3VpnVrfConfRowStatus=_MplsL3VpnVrfConfRowStatus_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,13),_MplsL3VpnVrfConfRowStatus_Type())
mplsL3VpnVrfConfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfConfRowStatus.setStatus(_B)
class _MplsL3VpnVrfConfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_MplsL3VpnVrfConfAdminStatus_Type.__name__=_E
_MplsL3VpnVrfConfAdminStatus_Object=MibTableColumn
mplsL3VpnVrfConfAdminStatus=_MplsL3VpnVrfConfAdminStatus_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,14),_MplsL3VpnVrfConfAdminStatus_Type())
mplsL3VpnVrfConfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfConfAdminStatus.setStatus(_B)
class _MplsL3VpnVrfConfStorageType_Type(StorageType):defaultValue=2
_MplsL3VpnVrfConfStorageType_Type.__name__=_J
_MplsL3VpnVrfConfStorageType_Object=MibTableColumn
mplsL3VpnVrfConfStorageType=_MplsL3VpnVrfConfStorageType_Object((1,3,6,1,2,1,10,166,11,1,2,2,1,15),_MplsL3VpnVrfConfStorageType_Type())
mplsL3VpnVrfConfStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfConfStorageType.setStatus(_B)
_MplsL3VpnVrfRTTable_Object=MibTable
mplsL3VpnVrfRTTable=_MplsL3VpnVrfRTTable_Object((1,3,6,1,2,1,10,166,11,1,2,3))
if mibBuilder.loadTexts:mplsL3VpnVrfRTTable.setStatus(_B)
_MplsL3VpnVrfRTEntry_Object=MibTableRow
mplsL3VpnVrfRTEntry=_MplsL3VpnVrfRTEntry_Object((1,3,6,1,2,1,10,166,11,1,2,3,1))
mplsL3VpnVrfRTEntry.setIndexNames((0,_A,_H),(0,_A,_g),(0,_A,_h))
if mibBuilder.loadTexts:mplsL3VpnVrfRTEntry.setStatus(_B)
class _MplsL3VpnVrfRTIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MplsL3VpnVrfRTIndex_Type.__name__=_G
_MplsL3VpnVrfRTIndex_Object=MibTableColumn
mplsL3VpnVrfRTIndex=_MplsL3VpnVrfRTIndex_Object((1,3,6,1,2,1,10,166,11,1,2,3,1,2),_MplsL3VpnVrfRTIndex_Type())
mplsL3VpnVrfRTIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsL3VpnVrfRTIndex.setStatus(_B)
_MplsL3VpnVrfRTType_Type=MplsL3VpnRtType
_MplsL3VpnVrfRTType_Object=MibTableColumn
mplsL3VpnVrfRTType=_MplsL3VpnVrfRTType_Object((1,3,6,1,2,1,10,166,11,1,2,3,1,3),_MplsL3VpnVrfRTType_Type())
mplsL3VpnVrfRTType.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsL3VpnVrfRTType.setStatus(_B)
class _MplsL3VpnVrfRT_Type(MplsL3VpnRouteDistinguisher):defaultValue=OctetString('')
_MplsL3VpnVrfRT_Type.__name__=_O
_MplsL3VpnVrfRT_Object=MibTableColumn
mplsL3VpnVrfRT=_MplsL3VpnVrfRT_Object((1,3,6,1,2,1,10,166,11,1,2,3,1,4),_MplsL3VpnVrfRT_Type())
mplsL3VpnVrfRT.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRT.setStatus(_B)
class _MplsL3VpnVrfRTDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_MplsL3VpnVrfRTDescr_Type.__name__=_N
_MplsL3VpnVrfRTDescr_Object=MibTableColumn
mplsL3VpnVrfRTDescr=_MplsL3VpnVrfRTDescr_Object((1,3,6,1,2,1,10,166,11,1,2,3,1,5),_MplsL3VpnVrfRTDescr_Type())
mplsL3VpnVrfRTDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRTDescr.setStatus(_B)
_MplsL3VpnVrfRTRowStatus_Type=RowStatus
_MplsL3VpnVrfRTRowStatus_Object=MibTableColumn
mplsL3VpnVrfRTRowStatus=_MplsL3VpnVrfRTRowStatus_Object((1,3,6,1,2,1,10,166,11,1,2,3,1,6),_MplsL3VpnVrfRTRowStatus_Type())
mplsL3VpnVrfRTRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRTRowStatus.setStatus(_B)
class _MplsL3VpnVrfRTStorageType_Type(StorageType):defaultValue=2
_MplsL3VpnVrfRTStorageType_Type.__name__=_J
_MplsL3VpnVrfRTStorageType_Object=MibTableColumn
mplsL3VpnVrfRTStorageType=_MplsL3VpnVrfRTStorageType_Object((1,3,6,1,2,1,10,166,11,1,2,3,1,7),_MplsL3VpnVrfRTStorageType_Type())
mplsL3VpnVrfRTStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRTStorageType.setStatus(_B)
_MplsL3VpnVrfSecTable_Object=MibTable
mplsL3VpnVrfSecTable=_MplsL3VpnVrfSecTable_Object((1,3,6,1,2,1,10,166,11,1,2,6))
if mibBuilder.loadTexts:mplsL3VpnVrfSecTable.setStatus(_B)
_MplsL3VpnVrfSecEntry_Object=MibTableRow
mplsL3VpnVrfSecEntry=_MplsL3VpnVrfSecEntry_Object((1,3,6,1,2,1,10,166,11,1,2,6,1))
if mibBuilder.loadTexts:mplsL3VpnVrfSecEntry.setStatus(_B)
_MplsL3VpnVrfSecIllegalLblVltns_Type=Counter32
_MplsL3VpnVrfSecIllegalLblVltns_Object=MibTableColumn
mplsL3VpnVrfSecIllegalLblVltns=_MplsL3VpnVrfSecIllegalLblVltns_Object((1,3,6,1,2,1,10,166,11,1,2,6,1,1),_MplsL3VpnVrfSecIllegalLblVltns_Type())
mplsL3VpnVrfSecIllegalLblVltns.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfSecIllegalLblVltns.setStatus(_B)
_MplsL3VpnVrfSecDiscontinuityTime_Type=TimeStamp
_MplsL3VpnVrfSecDiscontinuityTime_Object=MibTableColumn
mplsL3VpnVrfSecDiscontinuityTime=_MplsL3VpnVrfSecDiscontinuityTime_Object((1,3,6,1,2,1,10,166,11,1,2,6,1,2),_MplsL3VpnVrfSecDiscontinuityTime_Type())
mplsL3VpnVrfSecDiscontinuityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfSecDiscontinuityTime.setStatus(_B)
_MplsL3VpnPerf_ObjectIdentity=ObjectIdentity
mplsL3VpnPerf=_MplsL3VpnPerf_ObjectIdentity((1,3,6,1,2,1,10,166,11,1,3))
_MplsL3VpnVrfPerfTable_Object=MibTable
mplsL3VpnVrfPerfTable=_MplsL3VpnVrfPerfTable_Object((1,3,6,1,2,1,10,166,11,1,3,1))
if mibBuilder.loadTexts:mplsL3VpnVrfPerfTable.setStatus(_B)
_MplsL3VpnVrfPerfEntry_Object=MibTableRow
mplsL3VpnVrfPerfEntry=_MplsL3VpnVrfPerfEntry_Object((1,3,6,1,2,1,10,166,11,1,3,1,1))
if mibBuilder.loadTexts:mplsL3VpnVrfPerfEntry.setStatus(_B)
_MplsL3VpnVrfPerfRoutesAdded_Type=Counter32
_MplsL3VpnVrfPerfRoutesAdded_Object=MibTableColumn
mplsL3VpnVrfPerfRoutesAdded=_MplsL3VpnVrfPerfRoutesAdded_Object((1,3,6,1,2,1,10,166,11,1,3,1,1,1),_MplsL3VpnVrfPerfRoutesAdded_Type())
mplsL3VpnVrfPerfRoutesAdded.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfPerfRoutesAdded.setStatus(_B)
_MplsL3VpnVrfPerfRoutesDeleted_Type=Counter32
_MplsL3VpnVrfPerfRoutesDeleted_Object=MibTableColumn
mplsL3VpnVrfPerfRoutesDeleted=_MplsL3VpnVrfPerfRoutesDeleted_Object((1,3,6,1,2,1,10,166,11,1,3,1,1,2),_MplsL3VpnVrfPerfRoutesDeleted_Type())
mplsL3VpnVrfPerfRoutesDeleted.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfPerfRoutesDeleted.setStatus(_B)
_MplsL3VpnVrfPerfCurrNumRoutes_Type=Gauge32
_MplsL3VpnVrfPerfCurrNumRoutes_Object=MibTableColumn
mplsL3VpnVrfPerfCurrNumRoutes=_MplsL3VpnVrfPerfCurrNumRoutes_Object((1,3,6,1,2,1,10,166,11,1,3,1,1,3),_MplsL3VpnVrfPerfCurrNumRoutes_Type())
mplsL3VpnVrfPerfCurrNumRoutes.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfPerfCurrNumRoutes.setStatus(_B)
_MplsL3VpnVrfPerfRoutesDropped_Type=Counter32
_MplsL3VpnVrfPerfRoutesDropped_Object=MibTableColumn
mplsL3VpnVrfPerfRoutesDropped=_MplsL3VpnVrfPerfRoutesDropped_Object((1,3,6,1,2,1,10,166,11,1,3,1,1,4),_MplsL3VpnVrfPerfRoutesDropped_Type())
mplsL3VpnVrfPerfRoutesDropped.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfPerfRoutesDropped.setStatus(_B)
_MplsL3VpnVrfPerfDiscTime_Type=TimeStamp
_MplsL3VpnVrfPerfDiscTime_Object=MibTableColumn
mplsL3VpnVrfPerfDiscTime=_MplsL3VpnVrfPerfDiscTime_Object((1,3,6,1,2,1,10,166,11,1,3,1,1,5),_MplsL3VpnVrfPerfDiscTime_Type())
mplsL3VpnVrfPerfDiscTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfPerfDiscTime.setStatus(_B)
_MplsL3VpnRoute_ObjectIdentity=ObjectIdentity
mplsL3VpnRoute=_MplsL3VpnRoute_ObjectIdentity((1,3,6,1,2,1,10,166,11,1,4))
_MplsL3VpnVrfRteTable_Object=MibTable
mplsL3VpnVrfRteTable=_MplsL3VpnVrfRteTable_Object((1,3,6,1,2,1,10,166,11,1,4,1))
if mibBuilder.loadTexts:mplsL3VpnVrfRteTable.setStatus(_B)
_MplsL3VpnVrfRteEntry_Object=MibTableRow
mplsL3VpnVrfRteEntry=_MplsL3VpnVrfRteEntry_Object((1,3,6,1,2,1,10,166,11,1,4,1,1))
mplsL3VpnVrfRteEntry.setIndexNames((0,_A,_H),(0,_A,_i),(0,_A,_j),(0,_A,_k),(0,_A,_l),(0,_A,_m),(0,_A,_n))
if mibBuilder.loadTexts:mplsL3VpnVrfRteEntry.setStatus(_B)
_MplsL3VpnVrfRteInetCidrDestType_Type=InetAddressType
_MplsL3VpnVrfRteInetCidrDestType_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrDestType=_MplsL3VpnVrfRteInetCidrDestType_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,1),_MplsL3VpnVrfRteInetCidrDestType_Type())
mplsL3VpnVrfRteInetCidrDestType.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrDestType.setStatus(_B)
_MplsL3VpnVrfRteInetCidrDest_Type=InetAddress
_MplsL3VpnVrfRteInetCidrDest_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrDest=_MplsL3VpnVrfRteInetCidrDest_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,2),_MplsL3VpnVrfRteInetCidrDest_Type())
mplsL3VpnVrfRteInetCidrDest.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrDest.setStatus(_B)
class _MplsL3VpnVrfRteInetCidrPfxLen_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_MplsL3VpnVrfRteInetCidrPfxLen_Type.__name__=_b
_MplsL3VpnVrfRteInetCidrPfxLen_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrPfxLen=_MplsL3VpnVrfRteInetCidrPfxLen_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,3),_MplsL3VpnVrfRteInetCidrPfxLen_Type())
mplsL3VpnVrfRteInetCidrPfxLen.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrPfxLen.setStatus(_B)
_MplsL3VpnVrfRteInetCidrPolicy_Type=ObjectIdentifier
_MplsL3VpnVrfRteInetCidrPolicy_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrPolicy=_MplsL3VpnVrfRteInetCidrPolicy_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,4),_MplsL3VpnVrfRteInetCidrPolicy_Type())
mplsL3VpnVrfRteInetCidrPolicy.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrPolicy.setStatus(_B)
_MplsL3VpnVrfRteInetCidrNHopType_Type=InetAddressType
_MplsL3VpnVrfRteInetCidrNHopType_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrNHopType=_MplsL3VpnVrfRteInetCidrNHopType_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,5),_MplsL3VpnVrfRteInetCidrNHopType_Type())
mplsL3VpnVrfRteInetCidrNHopType.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrNHopType.setStatus(_B)
_MplsL3VpnVrfRteInetCidrNextHop_Type=InetAddress
_MplsL3VpnVrfRteInetCidrNextHop_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrNextHop=_MplsL3VpnVrfRteInetCidrNextHop_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,6),_MplsL3VpnVrfRteInetCidrNextHop_Type())
mplsL3VpnVrfRteInetCidrNextHop.setMaxAccess(_F)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrNextHop.setStatus(_B)
class _MplsL3VpnVrfRteInetCidrIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_MplsL3VpnVrfRteInetCidrIfIndex_Type.__name__=_a
_MplsL3VpnVrfRteInetCidrIfIndex_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrIfIndex=_MplsL3VpnVrfRteInetCidrIfIndex_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,7),_MplsL3VpnVrfRteInetCidrIfIndex_Type())
mplsL3VpnVrfRteInetCidrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrIfIndex.setStatus(_B)
class _MplsL3VpnVrfRteInetCidrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('reject',2),('local',3),('remote',4),('blackhole',5)))
_MplsL3VpnVrfRteInetCidrType_Type.__name__=_E
_MplsL3VpnVrfRteInetCidrType_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrType=_MplsL3VpnVrfRteInetCidrType_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,8),_MplsL3VpnVrfRteInetCidrType_Type())
mplsL3VpnVrfRteInetCidrType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrType.setStatus(_B)
_MplsL3VpnVrfRteInetCidrProto_Type=IANAipRouteProtocol
_MplsL3VpnVrfRteInetCidrProto_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrProto=_MplsL3VpnVrfRteInetCidrProto_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,9),_MplsL3VpnVrfRteInetCidrProto_Type())
mplsL3VpnVrfRteInetCidrProto.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrProto.setStatus(_B)
_MplsL3VpnVrfRteInetCidrAge_Type=Gauge32
_MplsL3VpnVrfRteInetCidrAge_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrAge=_MplsL3VpnVrfRteInetCidrAge_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,10),_MplsL3VpnVrfRteInetCidrAge_Type())
mplsL3VpnVrfRteInetCidrAge.setMaxAccess(_D)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrAge.setStatus(_B)
class _MplsL3VpnVrfRteInetCidrNextHopAS_Type(InetAutonomousSystemNumber):defaultValue=0
_MplsL3VpnVrfRteInetCidrNextHopAS_Type.__name__=_c
_MplsL3VpnVrfRteInetCidrNextHopAS_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrNextHopAS=_MplsL3VpnVrfRteInetCidrNextHopAS_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,11),_MplsL3VpnVrfRteInetCidrNextHopAS_Type())
mplsL3VpnVrfRteInetCidrNextHopAS.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrNextHopAS.setStatus(_B)
class _MplsL3VpnVrfRteInetCidrMetric1_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_MplsL3VpnVrfRteInetCidrMetric1_Type.__name__=_E
_MplsL3VpnVrfRteInetCidrMetric1_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrMetric1=_MplsL3VpnVrfRteInetCidrMetric1_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,12),_MplsL3VpnVrfRteInetCidrMetric1_Type())
mplsL3VpnVrfRteInetCidrMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrMetric1.setStatus(_B)
class _MplsL3VpnVrfRteInetCidrMetric2_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_MplsL3VpnVrfRteInetCidrMetric2_Type.__name__=_E
_MplsL3VpnVrfRteInetCidrMetric2_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrMetric2=_MplsL3VpnVrfRteInetCidrMetric2_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,13),_MplsL3VpnVrfRteInetCidrMetric2_Type())
mplsL3VpnVrfRteInetCidrMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrMetric2.setStatus(_B)
class _MplsL3VpnVrfRteInetCidrMetric3_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_MplsL3VpnVrfRteInetCidrMetric3_Type.__name__=_E
_MplsL3VpnVrfRteInetCidrMetric3_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrMetric3=_MplsL3VpnVrfRteInetCidrMetric3_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,14),_MplsL3VpnVrfRteInetCidrMetric3_Type())
mplsL3VpnVrfRteInetCidrMetric3.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrMetric3.setStatus(_B)
class _MplsL3VpnVrfRteInetCidrMetric4_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_MplsL3VpnVrfRteInetCidrMetric4_Type.__name__=_E
_MplsL3VpnVrfRteInetCidrMetric4_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrMetric4=_MplsL3VpnVrfRteInetCidrMetric4_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,15),_MplsL3VpnVrfRteInetCidrMetric4_Type())
mplsL3VpnVrfRteInetCidrMetric4.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrMetric4.setStatus(_B)
class _MplsL3VpnVrfRteInetCidrMetric5_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,2147483647))
_MplsL3VpnVrfRteInetCidrMetric5_Type.__name__=_E
_MplsL3VpnVrfRteInetCidrMetric5_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrMetric5=_MplsL3VpnVrfRteInetCidrMetric5_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,16),_MplsL3VpnVrfRteInetCidrMetric5_Type())
mplsL3VpnVrfRteInetCidrMetric5.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrMetric5.setStatus(_B)
_MplsL3VpnVrfRteXCPointer_Type=MplsIndexType
_MplsL3VpnVrfRteXCPointer_Object=MibTableColumn
mplsL3VpnVrfRteXCPointer=_MplsL3VpnVrfRteXCPointer_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,17),_MplsL3VpnVrfRteXCPointer_Type())
mplsL3VpnVrfRteXCPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRteXCPointer.setStatus(_B)
_MplsL3VpnVrfRteInetCidrStatus_Type=RowStatus
_MplsL3VpnVrfRteInetCidrStatus_Object=MibTableColumn
mplsL3VpnVrfRteInetCidrStatus=_MplsL3VpnVrfRteInetCidrStatus_Object((1,3,6,1,2,1,10,166,11,1,4,1,1,18),_MplsL3VpnVrfRteInetCidrStatus_Type())
mplsL3VpnVrfRteInetCidrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsL3VpnVrfRteInetCidrStatus.setStatus(_B)
_MplsL3VpnConformance_ObjectIdentity=ObjectIdentity
mplsL3VpnConformance=_MplsL3VpnConformance_ObjectIdentity((1,3,6,1,2,1,10,166,11,2))
_MplsL3VpnGroups_ObjectIdentity=ObjectIdentity
mplsL3VpnGroups=_MplsL3VpnGroups_ObjectIdentity((1,3,6,1,2,1,10,166,11,2,1))
_MplsL3VpnCompliances_ObjectIdentity=ObjectIdentity
mplsL3VpnCompliances=_MplsL3VpnCompliances_ObjectIdentity((1,3,6,1,2,1,10,166,11,2,2))
mplsL3VpnVrfEntry.registerAugmentions((_A,_o))
mplsL3VpnVrfSecEntry.setIndexNames(*mplsL3VpnVrfEntry.getIndexNames())
mplsL3VpnVrfEntry.registerAugmentions((_A,_p))
mplsL3VpnVrfPerfEntry.setIndexNames(*mplsL3VpnVrfEntry.getIndexNames())
mplsL3VpnScalarGroup=ObjectGroup((1,3,6,1,2,1,10,166,11,2,1,1))
mplsL3VpnScalarGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:mplsL3VpnScalarGroup.setStatus(_B)
mplsL3VpnVrfGroup=ObjectGroup((1,3,6,1,2,1,10,166,11,2,1,2))
mplsL3VpnVrfGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_K),(_A,_A1),(_A,_A2),(_A,_P),(_A,_L),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:mplsL3VpnVrfGroup.setStatus(_B)
mplsL3VpnIfGroup=ObjectGroup((1,3,6,1,2,1,10,166,11,2,1,3))
mplsL3VpnIfGroup.setObjects(*((_A,_A8),(_A,_A9),(_A,_AA),(_A,_M)))
if mibBuilder.loadTexts:mplsL3VpnIfGroup.setStatus(_B)
mplsL3VpnPerfGroup=ObjectGroup((1,3,6,1,2,1,10,166,11,2,1,4))
mplsL3VpnPerfGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_I)))
if mibBuilder.loadTexts:mplsL3VpnPerfGroup.setStatus(_B)
mplsL3VpnPerfRouteGroup=ObjectGroup((1,3,6,1,2,1,10,166,11,2,1,5))
mplsL3VpnPerfRouteGroup.setObjects(*((_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:mplsL3VpnPerfRouteGroup.setStatus(_B)
mplsL3VpnSecGroup=ObjectGroup((1,3,6,1,2,1,10,166,11,2,1,7))
mplsL3VpnSecGroup.setObjects(*((_A,_Q),(_A,_AF)))
if mibBuilder.loadTexts:mplsL3VpnSecGroup.setStatus(_B)
mplsL3VpnVrfRteGroup=ObjectGroup((1,3,6,1,2,1,10,166,11,2,1,8))
mplsL3VpnVrfRteGroup.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:mplsL3VpnVrfRteGroup.setStatus(_B)
mplsL3VpnVrfRTGroup=ObjectGroup((1,3,6,1,2,1,10,166,11,2,1,9))
mplsL3VpnVrfRTGroup.setObjects(*((_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:mplsL3VpnVrfRTGroup.setStatus(_B)
mplsL3VpnVrfUp=NotificationType((1,3,6,1,2,1,10,166,11,0,1))
mplsL3VpnVrfUp.setObjects(*((_A,_M),(_A,_K)))
if mibBuilder.loadTexts:mplsL3VpnVrfUp.setStatus(_B)
mplsL3VpnVrfDown=NotificationType((1,3,6,1,2,1,10,166,11,0,2))
mplsL3VpnVrfDown.setObjects(*((_A,_M),(_A,_K)))
if mibBuilder.loadTexts:mplsL3VpnVrfDown.setStatus(_B)
mplsL3VpnVrfRouteMidThreshExceeded=NotificationType((1,3,6,1,2,1,10,166,11,0,3))
mplsL3VpnVrfRouteMidThreshExceeded.setObjects(*((_A,_I),(_A,_P)))
if mibBuilder.loadTexts:mplsL3VpnVrfRouteMidThreshExceeded.setStatus(_B)
mplsL3VpnVrfNumVrfRouteMaxThreshExceeded=NotificationType((1,3,6,1,2,1,10,166,11,0,4))
mplsL3VpnVrfNumVrfRouteMaxThreshExceeded.setObjects(*((_A,_I),(_A,_L)))
if mibBuilder.loadTexts:mplsL3VpnVrfNumVrfRouteMaxThreshExceeded.setStatus(_B)
mplsL3VpnNumVrfSecIllglLblThrshExcd=NotificationType((1,3,6,1,2,1,10,166,11,0,5))
mplsL3VpnNumVrfSecIllglLblThrshExcd.setObjects((_A,_Q))
if mibBuilder.loadTexts:mplsL3VpnNumVrfSecIllglLblThrshExcd.setStatus(_B)
mplsL3VpnNumVrfRouteMaxThreshCleared=NotificationType((1,3,6,1,2,1,10,166,11,0,6))
mplsL3VpnNumVrfRouteMaxThreshCleared.setObjects(*((_A,_I),(_A,_L)))
if mibBuilder.loadTexts:mplsL3VpnNumVrfRouteMaxThreshCleared.setStatus(_B)
mplsL3VpnNotificationGroup=NotificationGroup((1,3,6,1,2,1,10,166,11,2,1,10))
mplsL3VpnNotificationGroup.setObjects(*((_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:mplsL3VpnNotificationGroup.setStatus(_B)
mplsL3VpnModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,11,2,2,1))
mplsL3VpnModuleFullCompliance.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:mplsL3VpnModuleFullCompliance.setStatus(_B)
mplsL3VpnModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,11,2,2,2))
mplsL3VpnModuleReadOnlyCompliance.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:mplsL3VpnModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'MplsL3VpnName':MplsL3VpnName,_O:MplsL3VpnRouteDistinguisher,'MplsL3VpnRtType':MplsL3VpnRtType,'mplsL3VpnMIB':mplsL3VpnMIB,'mplsL3VpnNotifications':mplsL3VpnNotifications,_AW:mplsL3VpnVrfUp,_AX:mplsL3VpnVrfDown,_AY:mplsL3VpnVrfRouteMidThreshExceeded,_AZ:mplsL3VpnVrfNumVrfRouteMaxThreshExceeded,_Aa:mplsL3VpnNumVrfSecIllglLblThrshExcd,_Ab:mplsL3VpnNumVrfRouteMaxThreshCleared,'mplsL3VpnObjects':mplsL3VpnObjects,'mplsL3VpnScalars':mplsL3VpnScalars,_q:mplsL3VpnConfiguredVrfs,_r:mplsL3VpnActiveVrfs,_s:mplsL3VpnConnectedInterfaces,_t:mplsL3VpnNotificationEnable,_u:mplsL3VpnVrfConfMaxPossRts,_v:mplsL3VpnVrfConfRteMxThrshTime,_w:mplsL3VpnIllLblRcvThrsh,'mplsL3VpnConf':mplsL3VpnConf,'mplsL3VpnIfConfTable':mplsL3VpnIfConfTable,'mplsL3VpnIfConfEntry':mplsL3VpnIfConfEntry,_f:mplsL3VpnIfConfIndex,_A8:mplsL3VpnIfVpnClassification,_A9:mplsL3VpnIfVpnRouteDistProtocol,_AA:mplsL3VpnIfConfStorageType,_M:mplsL3VpnIfConfRowStatus,'mplsL3VpnVrfTable':mplsL3VpnVrfTable,'mplsL3VpnVrfEntry':mplsL3VpnVrfEntry,_H:mplsL3VpnVrfName,_x:mplsL3VpnVrfVpnId,_y:mplsL3VpnVrfDescription,_z:mplsL3VpnVrfRD,_A0:mplsL3VpnVrfCreationTime,_K:mplsL3VpnVrfOperStatus,_A1:mplsL3VpnVrfActiveInterfaces,_A2:mplsL3VpnVrfAssociatedInterfaces,_P:mplsL3VpnVrfConfMidRteThresh,_L:mplsL3VpnVrfConfHighRteThresh,_A3:mplsL3VpnVrfConfMaxRoutes,_A4:mplsL3VpnVrfConfLastChanged,_A5:mplsL3VpnVrfConfRowStatus,_A6:mplsL3VpnVrfConfAdminStatus,_A7:mplsL3VpnVrfConfStorageType,'mplsL3VpnVrfRTTable':mplsL3VpnVrfRTTable,'mplsL3VpnVrfRTEntry':mplsL3VpnVrfRTEntry,_g:mplsL3VpnVrfRTIndex,_h:mplsL3VpnVrfRTType,_AT:mplsL3VpnVrfRT,_AS:mplsL3VpnVrfRTDescr,_AU:mplsL3VpnVrfRTRowStatus,_AV:mplsL3VpnVrfRTStorageType,'mplsL3VpnVrfSecTable':mplsL3VpnVrfSecTable,_o:mplsL3VpnVrfSecEntry,_Q:mplsL3VpnVrfSecIllegalLblVltns,_AF:mplsL3VpnVrfSecDiscontinuityTime,'mplsL3VpnPerf':mplsL3VpnPerf,'mplsL3VpnVrfPerfTable':mplsL3VpnVrfPerfTable,_p:mplsL3VpnVrfPerfEntry,_AB:mplsL3VpnVrfPerfRoutesAdded,_AC:mplsL3VpnVrfPerfRoutesDeleted,_I:mplsL3VpnVrfPerfCurrNumRoutes,_AD:mplsL3VpnVrfPerfRoutesDropped,_AE:mplsL3VpnVrfPerfDiscTime,'mplsL3VpnRoute':mplsL3VpnRoute,'mplsL3VpnVrfRteTable':mplsL3VpnVrfRteTable,'mplsL3VpnVrfRteEntry':mplsL3VpnVrfRteEntry,_i:mplsL3VpnVrfRteInetCidrDestType,_j:mplsL3VpnVrfRteInetCidrDest,_k:mplsL3VpnVrfRteInetCidrPfxLen,_l:mplsL3VpnVrfRteInetCidrPolicy,_m:mplsL3VpnVrfRteInetCidrNHopType,_n:mplsL3VpnVrfRteInetCidrNextHop,_AG:mplsL3VpnVrfRteInetCidrIfIndex,_AH:mplsL3VpnVrfRteInetCidrType,_AI:mplsL3VpnVrfRteInetCidrProto,_AJ:mplsL3VpnVrfRteInetCidrAge,_AK:mplsL3VpnVrfRteInetCidrNextHopAS,_AL:mplsL3VpnVrfRteInetCidrMetric1,_AM:mplsL3VpnVrfRteInetCidrMetric2,_AN:mplsL3VpnVrfRteInetCidrMetric3,_AO:mplsL3VpnVrfRteInetCidrMetric4,_AP:mplsL3VpnVrfRteInetCidrMetric5,_AQ:mplsL3VpnVrfRteXCPointer,_AR:mplsL3VpnVrfRteInetCidrStatus,'mplsL3VpnConformance':mplsL3VpnConformance,'mplsL3VpnGroups':mplsL3VpnGroups,_R:mplsL3VpnScalarGroup,_S:mplsL3VpnVrfGroup,_T:mplsL3VpnIfGroup,_U:mplsL3VpnPerfGroup,_Z:mplsL3VpnPerfRouteGroup,_X:mplsL3VpnSecGroup,_V:mplsL3VpnVrfRteGroup,_W:mplsL3VpnVrfRTGroup,_Y:mplsL3VpnNotificationGroup,'mplsL3VpnCompliances':mplsL3VpnCompliances,'mplsL3VpnModuleFullCompliance':mplsL3VpnModuleFullCompliance,'mplsL3VpnModuleReadOnlyCompliance':mplsL3VpnModuleReadOnlyCompliance})