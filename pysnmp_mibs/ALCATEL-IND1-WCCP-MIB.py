_AS='wccpTrapsGroup'
_AR='wccpStatisticsGroup'
_AQ='wccpRestrictPortGroup'
_AP='wccpRestrictWebCacheGroup'
_AO='wccpRestrictVlanGroup'
_AN='wccpRouterGroup'
_AM='wccpWebCacheGroup'
_AL='wccpServiceGroup'
_AK='wccpFeatureGroup'
_AJ='wccpTrapOperStatus'
_AI='wccpStatsReset'
_AH='wccpStatsAuthFailures'
_AG='wccpStatsPacketsDeniedRedir'
_AF='wccpStatsPacketsLowRedir'
_AE='wccpStatsPacketsRedir'
_AD='wccpStatsMessagesDropped'
_AC='wccpStatsMessagesTransmitted'
_AB='wccpStatsMessagesReceived'
_AA='wccpRestrictPortRowStatus'
_A9='wccpRestrictWebCacheRowStatus'
_A8='wccpRestrictVlanRowStatus'
_A7='wccpRouterProtoVersion'
_A6='wccpWebCacheState'
_A5='wccpWebCacheConnectTime'
_A4='wccpWebCacheNumberOfWebCaches'
_A3='wccpWebCacheNumberOfRouters'
_A2='wccpWebCacheChangeNum'
_A1='wccpWebCacheReceiveId'
_A0='wccpWebCacheProtoVersion'
_z='wccpServicePortPortNum'
_y='wccpServiceRowStatus'
_x='wccpServicePrecedence'
_w='wccpServiceChangeNumber'
_v='wccpServiceReceiveId'
_u='wccpServiceWebCacheCount'
_t='wccpServiceVersion'
_s='wccpServiceType'
_r='wccpServicePassword'
_q='wccpServiceAdminEnabled'
_p='wccpServicePortType'
_o='wccpServiceMessageType'
_n='wccpServiceProtocol'
_m='wccpGlobalStatsReset'
_l='wccpGlobalStatsMessageInvalid'
_k='wccpServiceCount'
_j='wccpAdminEnabled'
_i='wccpStatsServiceId'
_h='wccpRestrictPortIndex'
_g='wccpRestrictPortServiceId'
_f='wccpRestrictWebCacheIpMask'
_e='wccpRestrictWebCacheIpMaskAddressType'
_d='wccpRestrictWebCacheIpAddress'
_c='wccpRestrictWebCacheIpAddressType'
_b='wccpRestrictWebCacheServiceId'
_a='wccpRestrictVlanVlanId'
_Z='wccpRestrictVlanServiceId'
_Y='wccpRouterIpAddress'
_X='wccpRouterIpAddressType'
_W='wccpRouterServiceId'
_V='wccpWebCacheIpAddress'
_U='wccpWebCacheIpAddressType'
_T='wccpWebCacheServiceId'
_S='wccpServicePortPortId'
_R='wccpServicePortServiceId'
_Q='wccpServiceId'
_P='default'
_O='SnmpAdminString'
_N='wccpTrapInfoWebCacheIpAddr'
_M='wccpTrapInfoServiceId'
_L='wccpTrapInfoOperStatus'
_K='wccpTrapInfoEntityGroup'
_J='read-write'
_I='unknown'
_H='InetAddressType'
_G='InetAddress'
_F='read-create'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='ALCATEL-IND1-WCCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Wccp,wccpTraps=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1Wccp','wccpTraps')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
alcatelIND1WCCPMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1))
class WccpServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('standard',1),('dynamic',2),(_I,3)))
class WccpVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('version1',1),('version2',2),(_I,3)))
class WccpServiceProtocolType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tcp',1),('udp',2),(_I,3)))
class WccpServiceMessageType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('multicast',2),(_I,3)))
class WccpServicePortType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('source',1),('destination',2),(_I,3)))
class WccpOperState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('outOfService',1),('inService',2)))
_AlcatelIND1WCCPMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1WCCPMIBNotifications=_AlcatelIND1WCCPMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,0))
if mibBuilder.loadTexts:alcatelIND1WCCPMIBNotifications.setStatus(_A)
_AlcatelIND1WCCPMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1WCCPMIBObjects=_AlcatelIND1WCCPMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,1))
if mibBuilder.loadTexts:alcatelIND1WCCPMIBObjects.setStatus(_A)
_WccpFeature_ObjectIdentity=ObjectIdentity
wccpFeature=_WccpFeature_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,1))
_WccpAdminEnabled_Type=TruthValue
_WccpAdminEnabled_Object=MibScalar
wccpAdminEnabled=_WccpAdminEnabled_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,1,1),_WccpAdminEnabled_Type())
wccpAdminEnabled.setMaxAccess(_J)
if mibBuilder.loadTexts:wccpAdminEnabled.setStatus(_A)
_WccpServiceCount_Type=Counter32
_WccpServiceCount_Object=MibScalar
wccpServiceCount=_WccpServiceCount_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,1,2),_WccpServiceCount_Type())
wccpServiceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpServiceCount.setStatus(_A)
class _WccpGlobalStatsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('reset',2)))
_WccpGlobalStatsReset_Type.__name__=_E
_WccpGlobalStatsReset_Object=MibScalar
wccpGlobalStatsReset=_WccpGlobalStatsReset_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,1,3),_WccpGlobalStatsReset_Type())
wccpGlobalStatsReset.setMaxAccess(_J)
if mibBuilder.loadTexts:wccpGlobalStatsReset.setStatus(_A)
_WccpGlobalStatsMessageInvalid_Type=Counter32
_WccpGlobalStatsMessageInvalid_Object=MibScalar
wccpGlobalStatsMessageInvalid=_WccpGlobalStatsMessageInvalid_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,1,4),_WccpGlobalStatsMessageInvalid_Type())
wccpGlobalStatsMessageInvalid.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpGlobalStatsMessageInvalid.setStatus(_A)
_WccpServices_ObjectIdentity=ObjectIdentity
wccpServices=_WccpServices_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2))
_WccpServiceTable_Object=MibTable
wccpServiceTable=_WccpServiceTable_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1))
if mibBuilder.loadTexts:wccpServiceTable.setStatus(_A)
_WccpServiceTableEntry_Object=MibTableRow
wccpServiceTableEntry=_WccpServiceTableEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1))
wccpServiceTableEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:wccpServiceTableEntry.setStatus(_A)
class _WccpServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WccpServiceId_Type.__name__=_E
_WccpServiceId_Object=MibTableColumn
wccpServiceId=_WccpServiceId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,1),_WccpServiceId_Type())
wccpServiceId.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpServiceId.setStatus(_A)
_WccpServiceProtocol_Type=WccpServiceProtocolType
_WccpServiceProtocol_Object=MibTableColumn
wccpServiceProtocol=_WccpServiceProtocol_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,2),_WccpServiceProtocol_Type())
wccpServiceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpServiceProtocol.setStatus(_A)
_WccpServiceMessageType_Type=WccpServiceMessageType
_WccpServiceMessageType_Object=MibTableColumn
wccpServiceMessageType=_WccpServiceMessageType_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,3),_WccpServiceMessageType_Type())
wccpServiceMessageType.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpServiceMessageType.setStatus(_A)
_WccpServicePortType_Type=WccpServicePortType
_WccpServicePortType_Object=MibTableColumn
wccpServicePortType=_WccpServicePortType_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,4),_WccpServicePortType_Type())
wccpServicePortType.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpServicePortType.setStatus(_A)
_WccpServiceAdminEnabled_Type=TruthValue
_WccpServiceAdminEnabled_Object=MibTableColumn
wccpServiceAdminEnabled=_WccpServiceAdminEnabled_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,5),_WccpServiceAdminEnabled_Type())
wccpServiceAdminEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:wccpServiceAdminEnabled.setStatus(_A)
class _WccpServicePassword_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_WccpServicePassword_Type.__name__=_O
_WccpServicePassword_Object=MibTableColumn
wccpServicePassword=_WccpServicePassword_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,6),_WccpServicePassword_Type())
wccpServicePassword.setMaxAccess(_F)
if mibBuilder.loadTexts:wccpServicePassword.setStatus(_A)
_WccpServiceType_Type=WccpServiceType
_WccpServiceType_Object=MibTableColumn
wccpServiceType=_WccpServiceType_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,7),_WccpServiceType_Type())
wccpServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpServiceType.setStatus(_A)
_WccpServiceVersion_Type=WccpVersion
_WccpServiceVersion_Object=MibTableColumn
wccpServiceVersion=_WccpServiceVersion_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,8),_WccpServiceVersion_Type())
wccpServiceVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpServiceVersion.setStatus(_A)
_WccpServiceWebCacheCount_Type=Counter32
_WccpServiceWebCacheCount_Object=MibTableColumn
wccpServiceWebCacheCount=_WccpServiceWebCacheCount_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,9),_WccpServiceWebCacheCount_Type())
wccpServiceWebCacheCount.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpServiceWebCacheCount.setStatus(_A)
_WccpServiceReceiveId_Type=Counter32
_WccpServiceReceiveId_Object=MibTableColumn
wccpServiceReceiveId=_WccpServiceReceiveId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,10),_WccpServiceReceiveId_Type())
wccpServiceReceiveId.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpServiceReceiveId.setStatus(_A)
_WccpServiceChangeNumber_Type=Counter32
_WccpServiceChangeNumber_Object=MibTableColumn
wccpServiceChangeNumber=_WccpServiceChangeNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,11),_WccpServiceChangeNumber_Type())
wccpServiceChangeNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpServiceChangeNumber.setStatus(_A)
class _WccpServicePrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WccpServicePrecedence_Type.__name__=_E
_WccpServicePrecedence_Object=MibTableColumn
wccpServicePrecedence=_WccpServicePrecedence_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,12),_WccpServicePrecedence_Type())
wccpServicePrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpServicePrecedence.setStatus(_A)
_WccpServiceRowStatus_Type=RowStatus
_WccpServiceRowStatus_Object=MibTableColumn
wccpServiceRowStatus=_WccpServiceRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,1,1,13),_WccpServiceRowStatus_Type())
wccpServiceRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wccpServiceRowStatus.setStatus(_A)
_WccpServicePortTable_Object=MibTable
wccpServicePortTable=_WccpServicePortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,2))
if mibBuilder.loadTexts:wccpServicePortTable.setStatus(_A)
_WccpServicePortTableEntry_Object=MibTableRow
wccpServicePortTableEntry=_WccpServicePortTableEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,2,1))
wccpServicePortTableEntry.setIndexNames((0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:wccpServicePortTableEntry.setStatus(_A)
class _WccpServicePortServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WccpServicePortServiceId_Type.__name__=_E
_WccpServicePortServiceId_Object=MibTableColumn
wccpServicePortServiceId=_WccpServicePortServiceId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,2,1,1),_WccpServicePortServiceId_Type())
wccpServicePortServiceId.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpServicePortServiceId.setStatus(_A)
class _WccpServicePortPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WccpServicePortPortId_Type.__name__=_E
_WccpServicePortPortId_Object=MibTableColumn
wccpServicePortPortId=_WccpServicePortPortId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,2,1,2),_WccpServicePortPortId_Type())
wccpServicePortPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpServicePortPortId.setStatus(_A)
_WccpServicePortPortNum_Type=Integer32
_WccpServicePortPortNum_Object=MibTableColumn
wccpServicePortPortNum=_WccpServicePortPortNum_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,2,2,1,3),_WccpServicePortPortNum_Type())
wccpServicePortPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpServicePortPortNum.setStatus(_A)
_WccpWebCaches_ObjectIdentity=ObjectIdentity
wccpWebCaches=_WccpWebCaches_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3))
_WccpWebCacheTable_Object=MibTable
wccpWebCacheTable=_WccpWebCacheTable_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1))
if mibBuilder.loadTexts:wccpWebCacheTable.setStatus(_A)
_WccpWebCacheTableEntry_Object=MibTableRow
wccpWebCacheTableEntry=_WccpWebCacheTableEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1,1))
wccpWebCacheTableEntry.setIndexNames((0,_B,_T),(0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:wccpWebCacheTableEntry.setStatus(_A)
class _WccpWebCacheServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WccpWebCacheServiceId_Type.__name__=_E
_WccpWebCacheServiceId_Object=MibTableColumn
wccpWebCacheServiceId=_WccpWebCacheServiceId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1,1,1),_WccpWebCacheServiceId_Type())
wccpWebCacheServiceId.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpWebCacheServiceId.setStatus(_A)
class _WccpWebCacheIpAddressType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_WccpWebCacheIpAddressType_Type.__name__=_H
_WccpWebCacheIpAddressType_Object=MibTableColumn
wccpWebCacheIpAddressType=_WccpWebCacheIpAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1,1,2),_WccpWebCacheIpAddressType_Type())
wccpWebCacheIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpWebCacheIpAddressType.setStatus(_A)
class _WccpWebCacheIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_WccpWebCacheIpAddress_Type.__name__=_G
_WccpWebCacheIpAddress_Object=MibTableColumn
wccpWebCacheIpAddress=_WccpWebCacheIpAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1,1,3),_WccpWebCacheIpAddress_Type())
wccpWebCacheIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpWebCacheIpAddress.setStatus(_A)
_WccpWebCacheProtoVersion_Type=WccpVersion
_WccpWebCacheProtoVersion_Object=MibTableColumn
wccpWebCacheProtoVersion=_WccpWebCacheProtoVersion_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1,1,4),_WccpWebCacheProtoVersion_Type())
wccpWebCacheProtoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpWebCacheProtoVersion.setStatus(_A)
_WccpWebCacheReceiveId_Type=Counter32
_WccpWebCacheReceiveId_Object=MibTableColumn
wccpWebCacheReceiveId=_WccpWebCacheReceiveId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1,1,5),_WccpWebCacheReceiveId_Type())
wccpWebCacheReceiveId.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpWebCacheReceiveId.setStatus(_A)
_WccpWebCacheChangeNum_Type=Counter32
_WccpWebCacheChangeNum_Object=MibTableColumn
wccpWebCacheChangeNum=_WccpWebCacheChangeNum_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1,1,6),_WccpWebCacheChangeNum_Type())
wccpWebCacheChangeNum.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpWebCacheChangeNum.setStatus(_A)
_WccpWebCacheNumberOfRouters_Type=Counter32
_WccpWebCacheNumberOfRouters_Object=MibTableColumn
wccpWebCacheNumberOfRouters=_WccpWebCacheNumberOfRouters_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1,1,7),_WccpWebCacheNumberOfRouters_Type())
wccpWebCacheNumberOfRouters.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpWebCacheNumberOfRouters.setStatus(_A)
_WccpWebCacheNumberOfWebCaches_Type=Counter32
_WccpWebCacheNumberOfWebCaches_Object=MibTableColumn
wccpWebCacheNumberOfWebCaches=_WccpWebCacheNumberOfWebCaches_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1,1,8),_WccpWebCacheNumberOfWebCaches_Type())
wccpWebCacheNumberOfWebCaches.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpWebCacheNumberOfWebCaches.setStatus(_A)
_WccpWebCacheState_Type=WccpOperState
_WccpWebCacheState_Object=MibTableColumn
wccpWebCacheState=_WccpWebCacheState_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1,1,9),_WccpWebCacheState_Type())
wccpWebCacheState.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpWebCacheState.setStatus(_A)
_WccpWebCacheConnectTime_Type=DateAndTime
_WccpWebCacheConnectTime_Object=MibTableColumn
wccpWebCacheConnectTime=_WccpWebCacheConnectTime_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,3,1,1,10),_WccpWebCacheConnectTime_Type())
wccpWebCacheConnectTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpWebCacheConnectTime.setStatus(_A)
_WccpRouters_ObjectIdentity=ObjectIdentity
wccpRouters=_WccpRouters_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,4))
_WccpRouterTable_Object=MibTable
wccpRouterTable=_WccpRouterTable_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,4,1))
if mibBuilder.loadTexts:wccpRouterTable.setStatus(_A)
_WccpRouterTableEntry_Object=MibTableRow
wccpRouterTableEntry=_WccpRouterTableEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,4,1,1))
wccpRouterTableEntry.setIndexNames((0,_B,_W),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:wccpRouterTableEntry.setStatus(_A)
class _WccpRouterServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WccpRouterServiceId_Type.__name__=_E
_WccpRouterServiceId_Object=MibTableColumn
wccpRouterServiceId=_WccpRouterServiceId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,4,1,1,1),_WccpRouterServiceId_Type())
wccpRouterServiceId.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRouterServiceId.setStatus(_A)
class _WccpRouterIpAddressType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_WccpRouterIpAddressType_Type.__name__=_H
_WccpRouterIpAddressType_Object=MibTableColumn
wccpRouterIpAddressType=_WccpRouterIpAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,4,1,1,2),_WccpRouterIpAddressType_Type())
wccpRouterIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRouterIpAddressType.setStatus(_A)
class _WccpRouterIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_WccpRouterIpAddress_Type.__name__=_G
_WccpRouterIpAddress_Object=MibTableColumn
wccpRouterIpAddress=_WccpRouterIpAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,4,1,1,3),_WccpRouterIpAddress_Type())
wccpRouterIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRouterIpAddress.setStatus(_A)
_WccpRouterProtoVersion_Type=WccpVersion
_WccpRouterProtoVersion_Object=MibTableColumn
wccpRouterProtoVersion=_WccpRouterProtoVersion_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,4,1,1,4),_WccpRouterProtoVersion_Type())
wccpRouterProtoVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpRouterProtoVersion.setStatus(_A)
_WccpRestrictVlan_ObjectIdentity=ObjectIdentity
wccpRestrictVlan=_WccpRestrictVlan_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,5))
_WccpRestrictVlanTable_Object=MibTable
wccpRestrictVlanTable=_WccpRestrictVlanTable_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,5,1))
if mibBuilder.loadTexts:wccpRestrictVlanTable.setStatus(_A)
_WccpRestrictVlanTableEntry_Object=MibTableRow
wccpRestrictVlanTableEntry=_WccpRestrictVlanTableEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,5,1,1))
wccpRestrictVlanTableEntry.setIndexNames((0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:wccpRestrictVlanTableEntry.setStatus(_A)
class _WccpRestrictVlanServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WccpRestrictVlanServiceId_Type.__name__=_E
_WccpRestrictVlanServiceId_Object=MibTableColumn
wccpRestrictVlanServiceId=_WccpRestrictVlanServiceId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,5,1,1,1),_WccpRestrictVlanServiceId_Type())
wccpRestrictVlanServiceId.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRestrictVlanServiceId.setStatus(_A)
class _WccpRestrictVlanVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_WccpRestrictVlanVlanId_Type.__name__=_E
_WccpRestrictVlanVlanId_Object=MibTableColumn
wccpRestrictVlanVlanId=_WccpRestrictVlanVlanId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,5,1,1,2),_WccpRestrictVlanVlanId_Type())
wccpRestrictVlanVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRestrictVlanVlanId.setStatus(_A)
_WccpRestrictVlanRowStatus_Type=RowStatus
_WccpRestrictVlanRowStatus_Object=MibTableColumn
wccpRestrictVlanRowStatus=_WccpRestrictVlanRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,5,1,1,3),_WccpRestrictVlanRowStatus_Type())
wccpRestrictVlanRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wccpRestrictVlanRowStatus.setStatus(_A)
_WccpRestrictWebCache_ObjectIdentity=ObjectIdentity
wccpRestrictWebCache=_WccpRestrictWebCache_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,6))
_WccpRestrictWebCacheTable_Object=MibTable
wccpRestrictWebCacheTable=_WccpRestrictWebCacheTable_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,6,1))
if mibBuilder.loadTexts:wccpRestrictWebCacheTable.setStatus(_A)
_WccpRestrictWebCacheTableEntry_Object=MibTableRow
wccpRestrictWebCacheTableEntry=_WccpRestrictWebCacheTableEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,6,1,1))
wccpRestrictWebCacheTableEntry.setIndexNames((0,_B,_b),(0,_B,_c),(0,_B,_d),(0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:wccpRestrictWebCacheTableEntry.setStatus(_A)
class _WccpRestrictWebCacheServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WccpRestrictWebCacheServiceId_Type.__name__=_E
_WccpRestrictWebCacheServiceId_Object=MibTableColumn
wccpRestrictWebCacheServiceId=_WccpRestrictWebCacheServiceId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,6,1,1,1),_WccpRestrictWebCacheServiceId_Type())
wccpRestrictWebCacheServiceId.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRestrictWebCacheServiceId.setStatus(_A)
class _WccpRestrictWebCacheIpAddressType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_WccpRestrictWebCacheIpAddressType_Type.__name__=_H
_WccpRestrictWebCacheIpAddressType_Object=MibTableColumn
wccpRestrictWebCacheIpAddressType=_WccpRestrictWebCacheIpAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,6,1,1,2),_WccpRestrictWebCacheIpAddressType_Type())
wccpRestrictWebCacheIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRestrictWebCacheIpAddressType.setStatus(_A)
class _WccpRestrictWebCacheIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_WccpRestrictWebCacheIpAddress_Type.__name__=_G
_WccpRestrictWebCacheIpAddress_Object=MibTableColumn
wccpRestrictWebCacheIpAddress=_WccpRestrictWebCacheIpAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,6,1,1,3),_WccpRestrictWebCacheIpAddress_Type())
wccpRestrictWebCacheIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRestrictWebCacheIpAddress.setStatus(_A)
class _WccpRestrictWebCacheIpMaskAddressType_Type(InetAddressType):subtypeSpec=InetAddressType.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2))
_WccpRestrictWebCacheIpMaskAddressType_Type.__name__=_H
_WccpRestrictWebCacheIpMaskAddressType_Object=MibTableColumn
wccpRestrictWebCacheIpMaskAddressType=_WccpRestrictWebCacheIpMaskAddressType_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,6,1,1,4),_WccpRestrictWebCacheIpMaskAddressType_Type())
wccpRestrictWebCacheIpMaskAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRestrictWebCacheIpMaskAddressType.setStatus(_A)
class _WccpRestrictWebCacheIpMask_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_WccpRestrictWebCacheIpMask_Type.__name__=_G
_WccpRestrictWebCacheIpMask_Object=MibTableColumn
wccpRestrictWebCacheIpMask=_WccpRestrictWebCacheIpMask_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,6,1,1,5),_WccpRestrictWebCacheIpMask_Type())
wccpRestrictWebCacheIpMask.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRestrictWebCacheIpMask.setStatus(_A)
_WccpRestrictWebCacheRowStatus_Type=RowStatus
_WccpRestrictWebCacheRowStatus_Object=MibTableColumn
wccpRestrictWebCacheRowStatus=_WccpRestrictWebCacheRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,6,1,1,6),_WccpRestrictWebCacheRowStatus_Type())
wccpRestrictWebCacheRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wccpRestrictWebCacheRowStatus.setStatus(_A)
_WccpRestrictPort_ObjectIdentity=ObjectIdentity
wccpRestrictPort=_WccpRestrictPort_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,7))
_WccpRestrictPortTable_Object=MibTable
wccpRestrictPortTable=_WccpRestrictPortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,7,1))
if mibBuilder.loadTexts:wccpRestrictPortTable.setStatus(_A)
_WccpRestrictPortTableEntry_Object=MibTableRow
wccpRestrictPortTableEntry=_WccpRestrictPortTableEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,7,1,1))
wccpRestrictPortTableEntry.setIndexNames((0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:wccpRestrictPortTableEntry.setStatus(_A)
class _WccpRestrictPortServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WccpRestrictPortServiceId_Type.__name__=_E
_WccpRestrictPortServiceId_Object=MibTableColumn
wccpRestrictPortServiceId=_WccpRestrictPortServiceId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,7,1,1,1),_WccpRestrictPortServiceId_Type())
wccpRestrictPortServiceId.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRestrictPortServiceId.setStatus(_A)
_WccpRestrictPortIndex_Type=InterfaceIndex
_WccpRestrictPortIndex_Object=MibTableColumn
wccpRestrictPortIndex=_WccpRestrictPortIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,7,1,1,2),_WccpRestrictPortIndex_Type())
wccpRestrictPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpRestrictPortIndex.setStatus(_A)
_WccpRestrictPortRowStatus_Type=RowStatus
_WccpRestrictPortRowStatus_Object=MibTableColumn
wccpRestrictPortRowStatus=_WccpRestrictPortRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,7,1,1,3),_WccpRestrictPortRowStatus_Type())
wccpRestrictPortRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wccpRestrictPortRowStatus.setStatus(_A)
_WccpStatistics_ObjectIdentity=ObjectIdentity
wccpStatistics=_WccpStatistics_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8))
_WccpStatisticsTable_Object=MibTable
wccpStatisticsTable=_WccpStatisticsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8,1))
if mibBuilder.loadTexts:wccpStatisticsTable.setStatus(_A)
_WccpStatisticsTableEntry_Object=MibTableRow
wccpStatisticsTableEntry=_WccpStatisticsTableEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8,1,1))
wccpStatisticsTableEntry.setIndexNames((0,_B,_i))
if mibBuilder.loadTexts:wccpStatisticsTableEntry.setStatus(_A)
class _WccpStatsServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WccpStatsServiceId_Type.__name__=_E
_WccpStatsServiceId_Object=MibTableColumn
wccpStatsServiceId=_WccpStatsServiceId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8,1,1,1),_WccpStatsServiceId_Type())
wccpStatsServiceId.setMaxAccess(_D)
if mibBuilder.loadTexts:wccpStatsServiceId.setStatus(_A)
_WccpStatsMessagesReceived_Type=Counter32
_WccpStatsMessagesReceived_Object=MibTableColumn
wccpStatsMessagesReceived=_WccpStatsMessagesReceived_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8,1,1,2),_WccpStatsMessagesReceived_Type())
wccpStatsMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpStatsMessagesReceived.setStatus(_A)
_WccpStatsMessagesTransmitted_Type=Counter32
_WccpStatsMessagesTransmitted_Object=MibTableColumn
wccpStatsMessagesTransmitted=_WccpStatsMessagesTransmitted_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8,1,1,3),_WccpStatsMessagesTransmitted_Type())
wccpStatsMessagesTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpStatsMessagesTransmitted.setStatus(_A)
_WccpStatsMessagesDropped_Type=Counter32
_WccpStatsMessagesDropped_Object=MibTableColumn
wccpStatsMessagesDropped=_WccpStatsMessagesDropped_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8,1,1,4),_WccpStatsMessagesDropped_Type())
wccpStatsMessagesDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpStatsMessagesDropped.setStatus(_A)
_WccpStatsPacketsRedir_Type=Counter32
_WccpStatsPacketsRedir_Object=MibTableColumn
wccpStatsPacketsRedir=_WccpStatsPacketsRedir_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8,1,1,5),_WccpStatsPacketsRedir_Type())
wccpStatsPacketsRedir.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpStatsPacketsRedir.setStatus(_A)
_WccpStatsPacketsLowRedir_Type=Counter32
_WccpStatsPacketsLowRedir_Object=MibTableColumn
wccpStatsPacketsLowRedir=_WccpStatsPacketsLowRedir_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8,1,1,6),_WccpStatsPacketsLowRedir_Type())
wccpStatsPacketsLowRedir.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpStatsPacketsLowRedir.setStatus(_A)
_WccpStatsPacketsDeniedRedir_Type=Counter32
_WccpStatsPacketsDeniedRedir_Object=MibTableColumn
wccpStatsPacketsDeniedRedir=_WccpStatsPacketsDeniedRedir_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8,1,1,7),_WccpStatsPacketsDeniedRedir_Type())
wccpStatsPacketsDeniedRedir.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpStatsPacketsDeniedRedir.setStatus(_A)
_WccpStatsAuthFailures_Type=Counter32
_WccpStatsAuthFailures_Object=MibTableColumn
wccpStatsAuthFailures=_WccpStatsAuthFailures_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8,1,1,8),_WccpStatsAuthFailures_Type())
wccpStatsAuthFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpStatsAuthFailures.setStatus(_A)
class _WccpStatsReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('reset',2)))
_WccpStatsReset_Type.__name__=_E
_WccpStatsReset_Object=MibTableColumn
wccpStatsReset=_WccpStatsReset_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,8,1,1,9),_WccpStatsReset_Type())
wccpStatsReset.setMaxAccess(_J)
if mibBuilder.loadTexts:wccpStatsReset.setStatus(_A)
_WccpTrapsObj_ObjectIdentity=ObjectIdentity
wccpTrapsObj=_WccpTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,9))
_WccpTrapInfoServiceId_Type=Integer32
_WccpTrapInfoServiceId_Object=MibScalar
wccpTrapInfoServiceId=_WccpTrapInfoServiceId_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,9,1),_WccpTrapInfoServiceId_Type())
wccpTrapInfoServiceId.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpTrapInfoServiceId.setStatus(_A)
_WccpTrapInfoOperStatus_Type=WccpOperState
_WccpTrapInfoOperStatus_Object=MibScalar
wccpTrapInfoOperStatus=_WccpTrapInfoOperStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,9,2),_WccpTrapInfoOperStatus_Type())
wccpTrapInfoOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpTrapInfoOperStatus.setStatus(_A)
_WccpTrapInfoWebCacheIpAddr_Type=IpAddress
_WccpTrapInfoWebCacheIpAddr_Object=MibScalar
wccpTrapInfoWebCacheIpAddr=_WccpTrapInfoWebCacheIpAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,9,3),_WccpTrapInfoWebCacheIpAddr_Type())
wccpTrapInfoWebCacheIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpTrapInfoWebCacheIpAddr.setStatus(_A)
class _WccpTrapInfoEntityGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('wccp',1),('service',2),('webcache',3)))
_WccpTrapInfoEntityGroup_Type.__name__=_E
_WccpTrapInfoEntityGroup_Object=MibScalar
wccpTrapInfoEntityGroup=_WccpTrapInfoEntityGroup_Object((1,3,6,1,4,1,6486,800,1,2,1,38,1,1,9,4),_WccpTrapInfoEntityGroup_Type())
wccpTrapInfoEntityGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:wccpTrapInfoEntityGroup.setStatus(_A)
_AlcatelIND1WCCPMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1WCCPMIBConformance=_AlcatelIND1WCCPMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,2))
if mibBuilder.loadTexts:alcatelIND1WCCPMIBConformance.setStatus(_A)
_AlcatelIND1WCCPMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1WCCPMIBGroups=_AlcatelIND1WCCPMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,1))
if mibBuilder.loadTexts:alcatelIND1WCCPMIBGroups.setStatus(_A)
_AlcatelIND1WCCPMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1WCCPMIBCompliances=_AlcatelIND1WCCPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,2))
if mibBuilder.loadTexts:alcatelIND1WCCPMIBCompliances.setStatus(_A)
wccpFeatureGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,1,1))
wccpFeatureGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:wccpFeatureGroup.setStatus(_A)
wccpServiceGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,1,2))
wccpServiceGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:wccpServiceGroup.setStatus(_A)
wccpWebCacheGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,1,3))
wccpWebCacheGroup.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:wccpWebCacheGroup.setStatus(_A)
wccpRouterGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,1,4))
wccpRouterGroup.setObjects((_B,_A7))
if mibBuilder.loadTexts:wccpRouterGroup.setStatus(_A)
wccpRestrictVlanGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,1,5))
wccpRestrictVlanGroup.setObjects((_B,_A8))
if mibBuilder.loadTexts:wccpRestrictVlanGroup.setStatus(_A)
wccpRestrictWebCacheGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,1,6))
wccpRestrictWebCacheGroup.setObjects((_B,_A9))
if mibBuilder.loadTexts:wccpRestrictWebCacheGroup.setStatus(_A)
wccpRestrictPortGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,1,7))
wccpRestrictPortGroup.setObjects((_B,_AA))
if mibBuilder.loadTexts:wccpRestrictPortGroup.setStatus(_A)
wccpStatisticsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,1,8))
wccpStatisticsGroup.setObjects(*((_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:wccpStatisticsGroup.setStatus(_A)
wccpOperStatusGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,1,10))
wccpOperStatusGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:wccpOperStatusGroup.setStatus(_A)
wccpTrapOperStatus=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,38,1,0,1))
wccpTrapOperStatus.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:wccpTrapOperStatus.setStatus(_A)
wccpTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,1,9))
wccpTrapsGroup.setObjects((_B,_AJ))
if mibBuilder.loadTexts:wccpTrapsGroup.setStatus(_A)
alcatelIND1WCCPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,38,1,2,2,1))
alcatelIND1WCCPMIBCompliance.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS)))
if mibBuilder.loadTexts:alcatelIND1WCCPMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'WccpServiceType':WccpServiceType,'WccpVersion':WccpVersion,'WccpServiceProtocolType':WccpServiceProtocolType,'WccpServiceMessageType':WccpServiceMessageType,'WccpServicePortType':WccpServicePortType,'WccpOperState':WccpOperState,'alcatelIND1WCCPMIB':alcatelIND1WCCPMIB,'alcatelIND1WCCPMIBNotifications':alcatelIND1WCCPMIBNotifications,_AJ:wccpTrapOperStatus,'alcatelIND1WCCPMIBObjects':alcatelIND1WCCPMIBObjects,'wccpFeature':wccpFeature,_j:wccpAdminEnabled,_k:wccpServiceCount,_m:wccpGlobalStatsReset,_l:wccpGlobalStatsMessageInvalid,'wccpServices':wccpServices,'wccpServiceTable':wccpServiceTable,'wccpServiceTableEntry':wccpServiceTableEntry,_Q:wccpServiceId,_n:wccpServiceProtocol,_o:wccpServiceMessageType,_p:wccpServicePortType,_q:wccpServiceAdminEnabled,_r:wccpServicePassword,_s:wccpServiceType,_t:wccpServiceVersion,_u:wccpServiceWebCacheCount,_v:wccpServiceReceiveId,_w:wccpServiceChangeNumber,_x:wccpServicePrecedence,_y:wccpServiceRowStatus,'wccpServicePortTable':wccpServicePortTable,'wccpServicePortTableEntry':wccpServicePortTableEntry,_R:wccpServicePortServiceId,_S:wccpServicePortPortId,_z:wccpServicePortPortNum,'wccpWebCaches':wccpWebCaches,'wccpWebCacheTable':wccpWebCacheTable,'wccpWebCacheTableEntry':wccpWebCacheTableEntry,_T:wccpWebCacheServiceId,_U:wccpWebCacheIpAddressType,_V:wccpWebCacheIpAddress,_A0:wccpWebCacheProtoVersion,_A1:wccpWebCacheReceiveId,_A2:wccpWebCacheChangeNum,_A3:wccpWebCacheNumberOfRouters,_A4:wccpWebCacheNumberOfWebCaches,_A6:wccpWebCacheState,_A5:wccpWebCacheConnectTime,'wccpRouters':wccpRouters,'wccpRouterTable':wccpRouterTable,'wccpRouterTableEntry':wccpRouterTableEntry,_W:wccpRouterServiceId,_X:wccpRouterIpAddressType,_Y:wccpRouterIpAddress,_A7:wccpRouterProtoVersion,'wccpRestrictVlan':wccpRestrictVlan,'wccpRestrictVlanTable':wccpRestrictVlanTable,'wccpRestrictVlanTableEntry':wccpRestrictVlanTableEntry,_Z:wccpRestrictVlanServiceId,_a:wccpRestrictVlanVlanId,_A8:wccpRestrictVlanRowStatus,'wccpRestrictWebCache':wccpRestrictWebCache,'wccpRestrictWebCacheTable':wccpRestrictWebCacheTable,'wccpRestrictWebCacheTableEntry':wccpRestrictWebCacheTableEntry,_b:wccpRestrictWebCacheServiceId,_c:wccpRestrictWebCacheIpAddressType,_d:wccpRestrictWebCacheIpAddress,_e:wccpRestrictWebCacheIpMaskAddressType,_f:wccpRestrictWebCacheIpMask,_A9:wccpRestrictWebCacheRowStatus,'wccpRestrictPort':wccpRestrictPort,'wccpRestrictPortTable':wccpRestrictPortTable,'wccpRestrictPortTableEntry':wccpRestrictPortTableEntry,_g:wccpRestrictPortServiceId,_h:wccpRestrictPortIndex,_AA:wccpRestrictPortRowStatus,'wccpStatistics':wccpStatistics,'wccpStatisticsTable':wccpStatisticsTable,'wccpStatisticsTableEntry':wccpStatisticsTableEntry,_i:wccpStatsServiceId,_AB:wccpStatsMessagesReceived,_AC:wccpStatsMessagesTransmitted,_AD:wccpStatsMessagesDropped,_AE:wccpStatsPacketsRedir,_AF:wccpStatsPacketsLowRedir,_AG:wccpStatsPacketsDeniedRedir,_AH:wccpStatsAuthFailures,_AI:wccpStatsReset,'wccpTrapsObj':wccpTrapsObj,_M:wccpTrapInfoServiceId,_L:wccpTrapInfoOperStatus,_N:wccpTrapInfoWebCacheIpAddr,_K:wccpTrapInfoEntityGroup,'alcatelIND1WCCPMIBConformance':alcatelIND1WCCPMIBConformance,'alcatelIND1WCCPMIBGroups':alcatelIND1WCCPMIBGroups,_AK:wccpFeatureGroup,_AL:wccpServiceGroup,_AM:wccpWebCacheGroup,_AN:wccpRouterGroup,_AO:wccpRestrictVlanGroup,_AP:wccpRestrictWebCacheGroup,_AQ:wccpRestrictPortGroup,_AR:wccpStatisticsGroup,_AS:wccpTrapsGroup,'wccpOperStatusGroup':wccpOperStatusGroup,'alcatelIND1WCCPMIBCompliances':alcatelIND1WCCPMIBCompliances,'alcatelIND1WCCPMIBCompliance':alcatelIND1WCCPMIBCompliance})