_AJ='ciscoMvpnMvrfChange'
_AI='ciscoMvpnTunnelMvrf'
_AH='ciscoMvpnTunnelName'
_AG='ciscoMvpnMdtJnSendMdtRefCt'
_AF='ciscoMvpnMdtJnSendMdtGroup'
_AE='ciscoMvpnMdtJnSendMdtGrpAddrType'
_AD='ciscoMvpnMdtJnRcvExpTime'
_AC='ciscoMvpnMdtJnRcvUpTime'
_AB='ciscoMvpnBgpMdtUpdateNexthop'
_AA='ciscoMvpnBgpMdtUpdNhAddrType'
_A9='ciscoMvpnBgpMdtUpdateOriginator'
_A8='ciscoMvpnBgpMdtUpdOrigAddrType'
_A7='ciscoMvpnBgpMdtUpdateRd'
_A6='ciscoMvpnMrouteMdtType'
_A5='ciscoMvpnMrouteMdtGroup'
_A4='ciscoMvpnMrouteMdtGrpAddrType'
_A3='ciscoMvpnMdtDataRowStatus'
_A2='ciscoMvpnMdtDataThreshold'
_A1='ciscoMvpnMdtDataWildcardBits'
_A0='ciscoMvpnMdtDataWildcardType'
_z='ciscoMvpnMdtDataRangeAddress'
_y='ciscoMvpnMdtDataRangeAddrType'
_x='ciscoMvpnMdtDefaultRowStatus'
_w='ciscoMvpnMdtEncapsType'
_v='ciscoMvpnMdtDefaultAddress'
_u='ciscoMvpnMdtDefaultAddrType'
_t='ciscoMvpnGenRowStatus'
_s='ciscoMvpnGenAssociatedInterfaces'
_r='ciscoMvpnGenOperChangeTime'
_q='ciscoMvpnNotificationEnable'
_p='ciscoMvpnMvrfNumber'
_o='ciscoMvpnMdtJnSendSource'
_n='ciscoMvpnMdtJnSendSrcAddrType'
_m='ciscoMvpnMdtJnSendGroup'
_l='ciscoMvpnMdtJnSendGrpAddrType'
_k='ciscoMvpnMdtJnRcvSource'
_j='ciscoMvpnMdtJnRcvSrcAddrType'
_i='ciscoMvpnMdtJnRcvGroup'
_h='ciscoMvpnMdtJnRcvGrpAddrType'
_g='ciscoMvpnBgpMdtUpdateSource'
_f='ciscoMvpnBgpMdtUpdSrcAddrType'
_e='ciscoMvpnBgpMdtUpdateGroup'
_d='ciscoMvpnBgpMdtUpdGrpAddrType'
_c='ciscoMvpnMrouteUpDownStreamInfo'
_b='ciscoMvpnMrouteMvrfSource'
_a='ciscoMvpnMrouteMvrfSrcAddrType'
_Z='ciscoMvpnMrouteMvrfGroup'
_Y='ciscoMvpnMrouteMvrfGrpAddrType'
_X='TruthValue'
_W='ifIndex'
_V='IF-MIB'
_U='ciscoMvpnNotificationGroup'
_T='ciscoMvpnTunnelGroup'
_S='ciscoMvpnMIBMdtJnSendGroup'
_R='ciscoMvpnMIBMdtJnRcvGroup'
_Q='ciscoMvpnMIBBgpMdtUpdateGroup'
_P='ciscoMvpnMIBMrouteMdtGroup'
_O='ciscoMvpnMIBMdtDataGroup'
_N='ciscoMvpnMIBMdtDefaultGroup'
_M='ciscoMvpnMIBGenericGroup'
_L='ciscoMvpnScalarGroup'
_K='ciscoMvpnGenOperStatusChange'
_J='Unsigned32'
_I='Integer32'
_H='mplsVpnVrfName'
_G='MPLS-VPN-MIB'
_F='InetAddress'
_E='read-create'
_D='not-accessible'
_C='read-only'
_B='CISCO-MVPN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_V,_W)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressType')
MplsVpnRouteDistinguisher,mplsVpnVrfName=mibBuilder.importSymbols(_G,'MplsVpnRouteDistinguisher',_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp',_X)
ciscoMvpnMIB=ModuleIdentity((1,3,6,1,4,1,9,10,113))
if mibBuilder.loadTexts:ciscoMvpnMIB.setRevisions(('2004-02-23 12:00',))
_CiscoMvpnNotifications_ObjectIdentity=ObjectIdentity
ciscoMvpnNotifications=_CiscoMvpnNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,113,0))
_CiscoMvpnObjects_ObjectIdentity=ObjectIdentity
ciscoMvpnObjects=_CiscoMvpnObjects_ObjectIdentity((1,3,6,1,4,1,9,10,113,1))
_CiscoMvpnScalars_ObjectIdentity=ObjectIdentity
ciscoMvpnScalars=_CiscoMvpnScalars_ObjectIdentity((1,3,6,1,4,1,9,10,113,1,1))
_CiscoMvpnMvrfNumber_Type=Unsigned32
_CiscoMvpnMvrfNumber_Object=MibScalar
ciscoMvpnMvrfNumber=_CiscoMvpnMvrfNumber_Object((1,3,6,1,4,1,9,10,113,1,1,1),_CiscoMvpnMvrfNumber_Type())
ciscoMvpnMvrfNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnMvrfNumber.setStatus(_A)
class _CiscoMvpnNotificationEnable_Type(TruthValue):defaultValue=2
_CiscoMvpnNotificationEnable_Type.__name__=_X
_CiscoMvpnNotificationEnable_Object=MibScalar
ciscoMvpnNotificationEnable=_CiscoMvpnNotificationEnable_Object((1,3,6,1,4,1,9,10,113,1,1,2),_CiscoMvpnNotificationEnable_Type())
ciscoMvpnNotificationEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:ciscoMvpnNotificationEnable.setStatus(_A)
_CiscoMvpnGeneric_ObjectIdentity=ObjectIdentity
ciscoMvpnGeneric=_CiscoMvpnGeneric_ObjectIdentity((1,3,6,1,4,1,9,10,113,1,2))
_CiscoMvpnGenericTable_Object=MibTable
ciscoMvpnGenericTable=_CiscoMvpnGenericTable_Object((1,3,6,1,4,1,9,10,113,1,2,1))
if mibBuilder.loadTexts:ciscoMvpnGenericTable.setStatus(_A)
_CiscoMvpnGenericEntry_Object=MibTableRow
ciscoMvpnGenericEntry=_CiscoMvpnGenericEntry_Object((1,3,6,1,4,1,9,10,113,1,2,1,1))
ciscoMvpnGenericEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ciscoMvpnGenericEntry.setStatus(_A)
class _CiscoMvpnGenOperStatusChange_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('createdMvrf',1),('deletedMvrf',2),('modifiedMvrfDefMdtConfig',3),('modifiedMvrfDataMdtConfig',4)))
_CiscoMvpnGenOperStatusChange_Type.__name__=_I
_CiscoMvpnGenOperStatusChange_Object=MibTableColumn
ciscoMvpnGenOperStatusChange=_CiscoMvpnGenOperStatusChange_Object((1,3,6,1,4,1,9,10,113,1,2,1,1,1),_CiscoMvpnGenOperStatusChange_Type())
ciscoMvpnGenOperStatusChange.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnGenOperStatusChange.setStatus(_A)
_CiscoMvpnGenOperChangeTime_Type=TimeStamp
_CiscoMvpnGenOperChangeTime_Object=MibTableColumn
ciscoMvpnGenOperChangeTime=_CiscoMvpnGenOperChangeTime_Object((1,3,6,1,4,1,9,10,113,1,2,1,1,2),_CiscoMvpnGenOperChangeTime_Type())
ciscoMvpnGenOperChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnGenOperChangeTime.setStatus(_A)
_CiscoMvpnGenAssociatedInterfaces_Type=Unsigned32
_CiscoMvpnGenAssociatedInterfaces_Object=MibTableColumn
ciscoMvpnGenAssociatedInterfaces=_CiscoMvpnGenAssociatedInterfaces_Object((1,3,6,1,4,1,9,10,113,1,2,1,1,3),_CiscoMvpnGenAssociatedInterfaces_Type())
ciscoMvpnGenAssociatedInterfaces.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnGenAssociatedInterfaces.setStatus(_A)
_CiscoMvpnGenRowStatus_Type=RowStatus
_CiscoMvpnGenRowStatus_Object=MibTableColumn
ciscoMvpnGenRowStatus=_CiscoMvpnGenRowStatus_Object((1,3,6,1,4,1,9,10,113,1,2,1,1,4),_CiscoMvpnGenRowStatus_Type())
ciscoMvpnGenRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoMvpnGenRowStatus.setStatus(_A)
_CiscoMvpnConfig_ObjectIdentity=ObjectIdentity
ciscoMvpnConfig=_CiscoMvpnConfig_ObjectIdentity((1,3,6,1,4,1,9,10,113,1,3))
_CiscoMvpnMdtDefaultTable_Object=MibTable
ciscoMvpnMdtDefaultTable=_CiscoMvpnMdtDefaultTable_Object((1,3,6,1,4,1,9,10,113,1,3,1))
if mibBuilder.loadTexts:ciscoMvpnMdtDefaultTable.setStatus(_A)
_CiscoMvpnMdtDefaultEntry_Object=MibTableRow
ciscoMvpnMdtDefaultEntry=_CiscoMvpnMdtDefaultEntry_Object((1,3,6,1,4,1,9,10,113,1,3,1,1))
ciscoMvpnMdtDefaultEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ciscoMvpnMdtDefaultEntry.setStatus(_A)
_CiscoMvpnMdtDefaultAddrType_Type=InetAddressType
_CiscoMvpnMdtDefaultAddrType_Object=MibTableColumn
ciscoMvpnMdtDefaultAddrType=_CiscoMvpnMdtDefaultAddrType_Object((1,3,6,1,4,1,9,10,113,1,3,1,1,1),_CiscoMvpnMdtDefaultAddrType_Type())
ciscoMvpnMdtDefaultAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoMvpnMdtDefaultAddrType.setStatus(_A)
_CiscoMvpnMdtDefaultAddress_Type=InetAddress
_CiscoMvpnMdtDefaultAddress_Object=MibTableColumn
ciscoMvpnMdtDefaultAddress=_CiscoMvpnMdtDefaultAddress_Object((1,3,6,1,4,1,9,10,113,1,3,1,1,2),_CiscoMvpnMdtDefaultAddress_Type())
ciscoMvpnMdtDefaultAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoMvpnMdtDefaultAddress.setStatus(_A)
class _CiscoMvpnMdtEncapsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('greIp',1),('ipIp',2),('mpls',3)))
_CiscoMvpnMdtEncapsType_Type.__name__=_I
_CiscoMvpnMdtEncapsType_Object=MibTableColumn
ciscoMvpnMdtEncapsType=_CiscoMvpnMdtEncapsType_Object((1,3,6,1,4,1,9,10,113,1,3,1,1,3),_CiscoMvpnMdtEncapsType_Type())
ciscoMvpnMdtEncapsType.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoMvpnMdtEncapsType.setStatus(_A)
_CiscoMvpnMdtDefaultRowStatus_Type=RowStatus
_CiscoMvpnMdtDefaultRowStatus_Object=MibTableColumn
ciscoMvpnMdtDefaultRowStatus=_CiscoMvpnMdtDefaultRowStatus_Object((1,3,6,1,4,1,9,10,113,1,3,1,1,4),_CiscoMvpnMdtDefaultRowStatus_Type())
ciscoMvpnMdtDefaultRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoMvpnMdtDefaultRowStatus.setStatus(_A)
_CiscoMvpnMdtDataTable_Object=MibTable
ciscoMvpnMdtDataTable=_CiscoMvpnMdtDataTable_Object((1,3,6,1,4,1,9,10,113,1,3,2))
if mibBuilder.loadTexts:ciscoMvpnMdtDataTable.setStatus(_A)
_CiscoMvpnMdtDataEntry_Object=MibTableRow
ciscoMvpnMdtDataEntry=_CiscoMvpnMdtDataEntry_Object((1,3,6,1,4,1,9,10,113,1,3,2,1))
ciscoMvpnMdtDataEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:ciscoMvpnMdtDataEntry.setStatus(_A)
_CiscoMvpnMdtDataRangeAddrType_Type=InetAddressType
_CiscoMvpnMdtDataRangeAddrType_Object=MibTableColumn
ciscoMvpnMdtDataRangeAddrType=_CiscoMvpnMdtDataRangeAddrType_Object((1,3,6,1,4,1,9,10,113,1,3,2,1,1),_CiscoMvpnMdtDataRangeAddrType_Type())
ciscoMvpnMdtDataRangeAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoMvpnMdtDataRangeAddrType.setStatus(_A)
_CiscoMvpnMdtDataRangeAddress_Type=InetAddress
_CiscoMvpnMdtDataRangeAddress_Object=MibTableColumn
ciscoMvpnMdtDataRangeAddress=_CiscoMvpnMdtDataRangeAddress_Object((1,3,6,1,4,1,9,10,113,1,3,2,1,2),_CiscoMvpnMdtDataRangeAddress_Type())
ciscoMvpnMdtDataRangeAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoMvpnMdtDataRangeAddress.setStatus(_A)
_CiscoMvpnMdtDataWildcardType_Type=InetAddressType
_CiscoMvpnMdtDataWildcardType_Object=MibTableColumn
ciscoMvpnMdtDataWildcardType=_CiscoMvpnMdtDataWildcardType_Object((1,3,6,1,4,1,9,10,113,1,3,2,1,3),_CiscoMvpnMdtDataWildcardType_Type())
ciscoMvpnMdtDataWildcardType.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoMvpnMdtDataWildcardType.setStatus(_A)
_CiscoMvpnMdtDataWildcardBits_Type=InetAddress
_CiscoMvpnMdtDataWildcardBits_Object=MibTableColumn
ciscoMvpnMdtDataWildcardBits=_CiscoMvpnMdtDataWildcardBits_Object((1,3,6,1,4,1,9,10,113,1,3,2,1,4),_CiscoMvpnMdtDataWildcardBits_Type())
ciscoMvpnMdtDataWildcardBits.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoMvpnMdtDataWildcardBits.setStatus(_A)
class _CiscoMvpnMdtDataThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiscoMvpnMdtDataThreshold_Type.__name__=_J
_CiscoMvpnMdtDataThreshold_Object=MibTableColumn
ciscoMvpnMdtDataThreshold=_CiscoMvpnMdtDataThreshold_Object((1,3,6,1,4,1,9,10,113,1,3,2,1,5),_CiscoMvpnMdtDataThreshold_Type())
ciscoMvpnMdtDataThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoMvpnMdtDataThreshold.setStatus(_A)
if mibBuilder.loadTexts:ciscoMvpnMdtDataThreshold.setUnits('kilobits per second')
_CiscoMvpnMdtDataRowStatus_Type=RowStatus
_CiscoMvpnMdtDataRowStatus_Object=MibTableColumn
ciscoMvpnMdtDataRowStatus=_CiscoMvpnMdtDataRowStatus_Object((1,3,6,1,4,1,9,10,113,1,3,2,1,6),_CiscoMvpnMdtDataRowStatus_Type())
ciscoMvpnMdtDataRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoMvpnMdtDataRowStatus.setStatus(_A)
_CiscoMvpnProtocol_ObjectIdentity=ObjectIdentity
ciscoMvpnProtocol=_CiscoMvpnProtocol_ObjectIdentity((1,3,6,1,4,1,9,10,113,1,4))
_CiscoMvpnMrouteMdtTable_Object=MibTable
ciscoMvpnMrouteMdtTable=_CiscoMvpnMrouteMdtTable_Object((1,3,6,1,4,1,9,10,113,1,4,1))
if mibBuilder.loadTexts:ciscoMvpnMrouteMdtTable.setStatus(_A)
_CiscoMvpnMrouteMdtEntry_Object=MibTableRow
ciscoMvpnMrouteMdtEntry=_CiscoMvpnMrouteMdtEntry_Object((1,3,6,1,4,1,9,10,113,1,4,1,1))
ciscoMvpnMrouteMdtEntry.setIndexNames((0,_G,_H),(0,_B,_Y),(0,_B,_Z),(0,_B,_a),(0,_B,_b),(0,_B,_c))
if mibBuilder.loadTexts:ciscoMvpnMrouteMdtEntry.setStatus(_A)
_CiscoMvpnMrouteMvrfGrpAddrType_Type=InetAddressType
_CiscoMvpnMrouteMvrfGrpAddrType_Object=MibTableColumn
ciscoMvpnMrouteMvrfGrpAddrType=_CiscoMvpnMrouteMvrfGrpAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,1,1,1),_CiscoMvpnMrouteMvrfGrpAddrType_Type())
ciscoMvpnMrouteMvrfGrpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMrouteMvrfGrpAddrType.setStatus(_A)
class _CiscoMvpnMrouteMvrfGroup_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CiscoMvpnMrouteMvrfGroup_Type.__name__=_F
_CiscoMvpnMrouteMvrfGroup_Object=MibTableColumn
ciscoMvpnMrouteMvrfGroup=_CiscoMvpnMrouteMvrfGroup_Object((1,3,6,1,4,1,9,10,113,1,4,1,1,2),_CiscoMvpnMrouteMvrfGroup_Type())
ciscoMvpnMrouteMvrfGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMrouteMvrfGroup.setStatus(_A)
_CiscoMvpnMrouteMvrfSrcAddrType_Type=InetAddressType
_CiscoMvpnMrouteMvrfSrcAddrType_Object=MibTableColumn
ciscoMvpnMrouteMvrfSrcAddrType=_CiscoMvpnMrouteMvrfSrcAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,1,1,3),_CiscoMvpnMrouteMvrfSrcAddrType_Type())
ciscoMvpnMrouteMvrfSrcAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMrouteMvrfSrcAddrType.setStatus(_A)
class _CiscoMvpnMrouteMvrfSource_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CiscoMvpnMrouteMvrfSource_Type.__name__=_F
_CiscoMvpnMrouteMvrfSource_Object=MibTableColumn
ciscoMvpnMrouteMvrfSource=_CiscoMvpnMrouteMvrfSource_Object((1,3,6,1,4,1,9,10,113,1,4,1,1,4),_CiscoMvpnMrouteMvrfSource_Type())
ciscoMvpnMrouteMvrfSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMrouteMvrfSource.setStatus(_A)
class _CiscoMvpnMrouteUpDownStreamInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('upstream',1),('downstream',2)))
_CiscoMvpnMrouteUpDownStreamInfo_Type.__name__=_I
_CiscoMvpnMrouteUpDownStreamInfo_Object=MibTableColumn
ciscoMvpnMrouteUpDownStreamInfo=_CiscoMvpnMrouteUpDownStreamInfo_Object((1,3,6,1,4,1,9,10,113,1,4,1,1,5),_CiscoMvpnMrouteUpDownStreamInfo_Type())
ciscoMvpnMrouteUpDownStreamInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMrouteUpDownStreamInfo.setStatus(_A)
_CiscoMvpnMrouteMdtGrpAddrType_Type=InetAddressType
_CiscoMvpnMrouteMdtGrpAddrType_Object=MibTableColumn
ciscoMvpnMrouteMdtGrpAddrType=_CiscoMvpnMrouteMdtGrpAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,1,1,6),_CiscoMvpnMrouteMdtGrpAddrType_Type())
ciscoMvpnMrouteMdtGrpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnMrouteMdtGrpAddrType.setStatus(_A)
_CiscoMvpnMrouteMdtGroup_Type=InetAddress
_CiscoMvpnMrouteMdtGroup_Object=MibTableColumn
ciscoMvpnMrouteMdtGroup=_CiscoMvpnMrouteMdtGroup_Object((1,3,6,1,4,1,9,10,113,1,4,1,1,7),_CiscoMvpnMrouteMdtGroup_Type())
ciscoMvpnMrouteMdtGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnMrouteMdtGroup.setStatus(_A)
class _CiscoMvpnMrouteMdtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mdtDefault',1),('mdtData',2)))
_CiscoMvpnMrouteMdtType_Type.__name__=_I
_CiscoMvpnMrouteMdtType_Object=MibTableColumn
ciscoMvpnMrouteMdtType=_CiscoMvpnMrouteMdtType_Object((1,3,6,1,4,1,9,10,113,1,4,1,1,8),_CiscoMvpnMrouteMdtType_Type())
ciscoMvpnMrouteMdtType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnMrouteMdtType.setStatus(_A)
_CiscoMvpnBgpMdtUpdateTable_Object=MibTable
ciscoMvpnBgpMdtUpdateTable=_CiscoMvpnBgpMdtUpdateTable_Object((1,3,6,1,4,1,9,10,113,1,4,2))
if mibBuilder.loadTexts:ciscoMvpnBgpMdtUpdateTable.setStatus(_A)
_CiscoMvpnBgpMdtUpdateEntry_Object=MibTableRow
ciscoMvpnBgpMdtUpdateEntry=_CiscoMvpnBgpMdtUpdateEntry_Object((1,3,6,1,4,1,9,10,113,1,4,2,1))
ciscoMvpnBgpMdtUpdateEntry.setIndexNames((0,_B,_d),(0,_B,_e),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:ciscoMvpnBgpMdtUpdateEntry.setStatus(_A)
_CiscoMvpnBgpMdtUpdGrpAddrType_Type=InetAddressType
_CiscoMvpnBgpMdtUpdGrpAddrType_Object=MibTableColumn
ciscoMvpnBgpMdtUpdGrpAddrType=_CiscoMvpnBgpMdtUpdGrpAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,2,1,1),_CiscoMvpnBgpMdtUpdGrpAddrType_Type())
ciscoMvpnBgpMdtUpdGrpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnBgpMdtUpdGrpAddrType.setStatus(_A)
class _CiscoMvpnBgpMdtUpdateGroup_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CiscoMvpnBgpMdtUpdateGroup_Type.__name__=_F
_CiscoMvpnBgpMdtUpdateGroup_Object=MibTableColumn
ciscoMvpnBgpMdtUpdateGroup=_CiscoMvpnBgpMdtUpdateGroup_Object((1,3,6,1,4,1,9,10,113,1,4,2,1,2),_CiscoMvpnBgpMdtUpdateGroup_Type())
ciscoMvpnBgpMdtUpdateGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnBgpMdtUpdateGroup.setStatus(_A)
_CiscoMvpnBgpMdtUpdateRd_Type=MplsVpnRouteDistinguisher
_CiscoMvpnBgpMdtUpdateRd_Object=MibTableColumn
ciscoMvpnBgpMdtUpdateRd=_CiscoMvpnBgpMdtUpdateRd_Object((1,3,6,1,4,1,9,10,113,1,4,2,1,3),_CiscoMvpnBgpMdtUpdateRd_Type())
ciscoMvpnBgpMdtUpdateRd.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnBgpMdtUpdateRd.setStatus(_A)
_CiscoMvpnBgpMdtUpdSrcAddrType_Type=InetAddressType
_CiscoMvpnBgpMdtUpdSrcAddrType_Object=MibTableColumn
ciscoMvpnBgpMdtUpdSrcAddrType=_CiscoMvpnBgpMdtUpdSrcAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,2,1,4),_CiscoMvpnBgpMdtUpdSrcAddrType_Type())
ciscoMvpnBgpMdtUpdSrcAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnBgpMdtUpdSrcAddrType.setStatus(_A)
class _CiscoMvpnBgpMdtUpdateSource_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CiscoMvpnBgpMdtUpdateSource_Type.__name__=_F
_CiscoMvpnBgpMdtUpdateSource_Object=MibTableColumn
ciscoMvpnBgpMdtUpdateSource=_CiscoMvpnBgpMdtUpdateSource_Object((1,3,6,1,4,1,9,10,113,1,4,2,1,5),_CiscoMvpnBgpMdtUpdateSource_Type())
ciscoMvpnBgpMdtUpdateSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnBgpMdtUpdateSource.setStatus(_A)
_CiscoMvpnBgpMdtUpdOrigAddrType_Type=InetAddressType
_CiscoMvpnBgpMdtUpdOrigAddrType_Object=MibTableColumn
ciscoMvpnBgpMdtUpdOrigAddrType=_CiscoMvpnBgpMdtUpdOrigAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,2,1,6),_CiscoMvpnBgpMdtUpdOrigAddrType_Type())
ciscoMvpnBgpMdtUpdOrigAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnBgpMdtUpdOrigAddrType.setStatus(_A)
_CiscoMvpnBgpMdtUpdateOriginator_Type=InetAddress
_CiscoMvpnBgpMdtUpdateOriginator_Object=MibTableColumn
ciscoMvpnBgpMdtUpdateOriginator=_CiscoMvpnBgpMdtUpdateOriginator_Object((1,3,6,1,4,1,9,10,113,1,4,2,1,7),_CiscoMvpnBgpMdtUpdateOriginator_Type())
ciscoMvpnBgpMdtUpdateOriginator.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnBgpMdtUpdateOriginator.setStatus(_A)
_CiscoMvpnBgpMdtUpdNhAddrType_Type=InetAddressType
_CiscoMvpnBgpMdtUpdNhAddrType_Object=MibTableColumn
ciscoMvpnBgpMdtUpdNhAddrType=_CiscoMvpnBgpMdtUpdNhAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,2,1,8),_CiscoMvpnBgpMdtUpdNhAddrType_Type())
ciscoMvpnBgpMdtUpdNhAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnBgpMdtUpdNhAddrType.setStatus(_A)
_CiscoMvpnBgpMdtUpdateNexthop_Type=InetAddress
_CiscoMvpnBgpMdtUpdateNexthop_Object=MibTableColumn
ciscoMvpnBgpMdtUpdateNexthop=_CiscoMvpnBgpMdtUpdateNexthop_Object((1,3,6,1,4,1,9,10,113,1,4,2,1,9),_CiscoMvpnBgpMdtUpdateNexthop_Type())
ciscoMvpnBgpMdtUpdateNexthop.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnBgpMdtUpdateNexthop.setStatus(_A)
_CiscoMvpnMdtJnRcvTable_Object=MibTable
ciscoMvpnMdtJnRcvTable=_CiscoMvpnMdtJnRcvTable_Object((1,3,6,1,4,1,9,10,113,1,4,3))
if mibBuilder.loadTexts:ciscoMvpnMdtJnRcvTable.setStatus(_A)
_CiscoMvpnMdtJnRcvEntry_Object=MibTableRow
ciscoMvpnMdtJnRcvEntry=_CiscoMvpnMdtJnRcvEntry_Object((1,3,6,1,4,1,9,10,113,1,4,3,1))
ciscoMvpnMdtJnRcvEntry.setIndexNames((0,_G,_H),(0,_B,_h),(0,_B,_i),(0,_B,_j),(0,_B,_k))
if mibBuilder.loadTexts:ciscoMvpnMdtJnRcvEntry.setStatus(_A)
_CiscoMvpnMdtJnRcvGrpAddrType_Type=InetAddressType
_CiscoMvpnMdtJnRcvGrpAddrType_Object=MibTableColumn
ciscoMvpnMdtJnRcvGrpAddrType=_CiscoMvpnMdtJnRcvGrpAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,3,1,1),_CiscoMvpnMdtJnRcvGrpAddrType_Type())
ciscoMvpnMdtJnRcvGrpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMdtJnRcvGrpAddrType.setStatus(_A)
class _CiscoMvpnMdtJnRcvGroup_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CiscoMvpnMdtJnRcvGroup_Type.__name__=_F
_CiscoMvpnMdtJnRcvGroup_Object=MibTableColumn
ciscoMvpnMdtJnRcvGroup=_CiscoMvpnMdtJnRcvGroup_Object((1,3,6,1,4,1,9,10,113,1,4,3,1,2),_CiscoMvpnMdtJnRcvGroup_Type())
ciscoMvpnMdtJnRcvGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMdtJnRcvGroup.setStatus(_A)
_CiscoMvpnMdtJnRcvSrcAddrType_Type=InetAddressType
_CiscoMvpnMdtJnRcvSrcAddrType_Object=MibTableColumn
ciscoMvpnMdtJnRcvSrcAddrType=_CiscoMvpnMdtJnRcvSrcAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,3,1,3),_CiscoMvpnMdtJnRcvSrcAddrType_Type())
ciscoMvpnMdtJnRcvSrcAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMdtJnRcvSrcAddrType.setStatus(_A)
class _CiscoMvpnMdtJnRcvSource_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CiscoMvpnMdtJnRcvSource_Type.__name__=_F
_CiscoMvpnMdtJnRcvSource_Object=MibTableColumn
ciscoMvpnMdtJnRcvSource=_CiscoMvpnMdtJnRcvSource_Object((1,3,6,1,4,1,9,10,113,1,4,3,1,4),_CiscoMvpnMdtJnRcvSource_Type())
ciscoMvpnMdtJnRcvSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMdtJnRcvSource.setStatus(_A)
_CiscoMvpnMdtJnRcvUpTime_Type=TimeInterval
_CiscoMvpnMdtJnRcvUpTime_Object=MibTableColumn
ciscoMvpnMdtJnRcvUpTime=_CiscoMvpnMdtJnRcvUpTime_Object((1,3,6,1,4,1,9,10,113,1,4,3,1,5),_CiscoMvpnMdtJnRcvUpTime_Type())
ciscoMvpnMdtJnRcvUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnMdtJnRcvUpTime.setStatus(_A)
_CiscoMvpnMdtJnRcvExpTime_Type=TimeInterval
_CiscoMvpnMdtJnRcvExpTime_Object=MibTableColumn
ciscoMvpnMdtJnRcvExpTime=_CiscoMvpnMdtJnRcvExpTime_Object((1,3,6,1,4,1,9,10,113,1,4,3,1,6),_CiscoMvpnMdtJnRcvExpTime_Type())
ciscoMvpnMdtJnRcvExpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnMdtJnRcvExpTime.setStatus(_A)
_CiscoMvpnMdtJnSendTable_Object=MibTable
ciscoMvpnMdtJnSendTable=_CiscoMvpnMdtJnSendTable_Object((1,3,6,1,4,1,9,10,113,1,4,4))
if mibBuilder.loadTexts:ciscoMvpnMdtJnSendTable.setStatus(_A)
_CiscoMvpnMdtJnSendEntry_Object=MibTableRow
ciscoMvpnMdtJnSendEntry=_CiscoMvpnMdtJnSendEntry_Object((1,3,6,1,4,1,9,10,113,1,4,4,1))
ciscoMvpnMdtJnSendEntry.setIndexNames((0,_G,_H),(0,_B,_l),(0,_B,_m),(0,_B,_n),(0,_B,_o))
if mibBuilder.loadTexts:ciscoMvpnMdtJnSendEntry.setStatus(_A)
_CiscoMvpnMdtJnSendGrpAddrType_Type=InetAddressType
_CiscoMvpnMdtJnSendGrpAddrType_Object=MibTableColumn
ciscoMvpnMdtJnSendGrpAddrType=_CiscoMvpnMdtJnSendGrpAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,4,1,1),_CiscoMvpnMdtJnSendGrpAddrType_Type())
ciscoMvpnMdtJnSendGrpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMdtJnSendGrpAddrType.setStatus(_A)
class _CiscoMvpnMdtJnSendGroup_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CiscoMvpnMdtJnSendGroup_Type.__name__=_F
_CiscoMvpnMdtJnSendGroup_Object=MibTableColumn
ciscoMvpnMdtJnSendGroup=_CiscoMvpnMdtJnSendGroup_Object((1,3,6,1,4,1,9,10,113,1,4,4,1,2),_CiscoMvpnMdtJnSendGroup_Type())
ciscoMvpnMdtJnSendGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMdtJnSendGroup.setStatus(_A)
_CiscoMvpnMdtJnSendSrcAddrType_Type=InetAddressType
_CiscoMvpnMdtJnSendSrcAddrType_Object=MibTableColumn
ciscoMvpnMdtJnSendSrcAddrType=_CiscoMvpnMdtJnSendSrcAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,4,1,3),_CiscoMvpnMdtJnSendSrcAddrType_Type())
ciscoMvpnMdtJnSendSrcAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMdtJnSendSrcAddrType.setStatus(_A)
class _CiscoMvpnMdtJnSendSource_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CiscoMvpnMdtJnSendSource_Type.__name__=_F
_CiscoMvpnMdtJnSendSource_Object=MibTableColumn
ciscoMvpnMdtJnSendSource=_CiscoMvpnMdtJnSendSource_Object((1,3,6,1,4,1,9,10,113,1,4,4,1,4),_CiscoMvpnMdtJnSendSource_Type())
ciscoMvpnMdtJnSendSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ciscoMvpnMdtJnSendSource.setStatus(_A)
_CiscoMvpnMdtJnSendMdtGrpAddrType_Type=InetAddressType
_CiscoMvpnMdtJnSendMdtGrpAddrType_Object=MibTableColumn
ciscoMvpnMdtJnSendMdtGrpAddrType=_CiscoMvpnMdtJnSendMdtGrpAddrType_Object((1,3,6,1,4,1,9,10,113,1,4,4,1,5),_CiscoMvpnMdtJnSendMdtGrpAddrType_Type())
ciscoMvpnMdtJnSendMdtGrpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnMdtJnSendMdtGrpAddrType.setStatus(_A)
_CiscoMvpnMdtJnSendMdtGroup_Type=InetAddress
_CiscoMvpnMdtJnSendMdtGroup_Object=MibTableColumn
ciscoMvpnMdtJnSendMdtGroup=_CiscoMvpnMdtJnSendMdtGroup_Object((1,3,6,1,4,1,9,10,113,1,4,4,1,6),_CiscoMvpnMdtJnSendMdtGroup_Type())
ciscoMvpnMdtJnSendMdtGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnMdtJnSendMdtGroup.setStatus(_A)
class _CiscoMvpnMdtJnSendMdtRefCt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiscoMvpnMdtJnSendMdtRefCt_Type.__name__=_J
_CiscoMvpnMdtJnSendMdtRefCt_Object=MibTableColumn
ciscoMvpnMdtJnSendMdtRefCt=_CiscoMvpnMdtJnSendMdtRefCt_Object((1,3,6,1,4,1,9,10,113,1,4,4,1,7),_CiscoMvpnMdtJnSendMdtRefCt_Type())
ciscoMvpnMdtJnSendMdtRefCt.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnMdtJnSendMdtRefCt.setStatus(_A)
_CiscoMvpnTunnelTable_Object=MibTable
ciscoMvpnTunnelTable=_CiscoMvpnTunnelTable_Object((1,3,6,1,4,1,9,10,113,1,4,5))
if mibBuilder.loadTexts:ciscoMvpnTunnelTable.setStatus(_A)
_CiscoMvpnTunnelEntry_Object=MibTableRow
ciscoMvpnTunnelEntry=_CiscoMvpnTunnelEntry_Object((1,3,6,1,4,1,9,10,113,1,4,5,1))
ciscoMvpnTunnelEntry.setIndexNames((0,_V,_W))
if mibBuilder.loadTexts:ciscoMvpnTunnelEntry.setStatus(_A)
_CiscoMvpnTunnelName_Type=DisplayString
_CiscoMvpnTunnelName_Object=MibTableColumn
ciscoMvpnTunnelName=_CiscoMvpnTunnelName_Object((1,3,6,1,4,1,9,10,113,1,4,5,1,1),_CiscoMvpnTunnelName_Type())
ciscoMvpnTunnelName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnTunnelName.setStatus(_A)
_CiscoMvpnTunnelMvrf_Type=SnmpAdminString
_CiscoMvpnTunnelMvrf_Object=MibTableColumn
ciscoMvpnTunnelMvrf=_CiscoMvpnTunnelMvrf_Object((1,3,6,1,4,1,9,10,113,1,4,5,1,2),_CiscoMvpnTunnelMvrf_Type())
ciscoMvpnTunnelMvrf.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoMvpnTunnelMvrf.setStatus(_A)
_CiscoMvpnConformance_ObjectIdentity=ObjectIdentity
ciscoMvpnConformance=_CiscoMvpnConformance_ObjectIdentity((1,3,6,1,4,1,9,10,113,2))
_CiscoMvpnGroups_ObjectIdentity=ObjectIdentity
ciscoMvpnGroups=_CiscoMvpnGroups_ObjectIdentity((1,3,6,1,4,1,9,10,113,2,1))
_CiscoMvpnCompliances_ObjectIdentity=ObjectIdentity
ciscoMvpnCompliances=_CiscoMvpnCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,113,2,2))
ciscoMvpnScalarGroup=ObjectGroup((1,3,6,1,4,1,9,10,113,2,1,1))
ciscoMvpnScalarGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ciscoMvpnScalarGroup.setStatus(_A)
ciscoMvpnMIBGenericGroup=ObjectGroup((1,3,6,1,4,1,9,10,113,2,1,2))
ciscoMvpnMIBGenericGroup.setObjects(*((_B,_K),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:ciscoMvpnMIBGenericGroup.setStatus(_A)
ciscoMvpnMIBMdtDefaultGroup=ObjectGroup((1,3,6,1,4,1,9,10,113,2,1,3))
ciscoMvpnMIBMdtDefaultGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:ciscoMvpnMIBMdtDefaultGroup.setStatus(_A)
ciscoMvpnMIBMdtDataGroup=ObjectGroup((1,3,6,1,4,1,9,10,113,2,1,4))
ciscoMvpnMIBMdtDataGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:ciscoMvpnMIBMdtDataGroup.setStatus(_A)
ciscoMvpnMIBMrouteMdtGroup=ObjectGroup((1,3,6,1,4,1,9,10,113,2,1,5))
ciscoMvpnMIBMrouteMdtGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ciscoMvpnMIBMrouteMdtGroup.setStatus(_A)
ciscoMvpnMIBBgpMdtUpdateGroup=ObjectGroup((1,3,6,1,4,1,9,10,113,2,1,6))
ciscoMvpnMIBBgpMdtUpdateGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:ciscoMvpnMIBBgpMdtUpdateGroup.setStatus(_A)
ciscoMvpnMIBMdtJnRcvGroup=ObjectGroup((1,3,6,1,4,1,9,10,113,2,1,7))
ciscoMvpnMIBMdtJnRcvGroup.setObjects(*((_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:ciscoMvpnMIBMdtJnRcvGroup.setStatus(_A)
ciscoMvpnMIBMdtJnSendGroup=ObjectGroup((1,3,6,1,4,1,9,10,113,2,1,8))
ciscoMvpnMIBMdtJnSendGroup.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:ciscoMvpnMIBMdtJnSendGroup.setStatus(_A)
ciscoMvpnTunnelGroup=ObjectGroup((1,3,6,1,4,1,9,10,113,2,1,9))
ciscoMvpnTunnelGroup.setObjects(*((_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:ciscoMvpnTunnelGroup.setStatus(_A)
ciscoMvpnMvrfChange=NotificationType((1,3,6,1,4,1,9,10,113,0,2))
ciscoMvpnMvrfChange.setObjects((_B,_K))
if mibBuilder.loadTexts:ciscoMvpnMvrfChange.setStatus(_A)
ciscoMvpnNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,10,113,2,1,10))
ciscoMvpnNotificationGroup.setObjects((_B,_AJ))
if mibBuilder.loadTexts:ciscoMvpnNotificationGroup.setStatus(_A)
ciscoMvpnModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,113,2,2,1))
ciscoMvpnModuleFullCompliance.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoMvpnModuleFullCompliance.setStatus(_A)
ciscoMvpnModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,113,2,2,2))
ciscoMvpnModuleReadOnlyCompliance.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoMvpnModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoMvpnMIB':ciscoMvpnMIB,'ciscoMvpnNotifications':ciscoMvpnNotifications,_AJ:ciscoMvpnMvrfChange,'ciscoMvpnObjects':ciscoMvpnObjects,'ciscoMvpnScalars':ciscoMvpnScalars,_p:ciscoMvpnMvrfNumber,_q:ciscoMvpnNotificationEnable,'ciscoMvpnGeneric':ciscoMvpnGeneric,'ciscoMvpnGenericTable':ciscoMvpnGenericTable,'ciscoMvpnGenericEntry':ciscoMvpnGenericEntry,_K:ciscoMvpnGenOperStatusChange,_r:ciscoMvpnGenOperChangeTime,_s:ciscoMvpnGenAssociatedInterfaces,_t:ciscoMvpnGenRowStatus,'ciscoMvpnConfig':ciscoMvpnConfig,'ciscoMvpnMdtDefaultTable':ciscoMvpnMdtDefaultTable,'ciscoMvpnMdtDefaultEntry':ciscoMvpnMdtDefaultEntry,_u:ciscoMvpnMdtDefaultAddrType,_v:ciscoMvpnMdtDefaultAddress,_w:ciscoMvpnMdtEncapsType,_x:ciscoMvpnMdtDefaultRowStatus,'ciscoMvpnMdtDataTable':ciscoMvpnMdtDataTable,'ciscoMvpnMdtDataEntry':ciscoMvpnMdtDataEntry,_y:ciscoMvpnMdtDataRangeAddrType,_z:ciscoMvpnMdtDataRangeAddress,_A0:ciscoMvpnMdtDataWildcardType,_A1:ciscoMvpnMdtDataWildcardBits,_A2:ciscoMvpnMdtDataThreshold,_A3:ciscoMvpnMdtDataRowStatus,'ciscoMvpnProtocol':ciscoMvpnProtocol,'ciscoMvpnMrouteMdtTable':ciscoMvpnMrouteMdtTable,'ciscoMvpnMrouteMdtEntry':ciscoMvpnMrouteMdtEntry,_Y:ciscoMvpnMrouteMvrfGrpAddrType,_Z:ciscoMvpnMrouteMvrfGroup,_a:ciscoMvpnMrouteMvrfSrcAddrType,_b:ciscoMvpnMrouteMvrfSource,_c:ciscoMvpnMrouteUpDownStreamInfo,_A4:ciscoMvpnMrouteMdtGrpAddrType,_A5:ciscoMvpnMrouteMdtGroup,_A6:ciscoMvpnMrouteMdtType,'ciscoMvpnBgpMdtUpdateTable':ciscoMvpnBgpMdtUpdateTable,'ciscoMvpnBgpMdtUpdateEntry':ciscoMvpnBgpMdtUpdateEntry,_d:ciscoMvpnBgpMdtUpdGrpAddrType,_e:ciscoMvpnBgpMdtUpdateGroup,_A7:ciscoMvpnBgpMdtUpdateRd,_f:ciscoMvpnBgpMdtUpdSrcAddrType,_g:ciscoMvpnBgpMdtUpdateSource,_A8:ciscoMvpnBgpMdtUpdOrigAddrType,_A9:ciscoMvpnBgpMdtUpdateOriginator,_AA:ciscoMvpnBgpMdtUpdNhAddrType,_AB:ciscoMvpnBgpMdtUpdateNexthop,'ciscoMvpnMdtJnRcvTable':ciscoMvpnMdtJnRcvTable,'ciscoMvpnMdtJnRcvEntry':ciscoMvpnMdtJnRcvEntry,_h:ciscoMvpnMdtJnRcvGrpAddrType,_i:ciscoMvpnMdtJnRcvGroup,_j:ciscoMvpnMdtJnRcvSrcAddrType,_k:ciscoMvpnMdtJnRcvSource,_AC:ciscoMvpnMdtJnRcvUpTime,_AD:ciscoMvpnMdtJnRcvExpTime,'ciscoMvpnMdtJnSendTable':ciscoMvpnMdtJnSendTable,'ciscoMvpnMdtJnSendEntry':ciscoMvpnMdtJnSendEntry,_l:ciscoMvpnMdtJnSendGrpAddrType,_m:ciscoMvpnMdtJnSendGroup,_n:ciscoMvpnMdtJnSendSrcAddrType,_o:ciscoMvpnMdtJnSendSource,_AE:ciscoMvpnMdtJnSendMdtGrpAddrType,_AF:ciscoMvpnMdtJnSendMdtGroup,_AG:ciscoMvpnMdtJnSendMdtRefCt,'ciscoMvpnTunnelTable':ciscoMvpnTunnelTable,'ciscoMvpnTunnelEntry':ciscoMvpnTunnelEntry,_AH:ciscoMvpnTunnelName,_AI:ciscoMvpnTunnelMvrf,'ciscoMvpnConformance':ciscoMvpnConformance,'ciscoMvpnGroups':ciscoMvpnGroups,_L:ciscoMvpnScalarGroup,_M:ciscoMvpnMIBGenericGroup,_N:ciscoMvpnMIBMdtDefaultGroup,_O:ciscoMvpnMIBMdtDataGroup,_P:ciscoMvpnMIBMrouteMdtGroup,_Q:ciscoMvpnMIBBgpMdtUpdateGroup,_R:ciscoMvpnMIBMdtJnRcvGroup,_S:ciscoMvpnMIBMdtJnSendGroup,_T:ciscoMvpnTunnelGroup,_U:ciscoMvpnNotificationGroup,'ciscoMvpnCompliances':ciscoMvpnCompliances,'ciscoMvpnModuleFullCompliance':ciscoMvpnModuleFullCompliance,'ciscoMvpnModuleReadOnlyCompliance':ciscoMvpnModuleReadOnlyCompliance})