_AA='zxAnSipHisPerfIntervalNumber'
_A9='zxAnSipIsdnBChanTimeSlot'
_A8='zxAnSipIsdnBChanIndex'
_A7='zxAnSipIsdnBChanSlot'
_A6='zxAnSipIsdnBChanShelf'
_A5='zxAnSipIsdnBChanRack'
_A4='zxAnSipIsdnPhoneIsdnPhone'
_A3='zxAnSipIsdnPhoneSipPhone'
_A2='zxAnSipIsdnUserSipPhoneNumber'
_A1='zxAnSipIsdnUserGroupId'
_A0='zxAnSipIsdnUserMgId'
_z='zxAnSipIsdnDLinkLinkId'
_y='zxAnSipIsdnDLinkGroupId'
_x='zxAnSipIsdnDLinkMgId'
_w='zxAnSipGroupId'
_v='zxAnSipGroupMgId'
_u='zxAnSipUaId'
_t='zxAnSipProxySvrId'
_s='noRedunt2833'
_r='redunt2833'
_q='zxMsagSipCapMgId'
_p='zxMsagSipGenFmtField'
_o='zxMsagSipGenFmtMgId'
_n='zxMsagSipServiceCodeType'
_m='zxMsagSipServiceCodeMgId'
_l='zxMsagSipAccessCodeId'
_k='zxMsagSipAccessCodeMgId'
_j='sipuser'
_i='zxMsagSipUserIndex'
_h='zxMsagSipUserSlot'
_g='zxMsagSipUserShelf'
_f='zxMsagSipUserRack'
_e='zxMsagSipUserId'
_d='zxMsagSipUserAuthusername'
_c='zxAnSipTrapMgcNo'
_b='zxAnSipTrapReason'
_a='sipuserid'
_Z='type3'
_Y='type2'
_X='disabled'
_W='enabled'
_V='erl'
_U='g729'
_T='g728'
_S='g726'
_R='g723'
_Q='g722'
_P='percent'
_O='seconds'
_N='disable'
_M='enable'
_L='pcmu'
_K='pcma'
_J='unconfig'
_I='TruthValue'
_H='DisplayString'
_G='not-accessible'
_F='ZTE-AN-SIP-MIB'
_E='read-write'
_D='read-only'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention',_I)
zxAnSipMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_ZxAnVoiceMgmt_ObjectIdentity=ObjectIdentity
zxAnVoiceMgmt=_ZxAnVoiceMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_ZxAnSipConfig_ObjectIdentity=ObjectIdentity
zxAnSipConfig=_ZxAnSipConfig_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,8))
_ZxMsagSipUserTable_Object=MibTable
zxMsagSipUserTable=_ZxMsagSipUserTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1))
if mibBuilder.loadTexts:zxMsagSipUserTable.setStatus(_A)
_ZxMsagSipUserEntry_Object=MibTableRow
zxMsagSipUserEntry=_ZxMsagSipUserEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1))
zxMsagSipUserEntry.setIndexNames((0,_F,_f),(0,_F,_g),(0,_F,_h),(0,_F,_i))
if mibBuilder.loadTexts:zxMsagSipUserEntry.setStatus(_A)
class _ZxMsagSipUserRack_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxMsagSipUserRack_Type.__name__=_B
_ZxMsagSipUserRack_Object=MibTableColumn
zxMsagSipUserRack=_ZxMsagSipUserRack_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,1),_ZxMsagSipUserRack_Type())
zxMsagSipUserRack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxMsagSipUserRack.setStatus(_A)
class _ZxMsagSipUserShelf_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_ZxMsagSipUserShelf_Type.__name__=_B
_ZxMsagSipUserShelf_Object=MibTableColumn
zxMsagSipUserShelf=_ZxMsagSipUserShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,2),_ZxMsagSipUserShelf_Type())
zxMsagSipUserShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxMsagSipUserShelf.setStatus(_A)
class _ZxMsagSipUserSlot_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_ZxMsagSipUserSlot_Type.__name__=_B
_ZxMsagSipUserSlot_Object=MibTableColumn
zxMsagSipUserSlot=_ZxMsagSipUserSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,3),_ZxMsagSipUserSlot_Type())
zxMsagSipUserSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxMsagSipUserSlot.setStatus(_A)
class _ZxMsagSipUserIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_ZxMsagSipUserIndex_Type.__name__=_B
_ZxMsagSipUserIndex_Object=MibTableColumn
zxMsagSipUserIndex=_ZxMsagSipUserIndex_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,4),_ZxMsagSipUserIndex_Type())
zxMsagSipUserIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxMsagSipUserIndex.setStatus(_A)
class _ZxMsagSipUserOperNum_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_ZxMsagSipUserOperNum_Type.__name__=_B
_ZxMsagSipUserOperNum_Object=MibTableColumn
zxMsagSipUserOperNum=_ZxMsagSipUserOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,5),_ZxMsagSipUserOperNum_Type())
zxMsagSipUserOperNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserOperNum.setStatus(_A)
class _ZxMsagSipUserSipDigit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxMsagSipUserSipDigit_Type.__name__=_H
_ZxMsagSipUserSipDigit_Object=MibTableColumn
zxMsagSipUserSipDigit=_ZxMsagSipUserSipDigit_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,6),_ZxMsagSipUserSipDigit_Type())
zxMsagSipUserSipDigit.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserSipDigit.setStatus(_A)
class _ZxMsagSipUserAuthusername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxMsagSipUserAuthusername_Type.__name__=_H
_ZxMsagSipUserAuthusername_Object=MibTableColumn
zxMsagSipUserAuthusername=_ZxMsagSipUserAuthusername_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,7),_ZxMsagSipUserAuthusername_Type())
zxMsagSipUserAuthusername.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserAuthusername.setStatus(_A)
class _ZxMsagSipUserId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxMsagSipUserId_Type.__name__=_H
_ZxMsagSipUserId_Object=MibTableColumn
zxMsagSipUserId=_ZxMsagSipUserId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,8),_ZxMsagSipUserId_Type())
zxMsagSipUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserId.setStatus(_A)
class _ZxMsagSipUserType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('type1',1),(_Y,2),(_Z,3)))
_ZxMsagSipUserType_Type.__name__=_B
_ZxMsagSipUserType_Object=MibTableColumn
zxMsagSipUserType=_ZxMsagSipUserType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,9),_ZxMsagSipUserType_Type())
zxMsagSipUserType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserType.setStatus(_A)
class _ZxMsagSipUserBeginNo_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxMsagSipUserBeginNo_Type.__name__=_B
_ZxMsagSipUserBeginNo_Object=MibTableColumn
zxMsagSipUserBeginNo=_ZxMsagSipUserBeginNo_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,10),_ZxMsagSipUserBeginNo_Type())
zxMsagSipUserBeginNo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserBeginNo.setStatus(_A)
class _ZxMsagSipUserDigitLen_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ZxMsagSipUserDigitLen_Type.__name__=_B
_ZxMsagSipUserDigitLen_Object=MibTableColumn
zxMsagSipUserDigitLen=_ZxMsagSipUserDigitLen_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,11),_ZxMsagSipUserDigitLen_Type())
zxMsagSipUserDigitLen.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserDigitLen.setStatus(_A)
class _ZxMsagSipUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxMsagSipUserPassword_Type.__name__=_H
_ZxMsagSipUserPassword_Object=MibTableColumn
zxMsagSipUserPassword=_ZxMsagSipUserPassword_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,12),_ZxMsagSipUserPassword_Type())
zxMsagSipUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserPassword.setStatus(_A)
class _ZxMsagSipUserDstngRing_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ZxMsagSipUserDstngRing_Type.__name__=_B
_ZxMsagSipUserDstngRing_Object=MibTableColumn
zxMsagSipUserDstngRing=_ZxMsagSipUserDstngRing_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,13),_ZxMsagSipUserDstngRing_Type())
zxMsagSipUserDstngRing.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserDstngRing.setStatus(_A)
class _ZxMsagSipUserHotlineType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noneHotline',1),('instantHotline',2),('delayHotline',3)))
_ZxMsagSipUserHotlineType_Type.__name__=_B
_ZxMsagSipUserHotlineType_Object=MibTableColumn
zxMsagSipUserHotlineType=_ZxMsagSipUserHotlineType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,14),_ZxMsagSipUserHotlineType_Type())
zxMsagSipUserHotlineType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserHotlineType.setStatus(_A)
class _ZxMsagSipUserHotlineNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxMsagSipUserHotlineNum_Type.__name__=_H
_ZxMsagSipUserHotlineNum_Object=MibTableColumn
zxMsagSipUserHotlineNum=_ZxMsagSipUserHotlineNum_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,15),_ZxMsagSipUserHotlineNum_Type())
zxMsagSipUserHotlineNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserHotlineNum.setStatus(_A)
class _ZxMsagSipUserDigitMap_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ZxMsagSipUserDigitMap_Type.__name__=_H
_ZxMsagSipUserDigitMap_Object=MibTableColumn
zxMsagSipUserDigitMap=_ZxMsagSipUserDigitMap_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,16),_ZxMsagSipUserDigitMap_Type())
zxMsagSipUserDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserDigitMap.setStatus(_A)
class _ZxMsagSipUserOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_a,2)))
_ZxMsagSipUserOperType_Type.__name__=_B
_ZxMsagSipUserOperType_Object=MibTableColumn
zxMsagSipUserOperType=_ZxMsagSipUserOperType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,17),_ZxMsagSipUserOperType_Type())
zxMsagSipUserOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserOperType.setStatus(_A)
class _ZxMsagSipUserGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_ZxMsagSipUserGroupId_Type.__name__=_B
_ZxMsagSipUserGroupId_Object=MibTableColumn
zxMsagSipUserGroupId=_ZxMsagSipUserGroupId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,18),_ZxMsagSipUserGroupId_Type())
zxMsagSipUserGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserGroupId.setStatus(_A)
class _ZxMsagSipUserAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxMsagSipUserAdminStatus_Type.__name__=_B
_ZxMsagSipUserAdminStatus_Object=MibTableColumn
zxMsagSipUserAdminStatus=_ZxMsagSipUserAdminStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,19),_ZxMsagSipUserAdminStatus_Type())
zxMsagSipUserAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserAdminStatus.setStatus(_A)
class _ZxMsagSipUserSessionLimit_Type(TruthValue):defaultValue=2
_ZxMsagSipUserSessionLimit_Type.__name__=_I
_ZxMsagSipUserSessionLimit_Object=MibTableColumn
zxMsagSipUserSessionLimit=_ZxMsagSipUserSessionLimit_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,20),_ZxMsagSipUserSessionLimit_Type())
zxMsagSipUserSessionLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserSessionLimit.setStatus(_A)
class _ZxMsagSipUserRegisterStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('failed',2)))
_ZxMsagSipUserRegisterStatus_Type.__name__=_B
_ZxMsagSipUserRegisterStatus_Object=MibTableColumn
zxMsagSipUserRegisterStatus=_ZxMsagSipUserRegisterStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,21),_ZxMsagSipUserRegisterStatus_Type())
zxMsagSipUserRegisterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxMsagSipUserRegisterStatus.setStatus(_A)
_ZxMsagSipUserRowStatus_Type=RowStatus
_ZxMsagSipUserRowStatus_Object=MibTableColumn
zxMsagSipUserRowStatus=_ZxMsagSipUserRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,8,1,1,50),_ZxMsagSipUserRowStatus_Type())
zxMsagSipUserRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipUserRowStatus.setStatus(_A)
_ZxMsagSipAccessCodeTable_Object=MibTable
zxMsagSipAccessCodeTable=_ZxMsagSipAccessCodeTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,2))
if mibBuilder.loadTexts:zxMsagSipAccessCodeTable.setStatus(_A)
_ZxMsagSipAccessCodeEntry_Object=MibTableRow
zxMsagSipAccessCodeEntry=_ZxMsagSipAccessCodeEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,2,1))
zxMsagSipAccessCodeEntry.setIndexNames((0,_F,_k),(0,_F,_l))
if mibBuilder.loadTexts:zxMsagSipAccessCodeEntry.setStatus(_A)
class _ZxMsagSipAccessCodeMgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxMsagSipAccessCodeMgId_Type.__name__=_B
_ZxMsagSipAccessCodeMgId_Object=MibTableColumn
zxMsagSipAccessCodeMgId=_ZxMsagSipAccessCodeMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,2,1,1),_ZxMsagSipAccessCodeMgId_Type())
zxMsagSipAccessCodeMgId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxMsagSipAccessCodeMgId.setStatus(_A)
class _ZxMsagSipAccessCodeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_ZxMsagSipAccessCodeId_Type.__name__=_B
_ZxMsagSipAccessCodeId_Object=MibTableColumn
zxMsagSipAccessCodeId=_ZxMsagSipAccessCodeId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,2,1,2),_ZxMsagSipAccessCodeId_Type())
zxMsagSipAccessCodeId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxMsagSipAccessCodeId.setStatus(_A)
class _ZxMsagSipAccessCodecode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,6))
_ZxMsagSipAccessCodecode_Type.__name__=_H
_ZxMsagSipAccessCodecode_Object=MibTableColumn
zxMsagSipAccessCodecode=_ZxMsagSipAccessCodecode_Object((1,3,6,1,4,1,3902,1015,5200,3,8,2,1,3),_ZxMsagSipAccessCodecode_Type())
zxMsagSipAccessCodecode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipAccessCodecode.setStatus(_A)
_ZxMsagSipAccessCodeRowStatus_Type=RowStatus
_ZxMsagSipAccessCodeRowStatus_Object=MibTableColumn
zxMsagSipAccessCodeRowStatus=_ZxMsagSipAccessCodeRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,8,2,1,20),_ZxMsagSipAccessCodeRowStatus_Type())
zxMsagSipAccessCodeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipAccessCodeRowStatus.setStatus(_A)
_ZxMsagSipServiceCodeTable_Object=MibTable
zxMsagSipServiceCodeTable=_ZxMsagSipServiceCodeTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,3))
if mibBuilder.loadTexts:zxMsagSipServiceCodeTable.setStatus(_A)
_ZxMsagSipServiceCodeEntry_Object=MibTableRow
zxMsagSipServiceCodeEntry=_ZxMsagSipServiceCodeEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,3,1))
zxMsagSipServiceCodeEntry.setIndexNames((0,_F,_m),(0,_F,_n))
if mibBuilder.loadTexts:zxMsagSipServiceCodeEntry.setStatus(_A)
class _ZxMsagSipServiceCodeMgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxMsagSipServiceCodeMgId_Type.__name__=_B
_ZxMsagSipServiceCodeMgId_Object=MibTableColumn
zxMsagSipServiceCodeMgId=_ZxMsagSipServiceCodeMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,3,1,1),_ZxMsagSipServiceCodeMgId_Type())
zxMsagSipServiceCodeMgId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxMsagSipServiceCodeMgId.setStatus(_A)
class _ZxMsagSipServiceCodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('conference',1),('threeWayConference',2),('refere',3)))
_ZxMsagSipServiceCodeType_Type.__name__=_B
_ZxMsagSipServiceCodeType_Object=MibTableColumn
zxMsagSipServiceCodeType=_ZxMsagSipServiceCodeType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,3,1,2),_ZxMsagSipServiceCodeType_Type())
zxMsagSipServiceCodeType.setMaxAccess(_G)
if mibBuilder.loadTexts:zxMsagSipServiceCodeType.setStatus(_A)
class _ZxMsagSipServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxMsagSipServiceCode_Type.__name__=_H
_ZxMsagSipServiceCode_Object=MibTableColumn
zxMsagSipServiceCode=_ZxMsagSipServiceCode_Object((1,3,6,1,4,1,3902,1015,5200,3,8,3,1,3),_ZxMsagSipServiceCode_Type())
zxMsagSipServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipServiceCode.setStatus(_A)
_ZxMsagSipServiceCodeRowStatus_Type=RowStatus
_ZxMsagSipServiceCodeRowStatus_Object=MibTableColumn
zxMsagSipServiceCodeRowStatus=_ZxMsagSipServiceCodeRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,8,3,1,20),_ZxMsagSipServiceCodeRowStatus_Type())
zxMsagSipServiceCodeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipServiceCodeRowStatus.setStatus(_A)
_ZxMsagSipGenFmtTable_Object=MibTable
zxMsagSipGenFmtTable=_ZxMsagSipGenFmtTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,4))
if mibBuilder.loadTexts:zxMsagSipGenFmtTable.setStatus(_A)
_ZxMsagSipGenFmtEntry_Object=MibTableRow
zxMsagSipGenFmtEntry=_ZxMsagSipGenFmtEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,4,1))
zxMsagSipGenFmtEntry.setIndexNames((0,_F,_o),(0,_F,_p))
if mibBuilder.loadTexts:zxMsagSipGenFmtEntry.setStatus(_A)
class _ZxMsagSipGenFmtMgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxMsagSipGenFmtMgId_Type.__name__=_B
_ZxMsagSipGenFmtMgId_Object=MibTableColumn
zxMsagSipGenFmtMgId=_ZxMsagSipGenFmtMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,4,1,1),_ZxMsagSipGenFmtMgId_Type())
zxMsagSipGenFmtMgId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxMsagSipGenFmtMgId.setStatus(_A)
class _ZxMsagSipGenFmtField_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('from',1),('to',2),('requireline',3)))
_ZxMsagSipGenFmtField_Type.__name__=_B
_ZxMsagSipGenFmtField_Object=MibTableColumn
zxMsagSipGenFmtField=_ZxMsagSipGenFmtField_Object((1,3,6,1,4,1,3902,1015,5200,3,8,4,1,2),_ZxMsagSipGenFmtField_Type())
zxMsagSipGenFmtField.setMaxAccess(_G)
if mibBuilder.loadTexts:zxMsagSipGenFmtField.setStatus(_A)
class _ZxMsagSipGenFmtValue_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),('telephone',2)))
_ZxMsagSipGenFmtValue_Type.__name__=_B
_ZxMsagSipGenFmtValue_Object=MibTableColumn
zxMsagSipGenFmtValue=_ZxMsagSipGenFmtValue_Object((1,3,6,1,4,1,3902,1015,5200,3,8,4,1,3),_ZxMsagSipGenFmtValue_Type())
zxMsagSipGenFmtValue.setMaxAccess(_C)
if mibBuilder.loadTexts:zxMsagSipGenFmtValue.setStatus(_A)
_ZxMsagSipCapTable_Object=MibTable
zxMsagSipCapTable=_ZxMsagSipCapTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5))
if mibBuilder.loadTexts:zxMsagSipCapTable.setStatus(_A)
_ZxMsagSipCapEntry_Object=MibTableRow
zxMsagSipCapEntry=_ZxMsagSipCapEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1))
zxMsagSipCapEntry.setIndexNames((0,_F,_q))
if mibBuilder.loadTexts:zxMsagSipCapEntry.setStatus(_A)
class _ZxMsagSipCapMgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxMsagSipCapMgId_Type.__name__=_B
_ZxMsagSipCapMgId_Object=MibTableColumn
zxMsagSipCapMgId=_ZxMsagSipCapMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,1),_ZxMsagSipCapMgId_Type())
zxMsagSipCapMgId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxMsagSipCapMgId.setStatus(_A)
class _ZxMsagSipCapSpPrecondition_Type(TruthValue):defaultValue=2
_ZxMsagSipCapSpPrecondition_Type.__name__=_I
_ZxMsagSipCapSpPrecondition_Object=MibTableColumn
zxMsagSipCapSpPrecondition=_ZxMsagSipCapSpPrecondition_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,2),_ZxMsagSipCapSpPrecondition_Type())
zxMsagSipCapSpPrecondition.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSpPrecondition.setStatus(_A)
class _ZxMsagSipCapNeedReserveRes_Type(TruthValue):defaultValue=2
_ZxMsagSipCapNeedReserveRes_Type.__name__=_I
_ZxMsagSipCapNeedReserveRes_Object=MibTableColumn
zxMsagSipCapNeedReserveRes=_ZxMsagSipCapNeedReserveRes_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,3),_ZxMsagSipCapNeedReserveRes_Type())
zxMsagSipCapNeedReserveRes.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapNeedReserveRes.setStatus(_A)
class _ZxMsagSipCapSpEarlySession_Type(TruthValue):defaultValue=2
_ZxMsagSipCapSpEarlySession_Type.__name__=_I
_ZxMsagSipCapSpEarlySession_Object=MibTableColumn
zxMsagSipCapSpEarlySession=_ZxMsagSipCapSpEarlySession_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,4),_ZxMsagSipCapSpEarlySession_Type())
zxMsagSipCapSpEarlySession.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSpEarlySession.setStatus(_A)
class _ZxMsagSipCapSp100Rel_Type(TruthValue):defaultValue=2
_ZxMsagSipCapSp100Rel_Type.__name__=_I
_ZxMsagSipCapSp100Rel_Object=MibTableColumn
zxMsagSipCapSp100Rel=_ZxMsagSipCapSp100Rel_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,5),_ZxMsagSipCapSp100Rel_Type())
zxMsagSipCapSp100Rel.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSp100Rel.setStatus(_A)
class _ZxMsagSipCapSpPath_Type(TruthValue):defaultValue=2
_ZxMsagSipCapSpPath_Type.__name__=_I
_ZxMsagSipCapSpPath_Object=MibTableColumn
zxMsagSipCapSpPath=_ZxMsagSipCapSpPath_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,6),_ZxMsagSipCapSpPath_Type())
zxMsagSipCapSpPath.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSpPath.setStatus(_A)
class _ZxMsagSipCapSpReplaces_Type(TruthValue):defaultValue=1
_ZxMsagSipCapSpReplaces_Type.__name__=_I
_ZxMsagSipCapSpReplaces_Object=MibTableColumn
zxMsagSipCapSpReplaces=_ZxMsagSipCapSpReplaces_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,7),_ZxMsagSipCapSpReplaces_Type())
zxMsagSipCapSpReplaces.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSpReplaces.setStatus(_A)
class _ZxMsagSipCapSpTimer_Type(TruthValue):defaultValue=1
_ZxMsagSipCapSpTimer_Type.__name__=_I
_ZxMsagSipCapSpTimer_Object=MibTableColumn
zxMsagSipCapSpTimer=_ZxMsagSipCapSpTimer_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,8),_ZxMsagSipCapSpTimer_Type())
zxMsagSipCapSpTimer.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSpTimer.setStatus(_A)
class _ZxMsagSipCapAudioCodePri1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_K,1),(_L,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_J,255)))
_ZxMsagSipCapAudioCodePri1_Type.__name__=_B
_ZxMsagSipCapAudioCodePri1_Object=MibTableColumn
zxMsagSipCapAudioCodePri1=_ZxMsagSipCapAudioCodePri1_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,9),_ZxMsagSipCapAudioCodePri1_Type())
zxMsagSipCapAudioCodePri1.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapAudioCodePri1.setStatus(_A)
class _ZxMsagSipCapAudioCodePri2_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_K,1),(_L,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_J,255)))
_ZxMsagSipCapAudioCodePri2_Type.__name__=_B
_ZxMsagSipCapAudioCodePri2_Object=MibTableColumn
zxMsagSipCapAudioCodePri2=_ZxMsagSipCapAudioCodePri2_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,10),_ZxMsagSipCapAudioCodePri2_Type())
zxMsagSipCapAudioCodePri2.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapAudioCodePri2.setStatus(_A)
class _ZxMsagSipCapAudioCodePri3_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_K,1),(_L,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_J,255)))
_ZxMsagSipCapAudioCodePri3_Type.__name__=_B
_ZxMsagSipCapAudioCodePri3_Object=MibTableColumn
zxMsagSipCapAudioCodePri3=_ZxMsagSipCapAudioCodePri3_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,11),_ZxMsagSipCapAudioCodePri3_Type())
zxMsagSipCapAudioCodePri3.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapAudioCodePri3.setStatus(_A)
class _ZxMsagSipCapAudioCodePri4_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_K,1),(_L,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_J,255)))
_ZxMsagSipCapAudioCodePri4_Type.__name__=_B
_ZxMsagSipCapAudioCodePri4_Object=MibTableColumn
zxMsagSipCapAudioCodePri4=_ZxMsagSipCapAudioCodePri4_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,12),_ZxMsagSipCapAudioCodePri4_Type())
zxMsagSipCapAudioCodePri4.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapAudioCodePri4.setStatus(_A)
class _ZxMsagSipCapAudioCodePri5_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_K,1),(_L,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_J,255)))
_ZxMsagSipCapAudioCodePri5_Type.__name__=_B
_ZxMsagSipCapAudioCodePri5_Object=MibTableColumn
zxMsagSipCapAudioCodePri5=_ZxMsagSipCapAudioCodePri5_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,13),_ZxMsagSipCapAudioCodePri5_Type())
zxMsagSipCapAudioCodePri5.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapAudioCodePri5.setStatus(_A)
class _ZxMsagSipCapAudioCodePri6_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_K,1),(_L,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_J,255)))
_ZxMsagSipCapAudioCodePri6_Type.__name__=_B
_ZxMsagSipCapAudioCodePri6_Object=MibTableColumn
zxMsagSipCapAudioCodePri6=_ZxMsagSipCapAudioCodePri6_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,14),_ZxMsagSipCapAudioCodePri6_Type())
zxMsagSipCapAudioCodePri6.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapAudioCodePri6.setStatus(_A)
class _ZxMsagSipCapAudioCodePri7_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,255)));namedValues=NamedValues(*((_K,1),(_L,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_J,255)))
_ZxMsagSipCapAudioCodePri7_Type.__name__=_B
_ZxMsagSipCapAudioCodePri7_Object=MibTableColumn
zxMsagSipCapAudioCodePri7=_ZxMsagSipCapAudioCodePri7_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,15),_ZxMsagSipCapAudioCodePri7_Type())
zxMsagSipCapAudioCodePri7.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapAudioCodePri7.setStatus(_A)
class _ZxMsagSipCapDtmfRelayPri1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_r,1),(_s,2),(_J,255)))
_ZxMsagSipCapDtmfRelayPri1_Type.__name__=_B
_ZxMsagSipCapDtmfRelayPri1_Object=MibTableColumn
zxMsagSipCapDtmfRelayPri1=_ZxMsagSipCapDtmfRelayPri1_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,16),_ZxMsagSipCapDtmfRelayPri1_Type())
zxMsagSipCapDtmfRelayPri1.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapDtmfRelayPri1.setStatus(_A)
class _ZxMsagSipCapDtmfRelayPri2_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_r,1),(_s,2),(_J,255)))
_ZxMsagSipCapDtmfRelayPri2_Type.__name__=_B
_ZxMsagSipCapDtmfRelayPri2_Object=MibTableColumn
zxMsagSipCapDtmfRelayPri2=_ZxMsagSipCapDtmfRelayPri2_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,17),_ZxMsagSipCapDtmfRelayPri2_Type())
zxMsagSipCapDtmfRelayPri2.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapDtmfRelayPri2.setStatus(_A)
class _ZxMsagSipCapFaxPri1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('t30',1),('t38',2),(_J,255)))
_ZxMsagSipCapFaxPri1_Type.__name__=_B
_ZxMsagSipCapFaxPri1_Object=MibTableColumn
zxMsagSipCapFaxPri1=_ZxMsagSipCapFaxPri1_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,18),_ZxMsagSipCapFaxPri1_Type())
zxMsagSipCapFaxPri1.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapFaxPri1.setStatus(_A)
class _ZxMsagSipCapFaxPri2_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('t30',1),('t38',2),(_J,255)))
_ZxMsagSipCapFaxPri2_Type.__name__=_B
_ZxMsagSipCapFaxPri2_Object=MibTableColumn
zxMsagSipCapFaxPri2=_ZxMsagSipCapFaxPri2_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,19),_ZxMsagSipCapFaxPri2_Type())
zxMsagSipCapFaxPri2.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapFaxPri2.setStatus(_A)
class _ZxMsagSipCapSpFaxModem_Type(TruthValue):defaultValue=2
_ZxMsagSipCapSpFaxModem_Type.__name__=_I
_ZxMsagSipCapSpFaxModem_Object=MibTableColumn
zxMsagSipCapSpFaxModem=_ZxMsagSipCapSpFaxModem_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,20),_ZxMsagSipCapSpFaxModem_Type())
zxMsagSipCapSpFaxModem.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSpFaxModem.setStatus(_A)
class _ZxMsagSipCapSessionMaxExpire_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxMsagSipCapSessionMaxExpire_Type.__name__=_B
_ZxMsagSipCapSessionMaxExpire_Object=MibTableColumn
zxMsagSipCapSessionMaxExpire=_ZxMsagSipCapSessionMaxExpire_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,21),_ZxMsagSipCapSessionMaxExpire_Type())
zxMsagSipCapSessionMaxExpire.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSessionMaxExpire.setStatus(_A)
class _ZxMsagSipCapSessionMinExpire_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxMsagSipCapSessionMinExpire_Type.__name__=_B
_ZxMsagSipCapSessionMinExpire_Object=MibTableColumn
zxMsagSipCapSessionMinExpire=_ZxMsagSipCapSessionMinExpire_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,22),_ZxMsagSipCapSessionMinExpire_Type())
zxMsagSipCapSessionMinExpire.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSessionMinExpire.setStatus(_A)
class _ZxMsagSipCapSessionRefresher_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_ZxMsagSipCapSessionRefresher_Type.__name__=_B
_ZxMsagSipCapSessionRefresher_Object=MibTableColumn
zxMsagSipCapSessionRefresher=_ZxMsagSipCapSessionRefresher_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,23),_ZxMsagSipCapSessionRefresher_Type())
zxMsagSipCapSessionRefresher.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSessionRefresher.setStatus(_A)
class _ZxMsagSipCapDisplayFrom_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('from',1),('pai',2)))
_ZxMsagSipCapDisplayFrom_Type.__name__=_B
_ZxMsagSipCapDisplayFrom_Object=MibTableColumn
zxMsagSipCapDisplayFrom=_ZxMsagSipCapDisplayFrom_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,24),_ZxMsagSipCapDisplayFrom_Type())
zxMsagSipCapDisplayFrom.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapDisplayFrom.setStatus(_A)
class _ZxMsagSipCapRegisterExpire_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxMsagSipCapRegisterExpire_Type.__name__=_B
_ZxMsagSipCapRegisterExpire_Object=MibTableColumn
zxMsagSipCapRegisterExpire=_ZxMsagSipCapRegisterExpire_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,25),_ZxMsagSipCapRegisterExpire_Type())
zxMsagSipCapRegisterExpire.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapRegisterExpire.setStatus(_A)
class _ZxMsagSipCapReqMsgAuth_Type(TruthValue):defaultValue=2
_ZxMsagSipCapReqMsgAuth_Type.__name__=_I
_ZxMsagSipCapReqMsgAuth_Object=MibTableColumn
zxMsagSipCapReqMsgAuth=_ZxMsagSipCapReqMsgAuth_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,26),_ZxMsagSipCapReqMsgAuth_Type())
zxMsagSipCapReqMsgAuth.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapReqMsgAuth.setStatus(_A)
class _ZxMsagSipCapPPreService_Type(TruthValue):defaultValue=1
_ZxMsagSipCapPPreService_Type.__name__=_I
_ZxMsagSipCapPPreService_Object=MibTableColumn
zxMsagSipCapPPreService=_ZxMsagSipCapPPreService_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,27),_ZxMsagSipCapPPreService_Type())
zxMsagSipCapPPreService.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapPPreService.setStatus(_A)
class _ZxMsagSipCapAuthWithDomain_Type(TruthValue):defaultValue=2
_ZxMsagSipCapAuthWithDomain_Type.__name__=_I
_ZxMsagSipCapAuthWithDomain_Object=MibTableColumn
zxMsagSipCapAuthWithDomain=_ZxMsagSipCapAuthWithDomain_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,28),_ZxMsagSipCapAuthWithDomain_Type())
zxMsagSipCapAuthWithDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapAuthWithDomain.setStatus(_A)
class _ZxMsagSipCapPackageInterval_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,50))
_ZxMsagSipCapPackageInterval_Type.__name__=_B
_ZxMsagSipCapPackageInterval_Object=MibTableColumn
zxMsagSipCapPackageInterval=_ZxMsagSipCapPackageInterval_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,29),_ZxMsagSipCapPackageInterval_Type())
zxMsagSipCapPackageInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapPackageInterval.setStatus(_A)
class _ZxMsagSipCapSessionLimit_Type(TruthValue):defaultValue=2
_ZxMsagSipCapSessionLimit_Type.__name__=_I
_ZxMsagSipCapSessionLimit_Object=MibTableColumn
zxMsagSipCapSessionLimit=_ZxMsagSipCapSessionLimit_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,30),_ZxMsagSipCapSessionLimit_Type())
zxMsagSipCapSessionLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSessionLimit.setStatus(_A)
class _ZxMsagSipCapUserParam_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('null',1),('phone',2),('ip',3),('other',4)))
_ZxMsagSipCapUserParam_Type.__name__=_B
_ZxMsagSipCapUserParam_Object=MibTableColumn
zxMsagSipCapUserParam=_ZxMsagSipCapUserParam_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,31),_ZxMsagSipCapUserParam_Type())
zxMsagSipCapUserParam.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapUserParam.setStatus(_A)
class _ZxMsagSipCapDtmfSendingType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('rtp',1),('sipinfo',2),('broadSoftInfo',3),('ibx1000Info',4)))
_ZxMsagSipCapDtmfSendingType_Type.__name__=_B
_ZxMsagSipCapDtmfSendingType_Object=MibTableColumn
zxMsagSipCapDtmfSendingType=_ZxMsagSipCapDtmfSendingType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,32),_ZxMsagSipCapDtmfSendingType_Type())
zxMsagSipCapDtmfSendingType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapDtmfSendingType.setStatus(_A)
class _ZxMsagSipCapEarlyMedia_Type(TruthValue):defaultValue=2
_ZxMsagSipCapEarlyMedia_Type.__name__=_I
_ZxMsagSipCapEarlyMedia_Object=MibTableColumn
zxMsagSipCapEarlyMedia=_ZxMsagSipCapEarlyMedia_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,33),_ZxMsagSipCapEarlyMedia_Type())
zxMsagSipCapEarlyMedia.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapEarlyMedia.setStatus(_A)
class _ZxMsagSipCapEchoCancel_Type(TruthValue):defaultValue=2
_ZxMsagSipCapEchoCancel_Type.__name__=_I
_ZxMsagSipCapEchoCancel_Object=MibTableColumn
zxMsagSipCapEchoCancel=_ZxMsagSipCapEchoCancel_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,34),_ZxMsagSipCapEchoCancel_Type())
zxMsagSipCapEchoCancel.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapEchoCancel.setStatus(_A)
class _ZxMsagSipCapHistoryInfo_Type(TruthValue):defaultValue=2
_ZxMsagSipCapHistoryInfo_Type.__name__=_I
_ZxMsagSipCapHistoryInfo_Object=MibTableColumn
zxMsagSipCapHistoryInfo=_ZxMsagSipCapHistoryInfo_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,35),_ZxMsagSipCapHistoryInfo_Type())
zxMsagSipCapHistoryInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapHistoryInfo.setStatus(_A)
class _ZxMsagSipCapThreePartySvrCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxMsagSipCapThreePartySvrCode_Type.__name__=_H
_ZxMsagSipCapThreePartySvrCode_Object=MibTableColumn
zxMsagSipCapThreePartySvrCode=_ZxMsagSipCapThreePartySvrCode_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,36),_ZxMsagSipCapThreePartySvrCode_Type())
zxMsagSipCapThreePartySvrCode.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapThreePartySvrCode.setStatus(_A)
class _ZxMsagSipCapUserRegisterType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('explicit',1),('implicit',2)))
_ZxMsagSipCapUserRegisterType_Type.__name__=_B
_ZxMsagSipCapUserRegisterType_Object=MibTableColumn
zxMsagSipCapUserRegisterType=_ZxMsagSipCapUserRegisterType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,37),_ZxMsagSipCapUserRegisterType_Type())
zxMsagSipCapUserRegisterType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapUserRegisterType.setStatus(_A)
class _ZxMsagSipCapHeartbeatEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_ZxMsagSipCapHeartbeatEnable_Type.__name__=_B
_ZxMsagSipCapHeartbeatEnable_Object=MibTableColumn
zxMsagSipCapHeartbeatEnable=_ZxMsagSipCapHeartbeatEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,51),_ZxMsagSipCapHeartbeatEnable_Type())
zxMsagSipCapHeartbeatEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapHeartbeatEnable.setStatus(_A)
class _ZxMsagSipCapHeartbeatInterval_Type(Integer32):defaultValue=3000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxMsagSipCapHeartbeatInterval_Type.__name__=_B
_ZxMsagSipCapHeartbeatInterval_Object=MibTableColumn
zxMsagSipCapHeartbeatInterval=_ZxMsagSipCapHeartbeatInterval_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,52),_ZxMsagSipCapHeartbeatInterval_Type())
zxMsagSipCapHeartbeatInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapHeartbeatInterval.setStatus(_A)
class _ZxMsagSipCapSelfswitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxMsagSipCapSelfswitch_Type.__name__=_B
_ZxMsagSipCapSelfswitch_Object=MibTableColumn
zxMsagSipCapSelfswitch=_ZxMsagSipCapSelfswitch_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,53),_ZxMsagSipCapSelfswitch_Type())
zxMsagSipCapSelfswitch.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapSelfswitch.setStatus(_A)
class _ZxMsagSipCapCallProtection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxMsagSipCapCallProtection_Type.__name__=_B
_ZxMsagSipCapCallProtection_Object=MibTableColumn
zxMsagSipCapCallProtection=_ZxMsagSipCapCallProtection_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,54),_ZxMsagSipCapCallProtection_Type())
zxMsagSipCapCallProtection.setMaxAccess(_E)
if mibBuilder.loadTexts:zxMsagSipCapCallProtection.setStatus(_A)
class _ZxAnSipCapVideoMediaNegotiation_Type(TruthValue):defaultValue=2
_ZxAnSipCapVideoMediaNegotiation_Type.__name__=_I
_ZxAnSipCapVideoMediaNegotiation_Object=MibTableColumn
zxAnSipCapVideoMediaNegotiation=_ZxAnSipCapVideoMediaNegotiation_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,55),_ZxAnSipCapVideoMediaNegotiation_Type())
zxAnSipCapVideoMediaNegotiation.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapVideoMediaNegotiation.setStatus(_A)
class _ZxAnSipCapUserPhoneAppendEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxAnSipCapUserPhoneAppendEnable_Type.__name__=_B
_ZxAnSipCapUserPhoneAppendEnable_Object=MibTableColumn
zxAnSipCapUserPhoneAppendEnable=_ZxAnSipCapUserPhoneAppendEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,56),_ZxAnSipCapUserPhoneAppendEnable_Type())
zxAnSipCapUserPhoneAppendEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapUserPhoneAppendEnable.setStatus(_A)
class _ZxAnSipCapSendSubscribeMsgEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxAnSipCapSendSubscribeMsgEnable_Type.__name__=_B
_ZxAnSipCapSendSubscribeMsgEnable_Object=MibTableColumn
zxAnSipCapSendSubscribeMsgEnable=_ZxAnSipCapSendSubscribeMsgEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,57),_ZxAnSipCapSendSubscribeMsgEnable_Type())
zxAnSipCapSendSubscribeMsgEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapSendSubscribeMsgEnable.setStatus(_A)
class _ZxAnSipCapFaxCodePri1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_K,1),(_L,2),(_J,255)))
_ZxAnSipCapFaxCodePri1_Type.__name__=_B
_ZxAnSipCapFaxCodePri1_Object=MibTableColumn
zxAnSipCapFaxCodePri1=_ZxAnSipCapFaxCodePri1_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,58),_ZxAnSipCapFaxCodePri1_Type())
zxAnSipCapFaxCodePri1.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapFaxCodePri1.setStatus(_A)
class _ZxAnSipCapFaxCodePri2_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_K,1),(_L,2),(_J,255)))
_ZxAnSipCapFaxCodePri2_Type.__name__=_B
_ZxAnSipCapFaxCodePri2_Object=MibTableColumn
zxAnSipCapFaxCodePri2=_ZxAnSipCapFaxCodePri2_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,59),_ZxAnSipCapFaxCodePri2_Type())
zxAnSipCapFaxCodePri2.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapFaxCodePri2.setStatus(_A)
class _ZxAnSipCapFaxCodePri3_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_K,1),(_L,2),(_J,255)))
_ZxAnSipCapFaxCodePri3_Type.__name__=_B
_ZxAnSipCapFaxCodePri3_Object=MibTableColumn
zxAnSipCapFaxCodePri3=_ZxAnSipCapFaxCodePri3_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,60),_ZxAnSipCapFaxCodePri3_Type())
zxAnSipCapFaxCodePri3.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapFaxCodePri3.setStatus(_A)
class _ZxAnSipCapFaxCodePri4_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*((_K,1),(_L,2),(_J,255)))
_ZxAnSipCapFaxCodePri4_Type.__name__=_B
_ZxAnSipCapFaxCodePri4_Object=MibTableColumn
zxAnSipCapFaxCodePri4=_ZxAnSipCapFaxCodePri4_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,61),_ZxAnSipCapFaxCodePri4_Type())
zxAnSipCapFaxCodePri4.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapFaxCodePri4.setStatus(_A)
class _ZxAnSipCapFaxPacketInterval_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,50))
_ZxAnSipCapFaxPacketInterval_Type.__name__=_B
_ZxAnSipCapFaxPacketInterval_Object=MibTableColumn
zxAnSipCapFaxPacketInterval=_ZxAnSipCapFaxPacketInterval_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,62),_ZxAnSipCapFaxPacketInterval_Type())
zxAnSipCapFaxPacketInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapFaxPacketInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipCapFaxPacketInterval.setUnits('ms')
class _ZxAnSipCapAutoRefreshEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxAnSipCapAutoRefreshEnable_Type.__name__=_B
_ZxAnSipCapAutoRefreshEnable_Object=MibTableColumn
zxAnSipCapAutoRefreshEnable=_ZxAnSipCapAutoRefreshEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,63),_ZxAnSipCapAutoRefreshEnable_Type())
zxAnSipCapAutoRefreshEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapAutoRefreshEnable.setStatus(_A)
class _ZxAnSipCapImsHotlineValidTime_Type(Integer32):defaultValue=86400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(90,900000))
_ZxAnSipCapImsHotlineValidTime_Type.__name__=_B
_ZxAnSipCapImsHotlineValidTime_Object=MibTableColumn
zxAnSipCapImsHotlineValidTime=_ZxAnSipCapImsHotlineValidTime_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,64),_ZxAnSipCapImsHotlineValidTime_Type())
zxAnSipCapImsHotlineValidTime.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapImsHotlineValidTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipCapImsHotlineValidTime.setUnits(_O)
class _ZxAnSipCapDnsRequestInterval_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,65535))
_ZxAnSipCapDnsRequestInterval_Type.__name__=_B
_ZxAnSipCapDnsRequestInterval_Object=MibTableColumn
zxAnSipCapDnsRequestInterval=_ZxAnSipCapDnsRequestInterval_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,65),_ZxAnSipCapDnsRequestInterval_Type())
zxAnSipCapDnsRequestInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapDnsRequestInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipCapDnsRequestInterval.setUnits(_O)
class _ZxAnSipCapCallWaitInvite18xRsp_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(180,182))
_ZxAnSipCapCallWaitInvite18xRsp_Type.__name__=_B
_ZxAnSipCapCallWaitInvite18xRsp_Object=MibTableColumn
zxAnSipCapCallWaitInvite18xRsp=_ZxAnSipCapCallWaitInvite18xRsp_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,66),_ZxAnSipCapCallWaitInvite18xRsp_Type())
zxAnSipCapCallWaitInvite18xRsp.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapCallWaitInvite18xRsp.setStatus(_A)
class _ZxAnSipCapSubscribeUaProfileEn_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_ZxAnSipCapSubscribeUaProfileEn_Type.__name__=_B
_ZxAnSipCapSubscribeUaProfileEn_Object=MibTableColumn
zxAnSipCapSubscribeUaProfileEn=_ZxAnSipCapSubscribeUaProfileEn_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,67),_ZxAnSipCapSubscribeUaProfileEn_Type())
zxAnSipCapSubscribeUaProfileEn.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapSubscribeUaProfileEn.setStatus(_A)
class _ZxAnSipCapSubscribeMsgSummaryEn_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_ZxAnSipCapSubscribeMsgSummaryEn_Type.__name__=_B
_ZxAnSipCapSubscribeMsgSummaryEn_Object=MibTableColumn
zxAnSipCapSubscribeMsgSummaryEn=_ZxAnSipCapSubscribeMsgSummaryEn_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,68),_ZxAnSipCapSubscribeMsgSummaryEn_Type())
zxAnSipCapSubscribeMsgSummaryEn.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapSubscribeMsgSummaryEn.setStatus(_A)
class _ZxAnSipCapCallerControlEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_ZxAnSipCapCallerControlEnable_Type.__name__=_B
_ZxAnSipCapCallerControlEnable_Object=MibTableColumn
zxAnSipCapCallerControlEnable=_ZxAnSipCapCallerControlEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,69),_ZxAnSipCapCallerControlEnable_Type())
zxAnSipCapCallerControlEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapCallerControlEnable.setStatus(_A)
class _ZxAnSipCapNoDialSendInviteEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_ZxAnSipCapNoDialSendInviteEnable_Type.__name__=_B
_ZxAnSipCapNoDialSendInviteEnable_Object=MibTableColumn
zxAnSipCapNoDialSendInviteEnable=_ZxAnSipCapNoDialSendInviteEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,70),_ZxAnSipCapNoDialSendInviteEnable_Type())
zxAnSipCapNoDialSendInviteEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapNoDialSendInviteEnable.setStatus(_A)
class _ZxAnSipCapProxySvrAutoDrEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_ZxAnSipCapProxySvrAutoDrEnable_Type.__name__=_B
_ZxAnSipCapProxySvrAutoDrEnable_Object=MibTableColumn
zxAnSipCapProxySvrAutoDrEnable=_ZxAnSipCapProxySvrAutoDrEnable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,71),_ZxAnSipCapProxySvrAutoDrEnable_Type())
zxAnSipCapProxySvrAutoDrEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapProxySvrAutoDrEnable.setStatus(_A)
class _ZxAnSipCapProxySvrDrMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primaryFirst',1),('roundRobin',2)))
_ZxAnSipCapProxySvrDrMode_Type.__name__=_B
_ZxAnSipCapProxySvrDrMode_Object=MibTableColumn
zxAnSipCapProxySvrDrMode=_ZxAnSipCapProxySvrDrMode_Object((1,3,6,1,4,1,3902,1015,5200,3,8,5,1,72),_ZxAnSipCapProxySvrDrMode_Type())
zxAnSipCapProxySvrDrMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipCapProxySvrDrMode.setStatus(_A)
_ZxAnSipGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnSipGlobalObjects=_ZxAnSipGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,8,6))
class _ZxAnSipMgmtCapabilities_Type(Bits):namedValues=NamedValues(*(('group',0),('sipUaIp',1),('proxySvrDomainName',2),('nbPlatform',3),('userAdminStatus',4),('userSessionLimit',5)))
_ZxAnSipMgmtCapabilities_Type.__name__='Bits'
_ZxAnSipMgmtCapabilities_Object=MibScalar
zxAnSipMgmtCapabilities=_ZxAnSipMgmtCapabilities_Object((1,3,6,1,4,1,3902,1015,5200,3,8,6,1),_ZxAnSipMgmtCapabilities_Type())
zxAnSipMgmtCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipMgmtCapabilities.setStatus(_A)
class _ZxAnSipProcessReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reboot',1))
_ZxAnSipProcessReboot_Type.__name__=_B
_ZxAnSipProcessReboot_Object=MibScalar
zxAnSipProcessReboot=_ZxAnSipProcessReboot_Object((1,3,6,1,4,1,3902,1015,5200,3,8,6,2),_ZxAnSipProcessReboot_Type())
zxAnSipProcessReboot.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipProcessReboot.setStatus(_A)
_ZxAnSipProxyServerTable_Object=MibTable
zxAnSipProxyServerTable=_ZxAnSipProxyServerTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,7))
if mibBuilder.loadTexts:zxAnSipProxyServerTable.setStatus(_A)
_ZxAnSipProxyServerEntry_Object=MibTableRow
zxAnSipProxyServerEntry=_ZxAnSipProxyServerEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,7,1))
zxAnSipProxyServerEntry.setIndexNames((0,_F,_t))
if mibBuilder.loadTexts:zxAnSipProxyServerEntry.setStatus(_A)
class _ZxAnSipProxySvrId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnSipProxySvrId_Type.__name__=_B
_ZxAnSipProxySvrId_Object=MibTableColumn
zxAnSipProxySvrId=_ZxAnSipProxySvrId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,7,1,1),_ZxAnSipProxySvrId_Type())
zxAnSipProxySvrId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipProxySvrId.setStatus(_A)
_ZxAnSipProxySvrIp_Type=IpAddress
_ZxAnSipProxySvrIp_Object=MibTableColumn
zxAnSipProxySvrIp=_ZxAnSipProxySvrIp_Object((1,3,6,1,4,1,3902,1015,5200,3,8,7,1,2),_ZxAnSipProxySvrIp_Type())
zxAnSipProxySvrIp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipProxySvrIp.setStatus(_A)
class _ZxAnSipProxySvrPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnSipProxySvrPort_Type.__name__=_B
_ZxAnSipProxySvrPort_Object=MibTableColumn
zxAnSipProxySvrPort=_ZxAnSipProxySvrPort_Object((1,3,6,1,4,1,3902,1015,5200,3,8,7,1,3),_ZxAnSipProxySvrPort_Type())
zxAnSipProxySvrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipProxySvrPort.setStatus(_A)
class _ZxAnSipProxySvrNamingType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('useIp',1),('useDomainName',2),('dhcpOption120',3)))
_ZxAnSipProxySvrNamingType_Type.__name__=_B
_ZxAnSipProxySvrNamingType_Object=MibTableColumn
zxAnSipProxySvrNamingType=_ZxAnSipProxySvrNamingType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,7,1,4),_ZxAnSipProxySvrNamingType_Type())
zxAnSipProxySvrNamingType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipProxySvrNamingType.setStatus(_A)
class _ZxAnSipProxySvrDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnSipProxySvrDomainName_Type.__name__=_H
_ZxAnSipProxySvrDomainName_Object=MibTableColumn
zxAnSipProxySvrDomainName=_ZxAnSipProxySvrDomainName_Object((1,3,6,1,4,1,3902,1015,5200,3,8,7,1,5),_ZxAnSipProxySvrDomainName_Type())
zxAnSipProxySvrDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipProxySvrDomainName.setStatus(_A)
_ZxAnSipProxySvrRowStatus_Type=RowStatus
_ZxAnSipProxySvrRowStatus_Object=MibTableColumn
zxAnSipProxySvrRowStatus=_ZxAnSipProxySvrRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,8,7,1,20),_ZxAnSipProxySvrRowStatus_Type())
zxAnSipProxySvrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipProxySvrRowStatus.setStatus(_A)
_ZxAnSipUserAgentTable_Object=MibTable
zxAnSipUserAgentTable=_ZxAnSipUserAgentTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8))
if mibBuilder.loadTexts:zxAnSipUserAgentTable.setStatus(_A)
_ZxAnSipUserAgentEntry_Object=MibTableRow
zxAnSipUserAgentEntry=_ZxAnSipUserAgentEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1))
zxAnSipUserAgentEntry.setIndexNames((0,_F,_u))
if mibBuilder.loadTexts:zxAnSipUserAgentEntry.setStatus(_A)
class _ZxAnSipUaId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxAnSipUaId_Type.__name__=_B
_ZxAnSipUaId_Object=MibTableColumn
zxAnSipUaId=_ZxAnSipUaId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,1),_ZxAnSipUaId_Type())
zxAnSipUaId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipUaId.setStatus(_A)
class _ZxAnSipUaPort_Type(Integer32):defaultValue=5060;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnSipUaPort_Type.__name__=_B
_ZxAnSipUaPort_Object=MibTableColumn
zxAnSipUaPort=_ZxAnSipUaPort_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,2),_ZxAnSipUaPort_Type())
zxAnSipUaPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipUaPort.setStatus(_A)
class _ZxAnSipUaDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnSipUaDomainName_Type.__name__=_H
_ZxAnSipUaDomainName_Object=MibTableColumn
zxAnSipUaDomainName=_ZxAnSipUaDomainName_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,3),_ZxAnSipUaDomainName_Type())
zxAnSipUaDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipUaDomainName.setStatus(_A)
class _ZxAnSipUaProxySvrId1_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxAnSipUaProxySvrId1_Type.__name__=_B
_ZxAnSipUaProxySvrId1_Object=MibTableColumn
zxAnSipUaProxySvrId1=_ZxAnSipUaProxySvrId1_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,4),_ZxAnSipUaProxySvrId1_Type())
zxAnSipUaProxySvrId1.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipUaProxySvrId1.setStatus(_A)
class _ZxAnSipUaProxySvrId2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnSipUaProxySvrId2_Type.__name__=_B
_ZxAnSipUaProxySvrId2_Object=MibTableColumn
zxAnSipUaProxySvrId2=_ZxAnSipUaProxySvrId2_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,5),_ZxAnSipUaProxySvrId2_Type())
zxAnSipUaProxySvrId2.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipUaProxySvrId2.setStatus(_A)
class _ZxAnSipUaProxySvrId3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnSipUaProxySvrId3_Type.__name__=_B
_ZxAnSipUaProxySvrId3_Object=MibTableColumn
zxAnSipUaProxySvrId3=_ZxAnSipUaProxySvrId3_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,6),_ZxAnSipUaProxySvrId3_Type())
zxAnSipUaProxySvrId3.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipUaProxySvrId3.setStatus(_A)
class _ZxAnSipUaProxySvrId4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnSipUaProxySvrId4_Type.__name__=_B
_ZxAnSipUaProxySvrId4_Object=MibTableColumn
zxAnSipUaProxySvrId4=_ZxAnSipUaProxySvrId4_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,7),_ZxAnSipUaProxySvrId4_Type())
zxAnSipUaProxySvrId4.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipUaProxySvrId4.setStatus(_A)
class _ZxAnSipUaSelfswitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxAnSipUaSelfswitch_Type.__name__=_B
_ZxAnSipUaSelfswitch_Object=MibTableColumn
zxAnSipUaSelfswitch=_ZxAnSipUaSelfswitch_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,8),_ZxAnSipUaSelfswitch_Type())
zxAnSipUaSelfswitch.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipUaSelfswitch.setStatus(_A)
class _ZxAnSipUaCallProtection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_ZxAnSipUaCallProtection_Type.__name__=_B
_ZxAnSipUaCallProtection_Object=MibTableColumn
zxAnSipUaCallProtection=_ZxAnSipUaCallProtection_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,9),_ZxAnSipUaCallProtection_Type())
zxAnSipUaCallProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipUaCallProtection.setStatus(_A)
_ZxAnSipUaIpType_Type=InetAddressType
_ZxAnSipUaIpType_Object=MibTableColumn
zxAnSipUaIpType=_ZxAnSipUaIpType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,10),_ZxAnSipUaIpType_Type())
zxAnSipUaIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipUaIpType.setStatus(_A)
_ZxAnSipUaIp_Type=InetAddress
_ZxAnSipUaIp_Object=MibTableColumn
zxAnSipUaIp=_ZxAnSipUaIp_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,11),_ZxAnSipUaIp_Type())
zxAnSipUaIp.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipUaIp.setStatus(_A)
class _ZxAnSipUaSwitchProxySvrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ZxAnSipUaSwitchProxySvrId_Type.__name__=_B
_ZxAnSipUaSwitchProxySvrId_Object=MibTableColumn
zxAnSipUaSwitchProxySvrId=_ZxAnSipUaSwitchProxySvrId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,12),_ZxAnSipUaSwitchProxySvrId_Type())
zxAnSipUaSwitchProxySvrId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipUaSwitchProxySvrId.setStatus(_A)
class _ZxAnSipUaCurrentProxySvrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_ZxAnSipUaCurrentProxySvrId_Type.__name__=_B
_ZxAnSipUaCurrentProxySvrId_Object=MibTableColumn
zxAnSipUaCurrentProxySvrId=_ZxAnSipUaCurrentProxySvrId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,13),_ZxAnSipUaCurrentProxySvrId_Type())
zxAnSipUaCurrentProxySvrId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipUaCurrentProxySvrId.setStatus(_A)
_ZxAnSipUaRowStatus_Type=RowStatus
_ZxAnSipUaRowStatus_Object=MibTableColumn
zxAnSipUaRowStatus=_ZxAnSipUaRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,8,8,1,50),_ZxAnSipUaRowStatus_Type())
zxAnSipUaRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipUaRowStatus.setStatus(_A)
_ZxAnSipGroupTable_Object=MibTable
zxAnSipGroupTable=_ZxAnSipGroupTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20))
if mibBuilder.loadTexts:zxAnSipGroupTable.setStatus(_A)
_ZxAnSipGroupEntry_Object=MibTableRow
zxAnSipGroupEntry=_ZxAnSipGroupEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1))
zxAnSipGroupEntry.setIndexNames((0,_F,_v),(0,_F,_w))
if mibBuilder.loadTexts:zxAnSipGroupEntry.setStatus(_A)
class _ZxAnSipGroupMgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxAnSipGroupMgId_Type.__name__=_B
_ZxAnSipGroupMgId_Object=MibTableColumn
zxAnSipGroupMgId=_ZxAnSipGroupMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,1),_ZxAnSipGroupMgId_Type())
zxAnSipGroupMgId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipGroupMgId.setStatus(_A)
class _ZxAnSipGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_ZxAnSipGroupId_Type.__name__=_B
_ZxAnSipGroupId_Object=MibTableColumn
zxAnSipGroupId=_ZxAnSipGroupId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,2),_ZxAnSipGroupId_Type())
zxAnSipGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipGroupId.setStatus(_A)
class _ZxAnSipGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZxAnSipGroupName_Type.__name__=_H
_ZxAnSipGroupName_Object=MibTableColumn
zxAnSipGroupName=_ZxAnSipGroupName_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,3),_ZxAnSipGroupName_Type())
zxAnSipGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupName.setStatus(_A)
class _ZxAnSipGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pstn',1),('isdnbri',2),('isdnpri',3)))
_ZxAnSipGroupType_Type.__name__=_B
_ZxAnSipGroupType_Object=MibTableColumn
zxAnSipGroupType=_ZxAnSipGroupType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,4),_ZxAnSipGroupType_Type())
zxAnSipGroupType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupType.setStatus(_A)
class _ZxAnSipGroupOperNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_ZxAnSipGroupOperNum_Type.__name__=_B
_ZxAnSipGroupOperNum_Object=MibTableColumn
zxAnSipGroupOperNum=_ZxAnSipGroupOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,5),_ZxAnSipGroupOperNum_Type())
zxAnSipGroupOperNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupOperNum.setStatus(_A)
class _ZxAnSipGroupPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnSipGroupPhoneNumber_Type.__name__=_H
_ZxAnSipGroupPhoneNumber_Object=MibTableColumn
zxAnSipGroupPhoneNumber=_ZxAnSipGroupPhoneNumber_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,6),_ZxAnSipGroupPhoneNumber_Type())
zxAnSipGroupPhoneNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupPhoneNumber.setStatus(_A)
class _ZxAnSipGroupUserId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxAnSipGroupUserId_Type.__name__=_H
_ZxAnSipGroupUserId_Object=MibTableColumn
zxAnSipGroupUserId=_ZxAnSipGroupUserId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,7),_ZxAnSipGroupUserId_Type())
zxAnSipGroupUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupUserId.setStatus(_A)
class _ZxAnSipGroupAuthUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxAnSipGroupAuthUserName_Type.__name__=_H
_ZxAnSipGroupAuthUserName_Object=MibTableColumn
zxAnSipGroupAuthUserName=_ZxAnSipGroupAuthUserName_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,8),_ZxAnSipGroupAuthUserName_Type())
zxAnSipGroupAuthUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupAuthUserName.setStatus(_A)
class _ZxAnSipGroupOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('username',1),('userid',2),('all',3),('none',4)))
_ZxAnSipGroupOperType_Type.__name__=_B
_ZxAnSipGroupOperType_Object=MibTableColumn
zxAnSipGroupOperType=_ZxAnSipGroupOperType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,9),_ZxAnSipGroupOperType_Type())
zxAnSipGroupOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupOperType.setStatus(_A)
class _ZxAnSipGroupUserType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_Y,2),(_Z,3)))
_ZxAnSipGroupUserType_Type.__name__=_B
_ZxAnSipGroupUserType_Object=MibTableColumn
zxAnSipGroupUserType=_ZxAnSipGroupUserType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,10),_ZxAnSipGroupUserType_Type())
zxAnSipGroupUserType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupUserType.setStatus(_A)
class _ZxAnSipGroupUserStartNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnSipGroupUserStartNumber_Type.__name__=_B
_ZxAnSipGroupUserStartNumber_Object=MibTableColumn
zxAnSipGroupUserStartNumber=_ZxAnSipGroupUserStartNumber_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,11),_ZxAnSipGroupUserStartNumber_Type())
zxAnSipGroupUserStartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupUserStartNumber.setStatus(_A)
class _ZxAnSipGroupUserDigitLen_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ZxAnSipGroupUserDigitLen_Type.__name__=_B
_ZxAnSipGroupUserDigitLen_Object=MibTableColumn
zxAnSipGroupUserDigitLen=_ZxAnSipGroupUserDigitLen_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,12),_ZxAnSipGroupUserDigitLen_Type())
zxAnSipGroupUserDigitLen.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupUserDigitLen.setStatus(_A)
class _ZxAnSipGroupPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxAnSipGroupPassword_Type.__name__=_H
_ZxAnSipGroupPassword_Object=MibTableColumn
zxAnSipGroupPassword=_ZxAnSipGroupPassword_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,13),_ZxAnSipGroupPassword_Type())
zxAnSipGroupPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupPassword.setStatus(_A)
_ZxAnSipGroupRowStatus_Type=RowStatus
_ZxAnSipGroupRowStatus_Object=MibTableColumn
zxAnSipGroupRowStatus=_ZxAnSipGroupRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,8,20,1,30),_ZxAnSipGroupRowStatus_Type())
zxAnSipGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipGroupRowStatus.setStatus(_A)
_ZxAnSipIsdnDLinkTable_Object=MibTable
zxAnSipIsdnDLinkTable=_ZxAnSipIsdnDLinkTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21))
if mibBuilder.loadTexts:zxAnSipIsdnDLinkTable.setStatus(_A)
_ZxAnSipIsdnDLinkEntry_Object=MibTableRow
zxAnSipIsdnDLinkEntry=_ZxAnSipIsdnDLinkEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1))
zxAnSipIsdnDLinkEntry.setIndexNames((0,_F,_x),(0,_F,_y),(0,_F,_z))
if mibBuilder.loadTexts:zxAnSipIsdnDLinkEntry.setStatus(_A)
class _ZxAnSipIsdnDLinkMgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxAnSipIsdnDLinkMgId_Type.__name__=_B
_ZxAnSipIsdnDLinkMgId_Object=MibTableColumn
zxAnSipIsdnDLinkMgId=_ZxAnSipIsdnDLinkMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1,1),_ZxAnSipIsdnDLinkMgId_Type())
zxAnSipIsdnDLinkMgId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnDLinkMgId.setStatus(_A)
class _ZxAnSipIsdnDLinkGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_ZxAnSipIsdnDLinkGroupId_Type.__name__=_B
_ZxAnSipIsdnDLinkGroupId_Object=MibTableColumn
zxAnSipIsdnDLinkGroupId=_ZxAnSipIsdnDLinkGroupId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1,2),_ZxAnSipIsdnDLinkGroupId_Type())
zxAnSipIsdnDLinkGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnDLinkGroupId.setStatus(_A)
class _ZxAnSipIsdnDLinkLinkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_ZxAnSipIsdnDLinkLinkId_Type.__name__=_B
_ZxAnSipIsdnDLinkLinkId_Object=MibTableColumn
zxAnSipIsdnDLinkLinkId=_ZxAnSipIsdnDLinkLinkId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1,3),_ZxAnSipIsdnDLinkLinkId_Type())
zxAnSipIsdnDLinkLinkId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnDLinkLinkId.setStatus(_A)
class _ZxAnSipIsdnDLinkRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnSipIsdnDLinkRack_Type.__name__=_B
_ZxAnSipIsdnDLinkRack_Object=MibTableColumn
zxAnSipIsdnDLinkRack=_ZxAnSipIsdnDLinkRack_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1,4),_ZxAnSipIsdnDLinkRack_Type())
zxAnSipIsdnDLinkRack.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnDLinkRack.setStatus(_A)
class _ZxAnSipIsdnDLinkShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_ZxAnSipIsdnDLinkShelf_Type.__name__=_B
_ZxAnSipIsdnDLinkShelf_Object=MibTableColumn
zxAnSipIsdnDLinkShelf=_ZxAnSipIsdnDLinkShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1,5),_ZxAnSipIsdnDLinkShelf_Type())
zxAnSipIsdnDLinkShelf.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnDLinkShelf.setStatus(_A)
class _ZxAnSipIsdnDLinkSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_ZxAnSipIsdnDLinkSlot_Type.__name__=_B
_ZxAnSipIsdnDLinkSlot_Object=MibTableColumn
zxAnSipIsdnDLinkSlot=_ZxAnSipIsdnDLinkSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1,6),_ZxAnSipIsdnDLinkSlot_Type())
zxAnSipIsdnDLinkSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnDLinkSlot.setStatus(_A)
class _ZxAnSipIsdnDLinkIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxAnSipIsdnDLinkIndex_Type.__name__=_B
_ZxAnSipIsdnDLinkIndex_Object=MibTableColumn
zxAnSipIsdnDLinkIndex=_ZxAnSipIsdnDLinkIndex_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1,7),_ZxAnSipIsdnDLinkIndex_Type())
zxAnSipIsdnDLinkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnDLinkIndex.setStatus(_A)
class _ZxAnSipIsdnDLinkDChanTs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_ZxAnSipIsdnDLinkDChanTs_Type.__name__=_B
_ZxAnSipIsdnDLinkDChanTs_Object=MibTableColumn
zxAnSipIsdnDLinkDChanTs=_ZxAnSipIsdnDLinkDChanTs_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1,8),_ZxAnSipIsdnDLinkDChanTs_Type())
zxAnSipIsdnDLinkDChanTs.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnDLinkDChanTs.setStatus(_A)
class _ZxAnSipIsdnDLinkOperNum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxAnSipIsdnDLinkOperNum_Type.__name__=_B
_ZxAnSipIsdnDLinkOperNum_Object=MibTableColumn
zxAnSipIsdnDLinkOperNum=_ZxAnSipIsdnDLinkOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1,9),_ZxAnSipIsdnDLinkOperNum_Type())
zxAnSipIsdnDLinkOperNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnDLinkOperNum.setStatus(_A)
class _ZxAnSipIsdnDLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('link2BplusD',1),('link30BplusD',2),('link23BplusD',3)))
_ZxAnSipIsdnDLinkType_Type.__name__=_B
_ZxAnSipIsdnDLinkType_Object=MibTableColumn
zxAnSipIsdnDLinkType=_ZxAnSipIsdnDLinkType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1,10),_ZxAnSipIsdnDLinkType_Type())
zxAnSipIsdnDLinkType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipIsdnDLinkType.setStatus(_A)
_ZxAnSipIsdnDLinkRowStatus_Type=RowStatus
_ZxAnSipIsdnDLinkRowStatus_Object=MibTableColumn
zxAnSipIsdnDLinkRowStatus=_ZxAnSipIsdnDLinkRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,8,21,1,20),_ZxAnSipIsdnDLinkRowStatus_Type())
zxAnSipIsdnDLinkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnDLinkRowStatus.setStatus(_A)
_ZxAnSipIsdnUserTable_Object=MibTable
zxAnSipIsdnUserTable=_ZxAnSipIsdnUserTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22))
if mibBuilder.loadTexts:zxAnSipIsdnUserTable.setStatus(_A)
_ZxAnSipIsdnUserEntry_Object=MibTableRow
zxAnSipIsdnUserEntry=_ZxAnSipIsdnUserEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1))
zxAnSipIsdnUserEntry.setIndexNames((0,_F,_A0),(0,_F,_A1),(0,_F,_A2))
if mibBuilder.loadTexts:zxAnSipIsdnUserEntry.setStatus(_A)
class _ZxAnSipIsdnUserMgId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxAnSipIsdnUserMgId_Type.__name__=_B
_ZxAnSipIsdnUserMgId_Object=MibTableColumn
zxAnSipIsdnUserMgId=_ZxAnSipIsdnUserMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,1),_ZxAnSipIsdnUserMgId_Type())
zxAnSipIsdnUserMgId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnUserMgId.setStatus(_A)
class _ZxAnSipIsdnUserGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_ZxAnSipIsdnUserGroupId_Type.__name__=_B
_ZxAnSipIsdnUserGroupId_Object=MibTableColumn
zxAnSipIsdnUserGroupId=_ZxAnSipIsdnUserGroupId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,2),_ZxAnSipIsdnUserGroupId_Type())
zxAnSipIsdnUserGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnUserGroupId.setStatus(_A)
class _ZxAnSipIsdnUserSipPhoneNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnSipIsdnUserSipPhoneNumber_Type.__name__=_H
_ZxAnSipIsdnUserSipPhoneNumber_Object=MibTableColumn
zxAnSipIsdnUserSipPhoneNumber=_ZxAnSipIsdnUserSipPhoneNumber_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,3),_ZxAnSipIsdnUserSipPhoneNumber_Type())
zxAnSipIsdnUserSipPhoneNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnUserSipPhoneNumber.setStatus(_A)
class _ZxAnSipIsdnUserOperNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_ZxAnSipIsdnUserOperNum_Type.__name__=_B
_ZxAnSipIsdnUserOperNum_Object=MibTableColumn
zxAnSipIsdnUserOperNum=_ZxAnSipIsdnUserOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,4),_ZxAnSipIsdnUserOperNum_Type())
zxAnSipIsdnUserOperNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserOperNum.setStatus(_A)
class _ZxAnSipIsdnUserOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_a,2)))
_ZxAnSipIsdnUserOperType_Type.__name__=_B
_ZxAnSipIsdnUserOperType_Object=MibTableColumn
zxAnSipIsdnUserOperType=_ZxAnSipIsdnUserOperType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,5),_ZxAnSipIsdnUserOperType_Type())
zxAnSipIsdnUserOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserOperType.setStatus(_A)
class _ZxAnSipIsdnUserAuthUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxAnSipIsdnUserAuthUsername_Type.__name__=_H
_ZxAnSipIsdnUserAuthUsername_Object=MibTableColumn
zxAnSipIsdnUserAuthUsername=_ZxAnSipIsdnUserAuthUsername_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,6),_ZxAnSipIsdnUserAuthUsername_Type())
zxAnSipIsdnUserAuthUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserAuthUsername.setStatus(_A)
class _ZxAnSipIsdnUserAuthType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_Y,2),(_Z,3)))
_ZxAnSipIsdnUserAuthType_Type.__name__=_B
_ZxAnSipIsdnUserAuthType_Object=MibTableColumn
zxAnSipIsdnUserAuthType=_ZxAnSipIsdnUserAuthType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,7),_ZxAnSipIsdnUserAuthType_Type())
zxAnSipIsdnUserAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserAuthType.setStatus(_A)
class _ZxAnSipIsdnUserAuthStartNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnSipIsdnUserAuthStartNumber_Type.__name__=_B
_ZxAnSipIsdnUserAuthStartNumber_Object=MibTableColumn
zxAnSipIsdnUserAuthStartNumber=_ZxAnSipIsdnUserAuthStartNumber_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,8),_ZxAnSipIsdnUserAuthStartNumber_Type())
zxAnSipIsdnUserAuthStartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserAuthStartNumber.setStatus(_A)
class _ZxAnSipIsdnUserAuthDigitLen_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ZxAnSipIsdnUserAuthDigitLen_Type.__name__=_B
_ZxAnSipIsdnUserAuthDigitLen_Object=MibTableColumn
zxAnSipIsdnUserAuthDigitLen=_ZxAnSipIsdnUserAuthDigitLen_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,9),_ZxAnSipIsdnUserAuthDigitLen_Type())
zxAnSipIsdnUserAuthDigitLen.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserAuthDigitLen.setStatus(_A)
class _ZxAnSipIsdnUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ZxAnSipIsdnUserPassword_Type.__name__=_H
_ZxAnSipIsdnUserPassword_Object=MibTableColumn
zxAnSipIsdnUserPassword=_ZxAnSipIsdnUserPassword_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,10),_ZxAnSipIsdnUserPassword_Type())
zxAnSipIsdnUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserPassword.setStatus(_A)
class _ZxAnSipIsdnUserId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ZxAnSipIsdnUserId_Type.__name__=_H
_ZxAnSipIsdnUserId_Object=MibTableColumn
zxAnSipIsdnUserId=_ZxAnSipIsdnUserId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,11),_ZxAnSipIsdnUserId_Type())
zxAnSipIsdnUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserId.setStatus(_A)
class _ZxAnSipIsdnUserIdType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_Y,2),(_Z,3)))
_ZxAnSipIsdnUserIdType_Type.__name__=_B
_ZxAnSipIsdnUserIdType_Object=MibTableColumn
zxAnSipIsdnUserIdType=_ZxAnSipIsdnUserIdType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,12),_ZxAnSipIsdnUserIdType_Type())
zxAnSipIsdnUserIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserIdType.setStatus(_A)
class _ZxAnSipIsdnUserIdStartNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnSipIsdnUserIdStartNumber_Type.__name__=_B
_ZxAnSipIsdnUserIdStartNumber_Object=MibTableColumn
zxAnSipIsdnUserIdStartNumber=_ZxAnSipIsdnUserIdStartNumber_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,13),_ZxAnSipIsdnUserIdStartNumber_Type())
zxAnSipIsdnUserIdStartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserIdStartNumber.setStatus(_A)
class _ZxAnSipIsdnUserIdDigitLen_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_ZxAnSipIsdnUserIdDigitLen_Type.__name__=_B
_ZxAnSipIsdnUserIdDigitLen_Object=MibTableColumn
zxAnSipIsdnUserIdDigitLen=_ZxAnSipIsdnUserIdDigitLen_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,14),_ZxAnSipIsdnUserIdDigitLen_Type())
zxAnSipIsdnUserIdDigitLen.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserIdDigitLen.setStatus(_A)
_ZxAnSipIsdnUserRowStatus_Type=RowStatus
_ZxAnSipIsdnUserRowStatus_Object=MibTableColumn
zxAnSipIsdnUserRowStatus=_ZxAnSipIsdnUserRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,8,22,1,50),_ZxAnSipIsdnUserRowStatus_Type())
zxAnSipIsdnUserRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnUserRowStatus.setStatus(_A)
_ZxAnSipIsdnPhoneTable_Object=MibTable
zxAnSipIsdnPhoneTable=_ZxAnSipIsdnPhoneTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,23))
if mibBuilder.loadTexts:zxAnSipIsdnPhoneTable.setStatus(_A)
_ZxAnSipIsdnPhoneEntry_Object=MibTableRow
zxAnSipIsdnPhoneEntry=_ZxAnSipIsdnPhoneEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,23,1))
zxAnSipIsdnPhoneEntry.setIndexNames((0,_F,_A3),(0,_F,_A4))
if mibBuilder.loadTexts:zxAnSipIsdnPhoneEntry.setStatus(_A)
class _ZxAnSipIsdnPhoneSipPhone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZxAnSipIsdnPhoneSipPhone_Type.__name__=_H
_ZxAnSipIsdnPhoneSipPhone_Object=MibTableColumn
zxAnSipIsdnPhoneSipPhone=_ZxAnSipIsdnPhoneSipPhone_Object((1,3,6,1,4,1,3902,1015,5200,3,8,23,1,1),_ZxAnSipIsdnPhoneSipPhone_Type())
zxAnSipIsdnPhoneSipPhone.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnPhoneSipPhone.setStatus(_A)
class _ZxAnSipIsdnPhoneIsdnPhone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZxAnSipIsdnPhoneIsdnPhone_Type.__name__=_H
_ZxAnSipIsdnPhoneIsdnPhone_Object=MibTableColumn
zxAnSipIsdnPhoneIsdnPhone=_ZxAnSipIsdnPhoneIsdnPhone_Object((1,3,6,1,4,1,3902,1015,5200,3,8,23,1,2),_ZxAnSipIsdnPhoneIsdnPhone_Type())
zxAnSipIsdnPhoneIsdnPhone.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnPhoneIsdnPhone.setStatus(_A)
class _ZxAnSipIsdnPhoneOperNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000))
_ZxAnSipIsdnPhoneOperNum_Type.__name__=_B
_ZxAnSipIsdnPhoneOperNum_Object=MibTableColumn
zxAnSipIsdnPhoneOperNum=_ZxAnSipIsdnPhoneOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,8,23,1,3),_ZxAnSipIsdnPhoneOperNum_Type())
zxAnSipIsdnPhoneOperNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnPhoneOperNum.setStatus(_A)
_ZxAnSipIsdnPhoneRowStatus_Type=RowStatus
_ZxAnSipIsdnPhoneRowStatus_Object=MibTableColumn
zxAnSipIsdnPhoneRowStatus=_ZxAnSipIsdnPhoneRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,8,23,1,10),_ZxAnSipIsdnPhoneRowStatus_Type())
zxAnSipIsdnPhoneRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnSipIsdnPhoneRowStatus.setStatus(_A)
_ZxAnSipIsdnBChanTable_Object=MibTable
zxAnSipIsdnBChanTable=_ZxAnSipIsdnBChanTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,24))
if mibBuilder.loadTexts:zxAnSipIsdnBChanTable.setStatus(_A)
_ZxAnSipIsdnBChanEntry_Object=MibTableRow
zxAnSipIsdnBChanEntry=_ZxAnSipIsdnBChanEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,24,1))
zxAnSipIsdnBChanEntry.setIndexNames((0,_F,_A5),(0,_F,_A6),(0,_F,_A7),(0,_F,_A8),(0,_F,_A9))
if mibBuilder.loadTexts:zxAnSipIsdnBChanEntry.setStatus(_A)
class _ZxAnSipIsdnBChanRack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnSipIsdnBChanRack_Type.__name__=_B
_ZxAnSipIsdnBChanRack_Object=MibTableColumn
zxAnSipIsdnBChanRack=_ZxAnSipIsdnBChanRack_Object((1,3,6,1,4,1,3902,1015,5200,3,8,24,1,1),_ZxAnSipIsdnBChanRack_Type())
zxAnSipIsdnBChanRack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnBChanRack.setStatus(_A)
class _ZxAnSipIsdnBChanShelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_ZxAnSipIsdnBChanShelf_Type.__name__=_B
_ZxAnSipIsdnBChanShelf_Object=MibTableColumn
zxAnSipIsdnBChanShelf=_ZxAnSipIsdnBChanShelf_Object((1,3,6,1,4,1,3902,1015,5200,3,8,24,1,2),_ZxAnSipIsdnBChanShelf_Type())
zxAnSipIsdnBChanShelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnBChanShelf.setStatus(_A)
class _ZxAnSipIsdnBChanSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_ZxAnSipIsdnBChanSlot_Type.__name__=_B
_ZxAnSipIsdnBChanSlot_Object=MibTableColumn
zxAnSipIsdnBChanSlot=_ZxAnSipIsdnBChanSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,8,24,1,3),_ZxAnSipIsdnBChanSlot_Type())
zxAnSipIsdnBChanSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnBChanSlot.setStatus(_A)
class _ZxAnSipIsdnBChanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxAnSipIsdnBChanIndex_Type.__name__=_B
_ZxAnSipIsdnBChanIndex_Object=MibTableColumn
zxAnSipIsdnBChanIndex=_ZxAnSipIsdnBChanIndex_Object((1,3,6,1,4,1,3902,1015,5200,3,8,24,1,4),_ZxAnSipIsdnBChanIndex_Type())
zxAnSipIsdnBChanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnBChanIndex.setStatus(_A)
class _ZxAnSipIsdnBChanTimeSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_ZxAnSipIsdnBChanTimeSlot_Type.__name__=_B
_ZxAnSipIsdnBChanTimeSlot_Object=MibTableColumn
zxAnSipIsdnBChanTimeSlot=_ZxAnSipIsdnBChanTimeSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,8,24,1,5),_ZxAnSipIsdnBChanTimeSlot_Type())
zxAnSipIsdnBChanTimeSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipIsdnBChanTimeSlot.setStatus(_A)
class _ZxAnSipIsdnBChanGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_ZxAnSipIsdnBChanGroupId_Type.__name__=_B
_ZxAnSipIsdnBChanGroupId_Object=MibTableColumn
zxAnSipIsdnBChanGroupId=_ZxAnSipIsdnBChanGroupId_Object((1,3,6,1,4,1,3902,1015,5200,3,8,24,1,6),_ZxAnSipIsdnBChanGroupId_Type())
zxAnSipIsdnBChanGroupId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipIsdnBChanGroupId.setStatus(_A)
class _ZxAnSipIsdnBChanPbxBChan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_ZxAnSipIsdnBChanPbxBChan_Type.__name__=_B
_ZxAnSipIsdnBChanPbxBChan_Object=MibTableColumn
zxAnSipIsdnBChanPbxBChan=_ZxAnSipIsdnBChanPbxBChan_Object((1,3,6,1,4,1,3902,1015,5200,3,8,24,1,7),_ZxAnSipIsdnBChanPbxBChan_Type())
zxAnSipIsdnBChanPbxBChan.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipIsdnBChanPbxBChan.setStatus(_A)
class _ZxAnSipIsdnBChanOperNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_ZxAnSipIsdnBChanOperNum_Type.__name__=_B
_ZxAnSipIsdnBChanOperNum_Object=MibTableColumn
zxAnSipIsdnBChanOperNum=_ZxAnSipIsdnBChanOperNum_Object((1,3,6,1,4,1,3902,1015,5200,3,8,24,1,8),_ZxAnSipIsdnBChanOperNum_Type())
zxAnSipIsdnBChanOperNum.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipIsdnBChanOperNum.setStatus(_A)
_ZxAnSipCallPerfTable_ObjectIdentity=ObjectIdentity
zxAnSipCallPerfTable=_ZxAnSipCallPerfTable_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,8,50))
_ZxAnSipRegCurrentUsers_Type=Gauge32
_ZxAnSipRegCurrentUsers_Object=MibScalar
zxAnSipRegCurrentUsers=_ZxAnSipRegCurrentUsers_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,1),_ZxAnSipRegCurrentUsers_Type())
zxAnSipRegCurrentUsers.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipRegCurrentUsers.setStatus(_A)
_ZxAnSipSuccessContactRegs_Type=Counter32
_ZxAnSipSuccessContactRegs_Object=MibScalar
zxAnSipSuccessContactRegs=_ZxAnSipSuccessContactRegs_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,2),_ZxAnSipSuccessContactRegs_Type())
zxAnSipSuccessContactRegs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipSuccessContactRegs.setStatus(_A)
_ZxAnSipFailedContactRegs_Type=Counter32
_ZxAnSipFailedContactRegs_Object=MibScalar
zxAnSipFailedContactRegs=_ZxAnSipFailedContactRegs_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,3),_ZxAnSipFailedContactRegs_Type())
zxAnSipFailedContactRegs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipFailedContactRegs.setStatus(_A)
_ZxAnSipSuccessIncomingCalls_Type=Counter32
_ZxAnSipSuccessIncomingCalls_Object=MibScalar
zxAnSipSuccessIncomingCalls=_ZxAnSipSuccessIncomingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,4),_ZxAnSipSuccessIncomingCalls_Type())
zxAnSipSuccessIncomingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipSuccessIncomingCalls.setStatus(_A)
_ZxAnSipFailedIncomingCalls_Type=Counter32
_ZxAnSipFailedIncomingCalls_Object=MibScalar
zxAnSipFailedIncomingCalls=_ZxAnSipFailedIncomingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,5),_ZxAnSipFailedIncomingCalls_Type())
zxAnSipFailedIncomingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipFailedIncomingCalls.setStatus(_A)
_ZxAnSipSuccessOutgoingCalls_Type=Counter32
_ZxAnSipSuccessOutgoingCalls_Object=MibScalar
zxAnSipSuccessOutgoingCalls=_ZxAnSipSuccessOutgoingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,6),_ZxAnSipSuccessOutgoingCalls_Type())
zxAnSipSuccessOutgoingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipSuccessOutgoingCalls.setStatus(_A)
_ZxAnSipFailedOutgoingCalls_Type=Counter32
_ZxAnSipFailedOutgoingCalls_Object=MibScalar
zxAnSipFailedOutgoingCalls=_ZxAnSipFailedOutgoingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,7),_ZxAnSipFailedOutgoingCalls_Type())
zxAnSipFailedOutgoingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipFailedOutgoingCalls.setStatus(_A)
_ZxAnSipPrev15MinSuccessContactRegs_Type=Counter32
_ZxAnSipPrev15MinSuccessContactRegs_Object=MibScalar
zxAnSipPrev15MinSuccessContactRegs=_ZxAnSipPrev15MinSuccessContactRegs_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,8),_ZxAnSipPrev15MinSuccessContactRegs_Type())
zxAnSipPrev15MinSuccessContactRegs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipPrev15MinSuccessContactRegs.setStatus(_A)
_ZxAnSipPrev15MinFailedContactRegs_Type=Counter32
_ZxAnSipPrev15MinFailedContactRegs_Object=MibScalar
zxAnSipPrev15MinFailedContactRegs=_ZxAnSipPrev15MinFailedContactRegs_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,9),_ZxAnSipPrev15MinFailedContactRegs_Type())
zxAnSipPrev15MinFailedContactRegs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipPrev15MinFailedContactRegs.setStatus(_A)
_ZxAnSipPrev15MinSuccessIncomingCalls_Type=Counter32
_ZxAnSipPrev15MinSuccessIncomingCalls_Object=MibScalar
zxAnSipPrev15MinSuccessIncomingCalls=_ZxAnSipPrev15MinSuccessIncomingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,10),_ZxAnSipPrev15MinSuccessIncomingCalls_Type())
zxAnSipPrev15MinSuccessIncomingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipPrev15MinSuccessIncomingCalls.setStatus(_A)
_ZxAnSipPrev15MinFailedIncomingCalls_Type=Counter32
_ZxAnSipPrev15MinFailedIncomingCalls_Object=MibScalar
zxAnSipPrev15MinFailedIncomingCalls=_ZxAnSipPrev15MinFailedIncomingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,11),_ZxAnSipPrev15MinFailedIncomingCalls_Type())
zxAnSipPrev15MinFailedIncomingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipPrev15MinFailedIncomingCalls.setStatus(_A)
_ZxAnSipPrev15MinSuccessOutgoingCalls_Type=Counter32
_ZxAnSipPrev15MinSuccessOutgoingCalls_Object=MibScalar
zxAnSipPrev15MinSuccessOutgoingCalls=_ZxAnSipPrev15MinSuccessOutgoingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,12),_ZxAnSipPrev15MinSuccessOutgoingCalls_Type())
zxAnSipPrev15MinSuccessOutgoingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipPrev15MinSuccessOutgoingCalls.setStatus(_A)
_ZxAnSipPrev15MinFailedOutgoingCalls_Type=Counter32
_ZxAnSipPrev15MinFailedOutgoingCalls_Object=MibScalar
zxAnSipPrev15MinFailedOutgoingCalls=_ZxAnSipPrev15MinFailedOutgoingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,13),_ZxAnSipPrev15MinFailedOutgoingCalls_Type())
zxAnSipPrev15MinFailedOutgoingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipPrev15MinFailedOutgoingCalls.setStatus(_A)
_ZxAnSipActiveIncomingCalls_Type=Counter32
_ZxAnSipActiveIncomingCalls_Object=MibScalar
zxAnSipActiveIncomingCalls=_ZxAnSipActiveIncomingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,14),_ZxAnSipActiveIncomingCalls_Type())
zxAnSipActiveIncomingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipActiveIncomingCalls.setStatus(_A)
_ZxAnSipActiveOutgoingCalls_Type=Counter32
_ZxAnSipActiveOutgoingCalls_Object=MibScalar
zxAnSipActiveOutgoingCalls=_ZxAnSipActiveOutgoingCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,15),_ZxAnSipActiveOutgoingCalls_Type())
zxAnSipActiveOutgoingCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipActiveOutgoingCalls.setStatus(_A)
_ZxAnSipOutgoingCallTraffic_Type=Integer32
_ZxAnSipOutgoingCallTraffic_Object=MibScalar
zxAnSipOutgoingCallTraffic=_ZxAnSipOutgoingCallTraffic_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,16),_ZxAnSipOutgoingCallTraffic_Type())
zxAnSipOutgoingCallTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipOutgoingCallTraffic.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipOutgoingCallTraffic.setUnits(_V)
_ZxAnSipIncomingCallTraffic_Type=Integer32
_ZxAnSipIncomingCallTraffic_Object=MibScalar
zxAnSipIncomingCallTraffic=_ZxAnSipIncomingCallTraffic_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,17),_ZxAnSipIncomingCallTraffic_Type())
zxAnSipIncomingCallTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipIncomingCallTraffic.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipIncomingCallTraffic.setUnits(_V)
_ZxAnSipTotalCallTraffic_Type=Integer32
_ZxAnSipTotalCallTraffic_Object=MibScalar
zxAnSipTotalCallTraffic=_ZxAnSipTotalCallTraffic_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,18),_ZxAnSipTotalCallTraffic_Type())
zxAnSipTotalCallTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipTotalCallTraffic.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipTotalCallTraffic.setUnits(_V)
_ZxAnSipOutgoingCallKeepingTime_Type=Counter32
_ZxAnSipOutgoingCallKeepingTime_Object=MibScalar
zxAnSipOutgoingCallKeepingTime=_ZxAnSipOutgoingCallKeepingTime_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,19),_ZxAnSipOutgoingCallKeepingTime_Type())
zxAnSipOutgoingCallKeepingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipOutgoingCallKeepingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipOutgoingCallKeepingTime.setUnits(_O)
_ZxAnSipIncomingCallKeepingTime_Type=Counter32
_ZxAnSipIncomingCallKeepingTime_Object=MibScalar
zxAnSipIncomingCallKeepingTime=_ZxAnSipIncomingCallKeepingTime_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,20),_ZxAnSipIncomingCallKeepingTime_Type())
zxAnSipIncomingCallKeepingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipIncomingCallKeepingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipIncomingCallKeepingTime.setUnits(_O)
_ZxAnSipTotalCallKeepingTime_Type=Counter32
_ZxAnSipTotalCallKeepingTime_Object=MibScalar
zxAnSipTotalCallKeepingTime=_ZxAnSipTotalCallKeepingTime_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,21),_ZxAnSipTotalCallKeepingTime_Type())
zxAnSipTotalCallKeepingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipTotalCallKeepingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipTotalCallKeepingTime.setUnits(_O)
_ZxAnSipOutgoingCallAttempts_Type=Counter32
_ZxAnSipOutgoingCallAttempts_Object=MibScalar
zxAnSipOutgoingCallAttempts=_ZxAnSipOutgoingCallAttempts_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,22),_ZxAnSipOutgoingCallAttempts_Type())
zxAnSipOutgoingCallAttempts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipOutgoingCallAttempts.setStatus(_A)
_ZxAnSipOutgoingCallCompletions_Type=Counter32
_ZxAnSipOutgoingCallCompletions_Object=MibScalar
zxAnSipOutgoingCallCompletions=_ZxAnSipOutgoingCallCompletions_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,23),_ZxAnSipOutgoingCallCompletions_Type())
zxAnSipOutgoingCallCompletions.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipOutgoingCallCompletions.setStatus(_A)
_ZxAnSipOutgoingCallLosses_Type=Counter32
_ZxAnSipOutgoingCallLosses_Object=MibScalar
zxAnSipOutgoingCallLosses=_ZxAnSipOutgoingCallLosses_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,24),_ZxAnSipOutgoingCallLosses_Type())
zxAnSipOutgoingCallLosses.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipOutgoingCallLosses.setStatus(_A)
_ZxAnSipIncomingCallAttempts_Type=Counter32
_ZxAnSipIncomingCallAttempts_Object=MibScalar
zxAnSipIncomingCallAttempts=_ZxAnSipIncomingCallAttempts_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,25),_ZxAnSipIncomingCallAttempts_Type())
zxAnSipIncomingCallAttempts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipIncomingCallAttempts.setStatus(_A)
_ZxAnSipIncomingCallCompletions_Type=Counter32
_ZxAnSipIncomingCallCompletions_Object=MibScalar
zxAnSipIncomingCallCompletions=_ZxAnSipIncomingCallCompletions_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,26),_ZxAnSipIncomingCallCompletions_Type())
zxAnSipIncomingCallCompletions.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipIncomingCallCompletions.setStatus(_A)
_ZxAnSipIncomingCallLosses_Type=Counter32
_ZxAnSipIncomingCallLosses_Object=MibScalar
zxAnSipIncomingCallLosses=_ZxAnSipIncomingCallLosses_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,27),_ZxAnSipIncomingCallLosses_Type())
zxAnSipIncomingCallLosses.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipIncomingCallLosses.setStatus(_A)
class _ZxAnSipOutgoingCallCompleteRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnSipOutgoingCallCompleteRatio_Type.__name__=_B
_ZxAnSipOutgoingCallCompleteRatio_Object=MibScalar
zxAnSipOutgoingCallCompleteRatio=_ZxAnSipOutgoingCallCompleteRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,28),_ZxAnSipOutgoingCallCompleteRatio_Type())
zxAnSipOutgoingCallCompleteRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipOutgoingCallCompleteRatio.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipOutgoingCallCompleteRatio.setUnits(_P)
class _ZxAnSipIncomingCallCompleteRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnSipIncomingCallCompleteRatio_Type.__name__=_B
_ZxAnSipIncomingCallCompleteRatio_Object=MibScalar
zxAnSipIncomingCallCompleteRatio=_ZxAnSipIncomingCallCompleteRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,29),_ZxAnSipIncomingCallCompleteRatio_Type())
zxAnSipIncomingCallCompleteRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipIncomingCallCompleteRatio.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipIncomingCallCompleteRatio.setUnits(_P)
class _ZxAnSipTotalCallCompleteRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnSipTotalCallCompleteRatio_Type.__name__=_B
_ZxAnSipTotalCallCompleteRatio_Object=MibScalar
zxAnSipTotalCallCompleteRatio=_ZxAnSipTotalCallCompleteRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,30),_ZxAnSipTotalCallCompleteRatio_Type())
zxAnSipTotalCallCompleteRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipTotalCallCompleteRatio.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipTotalCallCompleteRatio.setUnits(_P)
class _ZxAnSipTotalCallLossRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnSipTotalCallLossRatio_Type.__name__=_B
_ZxAnSipTotalCallLossRatio_Object=MibScalar
zxAnSipTotalCallLossRatio=_ZxAnSipTotalCallLossRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,8,50,31),_ZxAnSipTotalCallLossRatio_Type())
zxAnSipTotalCallLossRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipTotalCallLossRatio.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipTotalCallLossRatio.setUnits(_P)
_ZxAnSipHisPerfObjects_ObjectIdentity=ObjectIdentity
zxAnSipHisPerfObjects=_ZxAnSipHisPerfObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,8,51))
_ZxAnSipHisPerfGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnSipHisPerfGlobalObjects=_ZxAnSipHisPerfGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,8,51,1))
class _ZxAnSipHisPerfIntervalType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('oneHour',2)))
_ZxAnSipHisPerfIntervalType_Type.__name__=_B
_ZxAnSipHisPerfIntervalType_Object=MibScalar
zxAnSipHisPerfIntervalType=_ZxAnSipHisPerfIntervalType_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,1,1),_ZxAnSipHisPerfIntervalType_Type())
zxAnSipHisPerfIntervalType.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnSipHisPerfIntervalType.setStatus(_A)
_ZxAnSipHisPerfIntervalTable_Object=MibTable
zxAnSipHisPerfIntervalTable=_ZxAnSipHisPerfIntervalTable_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2))
if mibBuilder.loadTexts:zxAnSipHisPerfIntervalTable.setStatus(_A)
_ZxAnSipHisPerfIntervalEntry_Object=MibTableRow
zxAnSipHisPerfIntervalEntry=_ZxAnSipHisPerfIntervalEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1))
zxAnSipHisPerfIntervalEntry.setIndexNames((0,_F,_AA))
if mibBuilder.loadTexts:zxAnSipHisPerfIntervalEntry.setStatus(_A)
class _ZxAnSipHisPerfIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ZxAnSipHisPerfIntervalNumber_Type.__name__=_B
_ZxAnSipHisPerfIntervalNumber_Object=MibTableColumn
zxAnSipHisPerfIntervalNumber=_ZxAnSipHisPerfIntervalNumber_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,1),_ZxAnSipHisPerfIntervalNumber_Type())
zxAnSipHisPerfIntervalNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnSipHisPerfIntervalNumber.setStatus(_A)
_ZxAnSipHisValidData_Type=TruthValue
_ZxAnSipHisValidData_Object=MibTableColumn
zxAnSipHisValidData=_ZxAnSipHisValidData_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,2),_ZxAnSipHisValidData_Type())
zxAnSipHisValidData.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisValidData.setStatus(_A)
_ZxAnSipHisSuccessContactRegs_Type=Counter32
_ZxAnSipHisSuccessContactRegs_Object=MibTableColumn
zxAnSipHisSuccessContactRegs=_ZxAnSipHisSuccessContactRegs_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,3),_ZxAnSipHisSuccessContactRegs_Type())
zxAnSipHisSuccessContactRegs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisSuccessContactRegs.setStatus(_A)
_ZxAnSipHisFailedContactRegs_Type=Counter32
_ZxAnSipHisFailedContactRegs_Object=MibTableColumn
zxAnSipHisFailedContactRegs=_ZxAnSipHisFailedContactRegs_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,4),_ZxAnSipHisFailedContactRegs_Type())
zxAnSipHisFailedContactRegs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisFailedContactRegs.setStatus(_A)
_ZxAnSipHisSuccessInCalls_Type=Counter32
_ZxAnSipHisSuccessInCalls_Object=MibTableColumn
zxAnSipHisSuccessInCalls=_ZxAnSipHisSuccessInCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,5),_ZxAnSipHisSuccessInCalls_Type())
zxAnSipHisSuccessInCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisSuccessInCalls.setStatus(_A)
_ZxAnSipHisFailedInCalls_Type=Counter32
_ZxAnSipHisFailedInCalls_Object=MibTableColumn
zxAnSipHisFailedInCalls=_ZxAnSipHisFailedInCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,6),_ZxAnSipHisFailedInCalls_Type())
zxAnSipHisFailedInCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisFailedInCalls.setStatus(_A)
_ZxAnSipHisSuccessOutCalls_Type=Counter32
_ZxAnSipHisSuccessOutCalls_Object=MibTableColumn
zxAnSipHisSuccessOutCalls=_ZxAnSipHisSuccessOutCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,7),_ZxAnSipHisSuccessOutCalls_Type())
zxAnSipHisSuccessOutCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisSuccessOutCalls.setStatus(_A)
_ZxAnSipHisFailedOutCalls_Type=Counter32
_ZxAnSipHisFailedOutCalls_Object=MibTableColumn
zxAnSipHisFailedOutCalls=_ZxAnSipHisFailedOutCalls_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,8),_ZxAnSipHisFailedOutCalls_Type())
zxAnSipHisFailedOutCalls.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisFailedOutCalls.setStatus(_A)
_ZxAnSipHisOutCallTraffic_Type=Integer32
_ZxAnSipHisOutCallTraffic_Object=MibTableColumn
zxAnSipHisOutCallTraffic=_ZxAnSipHisOutCallTraffic_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,9),_ZxAnSipHisOutCallTraffic_Type())
zxAnSipHisOutCallTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisOutCallTraffic.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipHisOutCallTraffic.setUnits(_V)
_ZxAnSipHisInCallTraffic_Type=Integer32
_ZxAnSipHisInCallTraffic_Object=MibTableColumn
zxAnSipHisInCallTraffic=_ZxAnSipHisInCallTraffic_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,10),_ZxAnSipHisInCallTraffic_Type())
zxAnSipHisInCallTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisInCallTraffic.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipHisInCallTraffic.setUnits(_V)
_ZxAnSipHisTotalCallTraffic_Type=Integer32
_ZxAnSipHisTotalCallTraffic_Object=MibTableColumn
zxAnSipHisTotalCallTraffic=_ZxAnSipHisTotalCallTraffic_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,11),_ZxAnSipHisTotalCallTraffic_Type())
zxAnSipHisTotalCallTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisTotalCallTraffic.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipHisTotalCallTraffic.setUnits(_V)
_ZxAnSipHisOutCallKeepTime_Type=Counter32
_ZxAnSipHisOutCallKeepTime_Object=MibTableColumn
zxAnSipHisOutCallKeepTime=_ZxAnSipHisOutCallKeepTime_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,12),_ZxAnSipHisOutCallKeepTime_Type())
zxAnSipHisOutCallKeepTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisOutCallKeepTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipHisOutCallKeepTime.setUnits(_O)
_ZxAnSipHisInCallKeepTime_Type=Counter32
_ZxAnSipHisInCallKeepTime_Object=MibTableColumn
zxAnSipHisInCallKeepTime=_ZxAnSipHisInCallKeepTime_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,13),_ZxAnSipHisInCallKeepTime_Type())
zxAnSipHisInCallKeepTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisInCallKeepTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipHisInCallKeepTime.setUnits(_O)
_ZxAnSipHisTotalCallKeepTime_Type=Counter32
_ZxAnSipHisTotalCallKeepTime_Object=MibTableColumn
zxAnSipHisTotalCallKeepTime=_ZxAnSipHisTotalCallKeepTime_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,14),_ZxAnSipHisTotalCallKeepTime_Type())
zxAnSipHisTotalCallKeepTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisTotalCallKeepTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipHisTotalCallKeepTime.setUnits(_O)
_ZxAnSipHisOutCallAttempts_Type=Counter32
_ZxAnSipHisOutCallAttempts_Object=MibTableColumn
zxAnSipHisOutCallAttempts=_ZxAnSipHisOutCallAttempts_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,15),_ZxAnSipHisOutCallAttempts_Type())
zxAnSipHisOutCallAttempts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisOutCallAttempts.setStatus(_A)
_ZxAnSipHisOutCallCompletions_Type=Counter32
_ZxAnSipHisOutCallCompletions_Object=MibTableColumn
zxAnSipHisOutCallCompletions=_ZxAnSipHisOutCallCompletions_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,16),_ZxAnSipHisOutCallCompletions_Type())
zxAnSipHisOutCallCompletions.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisOutCallCompletions.setStatus(_A)
_ZxAnSipHisOutCallLosses_Type=Counter32
_ZxAnSipHisOutCallLosses_Object=MibTableColumn
zxAnSipHisOutCallLosses=_ZxAnSipHisOutCallLosses_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,17),_ZxAnSipHisOutCallLosses_Type())
zxAnSipHisOutCallLosses.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisOutCallLosses.setStatus(_A)
_ZxAnSipHisInCallAttempts_Type=Counter32
_ZxAnSipHisInCallAttempts_Object=MibTableColumn
zxAnSipHisInCallAttempts=_ZxAnSipHisInCallAttempts_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,18),_ZxAnSipHisInCallAttempts_Type())
zxAnSipHisInCallAttempts.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisInCallAttempts.setStatus(_A)
_ZxAnSipHisInCallCompletions_Type=Counter32
_ZxAnSipHisInCallCompletions_Object=MibTableColumn
zxAnSipHisInCallCompletions=_ZxAnSipHisInCallCompletions_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,19),_ZxAnSipHisInCallCompletions_Type())
zxAnSipHisInCallCompletions.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisInCallCompletions.setStatus(_A)
_ZxAnSipHisInCallLosses_Type=Counter32
_ZxAnSipHisInCallLosses_Object=MibTableColumn
zxAnSipHisInCallLosses=_ZxAnSipHisInCallLosses_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,20),_ZxAnSipHisInCallLosses_Type())
zxAnSipHisInCallLosses.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisInCallLosses.setStatus(_A)
class _ZxAnSipHisOutCallCompleteRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnSipHisOutCallCompleteRatio_Type.__name__=_B
_ZxAnSipHisOutCallCompleteRatio_Object=MibTableColumn
zxAnSipHisOutCallCompleteRatio=_ZxAnSipHisOutCallCompleteRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,21),_ZxAnSipHisOutCallCompleteRatio_Type())
zxAnSipHisOutCallCompleteRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisOutCallCompleteRatio.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipHisOutCallCompleteRatio.setUnits(_P)
class _ZxAnSipHisInCallCompleteRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnSipHisInCallCompleteRatio_Type.__name__=_B
_ZxAnSipHisInCallCompleteRatio_Object=MibTableColumn
zxAnSipHisInCallCompleteRatio=_ZxAnSipHisInCallCompleteRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,22),_ZxAnSipHisInCallCompleteRatio_Type())
zxAnSipHisInCallCompleteRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisInCallCompleteRatio.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipHisInCallCompleteRatio.setUnits(_P)
class _ZxAnSipHisTotalCallCompleteRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnSipHisTotalCallCompleteRatio_Type.__name__=_B
_ZxAnSipHisTotalCallCompleteRatio_Object=MibTableColumn
zxAnSipHisTotalCallCompleteRatio=_ZxAnSipHisTotalCallCompleteRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,23),_ZxAnSipHisTotalCallCompleteRatio_Type())
zxAnSipHisTotalCallCompleteRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisTotalCallCompleteRatio.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipHisTotalCallCompleteRatio.setUnits(_P)
class _ZxAnSipHisTotalCallLossRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnSipHisTotalCallLossRatio_Type.__name__=_B
_ZxAnSipHisTotalCallLossRatio_Object=MibTableColumn
zxAnSipHisTotalCallLossRatio=_ZxAnSipHisTotalCallLossRatio_Object((1,3,6,1,4,1,3902,1015,5200,3,8,51,2,1,24),_ZxAnSipHisTotalCallLossRatio_Type())
zxAnSipHisTotalCallLossRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipHisTotalCallLossRatio.setStatus(_A)
if mibBuilder.loadTexts:zxAnSipHisTotalCallLossRatio.setUnits(_P)
_ZxAnSipTrap_ObjectIdentity=ObjectIdentity
zxAnSipTrap=_ZxAnSipTrap_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,100))
_ZxAnSipTrapObjects_ObjectIdentity=ObjectIdentity
zxAnSipTrapObjects=_ZxAnSipTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,100,1))
_ZxAnSipTrapBindVar_ObjectIdentity=ObjectIdentity
zxAnSipTrapBindVar=_ZxAnSipTrapBindVar_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,100,2))
_ZxAnSipTrapReason_Type=Integer32
_ZxAnSipTrapReason_Object=MibScalar
zxAnSipTrapReason=_ZxAnSipTrapReason_Object((1,3,6,1,4,1,3902,1015,5200,3,100,2,1),_ZxAnSipTrapReason_Type())
zxAnSipTrapReason.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipTrapReason.setStatus(_A)
_ZxAnSipTrapMgcNo_Type=Integer32
_ZxAnSipTrapMgcNo_Object=MibScalar
zxAnSipTrapMgcNo=_ZxAnSipTrapMgcNo_Object((1,3,6,1,4,1,3902,1015,5200,3,100,2,2),_ZxAnSipTrapMgcNo_Type())
zxAnSipTrapMgcNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnSipTrapMgcNo.setStatus(_A)
zxAnSipLinkDown=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,100,1,1))
zxAnSipLinkDown.setObjects(*((_F,_b),(_F,_c)))
if mibBuilder.loadTexts:zxAnSipLinkDown.setStatus(_A)
zxAnSipLinkUp=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,100,1,2))
zxAnSipLinkUp.setObjects(*((_F,_b),(_F,_c)))
if mibBuilder.loadTexts:zxAnSipLinkUp.setStatus(_A)
zxAnSipUserRegisterFailedAlm=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,100,1,3))
zxAnSipUserRegisterFailedAlm.setObjects(*((_F,_d),(_F,_e)))
if mibBuilder.loadTexts:zxAnSipUserRegisterFailedAlm.setStatus(_A)
zxAnSipUserRegisterFailedClr=NotificationType((1,3,6,1,4,1,3902,1015,5200,3,100,1,4))
zxAnSipUserRegisterFailedClr.setObjects(*((_F,_d),(_F,_e)))
if mibBuilder.loadTexts:zxAnSipUserRegisterFailedClr.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zte':zte,'zxAn':zxAn,'zxAnSipMib':zxAnSipMib,'zxAnVoiceMgmt':zxAnVoiceMgmt,'zxAnSipConfig':zxAnSipConfig,'zxMsagSipUserTable':zxMsagSipUserTable,'zxMsagSipUserEntry':zxMsagSipUserEntry,_f:zxMsagSipUserRack,_g:zxMsagSipUserShelf,_h:zxMsagSipUserSlot,_i:zxMsagSipUserIndex,'zxMsagSipUserOperNum':zxMsagSipUserOperNum,'zxMsagSipUserSipDigit':zxMsagSipUserSipDigit,_d:zxMsagSipUserAuthusername,_e:zxMsagSipUserId,'zxMsagSipUserType':zxMsagSipUserType,'zxMsagSipUserBeginNo':zxMsagSipUserBeginNo,'zxMsagSipUserDigitLen':zxMsagSipUserDigitLen,'zxMsagSipUserPassword':zxMsagSipUserPassword,'zxMsagSipUserDstngRing':zxMsagSipUserDstngRing,'zxMsagSipUserHotlineType':zxMsagSipUserHotlineType,'zxMsagSipUserHotlineNum':zxMsagSipUserHotlineNum,'zxMsagSipUserDigitMap':zxMsagSipUserDigitMap,'zxMsagSipUserOperType':zxMsagSipUserOperType,'zxMsagSipUserGroupId':zxMsagSipUserGroupId,'zxMsagSipUserAdminStatus':zxMsagSipUserAdminStatus,'zxMsagSipUserSessionLimit':zxMsagSipUserSessionLimit,'zxMsagSipUserRegisterStatus':zxMsagSipUserRegisterStatus,'zxMsagSipUserRowStatus':zxMsagSipUserRowStatus,'zxMsagSipAccessCodeTable':zxMsagSipAccessCodeTable,'zxMsagSipAccessCodeEntry':zxMsagSipAccessCodeEntry,_k:zxMsagSipAccessCodeMgId,_l:zxMsagSipAccessCodeId,'zxMsagSipAccessCodecode':zxMsagSipAccessCodecode,'zxMsagSipAccessCodeRowStatus':zxMsagSipAccessCodeRowStatus,'zxMsagSipServiceCodeTable':zxMsagSipServiceCodeTable,'zxMsagSipServiceCodeEntry':zxMsagSipServiceCodeEntry,_m:zxMsagSipServiceCodeMgId,_n:zxMsagSipServiceCodeType,'zxMsagSipServiceCode':zxMsagSipServiceCode,'zxMsagSipServiceCodeRowStatus':zxMsagSipServiceCodeRowStatus,'zxMsagSipGenFmtTable':zxMsagSipGenFmtTable,'zxMsagSipGenFmtEntry':zxMsagSipGenFmtEntry,_o:zxMsagSipGenFmtMgId,_p:zxMsagSipGenFmtField,'zxMsagSipGenFmtValue':zxMsagSipGenFmtValue,'zxMsagSipCapTable':zxMsagSipCapTable,'zxMsagSipCapEntry':zxMsagSipCapEntry,_q:zxMsagSipCapMgId,'zxMsagSipCapSpPrecondition':zxMsagSipCapSpPrecondition,'zxMsagSipCapNeedReserveRes':zxMsagSipCapNeedReserveRes,'zxMsagSipCapSpEarlySession':zxMsagSipCapSpEarlySession,'zxMsagSipCapSp100Rel':zxMsagSipCapSp100Rel,'zxMsagSipCapSpPath':zxMsagSipCapSpPath,'zxMsagSipCapSpReplaces':zxMsagSipCapSpReplaces,'zxMsagSipCapSpTimer':zxMsagSipCapSpTimer,'zxMsagSipCapAudioCodePri1':zxMsagSipCapAudioCodePri1,'zxMsagSipCapAudioCodePri2':zxMsagSipCapAudioCodePri2,'zxMsagSipCapAudioCodePri3':zxMsagSipCapAudioCodePri3,'zxMsagSipCapAudioCodePri4':zxMsagSipCapAudioCodePri4,'zxMsagSipCapAudioCodePri5':zxMsagSipCapAudioCodePri5,'zxMsagSipCapAudioCodePri6':zxMsagSipCapAudioCodePri6,'zxMsagSipCapAudioCodePri7':zxMsagSipCapAudioCodePri7,'zxMsagSipCapDtmfRelayPri1':zxMsagSipCapDtmfRelayPri1,'zxMsagSipCapDtmfRelayPri2':zxMsagSipCapDtmfRelayPri2,'zxMsagSipCapFaxPri1':zxMsagSipCapFaxPri1,'zxMsagSipCapFaxPri2':zxMsagSipCapFaxPri2,'zxMsagSipCapSpFaxModem':zxMsagSipCapSpFaxModem,'zxMsagSipCapSessionMaxExpire':zxMsagSipCapSessionMaxExpire,'zxMsagSipCapSessionMinExpire':zxMsagSipCapSessionMinExpire,'zxMsagSipCapSessionRefresher':zxMsagSipCapSessionRefresher,'zxMsagSipCapDisplayFrom':zxMsagSipCapDisplayFrom,'zxMsagSipCapRegisterExpire':zxMsagSipCapRegisterExpire,'zxMsagSipCapReqMsgAuth':zxMsagSipCapReqMsgAuth,'zxMsagSipCapPPreService':zxMsagSipCapPPreService,'zxMsagSipCapAuthWithDomain':zxMsagSipCapAuthWithDomain,'zxMsagSipCapPackageInterval':zxMsagSipCapPackageInterval,'zxMsagSipCapSessionLimit':zxMsagSipCapSessionLimit,'zxMsagSipCapUserParam':zxMsagSipCapUserParam,'zxMsagSipCapDtmfSendingType':zxMsagSipCapDtmfSendingType,'zxMsagSipCapEarlyMedia':zxMsagSipCapEarlyMedia,'zxMsagSipCapEchoCancel':zxMsagSipCapEchoCancel,'zxMsagSipCapHistoryInfo':zxMsagSipCapHistoryInfo,'zxMsagSipCapThreePartySvrCode':zxMsagSipCapThreePartySvrCode,'zxMsagSipCapUserRegisterType':zxMsagSipCapUserRegisterType,'zxMsagSipCapHeartbeatEnable':zxMsagSipCapHeartbeatEnable,'zxMsagSipCapHeartbeatInterval':zxMsagSipCapHeartbeatInterval,'zxMsagSipCapSelfswitch':zxMsagSipCapSelfswitch,'zxMsagSipCapCallProtection':zxMsagSipCapCallProtection,'zxAnSipCapVideoMediaNegotiation':zxAnSipCapVideoMediaNegotiation,'zxAnSipCapUserPhoneAppendEnable':zxAnSipCapUserPhoneAppendEnable,'zxAnSipCapSendSubscribeMsgEnable':zxAnSipCapSendSubscribeMsgEnable,'zxAnSipCapFaxCodePri1':zxAnSipCapFaxCodePri1,'zxAnSipCapFaxCodePri2':zxAnSipCapFaxCodePri2,'zxAnSipCapFaxCodePri3':zxAnSipCapFaxCodePri3,'zxAnSipCapFaxCodePri4':zxAnSipCapFaxCodePri4,'zxAnSipCapFaxPacketInterval':zxAnSipCapFaxPacketInterval,'zxAnSipCapAutoRefreshEnable':zxAnSipCapAutoRefreshEnable,'zxAnSipCapImsHotlineValidTime':zxAnSipCapImsHotlineValidTime,'zxAnSipCapDnsRequestInterval':zxAnSipCapDnsRequestInterval,'zxAnSipCapCallWaitInvite18xRsp':zxAnSipCapCallWaitInvite18xRsp,'zxAnSipCapSubscribeUaProfileEn':zxAnSipCapSubscribeUaProfileEn,'zxAnSipCapSubscribeMsgSummaryEn':zxAnSipCapSubscribeMsgSummaryEn,'zxAnSipCapCallerControlEnable':zxAnSipCapCallerControlEnable,'zxAnSipCapNoDialSendInviteEnable':zxAnSipCapNoDialSendInviteEnable,'zxAnSipCapProxySvrAutoDrEnable':zxAnSipCapProxySvrAutoDrEnable,'zxAnSipCapProxySvrDrMode':zxAnSipCapProxySvrDrMode,'zxAnSipGlobalObjects':zxAnSipGlobalObjects,'zxAnSipMgmtCapabilities':zxAnSipMgmtCapabilities,'zxAnSipProcessReboot':zxAnSipProcessReboot,'zxAnSipProxyServerTable':zxAnSipProxyServerTable,'zxAnSipProxyServerEntry':zxAnSipProxyServerEntry,_t:zxAnSipProxySvrId,'zxAnSipProxySvrIp':zxAnSipProxySvrIp,'zxAnSipProxySvrPort':zxAnSipProxySvrPort,'zxAnSipProxySvrNamingType':zxAnSipProxySvrNamingType,'zxAnSipProxySvrDomainName':zxAnSipProxySvrDomainName,'zxAnSipProxySvrRowStatus':zxAnSipProxySvrRowStatus,'zxAnSipUserAgentTable':zxAnSipUserAgentTable,'zxAnSipUserAgentEntry':zxAnSipUserAgentEntry,_u:zxAnSipUaId,'zxAnSipUaPort':zxAnSipUaPort,'zxAnSipUaDomainName':zxAnSipUaDomainName,'zxAnSipUaProxySvrId1':zxAnSipUaProxySvrId1,'zxAnSipUaProxySvrId2':zxAnSipUaProxySvrId2,'zxAnSipUaProxySvrId3':zxAnSipUaProxySvrId3,'zxAnSipUaProxySvrId4':zxAnSipUaProxySvrId4,'zxAnSipUaSelfswitch':zxAnSipUaSelfswitch,'zxAnSipUaCallProtection':zxAnSipUaCallProtection,'zxAnSipUaIpType':zxAnSipUaIpType,'zxAnSipUaIp':zxAnSipUaIp,'zxAnSipUaSwitchProxySvrId':zxAnSipUaSwitchProxySvrId,'zxAnSipUaCurrentProxySvrId':zxAnSipUaCurrentProxySvrId,'zxAnSipUaRowStatus':zxAnSipUaRowStatus,'zxAnSipGroupTable':zxAnSipGroupTable,'zxAnSipGroupEntry':zxAnSipGroupEntry,_v:zxAnSipGroupMgId,_w:zxAnSipGroupId,'zxAnSipGroupName':zxAnSipGroupName,'zxAnSipGroupType':zxAnSipGroupType,'zxAnSipGroupOperNum':zxAnSipGroupOperNum,'zxAnSipGroupPhoneNumber':zxAnSipGroupPhoneNumber,'zxAnSipGroupUserId':zxAnSipGroupUserId,'zxAnSipGroupAuthUserName':zxAnSipGroupAuthUserName,'zxAnSipGroupOperType':zxAnSipGroupOperType,'zxAnSipGroupUserType':zxAnSipGroupUserType,'zxAnSipGroupUserStartNumber':zxAnSipGroupUserStartNumber,'zxAnSipGroupUserDigitLen':zxAnSipGroupUserDigitLen,'zxAnSipGroupPassword':zxAnSipGroupPassword,'zxAnSipGroupRowStatus':zxAnSipGroupRowStatus,'zxAnSipIsdnDLinkTable':zxAnSipIsdnDLinkTable,'zxAnSipIsdnDLinkEntry':zxAnSipIsdnDLinkEntry,_x:zxAnSipIsdnDLinkMgId,_y:zxAnSipIsdnDLinkGroupId,_z:zxAnSipIsdnDLinkLinkId,'zxAnSipIsdnDLinkRack':zxAnSipIsdnDLinkRack,'zxAnSipIsdnDLinkShelf':zxAnSipIsdnDLinkShelf,'zxAnSipIsdnDLinkSlot':zxAnSipIsdnDLinkSlot,'zxAnSipIsdnDLinkIndex':zxAnSipIsdnDLinkIndex,'zxAnSipIsdnDLinkDChanTs':zxAnSipIsdnDLinkDChanTs,'zxAnSipIsdnDLinkOperNum':zxAnSipIsdnDLinkOperNum,'zxAnSipIsdnDLinkType':zxAnSipIsdnDLinkType,'zxAnSipIsdnDLinkRowStatus':zxAnSipIsdnDLinkRowStatus,'zxAnSipIsdnUserTable':zxAnSipIsdnUserTable,'zxAnSipIsdnUserEntry':zxAnSipIsdnUserEntry,_A0:zxAnSipIsdnUserMgId,_A1:zxAnSipIsdnUserGroupId,_A2:zxAnSipIsdnUserSipPhoneNumber,'zxAnSipIsdnUserOperNum':zxAnSipIsdnUserOperNum,'zxAnSipIsdnUserOperType':zxAnSipIsdnUserOperType,'zxAnSipIsdnUserAuthUsername':zxAnSipIsdnUserAuthUsername,'zxAnSipIsdnUserAuthType':zxAnSipIsdnUserAuthType,'zxAnSipIsdnUserAuthStartNumber':zxAnSipIsdnUserAuthStartNumber,'zxAnSipIsdnUserAuthDigitLen':zxAnSipIsdnUserAuthDigitLen,'zxAnSipIsdnUserPassword':zxAnSipIsdnUserPassword,'zxAnSipIsdnUserId':zxAnSipIsdnUserId,'zxAnSipIsdnUserIdType':zxAnSipIsdnUserIdType,'zxAnSipIsdnUserIdStartNumber':zxAnSipIsdnUserIdStartNumber,'zxAnSipIsdnUserIdDigitLen':zxAnSipIsdnUserIdDigitLen,'zxAnSipIsdnUserRowStatus':zxAnSipIsdnUserRowStatus,'zxAnSipIsdnPhoneTable':zxAnSipIsdnPhoneTable,'zxAnSipIsdnPhoneEntry':zxAnSipIsdnPhoneEntry,_A3:zxAnSipIsdnPhoneSipPhone,_A4:zxAnSipIsdnPhoneIsdnPhone,'zxAnSipIsdnPhoneOperNum':zxAnSipIsdnPhoneOperNum,'zxAnSipIsdnPhoneRowStatus':zxAnSipIsdnPhoneRowStatus,'zxAnSipIsdnBChanTable':zxAnSipIsdnBChanTable,'zxAnSipIsdnBChanEntry':zxAnSipIsdnBChanEntry,_A5:zxAnSipIsdnBChanRack,_A6:zxAnSipIsdnBChanShelf,_A7:zxAnSipIsdnBChanSlot,_A8:zxAnSipIsdnBChanIndex,_A9:zxAnSipIsdnBChanTimeSlot,'zxAnSipIsdnBChanGroupId':zxAnSipIsdnBChanGroupId,'zxAnSipIsdnBChanPbxBChan':zxAnSipIsdnBChanPbxBChan,'zxAnSipIsdnBChanOperNum':zxAnSipIsdnBChanOperNum,'zxAnSipCallPerfTable':zxAnSipCallPerfTable,'zxAnSipRegCurrentUsers':zxAnSipRegCurrentUsers,'zxAnSipSuccessContactRegs':zxAnSipSuccessContactRegs,'zxAnSipFailedContactRegs':zxAnSipFailedContactRegs,'zxAnSipSuccessIncomingCalls':zxAnSipSuccessIncomingCalls,'zxAnSipFailedIncomingCalls':zxAnSipFailedIncomingCalls,'zxAnSipSuccessOutgoingCalls':zxAnSipSuccessOutgoingCalls,'zxAnSipFailedOutgoingCalls':zxAnSipFailedOutgoingCalls,'zxAnSipPrev15MinSuccessContactRegs':zxAnSipPrev15MinSuccessContactRegs,'zxAnSipPrev15MinFailedContactRegs':zxAnSipPrev15MinFailedContactRegs,'zxAnSipPrev15MinSuccessIncomingCalls':zxAnSipPrev15MinSuccessIncomingCalls,'zxAnSipPrev15MinFailedIncomingCalls':zxAnSipPrev15MinFailedIncomingCalls,'zxAnSipPrev15MinSuccessOutgoingCalls':zxAnSipPrev15MinSuccessOutgoingCalls,'zxAnSipPrev15MinFailedOutgoingCalls':zxAnSipPrev15MinFailedOutgoingCalls,'zxAnSipActiveIncomingCalls':zxAnSipActiveIncomingCalls,'zxAnSipActiveOutgoingCalls':zxAnSipActiveOutgoingCalls,'zxAnSipOutgoingCallTraffic':zxAnSipOutgoingCallTraffic,'zxAnSipIncomingCallTraffic':zxAnSipIncomingCallTraffic,'zxAnSipTotalCallTraffic':zxAnSipTotalCallTraffic,'zxAnSipOutgoingCallKeepingTime':zxAnSipOutgoingCallKeepingTime,'zxAnSipIncomingCallKeepingTime':zxAnSipIncomingCallKeepingTime,'zxAnSipTotalCallKeepingTime':zxAnSipTotalCallKeepingTime,'zxAnSipOutgoingCallAttempts':zxAnSipOutgoingCallAttempts,'zxAnSipOutgoingCallCompletions':zxAnSipOutgoingCallCompletions,'zxAnSipOutgoingCallLosses':zxAnSipOutgoingCallLosses,'zxAnSipIncomingCallAttempts':zxAnSipIncomingCallAttempts,'zxAnSipIncomingCallCompletions':zxAnSipIncomingCallCompletions,'zxAnSipIncomingCallLosses':zxAnSipIncomingCallLosses,'zxAnSipOutgoingCallCompleteRatio':zxAnSipOutgoingCallCompleteRatio,'zxAnSipIncomingCallCompleteRatio':zxAnSipIncomingCallCompleteRatio,'zxAnSipTotalCallCompleteRatio':zxAnSipTotalCallCompleteRatio,'zxAnSipTotalCallLossRatio':zxAnSipTotalCallLossRatio,'zxAnSipHisPerfObjects':zxAnSipHisPerfObjects,'zxAnSipHisPerfGlobalObjects':zxAnSipHisPerfGlobalObjects,'zxAnSipHisPerfIntervalType':zxAnSipHisPerfIntervalType,'zxAnSipHisPerfIntervalTable':zxAnSipHisPerfIntervalTable,'zxAnSipHisPerfIntervalEntry':zxAnSipHisPerfIntervalEntry,_AA:zxAnSipHisPerfIntervalNumber,'zxAnSipHisValidData':zxAnSipHisValidData,'zxAnSipHisSuccessContactRegs':zxAnSipHisSuccessContactRegs,'zxAnSipHisFailedContactRegs':zxAnSipHisFailedContactRegs,'zxAnSipHisSuccessInCalls':zxAnSipHisSuccessInCalls,'zxAnSipHisFailedInCalls':zxAnSipHisFailedInCalls,'zxAnSipHisSuccessOutCalls':zxAnSipHisSuccessOutCalls,'zxAnSipHisFailedOutCalls':zxAnSipHisFailedOutCalls,'zxAnSipHisOutCallTraffic':zxAnSipHisOutCallTraffic,'zxAnSipHisInCallTraffic':zxAnSipHisInCallTraffic,'zxAnSipHisTotalCallTraffic':zxAnSipHisTotalCallTraffic,'zxAnSipHisOutCallKeepTime':zxAnSipHisOutCallKeepTime,'zxAnSipHisInCallKeepTime':zxAnSipHisInCallKeepTime,'zxAnSipHisTotalCallKeepTime':zxAnSipHisTotalCallKeepTime,'zxAnSipHisOutCallAttempts':zxAnSipHisOutCallAttempts,'zxAnSipHisOutCallCompletions':zxAnSipHisOutCallCompletions,'zxAnSipHisOutCallLosses':zxAnSipHisOutCallLosses,'zxAnSipHisInCallAttempts':zxAnSipHisInCallAttempts,'zxAnSipHisInCallCompletions':zxAnSipHisInCallCompletions,'zxAnSipHisInCallLosses':zxAnSipHisInCallLosses,'zxAnSipHisOutCallCompleteRatio':zxAnSipHisOutCallCompleteRatio,'zxAnSipHisInCallCompleteRatio':zxAnSipHisInCallCompleteRatio,'zxAnSipHisTotalCallCompleteRatio':zxAnSipHisTotalCallCompleteRatio,'zxAnSipHisTotalCallLossRatio':zxAnSipHisTotalCallLossRatio,'zxAnSipTrap':zxAnSipTrap,'zxAnSipTrapObjects':zxAnSipTrapObjects,'zxAnSipLinkDown':zxAnSipLinkDown,'zxAnSipLinkUp':zxAnSipLinkUp,'zxAnSipUserRegisterFailedAlm':zxAnSipUserRegisterFailedAlm,'zxAnSipUserRegisterFailedClr':zxAnSipUserRegisterFailedClr,'zxAnSipTrapBindVar':zxAnSipTrapBindVar,_b:zxAnSipTrapReason,_c:zxAnSipTrapMgcNo})