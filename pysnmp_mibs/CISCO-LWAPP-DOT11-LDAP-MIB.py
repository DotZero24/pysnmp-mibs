_e='ciscoLwappDot11LdapMIBConfigGroupSup1'
_d='cldlServerAuthBindPassword'
_c='cldlServerAuthBindUserName'
_b='cldlServerBindType'
_a='cldlWlanLdapTertiaryServerIndex'
_Z='cldlWlanLdapSecondaryServerIndex'
_Y='cldlWlanLdapPrimaryServerIndex'
_X='cldlServerStorageType'
_W='cldlServerRowStatus'
_V='cldlServerSecurityEnable'
_U='cldlServerUserName'
_T='cldlServerUserNameAttribute'
_S='cldlServerUserBase'
_R='cldlServerTimeout'
_Q='cldlServerState'
_P='cldlServerPortNum'
_O='cldlServerAddress'
_N='cldlServerAddressType'
_M='CldlBindType'
_L='cldlServerIndex'
_K='TruthValue'
_J='StorageType'
_I='InetPortNumber'
_H='cLWlanIndex'
_G='CISCO-LWAPP-WLAN-MIB'
_F='ciscoLwappDot11LdapMIBConfigGroup'
_E='read-write'
_D='Unsigned32'
_C='read-create'
_B='CISCO-LWAPP-DOT11-LDAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cLWlanIndex,=mibBuilder.importSymbols(_G,_H)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_J,'TextualConvention',_K)
ciscoLwappDot11LdapMIB=ModuleIdentity((1,3,6,1,4,1,9,9,614))
if mibBuilder.loadTexts:ciscoLwappDot11LdapMIB.setRevisions(('2009-12-10 00:00','2007-01-13 00:00'))
class CldlBindType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('anonymous',1),('authenticated',2)))
_CiscoLwappDot11LdapMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoLwappDot11LdapMIBNotifs=_CiscoLwappDot11LdapMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,614,0))
_CiscoLwappDot11LdapMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLwappDot11LdapMIBObjects=_CiscoLwappDot11LdapMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,614,1))
_CldlConfig_ObjectIdentity=ObjectIdentity
cldlConfig=_CldlConfig_ObjectIdentity((1,3,6,1,4,1,9,9,614,1,1))
_CldlServerTable_Object=MibTable
cldlServerTable=_CldlServerTable_Object((1,3,6,1,4,1,9,9,614,1,1,1))
if mibBuilder.loadTexts:cldlServerTable.setStatus(_A)
_CldlServerEntry_Object=MibTableRow
cldlServerEntry=_CldlServerEntry_Object((1,3,6,1,4,1,9,9,614,1,1,1,1))
cldlServerEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cldlServerEntry.setStatus(_A)
class _CldlServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CldlServerIndex_Type.__name__=_D
_CldlServerIndex_Object=MibTableColumn
cldlServerIndex=_CldlServerIndex_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,1),_CldlServerIndex_Type())
cldlServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cldlServerIndex.setStatus(_A)
_CldlServerAddressType_Type=InetAddressType
_CldlServerAddressType_Object=MibTableColumn
cldlServerAddressType=_CldlServerAddressType_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,2),_CldlServerAddressType_Type())
cldlServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerAddressType.setStatus(_A)
_CldlServerAddress_Type=InetAddress
_CldlServerAddress_Object=MibTableColumn
cldlServerAddress=_CldlServerAddress_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,3),_CldlServerAddress_Type())
cldlServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerAddress.setStatus(_A)
class _CldlServerPortNum_Type(InetPortNumber):defaultValue=389
_CldlServerPortNum_Type.__name__=_I
_CldlServerPortNum_Object=MibTableColumn
cldlServerPortNum=_CldlServerPortNum_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,4),_CldlServerPortNum_Type())
cldlServerPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerPortNum.setStatus(_A)
_CldlServerState_Type=TruthValue
_CldlServerState_Object=MibTableColumn
cldlServerState=_CldlServerState_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,5),_CldlServerState_Type())
cldlServerState.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerState.setStatus(_A)
class _CldlServerTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_CldlServerTimeout_Type.__name__=_D
_CldlServerTimeout_Object=MibTableColumn
cldlServerTimeout=_CldlServerTimeout_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,6),_CldlServerTimeout_Type())
cldlServerTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerTimeout.setStatus(_A)
if mibBuilder.loadTexts:cldlServerTimeout.setUnits('seconds')
_CldlServerUserBase_Type=DisplayString
_CldlServerUserBase_Object=MibTableColumn
cldlServerUserBase=_CldlServerUserBase_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,7),_CldlServerUserBase_Type())
cldlServerUserBase.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerUserBase.setStatus(_A)
_CldlServerUserNameAttribute_Type=DisplayString
_CldlServerUserNameAttribute_Object=MibTableColumn
cldlServerUserNameAttribute=_CldlServerUserNameAttribute_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,8),_CldlServerUserNameAttribute_Type())
cldlServerUserNameAttribute.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerUserNameAttribute.setStatus(_A)
_CldlServerUserName_Type=DisplayString
_CldlServerUserName_Object=MibTableColumn
cldlServerUserName=_CldlServerUserName_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,9),_CldlServerUserName_Type())
cldlServerUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerUserName.setStatus(_A)
class _CldlServerSecurityEnable_Type(TruthValue):defaultValue=2
_CldlServerSecurityEnable_Type.__name__=_K
_CldlServerSecurityEnable_Object=MibTableColumn
cldlServerSecurityEnable=_CldlServerSecurityEnable_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,10),_CldlServerSecurityEnable_Type())
cldlServerSecurityEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerSecurityEnable.setStatus(_A)
class _CldlServerStorageType_Type(StorageType):defaultValue=3
_CldlServerStorageType_Type.__name__=_J
_CldlServerStorageType_Object=MibTableColumn
cldlServerStorageType=_CldlServerStorageType_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,11),_CldlServerStorageType_Type())
cldlServerStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerStorageType.setStatus(_A)
_CldlServerRowStatus_Type=RowStatus
_CldlServerRowStatus_Object=MibTableColumn
cldlServerRowStatus=_CldlServerRowStatus_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,12),_CldlServerRowStatus_Type())
cldlServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerRowStatus.setStatus(_A)
class _CldlServerBindType_Type(CldlBindType):defaultValue=1
_CldlServerBindType_Type.__name__=_M
_CldlServerBindType_Object=MibTableColumn
cldlServerBindType=_CldlServerBindType_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,13),_CldlServerBindType_Type())
cldlServerBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerBindType.setStatus(_A)
_CldlServerAuthBindUserName_Type=SnmpAdminString
_CldlServerAuthBindUserName_Object=MibTableColumn
cldlServerAuthBindUserName=_CldlServerAuthBindUserName_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,14),_CldlServerAuthBindUserName_Type())
cldlServerAuthBindUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerAuthBindUserName.setStatus(_A)
_CldlServerAuthBindPassword_Type=SnmpAdminString
_CldlServerAuthBindPassword_Object=MibTableColumn
cldlServerAuthBindPassword=_CldlServerAuthBindPassword_Object((1,3,6,1,4,1,9,9,614,1,1,1,1,15),_CldlServerAuthBindPassword_Type())
cldlServerAuthBindPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cldlServerAuthBindPassword.setStatus(_A)
_CldlWlanLdapTable_Object=MibTable
cldlWlanLdapTable=_CldlWlanLdapTable_Object((1,3,6,1,4,1,9,9,614,1,1,2))
if mibBuilder.loadTexts:cldlWlanLdapTable.setStatus(_A)
_CldlWlanLdapEntry_Object=MibTableRow
cldlWlanLdapEntry=_CldlWlanLdapEntry_Object((1,3,6,1,4,1,9,9,614,1,1,2,1))
cldlWlanLdapEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cldlWlanLdapEntry.setStatus(_A)
class _CldlWlanLdapPrimaryServerIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CldlWlanLdapPrimaryServerIndex_Type.__name__=_D
_CldlWlanLdapPrimaryServerIndex_Object=MibTableColumn
cldlWlanLdapPrimaryServerIndex=_CldlWlanLdapPrimaryServerIndex_Object((1,3,6,1,4,1,9,9,614,1,1,2,1,1),_CldlWlanLdapPrimaryServerIndex_Type())
cldlWlanLdapPrimaryServerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cldlWlanLdapPrimaryServerIndex.setStatus(_A)
class _CldlWlanLdapSecondaryServerIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CldlWlanLdapSecondaryServerIndex_Type.__name__=_D
_CldlWlanLdapSecondaryServerIndex_Object=MibTableColumn
cldlWlanLdapSecondaryServerIndex=_CldlWlanLdapSecondaryServerIndex_Object((1,3,6,1,4,1,9,9,614,1,1,2,1,2),_CldlWlanLdapSecondaryServerIndex_Type())
cldlWlanLdapSecondaryServerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cldlWlanLdapSecondaryServerIndex.setStatus(_A)
class _CldlWlanLdapTertiaryServerIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CldlWlanLdapTertiaryServerIndex_Type.__name__=_D
_CldlWlanLdapTertiaryServerIndex_Object=MibTableColumn
cldlWlanLdapTertiaryServerIndex=_CldlWlanLdapTertiaryServerIndex_Object((1,3,6,1,4,1,9,9,614,1,1,2,1,3),_CldlWlanLdapTertiaryServerIndex_Type())
cldlWlanLdapTertiaryServerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cldlWlanLdapTertiaryServerIndex.setStatus(_A)
_CldlStatus_ObjectIdentity=ObjectIdentity
cldlStatus=_CldlStatus_ObjectIdentity((1,3,6,1,4,1,9,9,614,1,2))
_CiscoLwappDot11LdapMIBConform_ObjectIdentity=ObjectIdentity
ciscoLwappDot11LdapMIBConform=_CiscoLwappDot11LdapMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,614,2))
_CiscoLwappDot11LdapMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoLwappDot11LdapMIBCompliances=_CiscoLwappDot11LdapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,614,2,1))
_CiscoLwappDot11LdapMIBGroups_ObjectIdentity=ObjectIdentity
ciscoLwappDot11LdapMIBGroups=_CiscoLwappDot11LdapMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,614,2,2))
ciscoLwappDot11LdapMIBConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,614,2,2,1))
ciscoLwappDot11LdapMIBConfigGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ciscoLwappDot11LdapMIBConfigGroup.setStatus(_A)
ciscoLwappDot11LdapMIBConfigGroupSup1=ObjectGroup((1,3,6,1,4,1,9,9,614,2,2,2))
ciscoLwappDot11LdapMIBConfigGroupSup1.setObjects(*((_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ciscoLwappDot11LdapMIBConfigGroupSup1.setStatus(_A)
ciscoLwappDot11LdapMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,614,2,1,1))
ciscoLwappDot11LdapMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:ciscoLwappDot11LdapMIBCompliance.setStatus('deprecated')
ciscoLwappDot11LdapMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,614,2,1,2))
ciscoLwappDot11LdapMIBComplianceRev1.setObjects(*((_B,_F),(_B,_e)))
if mibBuilder.loadTexts:ciscoLwappDot11LdapMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_M:CldlBindType,'ciscoLwappDot11LdapMIB':ciscoLwappDot11LdapMIB,'ciscoLwappDot11LdapMIBNotifs':ciscoLwappDot11LdapMIBNotifs,'ciscoLwappDot11LdapMIBObjects':ciscoLwappDot11LdapMIBObjects,'cldlConfig':cldlConfig,'cldlServerTable':cldlServerTable,'cldlServerEntry':cldlServerEntry,_L:cldlServerIndex,_N:cldlServerAddressType,_O:cldlServerAddress,_P:cldlServerPortNum,_Q:cldlServerState,_R:cldlServerTimeout,_S:cldlServerUserBase,_T:cldlServerUserNameAttribute,_U:cldlServerUserName,_V:cldlServerSecurityEnable,_X:cldlServerStorageType,_W:cldlServerRowStatus,_b:cldlServerBindType,_c:cldlServerAuthBindUserName,_d:cldlServerAuthBindPassword,'cldlWlanLdapTable':cldlWlanLdapTable,'cldlWlanLdapEntry':cldlWlanLdapEntry,_Y:cldlWlanLdapPrimaryServerIndex,_Z:cldlWlanLdapSecondaryServerIndex,_a:cldlWlanLdapTertiaryServerIndex,'cldlStatus':cldlStatus,'ciscoLwappDot11LdapMIBConform':ciscoLwappDot11LdapMIBConform,'ciscoLwappDot11LdapMIBCompliances':ciscoLwappDot11LdapMIBCompliances,'ciscoLwappDot11LdapMIBCompliance':ciscoLwappDot11LdapMIBCompliance,'ciscoLwappDot11LdapMIBComplianceRev1':ciscoLwappDot11LdapMIBComplianceRev1,'ciscoLwappDot11LdapMIBGroups':ciscoLwappDot11LdapMIBGroups,_F:ciscoLwappDot11LdapMIBConfigGroup,_e:ciscoLwappDot11LdapMIBConfigGroupSup1})