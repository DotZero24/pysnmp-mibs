_l='alaAutoFabricTrapsObjGroup'
_k='alaAutoFabricNotificationGroup'
_j='alaAutoFabricPortConfigGroup'
_i='alaAutoFabricBaseGroup'
_h='alaAutoFabricSTPModeChangeAlert'
_g='alaAutoFabricPortSPBDefaultProfile'
_f='alaAutoFabricPortStatus'
_e='alaAutoFabricPortMVRPProtocolStatus'
_d='alaAutoFabricPortSPBProtocolStatus'
_c='alaAutoFabricPortLACPProtocolStatus'
_b='alaAutoFabricPortConfigStatus'
_a='alaAutoFabricRemoveVCReload'
_Z='alaAutoFabricLBDProtocolStatus'
_Y='alaAutoFabricSPBDefaultProfile'
_X='alaAutoFabricGlobalISISProtocolStatus'
_W='alaAutoFabricGlobalOSPFv3ProtocolStatus'
_V='alaAutoFabricGlobalOSPFv2ProtocolStatus'
_U='alaAutoFabricRemoveGlobalConfig'
_T='alaAutoFabricGlobalDiscoveryTimer'
_S='alaAutoFabricGlobalConfigSaveTimerStatus'
_R='alaAutoFabricGlobalConfigSaveTimer'
_Q='alaAutoFabricGlobalMVRPProtocolStatus'
_P='alaAutoFabricGlobalSPBProtocolStatus'
_O='alaAutoFabricGlobalLACPProtocolStatus'
_N='alaAutoFabricGlobalDiscovery'
_M='alaAutoFabricGlobalStatus'
_L='autoVlan'
_K='singleService'
_J='alaAutoFabricPortConfigIfIndex'
_I='alaAutoFabricSTPMode'
_H='default'
_G='Unsigned32'
_F='disable'
_E='enable'
_D='read-write'
_C='Integer32'
_B='ALCATEL-ENT1-AUTO-FABRIC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1AutoFabric,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1AutoFabric')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1AUTOFABRICMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,75,1))
if mibBuilder.loadTexts:alcatelIND1AUTOFABRICMIB.setRevisions(('2012-11-25 00:00',))
_AlcatelIND1AUTOFABRICMIBNotifications_ObjectIdentity=ObjectIdentity
alcatelIND1AUTOFABRICMIBNotifications=_AlcatelIND1AUTOFABRICMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,75,1,0))
_AlcatelIND1AUTOFABRICMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1AUTOFABRICMIBObjects=_AlcatelIND1AUTOFABRICMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,75,1,1))
if mibBuilder.loadTexts:alcatelIND1AUTOFABRICMIBObjects.setStatus(_A)
class _AlaAutoFabricGlobalStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricGlobalStatus_Type.__name__=_C
_AlaAutoFabricGlobalStatus_Object=MibScalar
alaAutoFabricGlobalStatus=_AlaAutoFabricGlobalStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,1),_AlaAutoFabricGlobalStatus_Type())
alaAutoFabricGlobalStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricGlobalStatus.setStatus(_A)
class _AlaAutoFabricGlobalDiscovery_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('restart',2)))
_AlaAutoFabricGlobalDiscovery_Type.__name__=_C
_AlaAutoFabricGlobalDiscovery_Object=MibScalar
alaAutoFabricGlobalDiscovery=_AlaAutoFabricGlobalDiscovery_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,2),_AlaAutoFabricGlobalDiscovery_Type())
alaAutoFabricGlobalDiscovery.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricGlobalDiscovery.setStatus(_A)
class _AlaAutoFabricGlobalLACPProtocolStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricGlobalLACPProtocolStatus_Type.__name__=_C
_AlaAutoFabricGlobalLACPProtocolStatus_Object=MibScalar
alaAutoFabricGlobalLACPProtocolStatus=_AlaAutoFabricGlobalLACPProtocolStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,3),_AlaAutoFabricGlobalLACPProtocolStatus_Type())
alaAutoFabricGlobalLACPProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricGlobalLACPProtocolStatus.setStatus(_A)
class _AlaAutoFabricGlobalSPBProtocolStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricGlobalSPBProtocolStatus_Type.__name__=_C
_AlaAutoFabricGlobalSPBProtocolStatus_Object=MibScalar
alaAutoFabricGlobalSPBProtocolStatus=_AlaAutoFabricGlobalSPBProtocolStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,4),_AlaAutoFabricGlobalSPBProtocolStatus_Type())
alaAutoFabricGlobalSPBProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricGlobalSPBProtocolStatus.setStatus(_A)
class _AlaAutoFabricGlobalMVRPProtocolStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricGlobalMVRPProtocolStatus_Type.__name__=_C
_AlaAutoFabricGlobalMVRPProtocolStatus_Object=MibScalar
alaAutoFabricGlobalMVRPProtocolStatus=_AlaAutoFabricGlobalMVRPProtocolStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,5),_AlaAutoFabricGlobalMVRPProtocolStatus_Type())
alaAutoFabricGlobalMVRPProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricGlobalMVRPProtocolStatus.setStatus(_A)
class _AlaAutoFabricGlobalConfigSaveTimer_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_AlaAutoFabricGlobalConfigSaveTimer_Type.__name__=_G
_AlaAutoFabricGlobalConfigSaveTimer_Object=MibScalar
alaAutoFabricGlobalConfigSaveTimer=_AlaAutoFabricGlobalConfigSaveTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,6),_AlaAutoFabricGlobalConfigSaveTimer_Type())
alaAutoFabricGlobalConfigSaveTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricGlobalConfigSaveTimer.setStatus(_A)
if mibBuilder.loadTexts:alaAutoFabricGlobalConfigSaveTimer.setUnits('seconds')
class _AlaAutoFabricGlobalConfigSaveTimerStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricGlobalConfigSaveTimerStatus_Type.__name__=_C
_AlaAutoFabricGlobalConfigSaveTimerStatus_Object=MibScalar
alaAutoFabricGlobalConfigSaveTimerStatus=_AlaAutoFabricGlobalConfigSaveTimerStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,7),_AlaAutoFabricGlobalConfigSaveTimerStatus_Type())
alaAutoFabricGlobalConfigSaveTimerStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricGlobalConfigSaveTimerStatus.setStatus(_A)
class _AlaAutoFabricGlobalDiscoveryTimer_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_AlaAutoFabricGlobalDiscoveryTimer_Type.__name__=_G
_AlaAutoFabricGlobalDiscoveryTimer_Object=MibScalar
alaAutoFabricGlobalDiscoveryTimer=_AlaAutoFabricGlobalDiscoveryTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,8),_AlaAutoFabricGlobalDiscoveryTimer_Type())
alaAutoFabricGlobalDiscoveryTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricGlobalDiscoveryTimer.setStatus(_A)
if mibBuilder.loadTexts:alaAutoFabricGlobalDiscoveryTimer.setUnits('Minutes')
_AlaAutoFabricPortConfig_ObjectIdentity=ObjectIdentity
alaAutoFabricPortConfig=_AlaAutoFabricPortConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,9))
_AlaAutoFabricPortConfigTable_Object=MibTable
alaAutoFabricPortConfigTable=_AlaAutoFabricPortConfigTable_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,9,1))
if mibBuilder.loadTexts:alaAutoFabricPortConfigTable.setStatus(_A)
_AlaAutoFabricPortConfigEntry_Object=MibTableRow
alaAutoFabricPortConfigEntry=_AlaAutoFabricPortConfigEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,9,1,1))
alaAutoFabricPortConfigEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:alaAutoFabricPortConfigEntry.setStatus(_A)
_AlaAutoFabricPortConfigIfIndex_Type=InterfaceIndex
_AlaAutoFabricPortConfigIfIndex_Object=MibTableColumn
alaAutoFabricPortConfigIfIndex=_AlaAutoFabricPortConfigIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,9,1,1,1),_AlaAutoFabricPortConfigIfIndex_Type())
alaAutoFabricPortConfigIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:alaAutoFabricPortConfigIfIndex.setStatus(_A)
class _AlaAutoFabricPortConfigStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricPortConfigStatus_Type.__name__=_C
_AlaAutoFabricPortConfigStatus_Object=MibTableColumn
alaAutoFabricPortConfigStatus=_AlaAutoFabricPortConfigStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,9,1,1,2),_AlaAutoFabricPortConfigStatus_Type())
alaAutoFabricPortConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricPortConfigStatus.setStatus(_A)
class _AlaAutoFabricPortLACPProtocolStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricPortLACPProtocolStatus_Type.__name__=_C
_AlaAutoFabricPortLACPProtocolStatus_Object=MibTableColumn
alaAutoFabricPortLACPProtocolStatus=_AlaAutoFabricPortLACPProtocolStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,9,1,1,3),_AlaAutoFabricPortLACPProtocolStatus_Type())
alaAutoFabricPortLACPProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricPortLACPProtocolStatus.setStatus(_A)
class _AlaAutoFabricPortSPBProtocolStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricPortSPBProtocolStatus_Type.__name__=_C
_AlaAutoFabricPortSPBProtocolStatus_Object=MibTableColumn
alaAutoFabricPortSPBProtocolStatus=_AlaAutoFabricPortSPBProtocolStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,9,1,1,4),_AlaAutoFabricPortSPBProtocolStatus_Type())
alaAutoFabricPortSPBProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricPortSPBProtocolStatus.setStatus(_A)
class _AlaAutoFabricPortMVRPProtocolStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricPortMVRPProtocolStatus_Type.__name__=_C
_AlaAutoFabricPortMVRPProtocolStatus_Object=MibTableColumn
alaAutoFabricPortMVRPProtocolStatus=_AlaAutoFabricPortMVRPProtocolStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,9,1,1,5),_AlaAutoFabricPortMVRPProtocolStatus_Type())
alaAutoFabricPortMVRPProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricPortMVRPProtocolStatus.setStatus(_A)
class _AlaAutoFabricPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('pending',2),('complete',3)))
_AlaAutoFabricPortStatus_Type.__name__=_C
_AlaAutoFabricPortStatus_Object=MibTableColumn
alaAutoFabricPortStatus=_AlaAutoFabricPortStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,9,1,1,6),_AlaAutoFabricPortStatus_Type())
alaAutoFabricPortStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:alaAutoFabricPortStatus.setStatus(_A)
class _AlaAutoFabricPortSPBDefaultProfile_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AlaAutoFabricPortSPBDefaultProfile_Type.__name__=_C
_AlaAutoFabricPortSPBDefaultProfile_Object=MibTableColumn
alaAutoFabricPortSPBDefaultProfile=_AlaAutoFabricPortSPBDefaultProfile_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,9,1,1,7),_AlaAutoFabricPortSPBDefaultProfile_Type())
alaAutoFabricPortSPBDefaultProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricPortSPBDefaultProfile.setStatus(_A)
class _AlaAutoFabricRemoveGlobalConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('removeGlobalConfig',2)))
_AlaAutoFabricRemoveGlobalConfig_Type.__name__=_C
_AlaAutoFabricRemoveGlobalConfig_Object=MibScalar
alaAutoFabricRemoveGlobalConfig=_AlaAutoFabricRemoveGlobalConfig_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,10),_AlaAutoFabricRemoveGlobalConfig_Type())
alaAutoFabricRemoveGlobalConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricRemoveGlobalConfig.setStatus('deprecated')
class _AlaAutoFabricGlobalOSPFv2ProtocolStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricGlobalOSPFv2ProtocolStatus_Type.__name__=_C
_AlaAutoFabricGlobalOSPFv2ProtocolStatus_Object=MibScalar
alaAutoFabricGlobalOSPFv2ProtocolStatus=_AlaAutoFabricGlobalOSPFv2ProtocolStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,11),_AlaAutoFabricGlobalOSPFv2ProtocolStatus_Type())
alaAutoFabricGlobalOSPFv2ProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricGlobalOSPFv2ProtocolStatus.setStatus(_A)
class _AlaAutoFabricGlobalOSPFv3ProtocolStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricGlobalOSPFv3ProtocolStatus_Type.__name__=_C
_AlaAutoFabricGlobalOSPFv3ProtocolStatus_Object=MibScalar
alaAutoFabricGlobalOSPFv3ProtocolStatus=_AlaAutoFabricGlobalOSPFv3ProtocolStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,12),_AlaAutoFabricGlobalOSPFv3ProtocolStatus_Type())
alaAutoFabricGlobalOSPFv3ProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricGlobalOSPFv3ProtocolStatus.setStatus(_A)
class _AlaAutoFabricGlobalISISProtocolStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricGlobalISISProtocolStatus_Type.__name__=_C
_AlaAutoFabricGlobalISISProtocolStatus_Object=MibScalar
alaAutoFabricGlobalISISProtocolStatus=_AlaAutoFabricGlobalISISProtocolStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,13),_AlaAutoFabricGlobalISISProtocolStatus_Type())
alaAutoFabricGlobalISISProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricGlobalISISProtocolStatus.setStatus(_A)
class _AlaAutoFabricSPBDefaultProfile_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_AlaAutoFabricSPBDefaultProfile_Type.__name__=_C
_AlaAutoFabricSPBDefaultProfile_Object=MibScalar
alaAutoFabricSPBDefaultProfile=_AlaAutoFabricSPBDefaultProfile_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,14),_AlaAutoFabricSPBDefaultProfile_Type())
alaAutoFabricSPBDefaultProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricSPBDefaultProfile.setStatus(_A)
class _AlaAutoFabricLBDProtocolStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaAutoFabricLBDProtocolStatus_Type.__name__=_C
_AlaAutoFabricLBDProtocolStatus_Object=MibScalar
alaAutoFabricLBDProtocolStatus=_AlaAutoFabricLBDProtocolStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,15),_AlaAutoFabricLBDProtocolStatus_Type())
alaAutoFabricLBDProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricLBDProtocolStatus.setStatus(_A)
_AlaAutoFabricTrapsObj_ObjectIdentity=ObjectIdentity
alaAutoFabricTrapsObj=_AlaAutoFabricTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,16))
class _AlaAutoFabricSTPMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('flatMode',1),('perVlan',2)))
_AlaAutoFabricSTPMode_Type.__name__=_C
_AlaAutoFabricSTPMode_Object=MibScalar
alaAutoFabricSTPMode=_AlaAutoFabricSTPMode_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,16,1),_AlaAutoFabricSTPMode_Type())
alaAutoFabricSTPMode.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:alaAutoFabricSTPMode.setStatus(_A)
class _AlaAutoFabricRemoveVCReload_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('removeVCReload',2)))
_AlaAutoFabricRemoveVCReload_Type.__name__=_C
_AlaAutoFabricRemoveVCReload_Object=MibScalar
alaAutoFabricRemoveVCReload=_AlaAutoFabricRemoveVCReload_Object((1,3,6,1,4,1,6486,801,1,2,1,75,1,1,17),_AlaAutoFabricRemoveVCReload_Type())
alaAutoFabricRemoveVCReload.setMaxAccess(_D)
if mibBuilder.loadTexts:alaAutoFabricRemoveVCReload.setStatus(_A)
_AlcatelIND1AUTOFABRICMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1AUTOFABRICMIBConformance=_AlcatelIND1AUTOFABRICMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,75,1,2))
if mibBuilder.loadTexts:alcatelIND1AUTOFABRICMIBConformance.setStatus(_A)
_AlcatelIND1AUTOFABRICMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1AUTOFABRICMIBGroups=_AlcatelIND1AUTOFABRICMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,75,1,2,1))
if mibBuilder.loadTexts:alcatelIND1AUTOFABRICMIBGroups.setStatus(_A)
_AlcatelIND1AUTOFABRICMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1AUTOFABRICMIBCompliances=_AlcatelIND1AUTOFABRICMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,75,1,2,2))
if mibBuilder.loadTexts:alcatelIND1AUTOFABRICMIBCompliances.setStatus(_A)
alaAutoFabricBaseGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,75,1,2,1,1))
alaAutoFabricBaseGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:alaAutoFabricBaseGroup.setStatus(_A)
alaAutoFabricPortConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,75,1,2,1,2))
alaAutoFabricPortConfigGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:alaAutoFabricPortConfigGroup.setStatus(_A)
alaAutoFabricTrapsObjGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,75,1,2,1,4))
alaAutoFabricTrapsObjGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:alaAutoFabricTrapsObjGroup.setStatus(_A)
alaAutoFabricSTPModeChangeAlert=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,75,1,0,1))
alaAutoFabricSTPModeChangeAlert.setObjects((_B,_I))
if mibBuilder.loadTexts:alaAutoFabricSTPModeChangeAlert.setStatus(_A)
alaAutoFabricNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,75,1,2,1,3))
alaAutoFabricNotificationGroup.setObjects((_B,_h))
if mibBuilder.loadTexts:alaAutoFabricNotificationGroup.setStatus(_A)
alcatelIND1AUTOFABRICMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,75,1,2,2,1))
alcatelIND1AUTOFABRICMIBCompliance.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:alcatelIND1AUTOFABRICMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1AUTOFABRICMIB':alcatelIND1AUTOFABRICMIB,'alcatelIND1AUTOFABRICMIBNotifications':alcatelIND1AUTOFABRICMIBNotifications,_h:alaAutoFabricSTPModeChangeAlert,'alcatelIND1AUTOFABRICMIBObjects':alcatelIND1AUTOFABRICMIBObjects,_M:alaAutoFabricGlobalStatus,_N:alaAutoFabricGlobalDiscovery,_O:alaAutoFabricGlobalLACPProtocolStatus,_P:alaAutoFabricGlobalSPBProtocolStatus,_Q:alaAutoFabricGlobalMVRPProtocolStatus,_R:alaAutoFabricGlobalConfigSaveTimer,_S:alaAutoFabricGlobalConfigSaveTimerStatus,_T:alaAutoFabricGlobalDiscoveryTimer,'alaAutoFabricPortConfig':alaAutoFabricPortConfig,'alaAutoFabricPortConfigTable':alaAutoFabricPortConfigTable,'alaAutoFabricPortConfigEntry':alaAutoFabricPortConfigEntry,_J:alaAutoFabricPortConfigIfIndex,_b:alaAutoFabricPortConfigStatus,_c:alaAutoFabricPortLACPProtocolStatus,_d:alaAutoFabricPortSPBProtocolStatus,_e:alaAutoFabricPortMVRPProtocolStatus,_f:alaAutoFabricPortStatus,_g:alaAutoFabricPortSPBDefaultProfile,_U:alaAutoFabricRemoveGlobalConfig,_V:alaAutoFabricGlobalOSPFv2ProtocolStatus,_W:alaAutoFabricGlobalOSPFv3ProtocolStatus,_X:alaAutoFabricGlobalISISProtocolStatus,_Y:alaAutoFabricSPBDefaultProfile,_Z:alaAutoFabricLBDProtocolStatus,'alaAutoFabricTrapsObj':alaAutoFabricTrapsObj,_I:alaAutoFabricSTPMode,_a:alaAutoFabricRemoveVCReload,'alcatelIND1AUTOFABRICMIBConformance':alcatelIND1AUTOFABRICMIBConformance,'alcatelIND1AUTOFABRICMIBGroups':alcatelIND1AUTOFABRICMIBGroups,_i:alaAutoFabricBaseGroup,_j:alaAutoFabricPortConfigGroup,_k:alaAutoFabricNotificationGroup,_l:alaAutoFabricTrapsObjGroup,'alcatelIND1AUTOFABRICMIBCompliances':alcatelIND1AUTOFABRICMIBCompliances,'alcatelIND1AUTOFABRICMIBCompliance':alcatelIND1AUTOFABRICMIBCompliance})