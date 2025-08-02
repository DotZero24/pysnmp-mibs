_u='bsLldpXAvayaPortConfigEntry'
_t='bsLldpXAvayaRemFaIsidVlanAsgnsVlan'
_s='bsLldpXAvayaRemFaIsidVlanAsgnsIsid'
_r='bsLldpXAvayaRemPoeConsLevelValue'
_q='rejected'
_p='active'
_o='pending'
_n='bsLldpXAvayaLocFaIsidVlanAsgnsVlan'
_m='bsLldpXAvayaLocFaIsidVlanAsgnsIsid'
_l='bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex'
_k='faClientOnaSpbOIp'
_j='faClientOnaSdn'
_i='faClientSrvrEndpt'
_h='faClientVirtSwitch'
_g='faClientSecurityDev'
_f='faClientIpVideo'
_e='faClientIpCamera'
_d='faClientIpPhone'
_c='faClientRouter'
_b='faClientSwitch'
_a='faClientWapType2'
_Z='faClientWapType1'
_Y='faProxyNoAuth'
_X='faServerNoAuth'
_W='faProxy'
_V='faServer'
_U='read-create'
_T='bsLldpXAvayaLocFileServerNum'
_S='bsLldpXAvayaLocCallServerNum'
_R='untagged'
_Q='tagged'
_P='lldpLocPortNum'
_O='Bits'
_N='OctetString'
_M='other'
_L='disabled'
_K='enabled'
_J='read-write'
_I='not-accessible'
_H='lldpRemTimeMark'
_G='lldpRemLocalPortNum'
_F='lldpRemIndex'
_E='BAY-STACK-LLDP-X-AVAYA-MIB'
_D='Integer32'
_C='read-only'
_B='LLDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
lldpLocPortNum,lldpPortConfigEntry,lldpRemIndex,lldpRemLocalPortNum,lldpRemTimeMark=mibBuilder.importSymbols(_B,_P,'lldpPortConfigEntry',_F,_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_O,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackLldpXAvayaMib=ModuleIdentity((1,3,6,1,4,1,45,5,39))
if mibBuilder.loadTexts:bayStackLldpXAvayaMib.setRevisions(('2015-02-24 00:00','2014-10-01 00:00','2014-09-10 00:00','2014-02-25 00:00','2013-07-05 00:00','2010-10-29 00:00'))
_BsLldpXAvayaNotifications_ObjectIdentity=ObjectIdentity
bsLldpXAvayaNotifications=_BsLldpXAvayaNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,39,0))
_BsLldpXAvayaObjects_ObjectIdentity=ObjectIdentity
bsLldpXAvayaObjects=_BsLldpXAvayaObjects_ObjectIdentity((1,3,6,1,4,1,45,5,39,1))
_BsLldpXAvayaConfig_ObjectIdentity=ObjectIdentity
bsLldpXAvayaConfig=_BsLldpXAvayaConfig_ObjectIdentity((1,3,6,1,4,1,45,5,39,1,1))
_BsLldpXAvayaPortConfigTable_Object=MibTable
bsLldpXAvayaPortConfigTable=_BsLldpXAvayaPortConfigTable_Object((1,3,6,1,4,1,45,5,39,1,1,1))
if mibBuilder.loadTexts:bsLldpXAvayaPortConfigTable.setStatus(_A)
_BsLldpXAvayaPortConfigEntry_Object=MibTableRow
bsLldpXAvayaPortConfigEntry=_BsLldpXAvayaPortConfigEntry_Object((1,3,6,1,4,1,45,5,39,1,1,1,1))
if mibBuilder.loadTexts:bsLldpXAvayaPortConfigEntry.setStatus(_A)
class _BsLldpXAvayaPortConfigTLVsTxEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('poeConservationLevel',0),('callServer',1),('fileServer',2),('framingTlv',3),('faElementType',4),('faIsidVlanAsgns',5)))
_BsLldpXAvayaPortConfigTLVsTxEnable_Type.__name__=_O
_BsLldpXAvayaPortConfigTLVsTxEnable_Object=MibTableColumn
bsLldpXAvayaPortConfigTLVsTxEnable=_BsLldpXAvayaPortConfigTLVsTxEnable_Object((1,3,6,1,4,1,45,5,39,1,1,1,1,1),_BsLldpXAvayaPortConfigTLVsTxEnable_Type())
bsLldpXAvayaPortConfigTLVsTxEnable.setMaxAccess(_J)
if mibBuilder.loadTexts:bsLldpXAvayaPortConfigTLVsTxEnable.setStatus(_A)
_BsLldpXAvayaLocalData_ObjectIdentity=ObjectIdentity
bsLldpXAvayaLocalData=_BsLldpXAvayaLocalData_ObjectIdentity((1,3,6,1,4,1,45,5,39,1,2))
_BsLldpXAvayaLocPortTable_Object=MibTable
bsLldpXAvayaLocPortTable=_BsLldpXAvayaLocPortTable_Object((1,3,6,1,4,1,45,5,39,1,2,1))
if mibBuilder.loadTexts:bsLldpXAvayaLocPortTable.setStatus(_A)
_BsLldpXAvayaLocPortEntry_Object=MibTableRow
bsLldpXAvayaLocPortEntry=_BsLldpXAvayaLocPortEntry_Object((1,3,6,1,4,1,45,5,39,1,2,1,1))
bsLldpXAvayaLocPortEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:bsLldpXAvayaLocPortEntry.setStatus(_A)
class _BsLldpXAvayaLocPortPoeConsLevelRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BsLldpXAvayaLocPortPoeConsLevelRequest_Type.__name__=_D
_BsLldpXAvayaLocPortPoeConsLevelRequest_Object=MibTableColumn
bsLldpXAvayaLocPortPoeConsLevelRequest=_BsLldpXAvayaLocPortPoeConsLevelRequest_Object((1,3,6,1,4,1,45,5,39,1,2,1,1,1),_BsLldpXAvayaLocPortPoeConsLevelRequest_Type())
bsLldpXAvayaLocPortPoeConsLevelRequest.setMaxAccess(_J)
if mibBuilder.loadTexts:bsLldpXAvayaLocPortPoeConsLevelRequest.setStatus(_A)
class _BsLldpXAvayaLocPortDot1QFramingRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),('auto',3)))
_BsLldpXAvayaLocPortDot1QFramingRequest_Type.__name__=_D
_BsLldpXAvayaLocPortDot1QFramingRequest_Object=MibTableColumn
bsLldpXAvayaLocPortDot1QFramingRequest=_BsLldpXAvayaLocPortDot1QFramingRequest_Object((1,3,6,1,4,1,45,5,39,1,2,1,1,2),_BsLldpXAvayaLocPortDot1QFramingRequest_Type())
bsLldpXAvayaLocPortDot1QFramingRequest.setMaxAccess(_J)
if mibBuilder.loadTexts:bsLldpXAvayaLocPortDot1QFramingRequest.setStatus(_A)
_BsLldpXAvayaLocCallServerTable_Object=MibTable
bsLldpXAvayaLocCallServerTable=_BsLldpXAvayaLocCallServerTable_Object((1,3,6,1,4,1,45,5,39,1,2,2))
if mibBuilder.loadTexts:bsLldpXAvayaLocCallServerTable.setStatus(_A)
_BsLldpXAvayaLocCallServerEntry_Object=MibTableRow
bsLldpXAvayaLocCallServerEntry=_BsLldpXAvayaLocCallServerEntry_Object((1,3,6,1,4,1,45,5,39,1,2,2,1))
bsLldpXAvayaLocCallServerEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:bsLldpXAvayaLocCallServerEntry.setStatus(_A)
class _BsLldpXAvayaLocCallServerNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BsLldpXAvayaLocCallServerNum_Type.__name__=_D
_BsLldpXAvayaLocCallServerNum_Object=MibTableColumn
bsLldpXAvayaLocCallServerNum=_BsLldpXAvayaLocCallServerNum_Object((1,3,6,1,4,1,45,5,39,1,2,2,1,1),_BsLldpXAvayaLocCallServerNum_Type())
bsLldpXAvayaLocCallServerNum.setMaxAccess(_I)
if mibBuilder.loadTexts:bsLldpXAvayaLocCallServerNum.setStatus(_A)
_BsLldpXAvayaLocCallServerAddressType_Type=InetAddressType
_BsLldpXAvayaLocCallServerAddressType_Object=MibTableColumn
bsLldpXAvayaLocCallServerAddressType=_BsLldpXAvayaLocCallServerAddressType_Object((1,3,6,1,4,1,45,5,39,1,2,2,1,2),_BsLldpXAvayaLocCallServerAddressType_Type())
bsLldpXAvayaLocCallServerAddressType.setMaxAccess(_J)
if mibBuilder.loadTexts:bsLldpXAvayaLocCallServerAddressType.setStatus(_A)
_BsLldpXAvayaLocCallServerAddress_Type=InetAddress
_BsLldpXAvayaLocCallServerAddress_Object=MibTableColumn
bsLldpXAvayaLocCallServerAddress=_BsLldpXAvayaLocCallServerAddress_Object((1,3,6,1,4,1,45,5,39,1,2,2,1,3),_BsLldpXAvayaLocCallServerAddress_Type())
bsLldpXAvayaLocCallServerAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:bsLldpXAvayaLocCallServerAddress.setStatus(_A)
_BsLldpXAvayaLocFileServerTable_Object=MibTable
bsLldpXAvayaLocFileServerTable=_BsLldpXAvayaLocFileServerTable_Object((1,3,6,1,4,1,45,5,39,1,2,3))
if mibBuilder.loadTexts:bsLldpXAvayaLocFileServerTable.setStatus(_A)
_BsLldpXAvayaLocFileServerEntry_Object=MibTableRow
bsLldpXAvayaLocFileServerEntry=_BsLldpXAvayaLocFileServerEntry_Object((1,3,6,1,4,1,45,5,39,1,2,3,1))
bsLldpXAvayaLocFileServerEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:bsLldpXAvayaLocFileServerEntry.setStatus(_A)
class _BsLldpXAvayaLocFileServerNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BsLldpXAvayaLocFileServerNum_Type.__name__=_D
_BsLldpXAvayaLocFileServerNum_Object=MibTableColumn
bsLldpXAvayaLocFileServerNum=_BsLldpXAvayaLocFileServerNum_Object((1,3,6,1,4,1,45,5,39,1,2,3,1,1),_BsLldpXAvayaLocFileServerNum_Type())
bsLldpXAvayaLocFileServerNum.setMaxAccess(_I)
if mibBuilder.loadTexts:bsLldpXAvayaLocFileServerNum.setStatus(_A)
_BsLldpXAvayaLocFileServerAddressType_Type=InetAddressType
_BsLldpXAvayaLocFileServerAddressType_Object=MibTableColumn
bsLldpXAvayaLocFileServerAddressType=_BsLldpXAvayaLocFileServerAddressType_Object((1,3,6,1,4,1,45,5,39,1,2,3,1,2),_BsLldpXAvayaLocFileServerAddressType_Type())
bsLldpXAvayaLocFileServerAddressType.setMaxAccess(_U)
if mibBuilder.loadTexts:bsLldpXAvayaLocFileServerAddressType.setStatus(_A)
_BsLldpXAvayaLocFileServerAddress_Type=InetAddress
_BsLldpXAvayaLocFileServerAddress_Object=MibTableColumn
bsLldpXAvayaLocFileServerAddress=_BsLldpXAvayaLocFileServerAddress_Object((1,3,6,1,4,1,45,5,39,1,2,3,1,3),_BsLldpXAvayaLocFileServerAddress_Type())
bsLldpXAvayaLocFileServerAddress.setMaxAccess(_U)
if mibBuilder.loadTexts:bsLldpXAvayaLocFileServerAddress.setStatus(_A)
class _BsLldpXAvayaLocFaService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_BsLldpXAvayaLocFaService_Type.__name__=_D
_BsLldpXAvayaLocFaService_Object=MibScalar
bsLldpXAvayaLocFaService=_BsLldpXAvayaLocFaService_Object((1,3,6,1,4,1,45,5,39,1,2,4),_BsLldpXAvayaLocFaService_Type())
bsLldpXAvayaLocFaService.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaLocFaService.setStatus(_A)
class _BsLldpXAvayaLocFaElementType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_M,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7),(_b,8),(_c,9),(_d,10),(_e,11),(_f,12),(_g,13),(_h,14),(_i,15),(_j,16),(_k,17)))
_BsLldpXAvayaLocFaElementType_Type.__name__=_D
_BsLldpXAvayaLocFaElementType_Object=MibScalar
bsLldpXAvayaLocFaElementType=_BsLldpXAvayaLocFaElementType_Object((1,3,6,1,4,1,45,5,39,1,2,5),_BsLldpXAvayaLocFaElementType_Type())
bsLldpXAvayaLocFaElementType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaLocFaElementType.setStatus(_A)
class _BsLldpXAvayaLocFaElementMgmtVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_BsLldpXAvayaLocFaElementMgmtVlan_Type.__name__=_D
_BsLldpXAvayaLocFaElementMgmtVlan_Object=MibScalar
bsLldpXAvayaLocFaElementMgmtVlan=_BsLldpXAvayaLocFaElementMgmtVlan_Object((1,3,6,1,4,1,45,5,39,1,2,6),_BsLldpXAvayaLocFaElementMgmtVlan_Type())
bsLldpXAvayaLocFaElementMgmtVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaLocFaElementMgmtVlan.setStatus(_A)
class _BsLldpXAvayaLocFaElementPrimaryServerId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BsLldpXAvayaLocFaElementPrimaryServerId_Type.__name__=_N
_BsLldpXAvayaLocFaElementPrimaryServerId_Object=MibScalar
bsLldpXAvayaLocFaElementPrimaryServerId=_BsLldpXAvayaLocFaElementPrimaryServerId_Object((1,3,6,1,4,1,45,5,39,1,2,7),_BsLldpXAvayaLocFaElementPrimaryServerId_Type())
bsLldpXAvayaLocFaElementPrimaryServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaLocFaElementPrimaryServerId.setStatus(_A)
_BsLldpXAvayaLocFaIsidVlanAsgnsTable_Object=MibTable
bsLldpXAvayaLocFaIsidVlanAsgnsTable=_BsLldpXAvayaLocFaIsidVlanAsgnsTable_Object((1,3,6,1,4,1,45,5,39,1,2,8))
if mibBuilder.loadTexts:bsLldpXAvayaLocFaIsidVlanAsgnsTable.setStatus(_A)
_BsLldpXAvayaLocFaIsidVlanAsgnsEntry_Object=MibTableRow
bsLldpXAvayaLocFaIsidVlanAsgnsEntry=_BsLldpXAvayaLocFaIsidVlanAsgnsEntry_Object((1,3,6,1,4,1,45,5,39,1,2,8,1))
bsLldpXAvayaLocFaIsidVlanAsgnsEntry.setIndexNames((0,_E,_l),(0,_E,_m),(0,_E,_n))
if mibBuilder.loadTexts:bsLldpXAvayaLocFaIsidVlanAsgnsEntry.setStatus(_A)
class _BsLldpXAvayaLocFaIsidVlanAsgnsIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BsLldpXAvayaLocFaIsidVlanAsgnsIfIndex_Type.__name__=_D
_BsLldpXAvayaLocFaIsidVlanAsgnsIfIndex_Object=MibTableColumn
bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex=_BsLldpXAvayaLocFaIsidVlanAsgnsIfIndex_Object((1,3,6,1,4,1,45,5,39,1,2,8,1,1),_BsLldpXAvayaLocFaIsidVlanAsgnsIfIndex_Type())
bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex.setStatus(_A)
class _BsLldpXAvayaLocFaIsidVlanAsgnsIsid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_BsLldpXAvayaLocFaIsidVlanAsgnsIsid_Type.__name__=_D
_BsLldpXAvayaLocFaIsidVlanAsgnsIsid_Object=MibTableColumn
bsLldpXAvayaLocFaIsidVlanAsgnsIsid=_BsLldpXAvayaLocFaIsidVlanAsgnsIsid_Object((1,3,6,1,4,1,45,5,39,1,2,8,1,2),_BsLldpXAvayaLocFaIsidVlanAsgnsIsid_Type())
bsLldpXAvayaLocFaIsidVlanAsgnsIsid.setMaxAccess(_I)
if mibBuilder.loadTexts:bsLldpXAvayaLocFaIsidVlanAsgnsIsid.setStatus(_A)
class _BsLldpXAvayaLocFaIsidVlanAsgnsVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_BsLldpXAvayaLocFaIsidVlanAsgnsVlan_Type.__name__=_D
_BsLldpXAvayaLocFaIsidVlanAsgnsVlan_Object=MibTableColumn
bsLldpXAvayaLocFaIsidVlanAsgnsVlan=_BsLldpXAvayaLocFaIsidVlanAsgnsVlan_Object((1,3,6,1,4,1,45,5,39,1,2,8,1,3),_BsLldpXAvayaLocFaIsidVlanAsgnsVlan_Type())
bsLldpXAvayaLocFaIsidVlanAsgnsVlan.setMaxAccess(_I)
if mibBuilder.loadTexts:bsLldpXAvayaLocFaIsidVlanAsgnsVlan.setStatus(_A)
class _BsLldpXAvayaLocFaIsidVlanAsgnsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_o,2),(_p,3),(_q,4)))
_BsLldpXAvayaLocFaIsidVlanAsgnsStatus_Type.__name__=_D
_BsLldpXAvayaLocFaIsidVlanAsgnsStatus_Object=MibTableColumn
bsLldpXAvayaLocFaIsidVlanAsgnsStatus=_BsLldpXAvayaLocFaIsidVlanAsgnsStatus_Object((1,3,6,1,4,1,45,5,39,1,2,8,1,4),_BsLldpXAvayaLocFaIsidVlanAsgnsStatus_Type())
bsLldpXAvayaLocFaIsidVlanAsgnsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaLocFaIsidVlanAsgnsStatus.setStatus(_A)
class _BsLldpXAvayaLocFaZeroTouchService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_BsLldpXAvayaLocFaZeroTouchService_Type.__name__=_D
_BsLldpXAvayaLocFaZeroTouchService_Object=MibScalar
bsLldpXAvayaLocFaZeroTouchService=_BsLldpXAvayaLocFaZeroTouchService_Object((1,3,6,1,4,1,45,5,39,1,2,9),_BsLldpXAvayaLocFaZeroTouchService_Type())
bsLldpXAvayaLocFaZeroTouchService.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaLocFaZeroTouchService.setStatus(_A)
class _BsLldpXAvayaLocFaMsgAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_BsLldpXAvayaLocFaMsgAuthStatus_Type.__name__=_D
_BsLldpXAvayaLocFaMsgAuthStatus_Object=MibScalar
bsLldpXAvayaLocFaMsgAuthStatus=_BsLldpXAvayaLocFaMsgAuthStatus_Object((1,3,6,1,4,1,45,5,39,1,2,10),_BsLldpXAvayaLocFaMsgAuthStatus_Type())
bsLldpXAvayaLocFaMsgAuthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaLocFaMsgAuthStatus.setStatus(_A)
class _BsLldpXAvayaLocFaClientProxyService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_BsLldpXAvayaLocFaClientProxyService_Type.__name__=_D
_BsLldpXAvayaLocFaClientProxyService_Object=MibScalar
bsLldpXAvayaLocFaClientProxyService=_BsLldpXAvayaLocFaClientProxyService_Object((1,3,6,1,4,1,45,5,39,1,2,11),_BsLldpXAvayaLocFaClientProxyService_Type())
bsLldpXAvayaLocFaClientProxyService.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaLocFaClientProxyService.setStatus(_A)
_BsLldpXAvayaRemoteData_ObjectIdentity=ObjectIdentity
bsLldpXAvayaRemoteData=_BsLldpXAvayaRemoteData_ObjectIdentity((1,3,6,1,4,1,45,5,39,1,3))
_BsLldpXAvayaRemTable_Object=MibTable
bsLldpXAvayaRemTable=_BsLldpXAvayaRemTable_Object((1,3,6,1,4,1,45,5,39,1,3,1))
if mibBuilder.loadTexts:bsLldpXAvayaRemTable.setStatus(_A)
_BsLldpXAvayaRemEntry_Object=MibTableRow
bsLldpXAvayaRemEntry=_BsLldpXAvayaRemEntry_Object((1,3,6,1,4,1,45,5,39,1,3,1,1))
bsLldpXAvayaRemEntry.setIndexNames((0,_B,_H),(0,_B,_G),(0,_B,_F))
if mibBuilder.loadTexts:bsLldpXAvayaRemEntry.setStatus(_A)
class _BsLldpXAvayaRemCurrentConsLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,243))
_BsLldpXAvayaRemCurrentConsLevel_Type.__name__=_D
_BsLldpXAvayaRemCurrentConsLevel_Object=MibTableColumn
bsLldpXAvayaRemCurrentConsLevel=_BsLldpXAvayaRemCurrentConsLevel_Object((1,3,6,1,4,1,45,5,39,1,3,1,1,1),_BsLldpXAvayaRemCurrentConsLevel_Type())
bsLldpXAvayaRemCurrentConsLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemCurrentConsLevel.setStatus(_A)
_BsLldpXAvayaRemTypicalPower_Type=Integer32
_BsLldpXAvayaRemTypicalPower_Object=MibTableColumn
bsLldpXAvayaRemTypicalPower=_BsLldpXAvayaRemTypicalPower_Object((1,3,6,1,4,1,45,5,39,1,3,1,1,2),_BsLldpXAvayaRemTypicalPower_Type())
bsLldpXAvayaRemTypicalPower.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemTypicalPower.setStatus(_A)
_BsLldpXAvayaRemMaxPower_Type=Integer32
_BsLldpXAvayaRemMaxPower_Object=MibTableColumn
bsLldpXAvayaRemMaxPower=_BsLldpXAvayaRemMaxPower_Object((1,3,6,1,4,1,45,5,39,1,3,1,1,3),_BsLldpXAvayaRemMaxPower_Type())
bsLldpXAvayaRemMaxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemMaxPower.setStatus(_A)
_BsLldpXAvayaRemCallServerTable_Object=MibTable
bsLldpXAvayaRemCallServerTable=_BsLldpXAvayaRemCallServerTable_Object((1,3,6,1,4,1,45,5,39,1,3,2))
if mibBuilder.loadTexts:bsLldpXAvayaRemCallServerTable.setStatus(_A)
_BsLldpXAvayaRemCallServerEntry_Object=MibTableRow
bsLldpXAvayaRemCallServerEntry=_BsLldpXAvayaRemCallServerEntry_Object((1,3,6,1,4,1,45,5,39,1,3,2,1))
bsLldpXAvayaRemCallServerEntry.setIndexNames((0,_B,_H),(0,_B,_G),(0,_B,_F))
if mibBuilder.loadTexts:bsLldpXAvayaRemCallServerEntry.setStatus(_A)
_BsLldpXAvayaRemPortCallServerAddressType_Type=InetAddressType
_BsLldpXAvayaRemPortCallServerAddressType_Object=MibTableColumn
bsLldpXAvayaRemPortCallServerAddressType=_BsLldpXAvayaRemPortCallServerAddressType_Object((1,3,6,1,4,1,45,5,39,1,3,2,1,1),_BsLldpXAvayaRemPortCallServerAddressType_Type())
bsLldpXAvayaRemPortCallServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemPortCallServerAddressType.setStatus(_A)
_BsLldpXAvayaRemPortCallServerAddress_Type=InetAddress
_BsLldpXAvayaRemPortCallServerAddress_Object=MibTableColumn
bsLldpXAvayaRemPortCallServerAddress=_BsLldpXAvayaRemPortCallServerAddress_Object((1,3,6,1,4,1,45,5,39,1,3,2,1,2),_BsLldpXAvayaRemPortCallServerAddress_Type())
bsLldpXAvayaRemPortCallServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemPortCallServerAddress.setStatus(_A)
_BsLldpXAvayaRemFileServerTable_Object=MibTable
bsLldpXAvayaRemFileServerTable=_BsLldpXAvayaRemFileServerTable_Object((1,3,6,1,4,1,45,5,39,1,3,3))
if mibBuilder.loadTexts:bsLldpXAvayaRemFileServerTable.setStatus(_A)
_BsLldpXAvayaRemFileServerEntry_Object=MibTableRow
bsLldpXAvayaRemFileServerEntry=_BsLldpXAvayaRemFileServerEntry_Object((1,3,6,1,4,1,45,5,39,1,3,3,1))
bsLldpXAvayaRemFileServerEntry.setIndexNames((0,_B,_H),(0,_B,_G),(0,_B,_F))
if mibBuilder.loadTexts:bsLldpXAvayaRemFileServerEntry.setStatus(_A)
_BsLldpXAvayaRemPortFileServerAddressType_Type=InetAddressType
_BsLldpXAvayaRemPortFileServerAddressType_Object=MibTableColumn
bsLldpXAvayaRemPortFileServerAddressType=_BsLldpXAvayaRemPortFileServerAddressType_Object((1,3,6,1,4,1,45,5,39,1,3,3,1,1),_BsLldpXAvayaRemPortFileServerAddressType_Type())
bsLldpXAvayaRemPortFileServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemPortFileServerAddressType.setStatus(_A)
_BsLldpXAvayaRemPortFileServerAddress_Type=InetAddress
_BsLldpXAvayaRemPortFileServerAddress_Object=MibTableColumn
bsLldpXAvayaRemPortFileServerAddress=_BsLldpXAvayaRemPortFileServerAddress_Object((1,3,6,1,4,1,45,5,39,1,3,3,1,2),_BsLldpXAvayaRemPortFileServerAddress_Type())
bsLldpXAvayaRemPortFileServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemPortFileServerAddress.setStatus(_A)
_BsLldpXAvayaRemPoeConsLevelTable_Object=MibTable
bsLldpXAvayaRemPoeConsLevelTable=_BsLldpXAvayaRemPoeConsLevelTable_Object((1,3,6,1,4,1,45,5,39,1,3,4))
if mibBuilder.loadTexts:bsLldpXAvayaRemPoeConsLevelTable.setStatus(_A)
_BsLldpXAvayaRemPoeConsLevelEntry_Object=MibTableRow
bsLldpXAvayaRemPoeConsLevelEntry=_BsLldpXAvayaRemPoeConsLevelEntry_Object((1,3,6,1,4,1,45,5,39,1,3,4,1))
bsLldpXAvayaRemPoeConsLevelEntry.setIndexNames((0,_B,_H),(0,_B,_G),(0,_B,_F),(0,_E,_r))
if mibBuilder.loadTexts:bsLldpXAvayaRemPoeConsLevelEntry.setStatus(_A)
class _BsLldpXAvayaRemPoeConsLevelValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_BsLldpXAvayaRemPoeConsLevelValue_Type.__name__=_D
_BsLldpXAvayaRemPoeConsLevelValue_Object=MibTableColumn
bsLldpXAvayaRemPoeConsLevelValue=_BsLldpXAvayaRemPoeConsLevelValue_Object((1,3,6,1,4,1,45,5,39,1,3,4,1,2),_BsLldpXAvayaRemPoeConsLevelValue_Type())
bsLldpXAvayaRemPoeConsLevelValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemPoeConsLevelValue.setStatus(_A)
_BsLldpXAvayaRemDot1QTable_Object=MibTable
bsLldpXAvayaRemDot1QTable=_BsLldpXAvayaRemDot1QTable_Object((1,3,6,1,4,1,45,5,39,1,3,5))
if mibBuilder.loadTexts:bsLldpXAvayaRemDot1QTable.setStatus(_A)
_BsLldpXAvayaRemDot1QEntry_Object=MibTableRow
bsLldpXAvayaRemDot1QEntry=_BsLldpXAvayaRemDot1QEntry_Object((1,3,6,1,4,1,45,5,39,1,3,5,1))
bsLldpXAvayaRemDot1QEntry.setIndexNames((0,_B,_H),(0,_B,_G),(0,_B,_F))
if mibBuilder.loadTexts:bsLldpXAvayaRemDot1QEntry.setStatus(_A)
class _BsLldpXAvayaRemDot1QFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),('auto',3)))
_BsLldpXAvayaRemDot1QFraming_Type.__name__=_D
_BsLldpXAvayaRemDot1QFraming_Object=MibTableColumn
bsLldpXAvayaRemDot1QFraming=_BsLldpXAvayaRemDot1QFraming_Object((1,3,6,1,4,1,45,5,39,1,3,5,1,1),_BsLldpXAvayaRemDot1QFraming_Type())
bsLldpXAvayaRemDot1QFraming.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemDot1QFraming.setStatus(_A)
_BsLldpXAvayaRemPhoneIpTable_Object=MibTable
bsLldpXAvayaRemPhoneIpTable=_BsLldpXAvayaRemPhoneIpTable_Object((1,3,6,1,4,1,45,5,39,1,3,6))
if mibBuilder.loadTexts:bsLldpXAvayaRemPhoneIpTable.setStatus(_A)
_BsLldpXAvayaRemPhoneIpEntry_Object=MibTableRow
bsLldpXAvayaRemPhoneIpEntry=_BsLldpXAvayaRemPhoneIpEntry_Object((1,3,6,1,4,1,45,5,39,1,3,6,1))
bsLldpXAvayaRemPhoneIpEntry.setIndexNames((0,_B,_H),(0,_B,_G),(0,_B,_F))
if mibBuilder.loadTexts:bsLldpXAvayaRemPhoneIpEntry.setStatus(_A)
_BsLldpXAvayaRemPortPhoneAddressType_Type=InetAddressType
_BsLldpXAvayaRemPortPhoneAddressType_Object=MibTableColumn
bsLldpXAvayaRemPortPhoneAddressType=_BsLldpXAvayaRemPortPhoneAddressType_Object((1,3,6,1,4,1,45,5,39,1,3,6,1,1),_BsLldpXAvayaRemPortPhoneAddressType_Type())
bsLldpXAvayaRemPortPhoneAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemPortPhoneAddressType.setStatus(_A)
_BsLldpXAvayaRemPortPhoneAddress_Type=InetAddress
_BsLldpXAvayaRemPortPhoneAddress_Object=MibTableColumn
bsLldpXAvayaRemPortPhoneAddress=_BsLldpXAvayaRemPortPhoneAddress_Object((1,3,6,1,4,1,45,5,39,1,3,6,1,2),_BsLldpXAvayaRemPortPhoneAddress_Type())
bsLldpXAvayaRemPortPhoneAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemPortPhoneAddress.setStatus(_A)
_BsLldpXAvayaRemPortPhoneAddressMask_Type=InetAddressPrefixLength
_BsLldpXAvayaRemPortPhoneAddressMask_Object=MibTableColumn
bsLldpXAvayaRemPortPhoneAddressMask=_BsLldpXAvayaRemPortPhoneAddressMask_Object((1,3,6,1,4,1,45,5,39,1,3,6,1,3),_BsLldpXAvayaRemPortPhoneAddressMask_Type())
bsLldpXAvayaRemPortPhoneAddressMask.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemPortPhoneAddressMask.setStatus(_A)
_BsLldpXAvayaRemPortPhoneGatewayAddress_Type=InetAddress
_BsLldpXAvayaRemPortPhoneGatewayAddress_Object=MibTableColumn
bsLldpXAvayaRemPortPhoneGatewayAddress=_BsLldpXAvayaRemPortPhoneGatewayAddress_Object((1,3,6,1,4,1,45,5,39,1,3,6,1,4),_BsLldpXAvayaRemPortPhoneGatewayAddress_Type())
bsLldpXAvayaRemPortPhoneGatewayAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemPortPhoneGatewayAddress.setStatus(_A)
_BsLldpXAvayaRemFaElementTable_Object=MibTable
bsLldpXAvayaRemFaElementTable=_BsLldpXAvayaRemFaElementTable_Object((1,3,6,1,4,1,45,5,39,1,3,7))
if mibBuilder.loadTexts:bsLldpXAvayaRemFaElementTable.setStatus(_A)
_BsLldpXAvayaRemFaElementEntry_Object=MibTableRow
bsLldpXAvayaRemFaElementEntry=_BsLldpXAvayaRemFaElementEntry_Object((1,3,6,1,4,1,45,5,39,1,3,7,1))
bsLldpXAvayaRemFaElementEntry.setIndexNames((0,_B,_H),(0,_B,_G),(0,_B,_F))
if mibBuilder.loadTexts:bsLldpXAvayaRemFaElementEntry.setStatus(_A)
class _BsLldpXAvayaRemFaElementType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_M,1),(_V,2),(_W,3),(_X,4),(_Y,5),(_Z,6),(_a,7),(_b,8),(_c,9),(_d,10),(_e,11),(_f,12),(_g,13),(_h,14),(_i,15),(_j,16),(_k,17)))
_BsLldpXAvayaRemFaElementType_Type.__name__=_D
_BsLldpXAvayaRemFaElementType_Object=MibTableColumn
bsLldpXAvayaRemFaElementType=_BsLldpXAvayaRemFaElementType_Object((1,3,6,1,4,1,45,5,39,1,3,7,1,1),_BsLldpXAvayaRemFaElementType_Type())
bsLldpXAvayaRemFaElementType.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemFaElementType.setStatus(_A)
class _BsLldpXAvayaRemFaElementMgmtVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_BsLldpXAvayaRemFaElementMgmtVlan_Type.__name__=_D
_BsLldpXAvayaRemFaElementMgmtVlan_Object=MibTableColumn
bsLldpXAvayaRemFaElementMgmtVlan=_BsLldpXAvayaRemFaElementMgmtVlan_Object((1,3,6,1,4,1,45,5,39,1,3,7,1,2),_BsLldpXAvayaRemFaElementMgmtVlan_Type())
bsLldpXAvayaRemFaElementMgmtVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemFaElementMgmtVlan.setStatus(_A)
class _BsLldpXAvayaRemFaElementId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BsLldpXAvayaRemFaElementId_Type.__name__=_N
_BsLldpXAvayaRemFaElementId_Object=MibTableColumn
bsLldpXAvayaRemFaElementId=_BsLldpXAvayaRemFaElementId_Object((1,3,6,1,4,1,45,5,39,1,3,7,1,3),_BsLldpXAvayaRemFaElementId_Type())
bsLldpXAvayaRemFaElementId.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemFaElementId.setStatus(_A)
class _BsLldpXAvayaRemFaElementState_Type(Bits):namedValues=NamedValues(*(('trafficTagged',0),('trafficTaggedAndUntagged',1),('provisionModeDisabled',2),('provisionModeSpbm',3),('provisionModeVlan',4)))
_BsLldpXAvayaRemFaElementState_Type.__name__=_O
_BsLldpXAvayaRemFaElementState_Object=MibTableColumn
bsLldpXAvayaRemFaElementState=_BsLldpXAvayaRemFaElementState_Object((1,3,6,1,4,1,45,5,39,1,3,7,1,4),_BsLldpXAvayaRemFaElementState_Type())
bsLldpXAvayaRemFaElementState.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemFaElementState.setStatus(_A)
_BsLldpXAvayaRemFaIsidVlanAsgnsTable_Object=MibTable
bsLldpXAvayaRemFaIsidVlanAsgnsTable=_BsLldpXAvayaRemFaIsidVlanAsgnsTable_Object((1,3,6,1,4,1,45,5,39,1,3,8))
if mibBuilder.loadTexts:bsLldpXAvayaRemFaIsidVlanAsgnsTable.setStatus(_A)
_BsLldpXAvayaRemFaIsidVlanAsgnsEntry_Object=MibTableRow
bsLldpXAvayaRemFaIsidVlanAsgnsEntry=_BsLldpXAvayaRemFaIsidVlanAsgnsEntry_Object((1,3,6,1,4,1,45,5,39,1,3,8,1))
bsLldpXAvayaRemFaIsidVlanAsgnsEntry.setIndexNames((0,_B,_H),(0,_B,_G),(0,_B,_F),(0,_E,_s),(0,_E,_t))
if mibBuilder.loadTexts:bsLldpXAvayaRemFaIsidVlanAsgnsEntry.setStatus(_A)
class _BsLldpXAvayaRemFaIsidVlanAsgnsIsid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_BsLldpXAvayaRemFaIsidVlanAsgnsIsid_Type.__name__=_D
_BsLldpXAvayaRemFaIsidVlanAsgnsIsid_Object=MibTableColumn
bsLldpXAvayaRemFaIsidVlanAsgnsIsid=_BsLldpXAvayaRemFaIsidVlanAsgnsIsid_Object((1,3,6,1,4,1,45,5,39,1,3,8,1,1),_BsLldpXAvayaRemFaIsidVlanAsgnsIsid_Type())
bsLldpXAvayaRemFaIsidVlanAsgnsIsid.setMaxAccess(_I)
if mibBuilder.loadTexts:bsLldpXAvayaRemFaIsidVlanAsgnsIsid.setStatus(_A)
class _BsLldpXAvayaRemFaIsidVlanAsgnsVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_BsLldpXAvayaRemFaIsidVlanAsgnsVlan_Type.__name__=_D
_BsLldpXAvayaRemFaIsidVlanAsgnsVlan_Object=MibTableColumn
bsLldpXAvayaRemFaIsidVlanAsgnsVlan=_BsLldpXAvayaRemFaIsidVlanAsgnsVlan_Object((1,3,6,1,4,1,45,5,39,1,3,8,1,2),_BsLldpXAvayaRemFaIsidVlanAsgnsVlan_Type())
bsLldpXAvayaRemFaIsidVlanAsgnsVlan.setMaxAccess(_I)
if mibBuilder.loadTexts:bsLldpXAvayaRemFaIsidVlanAsgnsVlan.setStatus(_A)
class _BsLldpXAvayaRemFaIsidVlanAsgnsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_o,2),(_p,3),(_q,4)))
_BsLldpXAvayaRemFaIsidVlanAsgnsStatus_Type.__name__=_D
_BsLldpXAvayaRemFaIsidVlanAsgnsStatus_Object=MibTableColumn
bsLldpXAvayaRemFaIsidVlanAsgnsStatus=_BsLldpXAvayaRemFaIsidVlanAsgnsStatus_Object((1,3,6,1,4,1,45,5,39,1,3,8,1,3),_BsLldpXAvayaRemFaIsidVlanAsgnsStatus_Type())
bsLldpXAvayaRemFaIsidVlanAsgnsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsLldpXAvayaRemFaIsidVlanAsgnsStatus.setStatus(_A)
lldpPortConfigEntry.registerAugmentions((_E,_u))
bsLldpXAvayaPortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'bayStackLldpXAvayaMib':bayStackLldpXAvayaMib,'bsLldpXAvayaNotifications':bsLldpXAvayaNotifications,'bsLldpXAvayaObjects':bsLldpXAvayaObjects,'bsLldpXAvayaConfig':bsLldpXAvayaConfig,'bsLldpXAvayaPortConfigTable':bsLldpXAvayaPortConfigTable,_u:bsLldpXAvayaPortConfigEntry,'bsLldpXAvayaPortConfigTLVsTxEnable':bsLldpXAvayaPortConfigTLVsTxEnable,'bsLldpXAvayaLocalData':bsLldpXAvayaLocalData,'bsLldpXAvayaLocPortTable':bsLldpXAvayaLocPortTable,'bsLldpXAvayaLocPortEntry':bsLldpXAvayaLocPortEntry,'bsLldpXAvayaLocPortPoeConsLevelRequest':bsLldpXAvayaLocPortPoeConsLevelRequest,'bsLldpXAvayaLocPortDot1QFramingRequest':bsLldpXAvayaLocPortDot1QFramingRequest,'bsLldpXAvayaLocCallServerTable':bsLldpXAvayaLocCallServerTable,'bsLldpXAvayaLocCallServerEntry':bsLldpXAvayaLocCallServerEntry,_S:bsLldpXAvayaLocCallServerNum,'bsLldpXAvayaLocCallServerAddressType':bsLldpXAvayaLocCallServerAddressType,'bsLldpXAvayaLocCallServerAddress':bsLldpXAvayaLocCallServerAddress,'bsLldpXAvayaLocFileServerTable':bsLldpXAvayaLocFileServerTable,'bsLldpXAvayaLocFileServerEntry':bsLldpXAvayaLocFileServerEntry,_T:bsLldpXAvayaLocFileServerNum,'bsLldpXAvayaLocFileServerAddressType':bsLldpXAvayaLocFileServerAddressType,'bsLldpXAvayaLocFileServerAddress':bsLldpXAvayaLocFileServerAddress,'bsLldpXAvayaLocFaService':bsLldpXAvayaLocFaService,'bsLldpXAvayaLocFaElementType':bsLldpXAvayaLocFaElementType,'bsLldpXAvayaLocFaElementMgmtVlan':bsLldpXAvayaLocFaElementMgmtVlan,'bsLldpXAvayaLocFaElementPrimaryServerId':bsLldpXAvayaLocFaElementPrimaryServerId,'bsLldpXAvayaLocFaIsidVlanAsgnsTable':bsLldpXAvayaLocFaIsidVlanAsgnsTable,'bsLldpXAvayaLocFaIsidVlanAsgnsEntry':bsLldpXAvayaLocFaIsidVlanAsgnsEntry,_l:bsLldpXAvayaLocFaIsidVlanAsgnsIfIndex,_m:bsLldpXAvayaLocFaIsidVlanAsgnsIsid,_n:bsLldpXAvayaLocFaIsidVlanAsgnsVlan,'bsLldpXAvayaLocFaIsidVlanAsgnsStatus':bsLldpXAvayaLocFaIsidVlanAsgnsStatus,'bsLldpXAvayaLocFaZeroTouchService':bsLldpXAvayaLocFaZeroTouchService,'bsLldpXAvayaLocFaMsgAuthStatus':bsLldpXAvayaLocFaMsgAuthStatus,'bsLldpXAvayaLocFaClientProxyService':bsLldpXAvayaLocFaClientProxyService,'bsLldpXAvayaRemoteData':bsLldpXAvayaRemoteData,'bsLldpXAvayaRemTable':bsLldpXAvayaRemTable,'bsLldpXAvayaRemEntry':bsLldpXAvayaRemEntry,'bsLldpXAvayaRemCurrentConsLevel':bsLldpXAvayaRemCurrentConsLevel,'bsLldpXAvayaRemTypicalPower':bsLldpXAvayaRemTypicalPower,'bsLldpXAvayaRemMaxPower':bsLldpXAvayaRemMaxPower,'bsLldpXAvayaRemCallServerTable':bsLldpXAvayaRemCallServerTable,'bsLldpXAvayaRemCallServerEntry':bsLldpXAvayaRemCallServerEntry,'bsLldpXAvayaRemPortCallServerAddressType':bsLldpXAvayaRemPortCallServerAddressType,'bsLldpXAvayaRemPortCallServerAddress':bsLldpXAvayaRemPortCallServerAddress,'bsLldpXAvayaRemFileServerTable':bsLldpXAvayaRemFileServerTable,'bsLldpXAvayaRemFileServerEntry':bsLldpXAvayaRemFileServerEntry,'bsLldpXAvayaRemPortFileServerAddressType':bsLldpXAvayaRemPortFileServerAddressType,'bsLldpXAvayaRemPortFileServerAddress':bsLldpXAvayaRemPortFileServerAddress,'bsLldpXAvayaRemPoeConsLevelTable':bsLldpXAvayaRemPoeConsLevelTable,'bsLldpXAvayaRemPoeConsLevelEntry':bsLldpXAvayaRemPoeConsLevelEntry,_r:bsLldpXAvayaRemPoeConsLevelValue,'bsLldpXAvayaRemDot1QTable':bsLldpXAvayaRemDot1QTable,'bsLldpXAvayaRemDot1QEntry':bsLldpXAvayaRemDot1QEntry,'bsLldpXAvayaRemDot1QFraming':bsLldpXAvayaRemDot1QFraming,'bsLldpXAvayaRemPhoneIpTable':bsLldpXAvayaRemPhoneIpTable,'bsLldpXAvayaRemPhoneIpEntry':bsLldpXAvayaRemPhoneIpEntry,'bsLldpXAvayaRemPortPhoneAddressType':bsLldpXAvayaRemPortPhoneAddressType,'bsLldpXAvayaRemPortPhoneAddress':bsLldpXAvayaRemPortPhoneAddress,'bsLldpXAvayaRemPortPhoneAddressMask':bsLldpXAvayaRemPortPhoneAddressMask,'bsLldpXAvayaRemPortPhoneGatewayAddress':bsLldpXAvayaRemPortPhoneGatewayAddress,'bsLldpXAvayaRemFaElementTable':bsLldpXAvayaRemFaElementTable,'bsLldpXAvayaRemFaElementEntry':bsLldpXAvayaRemFaElementEntry,'bsLldpXAvayaRemFaElementType':bsLldpXAvayaRemFaElementType,'bsLldpXAvayaRemFaElementMgmtVlan':bsLldpXAvayaRemFaElementMgmtVlan,'bsLldpXAvayaRemFaElementId':bsLldpXAvayaRemFaElementId,'bsLldpXAvayaRemFaElementState':bsLldpXAvayaRemFaElementState,'bsLldpXAvayaRemFaIsidVlanAsgnsTable':bsLldpXAvayaRemFaIsidVlanAsgnsTable,'bsLldpXAvayaRemFaIsidVlanAsgnsEntry':bsLldpXAvayaRemFaIsidVlanAsgnsEntry,_s:bsLldpXAvayaRemFaIsidVlanAsgnsIsid,_t:bsLldpXAvayaRemFaIsidVlanAsgnsVlan,'bsLldpXAvayaRemFaIsidVlanAsgnsStatus':bsLldpXAvayaRemFaIsidVlanAsgnsStatus})