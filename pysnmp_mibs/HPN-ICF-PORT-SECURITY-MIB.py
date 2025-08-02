_b='hpnicfSecureBindingIndex'
_a='not-accessible'
_Z='hpnicfSecureOUIIndex'
_Y='hpnicfSecureAddrVlanID'
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
_N='hpnicfSecureRalmAuthUsername'
_M='hpnicfSecureRalmAuthMode'
_L='dot1xAuthSessionUserName'
_K='hpnicfSecurePortVlanMembershipList'
_J='DisplayString'
_I='IEEE8021-PAE-MIB'
_H='read-create'
_G='hpnicfSecureAddrMAC'
_F='ifIndex'
_E='Integer32'
_D='IF-MIB'
_C='read-write'
_B='HPN-ICF-PORT-SECURITY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfPortSecurity,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfPortSecurity')
dot1xAuthSessionAuthenticMethod,dot1xAuthSessionTerminateCause,dot1xAuthSessionUserName,dot1xPaePortNumber=mibBuilder.importSymbols(_I,_R,_S,_L,'dot1xPaePortNumber')
ifAdminStatus,ifIndex=mibBuilder.importSymbols(_D,_T,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention',_U)
hpnicfPortSecurityMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,26,1))
if mibBuilder.loadTexts:hpnicfPortSecurityMIB.setRevisions(('2004-11-24 00:00',))
_HpnicfPortSecurityLeaf_ObjectIdentity=ObjectIdentity
hpnicfPortSecurityLeaf=_HpnicfPortSecurityLeaf_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1))
class _HpnicfSecurePortSecurityControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_P,2)))
_HpnicfSecurePortSecurityControl_Type.__name__=_E
_HpnicfSecurePortSecurityControl_Object=MibScalar
hpnicfSecurePortSecurityControl=_HpnicfSecurePortSecurityControl_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,1),_HpnicfSecurePortSecurityControl_Type())
hpnicfSecurePortSecurityControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecurePortSecurityControl.setStatus(_A)
class _HpnicfSecurePortVlanMembershipList_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSecurePortVlanMembershipList_Type.__name__=_J
_HpnicfSecurePortVlanMembershipList_Object=MibScalar
hpnicfSecurePortVlanMembershipList=_HpnicfSecurePortVlanMembershipList_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,2),_HpnicfSecurePortVlanMembershipList_Type())
hpnicfSecurePortVlanMembershipList.setMaxAccess(_W)
if mibBuilder.loadTexts:hpnicfSecurePortVlanMembershipList.setStatus(_A)
_HpnicfSecureRalmObjects_ObjectIdentity=ObjectIdentity
hpnicfSecureRalmObjects=_HpnicfSecureRalmObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,4))
class _HpnicfSecureRalmDefaultSessionTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_HpnicfSecureRalmDefaultSessionTime_Type.__name__=_E
_HpnicfSecureRalmDefaultSessionTime_Object=MibScalar
hpnicfSecureRalmDefaultSessionTime=_HpnicfSecureRalmDefaultSessionTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,4,1),_HpnicfSecureRalmDefaultSessionTime_Type())
hpnicfSecureRalmDefaultSessionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureRalmDefaultSessionTime.setStatus(_A)
class _HpnicfSecureRalmHoldoffTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_HpnicfSecureRalmHoldoffTime_Type.__name__=_E
_HpnicfSecureRalmHoldoffTime_Object=MibScalar
hpnicfSecureRalmHoldoffTime=_HpnicfSecureRalmHoldoffTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,4,2),_HpnicfSecureRalmHoldoffTime_Type())
hpnicfSecureRalmHoldoffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureRalmHoldoffTime.setStatus(_A)
_HpnicfSecureRalmReauthenticate_Type=MacAddress
_HpnicfSecureRalmReauthenticate_Object=MibScalar
hpnicfSecureRalmReauthenticate=_HpnicfSecureRalmReauthenticate_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,4,3),_HpnicfSecureRalmReauthenticate_Type())
hpnicfSecureRalmReauthenticate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureRalmReauthenticate.setStatus(_A)
class _HpnicfSecureRalmAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('papUsernameAsMacAddress',1),('papUsernameFixed',2)))
_HpnicfSecureRalmAuthMode_Type.__name__=_E
_HpnicfSecureRalmAuthMode_Object=MibScalar
hpnicfSecureRalmAuthMode=_HpnicfSecureRalmAuthMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,4,4),_HpnicfSecureRalmAuthMode_Type())
hpnicfSecureRalmAuthMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureRalmAuthMode.setStatus(_A)
class _HpnicfSecureRalmAuthUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_HpnicfSecureRalmAuthUsername_Type.__name__=_J
_HpnicfSecureRalmAuthUsername_Object=MibScalar
hpnicfSecureRalmAuthUsername=_HpnicfSecureRalmAuthUsername_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,4,5),_HpnicfSecureRalmAuthUsername_Type())
hpnicfSecureRalmAuthUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureRalmAuthUsername.setStatus(_A)
class _HpnicfSecureRalmAuthPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfSecureRalmAuthPassword_Type.__name__=_J
_HpnicfSecureRalmAuthPassword_Object=MibScalar
hpnicfSecureRalmAuthPassword=_HpnicfSecureRalmAuthPassword_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,4,6),_HpnicfSecureRalmAuthPassword_Type())
hpnicfSecureRalmAuthPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureRalmAuthPassword.setStatus(_A)
class _HpnicfSecureRalmAuthDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,24))
_HpnicfSecureRalmAuthDomain_Type.__name__=_J
_HpnicfSecureRalmAuthDomain_Object=MibScalar
hpnicfSecureRalmAuthDomain=_HpnicfSecureRalmAuthDomain_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,4,7),_HpnicfSecureRalmAuthDomain_Type())
hpnicfSecureRalmAuthDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureRalmAuthDomain.setStatus(_A)
class _HpnicfSecureRalmAuthOfflineTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,2147483647))
_HpnicfSecureRalmAuthOfflineTime_Type.__name__=_E
_HpnicfSecureRalmAuthOfflineTime_Object=MibScalar
hpnicfSecureRalmAuthOfflineTime=_HpnicfSecureRalmAuthOfflineTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,4,8),_HpnicfSecureRalmAuthOfflineTime_Type())
hpnicfSecureRalmAuthOfflineTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureRalmAuthOfflineTime.setStatus(_A)
class _HpnicfSecureRalmAuthServerTimeoutTime_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfSecureRalmAuthServerTimeoutTime_Type.__name__=_E
_HpnicfSecureRalmAuthServerTimeoutTime_Object=MibScalar
hpnicfSecureRalmAuthServerTimeoutTime=_HpnicfSecureRalmAuthServerTimeoutTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,4,9),_HpnicfSecureRalmAuthServerTimeoutTime_Type())
hpnicfSecureRalmAuthServerTimeoutTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureRalmAuthServerTimeoutTime.setStatus(_A)
class _HpnicfSecureMacControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_P,2)))
_HpnicfSecureMacControl_Type.__name__=_E
_HpnicfSecureMacControl_Object=MibScalar
hpnicfSecureMacControl=_HpnicfSecureMacControl_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,1,4,10),_HpnicfSecureMacControl_Type())
hpnicfSecureMacControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureMacControl.setStatus(_A)
_HpnicfPortSecurityTables_ObjectIdentity=ObjectIdentity
hpnicfPortSecurityTables=_HpnicfPortSecurityTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2))
_HpnicfSecurePortTable_Object=MibTable
hpnicfSecurePortTable=_HpnicfSecurePortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,1))
if mibBuilder.loadTexts:hpnicfSecurePortTable.setStatus(_A)
_HpnicfSecurePortEntry_Object=MibTableRow
hpnicfSecurePortEntry=_HpnicfSecurePortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,1,1))
hpnicfSecurePortEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfSecurePortEntry.setStatus(_A)
class _HpnicfSecurePortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('noRestrictions',1),('continuousLearning',2),('autoLearn',3),('secure',4),('userLogin',5),('userLoginSecure',6),('userLoginWithOUI',7),('macAddressWithRadius',8),('macAddressOrUserLoginSecure',9),('macAddressElseUserLoginSecure',10),('userLoginSecureExt',11),('macAddressOrUserLoginSecureExt',12),('macAddressElseUserLoginSecureExt',13),('macAddressAndUserLoginSecure',14),('macAddressAndUserLoginSecureExt',15)))
_HpnicfSecurePortMode_Type.__name__=_E
_HpnicfSecurePortMode_Object=MibTableColumn
hpnicfSecurePortMode=_HpnicfSecurePortMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,1,1,1),_HpnicfSecurePortMode_Type())
hpnicfSecurePortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecurePortMode.setStatus(_A)
class _HpnicfSecureNeedToKnowMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,1),(_P,2),('needToKnowOnly',3),('needToKnowWithBroadcastsAllowed',4),('needToKnowWithMulticastsAllowed',5),('permanentNeedToKnowOnly',6),('permanentNeedToKnowWithBroadcastsAllowed',7),('permanentNeedToKnowWithMulticastsAllowed',8)))
_HpnicfSecureNeedToKnowMode_Type.__name__=_E
_HpnicfSecureNeedToKnowMode_Object=MibTableColumn
hpnicfSecureNeedToKnowMode=_HpnicfSecureNeedToKnowMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,1,1,2),_HpnicfSecureNeedToKnowMode_Type())
hpnicfSecureNeedToKnowMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureNeedToKnowMode.setStatus(_A)
class _HpnicfSecureIntrusionAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_X,1),('noAction',2),('disablePort',3),('disablePortTemporarily',4),('allowDefaultAccess',5),('blockMacAddress',6)))
_HpnicfSecureIntrusionAction_Type.__name__=_E
_HpnicfSecureIntrusionAction_Object=MibTableColumn
hpnicfSecureIntrusionAction=_HpnicfSecureIntrusionAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,1,1,3),_HpnicfSecureIntrusionAction_Type())
hpnicfSecureIntrusionAction.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureIntrusionAction.setStatus(_A)
_HpnicfSecureNumberAddresses_Type=Integer32
_HpnicfSecureNumberAddresses_Object=MibTableColumn
hpnicfSecureNumberAddresses=_HpnicfSecureNumberAddresses_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,1,1,4),_HpnicfSecureNumberAddresses_Type())
hpnicfSecureNumberAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureNumberAddresses.setStatus(_A)
_HpnicfSecureNumberAddressesStored_Type=Integer32
_HpnicfSecureNumberAddressesStored_Object=MibTableColumn
hpnicfSecureNumberAddressesStored=_HpnicfSecureNumberAddressesStored_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,1,1,5),_HpnicfSecureNumberAddressesStored_Type())
hpnicfSecureNumberAddressesStored.setMaxAccess(_Q)
if mibBuilder.loadTexts:hpnicfSecureNumberAddressesStored.setStatus(_A)
_HpnicfSecureMaximumAddresses_Type=Integer32
_HpnicfSecureMaximumAddresses_Object=MibTableColumn
hpnicfSecureMaximumAddresses=_HpnicfSecureMaximumAddresses_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,1,1,6),_HpnicfSecureMaximumAddresses_Type())
hpnicfSecureMaximumAddresses.setMaxAccess(_Q)
if mibBuilder.loadTexts:hpnicfSecureMaximumAddresses.setStatus(_A)
_HpnicfSecureAddressTable_Object=MibTable
hpnicfSecureAddressTable=_HpnicfSecureAddressTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,2))
if mibBuilder.loadTexts:hpnicfSecureAddressTable.setStatus(_A)
_HpnicfSecureAddressEntry_Object=MibTableRow
hpnicfSecureAddressEntry=_HpnicfSecureAddressEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,2,1))
hpnicfSecureAddressEntry.setIndexNames((0,_D,_F),(0,_B,_G),(0,_B,_Y))
if mibBuilder.loadTexts:hpnicfSecureAddressEntry.setStatus(_A)
_HpnicfSecureAddrMAC_Type=MacAddress
_HpnicfSecureAddrMAC_Object=MibTableColumn
hpnicfSecureAddrMAC=_HpnicfSecureAddrMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,2,1,1),_HpnicfSecureAddrMAC_Type())
hpnicfSecureAddrMAC.setMaxAccess(_W)
if mibBuilder.loadTexts:hpnicfSecureAddrMAC.setStatus(_A)
_HpnicfSecureAddrVlanID_Type=Integer32
_HpnicfSecureAddrVlanID_Object=MibTableColumn
hpnicfSecureAddrVlanID=_HpnicfSecureAddrVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,2,1,2),_HpnicfSecureAddrVlanID_Type())
hpnicfSecureAddrVlanID.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSecureAddrVlanID.setStatus(_A)
class _HpnicfSecureAddrMACStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('addressBlackhole',1),('addressUserConfig',2),('addressDot1xAuth',3),('addressRALM',4)))
_HpnicfSecureAddrMACStatus_Type.__name__=_E
_HpnicfSecureAddrMACStatus_Object=MibTableColumn
hpnicfSecureAddrMACStatus=_HpnicfSecureAddrMACStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,2,1,3),_HpnicfSecureAddrMACStatus_Type())
hpnicfSecureAddrMACStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSecureAddrMACStatus.setStatus(_A)
_HpnicfSecureAddrRowStatus_Type=RowStatus
_HpnicfSecureAddrRowStatus_Object=MibTableColumn
hpnicfSecureAddrRowStatus=_HpnicfSecureAddrRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,2,1,4),_HpnicfSecureAddrRowStatus_Type())
hpnicfSecureAddrRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSecureAddrRowStatus.setStatus(_A)
_HpnicfSecureOUITable_Object=MibTable
hpnicfSecureOUITable=_HpnicfSecureOUITable_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,3))
if mibBuilder.loadTexts:hpnicfSecureOUITable.setStatus(_A)
_HpnicfSecureOUIEntry_Object=MibTableRow
hpnicfSecureOUIEntry=_HpnicfSecureOUIEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,3,1))
hpnicfSecureOUIEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:hpnicfSecureOUIEntry.setStatus(_A)
class _HpnicfSecureOUIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfSecureOUIIndex_Type.__name__=_E
_HpnicfSecureOUIIndex_Object=MibTableColumn
hpnicfSecureOUIIndex=_HpnicfSecureOUIIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,3,1,1),_HpnicfSecureOUIIndex_Type())
hpnicfSecureOUIIndex.setMaxAccess(_a)
if mibBuilder.loadTexts:hpnicfSecureOUIIndex.setStatus(_A)
class _HpnicfSecureOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpnicfSecureOUI_Type.__name__=_O
_HpnicfSecureOUI_Object=MibTableColumn
hpnicfSecureOUI=_HpnicfSecureOUI_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,3,1,2),_HpnicfSecureOUI_Type())
hpnicfSecureOUI.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSecureOUI.setStatus(_A)
_HpnicfSecureOUIRowStatus_Type=RowStatus
_HpnicfSecureOUIRowStatus_Object=MibTableColumn
hpnicfSecureOUIRowStatus=_HpnicfSecureOUIRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,3,1,3),_HpnicfSecureOUIRowStatus_Type())
hpnicfSecureOUIRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSecureOUIRowStatus.setStatus(_A)
_HpnicfSecureBindingTable_Object=MibTable
hpnicfSecureBindingTable=_HpnicfSecureBindingTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,4))
if mibBuilder.loadTexts:hpnicfSecureBindingTable.setStatus(_A)
_HpnicfSecureBindingEntry_Object=MibTableRow
hpnicfSecureBindingEntry=_HpnicfSecureBindingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,4,1))
hpnicfSecureBindingEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:hpnicfSecureBindingEntry.setStatus(_A)
_HpnicfSecureBindingIndex_Type=Integer32
_HpnicfSecureBindingIndex_Object=MibTableColumn
hpnicfSecureBindingIndex=_HpnicfSecureBindingIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,4,1,1),_HpnicfSecureBindingIndex_Type())
hpnicfSecureBindingIndex.setMaxAccess(_a)
if mibBuilder.loadTexts:hpnicfSecureBindingIndex.setStatus(_A)
_HpnicfSecureBindingPort_Type=Integer32
_HpnicfSecureBindingPort_Object=MibTableColumn
hpnicfSecureBindingPort=_HpnicfSecureBindingPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,4,1,2),_HpnicfSecureBindingPort_Type())
hpnicfSecureBindingPort.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSecureBindingPort.setStatus(_A)
_HpnicfSecureBindingAddrMAC_Type=MacAddress
_HpnicfSecureBindingAddrMAC_Object=MibTableColumn
hpnicfSecureBindingAddrMAC=_HpnicfSecureBindingAddrMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,4,1,3),_HpnicfSecureBindingAddrMAC_Type())
hpnicfSecureBindingAddrMAC.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSecureBindingAddrMAC.setStatus(_A)
_HpnicfSecureBindingAddrIp_Type=IpAddress
_HpnicfSecureBindingAddrIp_Object=MibTableColumn
hpnicfSecureBindingAddrIp=_HpnicfSecureBindingAddrIp_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,4,1,4),_HpnicfSecureBindingAddrIp_Type())
hpnicfSecureBindingAddrIp.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSecureBindingAddrIp.setStatus(_A)
_HpnicfSecureBindingRowStatus_Type=RowStatus
_HpnicfSecureBindingRowStatus_Object=MibTableColumn
hpnicfSecureBindingRowStatus=_HpnicfSecureBindingRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,4,1,5),_HpnicfSecureBindingRowStatus_Type())
hpnicfSecureBindingRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSecureBindingRowStatus.setStatus(_A)
_HpnicfSecureAssignTable_Object=MibTable
hpnicfSecureAssignTable=_HpnicfSecureAssignTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,5))
if mibBuilder.loadTexts:hpnicfSecureAssignTable.setStatus(_A)
_HpnicfSecureAssignEntry_Object=MibTableRow
hpnicfSecureAssignEntry=_HpnicfSecureAssignEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,5,1))
hpnicfSecureAssignEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfSecureAssignEntry.setStatus(_A)
class _HpnicfSecureAssignEnable_Type(TruthValue):defaultValue=1
_HpnicfSecureAssignEnable_Type.__name__=_U
_HpnicfSecureAssignEnable_Object=MibTableColumn
hpnicfSecureAssignEnable=_HpnicfSecureAssignEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,5,1,1),_HpnicfSecureAssignEnable_Type())
hpnicfSecureAssignEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSecureAssignEnable.setStatus(_A)
class _HpnicfSecureVlanAssignment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfSecureVlanAssignment_Type.__name__=_O
_HpnicfSecureVlanAssignment_Object=MibTableColumn
hpnicfSecureVlanAssignment=_HpnicfSecureVlanAssignment_Object((1,3,6,1,4,1,11,2,14,11,15,2,26,1,2,5,1,2),_HpnicfSecureVlanAssignment_Type())
hpnicfSecureVlanAssignment.setMaxAccess(_Q)
if mibBuilder.loadTexts:hpnicfSecureVlanAssignment.setStatus(_A)
_HpnicfPortSecurityNotifications_ObjectIdentity=ObjectIdentity
hpnicfPortSecurityNotifications=_HpnicfPortSecurityNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,26,1,3))
hpnicfSecureAddressLearned=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,26,1,3,1))
hpnicfSecureAddressLearned.setObjects(*((_D,_F),(_B,_G)))
if mibBuilder.loadTexts:hpnicfSecureAddressLearned.setStatus(_A)
hpnicfSecureViolation=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,26,1,3,2))
hpnicfSecureViolation.setObjects(*((_D,_F),(_B,_G),(_D,_T)))
if mibBuilder.loadTexts:hpnicfSecureViolation.setStatus(_A)
hpnicfSecureLoginFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,26,1,3,3))
hpnicfSecureLoginFailure.setObjects(*((_D,_F),(_B,_G),(_I,_L)))
if mibBuilder.loadTexts:hpnicfSecureLoginFailure.setStatus(_A)
hpnicfSecureLogon=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,26,1,3,4))
hpnicfSecureLogon.setObjects(*((_D,_F),(_B,_G),(_I,_L),(_I,_R),(_B,_K)))
if mibBuilder.loadTexts:hpnicfSecureLogon.setStatus(_A)
hpnicfSecureLogoff=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,26,1,3,5))
hpnicfSecureLogoff.setObjects(*((_D,_F),(_B,_G),(_I,_L),(_I,_S),(_B,_K)))
if mibBuilder.loadTexts:hpnicfSecureLogoff.setStatus(_A)
hpnicfSecureRalmLoginFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,26,1,3,6))
hpnicfSecureRalmLoginFailure.setObjects(*((_D,_F),(_B,_G),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpnicfSecureRalmLoginFailure.setStatus(_A)
hpnicfSecureRalmLogon=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,26,1,3,7))
hpnicfSecureRalmLogon.setObjects(*((_D,_F),(_B,_G),(_B,_M),(_B,_N),(_B,_K)))
if mibBuilder.loadTexts:hpnicfSecureRalmLogon.setStatus(_A)
hpnicfSecureRalmLogoff=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,26,1,3,8))
hpnicfSecureRalmLogoff.setObjects(*((_D,_F),(_B,_G),(_B,_M),(_B,_N),(_B,_K)))
if mibBuilder.loadTexts:hpnicfSecureRalmLogoff.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfPortSecurityMIB':hpnicfPortSecurityMIB,'hpnicfPortSecurityLeaf':hpnicfPortSecurityLeaf,'hpnicfSecurePortSecurityControl':hpnicfSecurePortSecurityControl,_K:hpnicfSecurePortVlanMembershipList,'hpnicfSecureRalmObjects':hpnicfSecureRalmObjects,'hpnicfSecureRalmDefaultSessionTime':hpnicfSecureRalmDefaultSessionTime,'hpnicfSecureRalmHoldoffTime':hpnicfSecureRalmHoldoffTime,'hpnicfSecureRalmReauthenticate':hpnicfSecureRalmReauthenticate,_M:hpnicfSecureRalmAuthMode,_N:hpnicfSecureRalmAuthUsername,'hpnicfSecureRalmAuthPassword':hpnicfSecureRalmAuthPassword,'hpnicfSecureRalmAuthDomain':hpnicfSecureRalmAuthDomain,'hpnicfSecureRalmAuthOfflineTime':hpnicfSecureRalmAuthOfflineTime,'hpnicfSecureRalmAuthServerTimeoutTime':hpnicfSecureRalmAuthServerTimeoutTime,'hpnicfSecureMacControl':hpnicfSecureMacControl,'hpnicfPortSecurityTables':hpnicfPortSecurityTables,'hpnicfSecurePortTable':hpnicfSecurePortTable,'hpnicfSecurePortEntry':hpnicfSecurePortEntry,'hpnicfSecurePortMode':hpnicfSecurePortMode,'hpnicfSecureNeedToKnowMode':hpnicfSecureNeedToKnowMode,'hpnicfSecureIntrusionAction':hpnicfSecureIntrusionAction,'hpnicfSecureNumberAddresses':hpnicfSecureNumberAddresses,'hpnicfSecureNumberAddressesStored':hpnicfSecureNumberAddressesStored,'hpnicfSecureMaximumAddresses':hpnicfSecureMaximumAddresses,'hpnicfSecureAddressTable':hpnicfSecureAddressTable,'hpnicfSecureAddressEntry':hpnicfSecureAddressEntry,_G:hpnicfSecureAddrMAC,_Y:hpnicfSecureAddrVlanID,'hpnicfSecureAddrMACStatus':hpnicfSecureAddrMACStatus,'hpnicfSecureAddrRowStatus':hpnicfSecureAddrRowStatus,'hpnicfSecureOUITable':hpnicfSecureOUITable,'hpnicfSecureOUIEntry':hpnicfSecureOUIEntry,_Z:hpnicfSecureOUIIndex,'hpnicfSecureOUI':hpnicfSecureOUI,'hpnicfSecureOUIRowStatus':hpnicfSecureOUIRowStatus,'hpnicfSecureBindingTable':hpnicfSecureBindingTable,'hpnicfSecureBindingEntry':hpnicfSecureBindingEntry,_b:hpnicfSecureBindingIndex,'hpnicfSecureBindingPort':hpnicfSecureBindingPort,'hpnicfSecureBindingAddrMAC':hpnicfSecureBindingAddrMAC,'hpnicfSecureBindingAddrIp':hpnicfSecureBindingAddrIp,'hpnicfSecureBindingRowStatus':hpnicfSecureBindingRowStatus,'hpnicfSecureAssignTable':hpnicfSecureAssignTable,'hpnicfSecureAssignEntry':hpnicfSecureAssignEntry,'hpnicfSecureAssignEnable':hpnicfSecureAssignEnable,'hpnicfSecureVlanAssignment':hpnicfSecureVlanAssignment,'hpnicfPortSecurityNotifications':hpnicfPortSecurityNotifications,'hpnicfSecureAddressLearned':hpnicfSecureAddressLearned,'hpnicfSecureViolation':hpnicfSecureViolation,'hpnicfSecureLoginFailure':hpnicfSecureLoginFailure,'hpnicfSecureLogon':hpnicfSecureLogon,'hpnicfSecureLogoff':hpnicfSecureLogoff,'hpnicfSecureRalmLoginFailure':hpnicfSecureRalmLoginFailure,'hpnicfSecureRalmLogon':hpnicfSecureRalmLogon,'hpnicfSecureRalmLogoff':hpnicfSecureRalmLogoff})