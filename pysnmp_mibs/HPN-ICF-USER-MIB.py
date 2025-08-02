_L='hpnicfUserGroupName'
_K='hpnicfUserRole'
_J='DateAndTime'
_I='read-only'
_H='not-accessible'
_G='DisplayString'
_F='hpnicfUserIndex'
_E='Integer32'
_D='HPN-ICF-USER-MIB'
_C='read-create'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,_G,'MacAddress','PhysAddress','RowStatus','TextualConvention')
hpnicfUser=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,12))
class ServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpnicfUserObjects_ObjectIdentity=ObjectIdentity
hpnicfUserObjects=_HpnicfUserObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,12,1))
_HpnicfUserInfoTable_Object=MibTable
hpnicfUserInfoTable=_HpnicfUserInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,1))
if mibBuilder.loadTexts:hpnicfUserInfoTable.setStatus(_A)
_HpnicfUserInfoEntry_Object=MibTableRow
hpnicfUserInfoEntry=_HpnicfUserInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,1,1))
hpnicfUserInfoEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfUserInfoEntry.setStatus(_A)
_HpnicfUserName_Type=DisplayString
_HpnicfUserName_Object=MibTableColumn
hpnicfUserName=_HpnicfUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,1,1,1),_HpnicfUserName_Type())
hpnicfUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserName.setStatus(_A)
_HpnicfUserPassword_Type=DisplayString
_HpnicfUserPassword_Object=MibTableColumn
hpnicfUserPassword=_HpnicfUserPassword_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,1,1,2),_HpnicfUserPassword_Type())
hpnicfUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserPassword.setStatus(_A)
_HpnicfAuthMode_Type=Integer32
_HpnicfAuthMode_Object=MibTableColumn
hpnicfAuthMode=_HpnicfAuthMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,1,1,3),_HpnicfAuthMode_Type())
hpnicfAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfAuthMode.setStatus(_A)
_HpnicfUserLevel_Type=Integer32
_HpnicfUserLevel_Object=MibTableColumn
hpnicfUserLevel=_HpnicfUserLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,1,1,4),_HpnicfUserLevel_Type())
hpnicfUserLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserLevel.setStatus(_A)
class _HpnicfUserState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('active',0),('block',1)))
_HpnicfUserState_Type.__name__=_E
_HpnicfUserState_Object=MibTableColumn
hpnicfUserState=_HpnicfUserState_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,1,1,5),_HpnicfUserState_Type())
hpnicfUserState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserState.setStatus(_A)
_HpnicfUserInfoRowStatus_Type=RowStatus
_HpnicfUserInfoRowStatus_Object=MibTableColumn
hpnicfUserInfoRowStatus=_HpnicfUserInfoRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,1,1,6),_HpnicfUserInfoRowStatus_Type())
hpnicfUserInfoRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserInfoRowStatus.setStatus(_A)
class _HpnicfUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483646))
_HpnicfUserIndex_Type.__name__=_E
_HpnicfUserIndex_Object=MibTableColumn
hpnicfUserIndex=_HpnicfUserIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,1,1,7),_HpnicfUserIndex_Type())
hpnicfUserIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfUserIndex.setStatus(_A)
_HpnicfUserAttributeTable_Object=MibTable
hpnicfUserAttributeTable=_HpnicfUserAttributeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2))
if mibBuilder.loadTexts:hpnicfUserAttributeTable.setStatus(_A)
_HpnicfUserAttributeEntry_Object=MibTableRow
hpnicfUserAttributeEntry=_HpnicfUserAttributeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1))
hpnicfUserAttributeEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfUserAttributeEntry.setStatus(_A)
_HpnicfAccessLimit_Type=Integer32
_HpnicfAccessLimit_Object=MibTableColumn
hpnicfAccessLimit=_HpnicfAccessLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,1),_HpnicfAccessLimit_Type())
hpnicfAccessLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAccessLimit.setStatus(_A)
_HpnicfIdleCut_Type=Integer32
_HpnicfIdleCut_Object=MibTableColumn
hpnicfIdleCut=_HpnicfIdleCut_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,2),_HpnicfIdleCut_Type())
hpnicfIdleCut.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIdleCut.setStatus(_A)
_HpnicfIPAddress_Type=IpAddress
_HpnicfIPAddress_Object=MibTableColumn
hpnicfIPAddress=_HpnicfIPAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,3),_HpnicfIPAddress_Type())
hpnicfIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIPAddress.setStatus(_A)
_HpnicfNasIPAddress_Type=IpAddress
_HpnicfNasIPAddress_Object=MibTableColumn
hpnicfNasIPAddress=_HpnicfNasIPAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,4),_HpnicfNasIPAddress_Type())
hpnicfNasIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfNasIPAddress.setStatus(_A)
_HpnicfSlotNum_Type=Integer32
_HpnicfSlotNum_Object=MibTableColumn
hpnicfSlotNum=_HpnicfSlotNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,5),_HpnicfSlotNum_Type())
hpnicfSlotNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSlotNum.setStatus(_A)
_HpnicfSubSlotNum_Type=Integer32
_HpnicfSubSlotNum_Object=MibTableColumn
hpnicfSubSlotNum=_HpnicfSubSlotNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,6),_HpnicfSubSlotNum_Type())
hpnicfSubSlotNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSubSlotNum.setStatus(_A)
_HpnicfPortNum_Type=Integer32
_HpnicfPortNum_Object=MibTableColumn
hpnicfPortNum=_HpnicfPortNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,7),_HpnicfPortNum_Type())
hpnicfPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortNum.setStatus(_A)
_HpnicfMacAddress_Type=MacAddress
_HpnicfMacAddress_Object=MibTableColumn
hpnicfMacAddress=_HpnicfMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,8),_HpnicfMacAddress_Type())
hpnicfMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfMacAddress.setStatus(_A)
class _HpnicfVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfVlan_Type.__name__=_E
_HpnicfVlan_Object=MibTableColumn
hpnicfVlan=_HpnicfVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,9),_HpnicfVlan_Type())
hpnicfVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVlan.setStatus(_A)
_HpnicfFtpService_Type=ServiceType
_HpnicfFtpService_Object=MibTableColumn
hpnicfFtpService=_HpnicfFtpService_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,10),_HpnicfFtpService_Type())
hpnicfFtpService.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFtpService.setStatus(_A)
_HpnicfFtpDirectory_Type=OctetString
_HpnicfFtpDirectory_Object=MibTableColumn
hpnicfFtpDirectory=_HpnicfFtpDirectory_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,11),_HpnicfFtpDirectory_Type())
hpnicfFtpDirectory.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFtpDirectory.setStatus(_A)
_HpnicfLanAccessService_Type=ServiceType
_HpnicfLanAccessService_Object=MibTableColumn
hpnicfLanAccessService=_HpnicfLanAccessService_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,12),_HpnicfLanAccessService_Type())
hpnicfLanAccessService.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLanAccessService.setStatus(_A)
_HpnicfSshService_Type=ServiceType
_HpnicfSshService_Object=MibTableColumn
hpnicfSshService=_HpnicfSshService_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,13),_HpnicfSshService_Type())
hpnicfSshService.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfSshService.setStatus(_A)
_HpnicfTelnetService_Type=ServiceType
_HpnicfTelnetService_Object=MibTableColumn
hpnicfTelnetService=_HpnicfTelnetService_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,14),_HpnicfTelnetService_Type())
hpnicfTelnetService.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTelnetService.setStatus(_A)
_HpnicfTerminalService_Type=ServiceType
_HpnicfTerminalService_Object=MibTableColumn
hpnicfTerminalService=_HpnicfTerminalService_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,15),_HpnicfTerminalService_Type())
hpnicfTerminalService.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfTerminalService.setStatus(_A)
class _HpnicfExpirationDate_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HpnicfExpirationDate_Type.__name__=_J
_HpnicfExpirationDate_Object=MibTableColumn
hpnicfExpirationDate=_HpnicfExpirationDate_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,16),_HpnicfExpirationDate_Type())
hpnicfExpirationDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfExpirationDate.setStatus(_A)
_HpnicfUserGroup_Type=DisplayString
_HpnicfUserGroup_Object=MibTableColumn
hpnicfUserGroup=_HpnicfUserGroup_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,17),_HpnicfUserGroup_Type())
hpnicfUserGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfUserGroup.setStatus(_A)
_HpnicfPortalService_Type=ServiceType
_HpnicfPortalService_Object=MibTableColumn
hpnicfPortalService=_HpnicfPortalService_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,18),_HpnicfPortalService_Type())
hpnicfPortalService.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPortalService.setStatus(_A)
_HpnicfPPPService_Type=ServiceType
_HpnicfPPPService_Object=MibTableColumn
hpnicfPPPService=_HpnicfPPPService_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,19),_HpnicfPPPService_Type())
hpnicfPPPService.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfPPPService.setStatus(_A)
_HpnicfHttpService_Type=ServiceType
_HpnicfHttpService_Object=MibTableColumn
hpnicfHttpService=_HpnicfHttpService_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,20),_HpnicfHttpService_Type())
hpnicfHttpService.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfHttpService.setStatus(_A)
_HpnicfHttpsService_Type=ServiceType
_HpnicfHttpsService_Object=MibTableColumn
hpnicfHttpsService=_HpnicfHttpsService_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,21),_HpnicfHttpsService_Type())
hpnicfHttpsService.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfHttpsService.setStatus(_A)
_HpnicfUserIfIndex_Type=Integer32
_HpnicfUserIfIndex_Object=MibTableColumn
hpnicfUserIfIndex=_HpnicfUserIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,2,1,22),_HpnicfUserIfIndex_Type())
hpnicfUserIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfUserIfIndex.setStatus(_A)
_HpnicfUserMaxNum_Type=Integer32
_HpnicfUserMaxNum_Object=MibScalar
hpnicfUserMaxNum=_HpnicfUserMaxNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,3),_HpnicfUserMaxNum_Type())
hpnicfUserMaxNum.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfUserMaxNum.setStatus(_A)
_HpnicfUserCurrNum_Type=Integer32
_HpnicfUserCurrNum_Object=MibScalar
hpnicfUserCurrNum=_HpnicfUserCurrNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,4),_HpnicfUserCurrNum_Type())
hpnicfUserCurrNum.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfUserCurrNum.setStatus(_A)
_HpnicfUserIndexIndicator_Type=Integer32
_HpnicfUserIndexIndicator_Object=MibScalar
hpnicfUserIndexIndicator=_HpnicfUserIndexIndicator_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,5),_HpnicfUserIndexIndicator_Type())
hpnicfUserIndexIndicator.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfUserIndexIndicator.setStatus(_A)
_HpnicfUserRoleTable_Object=MibTable
hpnicfUserRoleTable=_HpnicfUserRoleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,6))
if mibBuilder.loadTexts:hpnicfUserRoleTable.setStatus(_A)
_HpnicfUserRoleEntry_Object=MibTableRow
hpnicfUserRoleEntry=_HpnicfUserRoleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,6,1))
hpnicfUserRoleEntry.setIndexNames((0,_D,_F),(0,_D,_K))
if mibBuilder.loadTexts:hpnicfUserRoleEntry.setStatus(_A)
class _HpnicfUserRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_HpnicfUserRole_Type.__name__=_G
_HpnicfUserRole_Object=MibTableColumn
hpnicfUserRole=_HpnicfUserRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,6,1,1),_HpnicfUserRole_Type())
hpnicfUserRole.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfUserRole.setStatus(_A)
_HpnicfUserRoleStatus_Type=RowStatus
_HpnicfUserRoleStatus_Object=MibTableColumn
hpnicfUserRoleStatus=_HpnicfUserRoleStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,1,6,1,2),_HpnicfUserRoleStatus_Type())
hpnicfUserRoleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserRoleStatus.setStatus(_A)
_HpnicfUserGroupObjects_ObjectIdentity=ObjectIdentity
hpnicfUserGroupObjects=_HpnicfUserGroupObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,12,2))
_HpnicfUserGroupInfoTable_Object=MibTable
hpnicfUserGroupInfoTable=_HpnicfUserGroupInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,2,1))
if mibBuilder.loadTexts:hpnicfUserGroupInfoTable.setStatus(_A)
_HpnicfUserGroupInfoEntry_Object=MibTableRow
hpnicfUserGroupInfoEntry=_HpnicfUserGroupInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,2,1,1))
hpnicfUserGroupInfoEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:hpnicfUserGroupInfoEntry.setStatus(_A)
class _HpnicfUserGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_HpnicfUserGroupName_Type.__name__=_G
_HpnicfUserGroupName_Object=MibTableColumn
hpnicfUserGroupName=_HpnicfUserGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,2,1,1,1),_HpnicfUserGroupName_Type())
hpnicfUserGroupName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfUserGroupName.setStatus(_A)
_HpnicfUserGroupInfoRowStatus_Type=RowStatus
_HpnicfUserGroupInfoRowStatus_Object=MibTableColumn
hpnicfUserGroupInfoRowStatus=_HpnicfUserGroupInfoRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,12,2,1,1,2),_HpnicfUserGroupInfoRowStatus_Type())
hpnicfUserGroupInfoRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserGroupInfoRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ServiceType':ServiceType,'hpnicfUser':hpnicfUser,'hpnicfUserObjects':hpnicfUserObjects,'hpnicfUserInfoTable':hpnicfUserInfoTable,'hpnicfUserInfoEntry':hpnicfUserInfoEntry,'hpnicfUserName':hpnicfUserName,'hpnicfUserPassword':hpnicfUserPassword,'hpnicfAuthMode':hpnicfAuthMode,'hpnicfUserLevel':hpnicfUserLevel,'hpnicfUserState':hpnicfUserState,'hpnicfUserInfoRowStatus':hpnicfUserInfoRowStatus,_F:hpnicfUserIndex,'hpnicfUserAttributeTable':hpnicfUserAttributeTable,'hpnicfUserAttributeEntry':hpnicfUserAttributeEntry,'hpnicfAccessLimit':hpnicfAccessLimit,'hpnicfIdleCut':hpnicfIdleCut,'hpnicfIPAddress':hpnicfIPAddress,'hpnicfNasIPAddress':hpnicfNasIPAddress,'hpnicfSlotNum':hpnicfSlotNum,'hpnicfSubSlotNum':hpnicfSubSlotNum,'hpnicfPortNum':hpnicfPortNum,'hpnicfMacAddress':hpnicfMacAddress,'hpnicfVlan':hpnicfVlan,'hpnicfFtpService':hpnicfFtpService,'hpnicfFtpDirectory':hpnicfFtpDirectory,'hpnicfLanAccessService':hpnicfLanAccessService,'hpnicfSshService':hpnicfSshService,'hpnicfTelnetService':hpnicfTelnetService,'hpnicfTerminalService':hpnicfTerminalService,'hpnicfExpirationDate':hpnicfExpirationDate,'hpnicfUserGroup':hpnicfUserGroup,'hpnicfPortalService':hpnicfPortalService,'hpnicfPPPService':hpnicfPPPService,'hpnicfHttpService':hpnicfHttpService,'hpnicfHttpsService':hpnicfHttpsService,'hpnicfUserIfIndex':hpnicfUserIfIndex,'hpnicfUserMaxNum':hpnicfUserMaxNum,'hpnicfUserCurrNum':hpnicfUserCurrNum,'hpnicfUserIndexIndicator':hpnicfUserIndexIndicator,'hpnicfUserRoleTable':hpnicfUserRoleTable,'hpnicfUserRoleEntry':hpnicfUserRoleEntry,_K:hpnicfUserRole,'hpnicfUserRoleStatus':hpnicfUserRoleStatus,'hpnicfUserGroupObjects':hpnicfUserGroupObjects,'hpnicfUserGroupInfoTable':hpnicfUserGroupInfoTable,'hpnicfUserGroupInfoEntry':hpnicfUserGroupInfoEntry,_L:hpnicfUserGroupName,'hpnicfUserGroupInfoRowStatus':hpnicfUserGroupInfoRowStatus})