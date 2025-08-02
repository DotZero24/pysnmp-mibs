_b='h3cSecureBindingIndex'
_a='not-accessible'
_Z='h3cSecureOUIIndex'
_Y='h3cSecureAddrVlanID'
_X='notAvailable'
_W='accessible-for-notify'
_V='enabled'
_U='TruthValue'
_T='ifAdminStatus'
_S='dot1xAuthSessionTerminateCause'
_R='dot1xAuthSessionAuthenticMethod'
_Q='read-only'
_P='disabled'
_O='OctetString'
_N='h3cSecureRalmAuthUsername'
_M='h3cSecureRalmAuthMode'
_L='dot1xAuthSessionUserName'
_K='h3cSecurePortVlanMembershipList'
_J='DisplayString'
_I='IEEE8021-PAE-MIB'
_H='read-create'
_G='h3cSecureAddrMAC'
_F='ifIndex'
_E='Integer32'
_D='IF-MIB'
_C='read-write'
_B='A3COM-HUAWEI-PORT-SECURITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cPortSecurity,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cPortSecurity')
dot1xAuthSessionAuthenticMethod,dot1xAuthSessionTerminateCause,dot1xAuthSessionUserName,dot1xPaePortNumber=mibBuilder.importSymbols(_I,_R,_S,_L,'dot1xPaePortNumber')
ifAdminStatus,ifIndex=mibBuilder.importSymbols(_D,_T,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention',_U)
h3cPortSecurityMIB=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,26,1))
if mibBuilder.loadTexts:h3cPortSecurityMIB.setRevisions(('2004-11-24 00:00',))
_H3cPortSecurityLeaf_ObjectIdentity=ObjectIdentity
h3cPortSecurityLeaf=_H3cPortSecurityLeaf_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,26,1,1))
class _H3cSecurePortSecurityControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_P,2)))
_H3cSecurePortSecurityControl_Type.__name__=_E
_H3cSecurePortSecurityControl_Object=MibScalar
h3cSecurePortSecurityControl=_H3cSecurePortSecurityControl_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,1),_H3cSecurePortSecurityControl_Type())
h3cSecurePortSecurityControl.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecurePortSecurityControl.setStatus(_A)
class _H3cSecurePortVlanMembershipList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSecurePortVlanMembershipList_Type.__name__=_J
_H3cSecurePortVlanMembershipList_Object=MibScalar
h3cSecurePortVlanMembershipList=_H3cSecurePortVlanMembershipList_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,2),_H3cSecurePortVlanMembershipList_Type())
h3cSecurePortVlanMembershipList.setMaxAccess(_W)
if mibBuilder.loadTexts:h3cSecurePortVlanMembershipList.setStatus(_A)
_H3cSecureRalmObjects_ObjectIdentity=ObjectIdentity
h3cSecureRalmObjects=_H3cSecureRalmObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,26,1,1,4))
class _H3cSecureRalmDefaultSessionTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_H3cSecureRalmDefaultSessionTime_Type.__name__=_E
_H3cSecureRalmDefaultSessionTime_Object=MibScalar
h3cSecureRalmDefaultSessionTime=_H3cSecureRalmDefaultSessionTime_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,4,1),_H3cSecureRalmDefaultSessionTime_Type())
h3cSecureRalmDefaultSessionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureRalmDefaultSessionTime.setStatus(_A)
class _H3cSecureRalmHoldoffTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_H3cSecureRalmHoldoffTime_Type.__name__=_E
_H3cSecureRalmHoldoffTime_Object=MibScalar
h3cSecureRalmHoldoffTime=_H3cSecureRalmHoldoffTime_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,4,2),_H3cSecureRalmHoldoffTime_Type())
h3cSecureRalmHoldoffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureRalmHoldoffTime.setStatus(_A)
_H3cSecureRalmReauthenticate_Type=MacAddress
_H3cSecureRalmReauthenticate_Object=MibScalar
h3cSecureRalmReauthenticate=_H3cSecureRalmReauthenticate_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,4,3),_H3cSecureRalmReauthenticate_Type())
h3cSecureRalmReauthenticate.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureRalmReauthenticate.setStatus(_A)
class _H3cSecureRalmAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('papUsernameAsMacAddress',1),('papUsernameFixed',2)))
_H3cSecureRalmAuthMode_Type.__name__=_E
_H3cSecureRalmAuthMode_Object=MibScalar
h3cSecureRalmAuthMode=_H3cSecureRalmAuthMode_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,4,4),_H3cSecureRalmAuthMode_Type())
h3cSecureRalmAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureRalmAuthMode.setStatus(_A)
class _H3cSecureRalmAuthUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_H3cSecureRalmAuthUsername_Type.__name__=_J
_H3cSecureRalmAuthUsername_Object=MibScalar
h3cSecureRalmAuthUsername=_H3cSecureRalmAuthUsername_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,4,5),_H3cSecureRalmAuthUsername_Type())
h3cSecureRalmAuthUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureRalmAuthUsername.setStatus(_A)
class _H3cSecureRalmAuthPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cSecureRalmAuthPassword_Type.__name__=_J
_H3cSecureRalmAuthPassword_Object=MibScalar
h3cSecureRalmAuthPassword=_H3cSecureRalmAuthPassword_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,4,6),_H3cSecureRalmAuthPassword_Type())
h3cSecureRalmAuthPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureRalmAuthPassword.setStatus(_A)
class _H3cSecureRalmAuthDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_H3cSecureRalmAuthDomain_Type.__name__=_J
_H3cSecureRalmAuthDomain_Object=MibScalar
h3cSecureRalmAuthDomain=_H3cSecureRalmAuthDomain_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,4,7),_H3cSecureRalmAuthDomain_Type())
h3cSecureRalmAuthDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureRalmAuthDomain.setStatus(_A)
class _H3cSecureRalmAuthOfflineTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cSecureRalmAuthOfflineTime_Type.__name__=_E
_H3cSecureRalmAuthOfflineTime_Object=MibScalar
h3cSecureRalmAuthOfflineTime=_H3cSecureRalmAuthOfflineTime_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,4,8),_H3cSecureRalmAuthOfflineTime_Type())
h3cSecureRalmAuthOfflineTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureRalmAuthOfflineTime.setStatus(_A)
class _H3cSecureRalmAuthServerTimeoutTime_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cSecureRalmAuthServerTimeoutTime_Type.__name__=_E
_H3cSecureRalmAuthServerTimeoutTime_Object=MibScalar
h3cSecureRalmAuthServerTimeoutTime=_H3cSecureRalmAuthServerTimeoutTime_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,4,9),_H3cSecureRalmAuthServerTimeoutTime_Type())
h3cSecureRalmAuthServerTimeoutTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureRalmAuthServerTimeoutTime.setStatus(_A)
class _H3cSecureMacControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_P,2)))
_H3cSecureMacControl_Type.__name__=_E
_H3cSecureMacControl_Object=MibScalar
h3cSecureMacControl=_H3cSecureMacControl_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,1,4,10),_H3cSecureMacControl_Type())
h3cSecureMacControl.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureMacControl.setStatus(_A)
_H3cPortSecurityTables_ObjectIdentity=ObjectIdentity
h3cPortSecurityTables=_H3cPortSecurityTables_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,26,1,2))
_H3cSecurePortTable_Object=MibTable
h3cSecurePortTable=_H3cSecurePortTable_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,1))
if mibBuilder.loadTexts:h3cSecurePortTable.setStatus(_A)
_H3cSecurePortEntry_Object=MibTableRow
h3cSecurePortEntry=_H3cSecurePortEntry_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,1,1))
h3cSecurePortEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cSecurePortEntry.setStatus(_A)
class _H3cSecurePortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('noRestrictions',1),('continuousLearning',2),('autoLearn',3),('secure',4),('userLogin',5),('userLoginSecure',6),('userLoginWithOUI',7),('macAddressWithRadius',8),('macAddressOrUserLoginSecure',9),('macAddressElseUserLoginSecure',10),('userLoginSecureExt',11),('macAddressOrUserLoginSecureExt',12),('macAddressElseUserLoginSecureExt',13),('macAddressAndUserLoginSecure',14),('macAddressAndUserLoginSecureExt',15)))
_H3cSecurePortMode_Type.__name__=_E
_H3cSecurePortMode_Object=MibTableColumn
h3cSecurePortMode=_H3cSecurePortMode_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,1,1,1),_H3cSecurePortMode_Type())
h3cSecurePortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecurePortMode.setStatus(_A)
class _H3cSecureNeedToKnowMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,1),(_P,2),('needToKnowOnly',3),('needToKnowWithBroadcastsAllowed',4),('needToKnowWithMulticastsAllowed',5),('permanentNeedToKnowOnly',6),('permanentNeedToKnowWithBroadcastsAllowed',7),('permanentNeedToKnowWithMulticastsAllowed',8)))
_H3cSecureNeedToKnowMode_Type.__name__=_E
_H3cSecureNeedToKnowMode_Object=MibTableColumn
h3cSecureNeedToKnowMode=_H3cSecureNeedToKnowMode_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,1,1,2),_H3cSecureNeedToKnowMode_Type())
h3cSecureNeedToKnowMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureNeedToKnowMode.setStatus(_A)
class _H3cSecureIntrusionAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_X,1),('noAction',2),('disablePort',3),('disablePortTemporarily',4),('allowDefaultAccess',5),('blockMacAddress',6)))
_H3cSecureIntrusionAction_Type.__name__=_E
_H3cSecureIntrusionAction_Object=MibTableColumn
h3cSecureIntrusionAction=_H3cSecureIntrusionAction_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,1,1,3),_H3cSecureIntrusionAction_Type())
h3cSecureIntrusionAction.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureIntrusionAction.setStatus(_A)
_H3cSecureNumberAddresses_Type=Integer32
_H3cSecureNumberAddresses_Object=MibTableColumn
h3cSecureNumberAddresses=_H3cSecureNumberAddresses_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,1,1,4),_H3cSecureNumberAddresses_Type())
h3cSecureNumberAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureNumberAddresses.setStatus(_A)
_H3cSecureNumberAddressesStored_Type=Integer32
_H3cSecureNumberAddressesStored_Object=MibTableColumn
h3cSecureNumberAddressesStored=_H3cSecureNumberAddressesStored_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,1,1,5),_H3cSecureNumberAddressesStored_Type())
h3cSecureNumberAddressesStored.setMaxAccess(_Q)
if mibBuilder.loadTexts:h3cSecureNumberAddressesStored.setStatus(_A)
_H3cSecureMaximumAddresses_Type=Integer32
_H3cSecureMaximumAddresses_Object=MibTableColumn
h3cSecureMaximumAddresses=_H3cSecureMaximumAddresses_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,1,1,6),_H3cSecureMaximumAddresses_Type())
h3cSecureMaximumAddresses.setMaxAccess(_Q)
if mibBuilder.loadTexts:h3cSecureMaximumAddresses.setStatus(_A)
_H3cSecureAddressTable_Object=MibTable
h3cSecureAddressTable=_H3cSecureAddressTable_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,2))
if mibBuilder.loadTexts:h3cSecureAddressTable.setStatus(_A)
_H3cSecureAddressEntry_Object=MibTableRow
h3cSecureAddressEntry=_H3cSecureAddressEntry_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,2,1))
h3cSecureAddressEntry.setIndexNames((0,_D,_F),(0,_B,_G),(0,_B,_Y))
if mibBuilder.loadTexts:h3cSecureAddressEntry.setStatus(_A)
_H3cSecureAddrMAC_Type=MacAddress
_H3cSecureAddrMAC_Object=MibTableColumn
h3cSecureAddrMAC=_H3cSecureAddrMAC_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,2,1,1),_H3cSecureAddrMAC_Type())
h3cSecureAddrMAC.setMaxAccess(_W)
if mibBuilder.loadTexts:h3cSecureAddrMAC.setStatus(_A)
_H3cSecureAddrVlanID_Type=Integer32
_H3cSecureAddrVlanID_Object=MibTableColumn
h3cSecureAddrVlanID=_H3cSecureAddrVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,2,1,2),_H3cSecureAddrVlanID_Type())
h3cSecureAddrVlanID.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSecureAddrVlanID.setStatus(_A)
class _H3cSecureAddrMACStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('addressBlackhole',1),('addressUserConfig',2),('addressDot1xAuth',3),('addressRALM',4)))
_H3cSecureAddrMACStatus_Type.__name__=_E
_H3cSecureAddrMACStatus_Object=MibTableColumn
h3cSecureAddrMACStatus=_H3cSecureAddrMACStatus_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,2,1,3),_H3cSecureAddrMACStatus_Type())
h3cSecureAddrMACStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSecureAddrMACStatus.setStatus(_A)
_H3cSecureAddrRowStatus_Type=RowStatus
_H3cSecureAddrRowStatus_Object=MibTableColumn
h3cSecureAddrRowStatus=_H3cSecureAddrRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,2,1,4),_H3cSecureAddrRowStatus_Type())
h3cSecureAddrRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSecureAddrRowStatus.setStatus(_A)
_H3cSecureOUITable_Object=MibTable
h3cSecureOUITable=_H3cSecureOUITable_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,3))
if mibBuilder.loadTexts:h3cSecureOUITable.setStatus(_A)
_H3cSecureOUIEntry_Object=MibTableRow
h3cSecureOUIEntry=_H3cSecureOUIEntry_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,3,1))
h3cSecureOUIEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:h3cSecureOUIEntry.setStatus(_A)
class _H3cSecureOUIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_H3cSecureOUIIndex_Type.__name__=_E
_H3cSecureOUIIndex_Object=MibTableColumn
h3cSecureOUIIndex=_H3cSecureOUIIndex_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,3,1,1),_H3cSecureOUIIndex_Type())
h3cSecureOUIIndex.setMaxAccess(_a)
if mibBuilder.loadTexts:h3cSecureOUIIndex.setStatus(_A)
class _H3cSecureOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_H3cSecureOUI_Type.__name__=_O
_H3cSecureOUI_Object=MibTableColumn
h3cSecureOUI=_H3cSecureOUI_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,3,1,2),_H3cSecureOUI_Type())
h3cSecureOUI.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSecureOUI.setStatus(_A)
_H3cSecureOUIRowStatus_Type=RowStatus
_H3cSecureOUIRowStatus_Object=MibTableColumn
h3cSecureOUIRowStatus=_H3cSecureOUIRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,3,1,3),_H3cSecureOUIRowStatus_Type())
h3cSecureOUIRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSecureOUIRowStatus.setStatus(_A)
_H3cSecureBindingTable_Object=MibTable
h3cSecureBindingTable=_H3cSecureBindingTable_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,4))
if mibBuilder.loadTexts:h3cSecureBindingTable.setStatus(_A)
_H3cSecureBindingEntry_Object=MibTableRow
h3cSecureBindingEntry=_H3cSecureBindingEntry_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,4,1))
h3cSecureBindingEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:h3cSecureBindingEntry.setStatus(_A)
_H3cSecureBindingIndex_Type=Integer32
_H3cSecureBindingIndex_Object=MibTableColumn
h3cSecureBindingIndex=_H3cSecureBindingIndex_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,4,1,1),_H3cSecureBindingIndex_Type())
h3cSecureBindingIndex.setMaxAccess(_a)
if mibBuilder.loadTexts:h3cSecureBindingIndex.setStatus(_A)
_H3cSecureBindingPort_Type=Integer32
_H3cSecureBindingPort_Object=MibTableColumn
h3cSecureBindingPort=_H3cSecureBindingPort_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,4,1,2),_H3cSecureBindingPort_Type())
h3cSecureBindingPort.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSecureBindingPort.setStatus(_A)
_H3cSecureBindingAddrMAC_Type=MacAddress
_H3cSecureBindingAddrMAC_Object=MibTableColumn
h3cSecureBindingAddrMAC=_H3cSecureBindingAddrMAC_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,4,1,3),_H3cSecureBindingAddrMAC_Type())
h3cSecureBindingAddrMAC.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSecureBindingAddrMAC.setStatus(_A)
_H3cSecureBindingAddrIp_Type=IpAddress
_H3cSecureBindingAddrIp_Object=MibTableColumn
h3cSecureBindingAddrIp=_H3cSecureBindingAddrIp_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,4,1,4),_H3cSecureBindingAddrIp_Type())
h3cSecureBindingAddrIp.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSecureBindingAddrIp.setStatus(_A)
_H3cSecureBindingRowStatus_Type=RowStatus
_H3cSecureBindingRowStatus_Object=MibTableColumn
h3cSecureBindingRowStatus=_H3cSecureBindingRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,4,1,5),_H3cSecureBindingRowStatus_Type())
h3cSecureBindingRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSecureBindingRowStatus.setStatus(_A)
_H3cSecureAssignTable_Object=MibTable
h3cSecureAssignTable=_H3cSecureAssignTable_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,5))
if mibBuilder.loadTexts:h3cSecureAssignTable.setStatus(_A)
_H3cSecureAssignEntry_Object=MibTableRow
h3cSecureAssignEntry=_H3cSecureAssignEntry_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,5,1))
h3cSecureAssignEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:h3cSecureAssignEntry.setStatus(_A)
class _H3cSecureAssignEnable_Type(TruthValue):defaultValue=1
_H3cSecureAssignEnable_Type.__name__=_U
_H3cSecureAssignEnable_Object=MibTableColumn
h3cSecureAssignEnable=_H3cSecureAssignEnable_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,5,1,1),_H3cSecureAssignEnable_Type())
h3cSecureAssignEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cSecureAssignEnable.setStatus(_A)
class _H3cSecureVlanAssignment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cSecureVlanAssignment_Type.__name__=_O
_H3cSecureVlanAssignment_Object=MibTableColumn
h3cSecureVlanAssignment=_H3cSecureVlanAssignment_Object((1,3,6,1,4,1,43,45,1,10,2,26,1,2,5,1,2),_H3cSecureVlanAssignment_Type())
h3cSecureVlanAssignment.setMaxAccess(_Q)
if mibBuilder.loadTexts:h3cSecureVlanAssignment.setStatus(_A)
_H3cPortSecurityNotifications_ObjectIdentity=ObjectIdentity
h3cPortSecurityNotifications=_H3cPortSecurityNotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,26,1,3))
h3cSecureAddressLearned=NotificationType((1,3,6,1,4,1,43,45,1,10,2,26,1,3,1))
h3cSecureAddressLearned.setObjects(*((_D,_F),(_B,_G)))
if mibBuilder.loadTexts:h3cSecureAddressLearned.setStatus(_A)
h3cSecureViolation=NotificationType((1,3,6,1,4,1,43,45,1,10,2,26,1,3,2))
h3cSecureViolation.setObjects(*((_D,_F),(_B,_G),(_D,_T)))
if mibBuilder.loadTexts:h3cSecureViolation.setStatus(_A)
h3cSecureLoginFailure=NotificationType((1,3,6,1,4,1,43,45,1,10,2,26,1,3,3))
h3cSecureLoginFailure.setObjects(*((_D,_F),(_B,_G),(_I,_L)))
if mibBuilder.loadTexts:h3cSecureLoginFailure.setStatus(_A)
h3cSecureLogon=NotificationType((1,3,6,1,4,1,43,45,1,10,2,26,1,3,4))
h3cSecureLogon.setObjects(*((_D,_F),(_B,_G),(_I,_L),(_I,_R),(_B,_K)))
if mibBuilder.loadTexts:h3cSecureLogon.setStatus(_A)
h3cSecureLogoff=NotificationType((1,3,6,1,4,1,43,45,1,10,2,26,1,3,5))
h3cSecureLogoff.setObjects(*((_D,_F),(_B,_G),(_I,_L),(_I,_S),(_B,_K)))
if mibBuilder.loadTexts:h3cSecureLogoff.setStatus(_A)
h3cSecureRalmLoginFailure=NotificationType((1,3,6,1,4,1,43,45,1,10,2,26,1,3,6))
h3cSecureRalmLoginFailure.setObjects(*((_D,_F),(_B,_G),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:h3cSecureRalmLoginFailure.setStatus(_A)
h3cSecureRalmLogon=NotificationType((1,3,6,1,4,1,43,45,1,10,2,26,1,3,7))
h3cSecureRalmLogon.setObjects(*((_D,_F),(_B,_G),(_B,_M),(_B,_N),(_B,_K)))
if mibBuilder.loadTexts:h3cSecureRalmLogon.setStatus(_A)
h3cSecureRalmLogoff=NotificationType((1,3,6,1,4,1,43,45,1,10,2,26,1,3,8))
h3cSecureRalmLogoff.setObjects(*((_D,_F),(_B,_G),(_B,_M),(_B,_N),(_B,_K)))
if mibBuilder.loadTexts:h3cSecureRalmLogoff.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cPortSecurityMIB':h3cPortSecurityMIB,'h3cPortSecurityLeaf':h3cPortSecurityLeaf,'h3cSecurePortSecurityControl':h3cSecurePortSecurityControl,_K:h3cSecurePortVlanMembershipList,'h3cSecureRalmObjects':h3cSecureRalmObjects,'h3cSecureRalmDefaultSessionTime':h3cSecureRalmDefaultSessionTime,'h3cSecureRalmHoldoffTime':h3cSecureRalmHoldoffTime,'h3cSecureRalmReauthenticate':h3cSecureRalmReauthenticate,_M:h3cSecureRalmAuthMode,_N:h3cSecureRalmAuthUsername,'h3cSecureRalmAuthPassword':h3cSecureRalmAuthPassword,'h3cSecureRalmAuthDomain':h3cSecureRalmAuthDomain,'h3cSecureRalmAuthOfflineTime':h3cSecureRalmAuthOfflineTime,'h3cSecureRalmAuthServerTimeoutTime':h3cSecureRalmAuthServerTimeoutTime,'h3cSecureMacControl':h3cSecureMacControl,'h3cPortSecurityTables':h3cPortSecurityTables,'h3cSecurePortTable':h3cSecurePortTable,'h3cSecurePortEntry':h3cSecurePortEntry,'h3cSecurePortMode':h3cSecurePortMode,'h3cSecureNeedToKnowMode':h3cSecureNeedToKnowMode,'h3cSecureIntrusionAction':h3cSecureIntrusionAction,'h3cSecureNumberAddresses':h3cSecureNumberAddresses,'h3cSecureNumberAddressesStored':h3cSecureNumberAddressesStored,'h3cSecureMaximumAddresses':h3cSecureMaximumAddresses,'h3cSecureAddressTable':h3cSecureAddressTable,'h3cSecureAddressEntry':h3cSecureAddressEntry,_G:h3cSecureAddrMAC,_Y:h3cSecureAddrVlanID,'h3cSecureAddrMACStatus':h3cSecureAddrMACStatus,'h3cSecureAddrRowStatus':h3cSecureAddrRowStatus,'h3cSecureOUITable':h3cSecureOUITable,'h3cSecureOUIEntry':h3cSecureOUIEntry,_Z:h3cSecureOUIIndex,'h3cSecureOUI':h3cSecureOUI,'h3cSecureOUIRowStatus':h3cSecureOUIRowStatus,'h3cSecureBindingTable':h3cSecureBindingTable,'h3cSecureBindingEntry':h3cSecureBindingEntry,_b:h3cSecureBindingIndex,'h3cSecureBindingPort':h3cSecureBindingPort,'h3cSecureBindingAddrMAC':h3cSecureBindingAddrMAC,'h3cSecureBindingAddrIp':h3cSecureBindingAddrIp,'h3cSecureBindingRowStatus':h3cSecureBindingRowStatus,'h3cSecureAssignTable':h3cSecureAssignTable,'h3cSecureAssignEntry':h3cSecureAssignEntry,'h3cSecureAssignEnable':h3cSecureAssignEnable,'h3cSecureVlanAssignment':h3cSecureVlanAssignment,'h3cPortSecurityNotifications':h3cPortSecurityNotifications,'h3cSecureAddressLearned':h3cSecureAddressLearned,'h3cSecureViolation':h3cSecureViolation,'h3cSecureLoginFailure':h3cSecureLoginFailure,'h3cSecureLogon':h3cSecureLogon,'h3cSecureLogoff':h3cSecureLogoff,'h3cSecureRalmLoginFailure':h3cSecureRalmLoginFailure,'h3cSecureRalmLogon':h3cSecureRalmLogon,'h3cSecureRalmLogoff':h3cSecureRalmLogoff})