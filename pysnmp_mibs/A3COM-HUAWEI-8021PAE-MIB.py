_O='proxycheckUsrName'
_N='proxycheckIpaddr'
_M='proxycheckMacAddr'
_L='proxycheckPortName'
_K='proxycheckVlanId'
_J='dot1xPaePortNumber'
_I='IEEE8021-PAE-MIB'
_H='disabled'
_G='enabled'
_F='accessible-for-notify'
_E='A3COM-HUAWEI-8021PAE-MIB'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huaweiMgmt,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huaweiMgmt')
dot1xPaePortNumber,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hwpaeExtMib=ModuleIdentity((1,3,6,1,4,1,43,45,1,5,22))
if mibBuilder.loadTexts:hwpaeExtMib.setRevisions(('2001-06-29 00:00',))
_HwpaeExtMibObjects_ObjectIdentity=ObjectIdentity
hwpaeExtMibObjects=_HwpaeExtMibObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,22,1))
_Hwdot1xPaeTraps_ObjectIdentity=ObjectIdentity
hwdot1xPaeTraps=_Hwdot1xPaeTraps_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,22,1,0))
_ProxycheckVlanId_Type=Integer32
_ProxycheckVlanId_Object=MibScalar
proxycheckVlanId=_ProxycheckVlanId_Object((1,3,6,1,4,1,43,45,1,5,22,1,0,2),_ProxycheckVlanId_Type())
proxycheckVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:proxycheckVlanId.setStatus(_A)
_ProxycheckPortName_Type=OctetString
_ProxycheckPortName_Object=MibScalar
proxycheckPortName=_ProxycheckPortName_Object((1,3,6,1,4,1,43,45,1,5,22,1,0,3),_ProxycheckPortName_Type())
proxycheckPortName.setMaxAccess(_F)
if mibBuilder.loadTexts:proxycheckPortName.setStatus(_A)
_ProxycheckMacAddr_Type=MacAddress
_ProxycheckMacAddr_Object=MibScalar
proxycheckMacAddr=_ProxycheckMacAddr_Object((1,3,6,1,4,1,43,45,1,5,22,1,0,4),_ProxycheckMacAddr_Type())
proxycheckMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:proxycheckMacAddr.setStatus(_A)
_ProxycheckIpaddr_Type=IpAddress
_ProxycheckIpaddr_Object=MibScalar
proxycheckIpaddr=_ProxycheckIpaddr_Object((1,3,6,1,4,1,43,45,1,5,22,1,0,5),_ProxycheckIpaddr_Type())
proxycheckIpaddr.setMaxAccess(_F)
if mibBuilder.loadTexts:proxycheckIpaddr.setStatus(_A)
_ProxycheckUsrName_Type=OctetString
_ProxycheckUsrName_Object=MibScalar
proxycheckUsrName=_ProxycheckUsrName_Object((1,3,6,1,4,1,43,45,1,5,22,1,0,6),_ProxycheckUsrName_Type())
proxycheckUsrName.setMaxAccess(_F)
if mibBuilder.loadTexts:proxycheckUsrName.setStatus(_A)
_Hwdot1xPaeSystem_ObjectIdentity=ObjectIdentity
hwdot1xPaeSystem=_Hwdot1xPaeSystem_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,22,1,1))
class _Hwdot1xAuthQuietPeriod_Type(Unsigned32):defaultValue=60
_Hwdot1xAuthQuietPeriod_Type.__name__=_D
_Hwdot1xAuthQuietPeriod_Object=MibScalar
hwdot1xAuthQuietPeriod=_Hwdot1xAuthQuietPeriod_Object((1,3,6,1,4,1,43,45,1,5,22,1,1,1),_Hwdot1xAuthQuietPeriod_Type())
hwdot1xAuthQuietPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xAuthQuietPeriod.setStatus(_A)
class _Hwdot1xAuthTxPeriod_Type(Unsigned32):defaultValue=30
_Hwdot1xAuthTxPeriod_Type.__name__=_D
_Hwdot1xAuthTxPeriod_Object=MibScalar
hwdot1xAuthTxPeriod=_Hwdot1xAuthTxPeriod_Object((1,3,6,1,4,1,43,45,1,5,22,1,1,2),_Hwdot1xAuthTxPeriod_Type())
hwdot1xAuthTxPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xAuthTxPeriod.setStatus(_A)
class _Hwdot1xAuthSuppTimeout_Type(Unsigned32):defaultValue=30
_Hwdot1xAuthSuppTimeout_Type.__name__=_D
_Hwdot1xAuthSuppTimeout_Object=MibScalar
hwdot1xAuthSuppTimeout=_Hwdot1xAuthSuppTimeout_Object((1,3,6,1,4,1,43,45,1,5,22,1,1,3),_Hwdot1xAuthSuppTimeout_Type())
hwdot1xAuthSuppTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xAuthSuppTimeout.setStatus(_A)
class _Hwdot1xAuthServerTimeout_Type(Unsigned32):defaultValue=100
_Hwdot1xAuthServerTimeout_Type.__name__=_D
_Hwdot1xAuthServerTimeout_Object=MibScalar
hwdot1xAuthServerTimeout=_Hwdot1xAuthServerTimeout_Object((1,3,6,1,4,1,43,45,1,5,22,1,1,4),_Hwdot1xAuthServerTimeout_Type())
hwdot1xAuthServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xAuthServerTimeout.setStatus(_A)
class _Hwdot1xAuthMaxReq_Type(Unsigned32):defaultValue=2
_Hwdot1xAuthMaxReq_Type.__name__=_D
_Hwdot1xAuthMaxReq_Object=MibScalar
hwdot1xAuthMaxReq=_Hwdot1xAuthMaxReq_Object((1,3,6,1,4,1,43,45,1,5,22,1,1,5),_Hwdot1xAuthMaxReq_Type())
hwdot1xAuthMaxReq.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xAuthMaxReq.setStatus(_A)
class _Hwdot1xAuthReAuthPeriod_Type(Unsigned32):defaultValue=3600
_Hwdot1xAuthReAuthPeriod_Type.__name__=_D
_Hwdot1xAuthReAuthPeriod_Object=MibScalar
hwdot1xAuthReAuthPeriod=_Hwdot1xAuthReAuthPeriod_Object((1,3,6,1,4,1,43,45,1,5,22,1,1,6),_Hwdot1xAuthReAuthPeriod_Type())
hwdot1xAuthReAuthPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xAuthReAuthPeriod.setStatus(_A)
class _Hwdot1xAuthMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('chap',1),('pap',2),('eap',3)))
_Hwdot1xAuthMethod_Type.__name__=_C
_Hwdot1xAuthMethod_Object=MibScalar
hwdot1xAuthMethod=_Hwdot1xAuthMethod_Object((1,3,6,1,4,1,43,45,1,5,22,1,1,7),_Hwdot1xAuthMethod_Type())
hwdot1xAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xAuthMethod.setStatus(_A)
_Hwdot1xPaeAuthenticator_ObjectIdentity=ObjectIdentity
hwdot1xPaeAuthenticator=_Hwdot1xPaeAuthenticator_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,22,1,2))
_Hwdot1xAuthConfigExtTable_Object=MibTable
hwdot1xAuthConfigExtTable=_Hwdot1xAuthConfigExtTable_Object((1,3,6,1,4,1,43,45,1,5,22,1,2,1))
if mibBuilder.loadTexts:hwdot1xAuthConfigExtTable.setStatus(_A)
_Hwdot1xAuthConfigExtEntry_Object=MibTableRow
hwdot1xAuthConfigExtEntry=_Hwdot1xAuthConfigExtEntry_Object((1,3,6,1,4,1,43,45,1,5,22,1,2,1,1))
hwdot1xAuthConfigExtEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hwdot1xAuthConfigExtEntry.setStatus(_A)
class _Hwdot1xpaeportAuthAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Hwdot1xpaeportAuthAdminStatus_Type.__name__=_C
_Hwdot1xpaeportAuthAdminStatus_Object=MibTableColumn
hwdot1xpaeportAuthAdminStatus=_Hwdot1xpaeportAuthAdminStatus_Object((1,3,6,1,4,1,43,45,1,5,22,1,2,1,1,1),_Hwdot1xpaeportAuthAdminStatus_Type())
hwdot1xpaeportAuthAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xpaeportAuthAdminStatus.setStatus(_A)
class _Hwdot1xpaeportControlledType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('mac',2)))
_Hwdot1xpaeportControlledType_Type.__name__=_C
_Hwdot1xpaeportControlledType_Object=MibTableColumn
hwdot1xpaeportControlledType=_Hwdot1xpaeportControlledType_Object((1,3,6,1,4,1,43,45,1,5,22,1,2,1,1,2),_Hwdot1xpaeportControlledType_Type())
hwdot1xpaeportControlledType.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xpaeportControlledType.setStatus(_A)
class _Hwdot1xpaeportMaxUserNum_Type(Integer32):defaultValue=256
_Hwdot1xpaeportMaxUserNum_Type.__name__=_C
_Hwdot1xpaeportMaxUserNum_Object=MibTableColumn
hwdot1xpaeportMaxUserNum=_Hwdot1xpaeportMaxUserNum_Object((1,3,6,1,4,1,43,45,1,5,22,1,2,1,1,3),_Hwdot1xpaeportMaxUserNum_Type())
hwdot1xpaeportMaxUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xpaeportMaxUserNum.setStatus(_A)
_Hwdot1xpaeportUserNumNow_Type=Integer32
_Hwdot1xpaeportUserNumNow_Object=MibTableColumn
hwdot1xpaeportUserNumNow=_Hwdot1xpaeportUserNumNow_Object((1,3,6,1,4,1,43,45,1,5,22,1,2,1,1,4),_Hwdot1xpaeportUserNumNow_Type())
hwdot1xpaeportUserNumNow.setMaxAccess('read-only')
if mibBuilder.loadTexts:hwdot1xpaeportUserNumNow.setStatus(_A)
class _Hwdot1xpaeportClearStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_Hwdot1xpaeportClearStatistics_Type.__name__=_C
_Hwdot1xpaeportClearStatistics_Object=MibTableColumn
hwdot1xpaeportClearStatistics=_Hwdot1xpaeportClearStatistics_Object((1,3,6,1,4,1,43,45,1,5,22,1,2,1,1,5),_Hwdot1xpaeportClearStatistics_Type())
hwdot1xpaeportClearStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xpaeportClearStatistics.setStatus(_A)
class _Hwdot1xpaeportMcastTrigStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Hwdot1xpaeportMcastTrigStatus_Type.__name__=_C
_Hwdot1xpaeportMcastTrigStatus_Object=MibTableColumn
hwdot1xpaeportMcastTrigStatus=_Hwdot1xpaeportMcastTrigStatus_Object((1,3,6,1,4,1,43,45,1,5,22,1,2,1,1,6),_Hwdot1xpaeportMcastTrigStatus_Type())
hwdot1xpaeportMcastTrigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xpaeportMcastTrigStatus.setStatus(_A)
class _Hwdot1xpaeportHandshakeStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Hwdot1xpaeportHandshakeStatus_Type.__name__=_C
_Hwdot1xpaeportHandshakeStatus_Object=MibTableColumn
hwdot1xpaeportHandshakeStatus=_Hwdot1xpaeportHandshakeStatus_Object((1,3,6,1,4,1,43,45,1,5,22,1,2,1,1,7),_Hwdot1xpaeportHandshakeStatus_Type())
hwdot1xpaeportHandshakeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hwdot1xpaeportHandshakeStatus.setStatus(_A)
supplicantproxycheck=NotificationType((1,3,6,1,4,1,43,45,1,5,22,1,0,1))
supplicantproxycheck.setObjects(*((_E,_K),(_E,_L),(_E,_M),(_E,_N),(_E,_O)))
if mibBuilder.loadTexts:supplicantproxycheck.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hwpaeExtMib':hwpaeExtMib,'hwpaeExtMibObjects':hwpaeExtMibObjects,'hwdot1xPaeTraps':hwdot1xPaeTraps,'supplicantproxycheck':supplicantproxycheck,_K:proxycheckVlanId,_L:proxycheckPortName,_M:proxycheckMacAddr,_N:proxycheckIpaddr,_O:proxycheckUsrName,'hwdot1xPaeSystem':hwdot1xPaeSystem,'hwdot1xAuthQuietPeriod':hwdot1xAuthQuietPeriod,'hwdot1xAuthTxPeriod':hwdot1xAuthTxPeriod,'hwdot1xAuthSuppTimeout':hwdot1xAuthSuppTimeout,'hwdot1xAuthServerTimeout':hwdot1xAuthServerTimeout,'hwdot1xAuthMaxReq':hwdot1xAuthMaxReq,'hwdot1xAuthReAuthPeriod':hwdot1xAuthReAuthPeriod,'hwdot1xAuthMethod':hwdot1xAuthMethod,'hwdot1xPaeAuthenticator':hwdot1xPaeAuthenticator,'hwdot1xAuthConfigExtTable':hwdot1xAuthConfigExtTable,'hwdot1xAuthConfigExtEntry':hwdot1xAuthConfigExtEntry,'hwdot1xpaeportAuthAdminStatus':hwdot1xpaeportAuthAdminStatus,'hwdot1xpaeportControlledType':hwdot1xpaeportControlledType,'hwdot1xpaeportMaxUserNum':hwdot1xpaeportMaxUserNum,'hwdot1xpaeportUserNumNow':hwdot1xpaeportUserNumNow,'hwdot1xpaeportClearStatistics':hwdot1xpaeportClearStatistics,'hwdot1xpaeportMcastTrigStatus':hwdot1xpaeportMcastTrigStatus,'hwdot1xpaeportHandshakeStatus':hwdot1xpaeportHandshakeStatus})