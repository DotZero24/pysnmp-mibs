_AE='avFabricAttachDiscElemsMgmtOid'
_AD='avFabricAttachDiscElemsSysDescr'
_AC='avFabricAttachDiscElemsElementAuth'
_AB='accessible-for-notify'
_AA='avFabricAttachZeroTouchClientDetectMethod'
_A9='avFabricAttachZeroTouchClientDetectType'
_A8='avFabricAttachZeroTouchClientAttachType'
_A7='avFabricAttachZeroTouchClientType'
_A6='avFabricAttachStatsPortIndex'
_A5='avFabricAttachZeroTouchNsvType'
_A4='autoMgmtVlanFaClient'
_A3='autoClientAttach'
_A2='autoPvidModeFaClient'
_A1='autoTrustedModeFaClient'
_A0='radiusServer'
_z='autoPortModeMhmv'
_y='autoPortModeFaClient'
_x='ipAddrDhcp'
_w='failLocalNoAuthRemoteAuth'
_v='failLocalAuthRemoteNoAuth'
_u='failMismatchedKeys'
_t='successAuth'
_s='successNoAuth'
_r='notAuthenticated'
_q='authenticationFail'
_p='authenticationPass'
_o='avFabricAttachDiscElemsIfIndex'
_n='standard'
_m='avFabricAttachPortIfIndex'
_l='avFabricAttachIsidVlanAsgnsVlan'
_k='avFabricAttachIsidVlanAsgnsIsid'
_j='avFabricAttachIsidVlanAsgnsIfIndex'
_i='faClientOnaSpbOIp'
_h='faClientOnaSdn'
_g='faClientSrvrEndpt'
_f='faClientVirtSwitch'
_e='faClientSecurityDev'
_d='faClientIpVideo'
_c='faClientIpCamera'
_b='faClientIpPhone'
_a='faClientRouter'
_Z='faClientSwitch'
_Y='faClientWapType2'
_X='faClientWapType1'
_W='faProxyNoAuth'
_V='faServerNoAuth'
_U='2015-10-30 00:00'
_T='avFabricAttachDiscElemsElementId'
_S='avFabricAttachDiscElemsElementType'
_R='faServer'
_Q='TruthValue'
_P='DisplayString'
_O='none'
_N='faProxy'
_M='other'
_L='Bits'
_K='SnmpAdminString'
_J='OctetString'
_I='enabled'
_H='not-accessible'
_G='disabled'
_F='read-write'
_E='AVAYA-FABRIC-ATTACH-MIB'
_D='read-create'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','RowStatus','TextualConvention',_Q)
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
avayaFabricAttachMib=ModuleIdentity((1,3,6,1,4,1,45,5,46))
if mibBuilder.loadTexts:avayaFabricAttachMib.setRevisions(('2020-09-04 00:00','2020-08-03 00:00','2018-01-25 00:00','2016-11-21 00:00','2016-10-26 00:00','2016-07-12 00:00','2016-05-09 00:00','2016-04-04 00:00','2016-02-12 00:00','2016-01-26 00:00','2015-11-12 00:00',_U,_U,'2015-09-01 00:00','2015-04-27 00:00','2015-04-20 00:00','2015-04-08 00:00','2015-03-11 00:00','2014-12-18 00:00','2014-12-05 00:00','2014-11-10 00:00','2014-10-28 00:00','2014-10-06 00:00','2014-09-10 00:00','2014-07-16 00:00','2014-04-24 00:00','2014-03-03 00:00','2014-01-30 00:00','2013-11-22 00:00','2013-10-11 00:00','2013-08-12 00:00'))
_AvFabricAttachNotifications_ObjectIdentity=ObjectIdentity
avFabricAttachNotifications=_AvFabricAttachNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,46,0))
_AvFabricAttachObjects_ObjectIdentity=ObjectIdentity
avFabricAttachObjects=_AvFabricAttachObjects_ObjectIdentity((1,3,6,1,4,1,45,5,46,1))
class _AvFabricAttachService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AvFabricAttachService_Type.__name__=_B
_AvFabricAttachService_Object=MibScalar
avFabricAttachService=_AvFabricAttachService_Object((1,3,6,1,4,1,45,5,46,1,1),_AvFabricAttachService_Type())
avFabricAttachService.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachService.setStatus(_A)
class _AvFabricAttachElementType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_M,1),(_R,2),(_N,3),(_V,4),(_W,5),(_X,6),(_Y,7),(_Z,8),(_a,9),(_b,10),(_c,11),(_d,12),(_e,13),(_f,14),(_g,15),(_h,16),(_i,17)))
_AvFabricAttachElementType_Type.__name__=_B
_AvFabricAttachElementType_Object=MibScalar
avFabricAttachElementType=_AvFabricAttachElementType_Object((1,3,6,1,4,1,45,5,46,1,2),_AvFabricAttachElementType_Type())
avFabricAttachElementType.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachElementType.setStatus(_A)
class _AvFabricAttachPrimaryServerId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvFabricAttachPrimaryServerId_Type.__name__=_J
_AvFabricAttachPrimaryServerId_Object=MibScalar
avFabricAttachPrimaryServerId=_AvFabricAttachPrimaryServerId_Object((1,3,6,1,4,1,45,5,46,1,3),_AvFabricAttachPrimaryServerId_Type())
avFabricAttachPrimaryServerId.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachPrimaryServerId.setStatus(_A)
class _AvFabricAttachPrimaryServerDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AvFabricAttachPrimaryServerDescr_Type.__name__=_K
_AvFabricAttachPrimaryServerDescr_Object=MibScalar
avFabricAttachPrimaryServerDescr=_AvFabricAttachPrimaryServerDescr_Object((1,3,6,1,4,1,45,5,46,1,4),_AvFabricAttachPrimaryServerDescr_Type())
avFabricAttachPrimaryServerDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachPrimaryServerDescr.setStatus(_A)
_AvFabricAttachIsidVlanAsgnsTable_Object=MibTable
avFabricAttachIsidVlanAsgnsTable=_AvFabricAttachIsidVlanAsgnsTable_Object((1,3,6,1,4,1,45,5,46,1,5))
if mibBuilder.loadTexts:avFabricAttachIsidVlanAsgnsTable.setStatus(_A)
_AvFabricAttachIsidVlanAsgnsEntry_Object=MibTableRow
avFabricAttachIsidVlanAsgnsEntry=_AvFabricAttachIsidVlanAsgnsEntry_Object((1,3,6,1,4,1,45,5,46,1,5,1))
avFabricAttachIsidVlanAsgnsEntry.setIndexNames((0,_E,_j),(0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:avFabricAttachIsidVlanAsgnsEntry.setStatus(_A)
class _AvFabricAttachIsidVlanAsgnsIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvFabricAttachIsidVlanAsgnsIfIndex_Type.__name__=_B
_AvFabricAttachIsidVlanAsgnsIfIndex_Object=MibTableColumn
avFabricAttachIsidVlanAsgnsIfIndex=_AvFabricAttachIsidVlanAsgnsIfIndex_Object((1,3,6,1,4,1,45,5,46,1,5,1,1),_AvFabricAttachIsidVlanAsgnsIfIndex_Type())
avFabricAttachIsidVlanAsgnsIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:avFabricAttachIsidVlanAsgnsIfIndex.setStatus(_A)
class _AvFabricAttachIsidVlanAsgnsIsid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AvFabricAttachIsidVlanAsgnsIsid_Type.__name__=_B
_AvFabricAttachIsidVlanAsgnsIsid_Object=MibTableColumn
avFabricAttachIsidVlanAsgnsIsid=_AvFabricAttachIsidVlanAsgnsIsid_Object((1,3,6,1,4,1,45,5,46,1,5,1,2),_AvFabricAttachIsidVlanAsgnsIsid_Type())
avFabricAttachIsidVlanAsgnsIsid.setMaxAccess(_H)
if mibBuilder.loadTexts:avFabricAttachIsidVlanAsgnsIsid.setStatus(_A)
class _AvFabricAttachIsidVlanAsgnsVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AvFabricAttachIsidVlanAsgnsVlan_Type.__name__=_B
_AvFabricAttachIsidVlanAsgnsVlan_Object=MibTableColumn
avFabricAttachIsidVlanAsgnsVlan=_AvFabricAttachIsidVlanAsgnsVlan_Object((1,3,6,1,4,1,45,5,46,1,5,1,3),_AvFabricAttachIsidVlanAsgnsVlan_Type())
avFabricAttachIsidVlanAsgnsVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:avFabricAttachIsidVlanAsgnsVlan.setStatus(_A)
class _AvFabricAttachIsidVlanAsgnsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('pending',2),('active',3),('rejected',4)))
_AvFabricAttachIsidVlanAsgnsState_Type.__name__=_B
_AvFabricAttachIsidVlanAsgnsState_Object=MibTableColumn
avFabricAttachIsidVlanAsgnsState=_AvFabricAttachIsidVlanAsgnsState_Object((1,3,6,1,4,1,45,5,46,1,5,1,4),_AvFabricAttachIsidVlanAsgnsState_Type())
avFabricAttachIsidVlanAsgnsState.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachIsidVlanAsgnsState.setStatus(_A)
_AvFabricAttachIsidVlanAsgnsRowStatus_Type=RowStatus
_AvFabricAttachIsidVlanAsgnsRowStatus_Object=MibTableColumn
avFabricAttachIsidVlanAsgnsRowStatus=_AvFabricAttachIsidVlanAsgnsRowStatus_Object((1,3,6,1,4,1,45,5,46,1,5,1,5),_AvFabricAttachIsidVlanAsgnsRowStatus_Type())
avFabricAttachIsidVlanAsgnsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachIsidVlanAsgnsRowStatus.setStatus(_A)
class _AvFabricAttachIsidVlanAsgnsOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_N,2),('faClient',3),('faRadiusClient',4),('faZeroTouchClient',5)))
_AvFabricAttachIsidVlanAsgnsOrigin_Type.__name__=_B
_AvFabricAttachIsidVlanAsgnsOrigin_Object=MibTableColumn
avFabricAttachIsidVlanAsgnsOrigin=_AvFabricAttachIsidVlanAsgnsOrigin_Object((1,3,6,1,4,1,45,5,46,1,5,1,6),_AvFabricAttachIsidVlanAsgnsOrigin_Type())
avFabricAttachIsidVlanAsgnsOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachIsidVlanAsgnsOrigin.setStatus(_A)
class _AvFabricAttachIsidVlanAsgnsIsidName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvFabricAttachIsidVlanAsgnsIsidName_Type.__name__=_P
_AvFabricAttachIsidVlanAsgnsIsidName_Object=MibTableColumn
avFabricAttachIsidVlanAsgnsIsidName=_AvFabricAttachIsidVlanAsgnsIsidName_Object((1,3,6,1,4,1,45,5,46,1,5,1,7),_AvFabricAttachIsidVlanAsgnsIsidName_Type())
avFabricAttachIsidVlanAsgnsIsidName.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachIsidVlanAsgnsIsidName.setStatus(_A)
_AvFabricAttachPortTable_Object=MibTable
avFabricAttachPortTable=_AvFabricAttachPortTable_Object((1,3,6,1,4,1,45,5,46,1,6))
if mibBuilder.loadTexts:avFabricAttachPortTable.setStatus(_A)
_AvFabricAttachPortEntry_Object=MibTableRow
avFabricAttachPortEntry=_AvFabricAttachPortEntry_Object((1,3,6,1,4,1,45,5,46,1,6,1))
avFabricAttachPortEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:avFabricAttachPortEntry.setStatus(_A)
class _AvFabricAttachPortIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvFabricAttachPortIfIndex_Type.__name__=_B
_AvFabricAttachPortIfIndex_Object=MibTableColumn
avFabricAttachPortIfIndex=_AvFabricAttachPortIfIndex_Object((1,3,6,1,4,1,45,5,46,1,6,1,1),_AvFabricAttachPortIfIndex_Type())
avFabricAttachPortIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:avFabricAttachPortIfIndex.setStatus(_A)
class _AvFabricAttachPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AvFabricAttachPortState_Type.__name__=_B
_AvFabricAttachPortState_Object=MibTableColumn
avFabricAttachPortState=_AvFabricAttachPortState_Object((1,3,6,1,4,1,45,5,46,1,6,1,2),_AvFabricAttachPortState_Type())
avFabricAttachPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachPortState.setStatus(_A)
_AvFabricAttachPortRowStatus_Type=RowStatus
_AvFabricAttachPortRowStatus_Object=MibTableColumn
avFabricAttachPortRowStatus=_AvFabricAttachPortRowStatus_Object((1,3,6,1,4,1,45,5,46,1,6,1,3),_AvFabricAttachPortRowStatus_Type())
avFabricAttachPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachPortRowStatus.setStatus(_A)
class _AvFabricAttachPortMsgAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AvFabricAttachPortMsgAuthStatus_Type.__name__=_B
_AvFabricAttachPortMsgAuthStatus_Object=MibTableColumn
avFabricAttachPortMsgAuthStatus=_AvFabricAttachPortMsgAuthStatus_Object((1,3,6,1,4,1,45,5,46,1,6,1,4),_AvFabricAttachPortMsgAuthStatus_Type())
avFabricAttachPortMsgAuthStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachPortMsgAuthStatus.setStatus(_A)
class _AvFabricAttachPortMsgAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvFabricAttachPortMsgAuthKey_Type.__name__=_J
_AvFabricAttachPortMsgAuthKey_Object=MibTableColumn
avFabricAttachPortMsgAuthKey=_AvFabricAttachPortMsgAuthKey_Object((1,3,6,1,4,1,45,5,46,1,6,1,5),_AvFabricAttachPortMsgAuthKey_Type())
avFabricAttachPortMsgAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachPortMsgAuthKey.setStatus(_A)
class _AvFabricAttachPortMgmtIsid_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AvFabricAttachPortMgmtIsid_Type.__name__=_B
_AvFabricAttachPortMgmtIsid_Object=MibTableColumn
avFabricAttachPortMgmtIsid=_AvFabricAttachPortMgmtIsid_Object((1,3,6,1,4,1,45,5,46,1,6,1,6),_AvFabricAttachPortMgmtIsid_Type())
avFabricAttachPortMgmtIsid.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachPortMgmtIsid.setStatus(_A)
class _AvFabricAttachPortMgmtCvid_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_AvFabricAttachPortMgmtCvid_Type.__name__=_B
_AvFabricAttachPortMgmtCvid_Object=MibTableColumn
avFabricAttachPortMgmtCvid=_AvFabricAttachPortMgmtCvid_Object((1,3,6,1,4,1,45,5,46,1,6,1,7),_AvFabricAttachPortMgmtCvid_Type())
avFabricAttachPortMgmtCvid.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachPortMgmtCvid.setStatus(_A)
class _AvFabricAttachPortMsgAuthKeymode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),(_n,2)))
_AvFabricAttachPortMsgAuthKeymode_Type.__name__=_B
_AvFabricAttachPortMsgAuthKeymode_Object=MibTableColumn
avFabricAttachPortMsgAuthKeymode=_AvFabricAttachPortMsgAuthKeymode_Object((1,3,6,1,4,1,45,5,46,1,6,1,8),_AvFabricAttachPortMsgAuthKeymode_Type())
avFabricAttachPortMsgAuthKeymode.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachPortMsgAuthKeymode.setStatus(_A)
class _AvFabricAttachPortOrigin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('config',1),('autoSense',2)))
_AvFabricAttachPortOrigin_Type.__name__=_B
_AvFabricAttachPortOrigin_Object=MibTableColumn
avFabricAttachPortOrigin=_AvFabricAttachPortOrigin_Object((1,3,6,1,4,1,45,5,46,1,6,1,9),_AvFabricAttachPortOrigin_Type())
avFabricAttachPortOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachPortOrigin.setStatus(_A)
class _AvFabricAttachZeroTouchService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AvFabricAttachZeroTouchService_Type.__name__=_B
_AvFabricAttachZeroTouchService_Object=MibScalar
avFabricAttachZeroTouchService=_AvFabricAttachZeroTouchService_Object((1,3,6,1,4,1,45,5,46,1,7),_AvFabricAttachZeroTouchService_Type())
avFabricAttachZeroTouchService.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachZeroTouchService.setStatus(_A)
class _AvFabricAttachMsgAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AvFabricAttachMsgAuthStatus_Type.__name__=_B
_AvFabricAttachMsgAuthStatus_Object=MibScalar
avFabricAttachMsgAuthStatus=_AvFabricAttachMsgAuthStatus_Object((1,3,6,1,4,1,45,5,46,1,8),_AvFabricAttachMsgAuthStatus_Type())
avFabricAttachMsgAuthStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachMsgAuthStatus.setStatus(_A)
class _AvFabricAttachMsgAuthKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvFabricAttachMsgAuthKey_Type.__name__=_J
_AvFabricAttachMsgAuthKey_Object=MibScalar
avFabricAttachMsgAuthKey=_AvFabricAttachMsgAuthKey_Object((1,3,6,1,4,1,45,5,46,1,9),_AvFabricAttachMsgAuthKey_Type())
avFabricAttachMsgAuthKey.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachMsgAuthKey.setStatus(_A)
class _AvFabricAttachClientProxyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AvFabricAttachClientProxyStatus_Type.__name__=_B
_AvFabricAttachClientProxyStatus_Object=MibScalar
avFabricAttachClientProxyStatus=_AvFabricAttachClientProxyStatus_Object((1,3,6,1,4,1,45,5,46,1,10),_AvFabricAttachClientProxyStatus_Type())
avFabricAttachClientProxyStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachClientProxyStatus.setStatus(_A)
_AvFabricAttachDiscElemsTable_Object=MibTable
avFabricAttachDiscElemsTable=_AvFabricAttachDiscElemsTable_Object((1,3,6,1,4,1,45,5,46,1,11))
if mibBuilder.loadTexts:avFabricAttachDiscElemsTable.setStatus(_A)
_AvFabricAttachDiscElemsEntry_Object=MibTableRow
avFabricAttachDiscElemsEntry=_AvFabricAttachDiscElemsEntry_Object((1,3,6,1,4,1,45,5,46,1,11,1))
avFabricAttachDiscElemsEntry.setIndexNames((0,_E,_o))
if mibBuilder.loadTexts:avFabricAttachDiscElemsEntry.setStatus(_A)
class _AvFabricAttachDiscElemsIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvFabricAttachDiscElemsIfIndex_Type.__name__=_B
_AvFabricAttachDiscElemsIfIndex_Object=MibTableColumn
avFabricAttachDiscElemsIfIndex=_AvFabricAttachDiscElemsIfIndex_Object((1,3,6,1,4,1,45,5,46,1,11,1,1),_AvFabricAttachDiscElemsIfIndex_Type())
avFabricAttachDiscElemsIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:avFabricAttachDiscElemsIfIndex.setStatus(_A)
class _AvFabricAttachDiscElemsElementType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_M,1),(_R,2),(_N,3),(_V,4),(_W,5),(_X,6),(_Y,7),(_Z,8),(_a,9),(_b,10),(_c,11),(_d,12),(_e,13),(_f,14),(_g,15),(_h,16),(_i,17)))
_AvFabricAttachDiscElemsElementType_Type.__name__=_B
_AvFabricAttachDiscElemsElementType_Object=MibTableColumn
avFabricAttachDiscElemsElementType=_AvFabricAttachDiscElemsElementType_Object((1,3,6,1,4,1,45,5,46,1,11,1,2),_AvFabricAttachDiscElemsElementType_Type())
avFabricAttachDiscElemsElementType.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachDiscElemsElementType.setStatus(_A)
class _AvFabricAttachDiscElemsElementVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_AvFabricAttachDiscElemsElementVlan_Type.__name__=_B
_AvFabricAttachDiscElemsElementVlan_Object=MibTableColumn
avFabricAttachDiscElemsElementVlan=_AvFabricAttachDiscElemsElementVlan_Object((1,3,6,1,4,1,45,5,46,1,11,1,3),_AvFabricAttachDiscElemsElementVlan_Type())
avFabricAttachDiscElemsElementVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachDiscElemsElementVlan.setStatus(_A)
class _AvFabricAttachDiscElemsElementId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvFabricAttachDiscElemsElementId_Type.__name__=_J
_AvFabricAttachDiscElemsElementId_Object=MibTableColumn
avFabricAttachDiscElemsElementId=_AvFabricAttachDiscElemsElementId_Object((1,3,6,1,4,1,45,5,46,1,11,1,4),_AvFabricAttachDiscElemsElementId_Type())
avFabricAttachDiscElemsElementId.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachDiscElemsElementId.setStatus(_A)
class _AvFabricAttachDiscElemsElementState_Type(Bits):namedValues=NamedValues(*(('trafficTagged',0),('trafficTaggedAndUntagged',1),('provisionModeDisabled',2),('provisionModeSpbm',3),('provisionModeVlan',4)))
_AvFabricAttachDiscElemsElementState_Type.__name__=_L
_AvFabricAttachDiscElemsElementState_Object=MibTableColumn
avFabricAttachDiscElemsElementState=_AvFabricAttachDiscElemsElementState_Object((1,3,6,1,4,1,45,5,46,1,11,1,5),_AvFabricAttachDiscElemsElementState_Type())
avFabricAttachDiscElemsElementState.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachDiscElemsElementState.setStatus(_A)
class _AvFabricAttachDiscElemsElementAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3),(_O,4)))
_AvFabricAttachDiscElemsElementAuth_Type.__name__=_B
_AvFabricAttachDiscElemsElementAuth_Object=MibTableColumn
avFabricAttachDiscElemsElementAuth=_AvFabricAttachDiscElemsElementAuth_Object((1,3,6,1,4,1,45,5,46,1,11,1,6),_AvFabricAttachDiscElemsElementAuth_Type())
avFabricAttachDiscElemsElementAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachDiscElemsElementAuth.setStatus(_A)
class _AvFabricAttachDiscElemsElementTrunkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvFabricAttachDiscElemsElementTrunkId_Type.__name__=_B
_AvFabricAttachDiscElemsElementTrunkId_Object=MibTableColumn
avFabricAttachDiscElemsElementTrunkId=_AvFabricAttachDiscElemsElementTrunkId_Object((1,3,6,1,4,1,45,5,46,1,11,1,7),_AvFabricAttachDiscElemsElementTrunkId_Type())
avFabricAttachDiscElemsElementTrunkId.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachDiscElemsElementTrunkId.setStatus(_A)
class _AvFabricAttachDiscElemsElementOperAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_s,2),(_t,3),(_u,4),(_v,5),(_w,6)))
_AvFabricAttachDiscElemsElementOperAuthStatus_Type.__name__=_B
_AvFabricAttachDiscElemsElementOperAuthStatus_Object=MibTableColumn
avFabricAttachDiscElemsElementOperAuthStatus=_AvFabricAttachDiscElemsElementOperAuthStatus_Object((1,3,6,1,4,1,45,5,46,1,11,1,8),_AvFabricAttachDiscElemsElementOperAuthStatus_Type())
avFabricAttachDiscElemsElementOperAuthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachDiscElemsElementOperAuthStatus.setStatus(_A)
class _AvFabricAttachDiscElemsElementAsgnsOperAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_s,2),(_t,3),(_u,4),(_v,5),(_w,6)))
_AvFabricAttachDiscElemsElementAsgnsOperAuthStatus_Type.__name__=_B
_AvFabricAttachDiscElemsElementAsgnsOperAuthStatus_Object=MibTableColumn
avFabricAttachDiscElemsElementAsgnsOperAuthStatus=_AvFabricAttachDiscElemsElementAsgnsOperAuthStatus_Object((1,3,6,1,4,1,45,5,46,1,11,1,9),_AvFabricAttachDiscElemsElementAsgnsOperAuthStatus_Type())
avFabricAttachDiscElemsElementAsgnsOperAuthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachDiscElemsElementAsgnsOperAuthStatus.setStatus(_A)
class _AvFabricAttachDiscElemsAsgnsAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_p,1),(_q,2),(_r,3),(_O,4)))
_AvFabricAttachDiscElemsAsgnsAuth_Type.__name__=_B
_AvFabricAttachDiscElemsAsgnsAuth_Object=MibTableColumn
avFabricAttachDiscElemsAsgnsAuth=_AvFabricAttachDiscElemsAsgnsAuth_Object((1,3,6,1,4,1,45,5,46,1,11,1,10),_AvFabricAttachDiscElemsAsgnsAuth_Type())
avFabricAttachDiscElemsAsgnsAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachDiscElemsAsgnsAuth.setStatus(_A)
class _AvFabricAttachAutoProvision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_R,2),(_N,3)))
_AvFabricAttachAutoProvision_Type.__name__=_B
_AvFabricAttachAutoProvision_Object=MibScalar
avFabricAttachAutoProvision=_AvFabricAttachAutoProvision_Object((1,3,6,1,4,1,45,5,46,1,12),_AvFabricAttachAutoProvision_Type())
avFabricAttachAutoProvision.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachAutoProvision.setStatus(_A)
class _AvFabricAttachProvisionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('spbm',2),('vlan',3)))
_AvFabricAttachProvisionMode_Type.__name__=_B
_AvFabricAttachProvisionMode_Object=MibScalar
avFabricAttachProvisionMode=_AvFabricAttachProvisionMode_Object((1,3,6,1,4,1,45,5,46,1,13),_AvFabricAttachProvisionMode_Type())
avFabricAttachProvisionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachProvisionMode.setStatus(_A)
class _AvFabricAttachZeroTouchOptionFlags_Type(Bits):namedValues=NamedValues(*((_x,0),(_y,1),(_z,2),(_A0,3),('nsv',4),(_A1,5),(_A2,6),(_A3,7),(_A4,8)))
_AvFabricAttachZeroTouchOptionFlags_Type.__name__=_L
_AvFabricAttachZeroTouchOptionFlags_Object=MibScalar
avFabricAttachZeroTouchOptionFlags=_AvFabricAttachZeroTouchOptionFlags_Object((1,3,6,1,4,1,45,5,46,1,14),_AvFabricAttachZeroTouchOptionFlags_Type())
avFabricAttachZeroTouchOptionFlags.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachZeroTouchOptionFlags.setStatus(_A)
_AvFabricAttachZeroTouchNsvTable_Object=MibTable
avFabricAttachZeroTouchNsvTable=_AvFabricAttachZeroTouchNsvTable_Object((1,3,6,1,4,1,45,5,46,1,15))
if mibBuilder.loadTexts:avFabricAttachZeroTouchNsvTable.setStatus(_A)
_AvFabricAttachZeroTouchNsvEntry_Object=MibTableRow
avFabricAttachZeroTouchNsvEntry=_AvFabricAttachZeroTouchNsvEntry_Object((1,3,6,1,4,1,45,5,46,1,15,1))
avFabricAttachZeroTouchNsvEntry.setIndexNames((0,_E,_A5))
if mibBuilder.loadTexts:avFabricAttachZeroTouchNsvEntry.setStatus(_A)
class _AvFabricAttachZeroTouchNsvType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AvFabricAttachZeroTouchNsvType_Type.__name__=_B
_AvFabricAttachZeroTouchNsvType_Object=MibTableColumn
avFabricAttachZeroTouchNsvType=_AvFabricAttachZeroTouchNsvType_Object((1,3,6,1,4,1,45,5,46,1,15,1,1),_AvFabricAttachZeroTouchNsvType_Type())
avFabricAttachZeroTouchNsvType.setMaxAccess(_H)
if mibBuilder.loadTexts:avFabricAttachZeroTouchNsvType.setStatus(_A)
class _AvFabricAttachZeroTouchNsvVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_AvFabricAttachZeroTouchNsvVlan_Type.__name__=_B
_AvFabricAttachZeroTouchNsvVlan_Object=MibTableColumn
avFabricAttachZeroTouchNsvVlan=_AvFabricAttachZeroTouchNsvVlan_Object((1,3,6,1,4,1,45,5,46,1,15,1,2),_AvFabricAttachZeroTouchNsvVlan_Type())
avFabricAttachZeroTouchNsvVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchNsvVlan.setStatus(_A)
class _AvFabricAttachZeroTouchNsvPortPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AvFabricAttachZeroTouchNsvPortPriority_Type.__name__=_B
_AvFabricAttachZeroTouchNsvPortPriority_Object=MibTableColumn
avFabricAttachZeroTouchNsvPortPriority=_AvFabricAttachZeroTouchNsvPortPriority_Object((1,3,6,1,4,1,45,5,46,1,15,1,3),_AvFabricAttachZeroTouchNsvPortPriority_Type())
avFabricAttachZeroTouchNsvPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchNsvPortPriority.setStatus(_A)
class _AvFabricAttachZeroTouchNsvStateFlags_Type(Bits):namedValues=NamedValues(*(('updatePvid',0),('updatePortPriority',1)))
_AvFabricAttachZeroTouchNsvStateFlags_Type.__name__=_L
_AvFabricAttachZeroTouchNsvStateFlags_Object=MibTableColumn
avFabricAttachZeroTouchNsvStateFlags=_AvFabricAttachZeroTouchNsvStateFlags_Object((1,3,6,1,4,1,45,5,46,1,15,1,4),_AvFabricAttachZeroTouchNsvStateFlags_Type())
avFabricAttachZeroTouchNsvStateFlags.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchNsvStateFlags.setStatus(_A)
_AvFabricAttachZeroTouchNsvRowStatus_Type=RowStatus
_AvFabricAttachZeroTouchNsvRowStatus_Object=MibTableColumn
avFabricAttachZeroTouchNsvRowStatus=_AvFabricAttachZeroTouchNsvRowStatus_Object((1,3,6,1,4,1,45,5,46,1,15,1,5),_AvFabricAttachZeroTouchNsvRowStatus_Type())
avFabricAttachZeroTouchNsvRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchNsvRowStatus.setStatus(_A)
class _AvFabricAttachZeroTouchNsvIsid_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777214))
_AvFabricAttachZeroTouchNsvIsid_Type.__name__=_B
_AvFabricAttachZeroTouchNsvIsid_Object=MibTableColumn
avFabricAttachZeroTouchNsvIsid=_AvFabricAttachZeroTouchNsvIsid_Object((1,3,6,1,4,1,45,5,46,1,15,1,6),_AvFabricAttachZeroTouchNsvIsid_Type())
avFabricAttachZeroTouchNsvIsid.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchNsvIsid.setStatus(_A)
class _AvFabricAttachZeroTouchRadiusPriSrvrIpv4Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_AvFabricAttachZeroTouchRadiusPriSrvrIpv4Addr_Type.__name__=_J
_AvFabricAttachZeroTouchRadiusPriSrvrIpv4Addr_Object=MibScalar
avFabricAttachZeroTouchRadiusPriSrvrIpv4Addr=_AvFabricAttachZeroTouchRadiusPriSrvrIpv4Addr_Object((1,3,6,1,4,1,45,5,46,1,16),_AvFabricAttachZeroTouchRadiusPriSrvrIpv4Addr_Type())
avFabricAttachZeroTouchRadiusPriSrvrIpv4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachZeroTouchRadiusPriSrvrIpv4Addr.setStatus(_A)
class _AvFabricAttachZeroTouchRadiusSecSrvrIpv4Addr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_AvFabricAttachZeroTouchRadiusSecSrvrIpv4Addr_Type.__name__=_J
_AvFabricAttachZeroTouchRadiusSecSrvrIpv4Addr_Object=MibScalar
avFabricAttachZeroTouchRadiusSecSrvrIpv4Addr=_AvFabricAttachZeroTouchRadiusSecSrvrIpv4Addr_Object((1,3,6,1,4,1,45,5,46,1,17),_AvFabricAttachZeroTouchRadiusSecSrvrIpv4Addr_Type())
avFabricAttachZeroTouchRadiusSecSrvrIpv4Addr.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachZeroTouchRadiusSecSrvrIpv4Addr.setStatus(_A)
class _AvFabricAttachZeroTouchRadiusTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_AvFabricAttachZeroTouchRadiusTimeout_Type.__name__=_B
_AvFabricAttachZeroTouchRadiusTimeout_Object=MibScalar
avFabricAttachZeroTouchRadiusTimeout=_AvFabricAttachZeroTouchRadiusTimeout_Object((1,3,6,1,4,1,45,5,46,1,18),_AvFabricAttachZeroTouchRadiusTimeout_Type())
avFabricAttachZeroTouchRadiusTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachZeroTouchRadiusTimeout.setStatus(_A)
class _AvFabricAttachStandaloneProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AvFabricAttachStandaloneProxy_Type.__name__=_B
_AvFabricAttachStandaloneProxy_Object=MibScalar
avFabricAttachStandaloneProxy=_AvFabricAttachStandaloneProxy_Object((1,3,6,1,4,1,45,5,46,1,19),_AvFabricAttachStandaloneProxy_Type())
avFabricAttachStandaloneProxy.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachStandaloneProxy.setStatus(_A)
class _AvFabricAttachStaticUplinkIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvFabricAttachStaticUplinkIfIndex_Type.__name__=_B
_AvFabricAttachStaticUplinkIfIndex_Object=MibScalar
avFabricAttachStaticUplinkIfIndex=_AvFabricAttachStaticUplinkIfIndex_Object((1,3,6,1,4,1,45,5,46,1,20),_AvFabricAttachStaticUplinkIfIndex_Type())
avFabricAttachStaticUplinkIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachStaticUplinkIfIndex.setStatus(_A)
class _AvFabricAttachStaticUplinkTrunk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_AvFabricAttachStaticUplinkTrunk_Type.__name__=_B
_AvFabricAttachStaticUplinkTrunk_Object=MibScalar
avFabricAttachStaticUplinkTrunk=_AvFabricAttachStaticUplinkTrunk_Object((1,3,6,1,4,1,45,5,46,1,21),_AvFabricAttachStaticUplinkTrunk_Type())
avFabricAttachStaticUplinkTrunk.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachStaticUplinkTrunk.setStatus(_A)
class _AvFabricAttachAsgnTimeout_Type(Integer32):defaultValue=240;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,480))
_AvFabricAttachAsgnTimeout_Type.__name__=_B
_AvFabricAttachAsgnTimeout_Object=MibScalar
avFabricAttachAsgnTimeout=_AvFabricAttachAsgnTimeout_Object((1,3,6,1,4,1,45,5,46,1,22),_AvFabricAttachAsgnTimeout_Type())
avFabricAttachAsgnTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachAsgnTimeout.setStatus(_A)
_AvFabricAttachStatsTable_Object=MibTable
avFabricAttachStatsTable=_AvFabricAttachStatsTable_Object((1,3,6,1,4,1,45,5,46,1,23))
if mibBuilder.loadTexts:avFabricAttachStatsTable.setStatus(_A)
_AvFabricAttachStatsEntry_Object=MibTableRow
avFabricAttachStatsEntry=_AvFabricAttachStatsEntry_Object((1,3,6,1,4,1,45,5,46,1,23,1))
avFabricAttachStatsEntry.setIndexNames((0,_E,_A6))
if mibBuilder.loadTexts:avFabricAttachStatsEntry.setStatus(_A)
class _AvFabricAttachStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvFabricAttachStatsPortIndex_Type.__name__=_B
_AvFabricAttachStatsPortIndex_Object=MibTableColumn
avFabricAttachStatsPortIndex=_AvFabricAttachStatsPortIndex_Object((1,3,6,1,4,1,45,5,46,1,23,1,1),_AvFabricAttachStatsPortIndex_Type())
avFabricAttachStatsPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:avFabricAttachStatsPortIndex.setStatus(_A)
_AvFabricAttachStatsDiscElemReceived_Type=Counter32
_AvFabricAttachStatsDiscElemReceived_Object=MibTableColumn
avFabricAttachStatsDiscElemReceived=_AvFabricAttachStatsDiscElemReceived_Object((1,3,6,1,4,1,45,5,46,1,23,1,2),_AvFabricAttachStatsDiscElemReceived_Type())
avFabricAttachStatsDiscElemReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachStatsDiscElemReceived.setStatus(_A)
_AvFabricAttachStatsAsgnReceived_Type=Counter32
_AvFabricAttachStatsAsgnReceived_Object=MibTableColumn
avFabricAttachStatsAsgnReceived=_AvFabricAttachStatsAsgnReceived_Object((1,3,6,1,4,1,45,5,46,1,23,1,3),_AvFabricAttachStatsAsgnReceived_Type())
avFabricAttachStatsAsgnReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachStatsAsgnReceived.setStatus(_A)
_AvFabricAttachStatsAsgnAccepted_Type=Counter32
_AvFabricAttachStatsAsgnAccepted_Object=MibTableColumn
avFabricAttachStatsAsgnAccepted=_AvFabricAttachStatsAsgnAccepted_Object((1,3,6,1,4,1,45,5,46,1,23,1,4),_AvFabricAttachStatsAsgnAccepted_Type())
avFabricAttachStatsAsgnAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachStatsAsgnAccepted.setStatus(_A)
_AvFabricAttachStatsAsgnRejected_Type=Counter32
_AvFabricAttachStatsAsgnRejected_Object=MibTableColumn
avFabricAttachStatsAsgnRejected=_AvFabricAttachStatsAsgnRejected_Object((1,3,6,1,4,1,45,5,46,1,23,1,5),_AvFabricAttachStatsAsgnRejected_Type())
avFabricAttachStatsAsgnRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachStatsAsgnRejected.setStatus(_A)
_AvFabricAttachStatsAsgnExpired_Type=Counter32
_AvFabricAttachStatsAsgnExpired_Object=MibTableColumn
avFabricAttachStatsAsgnExpired=_AvFabricAttachStatsAsgnExpired_Object((1,3,6,1,4,1,45,5,46,1,23,1,6),_AvFabricAttachStatsAsgnExpired_Type())
avFabricAttachStatsAsgnExpired.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachStatsAsgnExpired.setStatus(_A)
_AvFabricAttachStatsDiscAuthFailed_Type=Counter32
_AvFabricAttachStatsDiscAuthFailed_Object=MibTableColumn
avFabricAttachStatsDiscAuthFailed=_AvFabricAttachStatsDiscAuthFailed_Object((1,3,6,1,4,1,45,5,46,1,23,1,7),_AvFabricAttachStatsDiscAuthFailed_Type())
avFabricAttachStatsDiscAuthFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachStatsDiscAuthFailed.setStatus(_A)
_AvFabricAttachStatsDiscElemExpired_Type=Counter32
_AvFabricAttachStatsDiscElemExpired_Object=MibTableColumn
avFabricAttachStatsDiscElemExpired=_AvFabricAttachStatsDiscElemExpired_Object((1,3,6,1,4,1,45,5,46,1,23,1,8),_AvFabricAttachStatsDiscElemExpired_Type())
avFabricAttachStatsDiscElemExpired.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachStatsDiscElemExpired.setStatus(_A)
_AvFabricAttachStatsDiscElemDeleted_Type=Counter32
_AvFabricAttachStatsDiscElemDeleted_Object=MibTableColumn
avFabricAttachStatsDiscElemDeleted=_AvFabricAttachStatsDiscElemDeleted_Object((1,3,6,1,4,1,45,5,46,1,23,1,9),_AvFabricAttachStatsDiscElemDeleted_Type())
avFabricAttachStatsDiscElemDeleted.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachStatsDiscElemDeleted.setStatus(_A)
_AvFabricAttachStatsAsgnDeleted_Type=Counter32
_AvFabricAttachStatsAsgnDeleted_Object=MibTableColumn
avFabricAttachStatsAsgnDeleted=_AvFabricAttachStatsAsgnDeleted_Object((1,3,6,1,4,1,45,5,46,1,23,1,10),_AvFabricAttachStatsAsgnDeleted_Type())
avFabricAttachStatsAsgnDeleted.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachStatsAsgnDeleted.setStatus(_A)
_AvFabricAttachStatsAsgnAuthFailed_Type=Counter32
_AvFabricAttachStatsAsgnAuthFailed_Object=MibTableColumn
avFabricAttachStatsAsgnAuthFailed=_AvFabricAttachStatsAsgnAuthFailed_Object((1,3,6,1,4,1,45,5,46,1,23,1,11),_AvFabricAttachStatsAsgnAuthFailed_Type())
avFabricAttachStatsAsgnAuthFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachStatsAsgnAuthFailed.setStatus(_A)
_AvFabricAttachGlobalStats_ObjectIdentity=ObjectIdentity
avFabricAttachGlobalStats=_AvFabricAttachGlobalStats_ObjectIdentity((1,3,6,1,4,1,45,5,46,1,24))
_AvFabricAttachGlobalStatsDiscElemReceived_Type=Counter32
_AvFabricAttachGlobalStatsDiscElemReceived_Object=MibScalar
avFabricAttachGlobalStatsDiscElemReceived=_AvFabricAttachGlobalStatsDiscElemReceived_Object((1,3,6,1,4,1,45,5,46,1,24,1),_AvFabricAttachGlobalStatsDiscElemReceived_Type())
avFabricAttachGlobalStatsDiscElemReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsDiscElemReceived.setStatus(_A)
_AvFabricAttachGlobalStatsAsgnReceived_Type=Counter32
_AvFabricAttachGlobalStatsAsgnReceived_Object=MibScalar
avFabricAttachGlobalStatsAsgnReceived=_AvFabricAttachGlobalStatsAsgnReceived_Object((1,3,6,1,4,1,45,5,46,1,24,2),_AvFabricAttachGlobalStatsAsgnReceived_Type())
avFabricAttachGlobalStatsAsgnReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsAsgnReceived.setStatus(_A)
_AvFabricAttachGlobalStatsAsgnAccepted_Type=Counter32
_AvFabricAttachGlobalStatsAsgnAccepted_Object=MibScalar
avFabricAttachGlobalStatsAsgnAccepted=_AvFabricAttachGlobalStatsAsgnAccepted_Object((1,3,6,1,4,1,45,5,46,1,24,3),_AvFabricAttachGlobalStatsAsgnAccepted_Type())
avFabricAttachGlobalStatsAsgnAccepted.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsAsgnAccepted.setStatus(_A)
_AvFabricAttachGlobalStatsAsgnRejected_Type=Counter32
_AvFabricAttachGlobalStatsAsgnRejected_Object=MibScalar
avFabricAttachGlobalStatsAsgnRejected=_AvFabricAttachGlobalStatsAsgnRejected_Object((1,3,6,1,4,1,45,5,46,1,24,4),_AvFabricAttachGlobalStatsAsgnRejected_Type())
avFabricAttachGlobalStatsAsgnRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsAsgnRejected.setStatus(_A)
_AvFabricAttachGlobalStatsAsgnExpired_Type=Counter32
_AvFabricAttachGlobalStatsAsgnExpired_Object=MibScalar
avFabricAttachGlobalStatsAsgnExpired=_AvFabricAttachGlobalStatsAsgnExpired_Object((1,3,6,1,4,1,45,5,46,1,24,5),_AvFabricAttachGlobalStatsAsgnExpired_Type())
avFabricAttachGlobalStatsAsgnExpired.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsAsgnExpired.setStatus(_A)
_AvFabricAttachGlobalStatsDiscAuthFailed_Type=Counter32
_AvFabricAttachGlobalStatsDiscAuthFailed_Object=MibScalar
avFabricAttachGlobalStatsDiscAuthFailed=_AvFabricAttachGlobalStatsDiscAuthFailed_Object((1,3,6,1,4,1,45,5,46,1,24,6),_AvFabricAttachGlobalStatsDiscAuthFailed_Type())
avFabricAttachGlobalStatsDiscAuthFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsDiscAuthFailed.setStatus(_A)
_AvFabricAttachGlobalStatsDiscElemExpired_Type=Counter32
_AvFabricAttachGlobalStatsDiscElemExpired_Object=MibScalar
avFabricAttachGlobalStatsDiscElemExpired=_AvFabricAttachGlobalStatsDiscElemExpired_Object((1,3,6,1,4,1,45,5,46,1,24,7),_AvFabricAttachGlobalStatsDiscElemExpired_Type())
avFabricAttachGlobalStatsDiscElemExpired.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsDiscElemExpired.setStatus(_A)
_AvFabricAttachGlobalStatsDiscElemDeleted_Type=Counter32
_AvFabricAttachGlobalStatsDiscElemDeleted_Object=MibScalar
avFabricAttachGlobalStatsDiscElemDeleted=_AvFabricAttachGlobalStatsDiscElemDeleted_Object((1,3,6,1,4,1,45,5,46,1,24,8),_AvFabricAttachGlobalStatsDiscElemDeleted_Type())
avFabricAttachGlobalStatsDiscElemDeleted.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsDiscElemDeleted.setStatus(_A)
_AvFabricAttachGlobalStatsAsgnDeleted_Type=Counter32
_AvFabricAttachGlobalStatsAsgnDeleted_Object=MibScalar
avFabricAttachGlobalStatsAsgnDeleted=_AvFabricAttachGlobalStatsAsgnDeleted_Object((1,3,6,1,4,1,45,5,46,1,24,9),_AvFabricAttachGlobalStatsAsgnDeleted_Type())
avFabricAttachGlobalStatsAsgnDeleted.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsAsgnDeleted.setStatus(_A)
_AvFabricAttachGlobalStatsAsgnAuthFailed_Type=Counter32
_AvFabricAttachGlobalStatsAsgnAuthFailed_Object=MibScalar
avFabricAttachGlobalStatsAsgnAuthFailed=_AvFabricAttachGlobalStatsAsgnAuthFailed_Object((1,3,6,1,4,1,45,5,46,1,24,10),_AvFabricAttachGlobalStatsAsgnAuthFailed_Type())
avFabricAttachGlobalStatsAsgnAuthFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsAsgnAuthFailed.setStatus(_A)
_AvFabricAttachGlobalStatsCurReceivedBindings_Type=Counter32
_AvFabricAttachGlobalStatsCurReceivedBindings_Object=MibScalar
avFabricAttachGlobalStatsCurReceivedBindings=_AvFabricAttachGlobalStatsCurReceivedBindings_Object((1,3,6,1,4,1,45,5,46,1,24,11),_AvFabricAttachGlobalStatsCurReceivedBindings_Type())
avFabricAttachGlobalStatsCurReceivedBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsCurReceivedBindings.setStatus(_A)
_AvFabricAttachGlobalStatsCurAdvertisedBindings_Type=Counter32
_AvFabricAttachGlobalStatsCurAdvertisedBindings_Object=MibScalar
avFabricAttachGlobalStatsCurAdvertisedBindings=_AvFabricAttachGlobalStatsCurAdvertisedBindings_Object((1,3,6,1,4,1,45,5,46,1,24,12),_AvFabricAttachGlobalStatsCurAdvertisedBindings_Type())
avFabricAttachGlobalStatsCurAdvertisedBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachGlobalStatsCurAdvertisedBindings.setStatus(_A)
class _AvFabricAttachExtendedLogging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AvFabricAttachExtendedLogging_Type.__name__=_B
_AvFabricAttachExtendedLogging_Object=MibScalar
avFabricAttachExtendedLogging=_AvFabricAttachExtendedLogging_Object((1,3,6,1,4,1,45,5,46,1,25),_AvFabricAttachExtendedLogging_Type())
avFabricAttachExtendedLogging.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachExtendedLogging.setStatus(_A)
class _AvFabricAttachDiscTimeout_Type(Integer32):defaultValue=240;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,480))
_AvFabricAttachDiscTimeout_Type.__name__=_B
_AvFabricAttachDiscTimeout_Object=MibScalar
avFabricAttachDiscTimeout=_AvFabricAttachDiscTimeout_Object((1,3,6,1,4,1,45,5,46,1,26),_AvFabricAttachDiscTimeout_Type())
avFabricAttachDiscTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachDiscTimeout.setStatus(_A)
_AvFabricAttachZeroTouchClientTable_Object=MibTable
avFabricAttachZeroTouchClientTable=_AvFabricAttachZeroTouchClientTable_Object((1,3,6,1,4,1,45,5,46,1,27))
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientTable.setStatus(_A)
_AvFabricAttachZeroTouchClientEntry_Object=MibTableRow
avFabricAttachZeroTouchClientEntry=_AvFabricAttachZeroTouchClientEntry_Object((1,3,6,1,4,1,45,5,46,1,27,1))
avFabricAttachZeroTouchClientEntry.setIndexNames((0,_E,_A7))
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientEntry.setStatus(_A)
class _AvFabricAttachZeroTouchClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AvFabricAttachZeroTouchClientType_Type.__name__=_B
_AvFabricAttachZeroTouchClientType_Object=MibTableColumn
avFabricAttachZeroTouchClientType=_AvFabricAttachZeroTouchClientType_Object((1,3,6,1,4,1,45,5,46,1,27,1,1),_AvFabricAttachZeroTouchClientType_Type())
avFabricAttachZeroTouchClientType.setMaxAccess(_H)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientType.setStatus(_A)
class _AvFabricAttachZeroTouchClientDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_AvFabricAttachZeroTouchClientDescr_Type.__name__=_K
_AvFabricAttachZeroTouchClientDescr_Object=MibTableColumn
avFabricAttachZeroTouchClientDescr=_AvFabricAttachZeroTouchClientDescr_Object((1,3,6,1,4,1,45,5,46,1,27,1,2),_AvFabricAttachZeroTouchClientDescr_Type())
avFabricAttachZeroTouchClientDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientDescr.setStatus(_A)
class _AvFabricAttachZeroTouchClientOptionFlags_Type(Bits):namedValues=NamedValues(*((_x,0),(_y,1),(_z,2),(_A0,3),('nsv',4),(_A1,5),(_A2,6),(_A3,7),(_A4,8)))
_AvFabricAttachZeroTouchClientOptionFlags_Type.__name__=_L
_AvFabricAttachZeroTouchClientOptionFlags_Object=MibTableColumn
avFabricAttachZeroTouchClientOptionFlags=_AvFabricAttachZeroTouchClientOptionFlags_Object((1,3,6,1,4,1,45,5,46,1,27,1,3),_AvFabricAttachZeroTouchClientOptionFlags_Type())
avFabricAttachZeroTouchClientOptionFlags.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientOptionFlags.setStatus(_A)
_AvFabricAttachZeroTouchClientRowStatus_Type=RowStatus
_AvFabricAttachZeroTouchClientRowStatus_Object=MibTableColumn
avFabricAttachZeroTouchClientRowStatus=_AvFabricAttachZeroTouchClientRowStatus_Object((1,3,6,1,4,1,45,5,46,1,27,1,4),_AvFabricAttachZeroTouchClientRowStatus_Type())
avFabricAttachZeroTouchClientRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientRowStatus.setStatus(_A)
class _AvFabricAttachZeroTouchClientName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvFabricAttachZeroTouchClientName_Type.__name__=_K
_AvFabricAttachZeroTouchClientName_Object=MibTableColumn
avFabricAttachZeroTouchClientName=_AvFabricAttachZeroTouchClientName_Object((1,3,6,1,4,1,45,5,46,1,27,1,5),_AvFabricAttachZeroTouchClientName_Type())
avFabricAttachZeroTouchClientName.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientName.setStatus(_A)
class _AvFabricAttachZeroTouchClientOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_n,1),('custom',2)))
_AvFabricAttachZeroTouchClientOrigin_Type.__name__=_B
_AvFabricAttachZeroTouchClientOrigin_Object=MibTableColumn
avFabricAttachZeroTouchClientOrigin=_AvFabricAttachZeroTouchClientOrigin_Object((1,3,6,1,4,1,45,5,46,1,27,1,6),_AvFabricAttachZeroTouchClientOrigin_Type())
avFabricAttachZeroTouchClientOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientOrigin.setStatus(_A)
_AvFabricAttachStats_ObjectIdentity=ObjectIdentity
avFabricAttachStats=_AvFabricAttachStats_ObjectIdentity((1,3,6,1,4,1,45,5,46,1,28))
class _AvFabricAttachStatsClearErrorCounters_Type(TruthValue):defaultValue=2
_AvFabricAttachStatsClearErrorCounters_Type.__name__=_Q
_AvFabricAttachStatsClearErrorCounters_Object=MibScalar
avFabricAttachStatsClearErrorCounters=_AvFabricAttachStatsClearErrorCounters_Object((1,3,6,1,4,1,45,5,46,1,28,1),_AvFabricAttachStatsClearErrorCounters_Type())
avFabricAttachStatsClearErrorCounters.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachStatsClearErrorCounters.setStatus(_A)
class _AvFabricAttachStatsClearGlobalErrorCounters_Type(TruthValue):defaultValue=2
_AvFabricAttachStatsClearGlobalErrorCounters_Type.__name__=_Q
_AvFabricAttachStatsClearGlobalErrorCounters_Object=MibScalar
avFabricAttachStatsClearGlobalErrorCounters=_AvFabricAttachStatsClearGlobalErrorCounters_Object((1,3,6,1,4,1,45,5,46,1,28,2),_AvFabricAttachStatsClearGlobalErrorCounters_Type())
avFabricAttachStatsClearGlobalErrorCounters.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachStatsClearGlobalErrorCounters.setStatus(_A)
class _AvFabricAttachStatsClearPortErrorCounters_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AvFabricAttachStatsClearPortErrorCounters_Type.__name__=_B
_AvFabricAttachStatsClearPortErrorCounters_Object=MibScalar
avFabricAttachStatsClearPortErrorCounters=_AvFabricAttachStatsClearPortErrorCounters_Object((1,3,6,1,4,1,45,5,46,1,28,3),_AvFabricAttachStatsClearPortErrorCounters_Type())
avFabricAttachStatsClearPortErrorCounters.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachStatsClearPortErrorCounters.setStatus(_A)
_AvFabricAttachZeroTouchClientAttachTable_Object=MibTable
avFabricAttachZeroTouchClientAttachTable=_AvFabricAttachZeroTouchClientAttachTable_Object((1,3,6,1,4,1,45,5,46,1,29))
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientAttachTable.setStatus(_A)
_AvFabricAttachZeroTouchClientAttachEntry_Object=MibTableRow
avFabricAttachZeroTouchClientAttachEntry=_AvFabricAttachZeroTouchClientAttachEntry_Object((1,3,6,1,4,1,45,5,46,1,29,1))
avFabricAttachZeroTouchClientAttachEntry.setIndexNames((0,_E,_A8))
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientAttachEntry.setStatus(_A)
class _AvFabricAttachZeroTouchClientAttachType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AvFabricAttachZeroTouchClientAttachType_Type.__name__=_B
_AvFabricAttachZeroTouchClientAttachType_Object=MibTableColumn
avFabricAttachZeroTouchClientAttachType=_AvFabricAttachZeroTouchClientAttachType_Object((1,3,6,1,4,1,45,5,46,1,29,1,1),_AvFabricAttachZeroTouchClientAttachType_Type())
avFabricAttachZeroTouchClientAttachType.setMaxAccess(_H)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientAttachType.setStatus(_A)
class _AvFabricAttachZeroTouchClientAttachVlan_Type(Integer32):defaultValue=4096;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_AvFabricAttachZeroTouchClientAttachVlan_Type.__name__=_B
_AvFabricAttachZeroTouchClientAttachVlan_Object=MibTableColumn
avFabricAttachZeroTouchClientAttachVlan=_AvFabricAttachZeroTouchClientAttachVlan_Object((1,3,6,1,4,1,45,5,46,1,29,1,2),_AvFabricAttachZeroTouchClientAttachVlan_Type())
avFabricAttachZeroTouchClientAttachVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientAttachVlan.setStatus(_A)
class _AvFabricAttachZeroTouchClientAttachPortPriority_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_AvFabricAttachZeroTouchClientAttachPortPriority_Type.__name__=_B
_AvFabricAttachZeroTouchClientAttachPortPriority_Object=MibTableColumn
avFabricAttachZeroTouchClientAttachPortPriority=_AvFabricAttachZeroTouchClientAttachPortPriority_Object((1,3,6,1,4,1,45,5,46,1,29,1,3),_AvFabricAttachZeroTouchClientAttachPortPriority_Type())
avFabricAttachZeroTouchClientAttachPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientAttachPortPriority.setStatus(_A)
class _AvFabricAttachZeroTouchClientAttachIsid_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777214))
_AvFabricAttachZeroTouchClientAttachIsid_Type.__name__=_B
_AvFabricAttachZeroTouchClientAttachIsid_Object=MibTableColumn
avFabricAttachZeroTouchClientAttachIsid=_AvFabricAttachZeroTouchClientAttachIsid_Object((1,3,6,1,4,1,45,5,46,1,29,1,4),_AvFabricAttachZeroTouchClientAttachIsid_Type())
avFabricAttachZeroTouchClientAttachIsid.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientAttachIsid.setStatus(_A)
_AvFabricAttachZeroTouchClientAttachRowStatus_Type=RowStatus
_AvFabricAttachZeroTouchClientAttachRowStatus_Object=MibTableColumn
avFabricAttachZeroTouchClientAttachRowStatus=_AvFabricAttachZeroTouchClientAttachRowStatus_Object((1,3,6,1,4,1,45,5,46,1,29,1,5),_AvFabricAttachZeroTouchClientAttachRowStatus_Type())
avFabricAttachZeroTouchClientAttachRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientAttachRowStatus.setStatus(_A)
class _AvFabricAttachZeroTouchClientAttachExcludeStatic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('keepStaticVlans',1),('removeStaticVlans',2)))
_AvFabricAttachZeroTouchClientAttachExcludeStatic_Type.__name__=_B
_AvFabricAttachZeroTouchClientAttachExcludeStatic_Object=MibTableColumn
avFabricAttachZeroTouchClientAttachExcludeStatic=_AvFabricAttachZeroTouchClientAttachExcludeStatic_Object((1,3,6,1,4,1,45,5,46,1,29,1,6),_AvFabricAttachZeroTouchClientAttachExcludeStatic_Type())
avFabricAttachZeroTouchClientAttachExcludeStatic.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientAttachExcludeStatic.setStatus(_A)
class _AvFabricAttachZeroTouchClientAttachIsidName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AvFabricAttachZeroTouchClientAttachIsidName_Type.__name__=_P
_AvFabricAttachZeroTouchClientAttachIsidName_Object=MibTableColumn
avFabricAttachZeroTouchClientAttachIsidName=_AvFabricAttachZeroTouchClientAttachIsidName_Object((1,3,6,1,4,1,45,5,46,1,29,1,7),_AvFabricAttachZeroTouchClientAttachIsidName_Type())
avFabricAttachZeroTouchClientAttachIsidName.setMaxAccess(_C)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientAttachIsidName.setStatus(_A)
_AvFabricAttachZeroTouchClientDetectTable_Object=MibTable
avFabricAttachZeroTouchClientDetectTable=_AvFabricAttachZeroTouchClientDetectTable_Object((1,3,6,1,4,1,45,5,46,1,30))
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientDetectTable.setStatus(_A)
_AvFabricAttachZeroTouchClientDetectEntry_Object=MibTableRow
avFabricAttachZeroTouchClientDetectEntry=_AvFabricAttachZeroTouchClientDetectEntry_Object((1,3,6,1,4,1,45,5,46,1,30,1))
avFabricAttachZeroTouchClientDetectEntry.setIndexNames((0,_E,_A9),(0,_E,_AA))
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientDetectEntry.setStatus(_A)
class _AvFabricAttachZeroTouchClientDetectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AvFabricAttachZeroTouchClientDetectType_Type.__name__=_B
_AvFabricAttachZeroTouchClientDetectType_Object=MibTableColumn
avFabricAttachZeroTouchClientDetectType=_AvFabricAttachZeroTouchClientDetectType_Object((1,3,6,1,4,1,45,5,46,1,30,1,1),_AvFabricAttachZeroTouchClientDetectType_Type())
avFabricAttachZeroTouchClientDetectType.setMaxAccess(_H)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientDetectType.setStatus(_A)
class _AvFabricAttachZeroTouchClientDetectMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('lldpChassisIdMac',1),('lldpChassisIdString',2),('lldpSystemDescrString',3),('lldpMgmtAddrIPv4',4)))
_AvFabricAttachZeroTouchClientDetectMethod_Type.__name__=_B
_AvFabricAttachZeroTouchClientDetectMethod_Object=MibTableColumn
avFabricAttachZeroTouchClientDetectMethod=_AvFabricAttachZeroTouchClientDetectMethod_Object((1,3,6,1,4,1,45,5,46,1,30,1,2),_AvFabricAttachZeroTouchClientDetectMethod_Type())
avFabricAttachZeroTouchClientDetectMethod.setMaxAccess(_H)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientDetectMethod.setStatus(_A)
class _AvFabricAttachZeroTouchClientDetectData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_AvFabricAttachZeroTouchClientDetectData_Type.__name__=_J
_AvFabricAttachZeroTouchClientDetectData_Object=MibTableColumn
avFabricAttachZeroTouchClientDetectData=_AvFabricAttachZeroTouchClientDetectData_Object((1,3,6,1,4,1,45,5,46,1,30,1,3),_AvFabricAttachZeroTouchClientDetectData_Type())
avFabricAttachZeroTouchClientDetectData.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientDetectData.setStatus(_A)
class _AvFabricAttachZeroTouchClientDetectElementType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AvFabricAttachZeroTouchClientDetectElementType_Type.__name__=_B
_AvFabricAttachZeroTouchClientDetectElementType_Object=MibTableColumn
avFabricAttachZeroTouchClientDetectElementType=_AvFabricAttachZeroTouchClientDetectElementType_Object((1,3,6,1,4,1,45,5,46,1,30,1,4),_AvFabricAttachZeroTouchClientDetectElementType_Type())
avFabricAttachZeroTouchClientDetectElementType.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientDetectElementType.setStatus(_A)
class _AvFabricAttachZeroTouchClientDetectLogicOper_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('and',1),('or',2)))
_AvFabricAttachZeroTouchClientDetectLogicOper_Type.__name__=_B
_AvFabricAttachZeroTouchClientDetectLogicOper_Object=MibTableColumn
avFabricAttachZeroTouchClientDetectLogicOper=_AvFabricAttachZeroTouchClientDetectLogicOper_Object((1,3,6,1,4,1,45,5,46,1,30,1,5),_AvFabricAttachZeroTouchClientDetectLogicOper_Type())
avFabricAttachZeroTouchClientDetectLogicOper.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientDetectLogicOper.setStatus(_A)
_AvFabricAttachZeroTouchClientDetectRowStatus_Type=RowStatus
_AvFabricAttachZeroTouchClientDetectRowStatus_Object=MibTableColumn
avFabricAttachZeroTouchClientDetectRowStatus=_AvFabricAttachZeroTouchClientDetectRowStatus_Object((1,3,6,1,4,1,45,5,46,1,30,1,6),_AvFabricAttachZeroTouchClientDetectRowStatus_Type())
avFabricAttachZeroTouchClientDetectRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:avFabricAttachZeroTouchClientDetectRowStatus.setStatus(_A)
class _AvFabricAttachZeroTouchMgmtVlanDist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AvFabricAttachZeroTouchMgmtVlanDist_Type.__name__=_B
_AvFabricAttachZeroTouchMgmtVlanDist_Object=MibScalar
avFabricAttachZeroTouchMgmtVlanDist=_AvFabricAttachZeroTouchMgmtVlanDist_Object((1,3,6,1,4,1,45,5,46,1,31),_AvFabricAttachZeroTouchMgmtVlanDist_Type())
avFabricAttachZeroTouchMgmtVlanDist.setMaxAccess(_F)
if mibBuilder.loadTexts:avFabricAttachZeroTouchMgmtVlanDist.setStatus(_A)
_AvFabricAttachNotifyObjects_ObjectIdentity=ObjectIdentity
avFabricAttachNotifyObjects=_AvFabricAttachNotifyObjects_ObjectIdentity((1,3,6,1,4,1,45,5,46,2))
class _AvFabricAttachDiscElemsSysDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AvFabricAttachDiscElemsSysDescr_Type.__name__=_K
_AvFabricAttachDiscElemsSysDescr_Object=MibScalar
avFabricAttachDiscElemsSysDescr=_AvFabricAttachDiscElemsSysDescr_Object((1,3,6,1,4,1,45,5,46,2,1),_AvFabricAttachDiscElemsSysDescr_Type())
avFabricAttachDiscElemsSysDescr.setMaxAccess(_AB)
if mibBuilder.loadTexts:avFabricAttachDiscElemsSysDescr.setStatus(_A)
_AvFabricAttachDiscElemsMgmtOid_Type=ObjectIdentifier
_AvFabricAttachDiscElemsMgmtOid_Object=MibScalar
avFabricAttachDiscElemsMgmtOid=_AvFabricAttachDiscElemsMgmtOid_Object((1,3,6,1,4,1,45,5,46,2,2),_AvFabricAttachDiscElemsMgmtOid_Type())
avFabricAttachDiscElemsMgmtOid.setMaxAccess(_AB)
if mibBuilder.loadTexts:avFabricAttachDiscElemsMgmtOid.setStatus(_A)
avFabricAttachDiscoveredElement=NotificationType((1,3,6,1,4,1,45,5,46,0,1))
avFabricAttachDiscoveredElement.setObjects(*((_E,_S),(_E,_T),(_E,_AC),(_E,_AD),(_E,_AE)))
if mibBuilder.loadTexts:avFabricAttachDiscoveredElement.setStatus(_A)
avFabricAttachExpiredElement=NotificationType((1,3,6,1,4,1,45,5,46,0,2))
avFabricAttachExpiredElement.setObjects(*((_E,_S),(_E,_T)))
if mibBuilder.loadTexts:avFabricAttachExpiredElement.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'avayaFabricAttachMib':avayaFabricAttachMib,'avFabricAttachNotifications':avFabricAttachNotifications,'avFabricAttachDiscoveredElement':avFabricAttachDiscoveredElement,'avFabricAttachExpiredElement':avFabricAttachExpiredElement,'avFabricAttachObjects':avFabricAttachObjects,'avFabricAttachService':avFabricAttachService,'avFabricAttachElementType':avFabricAttachElementType,'avFabricAttachPrimaryServerId':avFabricAttachPrimaryServerId,'avFabricAttachPrimaryServerDescr':avFabricAttachPrimaryServerDescr,'avFabricAttachIsidVlanAsgnsTable':avFabricAttachIsidVlanAsgnsTable,'avFabricAttachIsidVlanAsgnsEntry':avFabricAttachIsidVlanAsgnsEntry,_j:avFabricAttachIsidVlanAsgnsIfIndex,_k:avFabricAttachIsidVlanAsgnsIsid,_l:avFabricAttachIsidVlanAsgnsVlan,'avFabricAttachIsidVlanAsgnsState':avFabricAttachIsidVlanAsgnsState,'avFabricAttachIsidVlanAsgnsRowStatus':avFabricAttachIsidVlanAsgnsRowStatus,'avFabricAttachIsidVlanAsgnsOrigin':avFabricAttachIsidVlanAsgnsOrigin,'avFabricAttachIsidVlanAsgnsIsidName':avFabricAttachIsidVlanAsgnsIsidName,'avFabricAttachPortTable':avFabricAttachPortTable,'avFabricAttachPortEntry':avFabricAttachPortEntry,_m:avFabricAttachPortIfIndex,'avFabricAttachPortState':avFabricAttachPortState,'avFabricAttachPortRowStatus':avFabricAttachPortRowStatus,'avFabricAttachPortMsgAuthStatus':avFabricAttachPortMsgAuthStatus,'avFabricAttachPortMsgAuthKey':avFabricAttachPortMsgAuthKey,'avFabricAttachPortMgmtIsid':avFabricAttachPortMgmtIsid,'avFabricAttachPortMgmtCvid':avFabricAttachPortMgmtCvid,'avFabricAttachPortMsgAuthKeymode':avFabricAttachPortMsgAuthKeymode,'avFabricAttachPortOrigin':avFabricAttachPortOrigin,'avFabricAttachZeroTouchService':avFabricAttachZeroTouchService,'avFabricAttachMsgAuthStatus':avFabricAttachMsgAuthStatus,'avFabricAttachMsgAuthKey':avFabricAttachMsgAuthKey,'avFabricAttachClientProxyStatus':avFabricAttachClientProxyStatus,'avFabricAttachDiscElemsTable':avFabricAttachDiscElemsTable,'avFabricAttachDiscElemsEntry':avFabricAttachDiscElemsEntry,_o:avFabricAttachDiscElemsIfIndex,_S:avFabricAttachDiscElemsElementType,'avFabricAttachDiscElemsElementVlan':avFabricAttachDiscElemsElementVlan,_T:avFabricAttachDiscElemsElementId,'avFabricAttachDiscElemsElementState':avFabricAttachDiscElemsElementState,_AC:avFabricAttachDiscElemsElementAuth,'avFabricAttachDiscElemsElementTrunkId':avFabricAttachDiscElemsElementTrunkId,'avFabricAttachDiscElemsElementOperAuthStatus':avFabricAttachDiscElemsElementOperAuthStatus,'avFabricAttachDiscElemsElementAsgnsOperAuthStatus':avFabricAttachDiscElemsElementAsgnsOperAuthStatus,'avFabricAttachDiscElemsAsgnsAuth':avFabricAttachDiscElemsAsgnsAuth,'avFabricAttachAutoProvision':avFabricAttachAutoProvision,'avFabricAttachProvisionMode':avFabricAttachProvisionMode,'avFabricAttachZeroTouchOptionFlags':avFabricAttachZeroTouchOptionFlags,'avFabricAttachZeroTouchNsvTable':avFabricAttachZeroTouchNsvTable,'avFabricAttachZeroTouchNsvEntry':avFabricAttachZeroTouchNsvEntry,_A5:avFabricAttachZeroTouchNsvType,'avFabricAttachZeroTouchNsvVlan':avFabricAttachZeroTouchNsvVlan,'avFabricAttachZeroTouchNsvPortPriority':avFabricAttachZeroTouchNsvPortPriority,'avFabricAttachZeroTouchNsvStateFlags':avFabricAttachZeroTouchNsvStateFlags,'avFabricAttachZeroTouchNsvRowStatus':avFabricAttachZeroTouchNsvRowStatus,'avFabricAttachZeroTouchNsvIsid':avFabricAttachZeroTouchNsvIsid,'avFabricAttachZeroTouchRadiusPriSrvrIpv4Addr':avFabricAttachZeroTouchRadiusPriSrvrIpv4Addr,'avFabricAttachZeroTouchRadiusSecSrvrIpv4Addr':avFabricAttachZeroTouchRadiusSecSrvrIpv4Addr,'avFabricAttachZeroTouchRadiusTimeout':avFabricAttachZeroTouchRadiusTimeout,'avFabricAttachStandaloneProxy':avFabricAttachStandaloneProxy,'avFabricAttachStaticUplinkIfIndex':avFabricAttachStaticUplinkIfIndex,'avFabricAttachStaticUplinkTrunk':avFabricAttachStaticUplinkTrunk,'avFabricAttachAsgnTimeout':avFabricAttachAsgnTimeout,'avFabricAttachStatsTable':avFabricAttachStatsTable,'avFabricAttachStatsEntry':avFabricAttachStatsEntry,_A6:avFabricAttachStatsPortIndex,'avFabricAttachStatsDiscElemReceived':avFabricAttachStatsDiscElemReceived,'avFabricAttachStatsAsgnReceived':avFabricAttachStatsAsgnReceived,'avFabricAttachStatsAsgnAccepted':avFabricAttachStatsAsgnAccepted,'avFabricAttachStatsAsgnRejected':avFabricAttachStatsAsgnRejected,'avFabricAttachStatsAsgnExpired':avFabricAttachStatsAsgnExpired,'avFabricAttachStatsDiscAuthFailed':avFabricAttachStatsDiscAuthFailed,'avFabricAttachStatsDiscElemExpired':avFabricAttachStatsDiscElemExpired,'avFabricAttachStatsDiscElemDeleted':avFabricAttachStatsDiscElemDeleted,'avFabricAttachStatsAsgnDeleted':avFabricAttachStatsAsgnDeleted,'avFabricAttachStatsAsgnAuthFailed':avFabricAttachStatsAsgnAuthFailed,'avFabricAttachGlobalStats':avFabricAttachGlobalStats,'avFabricAttachGlobalStatsDiscElemReceived':avFabricAttachGlobalStatsDiscElemReceived,'avFabricAttachGlobalStatsAsgnReceived':avFabricAttachGlobalStatsAsgnReceived,'avFabricAttachGlobalStatsAsgnAccepted':avFabricAttachGlobalStatsAsgnAccepted,'avFabricAttachGlobalStatsAsgnRejected':avFabricAttachGlobalStatsAsgnRejected,'avFabricAttachGlobalStatsAsgnExpired':avFabricAttachGlobalStatsAsgnExpired,'avFabricAttachGlobalStatsDiscAuthFailed':avFabricAttachGlobalStatsDiscAuthFailed,'avFabricAttachGlobalStatsDiscElemExpired':avFabricAttachGlobalStatsDiscElemExpired,'avFabricAttachGlobalStatsDiscElemDeleted':avFabricAttachGlobalStatsDiscElemDeleted,'avFabricAttachGlobalStatsAsgnDeleted':avFabricAttachGlobalStatsAsgnDeleted,'avFabricAttachGlobalStatsAsgnAuthFailed':avFabricAttachGlobalStatsAsgnAuthFailed,'avFabricAttachGlobalStatsCurReceivedBindings':avFabricAttachGlobalStatsCurReceivedBindings,'avFabricAttachGlobalStatsCurAdvertisedBindings':avFabricAttachGlobalStatsCurAdvertisedBindings,'avFabricAttachExtendedLogging':avFabricAttachExtendedLogging,'avFabricAttachDiscTimeout':avFabricAttachDiscTimeout,'avFabricAttachZeroTouchClientTable':avFabricAttachZeroTouchClientTable,'avFabricAttachZeroTouchClientEntry':avFabricAttachZeroTouchClientEntry,_A7:avFabricAttachZeroTouchClientType,'avFabricAttachZeroTouchClientDescr':avFabricAttachZeroTouchClientDescr,'avFabricAttachZeroTouchClientOptionFlags':avFabricAttachZeroTouchClientOptionFlags,'avFabricAttachZeroTouchClientRowStatus':avFabricAttachZeroTouchClientRowStatus,'avFabricAttachZeroTouchClientName':avFabricAttachZeroTouchClientName,'avFabricAttachZeroTouchClientOrigin':avFabricAttachZeroTouchClientOrigin,'avFabricAttachStats':avFabricAttachStats,'avFabricAttachStatsClearErrorCounters':avFabricAttachStatsClearErrorCounters,'avFabricAttachStatsClearGlobalErrorCounters':avFabricAttachStatsClearGlobalErrorCounters,'avFabricAttachStatsClearPortErrorCounters':avFabricAttachStatsClearPortErrorCounters,'avFabricAttachZeroTouchClientAttachTable':avFabricAttachZeroTouchClientAttachTable,'avFabricAttachZeroTouchClientAttachEntry':avFabricAttachZeroTouchClientAttachEntry,_A8:avFabricAttachZeroTouchClientAttachType,'avFabricAttachZeroTouchClientAttachVlan':avFabricAttachZeroTouchClientAttachVlan,'avFabricAttachZeroTouchClientAttachPortPriority':avFabricAttachZeroTouchClientAttachPortPriority,'avFabricAttachZeroTouchClientAttachIsid':avFabricAttachZeroTouchClientAttachIsid,'avFabricAttachZeroTouchClientAttachRowStatus':avFabricAttachZeroTouchClientAttachRowStatus,'avFabricAttachZeroTouchClientAttachExcludeStatic':avFabricAttachZeroTouchClientAttachExcludeStatic,'avFabricAttachZeroTouchClientAttachIsidName':avFabricAttachZeroTouchClientAttachIsidName,'avFabricAttachZeroTouchClientDetectTable':avFabricAttachZeroTouchClientDetectTable,'avFabricAttachZeroTouchClientDetectEntry':avFabricAttachZeroTouchClientDetectEntry,_A9:avFabricAttachZeroTouchClientDetectType,_AA:avFabricAttachZeroTouchClientDetectMethod,'avFabricAttachZeroTouchClientDetectData':avFabricAttachZeroTouchClientDetectData,'avFabricAttachZeroTouchClientDetectElementType':avFabricAttachZeroTouchClientDetectElementType,'avFabricAttachZeroTouchClientDetectLogicOper':avFabricAttachZeroTouchClientDetectLogicOper,'avFabricAttachZeroTouchClientDetectRowStatus':avFabricAttachZeroTouchClientDetectRowStatus,'avFabricAttachZeroTouchMgmtVlanDist':avFabricAttachZeroTouchMgmtVlanDist,'avFabricAttachNotifyObjects':avFabricAttachNotifyObjects,_AD:avFabricAttachDiscElemsSysDescr,_AE:avFabricAttachDiscElemsMgmtOid})