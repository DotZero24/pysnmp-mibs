_AC='tmnxRpkiNotificationGroup'
_AB='tmnxRpkiOriginValidGroup'
_AA='tmnxRpkiStaleTimerExpiry'
_A9='tmnxRpkiNotifySession'
_A8='vRtrRpkiSessInstanceLastChange'
_A7='vRtrRpkiSessInstanceSessionId'
_A6='vRtrRpkiSessInstanceSerialId'
_A5='vRtrOrigValASRouteValidity'
_A4='vRtrOrigValStaticASValidity'
_A3='vRtrOrigValStaticRowStatus'
_A2='vRtrRpkiSessInstanceActIpv6Rec'
_A1='vRtrRpkiSessInstanceActIpv4Rec'
_A0='vRtrRpkiSessInstanceUptime'
_z='vRtrRpkiSessInstanceSessionFlaps'
_y='vRtrRpkiSessInstanceSessionState'
_x='vRtrRpkiSessInstanceStaleRoutTim'
_w='vRtrRpkiSessInstanceAdminState'
_v='vRtrRpkiSessInstanceRefreshTime'
_u='vRtrRpkiSessInstancePort'
_t='vRtrRpkiSessLocalAddress'
_s='vRtrRpkiSessLocalAddressType'
_r='vRtrRpkiSessInstanceHoldTime'
_q='vRtrRpkiSessInstanceDescription'
_p='vRtrRpkiSessInstanceConnectRetry'
_o='vRtrRpkiSessInstanceRowStatus'
_n='vRtrOrigValRouteRpkiAddress'
_m='vRtrOrigValRouteRpkiAddrType'
_l='vRtrOrigValRouteRpkiVrId'
_k='vRtrOrigValRouteType'
_j='vRtrOrigValRouteAS4Byte'
_i='vRtrOrigValRouteMaxPrefixLen'
_h='vRtrOrigValRouteMinPrefixLen'
_g='vRtrOrigValRouteIpPrefix'
_f='vRtrOrigValRouteIpPrefixType'
_e='vRtrOrigValStaticAS4Byte'
_d='vRtrOrigValStaticMaxPrefixLen'
_c='vRtrOrigValStaticMinPrefixLen'
_b='vRtrOrigValStaticIpPrefix'
_a='vRtrOrigValStaticIpPrefixType'
_Z='vRtrRpkiSessInstanceAddress'
_Y='vRtrRpkiSessInstanceAddressType'
_X='TmnxAdminState'
_W='BgpHoldTime'
_V='BgpConnectRetryTime'
_U='TruthValue'
_T='DisplayString'
_S='InetAutonomousSystemNumber'
_R='InetAddressType'
_Q='tmnxRpkiTrapStatus'
_P='tmnxRpkiErrorType'
_O='tmnxRpkiPeerAddrType'
_N='tmnxRpkiPeerAddr'
_M='accessible-for-notify'
_L='seconds'
_K='vRtrID'
_J='TIMETRA-VRTR-MIB'
_I='Unsigned32'
_H='Integer32'
_G='InetAddressPrefixLength'
_F='InetAddress'
_E='read-only'
_D='read-create'
_C='not-accessible'
_B='TIMETRA-RPKI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,_G,_R,_S)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_T,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_U)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
BgpConnectRetryTime,BgpHoldTime,TmnxAdminState,TmnxVRtrID=mibBuilder.importSymbols('TIMETRA-TC-MIB',_V,_W,_X,'TmnxVRtrID')
vRtrID,=mibBuilder.importSymbols(_J,_K)
timetraRpkiOriginValidMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,96))
if mibBuilder.loadTexts:timetraRpkiOriginValidMIBModule.setRevisions(('2014-03-10 00:00',))
_TmnxRpkiConformance_ObjectIdentity=ObjectIdentity
tmnxRpkiConformance=_TmnxRpkiConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,96))
_TmnxRpkiCompliances_ObjectIdentity=ObjectIdentity
tmnxRpkiCompliances=_TmnxRpkiCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,96,1))
_TmnxRpkiGroups_ObjectIdentity=ObjectIdentity
tmnxRpkiGroups=_TmnxRpkiGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,96,2))
_TmnxRpkiObjs_ObjectIdentity=ObjectIdentity
tmnxRpkiObjs=_TmnxRpkiObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,96))
_VRtrRpkiSessInstanceTable_Object=MibTable
vRtrRpkiSessInstanceTable=_VRtrRpkiSessInstanceTable_Object((1,3,6,1,4,1,6527,3,1,2,96,1))
if mibBuilder.loadTexts:vRtrRpkiSessInstanceTable.setStatus(_A)
_VRtrRpkiSessInstanceEntry_Object=MibTableRow
vRtrRpkiSessInstanceEntry=_VRtrRpkiSessInstanceEntry_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1))
vRtrRpkiSessInstanceEntry.setIndexNames((0,_J,_K),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:vRtrRpkiSessInstanceEntry.setStatus(_A)
_VRtrRpkiSessInstanceAddressType_Type=InetAddressType
_VRtrRpkiSessInstanceAddressType_Object=MibTableColumn
vRtrRpkiSessInstanceAddressType=_VRtrRpkiSessInstanceAddressType_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,1),_VRtrRpkiSessInstanceAddressType_Type())
vRtrRpkiSessInstanceAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceAddressType.setStatus(_A)
class _VRtrRpkiSessInstanceAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_VRtrRpkiSessInstanceAddress_Type.__name__=_F
_VRtrRpkiSessInstanceAddress_Object=MibTableColumn
vRtrRpkiSessInstanceAddress=_VRtrRpkiSessInstanceAddress_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,2),_VRtrRpkiSessInstanceAddress_Type())
vRtrRpkiSessInstanceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceAddress.setStatus(_A)
_VRtrRpkiSessInstanceRowStatus_Type=RowStatus
_VRtrRpkiSessInstanceRowStatus_Object=MibTableColumn
vRtrRpkiSessInstanceRowStatus=_VRtrRpkiSessInstanceRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,3),_VRtrRpkiSessInstanceRowStatus_Type())
vRtrRpkiSessInstanceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceRowStatus.setStatus(_A)
class _VRtrRpkiSessInstanceConnectRetry_Type(BgpConnectRetryTime):defaultValue=120
_VRtrRpkiSessInstanceConnectRetry_Type.__name__=_V
_VRtrRpkiSessInstanceConnectRetry_Object=MibTableColumn
vRtrRpkiSessInstanceConnectRetry=_VRtrRpkiSessInstanceConnectRetry_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,4),_VRtrRpkiSessInstanceConnectRetry_Type())
vRtrRpkiSessInstanceConnectRetry.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceConnectRetry.setStatus(_A)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceConnectRetry.setUnits(_L)
class _VRtrRpkiSessInstanceDescription_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_VRtrRpkiSessInstanceDescription_Type.__name__=_T
_VRtrRpkiSessInstanceDescription_Object=MibTableColumn
vRtrRpkiSessInstanceDescription=_VRtrRpkiSessInstanceDescription_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,5),_VRtrRpkiSessInstanceDescription_Type())
vRtrRpkiSessInstanceDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceDescription.setStatus(_A)
class _VRtrRpkiSessInstanceHoldTime_Type(BgpHoldTime):defaultValue=600
_VRtrRpkiSessInstanceHoldTime_Type.__name__=_W
_VRtrRpkiSessInstanceHoldTime_Object=MibTableColumn
vRtrRpkiSessInstanceHoldTime=_VRtrRpkiSessInstanceHoldTime_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,6),_VRtrRpkiSessInstanceHoldTime_Type())
vRtrRpkiSessInstanceHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceHoldTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceHoldTime.setUnits(_L)
class _VRtrRpkiSessLocalAddressType_Type(InetAddressType):defaultValue=0
_VRtrRpkiSessLocalAddressType_Type.__name__=_R
_VRtrRpkiSessLocalAddressType_Object=MibTableColumn
vRtrRpkiSessLocalAddressType=_VRtrRpkiSessLocalAddressType_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,7),_VRtrRpkiSessLocalAddressType_Type())
vRtrRpkiSessLocalAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrRpkiSessLocalAddressType.setStatus(_A)
class _VRtrRpkiSessLocalAddress_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrRpkiSessLocalAddress_Type.__name__=_F
_VRtrRpkiSessLocalAddress_Object=MibTableColumn
vRtrRpkiSessLocalAddress=_VRtrRpkiSessLocalAddress_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,8),_VRtrRpkiSessLocalAddress_Type())
vRtrRpkiSessLocalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrRpkiSessLocalAddress.setStatus(_A)
class _VRtrRpkiSessInstancePort_Type(Unsigned32):defaultValue=323;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VRtrRpkiSessInstancePort_Type.__name__=_I
_VRtrRpkiSessInstancePort_Object=MibTableColumn
vRtrRpkiSessInstancePort=_VRtrRpkiSessInstancePort_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,9),_VRtrRpkiSessInstancePort_Type())
vRtrRpkiSessInstancePort.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrRpkiSessInstancePort.setStatus(_A)
class _VRtrRpkiSessInstanceRefreshTime_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,32767))
_VRtrRpkiSessInstanceRefreshTime_Type.__name__=_I
_VRtrRpkiSessInstanceRefreshTime_Object=MibTableColumn
vRtrRpkiSessInstanceRefreshTime=_VRtrRpkiSessInstanceRefreshTime_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,10),_VRtrRpkiSessInstanceRefreshTime_Type())
vRtrRpkiSessInstanceRefreshTime.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceRefreshTime.setStatus(_A)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceRefreshTime.setUnits(_L)
class _VRtrRpkiSessInstanceAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrRpkiSessInstanceAdminState_Type.__name__=_X
_VRtrRpkiSessInstanceAdminState_Object=MibTableColumn
vRtrRpkiSessInstanceAdminState=_VRtrRpkiSessInstanceAdminState_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,11),_VRtrRpkiSessInstanceAdminState_Type())
vRtrRpkiSessInstanceAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceAdminState.setStatus(_A)
class _VRtrRpkiSessInstanceStaleRoutTim_Type(Unsigned32):defaultValue=3600;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_VRtrRpkiSessInstanceStaleRoutTim_Type.__name__=_I
_VRtrRpkiSessInstanceStaleRoutTim_Object=MibTableColumn
vRtrRpkiSessInstanceStaleRoutTim=_VRtrRpkiSessInstanceStaleRoutTim_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,12),_VRtrRpkiSessInstanceStaleRoutTim_Type())
vRtrRpkiSessInstanceStaleRoutTim.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceStaleRoutTim.setStatus(_A)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceStaleRoutTim.setUnits(_L)
class _VRtrRpkiSessInstanceSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('idle',0),('connect',1),('established',2),('cleanup',3)))
_VRtrRpkiSessInstanceSessionState_Type.__name__=_H
_VRtrRpkiSessInstanceSessionState_Object=MibTableColumn
vRtrRpkiSessInstanceSessionState=_VRtrRpkiSessInstanceSessionState_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,13),_VRtrRpkiSessInstanceSessionState_Type())
vRtrRpkiSessInstanceSessionState.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceSessionState.setStatus(_A)
_VRtrRpkiSessInstanceSessionFlaps_Type=Unsigned32
_VRtrRpkiSessInstanceSessionFlaps_Object=MibTableColumn
vRtrRpkiSessInstanceSessionFlaps=_VRtrRpkiSessInstanceSessionFlaps_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,14),_VRtrRpkiSessInstanceSessionFlaps_Type())
vRtrRpkiSessInstanceSessionFlaps.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceSessionFlaps.setStatus(_A)
_VRtrRpkiSessInstanceUptime_Type=TimeStamp
_VRtrRpkiSessInstanceUptime_Object=MibTableColumn
vRtrRpkiSessInstanceUptime=_VRtrRpkiSessInstanceUptime_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,15),_VRtrRpkiSessInstanceUptime_Type())
vRtrRpkiSessInstanceUptime.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceUptime.setStatus(_A)
_VRtrRpkiSessInstanceActIpv4Rec_Type=Unsigned32
_VRtrRpkiSessInstanceActIpv4Rec_Object=MibTableColumn
vRtrRpkiSessInstanceActIpv4Rec=_VRtrRpkiSessInstanceActIpv4Rec_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,16),_VRtrRpkiSessInstanceActIpv4Rec_Type())
vRtrRpkiSessInstanceActIpv4Rec.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceActIpv4Rec.setStatus(_A)
_VRtrRpkiSessInstanceActIpv6Rec_Type=Unsigned32
_VRtrRpkiSessInstanceActIpv6Rec_Object=MibTableColumn
vRtrRpkiSessInstanceActIpv6Rec=_VRtrRpkiSessInstanceActIpv6Rec_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,17),_VRtrRpkiSessInstanceActIpv6Rec_Type())
vRtrRpkiSessInstanceActIpv6Rec.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceActIpv6Rec.setStatus(_A)
_VRtrRpkiSessInstanceSerialId_Type=Unsigned32
_VRtrRpkiSessInstanceSerialId_Object=MibTableColumn
vRtrRpkiSessInstanceSerialId=_VRtrRpkiSessInstanceSerialId_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,18),_VRtrRpkiSessInstanceSerialId_Type())
vRtrRpkiSessInstanceSerialId.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceSerialId.setStatus(_A)
_VRtrRpkiSessInstanceSessionId_Type=Unsigned32
_VRtrRpkiSessInstanceSessionId_Object=MibTableColumn
vRtrRpkiSessInstanceSessionId=_VRtrRpkiSessInstanceSessionId_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,19),_VRtrRpkiSessInstanceSessionId_Type())
vRtrRpkiSessInstanceSessionId.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceSessionId.setStatus(_A)
_VRtrRpkiSessInstanceLastChange_Type=TimeStamp
_VRtrRpkiSessInstanceLastChange_Object=MibTableColumn
vRtrRpkiSessInstanceLastChange=_VRtrRpkiSessInstanceLastChange_Object((1,3,6,1,4,1,6527,3,1,2,96,1,1,20),_VRtrRpkiSessInstanceLastChange_Type())
vRtrRpkiSessInstanceLastChange.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrRpkiSessInstanceLastChange.setStatus(_A)
_VRtrOriginValStaticTable_Object=MibTable
vRtrOriginValStaticTable=_VRtrOriginValStaticTable_Object((1,3,6,1,4,1,6527,3,1,2,96,2))
if mibBuilder.loadTexts:vRtrOriginValStaticTable.setStatus(_A)
_VRtrOriginValStaticEntry_Object=MibTableRow
vRtrOriginValStaticEntry=_VRtrOriginValStaticEntry_Object((1,3,6,1,4,1,6527,3,1,2,96,2,1))
vRtrOriginValStaticEntry.setIndexNames((0,_J,_K),(0,_B,_a),(0,_B,_b),(0,_B,_c),(0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:vRtrOriginValStaticEntry.setStatus(_A)
_VRtrOrigValStaticIpPrefixType_Type=InetAddressType
_VRtrOrigValStaticIpPrefixType_Object=MibTableColumn
vRtrOrigValStaticIpPrefixType=_VRtrOrigValStaticIpPrefixType_Object((1,3,6,1,4,1,6527,3,1,2,96,2,1,1),_VRtrOrigValStaticIpPrefixType_Type())
vRtrOrigValStaticIpPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValStaticIpPrefixType.setStatus(_A)
class _VRtrOrigValStaticIpPrefix_Type(InetAddress):defaultHexValue='';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrOrigValStaticIpPrefix_Type.__name__=_F
_VRtrOrigValStaticIpPrefix_Object=MibTableColumn
vRtrOrigValStaticIpPrefix=_VRtrOrigValStaticIpPrefix_Object((1,3,6,1,4,1,6527,3,1,2,96,2,1,2),_VRtrOrigValStaticIpPrefix_Type())
vRtrOrigValStaticIpPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValStaticIpPrefix.setStatus(_A)
class _VRtrOrigValStaticMinPrefixLen_Type(InetAddressPrefixLength):defaultValue=0;subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_VRtrOrigValStaticMinPrefixLen_Type.__name__=_G
_VRtrOrigValStaticMinPrefixLen_Object=MibTableColumn
vRtrOrigValStaticMinPrefixLen=_VRtrOrigValStaticMinPrefixLen_Object((1,3,6,1,4,1,6527,3,1,2,96,2,1,3),_VRtrOrigValStaticMinPrefixLen_Type())
vRtrOrigValStaticMinPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValStaticMinPrefixLen.setStatus(_A)
class _VRtrOrigValStaticMaxPrefixLen_Type(InetAddressPrefixLength):defaultValue=0;subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_VRtrOrigValStaticMaxPrefixLen_Type.__name__=_G
_VRtrOrigValStaticMaxPrefixLen_Object=MibTableColumn
vRtrOrigValStaticMaxPrefixLen=_VRtrOrigValStaticMaxPrefixLen_Object((1,3,6,1,4,1,6527,3,1,2,96,2,1,4),_VRtrOrigValStaticMaxPrefixLen_Type())
vRtrOrigValStaticMaxPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValStaticMaxPrefixLen.setStatus(_A)
class _VRtrOrigValStaticAS4Byte_Type(InetAutonomousSystemNumber):defaultValue=0
_VRtrOrigValStaticAS4Byte_Type.__name__=_S
_VRtrOrigValStaticAS4Byte_Object=MibTableColumn
vRtrOrigValStaticAS4Byte=_VRtrOrigValStaticAS4Byte_Object((1,3,6,1,4,1,6527,3,1,2,96,2,1,5),_VRtrOrigValStaticAS4Byte_Type())
vRtrOrigValStaticAS4Byte.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValStaticAS4Byte.setStatus(_A)
_VRtrOrigValStaticRowStatus_Type=RowStatus
_VRtrOrigValStaticRowStatus_Object=MibTableColumn
vRtrOrigValStaticRowStatus=_VRtrOrigValStaticRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,96,2,1,6),_VRtrOrigValStaticRowStatus_Type())
vRtrOrigValStaticRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrOrigValStaticRowStatus.setStatus(_A)
class _VRtrOrigValStaticASValidity_Type(TruthValue):defaultValue=1
_VRtrOrigValStaticASValidity_Type.__name__=_U
_VRtrOrigValStaticASValidity_Object=MibTableColumn
vRtrOrigValStaticASValidity=_VRtrOrigValStaticASValidity_Object((1,3,6,1,4,1,6527,3,1,2,96,2,1,7),_VRtrOrigValStaticASValidity_Type())
vRtrOrigValStaticASValidity.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrOrigValStaticASValidity.setStatus(_A)
_VRtrOriginValRouteTable_Object=MibTable
vRtrOriginValRouteTable=_VRtrOriginValRouteTable_Object((1,3,6,1,4,1,6527,3,1,2,96,3))
if mibBuilder.loadTexts:vRtrOriginValRouteTable.setStatus(_A)
_VRtrOriginValRouteEntry_Object=MibTableRow
vRtrOriginValRouteEntry=_VRtrOriginValRouteEntry_Object((1,3,6,1,4,1,6527,3,1,2,96,3,1))
vRtrOriginValRouteEntry.setIndexNames((0,_J,_K),(0,_B,_f),(0,_B,_g),(0,_B,_h),(0,_B,_i),(0,_B,_j),(0,_B,_k),(0,_B,_l),(0,_B,_m),(0,_B,_n))
if mibBuilder.loadTexts:vRtrOriginValRouteEntry.setStatus(_A)
_VRtrOrigValRouteIpPrefixType_Type=InetAddressType
_VRtrOrigValRouteIpPrefixType_Object=MibTableColumn
vRtrOrigValRouteIpPrefixType=_VRtrOrigValRouteIpPrefixType_Object((1,3,6,1,4,1,6527,3,1,2,96,3,1,1),_VRtrOrigValRouteIpPrefixType_Type())
vRtrOrigValRouteIpPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValRouteIpPrefixType.setStatus(_A)
class _VRtrOrigValRouteIpPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrOrigValRouteIpPrefix_Type.__name__=_F
_VRtrOrigValRouteIpPrefix_Object=MibTableColumn
vRtrOrigValRouteIpPrefix=_VRtrOrigValRouteIpPrefix_Object((1,3,6,1,4,1,6527,3,1,2,96,3,1,2),_VRtrOrigValRouteIpPrefix_Type())
vRtrOrigValRouteIpPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValRouteIpPrefix.setStatus(_A)
class _VRtrOrigValRouteMinPrefixLen_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_VRtrOrigValRouteMinPrefixLen_Type.__name__=_G
_VRtrOrigValRouteMinPrefixLen_Object=MibTableColumn
vRtrOrigValRouteMinPrefixLen=_VRtrOrigValRouteMinPrefixLen_Object((1,3,6,1,4,1,6527,3,1,2,96,3,1,3),_VRtrOrigValRouteMinPrefixLen_Type())
vRtrOrigValRouteMinPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValRouteMinPrefixLen.setStatus(_A)
class _VRtrOrigValRouteMaxPrefixLen_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_VRtrOrigValRouteMaxPrefixLen_Type.__name__=_G
_VRtrOrigValRouteMaxPrefixLen_Object=MibTableColumn
vRtrOrigValRouteMaxPrefixLen=_VRtrOrigValRouteMaxPrefixLen_Object((1,3,6,1,4,1,6527,3,1,2,96,3,1,4),_VRtrOrigValRouteMaxPrefixLen_Type())
vRtrOrigValRouteMaxPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValRouteMaxPrefixLen.setStatus(_A)
_VRtrOrigValRouteAS4Byte_Type=InetAutonomousSystemNumber
_VRtrOrigValRouteAS4Byte_Object=MibTableColumn
vRtrOrigValRouteAS4Byte=_VRtrOrigValRouteAS4Byte_Object((1,3,6,1,4,1,6527,3,1,2,96,3,1,5),_VRtrOrigValRouteAS4Byte_Type())
vRtrOrigValRouteAS4Byte.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValRouteAS4Byte.setStatus(_A)
class _VRtrOrigValRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_VRtrOrigValRouteType_Type.__name__=_H
_VRtrOrigValRouteType_Object=MibTableColumn
vRtrOrigValRouteType=_VRtrOrigValRouteType_Object((1,3,6,1,4,1,6527,3,1,2,96,3,1,6),_VRtrOrigValRouteType_Type())
vRtrOrigValRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValRouteType.setStatus(_A)
_VRtrOrigValRouteRpkiVrId_Type=TmnxVRtrID
_VRtrOrigValRouteRpkiVrId_Object=MibTableColumn
vRtrOrigValRouteRpkiVrId=_VRtrOrigValRouteRpkiVrId_Object((1,3,6,1,4,1,6527,3,1,2,96,3,1,7),_VRtrOrigValRouteRpkiVrId_Type())
vRtrOrigValRouteRpkiVrId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValRouteRpkiVrId.setStatus(_A)
_VRtrOrigValRouteRpkiAddrType_Type=InetAddressType
_VRtrOrigValRouteRpkiAddrType_Object=MibTableColumn
vRtrOrigValRouteRpkiAddrType=_VRtrOrigValRouteRpkiAddrType_Object((1,3,6,1,4,1,6527,3,1,2,96,3,1,8),_VRtrOrigValRouteRpkiAddrType_Type())
vRtrOrigValRouteRpkiAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValRouteRpkiAddrType.setStatus(_A)
class _VRtrOrigValRouteRpkiAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_VRtrOrigValRouteRpkiAddress_Type.__name__=_F
_VRtrOrigValRouteRpkiAddress_Object=MibTableColumn
vRtrOrigValRouteRpkiAddress=_VRtrOrigValRouteRpkiAddress_Object((1,3,6,1,4,1,6527,3,1,2,96,3,1,9),_VRtrOrigValRouteRpkiAddress_Type())
vRtrOrigValRouteRpkiAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrOrigValRouteRpkiAddress.setStatus(_A)
_VRtrOrigValASRouteValidity_Type=TruthValue
_VRtrOrigValASRouteValidity_Object=MibTableColumn
vRtrOrigValASRouteValidity=_VRtrOrigValASRouteValidity_Object((1,3,6,1,4,1,6527,3,1,2,96,3,1,10),_VRtrOrigValASRouteValidity_Type())
vRtrOrigValASRouteValidity.setMaxAccess(_E)
if mibBuilder.loadTexts:vRtrOrigValASRouteValidity.setStatus(_A)
_TmnxRpkiNotificationObjs_ObjectIdentity=ObjectIdentity
tmnxRpkiNotificationObjs=_TmnxRpkiNotificationObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,96,4))
_TmnxRpkiPeerAddrType_Type=InetAddressType
_TmnxRpkiPeerAddrType_Object=MibScalar
tmnxRpkiPeerAddrType=_TmnxRpkiPeerAddrType_Object((1,3,6,1,4,1,6527,3,1,2,96,4,1),_TmnxRpkiPeerAddrType_Type())
tmnxRpkiPeerAddrType.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxRpkiPeerAddrType.setStatus(_A)
_TmnxRpkiPeerAddr_Type=InetAddress
_TmnxRpkiPeerAddr_Object=MibScalar
tmnxRpkiPeerAddr=_TmnxRpkiPeerAddr_Object((1,3,6,1,4,1,6527,3,1,2,96,4,2),_TmnxRpkiPeerAddr_Type())
tmnxRpkiPeerAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxRpkiPeerAddr.setStatus(_A)
class _TmnxRpkiErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('holdTimerExpired',1),('tcpConnectionFailure',2),('sessionIdMismatch',3),('fatalErrorCode',4),('sessionEstablished',5),('adminDown',6)))
_TmnxRpkiErrorType_Type.__name__=_H
_TmnxRpkiErrorType_Object=MibScalar
tmnxRpkiErrorType=_TmnxRpkiErrorType_Object((1,3,6,1,4,1,6527,3,1,2,96,4,3),_TmnxRpkiErrorType_Type())
tmnxRpkiErrorType.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxRpkiErrorType.setStatus(_A)
class _TmnxRpkiTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_TmnxRpkiTrapStatus_Type.__name__=_H
_TmnxRpkiTrapStatus_Object=MibScalar
tmnxRpkiTrapStatus=_TmnxRpkiTrapStatus_Object((1,3,6,1,4,1,6527,3,1,2,96,4,4),_TmnxRpkiTrapStatus_Type())
tmnxRpkiTrapStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxRpkiTrapStatus.setStatus(_A)
_TmnxRpkiNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxRpkiNotifyPrefix=_TmnxRpkiNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,96))
_TmnxRpkiNotifications_ObjectIdentity=ObjectIdentity
tmnxRpkiNotifications=_TmnxRpkiNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,96,0))
tmnxRpkiOriginValidGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,96,2,1))
tmnxRpkiOriginValidGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:tmnxRpkiOriginValidGroup.setStatus(_A)
tmnxRpkiNotifyObjsGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,96,2,2))
tmnxRpkiNotifyObjsGroup.setObjects(*((_B,_P),(_B,_N),(_B,_O),(_B,_Q)))
if mibBuilder.loadTexts:tmnxRpkiNotifyObjsGroup.setStatus(_A)
tmnxRpkiNotifySession=NotificationType((1,3,6,1,4,1,6527,3,1,3,96,0,1))
tmnxRpkiNotifySession.setObjects(*((_B,_O),(_B,_N),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:tmnxRpkiNotifySession.setStatus(_A)
tmnxRpkiStaleTimerExpiry=NotificationType((1,3,6,1,4,1,6527,3,1,3,96,0,2))
tmnxRpkiStaleTimerExpiry.setObjects(*((_B,_O),(_B,_N)))
if mibBuilder.loadTexts:tmnxRpkiStaleTimerExpiry.setStatus(_A)
tmnxRpkiNotificationGroup=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,96,2,3))
tmnxRpkiNotificationGroup.setObjects(*((_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:tmnxRpkiNotificationGroup.setStatus(_A)
tmnxOriginValidV12v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,96,1,1))
tmnxOriginValidV12v0Compliance.setObjects(*((_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:tmnxOriginValidV12v0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'timetraRpkiOriginValidMIBModule':timetraRpkiOriginValidMIBModule,'tmnxRpkiConformance':tmnxRpkiConformance,'tmnxRpkiCompliances':tmnxRpkiCompliances,'tmnxOriginValidV12v0Compliance':tmnxOriginValidV12v0Compliance,'tmnxRpkiGroups':tmnxRpkiGroups,_AB:tmnxRpkiOriginValidGroup,'tmnxRpkiNotifyObjsGroup':tmnxRpkiNotifyObjsGroup,_AC:tmnxRpkiNotificationGroup,'tmnxRpkiObjs':tmnxRpkiObjs,'vRtrRpkiSessInstanceTable':vRtrRpkiSessInstanceTable,'vRtrRpkiSessInstanceEntry':vRtrRpkiSessInstanceEntry,_Y:vRtrRpkiSessInstanceAddressType,_Z:vRtrRpkiSessInstanceAddress,_o:vRtrRpkiSessInstanceRowStatus,_p:vRtrRpkiSessInstanceConnectRetry,_q:vRtrRpkiSessInstanceDescription,_r:vRtrRpkiSessInstanceHoldTime,_s:vRtrRpkiSessLocalAddressType,_t:vRtrRpkiSessLocalAddress,_u:vRtrRpkiSessInstancePort,_v:vRtrRpkiSessInstanceRefreshTime,_w:vRtrRpkiSessInstanceAdminState,_x:vRtrRpkiSessInstanceStaleRoutTim,_y:vRtrRpkiSessInstanceSessionState,_z:vRtrRpkiSessInstanceSessionFlaps,_A0:vRtrRpkiSessInstanceUptime,_A1:vRtrRpkiSessInstanceActIpv4Rec,_A2:vRtrRpkiSessInstanceActIpv6Rec,_A6:vRtrRpkiSessInstanceSerialId,_A7:vRtrRpkiSessInstanceSessionId,_A8:vRtrRpkiSessInstanceLastChange,'vRtrOriginValStaticTable':vRtrOriginValStaticTable,'vRtrOriginValStaticEntry':vRtrOriginValStaticEntry,_a:vRtrOrigValStaticIpPrefixType,_b:vRtrOrigValStaticIpPrefix,_c:vRtrOrigValStaticMinPrefixLen,_d:vRtrOrigValStaticMaxPrefixLen,_e:vRtrOrigValStaticAS4Byte,_A3:vRtrOrigValStaticRowStatus,_A4:vRtrOrigValStaticASValidity,'vRtrOriginValRouteTable':vRtrOriginValRouteTable,'vRtrOriginValRouteEntry':vRtrOriginValRouteEntry,_f:vRtrOrigValRouteIpPrefixType,_g:vRtrOrigValRouteIpPrefix,_h:vRtrOrigValRouteMinPrefixLen,_i:vRtrOrigValRouteMaxPrefixLen,_j:vRtrOrigValRouteAS4Byte,_k:vRtrOrigValRouteType,_l:vRtrOrigValRouteRpkiVrId,_m:vRtrOrigValRouteRpkiAddrType,_n:vRtrOrigValRouteRpkiAddress,_A5:vRtrOrigValASRouteValidity,'tmnxRpkiNotificationObjs':tmnxRpkiNotificationObjs,_O:tmnxRpkiPeerAddrType,_N:tmnxRpkiPeerAddr,_P:tmnxRpkiErrorType,_Q:tmnxRpkiTrapStatus,'tmnxRpkiNotifyPrefix':tmnxRpkiNotifyPrefix,'tmnxRpkiNotifications':tmnxRpkiNotifications,_A9:tmnxRpkiNotifySession,_AA:tmnxRpkiStaleTimerExpiry})