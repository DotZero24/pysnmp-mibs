_E='DisplayString'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
featureKeys=ModuleIdentity((1,3,6,1,4,1,3373,1103,101))
if mibBuilder.loadTexts:featureKeys.setRevisions(('2014-02-03 00:00','2013-04-16 00:00'))
class _FeatureKeysMibVersion_Type(Integer32):defaultValue=1
_FeatureKeysMibVersion_Type.__name__=_B
_FeatureKeysMibVersion_Object=MibScalar
featureKeysMibVersion=_FeatureKeysMibVersion_Object((1,3,6,1,4,1,3373,1103,101,1),_FeatureKeysMibVersion_Type())
featureKeysMibVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:featureKeysMibVersion.setStatus(_A)
_FeatureKeysRadioMap_Type=OctetString
_FeatureKeysRadioMap_Object=MibScalar
featureKeysRadioMap=_FeatureKeysRadioMap_Object((1,3,6,1,4,1,3373,1103,101,2),_FeatureKeysRadioMap_Type())
featureKeysRadioMap.setMaxAccess(_C)
if mibBuilder.loadTexts:featureKeysRadioMap.setStatus(_A)
_FeatureKeysLineMap_Type=OctetString
_FeatureKeysLineMap_Object=MibScalar
featureKeysLineMap=_FeatureKeysLineMap_Object((1,3,6,1,4,1,3373,1103,101,3),_FeatureKeysLineMap_Type())
featureKeysLineMap.setMaxAccess(_C)
if mibBuilder.loadTexts:featureKeysLineMap.setStatus(_A)
class _FeatureKeysActionRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('upload',2)))
_FeatureKeysActionRequest_Type.__name__=_B
_FeatureKeysActionRequest_Object=MibScalar
featureKeysActionRequest=_FeatureKeysActionRequest_Object((1,3,6,1,4,1,3373,1103,101,4),_FeatureKeysActionRequest_Type())
featureKeysActionRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:featureKeysActionRequest.setStatus(_A)
class _FeatureKeysCertificateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FeatureKeysCertificateName_Type.__name__=_E
_FeatureKeysCertificateName_Object=MibScalar
featureKeysCertificateName=_FeatureKeysCertificateName_Object((1,3,6,1,4,1,3373,1103,101,5),_FeatureKeysCertificateName_Type())
featureKeysCertificateName.setMaxAccess(_C)
if mibBuilder.loadTexts:featureKeysCertificateName.setStatus(_A)
_FeatureKeysCertificateRemoteIpAddress_Type=IpAddress
_FeatureKeysCertificateRemoteIpAddress_Object=MibScalar
featureKeysCertificateRemoteIpAddress=_FeatureKeysCertificateRemoteIpAddress_Object((1,3,6,1,4,1,3373,1103,101,6),_FeatureKeysCertificateRemoteIpAddress_Type())
featureKeysCertificateRemoteIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:featureKeysCertificateRemoteIpAddress.setStatus(_A)
class _FeatureKeysLastOperationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('initial',1),('downloadCompleted',2),('downloadTransferring',3),('downloadVerifying',4),('downloadInterrupted',5),('setSuccess',6),('setFailure',7)))
_FeatureKeysLastOperationState_Type.__name__=_B
_FeatureKeysLastOperationState_Object=MibScalar
featureKeysLastOperationState=_FeatureKeysLastOperationState_Object((1,3,6,1,4,1,3373,1103,101,7),_FeatureKeysLastOperationState_Type())
featureKeysLastOperationState.setMaxAccess(_D)
if mibBuilder.loadTexts:featureKeysLastOperationState.setStatus(_A)
class _FeatureKeysLastOperationFailure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noFailure',1),('transfer',2),('serialNo',3),('verifySign',4),('primaryDigest',5),('secondaryDigest',6)))
_FeatureKeysLastOperationFailure_Type.__name__=_B
_FeatureKeysLastOperationFailure_Object=MibScalar
featureKeysLastOperationFailure=_FeatureKeysLastOperationFailure_Object((1,3,6,1,4,1,3373,1103,101,8),_FeatureKeysLastOperationFailure_Type())
featureKeysLastOperationFailure.setMaxAccess(_D)
if mibBuilder.loadTexts:featureKeysLastOperationFailure.setStatus(_A)
mibBuilder.exportSymbols('SIAE-FEATUREKEYS-MIB',**{'featureKeys':featureKeys,'featureKeysMibVersion':featureKeysMibVersion,'featureKeysRadioMap':featureKeysRadioMap,'featureKeysLineMap':featureKeysLineMap,'featureKeysActionRequest':featureKeysActionRequest,'featureKeysCertificateName':featureKeysCertificateName,'featureKeysCertificateRemoteIpAddress':featureKeysCertificateRemoteIpAddress,'featureKeysLastOperationState':featureKeysLastOperationState,'featureKeysLastOperationFailure':featureKeysLastOperationFailure})