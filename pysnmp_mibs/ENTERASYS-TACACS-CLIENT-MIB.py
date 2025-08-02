_g='etsysTacacsClientSesnAuthGroup'
_f='etsysTacacsClientCmdAcctGroup'
_e='etsysTacacsClientCmdAuthGroup'
_d='etsysTacacsClientSessionGroup'
_c='etsysTacacsClientSesnAuthValue'
_b='etsysTacacsClientSesnAuthAttribute'
_a='etsysTacacsClientSesnAuthService'
_Z='etsysTacacsClientCmdAcctEnabled'
_Y='etsysTacacsClientCmdAuthEnabled'
_X='etsysTacacsClientServerStatus'
_W='etsysTacacsClientServerSecretEntered'
_V='etsysTacacsClientServerSecret'
_U='etsysTacacsClientServerTimeout'
_T='etsysTacacsClientServerPortNumber'
_S='etsysTacacsClientServerAddress'
_R='etsysTacacsClientServerAddressType'
_Q='etsysTacacsClientSingleConnection'
_P='etsysTacacsClientSesnAcctEnabled'
_O='etsysTacacsClientSesnAuthEnabled'
_N='etsysTacacsClientServerIndex'
_M='not-accessible'
_L='etsysTacacsClientSesnAuthLevel'
_K='InetPortNumber'
_J='InetAddressType'
_I='InetAddress'
_H='OctetString'
_G='SnmpAdminString'
_F='Integer32'
_E='read-create'
_D='EnabledStatus'
_C='read-write'
_B='ENTERASYS-TACACS-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,_J,_K)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_D)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
etsysTacacsClientMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,58))
if mibBuilder.loadTexts:etsysTacacsClientMIB.setRevisions(('2010-02-01 17:02','2005-02-10 17:57'))
_EtsysTacacsClientObjects_ObjectIdentity=ObjectIdentity
etsysTacacsClientObjects=_EtsysTacacsClientObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,58,1))
_EtsysTacacsClientControl_ObjectIdentity=ObjectIdentity
etsysTacacsClientControl=_EtsysTacacsClientControl_ObjectIdentity((1,3,6,1,4,1,5624,1,2,58,1,1))
class _EtsysTacacsClientSesnAuthEnabled_Type(EnabledStatus):defaultValue=2
_EtsysTacacsClientSesnAuthEnabled_Type.__name__=_D
_EtsysTacacsClientSesnAuthEnabled_Object=MibScalar
etsysTacacsClientSesnAuthEnabled=_EtsysTacacsClientSesnAuthEnabled_Object((1,3,6,1,4,1,5624,1,2,58,1,1,1),_EtsysTacacsClientSesnAuthEnabled_Type())
etsysTacacsClientSesnAuthEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysTacacsClientSesnAuthEnabled.setStatus(_A)
class _EtsysTacacsClientSesnAcctEnabled_Type(EnabledStatus):defaultValue=2
_EtsysTacacsClientSesnAcctEnabled_Type.__name__=_D
_EtsysTacacsClientSesnAcctEnabled_Object=MibScalar
etsysTacacsClientSesnAcctEnabled=_EtsysTacacsClientSesnAcctEnabled_Object((1,3,6,1,4,1,5624,1,2,58,1,1,2),_EtsysTacacsClientSesnAcctEnabled_Type())
etsysTacacsClientSesnAcctEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysTacacsClientSesnAcctEnabled.setStatus(_A)
class _EtsysTacacsClientCmdAuthEnabled_Type(EnabledStatus):defaultValue=2
_EtsysTacacsClientCmdAuthEnabled_Type.__name__=_D
_EtsysTacacsClientCmdAuthEnabled_Object=MibScalar
etsysTacacsClientCmdAuthEnabled=_EtsysTacacsClientCmdAuthEnabled_Object((1,3,6,1,4,1,5624,1,2,58,1,1,3),_EtsysTacacsClientCmdAuthEnabled_Type())
etsysTacacsClientCmdAuthEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysTacacsClientCmdAuthEnabled.setStatus(_A)
class _EtsysTacacsClientCmdAcctEnabled_Type(EnabledStatus):defaultValue=2
_EtsysTacacsClientCmdAcctEnabled_Type.__name__=_D
_EtsysTacacsClientCmdAcctEnabled_Object=MibScalar
etsysTacacsClientCmdAcctEnabled=_EtsysTacacsClientCmdAcctEnabled_Object((1,3,6,1,4,1,5624,1,2,58,1,1,4),_EtsysTacacsClientCmdAcctEnabled_Type())
etsysTacacsClientCmdAcctEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysTacacsClientCmdAcctEnabled.setStatus(_A)
class _EtsysTacacsClientSingleConnection_Type(EnabledStatus):defaultValue=2
_EtsysTacacsClientSingleConnection_Type.__name__=_D
_EtsysTacacsClientSingleConnection_Object=MibScalar
etsysTacacsClientSingleConnection=_EtsysTacacsClientSingleConnection_Object((1,3,6,1,4,1,5624,1,2,58,1,1,5),_EtsysTacacsClientSingleConnection_Type())
etsysTacacsClientSingleConnection.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysTacacsClientSingleConnection.setStatus(_A)
_EtsysTacacsClientSesnAuth_ObjectIdentity=ObjectIdentity
etsysTacacsClientSesnAuth=_EtsysTacacsClientSesnAuth_ObjectIdentity((1,3,6,1,4,1,5624,1,2,58,1,2))
class _EtsysTacacsClientSesnAuthService_Type(SnmpAdminString):defaultValue=OctetString('enable')
_EtsysTacacsClientSesnAuthService_Type.__name__=_G
_EtsysTacacsClientSesnAuthService_Object=MibScalar
etsysTacacsClientSesnAuthService=_EtsysTacacsClientSesnAuthService_Object((1,3,6,1,4,1,5624,1,2,58,1,2,1),_EtsysTacacsClientSesnAuthService_Type())
etsysTacacsClientSesnAuthService.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysTacacsClientSesnAuthService.setStatus(_A)
_EtsysTacacsClientSesnAuthTable_Object=MibTable
etsysTacacsClientSesnAuthTable=_EtsysTacacsClientSesnAuthTable_Object((1,3,6,1,4,1,5624,1,2,58,1,2,2))
if mibBuilder.loadTexts:etsysTacacsClientSesnAuthTable.setStatus(_A)
_EtsysTacacsClientSesnAuthEntry_Object=MibTableRow
etsysTacacsClientSesnAuthEntry=_EtsysTacacsClientSesnAuthEntry_Object((1,3,6,1,4,1,5624,1,2,58,1,2,2,1))
etsysTacacsClientSesnAuthEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:etsysTacacsClientSesnAuthEntry.setStatus(_A)
class _EtsysTacacsClientSesnAuthLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('readonly',1),('readwrite',2),('superuser',3),('debug',4)))
_EtsysTacacsClientSesnAuthLevel_Type.__name__=_F
_EtsysTacacsClientSesnAuthLevel_Object=MibTableColumn
etsysTacacsClientSesnAuthLevel=_EtsysTacacsClientSesnAuthLevel_Object((1,3,6,1,4,1,5624,1,2,58,1,2,2,1,1),_EtsysTacacsClientSesnAuthLevel_Type())
etsysTacacsClientSesnAuthLevel.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysTacacsClientSesnAuthLevel.setStatus(_A)
class _EtsysTacacsClientSesnAuthAttribute_Type(SnmpAdminString):defaultValue=OctetString('priv-lvl')
_EtsysTacacsClientSesnAuthAttribute_Type.__name__=_G
_EtsysTacacsClientSesnAuthAttribute_Object=MibTableColumn
etsysTacacsClientSesnAuthAttribute=_EtsysTacacsClientSesnAuthAttribute_Object((1,3,6,1,4,1,5624,1,2,58,1,2,2,1,2),_EtsysTacacsClientSesnAuthAttribute_Type())
etsysTacacsClientSesnAuthAttribute.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysTacacsClientSesnAuthAttribute.setStatus(_A)
_EtsysTacacsClientSesnAuthValue_Type=SnmpAdminString
_EtsysTacacsClientSesnAuthValue_Object=MibTableColumn
etsysTacacsClientSesnAuthValue=_EtsysTacacsClientSesnAuthValue_Object((1,3,6,1,4,1,5624,1,2,58,1,2,2,1,3),_EtsysTacacsClientSesnAuthValue_Type())
etsysTacacsClientSesnAuthValue.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysTacacsClientSesnAuthValue.setStatus(_A)
_EtsysTacacsClientServer_ObjectIdentity=ObjectIdentity
etsysTacacsClientServer=_EtsysTacacsClientServer_ObjectIdentity((1,3,6,1,4,1,5624,1,2,58,1,3))
_EtsysTacacsClientServerTable_Object=MibTable
etsysTacacsClientServerTable=_EtsysTacacsClientServerTable_Object((1,3,6,1,4,1,5624,1,2,58,1,3,1))
if mibBuilder.loadTexts:etsysTacacsClientServerTable.setStatus(_A)
_EtsysTacacsClientServerEntry_Object=MibTableRow
etsysTacacsClientServerEntry=_EtsysTacacsClientServerEntry_Object((1,3,6,1,4,1,5624,1,2,58,1,3,1,1))
etsysTacacsClientServerEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:etsysTacacsClientServerEntry.setStatus(_A)
class _EtsysTacacsClientServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EtsysTacacsClientServerIndex_Type.__name__=_F
_EtsysTacacsClientServerIndex_Object=MibTableColumn
etsysTacacsClientServerIndex=_EtsysTacacsClientServerIndex_Object((1,3,6,1,4,1,5624,1,2,58,1,3,1,1,1),_EtsysTacacsClientServerIndex_Type())
etsysTacacsClientServerIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:etsysTacacsClientServerIndex.setStatus(_A)
class _EtsysTacacsClientServerAddressType_Type(InetAddressType):defaultValue=1
_EtsysTacacsClientServerAddressType_Type.__name__=_J
_EtsysTacacsClientServerAddressType_Object=MibTableColumn
etsysTacacsClientServerAddressType=_EtsysTacacsClientServerAddressType_Object((1,3,6,1,4,1,5624,1,2,58,1,3,1,1,2),_EtsysTacacsClientServerAddressType_Type())
etsysTacacsClientServerAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysTacacsClientServerAddressType.setStatus(_A)
class _EtsysTacacsClientServerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_EtsysTacacsClientServerAddress_Type.__name__=_I
_EtsysTacacsClientServerAddress_Object=MibTableColumn
etsysTacacsClientServerAddress=_EtsysTacacsClientServerAddress_Object((1,3,6,1,4,1,5624,1,2,58,1,3,1,1,3),_EtsysTacacsClientServerAddress_Type())
etsysTacacsClientServerAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysTacacsClientServerAddress.setStatus(_A)
class _EtsysTacacsClientServerPortNumber_Type(InetPortNumber):defaultValue=49
_EtsysTacacsClientServerPortNumber_Type.__name__=_K
_EtsysTacacsClientServerPortNumber_Object=MibTableColumn
etsysTacacsClientServerPortNumber=_EtsysTacacsClientServerPortNumber_Object((1,3,6,1,4,1,5624,1,2,58,1,3,1,1,4),_EtsysTacacsClientServerPortNumber_Type())
etsysTacacsClientServerPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysTacacsClientServerPortNumber.setStatus(_A)
class _EtsysTacacsClientServerTimeout_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,180))
_EtsysTacacsClientServerTimeout_Type.__name__=_F
_EtsysTacacsClientServerTimeout_Object=MibTableColumn
etsysTacacsClientServerTimeout=_EtsysTacacsClientServerTimeout_Object((1,3,6,1,4,1,5624,1,2,58,1,3,1,1,5),_EtsysTacacsClientServerTimeout_Type())
etsysTacacsClientServerTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysTacacsClientServerTimeout.setStatus(_A)
if mibBuilder.loadTexts:etsysTacacsClientServerTimeout.setUnits('seconds')
class _EtsysTacacsClientServerSecret_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysTacacsClientServerSecret_Type.__name__=_H
_EtsysTacacsClientServerSecret_Object=MibTableColumn
etsysTacacsClientServerSecret=_EtsysTacacsClientServerSecret_Object((1,3,6,1,4,1,5624,1,2,58,1,3,1,1,6),_EtsysTacacsClientServerSecret_Type())
etsysTacacsClientServerSecret.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysTacacsClientServerSecret.setStatus(_A)
_EtsysTacacsClientServerSecretEntered_Type=TruthValue
_EtsysTacacsClientServerSecretEntered_Object=MibTableColumn
etsysTacacsClientServerSecretEntered=_EtsysTacacsClientServerSecretEntered_Object((1,3,6,1,4,1,5624,1,2,58,1,3,1,1,7),_EtsysTacacsClientServerSecretEntered_Type())
etsysTacacsClientServerSecretEntered.setMaxAccess('read-only')
if mibBuilder.loadTexts:etsysTacacsClientServerSecretEntered.setStatus(_A)
_EtsysTacacsClientServerStatus_Type=RowStatus
_EtsysTacacsClientServerStatus_Object=MibTableColumn
etsysTacacsClientServerStatus=_EtsysTacacsClientServerStatus_Object((1,3,6,1,4,1,5624,1,2,58,1,3,1,1,8),_EtsysTacacsClientServerStatus_Type())
etsysTacacsClientServerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysTacacsClientServerStatus.setStatus(_A)
_EtsysTacacsClientConformance_ObjectIdentity=ObjectIdentity
etsysTacacsClientConformance=_EtsysTacacsClientConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,58,2))
_EtsysTacacsClientCompliances_ObjectIdentity=ObjectIdentity
etsysTacacsClientCompliances=_EtsysTacacsClientCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,58,2,1))
_EtsysTacacsClientGroups_ObjectIdentity=ObjectIdentity
etsysTacacsClientGroups=_EtsysTacacsClientGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,58,2,2))
etsysTacacsClientSessionGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,58,2,2,1))
etsysTacacsClientSessionGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:etsysTacacsClientSessionGroup.setStatus(_A)
etsysTacacsClientCmdAuthGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,58,2,2,2))
etsysTacacsClientCmdAuthGroup.setObjects((_B,_Y))
if mibBuilder.loadTexts:etsysTacacsClientCmdAuthGroup.setStatus(_A)
etsysTacacsClientCmdAcctGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,58,2,2,3))
etsysTacacsClientCmdAcctGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:etsysTacacsClientCmdAcctGroup.setStatus(_A)
etsysTacacsClientSesnAuthGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,58,2,2,4))
etsysTacacsClientSesnAuthGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:etsysTacacsClientSesnAuthGroup.setStatus(_A)
etsysTacacsClientCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,58,2,1,1))
etsysTacacsClientCompliance.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:etsysTacacsClientCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysTacacsClientMIB':etsysTacacsClientMIB,'etsysTacacsClientObjects':etsysTacacsClientObjects,'etsysTacacsClientControl':etsysTacacsClientControl,_O:etsysTacacsClientSesnAuthEnabled,_P:etsysTacacsClientSesnAcctEnabled,_Y:etsysTacacsClientCmdAuthEnabled,_Z:etsysTacacsClientCmdAcctEnabled,_Q:etsysTacacsClientSingleConnection,'etsysTacacsClientSesnAuth':etsysTacacsClientSesnAuth,_a:etsysTacacsClientSesnAuthService,'etsysTacacsClientSesnAuthTable':etsysTacacsClientSesnAuthTable,'etsysTacacsClientSesnAuthEntry':etsysTacacsClientSesnAuthEntry,_L:etsysTacacsClientSesnAuthLevel,_b:etsysTacacsClientSesnAuthAttribute,_c:etsysTacacsClientSesnAuthValue,'etsysTacacsClientServer':etsysTacacsClientServer,'etsysTacacsClientServerTable':etsysTacacsClientServerTable,'etsysTacacsClientServerEntry':etsysTacacsClientServerEntry,_N:etsysTacacsClientServerIndex,_R:etsysTacacsClientServerAddressType,_S:etsysTacacsClientServerAddress,_T:etsysTacacsClientServerPortNumber,_U:etsysTacacsClientServerTimeout,_V:etsysTacacsClientServerSecret,_W:etsysTacacsClientServerSecretEntered,_X:etsysTacacsClientServerStatus,'etsysTacacsClientConformance':etsysTacacsClientConformance,'etsysTacacsClientCompliances':etsysTacacsClientCompliances,'etsysTacacsClientCompliance':etsysTacacsClientCompliance,'etsysTacacsClientGroups':etsysTacacsClientGroups,_d:etsysTacacsClientSessionGroup,_e:etsysTacacsClientCmdAuthGroup,_f:etsysTacacsClientCmdAcctGroup,_g:etsysTacacsClientSesnAuthGroup})