_v='fsCMPortalMIBGroup'
_u='fsApNasPortIdNasPortId'
_t='fsCMPortalNtfLogoutRespCount'
_s='fsCMPortalNtfLogoutReqCount'
_r='fsCMPortalLogoutRespCount'
_q='fsCMPortalLogoutReqCount'
_p='fsCMPortalAuthFailCodeCount'
_o='fsCMPortalAuthFailCode'
_n='fsCMPortalAuthFailCauseCount'
_m='fsACPortalCurrentMaxAuthNum'
_l='fsACPortalMaxAuthNum'
_k='fsCMPortalStarbucksAuthRespCount'
_j='fsCMPortalEDUAuthRespCount'
_i='fsCMPortalNormalAuthRespCount'
_h='fsCMPortalStarbucksAuthReqCount'
_g='fsCMPortalEDUAuthReqCount'
_f='fsCMPortalNormalAuthReqCount'
_e='fsCMPortalAuthSuccessedCount'
_d='fsCMPortalExceptionFailCount'
_c='fsCMPortalHttpRespCount'
_b='fsCMPortalHttpReqCount'
_a='fsCMPortalServerConfigStatus'
_Z='fsCMPortalServerInUsedCount'
_Y='fsCMPortalServerName'
_X='fsCMPortalServerURL'
_W='fsCMPortalGlobalServerURL'
_V='fsCMPortalChallengeRespCount'
_U='fsCMPortalChallengeReqCount'
_T='fsCMPortalAuthRespCount'
_S='fsCMPortalAuthReqCount'
_R='fsCMPortalCurAuthNum'
_Q='fsCMPortalMaxAuthNum'
_P='fsCMPortalAuthFailCodeIndex'
_O='fsCMPortalAuthFailCauseErrId'
_N='fsCMPortalServerURLId'
_M='Integer32'
_L='fsApNasPortIdWlanId'
_K='fsApNasPortIdRadioId'
_J='fsApNasPortIdApMacAddress'
_I='fsCMPortalServerUnavailableCode'
_H='fsCMPortalServerInetPortNumber'
_G='fsCMPortalServerInetAddress'
_F='fsCMPortalServerInetAddressType'
_E='DisplayString'
_D='read-write'
_C='read-only'
_B='FS-CM-PORTAL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention')
fsCMPortalMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,74))
if mibBuilder.loadTexts:fsCMPortalMIB.setRevisions(('2010-03-22 00:00',))
_FsCMPortalMIBTrap_ObjectIdentity=ObjectIdentity
fsCMPortalMIBTrap=_FsCMPortalMIBTrap_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,74,0))
_FsCMPortalMIBObjects_ObjectIdentity=ObjectIdentity
fsCMPortalMIBObjects=_FsCMPortalMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,74,1))
_FsCMPortalMaxAuthNum_Type=Integer32
_FsCMPortalMaxAuthNum_Object=MibScalar
fsCMPortalMaxAuthNum=_FsCMPortalMaxAuthNum_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,1),_FsCMPortalMaxAuthNum_Type())
fsCMPortalMaxAuthNum.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCMPortalMaxAuthNum.setStatus(_A)
_FsCMPortalCurAuthNum_Type=Integer32
_FsCMPortalCurAuthNum_Object=MibScalar
fsCMPortalCurAuthNum=_FsCMPortalCurAuthNum_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,2),_FsCMPortalCurAuthNum_Type())
fsCMPortalCurAuthNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalCurAuthNum.setStatus(_A)
_FsCMPortalServerInetAddressType_Type=InetAddressType
_FsCMPortalServerInetAddressType_Object=MibScalar
fsCMPortalServerInetAddressType=_FsCMPortalServerInetAddressType_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,3),_FsCMPortalServerInetAddressType_Type())
fsCMPortalServerInetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCMPortalServerInetAddressType.setStatus(_A)
_FsCMPortalServerInetAddress_Type=InetAddress
_FsCMPortalServerInetAddress_Object=MibScalar
fsCMPortalServerInetAddress=_FsCMPortalServerInetAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,4),_FsCMPortalServerInetAddress_Type())
fsCMPortalServerInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCMPortalServerInetAddress.setStatus(_A)
_FsCMPortalServerInetPortNumber_Type=Integer32
_FsCMPortalServerInetPortNumber_Object=MibScalar
fsCMPortalServerInetPortNumber=_FsCMPortalServerInetPortNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,5),_FsCMPortalServerInetPortNumber_Type())
fsCMPortalServerInetPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCMPortalServerInetPortNumber.setStatus(_A)
class _FsCMPortalServerUnavailableCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-configured',0),('ping-failed',1)))
_FsCMPortalServerUnavailableCode_Type.__name__=_M
_FsCMPortalServerUnavailableCode_Object=MibScalar
fsCMPortalServerUnavailableCode=_FsCMPortalServerUnavailableCode_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,6),_FsCMPortalServerUnavailableCode_Type())
fsCMPortalServerUnavailableCode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalServerUnavailableCode.setStatus(_A)
_FsCMPortalAuthReqCount_Type=Counter32
_FsCMPortalAuthReqCount_Object=MibScalar
fsCMPortalAuthReqCount=_FsCMPortalAuthReqCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,7),_FsCMPortalAuthReqCount_Type())
fsCMPortalAuthReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalAuthReqCount.setStatus(_A)
_FsCMPortalAuthRespCount_Type=Counter32
_FsCMPortalAuthRespCount_Object=MibScalar
fsCMPortalAuthRespCount=_FsCMPortalAuthRespCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,8),_FsCMPortalAuthRespCount_Type())
fsCMPortalAuthRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalAuthRespCount.setStatus(_A)
_FsCMPortalChallengeReqCount_Type=Counter32
_FsCMPortalChallengeReqCount_Object=MibScalar
fsCMPortalChallengeReqCount=_FsCMPortalChallengeReqCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,9),_FsCMPortalChallengeReqCount_Type())
fsCMPortalChallengeReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalChallengeReqCount.setStatus(_A)
_FsCMPortalChallengeRespCount_Type=Counter32
_FsCMPortalChallengeRespCount_Object=MibScalar
fsCMPortalChallengeRespCount=_FsCMPortalChallengeRespCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,10),_FsCMPortalChallengeRespCount_Type())
fsCMPortalChallengeRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalChallengeRespCount.setStatus(_A)
class _FsCMPortalGlobalServerURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsCMPortalGlobalServerURL_Type.__name__=_E
_FsCMPortalGlobalServerURL_Object=MibScalar
fsCMPortalGlobalServerURL=_FsCMPortalGlobalServerURL_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,11),_FsCMPortalGlobalServerURL_Type())
fsCMPortalGlobalServerURL.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCMPortalGlobalServerURL.setStatus(_A)
_FsCMPortalServerURLTable_Object=MibTable
fsCMPortalServerURLTable=_FsCMPortalServerURLTable_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,12))
if mibBuilder.loadTexts:fsCMPortalServerURLTable.setStatus(_A)
_FsCMPortalServerURLEntry_Object=MibTableRow
fsCMPortalServerURLEntry=_FsCMPortalServerURLEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,12,1))
fsCMPortalServerURLEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:fsCMPortalServerURLEntry.setStatus(_A)
_FsCMPortalServerURLId_Type=Unsigned32
_FsCMPortalServerURLId_Object=MibTableColumn
fsCMPortalServerURLId=_FsCMPortalServerURLId_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,12,1,1),_FsCMPortalServerURLId_Type())
fsCMPortalServerURLId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalServerURLId.setStatus(_A)
class _FsCMPortalServerURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsCMPortalServerURL_Type.__name__=_E
_FsCMPortalServerURL_Object=MibTableColumn
fsCMPortalServerURL=_FsCMPortalServerURL_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,12,1,2),_FsCMPortalServerURL_Type())
fsCMPortalServerURL.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCMPortalServerURL.setStatus(_A)
class _FsCMPortalServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsCMPortalServerName_Type.__name__=_E
_FsCMPortalServerName_Object=MibTableColumn
fsCMPortalServerName=_FsCMPortalServerName_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,12,1,3),_FsCMPortalServerName_Type())
fsCMPortalServerName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCMPortalServerName.setStatus(_A)
_FsCMPortalServerInUsedCount_Type=Unsigned32
_FsCMPortalServerInUsedCount_Object=MibTableColumn
fsCMPortalServerInUsedCount=_FsCMPortalServerInUsedCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,12,1,4),_FsCMPortalServerInUsedCount_Type())
fsCMPortalServerInUsedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalServerInUsedCount.setStatus(_A)
_FsCMPortalServerConfigStatus_Type=RowStatus
_FsCMPortalServerConfigStatus_Object=MibTableColumn
fsCMPortalServerConfigStatus=_FsCMPortalServerConfigStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,12,1,5),_FsCMPortalServerConfigStatus_Type())
fsCMPortalServerConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsCMPortalServerConfigStatus.setStatus(_A)
_FsCMPortalHttpReqCount_Type=Counter32
_FsCMPortalHttpReqCount_Object=MibScalar
fsCMPortalHttpReqCount=_FsCMPortalHttpReqCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,13),_FsCMPortalHttpReqCount_Type())
fsCMPortalHttpReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalHttpReqCount.setStatus(_A)
_FsCMPortalHttpRespCount_Type=Counter32
_FsCMPortalHttpRespCount_Object=MibScalar
fsCMPortalHttpRespCount=_FsCMPortalHttpRespCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,14),_FsCMPortalHttpRespCount_Type())
fsCMPortalHttpRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalHttpRespCount.setStatus(_A)
_FsCMPortalExceptionFailCount_Type=Counter32
_FsCMPortalExceptionFailCount_Object=MibScalar
fsCMPortalExceptionFailCount=_FsCMPortalExceptionFailCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,15),_FsCMPortalExceptionFailCount_Type())
fsCMPortalExceptionFailCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalExceptionFailCount.setStatus(_A)
_FsCMPortalAuthSuccessedCount_Type=Counter32
_FsCMPortalAuthSuccessedCount_Object=MibScalar
fsCMPortalAuthSuccessedCount=_FsCMPortalAuthSuccessedCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,16),_FsCMPortalAuthSuccessedCount_Type())
fsCMPortalAuthSuccessedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalAuthSuccessedCount.setStatus(_A)
_FsCMPortalNormalAuthReqCount_Type=Counter32
_FsCMPortalNormalAuthReqCount_Object=MibScalar
fsCMPortalNormalAuthReqCount=_FsCMPortalNormalAuthReqCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,17),_FsCMPortalNormalAuthReqCount_Type())
fsCMPortalNormalAuthReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalNormalAuthReqCount.setStatus(_A)
_FsCMPortalEDUAuthReqCount_Type=Counter32
_FsCMPortalEDUAuthReqCount_Object=MibScalar
fsCMPortalEDUAuthReqCount=_FsCMPortalEDUAuthReqCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,18),_FsCMPortalEDUAuthReqCount_Type())
fsCMPortalEDUAuthReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalEDUAuthReqCount.setStatus(_A)
_FsCMPortalStarbucksAuthReqCount_Type=Counter32
_FsCMPortalStarbucksAuthReqCount_Object=MibScalar
fsCMPortalStarbucksAuthReqCount=_FsCMPortalStarbucksAuthReqCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,19),_FsCMPortalStarbucksAuthReqCount_Type())
fsCMPortalStarbucksAuthReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalStarbucksAuthReqCount.setStatus(_A)
_FsCMPortalNormalAuthRespCount_Type=Counter32
_FsCMPortalNormalAuthRespCount_Object=MibScalar
fsCMPortalNormalAuthRespCount=_FsCMPortalNormalAuthRespCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,20),_FsCMPortalNormalAuthRespCount_Type())
fsCMPortalNormalAuthRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalNormalAuthRespCount.setStatus(_A)
_FsCMPortalEDUAuthRespCount_Type=Counter32
_FsCMPortalEDUAuthRespCount_Object=MibScalar
fsCMPortalEDUAuthRespCount=_FsCMPortalEDUAuthRespCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,21),_FsCMPortalEDUAuthRespCount_Type())
fsCMPortalEDUAuthRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalEDUAuthRespCount.setStatus(_A)
_FsCMPortalStarbucksAuthRespCount_Type=Counter32
_FsCMPortalStarbucksAuthRespCount_Object=MibScalar
fsCMPortalStarbucksAuthRespCount=_FsCMPortalStarbucksAuthRespCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,22),_FsCMPortalStarbucksAuthRespCount_Type())
fsCMPortalStarbucksAuthRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalStarbucksAuthRespCount.setStatus(_A)
_FsACPortalMaxAuthNum_Type=Integer32
_FsACPortalMaxAuthNum_Object=MibScalar
fsACPortalMaxAuthNum=_FsACPortalMaxAuthNum_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,23),_FsACPortalMaxAuthNum_Type())
fsACPortalMaxAuthNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsACPortalMaxAuthNum.setStatus(_A)
_FsACPortalCurrentMaxAuthNum_Type=Integer32
_FsACPortalCurrentMaxAuthNum_Object=MibScalar
fsACPortalCurrentMaxAuthNum=_FsACPortalCurrentMaxAuthNum_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,24),_FsACPortalCurrentMaxAuthNum_Type())
fsACPortalCurrentMaxAuthNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsACPortalCurrentMaxAuthNum.setStatus(_A)
_FsCMPortalAuthFailCauseTable_Object=MibTable
fsCMPortalAuthFailCauseTable=_FsCMPortalAuthFailCauseTable_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,25))
if mibBuilder.loadTexts:fsCMPortalAuthFailCauseTable.setStatus(_A)
_FsCMPortalAuthFailCauseEntry_Object=MibTableRow
fsCMPortalAuthFailCauseEntry=_FsCMPortalAuthFailCauseEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,25,1))
fsCMPortalAuthFailCauseEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:fsCMPortalAuthFailCauseEntry.setStatus(_A)
class _FsCMPortalAuthFailCauseErrId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsCMPortalAuthFailCauseErrId_Type.__name__=_E
_FsCMPortalAuthFailCauseErrId_Object=MibTableColumn
fsCMPortalAuthFailCauseErrId=_FsCMPortalAuthFailCauseErrId_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,25,1,1),_FsCMPortalAuthFailCauseErrId_Type())
fsCMPortalAuthFailCauseErrId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalAuthFailCauseErrId.setStatus(_A)
_FsCMPortalAuthFailCauseCount_Type=Unsigned32
_FsCMPortalAuthFailCauseCount_Object=MibTableColumn
fsCMPortalAuthFailCauseCount=_FsCMPortalAuthFailCauseCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,25,1,2),_FsCMPortalAuthFailCauseCount_Type())
fsCMPortalAuthFailCauseCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalAuthFailCauseCount.setStatus(_A)
_FsCMPortalAuthFailCodeTable_Object=MibTable
fsCMPortalAuthFailCodeTable=_FsCMPortalAuthFailCodeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,26))
if mibBuilder.loadTexts:fsCMPortalAuthFailCodeTable.setStatus(_A)
_FsCMPortalAuthFailCodeEntry_Object=MibTableRow
fsCMPortalAuthFailCodeEntry=_FsCMPortalAuthFailCodeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,26,1))
fsCMPortalAuthFailCodeEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:fsCMPortalAuthFailCodeEntry.setStatus(_A)
_FsCMPortalAuthFailCodeIndex_Type=Unsigned32
_FsCMPortalAuthFailCodeIndex_Object=MibTableColumn
fsCMPortalAuthFailCodeIndex=_FsCMPortalAuthFailCodeIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,26,1,1),_FsCMPortalAuthFailCodeIndex_Type())
fsCMPortalAuthFailCodeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalAuthFailCodeIndex.setStatus(_A)
_FsCMPortalAuthFailCode_Type=Unsigned32
_FsCMPortalAuthFailCode_Object=MibTableColumn
fsCMPortalAuthFailCode=_FsCMPortalAuthFailCode_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,26,1,2),_FsCMPortalAuthFailCode_Type())
fsCMPortalAuthFailCode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalAuthFailCode.setStatus(_A)
_FsCMPortalAuthFailCodeCount_Type=Unsigned32
_FsCMPortalAuthFailCodeCount_Object=MibTableColumn
fsCMPortalAuthFailCodeCount=_FsCMPortalAuthFailCodeCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,26,1,3),_FsCMPortalAuthFailCodeCount_Type())
fsCMPortalAuthFailCodeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalAuthFailCodeCount.setStatus(_A)
_FsCMPortalLogoutReqCount_Type=Counter32
_FsCMPortalLogoutReqCount_Object=MibScalar
fsCMPortalLogoutReqCount=_FsCMPortalLogoutReqCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,27),_FsCMPortalLogoutReqCount_Type())
fsCMPortalLogoutReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalLogoutReqCount.setStatus(_A)
_FsCMPortalLogoutRespCount_Type=Counter32
_FsCMPortalLogoutRespCount_Object=MibScalar
fsCMPortalLogoutRespCount=_FsCMPortalLogoutRespCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,28),_FsCMPortalLogoutRespCount_Type())
fsCMPortalLogoutRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalLogoutRespCount.setStatus(_A)
_FsCMPortalNtfLogoutReqCount_Type=Counter32
_FsCMPortalNtfLogoutReqCount_Object=MibScalar
fsCMPortalNtfLogoutReqCount=_FsCMPortalNtfLogoutReqCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,29),_FsCMPortalNtfLogoutReqCount_Type())
fsCMPortalNtfLogoutReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalNtfLogoutReqCount.setStatus(_A)
_FsCMPortalNtfLogoutRespCount_Type=Counter32
_FsCMPortalNtfLogoutRespCount_Object=MibScalar
fsCMPortalNtfLogoutRespCount=_FsCMPortalNtfLogoutRespCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,30),_FsCMPortalNtfLogoutRespCount_Type())
fsCMPortalNtfLogoutRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalNtfLogoutRespCount.setStatus(_A)
_FsApNasPortIdTable_Object=MibTable
fsApNasPortIdTable=_FsApNasPortIdTable_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,31))
if mibBuilder.loadTexts:fsApNasPortIdTable.setStatus(_A)
_FsApNasPortIdEntry_Object=MibTableRow
fsApNasPortIdEntry=_FsApNasPortIdEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,31,1))
fsApNasPortIdEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:fsApNasPortIdEntry.setStatus(_A)
_FsApNasPortIdApMacAddress_Type=MacAddress
_FsApNasPortIdApMacAddress_Object=MibTableColumn
fsApNasPortIdApMacAddress=_FsApNasPortIdApMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,31,1,1),_FsApNasPortIdApMacAddress_Type())
fsApNasPortIdApMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsApNasPortIdApMacAddress.setStatus(_A)
_FsApNasPortIdRadioId_Type=Unsigned32
_FsApNasPortIdRadioId_Object=MibTableColumn
fsApNasPortIdRadioId=_FsApNasPortIdRadioId_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,31,1,2),_FsApNasPortIdRadioId_Type())
fsApNasPortIdRadioId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsApNasPortIdRadioId.setStatus(_A)
_FsApNasPortIdWlanId_Type=Unsigned32
_FsApNasPortIdWlanId_Object=MibTableColumn
fsApNasPortIdWlanId=_FsApNasPortIdWlanId_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,31,1,3),_FsApNasPortIdWlanId_Type())
fsApNasPortIdWlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsApNasPortIdWlanId.setStatus(_A)
_FsApNasPortIdNasPortId_Type=DisplayString
_FsApNasPortIdNasPortId_Object=MibTableColumn
fsApNasPortIdNasPortId=_FsApNasPortIdNasPortId_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,31,1,4),_FsApNasPortIdNasPortId_Type())
fsApNasPortIdNasPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsApNasPortIdNasPortId.setStatus(_A)
_FsCMPortalAuthFailCount_Type=Counter32
_FsCMPortalAuthFailCount_Object=MibScalar
fsCMPortalAuthFailCount=_FsCMPortalAuthFailCount_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,32),_FsCMPortalAuthFailCount_Type())
fsCMPortalAuthFailCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalAuthFailCount.setStatus(_A)
_FsCMPortalMaxHttpConnectionNum_Type=Counter32
_FsCMPortalMaxHttpConnectionNum_Object=MibScalar
fsCMPortalMaxHttpConnectionNum=_FsCMPortalMaxHttpConnectionNum_Object((1,3,6,1,4,1,52642,1,1,10,2,74,1,33),_FsCMPortalMaxHttpConnectionNum_Type())
fsCMPortalMaxHttpConnectionNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsCMPortalMaxHttpConnectionNum.setStatus(_A)
_FsCMPortalMIBConformance_ObjectIdentity=ObjectIdentity
fsCMPortalMIBConformance=_FsCMPortalMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,74,2))
_FsCMPortalMIBCompliances_ObjectIdentity=ObjectIdentity
fsCMPortalMIBCompliances=_FsCMPortalMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,74,2,1))
_FsCMPortalMIBGroups_ObjectIdentity=ObjectIdentity
fsCMPortalMIBGroups=_FsCMPortalMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,74,2,2))
fsCMPortalMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,74,2,2,1))
fsCMPortalMIBGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_J),(_B,_K),(_B,_L),(_B,_u)))
if mibBuilder.loadTexts:fsCMPortalMIBGroup.setStatus('deprecated')
fsCMPortalServerDownTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,74,0,1))
fsCMPortalServerDownTrap.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:fsCMPortalServerDownTrap.setStatus(_A)
fsCMPortalServerRecoverTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,74,0,2))
fsCMPortalServerRecoverTrap.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:fsCMPortalServerRecoverTrap.setStatus(_A)
fsCMPortalMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,74,2,1,1))
fsCMPortalMIBCompliance.setObjects((_B,_v))
if mibBuilder.loadTexts:fsCMPortalMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsCMPortalMIB':fsCMPortalMIB,'fsCMPortalMIBTrap':fsCMPortalMIBTrap,'fsCMPortalServerDownTrap':fsCMPortalServerDownTrap,'fsCMPortalServerRecoverTrap':fsCMPortalServerRecoverTrap,'fsCMPortalMIBObjects':fsCMPortalMIBObjects,_Q:fsCMPortalMaxAuthNum,_R:fsCMPortalCurAuthNum,_F:fsCMPortalServerInetAddressType,_G:fsCMPortalServerInetAddress,_H:fsCMPortalServerInetPortNumber,_I:fsCMPortalServerUnavailableCode,_S:fsCMPortalAuthReqCount,_T:fsCMPortalAuthRespCount,_U:fsCMPortalChallengeReqCount,_V:fsCMPortalChallengeRespCount,_W:fsCMPortalGlobalServerURL,'fsCMPortalServerURLTable':fsCMPortalServerURLTable,'fsCMPortalServerURLEntry':fsCMPortalServerURLEntry,_N:fsCMPortalServerURLId,_X:fsCMPortalServerURL,_Y:fsCMPortalServerName,_Z:fsCMPortalServerInUsedCount,_a:fsCMPortalServerConfigStatus,_b:fsCMPortalHttpReqCount,_c:fsCMPortalHttpRespCount,_d:fsCMPortalExceptionFailCount,_e:fsCMPortalAuthSuccessedCount,_f:fsCMPortalNormalAuthReqCount,_g:fsCMPortalEDUAuthReqCount,_h:fsCMPortalStarbucksAuthReqCount,_i:fsCMPortalNormalAuthRespCount,_j:fsCMPortalEDUAuthRespCount,_k:fsCMPortalStarbucksAuthRespCount,_l:fsACPortalMaxAuthNum,_m:fsACPortalCurrentMaxAuthNum,'fsCMPortalAuthFailCauseTable':fsCMPortalAuthFailCauseTable,'fsCMPortalAuthFailCauseEntry':fsCMPortalAuthFailCauseEntry,_O:fsCMPortalAuthFailCauseErrId,_n:fsCMPortalAuthFailCauseCount,'fsCMPortalAuthFailCodeTable':fsCMPortalAuthFailCodeTable,'fsCMPortalAuthFailCodeEntry':fsCMPortalAuthFailCodeEntry,_P:fsCMPortalAuthFailCodeIndex,_o:fsCMPortalAuthFailCode,_p:fsCMPortalAuthFailCodeCount,_q:fsCMPortalLogoutReqCount,_r:fsCMPortalLogoutRespCount,_s:fsCMPortalNtfLogoutReqCount,_t:fsCMPortalNtfLogoutRespCount,'fsApNasPortIdTable':fsApNasPortIdTable,'fsApNasPortIdEntry':fsApNasPortIdEntry,_J:fsApNasPortIdApMacAddress,_K:fsApNasPortIdRadioId,_L:fsApNasPortIdWlanId,_u:fsApNasPortIdNasPortId,'fsCMPortalAuthFailCount':fsCMPortalAuthFailCount,'fsCMPortalMaxHttpConnectionNum':fsCMPortalMaxHttpConnectionNum,'fsCMPortalMIBConformance':fsCMPortalMIBConformance,'fsCMPortalMIBCompliances':fsCMPortalMIBCompliances,'fsCMPortalMIBCompliance':fsCMPortalMIBCompliance,'fsCMPortalMIBGroups':fsCMPortalMIBGroups,_v:fsCMPortalMIBGroup})