_U='hm2CamClientServerReplicationStatus'
_T='hm2CamClientServerStatus'
_S='hm2CamCertInfoIndex'
_R='unreachable'
_Q='InetPortNumber'
_P='InetAddressType'
_O='InetAddress'
_N='pending'
_M='unsuccessful'
_L='HmEnabledStatus'
_K='obsolete'
_J='hm2CamClientServerIndex'
_I='ok'
_H='other'
_G='HM2-CAM-MGMT-MIB'
_F='read-write'
_E='SnmpAdminString'
_D='read-create'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_L,'hm2ConfigurationMibs')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_O,_P,_Q)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hm2CamMgmtMib=ModuleIdentity((1,3,6,1,4,1,248,11,200))
if mibBuilder.loadTexts:hm2CamMgmtMib.setRevisions(('2013-07-01 00:00',))
_Hm2CamMgmtMibNotifications_ObjectIdentity=ObjectIdentity
hm2CamMgmtMibNotifications=_Hm2CamMgmtMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,200,0))
_Hm2CamMgmtMibObjects_ObjectIdentity=ObjectIdentity
hm2CamMgmtMibObjects=_Hm2CamMgmtMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,200,1))
_Hm2CamConfigGroup_ObjectIdentity=ObjectIdentity
hm2CamConfigGroup=_Hm2CamConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,11,200,1,1))
class _Hm2CamConfigAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2CamConfigAdminStatus_Type.__name__=_L
_Hm2CamConfigAdminStatus_Object=MibScalar
hm2CamConfigAdminStatus=_Hm2CamConfigAdminStatus_Object((1,3,6,1,4,1,248,11,200,1,1,1),_Hm2CamConfigAdminStatus_Type())
hm2CamConfigAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2CamConfigAdminStatus.setStatus(_A)
class _Hm2CamConfigLastValidServerindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Hm2CamConfigLastValidServerindex_Type.__name__=_B
_Hm2CamConfigLastValidServerindex_Object=MibScalar
hm2CamConfigLastValidServerindex=_Hm2CamConfigLastValidServerindex_Object((1,3,6,1,4,1,248,11,200,1,1,2),_Hm2CamConfigLastValidServerindex_Type())
hm2CamConfigLastValidServerindex.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2CamConfigLastValidServerindex.setStatus(_A)
_Hm2CamClientServerAddrTable_Object=MibTable
hm2CamClientServerAddrTable=_Hm2CamClientServerAddrTable_Object((1,3,6,1,4,1,248,11,200,1,1,10))
if mibBuilder.loadTexts:hm2CamClientServerAddrTable.setStatus(_A)
_Hm2CamClientServerAddrEntry_Object=MibTableRow
hm2CamClientServerAddrEntry=_Hm2CamClientServerAddrEntry_Object((1,3,6,1,4,1,248,11,200,1,1,10,1))
hm2CamClientServerAddrEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:hm2CamClientServerAddrEntry.setStatus(_A)
class _Hm2CamClientServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_Hm2CamClientServerIndex_Type.__name__=_B
_Hm2CamClientServerIndex_Object=MibTableColumn
hm2CamClientServerIndex=_Hm2CamClientServerIndex_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,1),_Hm2CamClientServerIndex_Type())
hm2CamClientServerIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hm2CamClientServerIndex.setStatus(_A)
class _Hm2CamClientServerAddrType_Type(InetAddressType):defaultValue=1
_Hm2CamClientServerAddrType_Type.__name__=_P
_Hm2CamClientServerAddrType_Object=MibTableColumn
hm2CamClientServerAddrType=_Hm2CamClientServerAddrType_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,2),_Hm2CamClientServerAddrType_Type())
hm2CamClientServerAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2CamClientServerAddrType.setStatus(_A)
class _Hm2CamClientServerAddr_Type(InetAddress):defaultHexValue='00000000'
_Hm2CamClientServerAddr_Type.__name__=_O
_Hm2CamClientServerAddr_Object=MibTableColumn
hm2CamClientServerAddr=_Hm2CamClientServerAddr_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,3),_Hm2CamClientServerAddr_Type())
hm2CamClientServerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2CamClientServerAddr.setStatus(_A)
class _Hm2CamClientServerPort_Type(InetPortNumber):defaultValue=389
_Hm2CamClientServerPort_Type.__name__=_Q
_Hm2CamClientServerPort_Object=MibTableColumn
hm2CamClientServerPort=_Hm2CamClientServerPort_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,4),_Hm2CamClientServerPort_Type())
hm2CamClientServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2CamClientServerPort.setStatus(_A)
class _Hm2CamClientServerDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_Hm2CamClientServerDescr_Type.__name__=_E
_Hm2CamClientServerDescr_Object=MibTableColumn
hm2CamClientServerDescr=_Hm2CamClientServerDescr_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,5),_Hm2CamClientServerDescr_Type())
hm2CamClientServerDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2CamClientServerDescr.setStatus(_A)
class _Hm2CamClientServerBaseDN_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_Hm2CamClientServerBaseDN_Type.__name__=_E
_Hm2CamClientServerBaseDN_Object=MibTableColumn
hm2CamClientServerBaseDN=_Hm2CamClientServerBaseDN_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,6),_Hm2CamClientServerBaseDN_Type())
hm2CamClientServerBaseDN.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2CamClientServerBaseDN.setStatus(_A)
class _Hm2CamClientServerSearchString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_Hm2CamClientServerSearchString_Type.__name__=_E
_Hm2CamClientServerSearchString_Object=MibTableColumn
hm2CamClientServerSearchString=_Hm2CamClientServerSearchString_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,7),_Hm2CamClientServerSearchString_Type())
hm2CamClientServerSearchString.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2CamClientServerSearchString.setStatus(_A)
class _Hm2CamClientServerStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_R,2),(_H,3)))
_Hm2CamClientServerStatus_Type.__name__=_B
_Hm2CamClientServerStatus_Object=MibTableColumn
hm2CamClientServerStatus=_Hm2CamClientServerStatus_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,8),_Hm2CamClientServerStatus_Type())
hm2CamClientServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2CamClientServerStatus.setStatus(_A)
class _Hm2CamClientServerReplicationInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1440))
_Hm2CamClientServerReplicationInterval_Type.__name__=_B
_Hm2CamClientServerReplicationInterval_Object=MibTableColumn
hm2CamClientServerReplicationInterval=_Hm2CamClientServerReplicationInterval_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,9),_Hm2CamClientServerReplicationInterval_Type())
hm2CamClientServerReplicationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2CamClientServerReplicationInterval.setStatus(_K)
if mibBuilder.loadTexts:hm2CamClientServerReplicationInterval.setUnits('minutes')
class _Hm2CamClientServerReplicationStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_M,2),(_H,3)))
_Hm2CamClientServerReplicationStatus_Type.__name__=_B
_Hm2CamClientServerReplicationStatus_Object=MibTableColumn
hm2CamClientServerReplicationStatus=_Hm2CamClientServerReplicationStatus_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,10),_Hm2CamClientServerReplicationStatus_Type())
hm2CamClientServerReplicationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2CamClientServerReplicationStatus.setStatus(_K)
_Hm2CamClientServerRowStatus_Type=RowStatus
_Hm2CamClientServerRowStatus_Object=MibTableColumn
hm2CamClientServerRowStatus=_Hm2CamClientServerRowStatus_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,11),_Hm2CamClientServerRowStatus_Type())
hm2CamClientServerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2CamClientServerRowStatus.setStatus(_A)
class _Hm2CamClientServerSslTls_Type(HmEnabledStatus):defaultValue=2
_Hm2CamClientServerSslTls_Type.__name__=_L
_Hm2CamClientServerSslTls_Object=MibTableColumn
hm2CamClientServerSslTls=_Hm2CamClientServerSslTls_Object((1,3,6,1,4,1,248,11,200,1,1,10,1,12),_Hm2CamClientServerSslTls_Type())
hm2CamClientServerSslTls.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2CamClientServerSslTls.setStatus(_A)
_Hm2CamActionGroup_ObjectIdentity=ObjectIdentity
hm2CamActionGroup=_Hm2CamActionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,200,1,10))
class _Hm2CamAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('testConnection',2)))
_Hm2CamAction_Type.__name__=_B
_Hm2CamAction_Object=MibScalar
hm2CamAction=_Hm2CamAction_Object((1,3,6,1,4,1,248,11,200,1,10,1),_Hm2CamAction_Type())
hm2CamAction.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2CamAction.setStatus(_A)
class _Hm2CamActionConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_R,2),(_N,3),(_H,4)))
_Hm2CamActionConnectionStatus_Type.__name__=_B
_Hm2CamActionConnectionStatus_Object=MibScalar
hm2CamActionConnectionStatus=_Hm2CamActionConnectionStatus_Object((1,3,6,1,4,1,248,11,200,1,10,2),_Hm2CamActionConnectionStatus_Type())
hm2CamActionConnectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2CamActionConnectionStatus.setStatus(_A)
class _Hm2CamActionReplicationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_M,2),(_N,3),(_H,4)))
_Hm2CamActionReplicationStatus_Type.__name__=_B
_Hm2CamActionReplicationStatus_Object=MibScalar
hm2CamActionReplicationStatus=_Hm2CamActionReplicationStatus_Object((1,3,6,1,4,1,248,11,200,1,10,3),_Hm2CamActionReplicationStatus_Type())
hm2CamActionReplicationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2CamActionReplicationStatus.setStatus(_K)
_Hm2CamPwdChangeGroup_ObjectIdentity=ObjectIdentity
hm2CamPwdChangeGroup=_Hm2CamPwdChangeGroup_ObjectIdentity((1,3,6,1,4,1,248,11,200,1,20))
class _Hm2CamPwdChangeUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_Hm2CamPwdChangeUserName_Type.__name__=_E
_Hm2CamPwdChangeUserName_Object=MibScalar
hm2CamPwdChangeUserName=_Hm2CamPwdChangeUserName_Object((1,3,6,1,4,1,248,11,200,1,20,1),_Hm2CamPwdChangeUserName_Type())
hm2CamPwdChangeUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2CamPwdChangeUserName.setStatus(_A)
class _Hm2CamPwdChangeUserPwOld_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_Hm2CamPwdChangeUserPwOld_Type.__name__=_E
_Hm2CamPwdChangeUserPwOld_Object=MibScalar
hm2CamPwdChangeUserPwOld=_Hm2CamPwdChangeUserPwOld_Object((1,3,6,1,4,1,248,11,200,1,20,2),_Hm2CamPwdChangeUserPwOld_Type())
hm2CamPwdChangeUserPwOld.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2CamPwdChangeUserPwOld.setStatus(_A)
class _Hm2CamPwdChangeUserPwNew_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_Hm2CamPwdChangeUserPwNew_Type.__name__=_E
_Hm2CamPwdChangeUserPwNew_Object=MibScalar
hm2CamPwdChangeUserPwNew=_Hm2CamPwdChangeUserPwNew_Object((1,3,6,1,4,1,248,11,200,1,20,3),_Hm2CamPwdChangeUserPwNew_Type())
hm2CamPwdChangeUserPwNew.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2CamPwdChangeUserPwNew.setStatus(_A)
class _Hm2CamPwdChangeAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('changePwd',2)))
_Hm2CamPwdChangeAction_Type.__name__=_B
_Hm2CamPwdChangeAction_Object=MibScalar
hm2CamPwdChangeAction=_Hm2CamPwdChangeAction_Object((1,3,6,1,4,1,248,11,200,1,20,4),_Hm2CamPwdChangeAction_Type())
hm2CamPwdChangeAction.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2CamPwdChangeAction.setStatus(_A)
class _Hm2CamPwdChangeActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_M,2),(_N,3),(_H,4)))
_Hm2CamPwdChangeActionStatus_Type.__name__=_B
_Hm2CamPwdChangeActionStatus_Object=MibScalar
hm2CamPwdChangeActionStatus=_Hm2CamPwdChangeActionStatus_Object((1,3,6,1,4,1,248,11,200,1,20,5),_Hm2CamPwdChangeActionStatus_Type())
hm2CamPwdChangeActionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2CamPwdChangeActionStatus.setStatus(_A)
_Hm2CamCertInfoGroup_ObjectIdentity=ObjectIdentity
hm2CamCertInfoGroup=_Hm2CamCertInfoGroup_ObjectIdentity((1,3,6,1,4,1,248,11,200,1,30))
_Hm2CamCertInfoTable_Object=MibTable
hm2CamCertInfoTable=_Hm2CamCertInfoTable_Object((1,3,6,1,4,1,248,11,200,1,30,1))
if mibBuilder.loadTexts:hm2CamCertInfoTable.setStatus(_A)
_Hm2CamCertInfoEntry_Object=MibTableRow
hm2CamCertInfoEntry=_Hm2CamCertInfoEntry_Object((1,3,6,1,4,1,248,11,200,1,30,1,1))
hm2CamCertInfoEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:hm2CamCertInfoEntry.setStatus(_A)
class _Hm2CamCertInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rootCert',1),('deviceCert',2)))
_Hm2CamCertInfoIndex_Type.__name__=_B
_Hm2CamCertInfoIndex_Object=MibTableColumn
hm2CamCertInfoIndex=_Hm2CamCertInfoIndex_Object((1,3,6,1,4,1,248,11,200,1,30,1,1,1),_Hm2CamCertInfoIndex_Type())
hm2CamCertInfoIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hm2CamCertInfoIndex.setStatus(_A)
_Hm2CamCertInfoPresent_Type=TruthValue
_Hm2CamCertInfoPresent_Object=MibTableColumn
hm2CamCertInfoPresent=_Hm2CamCertInfoPresent_Object((1,3,6,1,4,1,248,11,200,1,30,1,1,2),_Hm2CamCertInfoPresent_Type())
hm2CamCertInfoPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2CamCertInfoPresent.setStatus(_A)
_Hm2CamCertInfoExpiry_Type=SnmpAdminString
_Hm2CamCertInfoExpiry_Object=MibTableColumn
hm2CamCertInfoExpiry=_Hm2CamCertInfoExpiry_Object((1,3,6,1,4,1,248,11,200,1,30,1,1,3),_Hm2CamCertInfoExpiry_Type())
hm2CamCertInfoExpiry.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2CamCertInfoExpiry.setStatus(_A)
_Hm2CamCertInfoIssuer_Type=SnmpAdminString
_Hm2CamCertInfoIssuer_Object=MibTableColumn
hm2CamCertInfoIssuer=_Hm2CamCertInfoIssuer_Object((1,3,6,1,4,1,248,11,200,1,30,1,1,4),_Hm2CamCertInfoIssuer_Type())
hm2CamCertInfoIssuer.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2CamCertInfoIssuer.setStatus(_A)
_Hm2CamCertInfoSubject_Type=SnmpAdminString
_Hm2CamCertInfoSubject_Object=MibTableColumn
hm2CamCertInfoSubject=_Hm2CamCertInfoSubject_Object((1,3,6,1,4,1,248,11,200,1,30,1,1,5),_Hm2CamCertInfoSubject_Type())
hm2CamCertInfoSubject.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2CamCertInfoSubject.setStatus(_A)
_Hm2CamCertInfoSerialNumber_Type=SnmpAdminString
_Hm2CamCertInfoSerialNumber_Object=MibTableColumn
hm2CamCertInfoSerialNumber=_Hm2CamCertInfoSerialNumber_Object((1,3,6,1,4,1,248,11,200,1,30,1,1,6),_Hm2CamCertInfoSerialNumber_Type())
hm2CamCertInfoSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2CamCertInfoSerialNumber.setStatus(_A)
_Hm2CamMgmtMibSnmpExtensionGroup_ObjectIdentity=ObjectIdentity
hm2CamMgmtMibSnmpExtensionGroup=_Hm2CamMgmtMibSnmpExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,200,3))
_Hm2CamConfigSESGroup_ObjectIdentity=ObjectIdentity
hm2CamConfigSESGroup=_Hm2CamConfigSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,200,3,1))
_Hm2CamMgmtNoCaCertErrorReturn_ObjectIdentity=ObjectIdentity
hm2CamMgmtNoCaCertErrorReturn=_Hm2CamMgmtNoCaCertErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,200,3,1,1))
if mibBuilder.loadTexts:hm2CamMgmtNoCaCertErrorReturn.setStatus(_A)
_Hm2CamMgmtTestConnErrorReturn_ObjectIdentity=ObjectIdentity
hm2CamMgmtTestConnErrorReturn=_Hm2CamMgmtTestConnErrorReturn_ObjectIdentity((1,3,6,1,4,1,248,11,200,3,1,2))
if mibBuilder.loadTexts:hm2CamMgmtTestConnErrorReturn.setStatus(_A)
_Hm2CamActionSESGroup_ObjectIdentity=ObjectIdentity
hm2CamActionSESGroup=_Hm2CamActionSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,200,3,10))
_Hm2CamPwdChangeSESGroup_ObjectIdentity=ObjectIdentity
hm2CamPwdChangeSESGroup=_Hm2CamPwdChangeSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,200,3,20))
_Hm2CamCertInfoSESGroup_ObjectIdentity=ObjectIdentity
hm2CamCertInfoSESGroup=_Hm2CamCertInfoSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,200,3,30))
hm2CamConfigStatusTrap=NotificationType((1,3,6,1,4,1,248,11,200,0,1))
hm2CamConfigStatusTrap.setObjects(*((_G,_J),(_G,_T)))
if mibBuilder.loadTexts:hm2CamConfigStatusTrap.setStatus(_A)
hm2CamReplicationStatusTrap=NotificationType((1,3,6,1,4,1,248,11,200,0,2))
hm2CamReplicationStatusTrap.setObjects(*((_G,_J),(_G,_U)))
if mibBuilder.loadTexts:hm2CamReplicationStatusTrap.setStatus(_K)
mibBuilder.exportSymbols(_G,**{'hm2CamMgmtMib':hm2CamMgmtMib,'hm2CamMgmtMibNotifications':hm2CamMgmtMibNotifications,'hm2CamConfigStatusTrap':hm2CamConfigStatusTrap,'hm2CamReplicationStatusTrap':hm2CamReplicationStatusTrap,'hm2CamMgmtMibObjects':hm2CamMgmtMibObjects,'hm2CamConfigGroup':hm2CamConfigGroup,'hm2CamConfigAdminStatus':hm2CamConfigAdminStatus,'hm2CamConfigLastValidServerindex':hm2CamConfigLastValidServerindex,'hm2CamClientServerAddrTable':hm2CamClientServerAddrTable,'hm2CamClientServerAddrEntry':hm2CamClientServerAddrEntry,_J:hm2CamClientServerIndex,'hm2CamClientServerAddrType':hm2CamClientServerAddrType,'hm2CamClientServerAddr':hm2CamClientServerAddr,'hm2CamClientServerPort':hm2CamClientServerPort,'hm2CamClientServerDescr':hm2CamClientServerDescr,'hm2CamClientServerBaseDN':hm2CamClientServerBaseDN,'hm2CamClientServerSearchString':hm2CamClientServerSearchString,_T:hm2CamClientServerStatus,'hm2CamClientServerReplicationInterval':hm2CamClientServerReplicationInterval,_U:hm2CamClientServerReplicationStatus,'hm2CamClientServerRowStatus':hm2CamClientServerRowStatus,'hm2CamClientServerSslTls':hm2CamClientServerSslTls,'hm2CamActionGroup':hm2CamActionGroup,'hm2CamAction':hm2CamAction,'hm2CamActionConnectionStatus':hm2CamActionConnectionStatus,'hm2CamActionReplicationStatus':hm2CamActionReplicationStatus,'hm2CamPwdChangeGroup':hm2CamPwdChangeGroup,'hm2CamPwdChangeUserName':hm2CamPwdChangeUserName,'hm2CamPwdChangeUserPwOld':hm2CamPwdChangeUserPwOld,'hm2CamPwdChangeUserPwNew':hm2CamPwdChangeUserPwNew,'hm2CamPwdChangeAction':hm2CamPwdChangeAction,'hm2CamPwdChangeActionStatus':hm2CamPwdChangeActionStatus,'hm2CamCertInfoGroup':hm2CamCertInfoGroup,'hm2CamCertInfoTable':hm2CamCertInfoTable,'hm2CamCertInfoEntry':hm2CamCertInfoEntry,_S:hm2CamCertInfoIndex,'hm2CamCertInfoPresent':hm2CamCertInfoPresent,'hm2CamCertInfoExpiry':hm2CamCertInfoExpiry,'hm2CamCertInfoIssuer':hm2CamCertInfoIssuer,'hm2CamCertInfoSubject':hm2CamCertInfoSubject,'hm2CamCertInfoSerialNumber':hm2CamCertInfoSerialNumber,'hm2CamMgmtMibSnmpExtensionGroup':hm2CamMgmtMibSnmpExtensionGroup,'hm2CamConfigSESGroup':hm2CamConfigSESGroup,'hm2CamMgmtNoCaCertErrorReturn':hm2CamMgmtNoCaCertErrorReturn,'hm2CamMgmtTestConnErrorReturn':hm2CamMgmtTestConnErrorReturn,'hm2CamActionSESGroup':hm2CamActionSESGroup,'hm2CamPwdChangeSESGroup':hm2CamPwdChangeSESGroup,'hm2CamCertInfoSESGroup':hm2CamCertInfoSESGroup})