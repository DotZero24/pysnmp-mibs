_h='ciscoWlanDot11VlanConfigGroup'
_g='ciscoWlanVlanNotificationGroup'
_f='ciscoWlanRoamDomainGroup'
_e='ciscoWlanVlanWepChangeNotif'
_d='cwvlWlanWepChangeNotifEnabled'
_c='cwvlWlanNUcastKeyLen'
_b='cwvlWlanRowStatus'
_a='cwvlWlanEncryptionAlgorithm'
_Z='cwvlWlanWepKeyHashing'
_Y='cwvlWlanWepKeyPermuteAlgorithm'
_X='cwvlWlanMicAlgorithm'
_W='cwvlWlanEncryptionMandatory'
_V='cwvlWlanEncryptionMode'
_U='cwvlWlanNUcastKeyRotateInterval'
_T='cwvlWlanEnabled'
_S='cwvlPublicVlanId'
_R='cwvlVoIPVlanId'
_Q='cwvlVoIPVlanEnabled'
_P='cwvlBridgingNativeVlanId'
_O='cwvlWlanDot1qEncapEnabled'
_N='cwvlWlanNUcastKeyIndex'
_M='not-accessible'
_L='CDot11IfWepKeyPermuteAlgorithm'
_K='CDot11IfMicAlgorithm'
_J='cwvlWlanNUcastKeyValue'
_I='cwvlWlanVlanId'
_H='Integer32'
_G='CwvlVlanIdOrZero'
_F='Unsigned32'
_E='TruthValue'
_D='read-write'
_C='read-create'
_B='CISCO-WLAN-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CDot11IfMicAlgorithm,CDot11IfWepKeyPermuteAlgorithm,WepKeyType128=mibBuilder.importSymbols('CISCO-DOT11-IF-MIB',_K,_L,'WepKeyType128')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_E)
ciscoWlanVlanMIB=ModuleIdentity((1,3,6,1,4,1,9,9,268))
if mibBuilder.loadTexts:ciscoWlanVlanMIB.setRevisions(('2002-06-12 00:00','2002-04-04 00:00','2002-03-07 00:00'))
class CwvlVlanIdOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CiscoWlanVlanMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoWlanVlanMIBNotifications=_CiscoWlanVlanMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,268,0))
_CiscoWlanVlanMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWlanVlanMIBObjects=_CiscoWlanVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,268,1))
_CwvlRoamDomainConfig_ObjectIdentity=ObjectIdentity
cwvlRoamDomainConfig=_CwvlRoamDomainConfig_ObjectIdentity((1,3,6,1,4,1,9,9,268,1,1))
class _CwvlWlanDot1qEncapEnabled_Type(TruthValue):defaultValue=2
_CwvlWlanDot1qEncapEnabled_Type.__name__=_E
_CwvlWlanDot1qEncapEnabled_Object=MibScalar
cwvlWlanDot1qEncapEnabled=_CwvlWlanDot1qEncapEnabled_Object((1,3,6,1,4,1,9,9,268,1,1,1),_CwvlWlanDot1qEncapEnabled_Type())
cwvlWlanDot1qEncapEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cwvlWlanDot1qEncapEnabled.setStatus(_A)
class _CwvlBridgingNativeVlanId_Type(CwvlVlanIdOrZero):defaultValue=0
_CwvlBridgingNativeVlanId_Type.__name__=_G
_CwvlBridgingNativeVlanId_Object=MibScalar
cwvlBridgingNativeVlanId=_CwvlBridgingNativeVlanId_Object((1,3,6,1,4,1,9,9,268,1,1,2),_CwvlBridgingNativeVlanId_Type())
cwvlBridgingNativeVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cwvlBridgingNativeVlanId.setStatus(_A)
class _CwvlVoIPVlanEnabled_Type(TruthValue):defaultValue=1
_CwvlVoIPVlanEnabled_Type.__name__=_E
_CwvlVoIPVlanEnabled_Object=MibScalar
cwvlVoIPVlanEnabled=_CwvlVoIPVlanEnabled_Object((1,3,6,1,4,1,9,9,268,1,1,3),_CwvlVoIPVlanEnabled_Type())
cwvlVoIPVlanEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cwvlVoIPVlanEnabled.setStatus(_A)
class _CwvlVoIPVlanId_Type(CwvlVlanIdOrZero):defaultValue=4095
_CwvlVoIPVlanId_Type.__name__=_G
_CwvlVoIPVlanId_Object=MibScalar
cwvlVoIPVlanId=_CwvlVoIPVlanId_Object((1,3,6,1,4,1,9,9,268,1,1,4),_CwvlVoIPVlanId_Type())
cwvlVoIPVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cwvlVoIPVlanId.setStatus(_A)
class _CwvlPublicVlanId_Type(CwvlVlanIdOrZero):defaultValue=0
_CwvlPublicVlanId_Type.__name__=_G
_CwvlPublicVlanId_Object=MibScalar
cwvlPublicVlanId=_CwvlPublicVlanId_Object((1,3,6,1,4,1,9,9,268,1,1,5),_CwvlPublicVlanId_Type())
cwvlPublicVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cwvlPublicVlanId.setStatus(_A)
_CwvlDot11VlanConfig_ObjectIdentity=ObjectIdentity
cwvlDot11VlanConfig=_CwvlDot11VlanConfig_ObjectIdentity((1,3,6,1,4,1,9,9,268,1,2))
_CwvlWlanVlanTable_Object=MibTable
cwvlWlanVlanTable=_CwvlWlanVlanTable_Object((1,3,6,1,4,1,9,9,268,1,2,1))
if mibBuilder.loadTexts:cwvlWlanVlanTable.setStatus(_A)
_CwvlWlanVlanEntry_Object=MibTableRow
cwvlWlanVlanEntry=_CwvlWlanVlanEntry_Object((1,3,6,1,4,1,9,9,268,1,2,1,1))
cwvlWlanVlanEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cwvlWlanVlanEntry.setStatus(_A)
_CwvlWlanVlanId_Type=CwvlVlanIdOrZero
_CwvlWlanVlanId_Object=MibTableColumn
cwvlWlanVlanId=_CwvlWlanVlanId_Object((1,3,6,1,4,1,9,9,268,1,2,1,1,1),_CwvlWlanVlanId_Type())
cwvlWlanVlanId.setMaxAccess(_M)
if mibBuilder.loadTexts:cwvlWlanVlanId.setStatus(_A)
class _CwvlWlanEnabled_Type(TruthValue):defaultValue=1
_CwvlWlanEnabled_Type.__name__=_E
_CwvlWlanEnabled_Object=MibTableColumn
cwvlWlanEnabled=_CwvlWlanEnabled_Object((1,3,6,1,4,1,9,9,268,1,2,1,1,2),_CwvlWlanEnabled_Type())
cwvlWlanEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cwvlWlanEnabled.setStatus(_A)
class _CwvlWlanNUcastKeyRotateInterval_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_CwvlWlanNUcastKeyRotateInterval_Type.__name__=_F
_CwvlWlanNUcastKeyRotateInterval_Object=MibTableColumn
cwvlWlanNUcastKeyRotateInterval=_CwvlWlanNUcastKeyRotateInterval_Object((1,3,6,1,4,1,9,9,268,1,2,1,1,3),_CwvlWlanNUcastKeyRotateInterval_Type())
cwvlWlanNUcastKeyRotateInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cwvlWlanNUcastKeyRotateInterval.setStatus(_A)
if mibBuilder.loadTexts:cwvlWlanNUcastKeyRotateInterval.setUnits('seconds')
class _CwvlWlanEncryptionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('wep',2),('aes',3)))
_CwvlWlanEncryptionMode_Type.__name__=_H
_CwvlWlanEncryptionMode_Object=MibTableColumn
cwvlWlanEncryptionMode=_CwvlWlanEncryptionMode_Object((1,3,6,1,4,1,9,9,268,1,2,1,1,4),_CwvlWlanEncryptionMode_Type())
cwvlWlanEncryptionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cwvlWlanEncryptionMode.setStatus(_A)
class _CwvlWlanEncryptionMandatory_Type(TruthValue):defaultValue=1
_CwvlWlanEncryptionMandatory_Type.__name__=_E
_CwvlWlanEncryptionMandatory_Object=MibTableColumn
cwvlWlanEncryptionMandatory=_CwvlWlanEncryptionMandatory_Object((1,3,6,1,4,1,9,9,268,1,2,1,1,5),_CwvlWlanEncryptionMandatory_Type())
cwvlWlanEncryptionMandatory.setMaxAccess(_C)
if mibBuilder.loadTexts:cwvlWlanEncryptionMandatory.setStatus(_A)
class _CwvlWlanMicAlgorithm_Type(CDot11IfMicAlgorithm):defaultValue=1
_CwvlWlanMicAlgorithm_Type.__name__=_K
_CwvlWlanMicAlgorithm_Object=MibTableColumn
cwvlWlanMicAlgorithm=_CwvlWlanMicAlgorithm_Object((1,3,6,1,4,1,9,9,268,1,2,1,1,6),_CwvlWlanMicAlgorithm_Type())
cwvlWlanMicAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:cwvlWlanMicAlgorithm.setStatus(_A)
class _CwvlWlanWepKeyPermuteAlgorithm_Type(CDot11IfWepKeyPermuteAlgorithm):defaultValue=1
_CwvlWlanWepKeyPermuteAlgorithm_Type.__name__=_L
_CwvlWlanWepKeyPermuteAlgorithm_Object=MibTableColumn
cwvlWlanWepKeyPermuteAlgorithm=_CwvlWlanWepKeyPermuteAlgorithm_Object((1,3,6,1,4,1,9,9,268,1,2,1,1,7),_CwvlWlanWepKeyPermuteAlgorithm_Type())
cwvlWlanWepKeyPermuteAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:cwvlWlanWepKeyPermuteAlgorithm.setStatus(_A)
class _CwvlWlanWepKeyHashing_Type(TruthValue):defaultValue=2
_CwvlWlanWepKeyHashing_Type.__name__=_E
_CwvlWlanWepKeyHashing_Object=MibTableColumn
cwvlWlanWepKeyHashing=_CwvlWlanWepKeyHashing_Object((1,3,6,1,4,1,9,9,268,1,2,1,1,8),_CwvlWlanWepKeyHashing_Type())
cwvlWlanWepKeyHashing.setMaxAccess(_C)
if mibBuilder.loadTexts:cwvlWlanWepKeyHashing.setStatus(_A)
class _CwvlWlanEncryptionAlgorithm_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standard',1),('cisco',2)))
_CwvlWlanEncryptionAlgorithm_Type.__name__=_H
_CwvlWlanEncryptionAlgorithm_Object=MibTableColumn
cwvlWlanEncryptionAlgorithm=_CwvlWlanEncryptionAlgorithm_Object((1,3,6,1,4,1,9,9,268,1,2,1,1,9),_CwvlWlanEncryptionAlgorithm_Type())
cwvlWlanEncryptionAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:cwvlWlanEncryptionAlgorithm.setStatus(_A)
_CwvlWlanRowStatus_Type=RowStatus
_CwvlWlanRowStatus_Object=MibTableColumn
cwvlWlanRowStatus=_CwvlWlanRowStatus_Object((1,3,6,1,4,1,9,9,268,1,2,1,1,10),_CwvlWlanRowStatus_Type())
cwvlWlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwvlWlanRowStatus.setStatus(_A)
_CwvlWlanNUcastKeyTable_Object=MibTable
cwvlWlanNUcastKeyTable=_CwvlWlanNUcastKeyTable_Object((1,3,6,1,4,1,9,9,268,1,2,2))
if mibBuilder.loadTexts:cwvlWlanNUcastKeyTable.setStatus(_A)
_CwvlWlanNUcastKeyEntry_Object=MibTableRow
cwvlWlanNUcastKeyEntry=_CwvlWlanNUcastKeyEntry_Object((1,3,6,1,4,1,9,9,268,1,2,2,1))
cwvlWlanNUcastKeyEntry.setIndexNames((0,_B,_I),(0,_B,_N))
if mibBuilder.loadTexts:cwvlWlanNUcastKeyEntry.setStatus(_A)
class _CwvlWlanNUcastKeyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CwvlWlanNUcastKeyIndex_Type.__name__=_F
_CwvlWlanNUcastKeyIndex_Object=MibTableColumn
cwvlWlanNUcastKeyIndex=_CwvlWlanNUcastKeyIndex_Object((1,3,6,1,4,1,9,9,268,1,2,2,1,1),_CwvlWlanNUcastKeyIndex_Type())
cwvlWlanNUcastKeyIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:cwvlWlanNUcastKeyIndex.setStatus(_A)
class _CwvlWlanNUcastKeyLen_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,13))
_CwvlWlanNUcastKeyLen_Type.__name__=_F
_CwvlWlanNUcastKeyLen_Object=MibTableColumn
cwvlWlanNUcastKeyLen=_CwvlWlanNUcastKeyLen_Object((1,3,6,1,4,1,9,9,268,1,2,2,1,2),_CwvlWlanNUcastKeyLen_Type())
cwvlWlanNUcastKeyLen.setMaxAccess(_D)
if mibBuilder.loadTexts:cwvlWlanNUcastKeyLen.setStatus(_A)
_CwvlWlanNUcastKeyValue_Type=WepKeyType128
_CwvlWlanNUcastKeyValue_Object=MibTableColumn
cwvlWlanNUcastKeyValue=_CwvlWlanNUcastKeyValue_Object((1,3,6,1,4,1,9,9,268,1,2,2,1,3),_CwvlWlanNUcastKeyValue_Type())
cwvlWlanNUcastKeyValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cwvlWlanNUcastKeyValue.setStatus(_A)
class _CwvlWlanWepChangeNotifEnabled_Type(TruthValue):defaultValue=2
_CwvlWlanWepChangeNotifEnabled_Type.__name__=_E
_CwvlWlanWepChangeNotifEnabled_Object=MibScalar
cwvlWlanWepChangeNotifEnabled=_CwvlWlanWepChangeNotifEnabled_Object((1,3,6,1,4,1,9,9,268,1,2,3),_CwvlWlanWepChangeNotifEnabled_Type())
cwvlWlanWepChangeNotifEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cwvlWlanWepChangeNotifEnabled.setStatus(_A)
_CiscoWlanVlanMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWlanVlanMIBConformance=_CiscoWlanVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,268,2))
_CiscoWlanVlanMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWlanVlanMIBCompliances=_CiscoWlanVlanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,268,2,1))
_CiscoWlanVlanMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWlanVlanMIBGroups=_CiscoWlanVlanMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,268,2,2))
ciscoWlanRoamDomainGroup=ObjectGroup((1,3,6,1,4,1,9,9,268,2,2,1))
ciscoWlanRoamDomainGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ciscoWlanRoamDomainGroup.setStatus(_A)
ciscoWlanDot11VlanConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,268,2,2,2))
ciscoWlanDot11VlanConfigGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_J),(_B,_d)))
if mibBuilder.loadTexts:ciscoWlanDot11VlanConfigGroup.setStatus(_A)
ciscoWlanVlanWepChangeNotif=NotificationType((1,3,6,1,4,1,9,9,268,0,1))
ciscoWlanVlanWepChangeNotif.setObjects((_B,_J))
if mibBuilder.loadTexts:ciscoWlanVlanWepChangeNotif.setStatus(_A)
ciscoWlanVlanNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,268,2,2,3))
ciscoWlanVlanNotificationGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:ciscoWlanVlanNotificationGroup.setStatus(_A)
ciscoWlanVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,268,2,1,1))
ciscoWlanVlanMIBCompliance.setObjects(*((_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ciscoWlanVlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_G:CwvlVlanIdOrZero,'ciscoWlanVlanMIB':ciscoWlanVlanMIB,'ciscoWlanVlanMIBNotifications':ciscoWlanVlanMIBNotifications,_e:ciscoWlanVlanWepChangeNotif,'ciscoWlanVlanMIBObjects':ciscoWlanVlanMIBObjects,'cwvlRoamDomainConfig':cwvlRoamDomainConfig,_O:cwvlWlanDot1qEncapEnabled,_P:cwvlBridgingNativeVlanId,_Q:cwvlVoIPVlanEnabled,_R:cwvlVoIPVlanId,_S:cwvlPublicVlanId,'cwvlDot11VlanConfig':cwvlDot11VlanConfig,'cwvlWlanVlanTable':cwvlWlanVlanTable,'cwvlWlanVlanEntry':cwvlWlanVlanEntry,_I:cwvlWlanVlanId,_T:cwvlWlanEnabled,_U:cwvlWlanNUcastKeyRotateInterval,_V:cwvlWlanEncryptionMode,_W:cwvlWlanEncryptionMandatory,_X:cwvlWlanMicAlgorithm,_Y:cwvlWlanWepKeyPermuteAlgorithm,_Z:cwvlWlanWepKeyHashing,_a:cwvlWlanEncryptionAlgorithm,_b:cwvlWlanRowStatus,'cwvlWlanNUcastKeyTable':cwvlWlanNUcastKeyTable,'cwvlWlanNUcastKeyEntry':cwvlWlanNUcastKeyEntry,_N:cwvlWlanNUcastKeyIndex,_c:cwvlWlanNUcastKeyLen,_J:cwvlWlanNUcastKeyValue,_d:cwvlWlanWepChangeNotifEnabled,'ciscoWlanVlanMIBConformance':ciscoWlanVlanMIBConformance,'ciscoWlanVlanMIBCompliances':ciscoWlanVlanMIBCompliances,'ciscoWlanVlanMIBCompliance':ciscoWlanVlanMIBCompliance,'ciscoWlanVlanMIBGroups':ciscoWlanVlanMIBGroups,_f:ciscoWlanRoamDomainGroup,_h:ciscoWlanDot11VlanConfigGroup,_g:ciscoWlanVlanNotificationGroup})