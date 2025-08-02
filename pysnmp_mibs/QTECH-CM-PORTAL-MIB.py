_i='qtechCMPortalMIBGroup'
_h='qtechACPortalCurrentMaxAuthNum'
_g='qtechACPortalMaxAuthNum'
_f='qtechCMPortalStarbucksAuthRespCount'
_e='qtechCMPortalEDUAuthRespCount'
_d='qtechCMPortalNormalAuthRespCount'
_c='qtechCMPortalStarbucksAuthReqCount'
_b='qtechCMPortalEDUAuthReqCount'
_a='qtechCMPortalNormalAuthReqCount'
_Z='qtechCMPortalAuthSuccessedCount'
_Y='qtechCMPortalExceptionFailCount'
_X='qtechCMPortalHttpRespCount'
_W='qtechCMPortalHttpReqCount'
_V='qtechCMPortalServerConfigStatus'
_U='qtechCMPortalServerInUsedCount'
_T='qtechCMPortalServerName'
_S='qtechCMPortalServerURL'
_R='qtechCMPortalGlobalServerURL'
_Q='qtechCMPortalChallengeRespCount'
_P='qtechCMPortalChallengeReqCount'
_O='qtechCMPortalAuthRespCount'
_N='qtechCMPortalAuthReqCount'
_M='qtechCMPortalCurAuthNum'
_L='qtechCMPortalMaxAuthNum'
_K='qtechCMPortalServerURLId'
_J='Integer32'
_I='qtechCMPortalServerUnavailableCode'
_H='qtechCMPortalServerInetPortNumber'
_G='qtechCMPortalServerInetAddress'
_F='qtechCMPortalServerInetAddressType'
_E='DisplayString'
_D='read-write'
_C='read-only'
_B='current'
_A='QTECH-CM-PORTAL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
qtechCMPortalMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,74))
if mibBuilder.loadTexts:qtechCMPortalMIB.setRevisions(('2010-03-22 00:00',))
_QtechCMPortalMIBTrap_ObjectIdentity=ObjectIdentity
qtechCMPortalMIBTrap=_QtechCMPortalMIBTrap_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,74,0))
_QtechCMPortalMIBObjects_ObjectIdentity=ObjectIdentity
qtechCMPortalMIBObjects=_QtechCMPortalMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,74,1))
_QtechCMPortalMaxAuthNum_Type=Integer32
_QtechCMPortalMaxAuthNum_Object=MibScalar
qtechCMPortalMaxAuthNum=_QtechCMPortalMaxAuthNum_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,1),_QtechCMPortalMaxAuthNum_Type())
qtechCMPortalMaxAuthNum.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCMPortalMaxAuthNum.setStatus(_B)
_QtechCMPortalCurAuthNum_Type=Integer32
_QtechCMPortalCurAuthNum_Object=MibScalar
qtechCMPortalCurAuthNum=_QtechCMPortalCurAuthNum_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,2),_QtechCMPortalCurAuthNum_Type())
qtechCMPortalCurAuthNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalCurAuthNum.setStatus(_B)
_QtechCMPortalServerInetAddressType_Type=InetAddressType
_QtechCMPortalServerInetAddressType_Object=MibScalar
qtechCMPortalServerInetAddressType=_QtechCMPortalServerInetAddressType_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,3),_QtechCMPortalServerInetAddressType_Type())
qtechCMPortalServerInetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCMPortalServerInetAddressType.setStatus(_B)
_QtechCMPortalServerInetAddress_Type=InetAddress
_QtechCMPortalServerInetAddress_Object=MibScalar
qtechCMPortalServerInetAddress=_QtechCMPortalServerInetAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,4),_QtechCMPortalServerInetAddress_Type())
qtechCMPortalServerInetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCMPortalServerInetAddress.setStatus(_B)
_QtechCMPortalServerInetPortNumber_Type=Integer32
_QtechCMPortalServerInetPortNumber_Object=MibScalar
qtechCMPortalServerInetPortNumber=_QtechCMPortalServerInetPortNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,5),_QtechCMPortalServerInetPortNumber_Type())
qtechCMPortalServerInetPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCMPortalServerInetPortNumber.setStatus(_B)
class _QtechCMPortalServerUnavailableCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('not-configured',0),('ping-failed',1)))
_QtechCMPortalServerUnavailableCode_Type.__name__=_J
_QtechCMPortalServerUnavailableCode_Object=MibScalar
qtechCMPortalServerUnavailableCode=_QtechCMPortalServerUnavailableCode_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,6),_QtechCMPortalServerUnavailableCode_Type())
qtechCMPortalServerUnavailableCode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalServerUnavailableCode.setStatus(_B)
_QtechCMPortalAuthReqCount_Type=Counter32
_QtechCMPortalAuthReqCount_Object=MibScalar
qtechCMPortalAuthReqCount=_QtechCMPortalAuthReqCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,7),_QtechCMPortalAuthReqCount_Type())
qtechCMPortalAuthReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalAuthReqCount.setStatus(_B)
_QtechCMPortalAuthRespCount_Type=Counter32
_QtechCMPortalAuthRespCount_Object=MibScalar
qtechCMPortalAuthRespCount=_QtechCMPortalAuthRespCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,8),_QtechCMPortalAuthRespCount_Type())
qtechCMPortalAuthRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalAuthRespCount.setStatus(_B)
_QtechCMPortalChallengeReqCount_Type=Counter32
_QtechCMPortalChallengeReqCount_Object=MibScalar
qtechCMPortalChallengeReqCount=_QtechCMPortalChallengeReqCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,9),_QtechCMPortalChallengeReqCount_Type())
qtechCMPortalChallengeReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalChallengeReqCount.setStatus(_B)
_QtechCMPortalChallengeRespCount_Type=Counter32
_QtechCMPortalChallengeRespCount_Object=MibScalar
qtechCMPortalChallengeRespCount=_QtechCMPortalChallengeRespCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,10),_QtechCMPortalChallengeRespCount_Type())
qtechCMPortalChallengeRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalChallengeRespCount.setStatus(_B)
class _QtechCMPortalGlobalServerURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechCMPortalGlobalServerURL_Type.__name__=_E
_QtechCMPortalGlobalServerURL_Object=MibScalar
qtechCMPortalGlobalServerURL=_QtechCMPortalGlobalServerURL_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,11),_QtechCMPortalGlobalServerURL_Type())
qtechCMPortalGlobalServerURL.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCMPortalGlobalServerURL.setStatus(_B)
_QtechCMPortalServerURLTable_Object=MibTable
qtechCMPortalServerURLTable=_QtechCMPortalServerURLTable_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,12))
if mibBuilder.loadTexts:qtechCMPortalServerURLTable.setStatus(_B)
_QtechCMPortalServerURLEntry_Object=MibTableRow
qtechCMPortalServerURLEntry=_QtechCMPortalServerURLEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,12,1))
qtechCMPortalServerURLEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:qtechCMPortalServerURLEntry.setStatus(_B)
_QtechCMPortalServerURLId_Type=Unsigned32
_QtechCMPortalServerURLId_Object=MibTableColumn
qtechCMPortalServerURLId=_QtechCMPortalServerURLId_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,12,1,1),_QtechCMPortalServerURLId_Type())
qtechCMPortalServerURLId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalServerURLId.setStatus(_B)
class _QtechCMPortalServerURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_QtechCMPortalServerURL_Type.__name__=_E
_QtechCMPortalServerURL_Object=MibTableColumn
qtechCMPortalServerURL=_QtechCMPortalServerURL_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,12,1,2),_QtechCMPortalServerURL_Type())
qtechCMPortalServerURL.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCMPortalServerURL.setStatus(_B)
class _QtechCMPortalServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechCMPortalServerName_Type.__name__=_E
_QtechCMPortalServerName_Object=MibTableColumn
qtechCMPortalServerName=_QtechCMPortalServerName_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,12,1,3),_QtechCMPortalServerName_Type())
qtechCMPortalServerName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCMPortalServerName.setStatus(_B)
_QtechCMPortalServerInUsedCount_Type=Unsigned32
_QtechCMPortalServerInUsedCount_Object=MibTableColumn
qtechCMPortalServerInUsedCount=_QtechCMPortalServerInUsedCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,12,1,4),_QtechCMPortalServerInUsedCount_Type())
qtechCMPortalServerInUsedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalServerInUsedCount.setStatus(_B)
_QtechCMPortalServerConfigStatus_Type=RowStatus
_QtechCMPortalServerConfigStatus_Object=MibTableColumn
qtechCMPortalServerConfigStatus=_QtechCMPortalServerConfigStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,12,1,5),_QtechCMPortalServerConfigStatus_Type())
qtechCMPortalServerConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechCMPortalServerConfigStatus.setStatus(_B)
_QtechCMPortalHttpReqCount_Type=Counter32
_QtechCMPortalHttpReqCount_Object=MibScalar
qtechCMPortalHttpReqCount=_QtechCMPortalHttpReqCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,13),_QtechCMPortalHttpReqCount_Type())
qtechCMPortalHttpReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalHttpReqCount.setStatus(_B)
_QtechCMPortalHttpRespCount_Type=Counter32
_QtechCMPortalHttpRespCount_Object=MibScalar
qtechCMPortalHttpRespCount=_QtechCMPortalHttpRespCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,14),_QtechCMPortalHttpRespCount_Type())
qtechCMPortalHttpRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalHttpRespCount.setStatus(_B)
_QtechCMPortalExceptionFailCount_Type=Counter32
_QtechCMPortalExceptionFailCount_Object=MibScalar
qtechCMPortalExceptionFailCount=_QtechCMPortalExceptionFailCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,15),_QtechCMPortalExceptionFailCount_Type())
qtechCMPortalExceptionFailCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalExceptionFailCount.setStatus(_B)
_QtechCMPortalAuthSuccessedCount_Type=Counter32
_QtechCMPortalAuthSuccessedCount_Object=MibScalar
qtechCMPortalAuthSuccessedCount=_QtechCMPortalAuthSuccessedCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,16),_QtechCMPortalAuthSuccessedCount_Type())
qtechCMPortalAuthSuccessedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalAuthSuccessedCount.setStatus(_B)
_QtechCMPortalNormalAuthReqCount_Type=Counter32
_QtechCMPortalNormalAuthReqCount_Object=MibScalar
qtechCMPortalNormalAuthReqCount=_QtechCMPortalNormalAuthReqCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,17),_QtechCMPortalNormalAuthReqCount_Type())
qtechCMPortalNormalAuthReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalNormalAuthReqCount.setStatus(_B)
_QtechCMPortalEDUAuthReqCount_Type=Counter32
_QtechCMPortalEDUAuthReqCount_Object=MibScalar
qtechCMPortalEDUAuthReqCount=_QtechCMPortalEDUAuthReqCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,18),_QtechCMPortalEDUAuthReqCount_Type())
qtechCMPortalEDUAuthReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalEDUAuthReqCount.setStatus(_B)
_QtechCMPortalStarbucksAuthReqCount_Type=Counter32
_QtechCMPortalStarbucksAuthReqCount_Object=MibScalar
qtechCMPortalStarbucksAuthReqCount=_QtechCMPortalStarbucksAuthReqCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,19),_QtechCMPortalStarbucksAuthReqCount_Type())
qtechCMPortalStarbucksAuthReqCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalStarbucksAuthReqCount.setStatus(_B)
_QtechCMPortalNormalAuthRespCount_Type=Counter32
_QtechCMPortalNormalAuthRespCount_Object=MibScalar
qtechCMPortalNormalAuthRespCount=_QtechCMPortalNormalAuthRespCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,20),_QtechCMPortalNormalAuthRespCount_Type())
qtechCMPortalNormalAuthRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalNormalAuthRespCount.setStatus(_B)
_QtechCMPortalEDUAuthRespCount_Type=Counter32
_QtechCMPortalEDUAuthRespCount_Object=MibScalar
qtechCMPortalEDUAuthRespCount=_QtechCMPortalEDUAuthRespCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,21),_QtechCMPortalEDUAuthRespCount_Type())
qtechCMPortalEDUAuthRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalEDUAuthRespCount.setStatus(_B)
_QtechCMPortalStarbucksAuthRespCount_Type=Counter32
_QtechCMPortalStarbucksAuthRespCount_Object=MibScalar
qtechCMPortalStarbucksAuthRespCount=_QtechCMPortalStarbucksAuthRespCount_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,22),_QtechCMPortalStarbucksAuthRespCount_Type())
qtechCMPortalStarbucksAuthRespCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechCMPortalStarbucksAuthRespCount.setStatus(_B)
_QtechACPortalMaxAuthNum_Type=Integer32
_QtechACPortalMaxAuthNum_Object=MibScalar
qtechACPortalMaxAuthNum=_QtechACPortalMaxAuthNum_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,23),_QtechACPortalMaxAuthNum_Type())
qtechACPortalMaxAuthNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechACPortalMaxAuthNum.setStatus(_B)
_QtechACPortalCurrentMaxAuthNum_Type=Integer32
_QtechACPortalCurrentMaxAuthNum_Object=MibScalar
qtechACPortalCurrentMaxAuthNum=_QtechACPortalCurrentMaxAuthNum_Object((1,3,6,1,4,1,27514,1,1,10,2,74,1,24),_QtechACPortalCurrentMaxAuthNum_Type())
qtechACPortalCurrentMaxAuthNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechACPortalCurrentMaxAuthNum.setStatus(_B)
_QtechCMPortalMIBConformance_ObjectIdentity=ObjectIdentity
qtechCMPortalMIBConformance=_QtechCMPortalMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,74,2))
_QtechCMPortalMIBCompliances_ObjectIdentity=ObjectIdentity
qtechCMPortalMIBCompliances=_QtechCMPortalMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,74,2,1))
_QtechCMPortalMIBGroups_ObjectIdentity=ObjectIdentity
qtechCMPortalMIBGroups=_QtechCMPortalMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,74,2,2))
qtechCMPortalMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,74,2,2,1))
qtechCMPortalMIBGroup.setObjects(*((_A,_L),(_A,_M),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:qtechCMPortalMIBGroup.setStatus('deprecated')
qtechCMPortalServerDownTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,74,0,1))
qtechCMPortalServerDownTrap.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:qtechCMPortalServerDownTrap.setStatus(_B)
qtechCMPortalServerRecoverTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,74,0,2))
qtechCMPortalServerRecoverTrap.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:qtechCMPortalServerRecoverTrap.setStatus(_B)
qtechCMPortalMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,74,2,1,1))
qtechCMPortalMIBCompliance.setObjects((_A,_i))
if mibBuilder.loadTexts:qtechCMPortalMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtechCMPortalMIB':qtechCMPortalMIB,'qtechCMPortalMIBTrap':qtechCMPortalMIBTrap,'qtechCMPortalServerDownTrap':qtechCMPortalServerDownTrap,'qtechCMPortalServerRecoverTrap':qtechCMPortalServerRecoverTrap,'qtechCMPortalMIBObjects':qtechCMPortalMIBObjects,_L:qtechCMPortalMaxAuthNum,_M:qtechCMPortalCurAuthNum,_F:qtechCMPortalServerInetAddressType,_G:qtechCMPortalServerInetAddress,_H:qtechCMPortalServerInetPortNumber,_I:qtechCMPortalServerUnavailableCode,_N:qtechCMPortalAuthReqCount,_O:qtechCMPortalAuthRespCount,_P:qtechCMPortalChallengeReqCount,_Q:qtechCMPortalChallengeRespCount,_R:qtechCMPortalGlobalServerURL,'qtechCMPortalServerURLTable':qtechCMPortalServerURLTable,'qtechCMPortalServerURLEntry':qtechCMPortalServerURLEntry,_K:qtechCMPortalServerURLId,_S:qtechCMPortalServerURL,_T:qtechCMPortalServerName,_U:qtechCMPortalServerInUsedCount,_V:qtechCMPortalServerConfigStatus,_W:qtechCMPortalHttpReqCount,_X:qtechCMPortalHttpRespCount,_Y:qtechCMPortalExceptionFailCount,_Z:qtechCMPortalAuthSuccessedCount,_a:qtechCMPortalNormalAuthReqCount,_b:qtechCMPortalEDUAuthReqCount,_c:qtechCMPortalStarbucksAuthReqCount,_d:qtechCMPortalNormalAuthRespCount,_e:qtechCMPortalEDUAuthRespCount,_f:qtechCMPortalStarbucksAuthRespCount,_g:qtechACPortalMaxAuthNum,_h:qtechACPortalCurrentMaxAuthNum,'qtechCMPortalMIBConformance':qtechCMPortalMIBConformance,'qtechCMPortalMIBCompliances':qtechCMPortalMIBCompliances,'qtechCMPortalMIBCompliance':qtechCMPortalMIBCompliance,'qtechCMPortalMIBGroups':qtechCMPortalMIBGroups,_i:qtechCMPortalMIBGroup})