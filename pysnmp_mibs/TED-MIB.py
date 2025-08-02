_AI='tedNotificationGroup'
_AH='tedObjectsGroup'
_AG='tedEntryDeleted'
_AF='tedEntryCreated'
_AE='tedStatusChange'
_AD='tedSwCapIndication'
_AC='tedSwCapIfMtu'
_AB='tedSwCapMinLspBandwidth'
_AA='tedSwCapMaxLspBandwidthPri7'
_A9='tedSwCapMaxLspBandwidthPri6'
_A8='tedSwCapMaxLspBandwidthPri5'
_A7='tedSwCapMaxLspBandwidthPri4'
_A6='tedSwCapMaxLspBandwidthPri3'
_A5='tedSwCapMaxLspBandwidthPri2'
_A4='tedSwCapMaxLspBandwidthPri1'
_A3='tedSwCapMaxLspBandwidthPri0'
_A2='tedSwCapEncoding'
_A1='tedSwCapType'
_A0='tedRemoteIfAddrType'
_z='tedLocalIfAddrType'
_y='tedRemoteId'
_x='tedLocalId'
_w='tedCreatedDeletedNotificationMaxRate'
_v='tedStatusChangeNotificationMaxRate'
_u='tedLinkInformationData'
_t='tedLinkProtectionType'
_s='tedAdministrativeGroup'
_r='tedUnreservedBandwidthPri7'
_q='tedUnreservedBandwidthPri6'
_p='tedUnreservedBandwidthPri5'
_o='tedUnreservedBandwidthPri4'
_n='tedUnreservedBandwidthPri3'
_m='tedUnreservedBandwidthPri2'
_l='tedUnreservedBandwidthPri1'
_k='tedUnreservedBandwidthPri0'
_j='tedMaxReservableBandwidth'
_i='tedMaxBandwidth'
_h='tedMetric'
_g='tedLinkIdAddr'
_f='tedLinkIdAddrType'
_e='tedTeRouterIdAddr'
_d='tedTeRouterIdAddrType'
_c='tedLinkType'
_b='tedAreaId'
_a='read-write'
_Z='tedSrlgIndex'
_Y='tedSwCapIndex'
_X='tedRemoteIfAddr'
_W='tedLocalIfAddr'
_V='unknown'
_U='tedLinkInformationSource'
_T='tedRemoteRouterId'
_S='tedLocalRouterId'
_R='tedSrlgGroup'
_Q='tedSwCapIndicationGroup'
_P='tedSwCapIfMtuGroup'
_O='tedSwCapMinLspBandwidthGroup'
_N='tedSwCapGroup'
_M='tedNumberedLinkGroup'
_L='tedUnnumberedLinkGroup'
_K='tedMainGroup'
_J='InetAddress'
_I='tedLinkState'
_H='Unsigned32'
_G='Integer32'
_F='tedLinkIndex'
_E='not-accessible'
_D='Byte per second'
_C='read-only'
_B='current'
_A='TED-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Float32TC,=mibBuilder.importSymbols('FLOAT-TC-MIB','Float32TC')
IANAGmplsLSPEncodingTypeTC,IANAGmplsSwitchingTypeTC=mibBuilder.importSymbols('IANA-GMPLS-TC-MIB','IANAGmplsLSPEncodingTypeTC','IANAGmplsSwitchingTypeTC')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_J,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso','transmission')
DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention')
tedMIB=ModuleIdentity((1,3,6,1,2,1,10,273))
if mibBuilder.loadTexts:tedMIB.setRevisions(('2012-12-21 00:00',))
class TedAreaIdTC(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
class TedRouterIdTC(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
class TedLinkIndexTC(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_TedNotifications_ObjectIdentity=ObjectIdentity
tedNotifications=_TedNotifications_ObjectIdentity((1,3,6,1,2,1,10,273,0))
_TedObjects_ObjectIdentity=ObjectIdentity
tedObjects=_TedObjects_ObjectIdentity((1,3,6,1,2,1,10,273,1))
_TedTable_Object=MibTable
tedTable=_TedTable_Object((1,3,6,1,2,1,10,273,1,1))
if mibBuilder.loadTexts:tedTable.setStatus(_B)
_TedEntry_Object=MibTableRow
tedEntry=_TedEntry_Object((1,3,6,1,2,1,10,273,1,1,1))
tedEntry.setIndexNames((0,_A,_S),(0,_A,_T),(0,_A,_U),(0,_A,_F))
if mibBuilder.loadTexts:tedEntry.setStatus(_B)
class _TedLinkInformationSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_V,0),('locallyConfigured',1),('ospfv2',2),('ospfv3',3),('isis',4),('other',5)))
_TedLinkInformationSource_Type.__name__=_G
_TedLinkInformationSource_Object=MibTableColumn
tedLinkInformationSource=_TedLinkInformationSource_Object((1,3,6,1,2,1,10,273,1,1,1,1),_TedLinkInformationSource_Type())
tedLinkInformationSource.setMaxAccess(_E)
if mibBuilder.loadTexts:tedLinkInformationSource.setStatus(_B)
_TedLocalRouterId_Type=TedRouterIdTC
_TedLocalRouterId_Object=MibTableColumn
tedLocalRouterId=_TedLocalRouterId_Object((1,3,6,1,2,1,10,273,1,1,1,2),_TedLocalRouterId_Type())
tedLocalRouterId.setMaxAccess(_E)
if mibBuilder.loadTexts:tedLocalRouterId.setStatus(_B)
_TedRemoteRouterId_Type=TedRouterIdTC
_TedRemoteRouterId_Object=MibTableColumn
tedRemoteRouterId=_TedRemoteRouterId_Object((1,3,6,1,2,1,10,273,1,1,1,3),_TedRemoteRouterId_Type())
tedRemoteRouterId.setMaxAccess(_E)
if mibBuilder.loadTexts:tedRemoteRouterId.setStatus(_B)
_TedLinkIndex_Type=TedLinkIndexTC
_TedLinkIndex_Object=MibTableColumn
tedLinkIndex=_TedLinkIndex_Object((1,3,6,1,2,1,10,273,1,1,1,4),_TedLinkIndex_Type())
tedLinkIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tedLinkIndex.setStatus(_B)
_TedLinkInformationData_Type=RowPointer
_TedLinkInformationData_Object=MibTableColumn
tedLinkInformationData=_TedLinkInformationData_Object((1,3,6,1,2,1,10,273,1,1,1,5),_TedLinkInformationData_Type())
tedLinkInformationData.setMaxAccess(_C)
if mibBuilder.loadTexts:tedLinkInformationData.setStatus(_B)
class _TedLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_V,0),('up',1),('down',2)))
_TedLinkState_Type.__name__=_G
_TedLinkState_Object=MibTableColumn
tedLinkState=_TedLinkState_Object((1,3,6,1,2,1,10,273,1,1,1,6),_TedLinkState_Type())
tedLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:tedLinkState.setStatus(_B)
_TedAreaId_Type=TedAreaIdTC
_TedAreaId_Object=MibTableColumn
tedAreaId=_TedAreaId_Object((1,3,6,1,2,1,10,273,1,1,1,7),_TedAreaId_Type())
tedAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:tedAreaId.setStatus(_B)
class _TedLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pointToPoint',1),('multiAccess',2)))
_TedLinkType_Type.__name__=_G
_TedLinkType_Object=MibTableColumn
tedLinkType=_TedLinkType_Object((1,3,6,1,2,1,10,273,1,1,1,8),_TedLinkType_Type())
tedLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:tedLinkType.setStatus(_B)
_TedTeRouterIdAddrType_Type=InetAddressType
_TedTeRouterIdAddrType_Object=MibTableColumn
tedTeRouterIdAddrType=_TedTeRouterIdAddrType_Object((1,3,6,1,2,1,10,273,1,1,1,9),_TedTeRouterIdAddrType_Type())
tedTeRouterIdAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tedTeRouterIdAddrType.setStatus(_B)
_TedTeRouterIdAddr_Type=InetAddress
_TedTeRouterIdAddr_Object=MibTableColumn
tedTeRouterIdAddr=_TedTeRouterIdAddr_Object((1,3,6,1,2,1,10,273,1,1,1,10),_TedTeRouterIdAddr_Type())
tedTeRouterIdAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tedTeRouterIdAddr.setStatus(_B)
_TedLinkIdAddrType_Type=InetAddressType
_TedLinkIdAddrType_Object=MibTableColumn
tedLinkIdAddrType=_TedLinkIdAddrType_Object((1,3,6,1,2,1,10,273,1,1,1,11),_TedLinkIdAddrType_Type())
tedLinkIdAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tedLinkIdAddrType.setStatus(_B)
_TedLinkIdAddr_Type=InetAddress
_TedLinkIdAddr_Object=MibTableColumn
tedLinkIdAddr=_TedLinkIdAddr_Object((1,3,6,1,2,1,10,273,1,1,1,12),_TedLinkIdAddr_Type())
tedLinkIdAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tedLinkIdAddr.setStatus(_B)
_TedMetric_Type=Integer32
_TedMetric_Object=MibTableColumn
tedMetric=_TedMetric_Object((1,3,6,1,2,1,10,273,1,1,1,13),_TedMetric_Type())
tedMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:tedMetric.setStatus(_B)
_TedMaxBandwidth_Type=Float32TC
_TedMaxBandwidth_Object=MibTableColumn
tedMaxBandwidth=_TedMaxBandwidth_Object((1,3,6,1,2,1,10,273,1,1,1,14),_TedMaxBandwidth_Type())
tedMaxBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:tedMaxBandwidth.setStatus(_B)
if mibBuilder.loadTexts:tedMaxBandwidth.setUnits(_D)
_TedMaxReservableBandwidth_Type=Float32TC
_TedMaxReservableBandwidth_Object=MibTableColumn
tedMaxReservableBandwidth=_TedMaxReservableBandwidth_Object((1,3,6,1,2,1,10,273,1,1,1,15),_TedMaxReservableBandwidth_Type())
tedMaxReservableBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:tedMaxReservableBandwidth.setStatus(_B)
if mibBuilder.loadTexts:tedMaxReservableBandwidth.setUnits(_D)
_TedUnreservedBandwidthPri0_Type=Float32TC
_TedUnreservedBandwidthPri0_Object=MibTableColumn
tedUnreservedBandwidthPri0=_TedUnreservedBandwidthPri0_Object((1,3,6,1,2,1,10,273,1,1,1,16),_TedUnreservedBandwidthPri0_Type())
tedUnreservedBandwidthPri0.setMaxAccess(_C)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri0.setStatus(_B)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri0.setUnits(_D)
_TedUnreservedBandwidthPri1_Type=Float32TC
_TedUnreservedBandwidthPri1_Object=MibTableColumn
tedUnreservedBandwidthPri1=_TedUnreservedBandwidthPri1_Object((1,3,6,1,2,1,10,273,1,1,1,17),_TedUnreservedBandwidthPri1_Type())
tedUnreservedBandwidthPri1.setMaxAccess(_C)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri1.setStatus(_B)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri1.setUnits(_D)
_TedUnreservedBandwidthPri2_Type=Float32TC
_TedUnreservedBandwidthPri2_Object=MibTableColumn
tedUnreservedBandwidthPri2=_TedUnreservedBandwidthPri2_Object((1,3,6,1,2,1,10,273,1,1,1,18),_TedUnreservedBandwidthPri2_Type())
tedUnreservedBandwidthPri2.setMaxAccess(_C)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri2.setStatus(_B)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri2.setUnits(_D)
_TedUnreservedBandwidthPri3_Type=Float32TC
_TedUnreservedBandwidthPri3_Object=MibTableColumn
tedUnreservedBandwidthPri3=_TedUnreservedBandwidthPri3_Object((1,3,6,1,2,1,10,273,1,1,1,19),_TedUnreservedBandwidthPri3_Type())
tedUnreservedBandwidthPri3.setMaxAccess(_C)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri3.setStatus(_B)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri3.setUnits(_D)
_TedUnreservedBandwidthPri4_Type=Float32TC
_TedUnreservedBandwidthPri4_Object=MibTableColumn
tedUnreservedBandwidthPri4=_TedUnreservedBandwidthPri4_Object((1,3,6,1,2,1,10,273,1,1,1,20),_TedUnreservedBandwidthPri4_Type())
tedUnreservedBandwidthPri4.setMaxAccess(_C)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri4.setStatus(_B)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri4.setUnits(_D)
_TedUnreservedBandwidthPri5_Type=Float32TC
_TedUnreservedBandwidthPri5_Object=MibTableColumn
tedUnreservedBandwidthPri5=_TedUnreservedBandwidthPri5_Object((1,3,6,1,2,1,10,273,1,1,1,21),_TedUnreservedBandwidthPri5_Type())
tedUnreservedBandwidthPri5.setMaxAccess(_C)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri5.setStatus(_B)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri5.setUnits(_D)
_TedUnreservedBandwidthPri6_Type=Float32TC
_TedUnreservedBandwidthPri6_Object=MibTableColumn
tedUnreservedBandwidthPri6=_TedUnreservedBandwidthPri6_Object((1,3,6,1,2,1,10,273,1,1,1,22),_TedUnreservedBandwidthPri6_Type())
tedUnreservedBandwidthPri6.setMaxAccess(_C)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri6.setStatus(_B)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri6.setUnits(_D)
_TedUnreservedBandwidthPri7_Type=Float32TC
_TedUnreservedBandwidthPri7_Object=MibTableColumn
tedUnreservedBandwidthPri7=_TedUnreservedBandwidthPri7_Object((1,3,6,1,2,1,10,273,1,1,1,23),_TedUnreservedBandwidthPri7_Type())
tedUnreservedBandwidthPri7.setMaxAccess(_C)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri7.setStatus(_B)
if mibBuilder.loadTexts:tedUnreservedBandwidthPri7.setUnits(_D)
_TedAdministrativeGroup_Type=Integer32
_TedAdministrativeGroup_Object=MibTableColumn
tedAdministrativeGroup=_TedAdministrativeGroup_Object((1,3,6,1,2,1,10,273,1,1,1,24),_TedAdministrativeGroup_Type())
tedAdministrativeGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:tedAdministrativeGroup.setStatus(_B)
_TedLocalId_Type=Integer32
_TedLocalId_Object=MibTableColumn
tedLocalId=_TedLocalId_Object((1,3,6,1,2,1,10,273,1,1,1,25),_TedLocalId_Type())
tedLocalId.setMaxAccess(_C)
if mibBuilder.loadTexts:tedLocalId.setStatus(_B)
_TedRemoteId_Type=Integer32
_TedRemoteId_Object=MibTableColumn
tedRemoteId=_TedRemoteId_Object((1,3,6,1,2,1,10,273,1,1,1,26),_TedRemoteId_Type())
tedRemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:tedRemoteId.setStatus(_B)
class _TedLinkProtectionType_Type(Bits):namedValues=NamedValues(*(('extraTraffic',0),('unprotected',1),('shared',2),('dedicatedOneToOne',3),('dedicatedOnePlusOne',4),('enhanced',5)))
_TedLinkProtectionType_Type.__name__='Bits'
_TedLinkProtectionType_Object=MibTableColumn
tedLinkProtectionType=_TedLinkProtectionType_Object((1,3,6,1,2,1,10,273,1,1,1,27),_TedLinkProtectionType_Type())
tedLinkProtectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:tedLinkProtectionType.setStatus(_B)
_TedLocalIfAddrTable_Object=MibTable
tedLocalIfAddrTable=_TedLocalIfAddrTable_Object((1,3,6,1,2,1,10,273,1,2))
if mibBuilder.loadTexts:tedLocalIfAddrTable.setStatus(_B)
_TedLocalIfAddrEntry_Object=MibTableRow
tedLocalIfAddrEntry=_TedLocalIfAddrEntry_Object((1,3,6,1,2,1,10,273,1,2,1))
tedLocalIfAddrEntry.setIndexNames((0,_A,_F),(0,_A,_W))
if mibBuilder.loadTexts:tedLocalIfAddrEntry.setStatus(_B)
_TedLocalIfAddrType_Type=InetAddressType
_TedLocalIfAddrType_Object=MibTableColumn
tedLocalIfAddrType=_TedLocalIfAddrType_Object((1,3,6,1,2,1,10,273,1,2,1,1),_TedLocalIfAddrType_Type())
tedLocalIfAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tedLocalIfAddrType.setStatus(_B)
class _TedLocalIfAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_TedLocalIfAddr_Type.__name__=_J
_TedLocalIfAddr_Object=MibTableColumn
tedLocalIfAddr=_TedLocalIfAddr_Object((1,3,6,1,2,1,10,273,1,2,1,2),_TedLocalIfAddr_Type())
tedLocalIfAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:tedLocalIfAddr.setStatus(_B)
_TedRemoteIfAddrTable_Object=MibTable
tedRemoteIfAddrTable=_TedRemoteIfAddrTable_Object((1,3,6,1,2,1,10,273,1,3))
if mibBuilder.loadTexts:tedRemoteIfAddrTable.setStatus(_B)
_TedRemoteIfAddrEntry_Object=MibTableRow
tedRemoteIfAddrEntry=_TedRemoteIfAddrEntry_Object((1,3,6,1,2,1,10,273,1,3,1))
tedRemoteIfAddrEntry.setIndexNames((0,_A,_F),(0,_A,_X))
if mibBuilder.loadTexts:tedRemoteIfAddrEntry.setStatus(_B)
_TedRemoteIfAddrType_Type=InetAddressType
_TedRemoteIfAddrType_Object=MibTableColumn
tedRemoteIfAddrType=_TedRemoteIfAddrType_Object((1,3,6,1,2,1,10,273,1,3,1,1),_TedRemoteIfAddrType_Type())
tedRemoteIfAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tedRemoteIfAddrType.setStatus(_B)
class _TedRemoteIfAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_TedRemoteIfAddr_Type.__name__=_J
_TedRemoteIfAddr_Object=MibTableColumn
tedRemoteIfAddr=_TedRemoteIfAddr_Object((1,3,6,1,2,1,10,273,1,3,1,2),_TedRemoteIfAddr_Type())
tedRemoteIfAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:tedRemoteIfAddr.setStatus(_B)
_TedSwCapTable_Object=MibTable
tedSwCapTable=_TedSwCapTable_Object((1,3,6,1,2,1,10,273,1,4))
if mibBuilder.loadTexts:tedSwCapTable.setStatus(_B)
_TedSwCapEntry_Object=MibTableRow
tedSwCapEntry=_TedSwCapEntry_Object((1,3,6,1,2,1,10,273,1,4,1))
tedSwCapEntry.setIndexNames((0,_A,_F),(0,_A,_Y))
if mibBuilder.loadTexts:tedSwCapEntry.setStatus(_B)
class _TedSwCapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TedSwCapIndex_Type.__name__=_H
_TedSwCapIndex_Object=MibTableColumn
tedSwCapIndex=_TedSwCapIndex_Object((1,3,6,1,2,1,10,273,1,4,1,1),_TedSwCapIndex_Type())
tedSwCapIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tedSwCapIndex.setStatus(_B)
_TedSwCapType_Type=IANAGmplsSwitchingTypeTC
_TedSwCapType_Object=MibTableColumn
tedSwCapType=_TedSwCapType_Object((1,3,6,1,2,1,10,273,1,4,1,2),_TedSwCapType_Type())
tedSwCapType.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapType.setStatus(_B)
_TedSwCapEncoding_Type=IANAGmplsLSPEncodingTypeTC
_TedSwCapEncoding_Object=MibTableColumn
tedSwCapEncoding=_TedSwCapEncoding_Object((1,3,6,1,2,1,10,273,1,4,1,3),_TedSwCapEncoding_Type())
tedSwCapEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapEncoding.setStatus(_B)
_TedSwCapMaxLspBandwidthPri0_Type=Float32TC
_TedSwCapMaxLspBandwidthPri0_Object=MibTableColumn
tedSwCapMaxLspBandwidthPri0=_TedSwCapMaxLspBandwidthPri0_Object((1,3,6,1,2,1,10,273,1,4,1,4),_TedSwCapMaxLspBandwidthPri0_Type())
tedSwCapMaxLspBandwidthPri0.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri0.setStatus(_B)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri0.setUnits(_D)
_TedSwCapMaxLspBandwidthPri1_Type=Float32TC
_TedSwCapMaxLspBandwidthPri1_Object=MibTableColumn
tedSwCapMaxLspBandwidthPri1=_TedSwCapMaxLspBandwidthPri1_Object((1,3,6,1,2,1,10,273,1,4,1,5),_TedSwCapMaxLspBandwidthPri1_Type())
tedSwCapMaxLspBandwidthPri1.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri1.setStatus(_B)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri1.setUnits(_D)
_TedSwCapMaxLspBandwidthPri2_Type=Float32TC
_TedSwCapMaxLspBandwidthPri2_Object=MibTableColumn
tedSwCapMaxLspBandwidthPri2=_TedSwCapMaxLspBandwidthPri2_Object((1,3,6,1,2,1,10,273,1,4,1,6),_TedSwCapMaxLspBandwidthPri2_Type())
tedSwCapMaxLspBandwidthPri2.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri2.setStatus(_B)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri2.setUnits(_D)
_TedSwCapMaxLspBandwidthPri3_Type=Float32TC
_TedSwCapMaxLspBandwidthPri3_Object=MibTableColumn
tedSwCapMaxLspBandwidthPri3=_TedSwCapMaxLspBandwidthPri3_Object((1,3,6,1,2,1,10,273,1,4,1,7),_TedSwCapMaxLspBandwidthPri3_Type())
tedSwCapMaxLspBandwidthPri3.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri3.setStatus(_B)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri3.setUnits(_D)
_TedSwCapMaxLspBandwidthPri4_Type=Float32TC
_TedSwCapMaxLspBandwidthPri4_Object=MibTableColumn
tedSwCapMaxLspBandwidthPri4=_TedSwCapMaxLspBandwidthPri4_Object((1,3,6,1,2,1,10,273,1,4,1,8),_TedSwCapMaxLspBandwidthPri4_Type())
tedSwCapMaxLspBandwidthPri4.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri4.setStatus(_B)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri4.setUnits(_D)
_TedSwCapMaxLspBandwidthPri5_Type=Float32TC
_TedSwCapMaxLspBandwidthPri5_Object=MibTableColumn
tedSwCapMaxLspBandwidthPri5=_TedSwCapMaxLspBandwidthPri5_Object((1,3,6,1,2,1,10,273,1,4,1,9),_TedSwCapMaxLspBandwidthPri5_Type())
tedSwCapMaxLspBandwidthPri5.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri5.setStatus(_B)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri5.setUnits(_D)
_TedSwCapMaxLspBandwidthPri6_Type=Float32TC
_TedSwCapMaxLspBandwidthPri6_Object=MibTableColumn
tedSwCapMaxLspBandwidthPri6=_TedSwCapMaxLspBandwidthPri6_Object((1,3,6,1,2,1,10,273,1,4,1,10),_TedSwCapMaxLspBandwidthPri6_Type())
tedSwCapMaxLspBandwidthPri6.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri6.setStatus(_B)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri6.setUnits(_D)
_TedSwCapMaxLspBandwidthPri7_Type=Float32TC
_TedSwCapMaxLspBandwidthPri7_Object=MibTableColumn
tedSwCapMaxLspBandwidthPri7=_TedSwCapMaxLspBandwidthPri7_Object((1,3,6,1,2,1,10,273,1,4,1,11),_TedSwCapMaxLspBandwidthPri7_Type())
tedSwCapMaxLspBandwidthPri7.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri7.setStatus(_B)
if mibBuilder.loadTexts:tedSwCapMaxLspBandwidthPri7.setUnits(_D)
_TedSwCapMinLspBandwidth_Type=Float32TC
_TedSwCapMinLspBandwidth_Object=MibTableColumn
tedSwCapMinLspBandwidth=_TedSwCapMinLspBandwidth_Object((1,3,6,1,2,1,10,273,1,4,1,12),_TedSwCapMinLspBandwidth_Type())
tedSwCapMinLspBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapMinLspBandwidth.setStatus(_B)
if mibBuilder.loadTexts:tedSwCapMinLspBandwidth.setUnits(_D)
_TedSwCapIfMtu_Type=Integer32
_TedSwCapIfMtu_Object=MibTableColumn
tedSwCapIfMtu=_TedSwCapIfMtu_Object((1,3,6,1,2,1,10,273,1,4,1,13),_TedSwCapIfMtu_Type())
tedSwCapIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapIfMtu.setStatus(_B)
class _TedSwCapIndication_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('standard',0),('arbitrary',1)))
_TedSwCapIndication_Type.__name__=_G
_TedSwCapIndication_Object=MibTableColumn
tedSwCapIndication=_TedSwCapIndication_Object((1,3,6,1,2,1,10,273,1,4,1,14),_TedSwCapIndication_Type())
tedSwCapIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSwCapIndication.setStatus(_B)
_TedSrlgTable_Object=MibTable
tedSrlgTable=_TedSrlgTable_Object((1,3,6,1,2,1,10,273,1,5))
if mibBuilder.loadTexts:tedSrlgTable.setStatus(_B)
_TedSrlgEntry_Object=MibTableRow
tedSrlgEntry=_TedSrlgEntry_Object((1,3,6,1,2,1,10,273,1,5,1))
tedSrlgEntry.setIndexNames((0,_A,_F),(0,_A,_Z))
if mibBuilder.loadTexts:tedSrlgEntry.setStatus(_B)
class _TedSrlgIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TedSrlgIndex_Type.__name__=_H
_TedSrlgIndex_Object=MibTableColumn
tedSrlgIndex=_TedSrlgIndex_Object((1,3,6,1,2,1,10,273,1,5,1,1),_TedSrlgIndex_Type())
tedSrlgIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tedSrlgIndex.setStatus(_B)
_TedSrlg_Type=Integer32
_TedSrlg_Object=MibTableColumn
tedSrlg=_TedSrlg_Object((1,3,6,1,2,1,10,273,1,5,1,2),_TedSrlg_Type())
tedSrlg.setMaxAccess(_C)
if mibBuilder.loadTexts:tedSrlg.setStatus(_B)
class _TedStatusChangeNotificationMaxRate_Type(Unsigned32):defaultValue=1
_TedStatusChangeNotificationMaxRate_Type.__name__=_H
_TedStatusChangeNotificationMaxRate_Object=MibScalar
tedStatusChangeNotificationMaxRate=_TedStatusChangeNotificationMaxRate_Object((1,3,6,1,2,1,10,273,1,6),_TedStatusChangeNotificationMaxRate_Type())
tedStatusChangeNotificationMaxRate.setMaxAccess(_a)
if mibBuilder.loadTexts:tedStatusChangeNotificationMaxRate.setStatus(_B)
class _TedCreatedDeletedNotificationMaxRate_Type(Unsigned32):defaultValue=1
_TedCreatedDeletedNotificationMaxRate_Type.__name__=_H
_TedCreatedDeletedNotificationMaxRate_Object=MibScalar
tedCreatedDeletedNotificationMaxRate=_TedCreatedDeletedNotificationMaxRate_Object((1,3,6,1,2,1,10,273,1,7),_TedCreatedDeletedNotificationMaxRate_Type())
tedCreatedDeletedNotificationMaxRate.setMaxAccess(_a)
if mibBuilder.loadTexts:tedCreatedDeletedNotificationMaxRate.setStatus(_B)
_TedConformance_ObjectIdentity=ObjectIdentity
tedConformance=_TedConformance_ObjectIdentity((1,3,6,1,2,1,10,273,2))
_TedCompliances_ObjectIdentity=ObjectIdentity
tedCompliances=_TedCompliances_ObjectIdentity((1,3,6,1,2,1,10,273,2,1))
_TedGroups_ObjectIdentity=ObjectIdentity
tedGroups=_TedGroups_ObjectIdentity((1,3,6,1,2,1,10,273,2,2))
tedMainGroup=ObjectGroup((1,3,6,1,2,1,10,273,2,2,1))
tedMainGroup.setObjects(*((_A,_I),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:tedMainGroup.setStatus(_B)
tedObjectsGroup=ObjectGroup((1,3,6,1,2,1,10,273,2,2,2))
tedObjectsGroup.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:tedObjectsGroup.setStatus(_B)
tedUnnumberedLinkGroup=ObjectGroup((1,3,6,1,2,1,10,273,2,2,4))
tedUnnumberedLinkGroup.setObjects(*((_A,_x),(_A,_y)))
if mibBuilder.loadTexts:tedUnnumberedLinkGroup.setStatus(_B)
tedNumberedLinkGroup=ObjectGroup((1,3,6,1,2,1,10,273,2,2,5))
tedNumberedLinkGroup.setObjects(*((_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:tedNumberedLinkGroup.setStatus(_B)
tedSwCapGroup=ObjectGroup((1,3,6,1,2,1,10,273,2,2,6))
tedSwCapGroup.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:tedSwCapGroup.setStatus(_B)
tedSwCapMinLspBandwidthGroup=ObjectGroup((1,3,6,1,2,1,10,273,2,2,7))
tedSwCapMinLspBandwidthGroup.setObjects((_A,_AB))
if mibBuilder.loadTexts:tedSwCapMinLspBandwidthGroup.setStatus(_B)
tedSwCapIfMtuGroup=ObjectGroup((1,3,6,1,2,1,10,273,2,2,8))
tedSwCapIfMtuGroup.setObjects((_A,_AC))
if mibBuilder.loadTexts:tedSwCapIfMtuGroup.setStatus(_B)
tedSwCapIndicationGroup=ObjectGroup((1,3,6,1,2,1,10,273,2,2,9))
tedSwCapIndicationGroup.setObjects((_A,_AD))
if mibBuilder.loadTexts:tedSwCapIndicationGroup.setStatus(_B)
tedSrlgGroup=ObjectGroup((1,3,6,1,2,1,10,273,2,2,10))
tedSrlgGroup.setObjects((_A,'tedSrlg'))
if mibBuilder.loadTexts:tedSrlgGroup.setStatus(_B)
tedStatusChange=NotificationType((1,3,6,1,2,1,10,273,0,1))
tedStatusChange.setObjects((_A,_I))
if mibBuilder.loadTexts:tedStatusChange.setStatus(_B)
tedEntryCreated=NotificationType((1,3,6,1,2,1,10,273,0,2))
tedEntryCreated.setObjects((_A,_I))
if mibBuilder.loadTexts:tedEntryCreated.setStatus(_B)
tedEntryDeleted=NotificationType((1,3,6,1,2,1,10,273,0,3))
tedEntryDeleted.setObjects((_A,_I))
if mibBuilder.loadTexts:tedEntryDeleted.setStatus(_B)
tedNotificationGroup=NotificationGroup((1,3,6,1,2,1,10,273,2,2,3))
tedNotificationGroup.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:tedNotificationGroup.setStatus(_B)
tedModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,273,2,1,1))
tedModuleFullCompliance.setObjects(*((_A,_K),(_A,_AH),(_A,_AI),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:tedModuleFullCompliance.setStatus(_B)
tedModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,273,2,1,2))
tedModuleReadOnlyCompliance.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:tedModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'TedAreaIdTC':TedAreaIdTC,'TedRouterIdTC':TedRouterIdTC,'TedLinkIndexTC':TedLinkIndexTC,'tedMIB':tedMIB,'tedNotifications':tedNotifications,_AE:tedStatusChange,_AF:tedEntryCreated,_AG:tedEntryDeleted,'tedObjects':tedObjects,'tedTable':tedTable,'tedEntry':tedEntry,_U:tedLinkInformationSource,_S:tedLocalRouterId,_T:tedRemoteRouterId,_F:tedLinkIndex,_u:tedLinkInformationData,_I:tedLinkState,_b:tedAreaId,_c:tedLinkType,_d:tedTeRouterIdAddrType,_e:tedTeRouterIdAddr,_f:tedLinkIdAddrType,_g:tedLinkIdAddr,_h:tedMetric,_i:tedMaxBandwidth,_j:tedMaxReservableBandwidth,_k:tedUnreservedBandwidthPri0,_l:tedUnreservedBandwidthPri1,_m:tedUnreservedBandwidthPri2,_n:tedUnreservedBandwidthPri3,_o:tedUnreservedBandwidthPri4,_p:tedUnreservedBandwidthPri5,_q:tedUnreservedBandwidthPri6,_r:tedUnreservedBandwidthPri7,_s:tedAdministrativeGroup,_x:tedLocalId,_y:tedRemoteId,_t:tedLinkProtectionType,'tedLocalIfAddrTable':tedLocalIfAddrTable,'tedLocalIfAddrEntry':tedLocalIfAddrEntry,_z:tedLocalIfAddrType,_W:tedLocalIfAddr,'tedRemoteIfAddrTable':tedRemoteIfAddrTable,'tedRemoteIfAddrEntry':tedRemoteIfAddrEntry,_A0:tedRemoteIfAddrType,_X:tedRemoteIfAddr,'tedSwCapTable':tedSwCapTable,'tedSwCapEntry':tedSwCapEntry,_Y:tedSwCapIndex,_A1:tedSwCapType,_A2:tedSwCapEncoding,_A3:tedSwCapMaxLspBandwidthPri0,_A4:tedSwCapMaxLspBandwidthPri1,_A5:tedSwCapMaxLspBandwidthPri2,_A6:tedSwCapMaxLspBandwidthPri3,_A7:tedSwCapMaxLspBandwidthPri4,_A8:tedSwCapMaxLspBandwidthPri5,_A9:tedSwCapMaxLspBandwidthPri6,_AA:tedSwCapMaxLspBandwidthPri7,_AB:tedSwCapMinLspBandwidth,_AC:tedSwCapIfMtu,_AD:tedSwCapIndication,'tedSrlgTable':tedSrlgTable,'tedSrlgEntry':tedSrlgEntry,_Z:tedSrlgIndex,'tedSrlg':tedSrlg,_v:tedStatusChangeNotificationMaxRate,_w:tedCreatedDeletedNotificationMaxRate,'tedConformance':tedConformance,'tedCompliances':tedCompliances,'tedModuleFullCompliance':tedModuleFullCompliance,'tedModuleReadOnlyCompliance':tedModuleReadOnlyCompliance,'tedGroups':tedGroups,_K:tedMainGroup,_AH:tedObjectsGroup,_AI:tedNotificationGroup,_L:tedUnnumberedLinkGroup,_M:tedNumberedLinkGroup,_N:tedSwCapGroup,_O:tedSwCapMinLspBandwidthGroup,_P:tedSwCapIfMtuGroup,_Q:tedSwCapIndicationGroup,_R:tedSrlgGroup})