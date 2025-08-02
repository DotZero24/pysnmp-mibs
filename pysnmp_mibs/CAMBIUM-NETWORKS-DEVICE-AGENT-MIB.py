_F='TruthValue'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_B,'PhysAddress','TextualConvention',_F)
deviceAgent=ModuleIdentity((1,3,6,1,4,1,17713,24,2))
if mibBuilder.loadTexts:deviceAgent.setRevisions(('2021-11-30 00:00','2020-06-24 00:00','2019-02-19 15:00'))
_CnMatrix_ObjectIdentity=ObjectIdentity
cnMatrix=_CnMatrix_ObjectIdentity((1,3,6,1,4,1,17713,24))
class _CambiumDeviceAgentEnable_Type(TruthValue):defaultValue=1
_CambiumDeviceAgentEnable_Type.__name__=_F
_CambiumDeviceAgentEnable_Object=MibScalar
cambiumDeviceAgentEnable=_CambiumDeviceAgentEnable_Object((1,3,6,1,4,1,17713,24,2,1),_CambiumDeviceAgentEnable_Type())
cambiumDeviceAgentEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cambiumDeviceAgentEnable.setStatus(_A)
class _CambiumDeviceAgentStaticURL_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CambiumDeviceAgentStaticURL_Type.__name__=_B
_CambiumDeviceAgentStaticURL_Object=MibScalar
cambiumDeviceAgentStaticURL=_CambiumDeviceAgentStaticURL_Object((1,3,6,1,4,1,17713,24,2,2),_CambiumDeviceAgentStaticURL_Type())
cambiumDeviceAgentStaticURL.setMaxAccess(_D)
if mibBuilder.loadTexts:cambiumDeviceAgentStaticURL.setStatus(_A)
class _CambiumCNSDeviceAgentID_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CambiumCNSDeviceAgentID_Type.__name__=_B
_CambiumCNSDeviceAgentID_Object=MibScalar
cambiumCNSDeviceAgentID=_CambiumCNSDeviceAgentID_Object((1,3,6,1,4,1,17713,24,2,3),_CambiumCNSDeviceAgentID_Type())
cambiumCNSDeviceAgentID.setMaxAccess(_D)
if mibBuilder.loadTexts:cambiumCNSDeviceAgentID.setStatus(_A)
class _CambiumCNSDeviceAgentPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CambiumCNSDeviceAgentPassword_Type.__name__=_B
_CambiumCNSDeviceAgentPassword_Object=MibScalar
cambiumCNSDeviceAgentPassword=_CambiumCNSDeviceAgentPassword_Object((1,3,6,1,4,1,17713,24,2,4),_CambiumCNSDeviceAgentPassword_Type())
cambiumCNSDeviceAgentPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:cambiumCNSDeviceAgentPassword.setStatus(_A)
class _CambiumDeviceAgentValidateCert_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cloud-only',1),('disabled',2),('full',3)))
_CambiumDeviceAgentValidateCert_Type.__name__=_E
_CambiumDeviceAgentValidateCert_Object=MibScalar
cambiumDeviceAgentValidateCert=_CambiumDeviceAgentValidateCert_Object((1,3,6,1,4,1,17713,24,2,5),_CambiumDeviceAgentValidateCert_Type())
cambiumDeviceAgentValidateCert.setMaxAccess(_D)
if mibBuilder.loadTexts:cambiumDeviceAgentValidateCert.setStatus(_A)
class _CambiumDeviceAgentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('notConnected',1),('dnsFailed',2),('noCambiumId',3),('error',4),('connecting',5),('approvalPending',6),('connected',7),('ownershipError',8),('messageFromCNS',9)))
_CambiumDeviceAgentStatus_Type.__name__=_E
_CambiumDeviceAgentStatus_Object=MibScalar
cambiumDeviceAgentStatus=_CambiumDeviceAgentStatus_Object((1,3,6,1,4,1,17713,24,2,6),_CambiumDeviceAgentStatus_Type())
cambiumDeviceAgentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cambiumDeviceAgentStatus.setStatus(_A)
class _CambiumDeviceAgentStatusMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CambiumDeviceAgentStatusMessage_Type.__name__=_B
_CambiumDeviceAgentStatusMessage_Object=MibScalar
cambiumDeviceAgentStatusMessage=_CambiumDeviceAgentStatusMessage_Object((1,3,6,1,4,1,17713,24,2,7),_CambiumDeviceAgentStatusMessage_Type())
cambiumDeviceAgentStatusMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:cambiumDeviceAgentStatusMessage.setStatus(_A)
class _CambiumDeviceAgentCNSURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CambiumDeviceAgentCNSURL_Type.__name__=_B
_CambiumDeviceAgentCNSURL_Object=MibScalar
cambiumDeviceAgentCNSURL=_CambiumDeviceAgentCNSURL_Object((1,3,6,1,4,1,17713,24,2,8),_CambiumDeviceAgentCNSURL_Type())
cambiumDeviceAgentCNSURL.setMaxAccess(_C)
if mibBuilder.loadTexts:cambiumDeviceAgentCNSURL.setStatus(_A)
class _CambiumDeviceAgentAccountID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CambiumDeviceAgentAccountID_Type.__name__=_B
_CambiumDeviceAgentAccountID_Object=MibScalar
cambiumDeviceAgentAccountID=_CambiumDeviceAgentAccountID_Object((1,3,6,1,4,1,17713,24,2,9),_CambiumDeviceAgentAccountID_Type())
cambiumDeviceAgentAccountID.setMaxAccess(_C)
if mibBuilder.loadTexts:cambiumDeviceAgentAccountID.setStatus(_A)
class _CambiumDeviceAgentLastAction_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CambiumDeviceAgentLastAction_Type.__name__=_B
_CambiumDeviceAgentLastAction_Object=MibScalar
cambiumDeviceAgentLastAction=_CambiumDeviceAgentLastAction_Object((1,3,6,1,4,1,17713,24,2,10),_CambiumDeviceAgentLastAction_Type())
cambiumDeviceAgentLastAction.setMaxAccess(_C)
if mibBuilder.loadTexts:cambiumDeviceAgentLastAction.setStatus(_A)
_CambiumDeviceAgentLastSync_Type=DateAndTime
_CambiumDeviceAgentLastSync_Object=MibScalar
cambiumDeviceAgentLastSync=_CambiumDeviceAgentLastSync_Object((1,3,6,1,4,1,17713,24,2,11),_CambiumDeviceAgentLastSync_Type())
cambiumDeviceAgentLastSync.setMaxAccess(_C)
if mibBuilder.loadTexts:cambiumDeviceAgentLastSync.setStatus(_A)
class _CambiumDeviceAgentRemoteManager_Type(TruthValue):defaultValue=2
_CambiumDeviceAgentRemoteManager_Type.__name__=_F
_CambiumDeviceAgentRemoteManager_Object=MibScalar
cambiumDeviceAgentRemoteManager=_CambiumDeviceAgentRemoteManager_Object((1,3,6,1,4,1,17713,24,2,12),_CambiumDeviceAgentRemoteManager_Type())
cambiumDeviceAgentRemoteManager.setMaxAccess(_C)
if mibBuilder.loadTexts:cambiumDeviceAgentRemoteManager.setStatus(_A)
mibBuilder.exportSymbols('CAMBIUM-NETWORKS-DEVICE-AGENT-MIB',**{'cnMatrix':cnMatrix,'deviceAgent':deviceAgent,'cambiumDeviceAgentEnable':cambiumDeviceAgentEnable,'cambiumDeviceAgentStaticURL':cambiumDeviceAgentStaticURL,'cambiumCNSDeviceAgentID':cambiumCNSDeviceAgentID,'cambiumCNSDeviceAgentPassword':cambiumCNSDeviceAgentPassword,'cambiumDeviceAgentValidateCert':cambiumDeviceAgentValidateCert,'cambiumDeviceAgentStatus':cambiumDeviceAgentStatus,'cambiumDeviceAgentStatusMessage':cambiumDeviceAgentStatusMessage,'cambiumDeviceAgentCNSURL':cambiumDeviceAgentCNSURL,'cambiumDeviceAgentAccountID':cambiumDeviceAgentAccountID,'cambiumDeviceAgentLastAction':cambiumDeviceAgentLastAction,'cambiumDeviceAgentLastSync':cambiumDeviceAgentLastSync,'cambiumDeviceAgentRemoteManager':cambiumDeviceAgentRemoteManager})