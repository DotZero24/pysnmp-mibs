_Ad='ciscoGslbSystemResourceRegionGroup'
_Ac='ciscoGslbSystemResourceLocationGroup'
_Ab='ciscoGslbSystemResourceGroup'
_Aa='ciscoGslbSystemPeerEventStatus'
_AZ='cgsRegionIdRowStatus'
_AY='cgsRegionIdStorageType'
_AX='cgsUnAnswerCountRatePerRegionId4Hr'
_AW='cgsUnAnswerCountRatePerRegionId30Min'
_AV='cgsUnAnswerCountRatePerRegionId5Min'
_AU='cgsUnAnswerCountRatePerRegionId1Min'
_AT='cgsUnAnswerCountPerRegionId'
_AS='cgsAnswerCountRatePerRegionId4Hr'
_AR='cgsAnswerCountRatePerRegionId30Min'
_AQ='cgsAnswerCountRatePerRegionId5Min'
_AP='cgsAnswerCountRatePerRegionId1Min'
_AO='cgsAnswerCountPerRegionId'
_AN='cgsReqCountRatePerRegionId4Hr'
_AM='cgsReqCountRatePerRegionId30Min'
_AL='cgsReqCountRatePerRegionId5Min'
_AK='cgsReqCountRatePerRegionId1Min'
_AJ='cgsReqCountPerRegionId'
_AI='cgsRegionIdComments'
_AH='cgsRegionIdName'
_AG='cgsPeerEventNotifEnable'
_AF='cgsRegionRowStatus'
_AE='cgsRegionStorageType'
_AD='cgsRegionComments'
_AC='cgsProxRowStatus'
_AB='cgsProxStorageType'
_AA='cgsProxPeakRcvdRate'
_A9='cgsProxPeakSendRate'
_A8='cgsProxRcvdRate'
_A7='cgsProxSendRate'
_A6='cgsProxTotalRcvdResps'
_A5='cgsProxTotalSentReqs'
_A4='cgsProxRcvdMeasureResps'
_A3='cgsProxSentMeasureReqs'
_A2='cgsProxEchoRcvdResps'
_A1='cgsProxEchoSentReqs'
_A0='cgsProxSecondaryAddress'
_z='cgsProxSecondaryAddressType'
_y='cgsProxPrimaryAddress'
_x='cgsProxPrimaryAddressType'
_w='cgsPeerVersion'
_v='cgsPeerLocation'
_u='cgsNodeRegion'
_t='cgsNodeLocation'
_s='cgsNodeStatus'
_r='cgsNodeCommIfIndex'
_q='cgsNodeCommIfName'
_p='cgsNodeService'
_o='cgsRegionId'
_n='cgsLocationName'
_m='cgsRegionName'
_l='cgsProxZoneName'
_k='cgsPeerAddress'
_j='cgsPeerAddressType'
_i='TruthValue'
_h='Unsigned32'
_g='sysName'
_f='SNMPv2-MIB'
_e='ciscoGslbSystemNotifGroup'
_d='ciscoGslbSystemNotifObjectsGroup'
_c='ciscoGslbSystemNotifControlGroup'
_b='ciscoGslbSystemProxZoneGroup'
_a='ciscoGslbSystemPeerGroup'
_Z='ciscoGslbSystemGeneralGroup'
_Y='cgsPeerPrevStatus'
_X='cgsLocationRowStatus'
_W='cgsLocationStorageType'
_V='cgsLocationComments'
_U='cgsLocationZone'
_T='cgsLocationRegion'
_S='cgsPeerStatus'
_R='cgsPeerService'
_Q='cgsPeerDnsName'
_P='number of hits'
_O='responses'
_N='requests'
_M='InetAddressType'
_L='InetAddress'
_K='rate per second'
_J='read-write'
_I='StorageType'
_H='not-accessible'
_G='deprecated'
_F='hits per second'
_E='SnmpAdminString'
_D='read-create'
_C='read-only'
_B='current'
_A='CISCO-GSLB-SYSTEM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CiscoGslbNodeServices,CiscoGslbPeerStatus=mibBuilder.importSymbols('CISCO-GSLB-TC-MIB','CiscoGslbNodeServices','CiscoGslbPeerStatus')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressDNS,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_L,'InetAddressDNS',_M)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_f,_g)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_h,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_I,'TextualConvention',_i)
ciscoGslbSystemMIB=ModuleIdentity((1,3,6,1,4,1,9,9,589))
if mibBuilder.loadTexts:ciscoGslbSystemMIB.setRevisions(('2011-06-06 00:00','2006-12-04 00:00'))
_CiscoGslbSystemMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoGslbSystemMIBNotifs=_CiscoGslbSystemMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,589,0))
_CiscoGslbSystemMIBObjects_ObjectIdentity=ObjectIdentity
ciscoGslbSystemMIBObjects=_CiscoGslbSystemMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,589,1))
_CgsNotifControl_ObjectIdentity=ObjectIdentity
cgsNotifControl=_CgsNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,589,1,1))
class _CgsPeerEventNotifEnable_Type(TruthValue):defaultValue=2
_CgsPeerEventNotifEnable_Type.__name__=_i
_CgsPeerEventNotifEnable_Object=MibScalar
cgsPeerEventNotifEnable=_CgsPeerEventNotifEnable_Object((1,3,6,1,4,1,9,9,589,1,1,1),_CgsPeerEventNotifEnable_Type())
cgsPeerEventNotifEnable.setMaxAccess(_J)
if mibBuilder.loadTexts:cgsPeerEventNotifEnable.setStatus(_B)
_CgsNotifObjects_ObjectIdentity=ObjectIdentity
cgsNotifObjects=_CgsNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,589,1,2))
_CgsPeerPrevStatus_Type=CiscoGslbPeerStatus
_CgsPeerPrevStatus_Object=MibScalar
cgsPeerPrevStatus=_CgsPeerPrevStatus_Object((1,3,6,1,4,1,9,9,589,1,2,1),_CgsPeerPrevStatus_Type())
cgsPeerPrevStatus.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:cgsPeerPrevStatus.setStatus(_B)
_CgsGeneral_ObjectIdentity=ObjectIdentity
cgsGeneral=_CgsGeneral_ObjectIdentity((1,3,6,1,4,1,9,9,589,1,3))
_CgsNodeService_Type=CiscoGslbNodeServices
_CgsNodeService_Object=MibScalar
cgsNodeService=_CgsNodeService_Object((1,3,6,1,4,1,9,9,589,1,3,1),_CgsNodeService_Type())
cgsNodeService.setMaxAccess(_J)
if mibBuilder.loadTexts:cgsNodeService.setStatus(_B)
_CgsNodeCommIfName_Type=SnmpAdminString
_CgsNodeCommIfName_Object=MibScalar
cgsNodeCommIfName=_CgsNodeCommIfName_Object((1,3,6,1,4,1,9,9,589,1,3,2),_CgsNodeCommIfName_Type())
cgsNodeCommIfName.setMaxAccess(_J)
if mibBuilder.loadTexts:cgsNodeCommIfName.setStatus(_B)
_CgsNodeCommIfIndex_Type=InterfaceIndexOrZero
_CgsNodeCommIfIndex_Object=MibScalar
cgsNodeCommIfIndex=_CgsNodeCommIfIndex_Object((1,3,6,1,4,1,9,9,589,1,3,3),_CgsNodeCommIfIndex_Type())
cgsNodeCommIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsNodeCommIfIndex.setStatus(_B)
_CgsNodeStatus_Type=CiscoGslbPeerStatus
_CgsNodeStatus_Object=MibScalar
cgsNodeStatus=_CgsNodeStatus_Object((1,3,6,1,4,1,9,9,589,1,3,4),_CgsNodeStatus_Type())
cgsNodeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsNodeStatus.setStatus(_B)
class _CgsNodeLocation_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgsNodeLocation_Type.__name__=_E
_CgsNodeLocation_Object=MibScalar
cgsNodeLocation=_CgsNodeLocation_Object((1,3,6,1,4,1,9,9,589,1,3,5),_CgsNodeLocation_Type())
cgsNodeLocation.setMaxAccess(_J)
if mibBuilder.loadTexts:cgsNodeLocation.setStatus(_B)
class _CgsNodeRegion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgsNodeRegion_Type.__name__=_E
_CgsNodeRegion_Object=MibScalar
cgsNodeRegion=_CgsNodeRegion_Object((1,3,6,1,4,1,9,9,589,1,3,6),_CgsNodeRegion_Type())
cgsNodeRegion.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsNodeRegion.setStatus(_B)
_CgsPeer_ObjectIdentity=ObjectIdentity
cgsPeer=_CgsPeer_ObjectIdentity((1,3,6,1,4,1,9,9,589,1,4))
_CgsPeerTable_Object=MibTable
cgsPeerTable=_CgsPeerTable_Object((1,3,6,1,4,1,9,9,589,1,4,1))
if mibBuilder.loadTexts:cgsPeerTable.setStatus(_B)
_CgsPeerEntry_Object=MibTableRow
cgsPeerEntry=_CgsPeerEntry_Object((1,3,6,1,4,1,9,9,589,1,4,1,1))
cgsPeerEntry.setIndexNames((0,_A,_j),(0,_A,_k))
if mibBuilder.loadTexts:cgsPeerEntry.setStatus(_B)
_CgsPeerAddressType_Type=InetAddressType
_CgsPeerAddressType_Object=MibTableColumn
cgsPeerAddressType=_CgsPeerAddressType_Object((1,3,6,1,4,1,9,9,589,1,4,1,1,1),_CgsPeerAddressType_Type())
cgsPeerAddressType.setMaxAccess(_H)
if mibBuilder.loadTexts:cgsPeerAddressType.setStatus(_B)
class _CgsPeerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_CgsPeerAddress_Type.__name__=_L
_CgsPeerAddress_Object=MibTableColumn
cgsPeerAddress=_CgsPeerAddress_Object((1,3,6,1,4,1,9,9,589,1,4,1,1,2),_CgsPeerAddress_Type())
cgsPeerAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:cgsPeerAddress.setStatus(_B)
class _CgsPeerLocation_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgsPeerLocation_Type.__name__=_E
_CgsPeerLocation_Object=MibTableColumn
cgsPeerLocation=_CgsPeerLocation_Object((1,3,6,1,4,1,9,9,589,1,4,1,1,3),_CgsPeerLocation_Type())
cgsPeerLocation.setMaxAccess(_J)
if mibBuilder.loadTexts:cgsPeerLocation.setStatus(_B)
_CgsPeerDnsName_Type=InetAddressDNS
_CgsPeerDnsName_Object=MibTableColumn
cgsPeerDnsName=_CgsPeerDnsName_Object((1,3,6,1,4,1,9,9,589,1,4,1,1,4),_CgsPeerDnsName_Type())
cgsPeerDnsName.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsPeerDnsName.setStatus(_B)
_CgsPeerService_Type=CiscoGslbNodeServices
_CgsPeerService_Object=MibTableColumn
cgsPeerService=_CgsPeerService_Object((1,3,6,1,4,1,9,9,589,1,4,1,1,5),_CgsPeerService_Type())
cgsPeerService.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsPeerService.setStatus(_B)
_CgsPeerStatus_Type=CiscoGslbPeerStatus
_CgsPeerStatus_Object=MibTableColumn
cgsPeerStatus=_CgsPeerStatus_Object((1,3,6,1,4,1,9,9,589,1,4,1,1,6),_CgsPeerStatus_Type())
cgsPeerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsPeerStatus.setStatus(_B)
_CgsPeerVersion_Type=SnmpAdminString
_CgsPeerVersion_Object=MibTableColumn
cgsPeerVersion=_CgsPeerVersion_Object((1,3,6,1,4,1,9,9,589,1,4,1,1,7),_CgsPeerVersion_Type())
cgsPeerVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsPeerVersion.setStatus(_B)
_CgsProxZoneStats_ObjectIdentity=ObjectIdentity
cgsProxZoneStats=_CgsProxZoneStats_ObjectIdentity((1,3,6,1,4,1,9,9,589,1,5))
_CgsProxZoneTable_Object=MibTable
cgsProxZoneTable=_CgsProxZoneTable_Object((1,3,6,1,4,1,9,9,589,1,5,1))
if mibBuilder.loadTexts:cgsProxZoneTable.setStatus(_B)
_CgsProxZoneEntry_Object=MibTableRow
cgsProxZoneEntry=_CgsProxZoneEntry_Object((1,3,6,1,4,1,9,9,589,1,5,1,1))
cgsProxZoneEntry.setIndexNames((0,_A,_l))
if mibBuilder.loadTexts:cgsProxZoneEntry.setStatus(_B)
class _CgsProxZoneName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgsProxZoneName_Type.__name__=_E
_CgsProxZoneName_Object=MibTableColumn
cgsProxZoneName=_CgsProxZoneName_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,1),_CgsProxZoneName_Type())
cgsProxZoneName.setMaxAccess(_H)
if mibBuilder.loadTexts:cgsProxZoneName.setStatus(_B)
class _CgsProxPrimaryAddressType_Type(InetAddressType):defaultValue=1
_CgsProxPrimaryAddressType_Type.__name__=_M
_CgsProxPrimaryAddressType_Object=MibTableColumn
cgsProxPrimaryAddressType=_CgsProxPrimaryAddressType_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,2),_CgsProxPrimaryAddressType_Type())
cgsProxPrimaryAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsProxPrimaryAddressType.setStatus(_B)
_CgsProxPrimaryAddress_Type=InetAddress
_CgsProxPrimaryAddress_Object=MibTableColumn
cgsProxPrimaryAddress=_CgsProxPrimaryAddress_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,3),_CgsProxPrimaryAddress_Type())
cgsProxPrimaryAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsProxPrimaryAddress.setStatus(_B)
class _CgsProxSecondaryAddressType_Type(InetAddressType):defaultValue=1
_CgsProxSecondaryAddressType_Type.__name__=_M
_CgsProxSecondaryAddressType_Object=MibTableColumn
cgsProxSecondaryAddressType=_CgsProxSecondaryAddressType_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,4),_CgsProxSecondaryAddressType_Type())
cgsProxSecondaryAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsProxSecondaryAddressType.setStatus(_B)
class _CgsProxSecondaryAddress_Type(InetAddress):defaultValue=OctetString('')
_CgsProxSecondaryAddress_Type.__name__=_L
_CgsProxSecondaryAddress_Object=MibTableColumn
cgsProxSecondaryAddress=_CgsProxSecondaryAddress_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,5),_CgsProxSecondaryAddress_Type())
cgsProxSecondaryAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsProxSecondaryAddress.setStatus(_B)
_CgsProxEchoSentReqs_Type=Counter32
_CgsProxEchoSentReqs_Object=MibTableColumn
cgsProxEchoSentReqs=_CgsProxEchoSentReqs_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,6),_CgsProxEchoSentReqs_Type())
cgsProxEchoSentReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsProxEchoSentReqs.setStatus(_B)
if mibBuilder.loadTexts:cgsProxEchoSentReqs.setUnits(_N)
_CgsProxEchoRcvdResps_Type=Counter32
_CgsProxEchoRcvdResps_Object=MibTableColumn
cgsProxEchoRcvdResps=_CgsProxEchoRcvdResps_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,7),_CgsProxEchoRcvdResps_Type())
cgsProxEchoRcvdResps.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsProxEchoRcvdResps.setStatus(_B)
if mibBuilder.loadTexts:cgsProxEchoRcvdResps.setUnits(_O)
_CgsProxSentMeasureReqs_Type=Counter32
_CgsProxSentMeasureReqs_Object=MibTableColumn
cgsProxSentMeasureReqs=_CgsProxSentMeasureReqs_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,8),_CgsProxSentMeasureReqs_Type())
cgsProxSentMeasureReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsProxSentMeasureReqs.setStatus(_B)
if mibBuilder.loadTexts:cgsProxSentMeasureReqs.setUnits(_N)
_CgsProxRcvdMeasureResps_Type=Counter32
_CgsProxRcvdMeasureResps_Object=MibTableColumn
cgsProxRcvdMeasureResps=_CgsProxRcvdMeasureResps_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,9),_CgsProxRcvdMeasureResps_Type())
cgsProxRcvdMeasureResps.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsProxRcvdMeasureResps.setStatus(_B)
if mibBuilder.loadTexts:cgsProxRcvdMeasureResps.setUnits(_O)
_CgsProxTotalSentReqs_Type=Counter32
_CgsProxTotalSentReqs_Object=MibTableColumn
cgsProxTotalSentReqs=_CgsProxTotalSentReqs_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,10),_CgsProxTotalSentReqs_Type())
cgsProxTotalSentReqs.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsProxTotalSentReqs.setStatus(_B)
if mibBuilder.loadTexts:cgsProxTotalSentReqs.setUnits(_N)
_CgsProxTotalRcvdResps_Type=Counter32
_CgsProxTotalRcvdResps_Object=MibTableColumn
cgsProxTotalRcvdResps=_CgsProxTotalRcvdResps_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,11),_CgsProxTotalRcvdResps_Type())
cgsProxTotalRcvdResps.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsProxTotalRcvdResps.setStatus(_B)
if mibBuilder.loadTexts:cgsProxTotalRcvdResps.setUnits(_O)
_CgsProxSendRate_Type=Unsigned32
_CgsProxSendRate_Object=MibTableColumn
cgsProxSendRate=_CgsProxSendRate_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,12),_CgsProxSendRate_Type())
cgsProxSendRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsProxSendRate.setStatus(_B)
if mibBuilder.loadTexts:cgsProxSendRate.setUnits(_K)
_CgsProxRcvdRate_Type=Unsigned32
_CgsProxRcvdRate_Object=MibTableColumn
cgsProxRcvdRate=_CgsProxRcvdRate_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,13),_CgsProxRcvdRate_Type())
cgsProxRcvdRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsProxRcvdRate.setStatus(_B)
if mibBuilder.loadTexts:cgsProxRcvdRate.setUnits(_K)
_CgsProxPeakSendRate_Type=Unsigned32
_CgsProxPeakSendRate_Object=MibTableColumn
cgsProxPeakSendRate=_CgsProxPeakSendRate_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,14),_CgsProxPeakSendRate_Type())
cgsProxPeakSendRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsProxPeakSendRate.setStatus(_B)
if mibBuilder.loadTexts:cgsProxPeakSendRate.setUnits(_K)
_CgsProxPeakRcvdRate_Type=Unsigned32
_CgsProxPeakRcvdRate_Object=MibTableColumn
cgsProxPeakRcvdRate=_CgsProxPeakRcvdRate_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,15),_CgsProxPeakRcvdRate_Type())
cgsProxPeakRcvdRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsProxPeakRcvdRate.setStatus(_B)
if mibBuilder.loadTexts:cgsProxPeakRcvdRate.setUnits(_K)
class _CgsProxStorageType_Type(StorageType):defaultValue=3
_CgsProxStorageType_Type.__name__=_I
_CgsProxStorageType_Object=MibTableColumn
cgsProxStorageType=_CgsProxStorageType_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,16),_CgsProxStorageType_Type())
cgsProxStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsProxStorageType.setStatus(_B)
_CgsProxRowStatus_Type=RowStatus
_CgsProxRowStatus_Object=MibTableColumn
cgsProxRowStatus=_CgsProxRowStatus_Object((1,3,6,1,4,1,9,9,589,1,5,1,1,17),_CgsProxRowStatus_Type())
cgsProxRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsProxRowStatus.setStatus(_B)
_CgsResources_ObjectIdentity=ObjectIdentity
cgsResources=_CgsResources_ObjectIdentity((1,3,6,1,4,1,9,9,589,1,6))
_CgsRegionTable_Object=MibTable
cgsRegionTable=_CgsRegionTable_Object((1,3,6,1,4,1,9,9,589,1,6,1))
if mibBuilder.loadTexts:cgsRegionTable.setStatus(_G)
_CgsRegionEntry_Object=MibTableRow
cgsRegionEntry=_CgsRegionEntry_Object((1,3,6,1,4,1,9,9,589,1,6,1,1))
cgsRegionEntry.setIndexNames((0,_A,_m))
if mibBuilder.loadTexts:cgsRegionEntry.setStatus(_G)
class _CgsRegionName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgsRegionName_Type.__name__=_E
_CgsRegionName_Object=MibTableColumn
cgsRegionName=_CgsRegionName_Object((1,3,6,1,4,1,9,9,589,1,6,1,1,1),_CgsRegionName_Type())
cgsRegionName.setMaxAccess(_H)
if mibBuilder.loadTexts:cgsRegionName.setStatus(_G)
class _CgsRegionComments_Type(SnmpAdminString):defaultValue=OctetString('')
_CgsRegionComments_Type.__name__=_E
_CgsRegionComments_Object=MibTableColumn
cgsRegionComments=_CgsRegionComments_Object((1,3,6,1,4,1,9,9,589,1,6,1,1,2),_CgsRegionComments_Type())
cgsRegionComments.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsRegionComments.setStatus(_G)
class _CgsRegionStorageType_Type(StorageType):defaultValue=3
_CgsRegionStorageType_Type.__name__=_I
_CgsRegionStorageType_Object=MibTableColumn
cgsRegionStorageType=_CgsRegionStorageType_Object((1,3,6,1,4,1,9,9,589,1,6,1,1,3),_CgsRegionStorageType_Type())
cgsRegionStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsRegionStorageType.setStatus(_G)
_CgsRegionRowStatus_Type=RowStatus
_CgsRegionRowStatus_Object=MibTableColumn
cgsRegionRowStatus=_CgsRegionRowStatus_Object((1,3,6,1,4,1,9,9,589,1,6,1,1,4),_CgsRegionRowStatus_Type())
cgsRegionRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsRegionRowStatus.setStatus(_G)
_CgsLocationTable_Object=MibTable
cgsLocationTable=_CgsLocationTable_Object((1,3,6,1,4,1,9,9,589,1,6,2))
if mibBuilder.loadTexts:cgsLocationTable.setStatus(_B)
_CgsLocationEntry_Object=MibTableRow
cgsLocationEntry=_CgsLocationEntry_Object((1,3,6,1,4,1,9,9,589,1,6,2,1))
cgsLocationEntry.setIndexNames((0,_A,_n))
if mibBuilder.loadTexts:cgsLocationEntry.setStatus(_B)
class _CgsLocationName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgsLocationName_Type.__name__=_E
_CgsLocationName_Object=MibTableColumn
cgsLocationName=_CgsLocationName_Object((1,3,6,1,4,1,9,9,589,1,6,2,1,1),_CgsLocationName_Type())
cgsLocationName.setMaxAccess(_H)
if mibBuilder.loadTexts:cgsLocationName.setStatus(_B)
_CgsLocationRegion_Type=SnmpAdminString
_CgsLocationRegion_Object=MibTableColumn
cgsLocationRegion=_CgsLocationRegion_Object((1,3,6,1,4,1,9,9,589,1,6,2,1,2),_CgsLocationRegion_Type())
cgsLocationRegion.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsLocationRegion.setStatus(_B)
class _CgsLocationZone_Type(SnmpAdminString):defaultValue=OctetString('')
_CgsLocationZone_Type.__name__=_E
_CgsLocationZone_Object=MibTableColumn
cgsLocationZone=_CgsLocationZone_Object((1,3,6,1,4,1,9,9,589,1,6,2,1,3),_CgsLocationZone_Type())
cgsLocationZone.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsLocationZone.setStatus(_B)
class _CgsLocationComments_Type(SnmpAdminString):defaultValue=OctetString('')
_CgsLocationComments_Type.__name__=_E
_CgsLocationComments_Object=MibTableColumn
cgsLocationComments=_CgsLocationComments_Object((1,3,6,1,4,1,9,9,589,1,6,2,1,4),_CgsLocationComments_Type())
cgsLocationComments.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsLocationComments.setStatus(_B)
class _CgsLocationStorageType_Type(StorageType):defaultValue=3
_CgsLocationStorageType_Type.__name__=_I
_CgsLocationStorageType_Object=MibTableColumn
cgsLocationStorageType=_CgsLocationStorageType_Object((1,3,6,1,4,1,9,9,589,1,6,2,1,5),_CgsLocationStorageType_Type())
cgsLocationStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsLocationStorageType.setStatus(_B)
_CgsLocationRowStatus_Type=RowStatus
_CgsLocationRowStatus_Object=MibTableColumn
cgsLocationRowStatus=_CgsLocationRowStatus_Object((1,3,6,1,4,1,9,9,589,1,6,2,1,6),_CgsLocationRowStatus_Type())
cgsLocationRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsLocationRowStatus.setStatus(_B)
_CgsRegionIdTable_Object=MibTable
cgsRegionIdTable=_CgsRegionIdTable_Object((1,3,6,1,4,1,9,9,589,1,6,3))
if mibBuilder.loadTexts:cgsRegionIdTable.setStatus(_B)
_CgsRegionIdEntry_Object=MibTableRow
cgsRegionIdEntry=_CgsRegionIdEntry_Object((1,3,6,1,4,1,9,9,589,1,6,3,1))
cgsRegionIdEntry.setIndexNames((0,_A,_o))
if mibBuilder.loadTexts:cgsRegionIdEntry.setStatus(_B)
class _CgsRegionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CgsRegionId_Type.__name__=_h
_CgsRegionId_Object=MibTableColumn
cgsRegionId=_CgsRegionId_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,1),_CgsRegionId_Type())
cgsRegionId.setMaxAccess(_H)
if mibBuilder.loadTexts:cgsRegionId.setStatus(_B)
class _CgsRegionIdName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_CgsRegionIdName_Type.__name__=_E
_CgsRegionIdName_Object=MibTableColumn
cgsRegionIdName=_CgsRegionIdName_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,2),_CgsRegionIdName_Type())
cgsRegionIdName.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsRegionIdName.setStatus(_B)
class _CgsRegionIdComments_Type(SnmpAdminString):defaultValue=OctetString('')
_CgsRegionIdComments_Type.__name__=_E
_CgsRegionIdComments_Object=MibTableColumn
cgsRegionIdComments=_CgsRegionIdComments_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,3),_CgsRegionIdComments_Type())
cgsRegionIdComments.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsRegionIdComments.setStatus(_B)
_CgsReqCountPerRegionId_Type=Counter32
_CgsReqCountPerRegionId_Object=MibTableColumn
cgsReqCountPerRegionId=_CgsReqCountPerRegionId_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,4),_CgsReqCountPerRegionId_Type())
cgsReqCountPerRegionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsReqCountPerRegionId.setStatus(_B)
if mibBuilder.loadTexts:cgsReqCountPerRegionId.setUnits(_P)
_CgsReqCountRatePerRegionId1Min_Type=Gauge32
_CgsReqCountRatePerRegionId1Min_Object=MibTableColumn
cgsReqCountRatePerRegionId1Min=_CgsReqCountRatePerRegionId1Min_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,5),_CgsReqCountRatePerRegionId1Min_Type())
cgsReqCountRatePerRegionId1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsReqCountRatePerRegionId1Min.setStatus(_B)
if mibBuilder.loadTexts:cgsReqCountRatePerRegionId1Min.setUnits(_F)
_CgsReqCountRatePerRegionId5Min_Type=Gauge32
_CgsReqCountRatePerRegionId5Min_Object=MibTableColumn
cgsReqCountRatePerRegionId5Min=_CgsReqCountRatePerRegionId5Min_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,6),_CgsReqCountRatePerRegionId5Min_Type())
cgsReqCountRatePerRegionId5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsReqCountRatePerRegionId5Min.setStatus(_B)
if mibBuilder.loadTexts:cgsReqCountRatePerRegionId5Min.setUnits(_F)
_CgsReqCountRatePerRegionId30Min_Type=Gauge32
_CgsReqCountRatePerRegionId30Min_Object=MibTableColumn
cgsReqCountRatePerRegionId30Min=_CgsReqCountRatePerRegionId30Min_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,7),_CgsReqCountRatePerRegionId30Min_Type())
cgsReqCountRatePerRegionId30Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsReqCountRatePerRegionId30Min.setStatus(_B)
if mibBuilder.loadTexts:cgsReqCountRatePerRegionId30Min.setUnits(_F)
_CgsReqCountRatePerRegionId4Hr_Type=Gauge32
_CgsReqCountRatePerRegionId4Hr_Object=MibTableColumn
cgsReqCountRatePerRegionId4Hr=_CgsReqCountRatePerRegionId4Hr_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,8),_CgsReqCountRatePerRegionId4Hr_Type())
cgsReqCountRatePerRegionId4Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsReqCountRatePerRegionId4Hr.setStatus(_B)
if mibBuilder.loadTexts:cgsReqCountRatePerRegionId4Hr.setUnits(_F)
_CgsAnswerCountPerRegionId_Type=Counter32
_CgsAnswerCountPerRegionId_Object=MibTableColumn
cgsAnswerCountPerRegionId=_CgsAnswerCountPerRegionId_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,9),_CgsAnswerCountPerRegionId_Type())
cgsAnswerCountPerRegionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsAnswerCountPerRegionId.setStatus(_B)
if mibBuilder.loadTexts:cgsAnswerCountPerRegionId.setUnits(_P)
_CgsAnswerCountRatePerRegionId1Min_Type=Gauge32
_CgsAnswerCountRatePerRegionId1Min_Object=MibTableColumn
cgsAnswerCountRatePerRegionId1Min=_CgsAnswerCountRatePerRegionId1Min_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,10),_CgsAnswerCountRatePerRegionId1Min_Type())
cgsAnswerCountRatePerRegionId1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsAnswerCountRatePerRegionId1Min.setStatus(_B)
if mibBuilder.loadTexts:cgsAnswerCountRatePerRegionId1Min.setUnits(_F)
_CgsAnswerCountRatePerRegionId5Min_Type=Gauge32
_CgsAnswerCountRatePerRegionId5Min_Object=MibTableColumn
cgsAnswerCountRatePerRegionId5Min=_CgsAnswerCountRatePerRegionId5Min_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,11),_CgsAnswerCountRatePerRegionId5Min_Type())
cgsAnswerCountRatePerRegionId5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsAnswerCountRatePerRegionId5Min.setStatus(_B)
if mibBuilder.loadTexts:cgsAnswerCountRatePerRegionId5Min.setUnits(_F)
_CgsAnswerCountRatePerRegionId30Min_Type=Gauge32
_CgsAnswerCountRatePerRegionId30Min_Object=MibTableColumn
cgsAnswerCountRatePerRegionId30Min=_CgsAnswerCountRatePerRegionId30Min_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,12),_CgsAnswerCountRatePerRegionId30Min_Type())
cgsAnswerCountRatePerRegionId30Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsAnswerCountRatePerRegionId30Min.setStatus(_B)
if mibBuilder.loadTexts:cgsAnswerCountRatePerRegionId30Min.setUnits(_F)
_CgsAnswerCountRatePerRegionId4Hr_Type=Gauge32
_CgsAnswerCountRatePerRegionId4Hr_Object=MibTableColumn
cgsAnswerCountRatePerRegionId4Hr=_CgsAnswerCountRatePerRegionId4Hr_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,13),_CgsAnswerCountRatePerRegionId4Hr_Type())
cgsAnswerCountRatePerRegionId4Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsAnswerCountRatePerRegionId4Hr.setStatus(_B)
if mibBuilder.loadTexts:cgsAnswerCountRatePerRegionId4Hr.setUnits(_F)
_CgsUnAnswerCountPerRegionId_Type=Counter32
_CgsUnAnswerCountPerRegionId_Object=MibTableColumn
cgsUnAnswerCountPerRegionId=_CgsUnAnswerCountPerRegionId_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,14),_CgsUnAnswerCountPerRegionId_Type())
cgsUnAnswerCountPerRegionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsUnAnswerCountPerRegionId.setStatus(_B)
if mibBuilder.loadTexts:cgsUnAnswerCountPerRegionId.setUnits(_P)
_CgsUnAnswerCountRatePerRegionId1Min_Type=Gauge32
_CgsUnAnswerCountRatePerRegionId1Min_Object=MibTableColumn
cgsUnAnswerCountRatePerRegionId1Min=_CgsUnAnswerCountRatePerRegionId1Min_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,15),_CgsUnAnswerCountRatePerRegionId1Min_Type())
cgsUnAnswerCountRatePerRegionId1Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsUnAnswerCountRatePerRegionId1Min.setStatus(_B)
if mibBuilder.loadTexts:cgsUnAnswerCountRatePerRegionId1Min.setUnits(_F)
_CgsUnAnswerCountRatePerRegionId5Min_Type=Gauge32
_CgsUnAnswerCountRatePerRegionId5Min_Object=MibTableColumn
cgsUnAnswerCountRatePerRegionId5Min=_CgsUnAnswerCountRatePerRegionId5Min_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,16),_CgsUnAnswerCountRatePerRegionId5Min_Type())
cgsUnAnswerCountRatePerRegionId5Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsUnAnswerCountRatePerRegionId5Min.setStatus(_B)
if mibBuilder.loadTexts:cgsUnAnswerCountRatePerRegionId5Min.setUnits(_F)
_CgsUnAnswerCountRatePerRegionId30Min_Type=Gauge32
_CgsUnAnswerCountRatePerRegionId30Min_Object=MibTableColumn
cgsUnAnswerCountRatePerRegionId30Min=_CgsUnAnswerCountRatePerRegionId30Min_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,17),_CgsUnAnswerCountRatePerRegionId30Min_Type())
cgsUnAnswerCountRatePerRegionId30Min.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsUnAnswerCountRatePerRegionId30Min.setStatus(_B)
if mibBuilder.loadTexts:cgsUnAnswerCountRatePerRegionId30Min.setUnits(_F)
_CgsUnAnswerCountRatePerRegionId4Hr_Type=Gauge32
_CgsUnAnswerCountRatePerRegionId4Hr_Object=MibTableColumn
cgsUnAnswerCountRatePerRegionId4Hr=_CgsUnAnswerCountRatePerRegionId4Hr_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,18),_CgsUnAnswerCountRatePerRegionId4Hr_Type())
cgsUnAnswerCountRatePerRegionId4Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cgsUnAnswerCountRatePerRegionId4Hr.setStatus(_B)
if mibBuilder.loadTexts:cgsUnAnswerCountRatePerRegionId4Hr.setUnits(_F)
class _CgsRegionIdStorageType_Type(StorageType):defaultValue=3
_CgsRegionIdStorageType_Type.__name__=_I
_CgsRegionIdStorageType_Object=MibTableColumn
cgsRegionIdStorageType=_CgsRegionIdStorageType_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,19),_CgsRegionIdStorageType_Type())
cgsRegionIdStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsRegionIdStorageType.setStatus(_B)
_CgsRegionIdRowStatus_Type=RowStatus
_CgsRegionIdRowStatus_Object=MibTableColumn
cgsRegionIdRowStatus=_CgsRegionIdRowStatus_Object((1,3,6,1,4,1,9,9,589,1,6,3,1,20),_CgsRegionIdRowStatus_Type())
cgsRegionIdRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cgsRegionIdRowStatus.setStatus(_B)
_CiscoGslbSystemMIBConform_ObjectIdentity=ObjectIdentity
ciscoGslbSystemMIBConform=_CiscoGslbSystemMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,589,2))
_CiscoGslbSystemMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoGslbSystemMIBCompliances=_CiscoGslbSystemMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,589,2,1))
_CiscoGslbSystemMIBGroups_ObjectIdentity=ObjectIdentity
ciscoGslbSystemMIBGroups=_CiscoGslbSystemMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,589,2,2))
ciscoGslbSystemGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,9,589,2,2,1))
ciscoGslbSystemGeneralGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:ciscoGslbSystemGeneralGroup.setStatus(_B)
ciscoGslbSystemPeerGroup=ObjectGroup((1,3,6,1,4,1,9,9,589,2,2,2))
ciscoGslbSystemPeerGroup.setObjects(*((_A,_v),(_A,_Q),(_A,_R),(_A,_S),(_A,_w)))
if mibBuilder.loadTexts:ciscoGslbSystemPeerGroup.setStatus(_B)
ciscoGslbSystemProxZoneGroup=ObjectGroup((1,3,6,1,4,1,9,9,589,2,2,3))
ciscoGslbSystemProxZoneGroup.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:ciscoGslbSystemProxZoneGroup.setStatus(_B)
ciscoGslbSystemResourceGroup=ObjectGroup((1,3,6,1,4,1,9,9,589,2,2,4))
ciscoGslbSystemResourceGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoGslbSystemResourceGroup.setStatus(_G)
ciscoGslbSystemNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,589,2,2,5))
ciscoGslbSystemNotifControlGroup.setObjects((_A,_AG))
if mibBuilder.loadTexts:ciscoGslbSystemNotifControlGroup.setStatus(_B)
ciscoGslbSystemNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,589,2,2,6))
ciscoGslbSystemNotifObjectsGroup.setObjects((_A,_Y))
if mibBuilder.loadTexts:ciscoGslbSystemNotifObjectsGroup.setStatus(_B)
ciscoGslbSystemResourceLocationGroup=ObjectGroup((1,3,6,1,4,1,9,9,589,2,2,8))
ciscoGslbSystemResourceLocationGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoGslbSystemResourceLocationGroup.setStatus(_B)
ciscoGslbSystemResourceRegionGroup=ObjectGroup((1,3,6,1,4,1,9,9,589,2,2,9))
ciscoGslbSystemResourceRegionGroup.setObjects(*((_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ)))
if mibBuilder.loadTexts:ciscoGslbSystemResourceRegionGroup.setStatus(_B)
ciscoGslbSystemPeerEventStatus=NotificationType((1,3,6,1,4,1,9,9,589,0,1))
ciscoGslbSystemPeerEventStatus.setObjects(*((_f,_g),(_A,_Q),(_A,_R),(_A,_Y),(_A,_S)))
if mibBuilder.loadTexts:ciscoGslbSystemPeerEventStatus.setStatus(_B)
ciscoGslbSystemNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,589,2,2,7))
ciscoGslbSystemNotifGroup.setObjects((_A,_Aa))
if mibBuilder.loadTexts:ciscoGslbSystemNotifGroup.setStatus(_B)
ciscoGslbSystemMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,589,2,1,1))
ciscoGslbSystemMIBCompliance.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_Ab),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:ciscoGslbSystemMIBCompliance.setStatus(_G)
ciscoGslbSystemMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,589,2,1,2))
ciscoGslbSystemMIBComplianceRev1.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:ciscoGslbSystemMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoGslbSystemMIB':ciscoGslbSystemMIB,'ciscoGslbSystemMIBNotifs':ciscoGslbSystemMIBNotifs,_Aa:ciscoGslbSystemPeerEventStatus,'ciscoGslbSystemMIBObjects':ciscoGslbSystemMIBObjects,'cgsNotifControl':cgsNotifControl,_AG:cgsPeerEventNotifEnable,'cgsNotifObjects':cgsNotifObjects,_Y:cgsPeerPrevStatus,'cgsGeneral':cgsGeneral,_p:cgsNodeService,_q:cgsNodeCommIfName,_r:cgsNodeCommIfIndex,_s:cgsNodeStatus,_t:cgsNodeLocation,_u:cgsNodeRegion,'cgsPeer':cgsPeer,'cgsPeerTable':cgsPeerTable,'cgsPeerEntry':cgsPeerEntry,_j:cgsPeerAddressType,_k:cgsPeerAddress,_v:cgsPeerLocation,_Q:cgsPeerDnsName,_R:cgsPeerService,_S:cgsPeerStatus,_w:cgsPeerVersion,'cgsProxZoneStats':cgsProxZoneStats,'cgsProxZoneTable':cgsProxZoneTable,'cgsProxZoneEntry':cgsProxZoneEntry,_l:cgsProxZoneName,_x:cgsProxPrimaryAddressType,_y:cgsProxPrimaryAddress,_z:cgsProxSecondaryAddressType,_A0:cgsProxSecondaryAddress,_A1:cgsProxEchoSentReqs,_A2:cgsProxEchoRcvdResps,_A3:cgsProxSentMeasureReqs,_A4:cgsProxRcvdMeasureResps,_A5:cgsProxTotalSentReqs,_A6:cgsProxTotalRcvdResps,_A7:cgsProxSendRate,_A8:cgsProxRcvdRate,_A9:cgsProxPeakSendRate,_AA:cgsProxPeakRcvdRate,_AB:cgsProxStorageType,_AC:cgsProxRowStatus,'cgsResources':cgsResources,'cgsRegionTable':cgsRegionTable,'cgsRegionEntry':cgsRegionEntry,_m:cgsRegionName,_AD:cgsRegionComments,_AE:cgsRegionStorageType,_AF:cgsRegionRowStatus,'cgsLocationTable':cgsLocationTable,'cgsLocationEntry':cgsLocationEntry,_n:cgsLocationName,_T:cgsLocationRegion,_U:cgsLocationZone,_V:cgsLocationComments,_W:cgsLocationStorageType,_X:cgsLocationRowStatus,'cgsRegionIdTable':cgsRegionIdTable,'cgsRegionIdEntry':cgsRegionIdEntry,_o:cgsRegionId,_AH:cgsRegionIdName,_AI:cgsRegionIdComments,_AJ:cgsReqCountPerRegionId,_AK:cgsReqCountRatePerRegionId1Min,_AL:cgsReqCountRatePerRegionId5Min,_AM:cgsReqCountRatePerRegionId30Min,_AN:cgsReqCountRatePerRegionId4Hr,_AO:cgsAnswerCountPerRegionId,_AP:cgsAnswerCountRatePerRegionId1Min,_AQ:cgsAnswerCountRatePerRegionId5Min,_AR:cgsAnswerCountRatePerRegionId30Min,_AS:cgsAnswerCountRatePerRegionId4Hr,_AT:cgsUnAnswerCountPerRegionId,_AU:cgsUnAnswerCountRatePerRegionId1Min,_AV:cgsUnAnswerCountRatePerRegionId5Min,_AW:cgsUnAnswerCountRatePerRegionId30Min,_AX:cgsUnAnswerCountRatePerRegionId4Hr,_AY:cgsRegionIdStorageType,_AZ:cgsRegionIdRowStatus,'ciscoGslbSystemMIBConform':ciscoGslbSystemMIBConform,'ciscoGslbSystemMIBCompliances':ciscoGslbSystemMIBCompliances,'ciscoGslbSystemMIBCompliance':ciscoGslbSystemMIBCompliance,'ciscoGslbSystemMIBComplianceRev1':ciscoGslbSystemMIBComplianceRev1,'ciscoGslbSystemMIBGroups':ciscoGslbSystemMIBGroups,_Z:ciscoGslbSystemGeneralGroup,_a:ciscoGslbSystemPeerGroup,_b:ciscoGslbSystemProxZoneGroup,_Ab:ciscoGslbSystemResourceGroup,_c:ciscoGslbSystemNotifControlGroup,_d:ciscoGslbSystemNotifObjectsGroup,_e:ciscoGslbSystemNotifGroup,_Ac:ciscoGslbSystemResourceLocationGroup,_Ad:ciscoGslbSystemResourceRegionGroup})