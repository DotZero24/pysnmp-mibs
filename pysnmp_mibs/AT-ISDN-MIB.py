_d='ccBchannelChannelIndex'
_c='ccBchannelIfIndex'
_b='ccAttachmentEntryIndex'
_a='ccAttachmentDetailsIndex'
_Z='ccCallLogIndex'
_Y='undefined'
_X='ccActiveCallIndex'
_W='ccCliListEntryIndex'
_V='ccCliListListIndex'
_U='rate_56k'
_T='rate_64k'
_S='callname'
_R='useruser'
_Q='calledsub'
_P='ccDetailsIndex'
_O='none'
_N='InterfaceIndexOrZero'
_M='yes'
_L='no'
_K='out'
_J='in'
_I='remote'
_H='local'
_G='DisplayStringUnsized'
_F='off'
_E='AT-ISDN-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB',_G,'modules')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB',_N,'ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cc=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,37))
if mibBuilder.loadTexts:cc.setRevisions(('2006-06-28 12:22',))
_CcDetailsTable_Object=MibTable
ccDetailsTable=_CcDetailsTable_Object((1,3,6,1,4,1,207,8,4,4,4,37,1))
if mibBuilder.loadTexts:ccDetailsTable.setStatus(_A)
_CcDetailsEntry_Object=MibTableRow
ccDetailsEntry=_CcDetailsEntry_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1))
ccDetailsEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:ccDetailsEntry.setStatus(_A)
class _CcDetailsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CcDetailsIndex_Type.__name__=_B
_CcDetailsIndex_Object=MibTableColumn
ccDetailsIndex=_CcDetailsIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,1),_CcDetailsIndex_Type())
ccDetailsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccDetailsIndex.setStatus(_A)
class _CcDetailsName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CcDetailsName_Type.__name__=_G
_CcDetailsName_Object=MibTableColumn
ccDetailsName=_CcDetailsName_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,2),_CcDetailsName_Type())
ccDetailsName.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsName.setStatus(_A)
class _CcDetailsRemoteName_Type(DisplayStringUnsized):defaultValue=OctetString('');subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CcDetailsRemoteName_Type.__name__=_G
_CcDetailsRemoteName_Object=MibTableColumn
ccDetailsRemoteName=_CcDetailsRemoteName_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,3),_CcDetailsRemoteName_Type())
ccDetailsRemoteName.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsRemoteName.setStatus(_A)
class _CcDetailsCalledNumber_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CcDetailsCalledNumber_Type.__name__=_G
_CcDetailsCalledNumber_Object=MibTableColumn
ccDetailsCalledNumber=_CcDetailsCalledNumber_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,4),_CcDetailsCalledNumber_Type())
ccDetailsCalledNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsCalledNumber.setStatus(_A)
class _CcDetailsCallingNumber_Type(DisplayStringUnsized):defaultValue=OctetString('');subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CcDetailsCallingNumber_Type.__name__=_G
_CcDetailsCallingNumber_Object=MibTableColumn
ccDetailsCallingNumber=_CcDetailsCallingNumber_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,5),_CcDetailsCallingNumber_Type())
ccDetailsCallingNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsCallingNumber.setStatus(_A)
class _CcDetailsAlternateNumber_Type(DisplayStringUnsized):defaultValue=OctetString('');subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CcDetailsAlternateNumber_Type.__name__=_G
_CcDetailsAlternateNumber_Object=MibTableColumn
ccDetailsAlternateNumber=_CcDetailsAlternateNumber_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,6),_CcDetailsAlternateNumber_Type())
ccDetailsAlternateNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsAlternateNumber.setStatus(_A)
class _CcDetailsEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_CcDetailsEnabled_Type.__name__=_B
_CcDetailsEnabled_Object=MibTableColumn
ccDetailsEnabled=_CcDetailsEnabled_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,7),_CcDetailsEnabled_Type())
ccDetailsEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsEnabled.setStatus(_A)
class _CcDetailsDirection_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inOnly',1),('outOnly',2),('both',3)))
_CcDetailsDirection_Type.__name__=_B
_CcDetailsDirection_Object=MibTableColumn
ccDetailsDirection=_CcDetailsDirection_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,8),_CcDetailsDirection_Type())
ccDetailsDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsDirection.setStatus(_A)
class _CcDetailsPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_CcDetailsPrecedence_Type.__name__=_B
_CcDetailsPrecedence_Object=MibTableColumn
ccDetailsPrecedence=_CcDetailsPrecedence_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,9),_CcDetailsPrecedence_Type())
ccDetailsPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsPrecedence.setStatus(_A)
class _CcDetailsHoldupTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7200))
_CcDetailsHoldupTime_Type.__name__=_B
_CcDetailsHoldupTime_Object=MibTableColumn
ccDetailsHoldupTime=_CcDetailsHoldupTime_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,10),_CcDetailsHoldupTime_Type())
ccDetailsHoldupTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsHoldupTime.setStatus(_A)
class _CcDetailsPreferredIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_CcDetailsPreferredIfIndex_Type.__name__=_N
_CcDetailsPreferredIfIndex_Object=MibTableColumn
ccDetailsPreferredIfIndex=_CcDetailsPreferredIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,11),_CcDetailsPreferredIfIndex_Type())
ccDetailsPreferredIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsPreferredIfIndex.setStatus(_A)
class _CcDetailsRequiredIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_CcDetailsRequiredIfIndex_Type.__name__=_N
_CcDetailsRequiredIfIndex_Object=MibTableColumn
ccDetailsRequiredIfIndex=_CcDetailsRequiredIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,12),_CcDetailsRequiredIfIndex_Type())
ccDetailsRequiredIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsRequiredIfIndex.setStatus(_A)
class _CcDetailsPriority_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_CcDetailsPriority_Type.__name__=_B
_CcDetailsPriority_Object=MibTableColumn
ccDetailsPriority=_CcDetailsPriority_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,13),_CcDetailsPriority_Type())
ccDetailsPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsPriority.setStatus(_A)
class _CcDetailsRetryT1_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,120))
_CcDetailsRetryT1_Type.__name__=_B
_CcDetailsRetryT1_Object=MibTableColumn
ccDetailsRetryT1=_CcDetailsRetryT1_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,14),_CcDetailsRetryT1_Type())
ccDetailsRetryT1.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsRetryT1.setStatus(_A)
class _CcDetailsRetryN1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CcDetailsRetryN1_Type.__name__=_B
_CcDetailsRetryN1_Object=MibTableColumn
ccDetailsRetryN1=_CcDetailsRetryN1_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,15),_CcDetailsRetryN1_Type())
ccDetailsRetryN1.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsRetryN1.setStatus(_A)
class _CcDetailsRetryT2_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,1200))
_CcDetailsRetryT2_Type.__name__=_B
_CcDetailsRetryT2_Object=MibTableColumn
ccDetailsRetryT2=_CcDetailsRetryT2_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,16),_CcDetailsRetryT2_Type())
ccDetailsRetryT2.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsRetryT2.setStatus(_A)
class _CcDetailsRetryN2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_CcDetailsRetryN2_Type.__name__=_B
_CcDetailsRetryN2_Object=MibTableColumn
ccDetailsRetryN2=_CcDetailsRetryN2_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,17),_CcDetailsRetryN2_Type())
ccDetailsRetryN2.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsRetryN2.setStatus(_A)
class _CcDetailsKeepup_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_CcDetailsKeepup_Type.__name__=_B
_CcDetailsKeepup_Object=MibTableColumn
ccDetailsKeepup=_CcDetailsKeepup_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,18),_CcDetailsKeepup_Type())
ccDetailsKeepup.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsKeepup.setStatus(_A)
class _CcDetailsOutSetupCli_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('calling',2),('interface',3),('nonumber',4)))
_CcDetailsOutSetupCli_Type.__name__=_B
_CcDetailsOutSetupCli_Object=MibTableColumn
ccDetailsOutSetupCli=_CcDetailsOutSetupCli_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,19),_CcDetailsOutSetupCli_Type())
ccDetailsOutSetupCli.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsOutSetupCli.setStatus(_A)
class _CcDetailsOutSetupUser_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3)))
_CcDetailsOutSetupUser_Type.__name__=_B
_CcDetailsOutSetupUser_Object=MibTableColumn
ccDetailsOutSetupUser=_CcDetailsOutSetupUser_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,20),_CcDetailsOutSetupUser_Type())
ccDetailsOutSetupUser.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsOutSetupUser.setStatus(_A)
class _CcDetailsOutSetupCalledSub_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3)))
_CcDetailsOutSetupCalledSub_Type.__name__=_B
_CcDetailsOutSetupCalledSub_Object=MibTableColumn
ccDetailsOutSetupCalledSub=_CcDetailsOutSetupCalledSub_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,21),_CcDetailsOutSetupCalledSub_Type())
ccDetailsOutSetupCalledSub.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsOutSetupCalledSub.setStatus(_A)
class _CcDetailsOutSubaddress_Type(DisplayStringUnsized):defaultValue=OctetString('');subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CcDetailsOutSubaddress_Type.__name__=_G
_CcDetailsOutSubaddress_Object=MibTableColumn
ccDetailsOutSubaddress=_CcDetailsOutSubaddress_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,22),_CcDetailsOutSubaddress_Type())
ccDetailsOutSubaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsOutSubaddress.setStatus(_A)
class _CcDetailsCallback_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_CcDetailsCallback_Type.__name__=_B
_CcDetailsCallback_Object=MibTableColumn
ccDetailsCallback=_CcDetailsCallback_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,23),_CcDetailsCallback_Type())
ccDetailsCallback.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsCallback.setStatus(_A)
class _CcDetailsCallbackDelay_Type(Integer32):defaultValue=41;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CcDetailsCallbackDelay_Type.__name__=_B
_CcDetailsCallbackDelay_Object=MibTableColumn
ccDetailsCallbackDelay=_CcDetailsCallbackDelay_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,24),_CcDetailsCallbackDelay_Type())
ccDetailsCallbackDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsCallbackDelay.setStatus(_A)
class _CcDetailsInSetupCalledSubSearch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3)))
_CcDetailsInSetupCalledSubSearch_Type.__name__=_B
_CcDetailsInSetupCalledSubSearch_Object=MibTableColumn
ccDetailsInSetupCalledSubSearch=_CcDetailsInSetupCalledSubSearch_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,25),_CcDetailsInSetupCalledSubSearch_Type())
ccDetailsInSetupCalledSubSearch.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsInSetupCalledSubSearch.setStatus(_A)
class _CcDetailsInSetupUserSearch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3)))
_CcDetailsInSetupUserSearch_Type.__name__=_B
_CcDetailsInSetupUserSearch_Object=MibTableColumn
ccDetailsInSetupUserSearch=_CcDetailsInSetupUserSearch_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,26),_CcDetailsInSetupUserSearch_Type())
ccDetailsInSetupUserSearch.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsInSetupUserSearch.setStatus(_A)
class _CcDetailsInSetupCliSearch_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('on',2),('list',3)))
_CcDetailsInSetupCliSearch_Type.__name__=_B
_CcDetailsInSetupCliSearch_Object=MibTableColumn
ccDetailsInSetupCliSearch=_CcDetailsInSetupCliSearch_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,27),_CcDetailsInSetupCliSearch_Type())
ccDetailsInSetupCliSearch.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsInSetupCliSearch.setStatus(_A)
class _CcDetailsInSetupCliSearchList_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CcDetailsInSetupCliSearchList_Type.__name__=_B
_CcDetailsInSetupCliSearchList_Object=MibTableColumn
ccDetailsInSetupCliSearchList=_CcDetailsInSetupCliSearchList_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,28),_CcDetailsInSetupCliSearchList_Type())
ccDetailsInSetupCliSearchList.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsInSetupCliSearchList.setStatus(_A)
class _CcDetailsInAnyFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_CcDetailsInAnyFlag_Type.__name__=_B
_CcDetailsInAnyFlag_Object=MibTableColumn
ccDetailsInAnyFlag=_CcDetailsInAnyFlag_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,29),_CcDetailsInAnyFlag_Type())
ccDetailsInAnyFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsInAnyFlag.setStatus(_A)
class _CcDetailsInSetupCalledSubCheck_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3)))
_CcDetailsInSetupCalledSubCheck_Type.__name__=_B
_CcDetailsInSetupCalledSubCheck_Object=MibTableColumn
ccDetailsInSetupCalledSubCheck=_CcDetailsInSetupCalledSubCheck_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,30),_CcDetailsInSetupCalledSubCheck_Type())
ccDetailsInSetupCalledSubCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsInSetupCalledSubCheck.setStatus(_A)
class _CcDetailsInSetupUserCheck_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_H,2),(_I,3)))
_CcDetailsInSetupUserCheck_Type.__name__=_B
_CcDetailsInSetupUserCheck_Object=MibTableColumn
ccDetailsInSetupUserCheck=_CcDetailsInSetupUserCheck_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,31),_CcDetailsInSetupUserCheck_Type())
ccDetailsInSetupUserCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsInSetupUserCheck.setStatus(_A)
class _CcDetailsInSetupCliCheck_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('present',2),('required',3)))
_CcDetailsInSetupCliCheck_Type.__name__=_B
_CcDetailsInSetupCliCheck_Object=MibTableColumn
ccDetailsInSetupCliCheck=_CcDetailsInSetupCliCheck_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,32),_CcDetailsInSetupCliCheck_Type())
ccDetailsInSetupCliCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsInSetupCliCheck.setStatus(_A)
class _CcDetailsInSetupCliCheckList_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CcDetailsInSetupCliCheckList_Type.__name__=_B
_CcDetailsInSetupCliCheckList_Object=MibTableColumn
ccDetailsInSetupCliCheckList=_CcDetailsInSetupCliCheckList_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,33),_CcDetailsInSetupCliCheckList_Type())
ccDetailsInSetupCliCheckList.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsInSetupCliCheckList.setStatus(_A)
class _CcDetailsUserType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('attach',1),('ppp',2)))
_CcDetailsUserType_Type.__name__=_B
_CcDetailsUserType_Object=MibTableColumn
ccDetailsUserType=_CcDetailsUserType_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,34),_CcDetailsUserType_Type())
ccDetailsUserType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsUserType.setStatus(_A)
class _CcDetailsLoginType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_O,1),('userdb',2),('radius',3),('papTacacs',4),('chap',5),('papRadius',6),('tacacs',7),('all',8)))
_CcDetailsLoginType_Type.__name__=_B
_CcDetailsLoginType_Object=MibTableColumn
ccDetailsLoginType=_CcDetailsLoginType_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,35),_CcDetailsLoginType_Type())
ccDetailsLoginType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsLoginType.setStatus(_A)
class _CcDetailsUsername_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),('cli',2),(_Q,3),(_R,4),(_S,5)))
_CcDetailsUsername_Type.__name__=_B
_CcDetailsUsername_Object=MibTableColumn
ccDetailsUsername=_CcDetailsUsername_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,36),_CcDetailsUsername_Type())
ccDetailsUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsUsername.setStatus(_A)
class _CcDetailsPassword_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),('cli',2),(_Q,3),(_R,4),(_S,5)))
_CcDetailsPassword_Type.__name__=_B
_CcDetailsPassword_Object=MibTableColumn
ccDetailsPassword=_CcDetailsPassword_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,37),_CcDetailsPassword_Type())
ccDetailsPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsPassword.setStatus(_A)
class _CcDetailsBumpDelay_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CcDetailsBumpDelay_Type.__name__=_B
_CcDetailsBumpDelay_Object=MibTableColumn
ccDetailsBumpDelay=_CcDetailsBumpDelay_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,38),_CcDetailsBumpDelay_Type())
ccDetailsBumpDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsBumpDelay.setStatus(_A)
class _CcDetailsDataRate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_CcDetailsDataRate_Type.__name__=_B
_CcDetailsDataRate_Object=MibTableColumn
ccDetailsDataRate=_CcDetailsDataRate_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,39),_CcDetailsDataRate_Type())
ccDetailsDataRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsDataRate.setStatus(_A)
class _CcDetailsPppTemplate_Type(Integer32):defaultValue=33;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,33))
_CcDetailsPppTemplate_Type.__name__=_B
_CcDetailsPppTemplate_Object=MibTableColumn
ccDetailsPppTemplate=_CcDetailsPppTemplate_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,40),_CcDetailsPppTemplate_Type())
ccDetailsPppTemplate.setMaxAccess(_C)
if mibBuilder.loadTexts:ccDetailsPppTemplate.setStatus(_A)
_CcDetailsUserModule_Type=Integer32
_CcDetailsUserModule_Object=MibTableColumn
ccDetailsUserModule=_CcDetailsUserModule_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,41),_CcDetailsUserModule_Type())
ccDetailsUserModule.setMaxAccess(_D)
if mibBuilder.loadTexts:ccDetailsUserModule.setStatus(_A)
_CcDetailsNumberAttachments_Type=Integer32
_CcDetailsNumberAttachments_Object=MibTableColumn
ccDetailsNumberAttachments=_CcDetailsNumberAttachments_Object((1,3,6,1,4,1,207,8,4,4,4,37,1,1,42),_CcDetailsNumberAttachments_Type())
ccDetailsNumberAttachments.setMaxAccess(_D)
if mibBuilder.loadTexts:ccDetailsNumberAttachments.setStatus(_A)
_CcCliListTable_Object=MibTable
ccCliListTable=_CcCliListTable_Object((1,3,6,1,4,1,207,8,4,4,4,37,2))
if mibBuilder.loadTexts:ccCliListTable.setStatus(_A)
_CcCliListEntry_Object=MibTableRow
ccCliListEntry=_CcCliListEntry_Object((1,3,6,1,4,1,207,8,4,4,4,37,2,1))
ccCliListEntry.setIndexNames((0,_E,_V),(0,_E,_W))
if mibBuilder.loadTexts:ccCliListEntry.setStatus(_A)
class _CcCliListListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CcCliListListIndex_Type.__name__=_B
_CcCliListListIndex_Object=MibTableColumn
ccCliListListIndex=_CcCliListListIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,2,1,1),_CcCliListListIndex_Type())
ccCliListListIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCliListListIndex.setStatus(_A)
_CcCliListEntryIndex_Type=Integer32
_CcCliListEntryIndex_Object=MibTableColumn
ccCliListEntryIndex=_CcCliListEntryIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,2,1,2),_CcCliListEntryIndex_Type())
ccCliListEntryIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCliListEntryIndex.setStatus(_A)
class _CcCliListNumber_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CcCliListNumber_Type.__name__=_G
_CcCliListNumber_Object=MibTableColumn
ccCliListNumber=_CcCliListNumber_Object((1,3,6,1,4,1,207,8,4,4,4,37,2,1,3),_CcCliListNumber_Type())
ccCliListNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ccCliListNumber.setStatus(_A)
_CcActiveCallTable_Object=MibTable
ccActiveCallTable=_CcActiveCallTable_Object((1,3,6,1,4,1,207,8,4,4,4,37,3))
if mibBuilder.loadTexts:ccActiveCallTable.setStatus(_A)
_CcActiveCallEntry_Object=MibTableRow
ccActiveCallEntry=_CcActiveCallEntry_Object((1,3,6,1,4,1,207,8,4,4,4,37,3,1))
ccActiveCallEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:ccActiveCallEntry.setStatus(_A)
class _CcActiveCallIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CcActiveCallIndex_Type.__name__=_B
_CcActiveCallIndex_Object=MibTableColumn
ccActiveCallIndex=_CcActiveCallIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,3,1,1),_CcActiveCallIndex_Type())
ccActiveCallIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccActiveCallIndex.setStatus(_A)
class _CcActiveCallDetailsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CcActiveCallDetailsIndex_Type.__name__=_B
_CcActiveCallDetailsIndex_Object=MibTableColumn
ccActiveCallDetailsIndex=_CcActiveCallDetailsIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,3,1,2),_CcActiveCallDetailsIndex_Type())
ccActiveCallDetailsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccActiveCallDetailsIndex.setStatus(_A)
_CcActiveCallIfIndex_Type=InterfaceIndexOrZero
_CcActiveCallIfIndex_Object=MibTableColumn
ccActiveCallIfIndex=_CcActiveCallIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,3,1,3),_CcActiveCallIfIndex_Type())
ccActiveCallIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccActiveCallIfIndex.setStatus(_A)
class _CcActiveCallDataRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_CcActiveCallDataRate_Type.__name__=_B
_CcActiveCallDataRate_Object=MibTableColumn
ccActiveCallDataRate=_CcActiveCallDataRate_Object((1,3,6,1,4,1,207,8,4,4,4,37,3,1,4),_CcActiveCallDataRate_Type())
ccActiveCallDataRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ccActiveCallDataRate.setStatus(_A)
class _CcActiveCallState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('null',1),(_F,2),('try',3),('on',4),('wait',5),('await1',6)))
_CcActiveCallState_Type.__name__=_B
_CcActiveCallState_Object=MibTableColumn
ccActiveCallState=_CcActiveCallState_Object((1,3,6,1,4,1,207,8,4,4,4,37,3,1,5),_CcActiveCallState_Type())
ccActiveCallState.setMaxAccess(_D)
if mibBuilder.loadTexts:ccActiveCallState.setStatus(_A)
class _CcActiveCallDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),(_Y,3)))
_CcActiveCallDirection_Type.__name__=_B
_CcActiveCallDirection_Object=MibTableColumn
ccActiveCallDirection=_CcActiveCallDirection_Object((1,3,6,1,4,1,207,8,4,4,4,37,3,1,6),_CcActiveCallDirection_Type())
ccActiveCallDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:ccActiveCallDirection.setStatus(_A)
_CcActiveCallUserModule_Type=Integer32
_CcActiveCallUserModule_Object=MibTableColumn
ccActiveCallUserModule=_CcActiveCallUserModule_Object((1,3,6,1,4,1,207,8,4,4,4,37,3,1,7),_CcActiveCallUserModule_Type())
ccActiveCallUserModule.setMaxAccess(_D)
if mibBuilder.loadTexts:ccActiveCallUserModule.setStatus(_A)
_CcActiveCallUserInstance_Type=Integer32
_CcActiveCallUserInstance_Object=MibTableColumn
ccActiveCallUserInstance=_CcActiveCallUserInstance_Object((1,3,6,1,4,1,207,8,4,4,4,37,3,1,8),_CcActiveCallUserInstance_Type())
ccActiveCallUserInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:ccActiveCallUserInstance.setStatus(_A)
class _CcActiveCallBchannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_CcActiveCallBchannelIndex_Type.__name__=_B
_CcActiveCallBchannelIndex_Object=MibTableColumn
ccActiveCallBchannelIndex=_CcActiveCallBchannelIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,3,1,9),_CcActiveCallBchannelIndex_Type())
ccActiveCallBchannelIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccActiveCallBchannelIndex.setStatus(_A)
_CcCallLogTable_Object=MibTable
ccCallLogTable=_CcCallLogTable_Object((1,3,6,1,4,1,207,8,4,4,4,37,4))
if mibBuilder.loadTexts:ccCallLogTable.setStatus(_A)
_CcCallLogEntry_Object=MibTableRow
ccCallLogEntry=_CcCallLogEntry_Object((1,3,6,1,4,1,207,8,4,4,4,37,4,1))
ccCallLogEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:ccCallLogEntry.setStatus(_A)
_CcCallLogIndex_Type=Integer32
_CcCallLogIndex_Object=MibTableColumn
ccCallLogIndex=_CcCallLogIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,4,1,1),_CcCallLogIndex_Type())
ccCallLogIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCallLogIndex.setStatus(_A)
_CcCallLogName_Type=DisplayString
_CcCallLogName_Object=MibTableColumn
ccCallLogName=_CcCallLogName_Object((1,3,6,1,4,1,207,8,4,4,4,37,4,1,2),_CcCallLogName_Type())
ccCallLogName.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCallLogName.setStatus(_A)
class _CcCallLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('initial',1),('active',2),('disconnected',3),('cleared',4)))
_CcCallLogState_Type.__name__=_B
_CcCallLogState_Object=MibTableColumn
ccCallLogState=_CcCallLogState_Object((1,3,6,1,4,1,207,8,4,4,4,37,4,1,3),_CcCallLogState_Type())
ccCallLogState.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCallLogState.setStatus(_A)
_CcCallLogTimeStarted_Type=DisplayString
_CcCallLogTimeStarted_Object=MibTableColumn
ccCallLogTimeStarted=_CcCallLogTimeStarted_Object((1,3,6,1,4,1,207,8,4,4,4,37,4,1,4),_CcCallLogTimeStarted_Type())
ccCallLogTimeStarted.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCallLogTimeStarted.setStatus(_A)
class _CcCallLogDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_CcCallLogDirection_Type.__name__=_B
_CcCallLogDirection_Object=MibTableColumn
ccCallLogDirection=_CcCallLogDirection_Object((1,3,6,1,4,1,207,8,4,4,4,37,4,1,5),_CcCallLogDirection_Type())
ccCallLogDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCallLogDirection.setStatus(_A)
_CcCallLogDuration_Type=Integer32
_CcCallLogDuration_Object=MibTableColumn
ccCallLogDuration=_CcCallLogDuration_Object((1,3,6,1,4,1,207,8,4,4,4,37,4,1,6),_CcCallLogDuration_Type())
ccCallLogDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCallLogDuration.setStatus(_A)
_CcCallLogRemoteNumber_Type=DisplayString
_CcCallLogRemoteNumber_Object=MibTableColumn
ccCallLogRemoteNumber=_CcCallLogRemoteNumber_Object((1,3,6,1,4,1,207,8,4,4,4,37,4,1,7),_CcCallLogRemoteNumber_Type())
ccCallLogRemoteNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:ccCallLogRemoteNumber.setStatus(_A)
_CcAttachmentTable_Object=MibTable
ccAttachmentTable=_CcAttachmentTable_Object((1,3,6,1,4,1,207,8,4,4,4,37,5))
if mibBuilder.loadTexts:ccAttachmentTable.setStatus(_A)
_CcAttachmentEntry_Object=MibTableRow
ccAttachmentEntry=_CcAttachmentEntry_Object((1,3,6,1,4,1,207,8,4,4,4,37,5,1))
ccAttachmentEntry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:ccAttachmentEntry.setStatus(_A)
class _CcAttachmentDetailsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CcAttachmentDetailsIndex_Type.__name__=_B
_CcAttachmentDetailsIndex_Object=MibTableColumn
ccAttachmentDetailsIndex=_CcAttachmentDetailsIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,5,1,1),_CcAttachmentDetailsIndex_Type())
ccAttachmentDetailsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccAttachmentDetailsIndex.setStatus(_A)
_CcAttachmentEntryIndex_Type=Integer32
_CcAttachmentEntryIndex_Object=MibTableColumn
ccAttachmentEntryIndex=_CcAttachmentEntryIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,5,1,2),_CcAttachmentEntryIndex_Type())
ccAttachmentEntryIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccAttachmentEntryIndex.setStatus(_A)
class _CcAttachmentActiveCallIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_CcAttachmentActiveCallIndex_Type.__name__=_B
_CcAttachmentActiveCallIndex_Object=MibTableColumn
ccAttachmentActiveCallIndex=_CcAttachmentActiveCallIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,5,1,3),_CcAttachmentActiveCallIndex_Type())
ccAttachmentActiveCallIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccAttachmentActiveCallIndex.setStatus(_A)
_CcAttachmentUserInstance_Type=Integer32
_CcAttachmentUserInstance_Object=MibTableColumn
ccAttachmentUserInstance=_CcAttachmentUserInstance_Object((1,3,6,1,4,1,207,8,4,4,4,37,5,1,4),_CcAttachmentUserInstance_Type())
ccAttachmentUserInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:ccAttachmentUserInstance.setStatus(_A)
_CcBchannelTable_Object=MibTable
ccBchannelTable=_CcBchannelTable_Object((1,3,6,1,4,1,207,8,4,4,4,37,6))
if mibBuilder.loadTexts:ccBchannelTable.setStatus(_A)
_CcBchannelEntry_Object=MibTableRow
ccBchannelEntry=_CcBchannelEntry_Object((1,3,6,1,4,1,207,8,4,4,4,37,6,1))
ccBchannelEntry.setIndexNames((0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:ccBchannelEntry.setStatus(_A)
_CcBchannelIfIndex_Type=Integer32
_CcBchannelIfIndex_Object=MibTableColumn
ccBchannelIfIndex=_CcBchannelIfIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,6,1,1),_CcBchannelIfIndex_Type())
ccBchannelIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccBchannelIfIndex.setStatus(_A)
class _CcBchannelChannelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_CcBchannelChannelIndex_Type.__name__=_B
_CcBchannelChannelIndex_Object=MibTableColumn
ccBchannelChannelIndex=_CcBchannelChannelIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,6,1,2),_CcBchannelChannelIndex_Type())
ccBchannelChannelIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccBchannelChannelIndex.setStatus(_A)
class _CcBchannelAllocated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_CcBchannelAllocated_Type.__name__=_B
_CcBchannelAllocated_Object=MibTableColumn
ccBchannelAllocated=_CcBchannelAllocated_Object((1,3,6,1,4,1,207,8,4,4,4,37,6,1,3),_CcBchannelAllocated_Type())
ccBchannelAllocated.setMaxAccess(_D)
if mibBuilder.loadTexts:ccBchannelAllocated.setStatus(_A)
class _CcBchannelCallType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Y,1),('data',2),('voice',3),('x25',4)))
_CcBchannelCallType_Type.__name__=_B
_CcBchannelCallType_Object=MibTableColumn
ccBchannelCallType=_CcBchannelCallType_Object((1,3,6,1,4,1,207,8,4,4,4,37,6,1,4),_CcBchannelCallType_Type())
ccBchannelCallType.setMaxAccess(_D)
if mibBuilder.loadTexts:ccBchannelCallType.setStatus(_A)
class _CcBchannelActiveCallIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_CcBchannelActiveCallIndex_Type.__name__=_B
_CcBchannelActiveCallIndex_Object=MibTableColumn
ccBchannelActiveCallIndex=_CcBchannelActiveCallIndex_Object((1,3,6,1,4,1,207,8,4,4,4,37,6,1,5),_CcBchannelActiveCallIndex_Type())
ccBchannelActiveCallIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccBchannelActiveCallIndex.setStatus(_A)
_CcBchannelPriority_Type=Integer32
_CcBchannelPriority_Object=MibTableColumn
ccBchannelPriority=_CcBchannelPriority_Object((1,3,6,1,4,1,207,8,4,4,4,37,6,1,6),_CcBchannelPriority_Type())
ccBchannelPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ccBchannelPriority.setStatus(_A)
class _CcBchannelDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),('unallocated',3)))
_CcBchannelDirection_Type.__name__=_B
_CcBchannelDirection_Object=MibTableColumn
ccBchannelDirection=_CcBchannelDirection_Object((1,3,6,1,4,1,207,8,4,4,4,37,6,1,7),_CcBchannelDirection_Type())
ccBchannelDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:ccBchannelDirection.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'cc':cc,'ccDetailsTable':ccDetailsTable,'ccDetailsEntry':ccDetailsEntry,_P:ccDetailsIndex,'ccDetailsName':ccDetailsName,'ccDetailsRemoteName':ccDetailsRemoteName,'ccDetailsCalledNumber':ccDetailsCalledNumber,'ccDetailsCallingNumber':ccDetailsCallingNumber,'ccDetailsAlternateNumber':ccDetailsAlternateNumber,'ccDetailsEnabled':ccDetailsEnabled,'ccDetailsDirection':ccDetailsDirection,'ccDetailsPrecedence':ccDetailsPrecedence,'ccDetailsHoldupTime':ccDetailsHoldupTime,'ccDetailsPreferredIfIndex':ccDetailsPreferredIfIndex,'ccDetailsRequiredIfIndex':ccDetailsRequiredIfIndex,'ccDetailsPriority':ccDetailsPriority,'ccDetailsRetryT1':ccDetailsRetryT1,'ccDetailsRetryN1':ccDetailsRetryN1,'ccDetailsRetryT2':ccDetailsRetryT2,'ccDetailsRetryN2':ccDetailsRetryN2,'ccDetailsKeepup':ccDetailsKeepup,'ccDetailsOutSetupCli':ccDetailsOutSetupCli,'ccDetailsOutSetupUser':ccDetailsOutSetupUser,'ccDetailsOutSetupCalledSub':ccDetailsOutSetupCalledSub,'ccDetailsOutSubaddress':ccDetailsOutSubaddress,'ccDetailsCallback':ccDetailsCallback,'ccDetailsCallbackDelay':ccDetailsCallbackDelay,'ccDetailsInSetupCalledSubSearch':ccDetailsInSetupCalledSubSearch,'ccDetailsInSetupUserSearch':ccDetailsInSetupUserSearch,'ccDetailsInSetupCliSearch':ccDetailsInSetupCliSearch,'ccDetailsInSetupCliSearchList':ccDetailsInSetupCliSearchList,'ccDetailsInAnyFlag':ccDetailsInAnyFlag,'ccDetailsInSetupCalledSubCheck':ccDetailsInSetupCalledSubCheck,'ccDetailsInSetupUserCheck':ccDetailsInSetupUserCheck,'ccDetailsInSetupCliCheck':ccDetailsInSetupCliCheck,'ccDetailsInSetupCliCheckList':ccDetailsInSetupCliCheckList,'ccDetailsUserType':ccDetailsUserType,'ccDetailsLoginType':ccDetailsLoginType,'ccDetailsUsername':ccDetailsUsername,'ccDetailsPassword':ccDetailsPassword,'ccDetailsBumpDelay':ccDetailsBumpDelay,'ccDetailsDataRate':ccDetailsDataRate,'ccDetailsPppTemplate':ccDetailsPppTemplate,'ccDetailsUserModule':ccDetailsUserModule,'ccDetailsNumberAttachments':ccDetailsNumberAttachments,'ccCliListTable':ccCliListTable,'ccCliListEntry':ccCliListEntry,_V:ccCliListListIndex,_W:ccCliListEntryIndex,'ccCliListNumber':ccCliListNumber,'ccActiveCallTable':ccActiveCallTable,'ccActiveCallEntry':ccActiveCallEntry,_X:ccActiveCallIndex,'ccActiveCallDetailsIndex':ccActiveCallDetailsIndex,'ccActiveCallIfIndex':ccActiveCallIfIndex,'ccActiveCallDataRate':ccActiveCallDataRate,'ccActiveCallState':ccActiveCallState,'ccActiveCallDirection':ccActiveCallDirection,'ccActiveCallUserModule':ccActiveCallUserModule,'ccActiveCallUserInstance':ccActiveCallUserInstance,'ccActiveCallBchannelIndex':ccActiveCallBchannelIndex,'ccCallLogTable':ccCallLogTable,'ccCallLogEntry':ccCallLogEntry,_Z:ccCallLogIndex,'ccCallLogName':ccCallLogName,'ccCallLogState':ccCallLogState,'ccCallLogTimeStarted':ccCallLogTimeStarted,'ccCallLogDirection':ccCallLogDirection,'ccCallLogDuration':ccCallLogDuration,'ccCallLogRemoteNumber':ccCallLogRemoteNumber,'ccAttachmentTable':ccAttachmentTable,'ccAttachmentEntry':ccAttachmentEntry,_a:ccAttachmentDetailsIndex,_b:ccAttachmentEntryIndex,'ccAttachmentActiveCallIndex':ccAttachmentActiveCallIndex,'ccAttachmentUserInstance':ccAttachmentUserInstance,'ccBchannelTable':ccBchannelTable,'ccBchannelEntry':ccBchannelEntry,_c:ccBchannelIfIndex,_d:ccBchannelChannelIndex,'ccBchannelAllocated':ccBchannelAllocated,'ccBchannelCallType':ccBchannelCallType,'ccBchannelActiveCallIndex':ccBchannelActiveCallIndex,'ccBchannelPriority':ccBchannelPriority,'ccBchannelDirection':ccBchannelDirection})