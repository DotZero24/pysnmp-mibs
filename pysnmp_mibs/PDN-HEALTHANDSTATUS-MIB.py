_L='devFailureStatus'
_K='devSelfTestResults'
_J='devSNMPSetReqId'
_I='NotificationType'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='PDN-HEALTHANDSTATUS-MIB'
_C='DisplayString'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
ifIndex,=mibBuilder.importSymbols(_E,_F)
pdn_devStatus,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-devStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_I,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
_DevStatus_ObjectIdentity=ObjectIdentity
devStatus=_DevStatus_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,4,1))
class _DevHealthAndStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DevHealthAndStatus_Type.__name__=_C
_DevHealthAndStatus_Object=MibScalar
devHealthAndStatus=_DevHealthAndStatus_Object((1,3,6,1,4,1,1795,2,24,2,4,1,1),_DevHealthAndStatus_Type())
devHealthAndStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:devHealthAndStatus.setStatus(_A)
class _DevSelfTestResults_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DevSelfTestResults_Type.__name__=_C
_DevSelfTestResults_Object=MibScalar
devSelfTestResults=_DevSelfTestResults_Object((1,3,6,1,4,1,1795,2,24,2,4,1,2),_DevSelfTestResults_Type())
devSelfTestResults.setMaxAccess(_B)
if mibBuilder.loadTexts:devSelfTestResults.setStatus(_A)
class _DevAbortStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DevAbortStatus_Type.__name__=_C
_DevAbortStatus_Object=MibScalar
devAbortStatus=_DevAbortStatus_Object((1,3,6,1,4,1,1795,2,24,2,4,1,3),_DevAbortStatus_Type())
devAbortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:devAbortStatus.setStatus(_A)
_DevSNMPSetStatusTable_Object=MibTable
devSNMPSetStatusTable=_DevSNMPSetStatusTable_Object((1,3,6,1,4,1,1795,2,24,2,4,1,4))
if mibBuilder.loadTexts:devSNMPSetStatusTable.setStatus(_A)
_DevSNMPSetStatusEntry_Object=MibTableRow
devSNMPSetStatusEntry=_DevSNMPSetStatusEntry_Object((1,3,6,1,4,1,1795,2,24,2,4,1,4,1))
devSNMPSetStatusEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:devSNMPSetStatusEntry.setStatus(_A)
_DevSNMPSetReqId_Type=Integer32
_DevSNMPSetReqId_Object=MibTableColumn
devSNMPSetReqId=_DevSNMPSetReqId_Object((1,3,6,1,4,1,1795,2,24,2,4,1,4,1,1),_DevSNMPSetReqId_Type())
devSNMPSetReqId.setMaxAccess(_B)
if mibBuilder.loadTexts:devSNMPSetReqId.setStatus(_A)
class _DevSNMPSetStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DevSNMPSetStatus_Type.__name__=_C
_DevSNMPSetStatus_Object=MibTableColumn
devSNMPSetStatus=_DevSNMPSetStatus_Object((1,3,6,1,4,1,1795,2,24,2,4,1,4,1,2),_DevSNMPSetStatus_Type())
devSNMPSetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:devSNMPSetStatus.setStatus(_A)
_DevAuthenticationFailureIpAddress_Type=IpAddress
_DevAuthenticationFailureIpAddress_Object=MibScalar
devAuthenticationFailureIpAddress=_DevAuthenticationFailureIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,4,1,5),_DevAuthenticationFailureIpAddress_Type())
devAuthenticationFailureIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:devAuthenticationFailureIpAddress.setStatus(_A)
class _DevLastTrapString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DevLastTrapString_Type.__name__=_C
_DevLastTrapString_Object=MibScalar
devLastTrapString=_DevLastTrapString_Object((1,3,6,1,4,1,1795,2,24,2,4,1,6),_DevLastTrapString_Type())
devLastTrapString.setMaxAccess(_B)
if mibBuilder.loadTexts:devLastTrapString.setStatus(_A)
class _DevFailureStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DevFailureStatus_Type.__name__=_C
_DevFailureStatus_Object=MibScalar
devFailureStatus=_DevFailureStatus_Object((1,3,6,1,4,1,1795,2,24,2,4,1,7),_DevFailureStatus_Type())
devFailureStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:devFailureStatus.setStatus(_A)
_DevStatusTrapEnable_Type=Integer32
_DevStatusTrapEnable_Object=MibScalar
devStatusTrapEnable=_DevStatusTrapEnable_Object((1,3,6,1,4,1,1795,2,24,2,4,1,8),_DevStatusTrapEnable_Type())
devStatusTrapEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:devStatusTrapEnable.setStatus(_A)
_DevSelfTestResultTable_Object=MibTable
devSelfTestResultTable=_DevSelfTestResultTable_Object((1,3,6,1,4,1,1795,2,24,2,4,1,9))
if mibBuilder.loadTexts:devSelfTestResultTable.setStatus(_A)
_DevSelfTestResultEntry_Object=MibTableRow
devSelfTestResultEntry=_DevSelfTestResultEntry_Object((1,3,6,1,4,1,1795,2,24,2,4,1,9,1))
devSelfTestResultEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:devSelfTestResultEntry.setStatus(_A)
_DevSelfTestResult_Type=DisplayString
_DevSelfTestResult_Object=MibTableColumn
devSelfTestResult=_DevSelfTestResult_Object((1,3,6,1,4,1,1795,2,24,2,4,1,9,1,1),_DevSelfTestResult_Type())
devSelfTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:devSelfTestResult.setStatus(_A)
devSelfTestFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,4,1,0,1))
devSelfTestFailure.setObjects(*((_E,_F),(_D,_K)))
if mibBuilder.loadTexts:devSelfTestFailure.setStatus('')
deviceFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,4,1,0,2))
deviceFailure.setObjects(*((_E,_F),(_D,_L)))
if mibBuilder.loadTexts:deviceFailure.setStatus('')
mibBuilder.exportSymbols(_D,**{'devStatus':devStatus,'devSelfTestFailure':devSelfTestFailure,'deviceFailure':deviceFailure,'devHealthAndStatus':devHealthAndStatus,_K:devSelfTestResults,'devAbortStatus':devAbortStatus,'devSNMPSetStatusTable':devSNMPSetStatusTable,'devSNMPSetStatusEntry':devSNMPSetStatusEntry,_J:devSNMPSetReqId,'devSNMPSetStatus':devSNMPSetStatus,'devAuthenticationFailureIpAddress':devAuthenticationFailureIpAddress,'devLastTrapString':devLastTrapString,_L:devFailureStatus,'devStatusTrapEnable':devStatusTrapEnable,'devSelfTestResultTable':devSelfTestResultTable,'devSelfTestResultEntry':devSelfTestResultEntry,'devSelfTestResult':devSelfTestResult})