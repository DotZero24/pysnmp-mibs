_O='hpnicfproxycheckUsrName'
_N='hpnicfproxycheckIpaddr'
_M='hpnicfproxycheckMacAddr'
_L='hpnicfproxycheckPortName'
_K='hpnicfproxycheckVlanId'
_J='dot1xPaePortNumber'
_I='IEEE8021-PAE-MIB'
_H='disabled'
_G='enabled'
_F='accessible-for-notify'
_E='HPN-ICF-8021PAE-MIB'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfRhw,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRhw')
dot1xPaePortNumber,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hpnicfpaeExtMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,6))
if mibBuilder.loadTexts:hpnicfpaeExtMib.setRevisions(('2001-06-29 00:00',))
_HpnicfpaeExtMibObjects_ObjectIdentity=ObjectIdentity
hpnicfpaeExtMibObjects=_HpnicfpaeExtMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,6,1))
_Hpnicfdot1xPaeTraps_ObjectIdentity=ObjectIdentity
hpnicfdot1xPaeTraps=_Hpnicfdot1xPaeTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,6,1,0))
_HpnicfproxycheckVlanId_Type=Integer32
_HpnicfproxycheckVlanId_Object=MibScalar
hpnicfproxycheckVlanId=_HpnicfproxycheckVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,0,2),_HpnicfproxycheckVlanId_Type())
hpnicfproxycheckVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfproxycheckVlanId.setStatus(_A)
_HpnicfproxycheckPortName_Type=OctetString
_HpnicfproxycheckPortName_Object=MibScalar
hpnicfproxycheckPortName=_HpnicfproxycheckPortName_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,0,3),_HpnicfproxycheckPortName_Type())
hpnicfproxycheckPortName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfproxycheckPortName.setStatus(_A)
_HpnicfproxycheckMacAddr_Type=MacAddress
_HpnicfproxycheckMacAddr_Object=MibScalar
hpnicfproxycheckMacAddr=_HpnicfproxycheckMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,0,4),_HpnicfproxycheckMacAddr_Type())
hpnicfproxycheckMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfproxycheckMacAddr.setStatus(_A)
_HpnicfproxycheckIpaddr_Type=IpAddress
_HpnicfproxycheckIpaddr_Object=MibScalar
hpnicfproxycheckIpaddr=_HpnicfproxycheckIpaddr_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,0,5),_HpnicfproxycheckIpaddr_Type())
hpnicfproxycheckIpaddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfproxycheckIpaddr.setStatus(_A)
_HpnicfproxycheckUsrName_Type=OctetString
_HpnicfproxycheckUsrName_Object=MibScalar
hpnicfproxycheckUsrName=_HpnicfproxycheckUsrName_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,0,6),_HpnicfproxycheckUsrName_Type())
hpnicfproxycheckUsrName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfproxycheckUsrName.setStatus(_A)
_Hpnicfdot1xPaeSystem_ObjectIdentity=ObjectIdentity
hpnicfdot1xPaeSystem=_Hpnicfdot1xPaeSystem_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,6,1,1))
class _Hpnicfdot1xAuthQuietPeriod_Type(Unsigned32):defaultValue=60
_Hpnicfdot1xAuthQuietPeriod_Type.__name__=_D
_Hpnicfdot1xAuthQuietPeriod_Object=MibScalar
hpnicfdot1xAuthQuietPeriod=_Hpnicfdot1xAuthQuietPeriod_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,1,1),_Hpnicfdot1xAuthQuietPeriod_Type())
hpnicfdot1xAuthQuietPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xAuthQuietPeriod.setStatus(_A)
class _Hpnicfdot1xAuthTxPeriod_Type(Unsigned32):defaultValue=30
_Hpnicfdot1xAuthTxPeriod_Type.__name__=_D
_Hpnicfdot1xAuthTxPeriod_Object=MibScalar
hpnicfdot1xAuthTxPeriod=_Hpnicfdot1xAuthTxPeriod_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,1,2),_Hpnicfdot1xAuthTxPeriod_Type())
hpnicfdot1xAuthTxPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xAuthTxPeriod.setStatus(_A)
class _Hpnicfdot1xAuthSuppTimeout_Type(Unsigned32):defaultValue=30
_Hpnicfdot1xAuthSuppTimeout_Type.__name__=_D
_Hpnicfdot1xAuthSuppTimeout_Object=MibScalar
hpnicfdot1xAuthSuppTimeout=_Hpnicfdot1xAuthSuppTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,1,3),_Hpnicfdot1xAuthSuppTimeout_Type())
hpnicfdot1xAuthSuppTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xAuthSuppTimeout.setStatus(_A)
class _Hpnicfdot1xAuthServerTimeout_Type(Unsigned32):defaultValue=100
_Hpnicfdot1xAuthServerTimeout_Type.__name__=_D
_Hpnicfdot1xAuthServerTimeout_Object=MibScalar
hpnicfdot1xAuthServerTimeout=_Hpnicfdot1xAuthServerTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,1,4),_Hpnicfdot1xAuthServerTimeout_Type())
hpnicfdot1xAuthServerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xAuthServerTimeout.setStatus(_A)
class _Hpnicfdot1xAuthMaxReq_Type(Unsigned32):defaultValue=2
_Hpnicfdot1xAuthMaxReq_Type.__name__=_D
_Hpnicfdot1xAuthMaxReq_Object=MibScalar
hpnicfdot1xAuthMaxReq=_Hpnicfdot1xAuthMaxReq_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,1,5),_Hpnicfdot1xAuthMaxReq_Type())
hpnicfdot1xAuthMaxReq.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xAuthMaxReq.setStatus(_A)
class _Hpnicfdot1xAuthReAuthPeriod_Type(Unsigned32):defaultValue=3600
_Hpnicfdot1xAuthReAuthPeriod_Type.__name__=_D
_Hpnicfdot1xAuthReAuthPeriod_Object=MibScalar
hpnicfdot1xAuthReAuthPeriod=_Hpnicfdot1xAuthReAuthPeriod_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,1,6),_Hpnicfdot1xAuthReAuthPeriod_Type())
hpnicfdot1xAuthReAuthPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xAuthReAuthPeriod.setStatus(_A)
class _Hpnicfdot1xAuthMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('chap',1),('pap',2),('eap',3)))
_Hpnicfdot1xAuthMethod_Type.__name__=_C
_Hpnicfdot1xAuthMethod_Object=MibScalar
hpnicfdot1xAuthMethod=_Hpnicfdot1xAuthMethod_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,1,7),_Hpnicfdot1xAuthMethod_Type())
hpnicfdot1xAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xAuthMethod.setStatus(_A)
_Hpnicfdot1xPaeAuthenticator_ObjectIdentity=ObjectIdentity
hpnicfdot1xPaeAuthenticator=_Hpnicfdot1xPaeAuthenticator_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,6,1,2))
_Hpnicfdot1xAuthConfigExtTable_Object=MibTable
hpnicfdot1xAuthConfigExtTable=_Hpnicfdot1xAuthConfigExtTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,2,1))
if mibBuilder.loadTexts:hpnicfdot1xAuthConfigExtTable.setStatus(_A)
_Hpnicfdot1xAuthConfigExtEntry_Object=MibTableRow
hpnicfdot1xAuthConfigExtEntry=_Hpnicfdot1xAuthConfigExtEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,2,1,1))
hpnicfdot1xAuthConfigExtEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hpnicfdot1xAuthConfigExtEntry.setStatus(_A)
class _Hpnicfdot1xpaeportAuthAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Hpnicfdot1xpaeportAuthAdminStatus_Type.__name__=_C
_Hpnicfdot1xpaeportAuthAdminStatus_Object=MibTableColumn
hpnicfdot1xpaeportAuthAdminStatus=_Hpnicfdot1xpaeportAuthAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,2,1,1,1),_Hpnicfdot1xpaeportAuthAdminStatus_Type())
hpnicfdot1xpaeportAuthAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xpaeportAuthAdminStatus.setStatus(_A)
class _Hpnicfdot1xpaeportControlledType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('mac',2)))
_Hpnicfdot1xpaeportControlledType_Type.__name__=_C
_Hpnicfdot1xpaeportControlledType_Object=MibTableColumn
hpnicfdot1xpaeportControlledType=_Hpnicfdot1xpaeportControlledType_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,2,1,1,2),_Hpnicfdot1xpaeportControlledType_Type())
hpnicfdot1xpaeportControlledType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xpaeportControlledType.setStatus(_A)
class _Hpnicfdot1xpaeportMaxUserNum_Type(Integer32):defaultValue=256
_Hpnicfdot1xpaeportMaxUserNum_Type.__name__=_C
_Hpnicfdot1xpaeportMaxUserNum_Object=MibTableColumn
hpnicfdot1xpaeportMaxUserNum=_Hpnicfdot1xpaeportMaxUserNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,2,1,1,3),_Hpnicfdot1xpaeportMaxUserNum_Type())
hpnicfdot1xpaeportMaxUserNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xpaeportMaxUserNum.setStatus(_A)
_Hpnicfdot1xpaeportUserNumNow_Type=Integer32
_Hpnicfdot1xpaeportUserNumNow_Object=MibTableColumn
hpnicfdot1xpaeportUserNumNow=_Hpnicfdot1xpaeportUserNumNow_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,2,1,1,4),_Hpnicfdot1xpaeportUserNumNow_Type())
hpnicfdot1xpaeportUserNumNow.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfdot1xpaeportUserNumNow.setStatus(_A)
class _Hpnicfdot1xpaeportClearStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_Hpnicfdot1xpaeportClearStatistics_Type.__name__=_C
_Hpnicfdot1xpaeportClearStatistics_Object=MibTableColumn
hpnicfdot1xpaeportClearStatistics=_Hpnicfdot1xpaeportClearStatistics_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,2,1,1,5),_Hpnicfdot1xpaeportClearStatistics_Type())
hpnicfdot1xpaeportClearStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xpaeportClearStatistics.setStatus(_A)
class _Hpnicfdot1xpaeportMcastTrigStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Hpnicfdot1xpaeportMcastTrigStatus_Type.__name__=_C
_Hpnicfdot1xpaeportMcastTrigStatus_Object=MibTableColumn
hpnicfdot1xpaeportMcastTrigStatus=_Hpnicfdot1xpaeportMcastTrigStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,2,1,1,6),_Hpnicfdot1xpaeportMcastTrigStatus_Type())
hpnicfdot1xpaeportMcastTrigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xpaeportMcastTrigStatus.setStatus(_A)
class _Hpnicfdot1xpaeportHandshakeStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Hpnicfdot1xpaeportHandshakeStatus_Type.__name__=_C
_Hpnicfdot1xpaeportHandshakeStatus_Object=MibTableColumn
hpnicfdot1xpaeportHandshakeStatus=_Hpnicfdot1xpaeportHandshakeStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,6,1,2,1,1,7),_Hpnicfdot1xpaeportHandshakeStatus_Type())
hpnicfdot1xpaeportHandshakeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1xpaeportHandshakeStatus.setStatus(_A)
hpnicfsupplicantproxycheck=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,6,1,0,1))
hpnicfsupplicantproxycheck.setObjects(*((_E,_K),(_E,_L),(_E,_M),(_E,_N),(_E,_O)))
if mibBuilder.loadTexts:hpnicfsupplicantproxycheck.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfpaeExtMib':hpnicfpaeExtMib,'hpnicfpaeExtMibObjects':hpnicfpaeExtMibObjects,'hpnicfdot1xPaeTraps':hpnicfdot1xPaeTraps,'hpnicfsupplicantproxycheck':hpnicfsupplicantproxycheck,_K:hpnicfproxycheckVlanId,_L:hpnicfproxycheckPortName,_M:hpnicfproxycheckMacAddr,_N:hpnicfproxycheckIpaddr,_O:hpnicfproxycheckUsrName,'hpnicfdot1xPaeSystem':hpnicfdot1xPaeSystem,'hpnicfdot1xAuthQuietPeriod':hpnicfdot1xAuthQuietPeriod,'hpnicfdot1xAuthTxPeriod':hpnicfdot1xAuthTxPeriod,'hpnicfdot1xAuthSuppTimeout':hpnicfdot1xAuthSuppTimeout,'hpnicfdot1xAuthServerTimeout':hpnicfdot1xAuthServerTimeout,'hpnicfdot1xAuthMaxReq':hpnicfdot1xAuthMaxReq,'hpnicfdot1xAuthReAuthPeriod':hpnicfdot1xAuthReAuthPeriod,'hpnicfdot1xAuthMethod':hpnicfdot1xAuthMethod,'hpnicfdot1xPaeAuthenticator':hpnicfdot1xPaeAuthenticator,'hpnicfdot1xAuthConfigExtTable':hpnicfdot1xAuthConfigExtTable,'hpnicfdot1xAuthConfigExtEntry':hpnicfdot1xAuthConfigExtEntry,'hpnicfdot1xpaeportAuthAdminStatus':hpnicfdot1xpaeportAuthAdminStatus,'hpnicfdot1xpaeportControlledType':hpnicfdot1xpaeportControlledType,'hpnicfdot1xpaeportMaxUserNum':hpnicfdot1xpaeportMaxUserNum,'hpnicfdot1xpaeportUserNumNow':hpnicfdot1xpaeportUserNumNow,'hpnicfdot1xpaeportClearStatistics':hpnicfdot1xpaeportClearStatistics,'hpnicfdot1xpaeportMcastTrigStatus':hpnicfdot1xpaeportMcastTrigStatus,'hpnicfdot1xpaeportHandshakeStatus':hpnicfdot1xpaeportHandshakeStatus})