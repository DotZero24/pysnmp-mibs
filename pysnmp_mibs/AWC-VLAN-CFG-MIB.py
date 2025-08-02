_h='awcVlanCfgObjectsGroup'
_g='awcVlanAllowUnencryptedVlanId'
_f='awcVlanNUcastKeyValue'
_e='awcVlanNUcastKeyLen'
_d='awcVlanAlert'
_c='awcVlanDefaultUserPriority'
_b='awcVlanName'
_a='awcVlanWEPKeyPermuteAlgorithm'
_Z='awcVlanMicAlgorithm'
_Y='awcVlanRowStatus'
_X='awcVlanNUcastKeyRotationInterval'
_W='awcVlanEnabled'
_V='awcVlanPolId'
_U='awcVlanAllowEncrypted'
_T='awcNativeVlanId'
_S='awcVlanEncapMode'
_R='awcMaxVlanIds'
_Q='awcVlanNUcastKeyIndex'
_P='not-accessible'
_O='AwcVlanEncapType'
_N='read-only'
_M='AwcPolId'
_L='AwcPfPriority'
_K='AwcDot11WEPKeyPermuteAlgorithm'
_J='AwcDot11MicAlgorithm'
_I='OctetString'
_H='awcVlanIndex'
_G='AwcVlanId'
_F='Integer32'
_E='TruthValue'
_D='read-write'
_C='read-create'
_B='AWC-VLAN-CFG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AwcDot11MicAlgorithm,AwcDot11WEPKeyPermuteAlgorithm,AwcPfPriority,AwcPolId,AwcVlanId,WEPKeytype128,awcVx=mibBuilder.importSymbols('AWCVX-MIB',_J,_K,_L,_M,_G,'WEPKeytype128','awcVx')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_E)
awcVlanCfgMIB=ModuleIdentity((1,3,6,1,4,1,522,3,21))
if mibBuilder.loadTexts:awcVlanCfgMIB.setRevisions(('2001-07-11 00:00',))
class AwcVlanIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
class AwcVlanEncapType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dot1qDisabled',1),('dot1qPriority',2),('dot1qHybrid',3),('dot1qTrunk',4)))
_AwcVlanCfgObjects_ObjectIdentity=ObjectIdentity
awcVlanCfgObjects=_AwcVlanCfgObjects_ObjectIdentity((1,3,6,1,4,1,522,3,21,1))
_AwcMaxVlanIds_Type=Unsigned32
_AwcMaxVlanIds_Object=MibScalar
awcMaxVlanIds=_AwcMaxVlanIds_Object((1,3,6,1,4,1,522,3,21,1,1),_AwcMaxVlanIds_Type())
awcMaxVlanIds.setMaxAccess(_N)
if mibBuilder.loadTexts:awcMaxVlanIds.setStatus(_A)
class _AwcVlanEncapMode_Type(AwcVlanEncapType):defaultValue=1
_AwcVlanEncapMode_Type.__name__=_O
_AwcVlanEncapMode_Object=MibScalar
awcVlanEncapMode=_AwcVlanEncapMode_Object((1,3,6,1,4,1,522,3,21,1,2),_AwcVlanEncapMode_Type())
awcVlanEncapMode.setMaxAccess(_N)
if mibBuilder.loadTexts:awcVlanEncapMode.setStatus(_A)
class _AwcNativeVlanId_Type(AwcVlanId):defaultValue=0
_AwcNativeVlanId_Type.__name__=_G
_AwcNativeVlanId_Object=MibScalar
awcNativeVlanId=_AwcNativeVlanId_Object((1,3,6,1,4,1,522,3,21,1,3),_AwcNativeVlanId_Type())
awcNativeVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:awcNativeVlanId.setStatus(_A)
class _AwcVlanAllowEncrypted_Type(TruthValue):defaultValue=1
_AwcVlanAllowEncrypted_Type.__name__=_E
_AwcVlanAllowEncrypted_Object=MibScalar
awcVlanAllowEncrypted=_AwcVlanAllowEncrypted_Object((1,3,6,1,4,1,522,3,21,1,4),_AwcVlanAllowEncrypted_Type())
awcVlanAllowEncrypted.setMaxAccess(_D)
if mibBuilder.loadTexts:awcVlanAllowEncrypted.setStatus(_A)
class _AwcVlanAnyEnabled_Type(TruthValue):defaultValue=2
_AwcVlanAnyEnabled_Type.__name__=_E
_AwcVlanAnyEnabled_Object=MibScalar
awcVlanAnyEnabled=_AwcVlanAnyEnabled_Object((1,3,6,1,4,1,522,3,21,1,5),_AwcVlanAnyEnabled_Type())
awcVlanAnyEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:awcVlanAnyEnabled.setStatus(_A)
_AwcVlanCfgTable_Object=MibTable
awcVlanCfgTable=_AwcVlanCfgTable_Object((1,3,6,1,4,1,522,3,21,1,6))
if mibBuilder.loadTexts:awcVlanCfgTable.setStatus(_A)
_AwcVlanCfgEntry_Object=MibTableRow
awcVlanCfgEntry=_AwcVlanCfgEntry_Object((1,3,6,1,4,1,522,3,21,1,6,1))
awcVlanCfgEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:awcVlanCfgEntry.setStatus(_A)
_AwcVlanIndex_Type=AwcVlanIndex
_AwcVlanIndex_Object=MibTableColumn
awcVlanIndex=_AwcVlanIndex_Object((1,3,6,1,4,1,522,3,21,1,6,1,1),_AwcVlanIndex_Type())
awcVlanIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:awcVlanIndex.setStatus(_A)
class _AwcVlanPolId_Type(AwcPolId):defaultValue=0
_AwcVlanPolId_Type.__name__=_M
_AwcVlanPolId_Object=MibTableColumn
awcVlanPolId=_AwcVlanPolId_Object((1,3,6,1,4,1,522,3,21,1,6,1,2),_AwcVlanPolId_Type())
awcVlanPolId.setMaxAccess(_C)
if mibBuilder.loadTexts:awcVlanPolId.setStatus(_A)
class _AwcVlanEnabled_Type(TruthValue):defaultValue=2
_AwcVlanEnabled_Type.__name__=_E
_AwcVlanEnabled_Object=MibTableColumn
awcVlanEnabled=_AwcVlanEnabled_Object((1,3,6,1,4,1,522,3,21,1,6,1,3),_AwcVlanEnabled_Type())
awcVlanEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:awcVlanEnabled.setStatus(_A)
class _AwcVlanNUcastKeyRotationInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_AwcVlanNUcastKeyRotationInterval_Type.__name__=_F
_AwcVlanNUcastKeyRotationInterval_Object=MibTableColumn
awcVlanNUcastKeyRotationInterval=_AwcVlanNUcastKeyRotationInterval_Object((1,3,6,1,4,1,522,3,21,1,6,1,4),_AwcVlanNUcastKeyRotationInterval_Type())
awcVlanNUcastKeyRotationInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:awcVlanNUcastKeyRotationInterval.setStatus(_A)
if mibBuilder.loadTexts:awcVlanNUcastKeyRotationInterval.setUnits('seconds')
_AwcVlanRowStatus_Type=RowStatus
_AwcVlanRowStatus_Object=MibTableColumn
awcVlanRowStatus=_AwcVlanRowStatus_Object((1,3,6,1,4,1,522,3,21,1,6,1,5),_AwcVlanRowStatus_Type())
awcVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:awcVlanRowStatus.setStatus(_A)
class _AwcVlanMicAlgorithm_Type(AwcDot11MicAlgorithm):defaultValue=1
_AwcVlanMicAlgorithm_Type.__name__=_J
_AwcVlanMicAlgorithm_Object=MibTableColumn
awcVlanMicAlgorithm=_AwcVlanMicAlgorithm_Object((1,3,6,1,4,1,522,3,21,1,6,1,6),_AwcVlanMicAlgorithm_Type())
awcVlanMicAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:awcVlanMicAlgorithm.setStatus(_A)
class _AwcVlanWEPKeyPermuteAlgorithm_Type(AwcDot11WEPKeyPermuteAlgorithm):defaultValue=1
_AwcVlanWEPKeyPermuteAlgorithm_Type.__name__=_K
_AwcVlanWEPKeyPermuteAlgorithm_Object=MibTableColumn
awcVlanWEPKeyPermuteAlgorithm=_AwcVlanWEPKeyPermuteAlgorithm_Object((1,3,6,1,4,1,522,3,21,1,6,1,7),_AwcVlanWEPKeyPermuteAlgorithm_Type())
awcVlanWEPKeyPermuteAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:awcVlanWEPKeyPermuteAlgorithm.setStatus(_A)
class _AwcVlanName_Type(OctetString):defaultValue=OctetString('')
_AwcVlanName_Type.__name__=_I
_AwcVlanName_Object=MibTableColumn
awcVlanName=_AwcVlanName_Object((1,3,6,1,4,1,522,3,21,1,6,1,8),_AwcVlanName_Type())
awcVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:awcVlanName.setStatus(_A)
class _AwcVlanDefaultUserPriority_Type(AwcPfPriority):defaultValue=1
_AwcVlanDefaultUserPriority_Type.__name__=_L
_AwcVlanDefaultUserPriority_Object=MibTableColumn
awcVlanDefaultUserPriority=_AwcVlanDefaultUserPriority_Object((1,3,6,1,4,1,522,3,21,1,6,1,9),_AwcVlanDefaultUserPriority_Type())
awcVlanDefaultUserPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:awcVlanDefaultUserPriority.setStatus(_A)
class _AwcVlanAlert_Type(TruthValue):defaultValue=2
_AwcVlanAlert_Type.__name__=_E
_AwcVlanAlert_Object=MibTableColumn
awcVlanAlert=_AwcVlanAlert_Object((1,3,6,1,4,1,522,3,21,1,6,1,10),_AwcVlanAlert_Type())
awcVlanAlert.setMaxAccess(_C)
if mibBuilder.loadTexts:awcVlanAlert.setStatus(_A)
_AwcVlanNUcastKeyTable_Object=MibTable
awcVlanNUcastKeyTable=_AwcVlanNUcastKeyTable_Object((1,3,6,1,4,1,522,3,21,1,7))
if mibBuilder.loadTexts:awcVlanNUcastKeyTable.setStatus(_A)
_AwcVlanNUcastKeyEntry_Object=MibTableRow
awcVlanNUcastKeyEntry=_AwcVlanNUcastKeyEntry_Object((1,3,6,1,4,1,522,3,21,1,7,1))
awcVlanNUcastKeyEntry.setIndexNames((0,_B,_H),(0,_B,_Q))
if mibBuilder.loadTexts:awcVlanNUcastKeyEntry.setStatus(_A)
class _AwcVlanNUcastKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AwcVlanNUcastKeyIndex_Type.__name__=_F
_AwcVlanNUcastKeyIndex_Object=MibTableColumn
awcVlanNUcastKeyIndex=_AwcVlanNUcastKeyIndex_Object((1,3,6,1,4,1,522,3,21,1,7,1,1),_AwcVlanNUcastKeyIndex_Type())
awcVlanNUcastKeyIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:awcVlanNUcastKeyIndex.setStatus(_A)
class _AwcVlanNUcastKeyLen_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,13))
_AwcVlanNUcastKeyLen_Type.__name__=_F
_AwcVlanNUcastKeyLen_Object=MibTableColumn
awcVlanNUcastKeyLen=_AwcVlanNUcastKeyLen_Object((1,3,6,1,4,1,522,3,21,1,7,1,2),_AwcVlanNUcastKeyLen_Type())
awcVlanNUcastKeyLen.setMaxAccess(_D)
if mibBuilder.loadTexts:awcVlanNUcastKeyLen.setStatus(_A)
_AwcVlanNUcastKeyValue_Type=WEPKeytype128
_AwcVlanNUcastKeyValue_Object=MibTableColumn
awcVlanNUcastKeyValue=_AwcVlanNUcastKeyValue_Object((1,3,6,1,4,1,522,3,21,1,7,1,3),_AwcVlanNUcastKeyValue_Type())
awcVlanNUcastKeyValue.setMaxAccess(_D)
if mibBuilder.loadTexts:awcVlanNUcastKeyValue.setStatus(_A)
class _AwcVlanAllowUnencryptedVlanId_Type(AwcVlanId):defaultValue=0
_AwcVlanAllowUnencryptedVlanId_Type.__name__=_G
_AwcVlanAllowUnencryptedVlanId_Object=MibScalar
awcVlanAllowUnencryptedVlanId=_AwcVlanAllowUnencryptedVlanId_Object((1,3,6,1,4,1,522,3,21,1,8),_AwcVlanAllowUnencryptedVlanId_Type())
awcVlanAllowUnencryptedVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:awcVlanAllowUnencryptedVlanId.setStatus(_A)
_AwcVlanCfgNotifications_ObjectIdentity=ObjectIdentity
awcVlanCfgNotifications=_AwcVlanCfgNotifications_ObjectIdentity((1,3,6,1,4,1,522,3,21,2))
_AwcVlanCfgConformance_ObjectIdentity=ObjectIdentity
awcVlanCfgConformance=_AwcVlanCfgConformance_ObjectIdentity((1,3,6,1,4,1,522,3,21,3))
_AwcVlanCfgCompliances_ObjectIdentity=ObjectIdentity
awcVlanCfgCompliances=_AwcVlanCfgCompliances_ObjectIdentity((1,3,6,1,4,1,522,3,21,3,1))
_AwcVlanCfgGroups_ObjectIdentity=ObjectIdentity
awcVlanCfgGroups=_AwcVlanCfgGroups_ObjectIdentity((1,3,6,1,4,1,522,3,21,3,2))
awcVlanCfgObjectsGroup=ObjectGroup((1,3,6,1,4,1,522,3,21,3,2,1))
awcVlanCfgObjectsGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:awcVlanCfgObjectsGroup.setStatus(_A)
awcVlanCfgCompliance=ModuleCompliance((1,3,6,1,4,1,522,3,21,3,1,1))
awcVlanCfgCompliance.setObjects((_B,_h))
if mibBuilder.loadTexts:awcVlanCfgCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AwcVlanIndex':AwcVlanIndex,_O:AwcVlanEncapType,'awcVlanCfgMIB':awcVlanCfgMIB,'awcVlanCfgObjects':awcVlanCfgObjects,_R:awcMaxVlanIds,_S:awcVlanEncapMode,_T:awcNativeVlanId,_U:awcVlanAllowEncrypted,'awcVlanAnyEnabled':awcVlanAnyEnabled,'awcVlanCfgTable':awcVlanCfgTable,'awcVlanCfgEntry':awcVlanCfgEntry,_H:awcVlanIndex,_V:awcVlanPolId,_W:awcVlanEnabled,_X:awcVlanNUcastKeyRotationInterval,_Y:awcVlanRowStatus,_Z:awcVlanMicAlgorithm,_a:awcVlanWEPKeyPermuteAlgorithm,_b:awcVlanName,_c:awcVlanDefaultUserPriority,_d:awcVlanAlert,'awcVlanNUcastKeyTable':awcVlanNUcastKeyTable,'awcVlanNUcastKeyEntry':awcVlanNUcastKeyEntry,_Q:awcVlanNUcastKeyIndex,_e:awcVlanNUcastKeyLen,_f:awcVlanNUcastKeyValue,_g:awcVlanAllowUnencryptedVlanId,'awcVlanCfgNotifications':awcVlanCfgNotifications,'awcVlanCfgConformance':awcVlanCfgConformance,'awcVlanCfgCompliances':awcVlanCfgCompliances,'awcVlanCfgCompliance':awcVlanCfgCompliance,'awcVlanCfgGroups':awcVlanCfgGroups,_h:awcVlanCfgObjectsGroup})