_A0='ciscoTmsNotificationGroup'
_z='ciscoTmsThreatInterfaceGroup'
_y='ciscoTmsThreatActionGroup'
_x='ciscoTmsThreatGroup'
_w='ciscoTmsConsumerGroup'
_v='ciscoTmsMitigationActionFailed'
_u='ciscoTmsThreatStatusChange'
_t='ciscoTmsControllerUnreachable'
_s='ciscoTmsConsStateChange'
_r='ciThreatInterfaceMitigationApplied'
_q='ciTmsThreatTcdf'
_p='ciTmsThreatActiveTimeDuration'
_o='ciTmsThreatName'
_n='ciTmsThreatClass'
_m='ciTmsInActiveThreats'
_l='ciTmsActiveThreats'
_k='ciTmsGroupRowStatus'
_j='ciTmsGroupStorageType'
_i='ciTmsGroupNotifEnable'
_h='ciTmsConsStateChangeNotifEnable'
_g='ciTmsInterfaceMaxEntries'
_f='ciTmsThreatActionMaxEntries'
_e='ciTmsThreatsMaxEntries'
_d='ciTmsGroupsMaxEntries'
_c='ciTmsConsumerDeviceId'
_b='ciTmsThreatActionParamId'
_a='ciTmsThreatAction'
_Z='StorageType'
_Y='SnmpAdminString'
_X='ifIndex'
_W='IF-MIB'
_V='ciTmsThreatActionFailReason'
_U='ciTmsThreatActionParamValue'
_T='ciTmsThreatActionParamLength'
_S='ciTmsThreatActionParamType'
_R='ciTmsThreatPriority'
_Q='ciTmsThreatStatus'
_P='ciTmsThreatVer'
_O='ciTmsGroupConsumerRegStatus'
_N='ciTmsConsumerState'
_M='read-create'
_L='TruthValue'
_K='ciTmsThreatId'
_J='ciTmsThreatOwner'
_I='ciTmsControllerIp'
_H='ciTmsControllerIpType'
_G='ciTmsGroupId'
_F='not-accessible'
_E='read-write'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='CISCO-THREAT-MITIGATION-SERVICE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_W,_X)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Y)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus',_Z,'TextualConvention',_L)
ciscoThreatMitigationServiceMIB=ModuleIdentity((1,3,6,1,4,1,9,9,603))
if mibBuilder.loadTexts:ciscoThreatMitigationServiceMIB.setRevisions(('2007-01-09 00:00',))
class CTmsConsumerState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
class CTmsConsumerRegistrationStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notRegistered',1),('registrationRequestSent',2),('registered',3),('registrationFailed',4)))
class CTmsThreatStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('active',2),('inactive',3),('created',4),('pending',5),('activationFailed',6),('inactivationFailed',7),('deleted',8)))
class CTmsActionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('ignore',1),('aclDrop',2),('fpmDrop',3),('redirect',4),('police',5),('setIPDscp',6),('localException',7),('quarantine',8)))
class CTmsActionParamIdType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noParams',1),('cir',2),('bir',3),('be',4),('nexthop',5),('dscpVal',6),('vlanId',7)))
class CTmsActionParamType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unsigned',1),('networkAddress',2),('string',3)))
_CiscoTmsMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoTmsMIBNotifs=_CiscoTmsMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,603,0))
_CiscoTmsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoTmsMIBObjects=_CiscoTmsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,603,1))
_CiTmsConsumerGlobals_ObjectIdentity=ObjectIdentity
ciTmsConsumerGlobals=_CiTmsConsumerGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,603,1,1))
class _CiTmsActiveThreats_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiTmsActiveThreats_Type.__name__=_D
_CiTmsActiveThreats_Object=MibScalar
ciTmsActiveThreats=_CiTmsActiveThreats_Object((1,3,6,1,4,1,9,9,603,1,1,1),_CiTmsActiveThreats_Type())
ciTmsActiveThreats.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsActiveThreats.setStatus(_B)
class _CiTmsInActiveThreats_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiTmsInActiveThreats_Type.__name__=_D
_CiTmsInActiveThreats_Object=MibScalar
ciTmsInActiveThreats=_CiTmsInActiveThreats_Object((1,3,6,1,4,1,9,9,603,1,1,2),_CiTmsInActiveThreats_Type())
ciTmsInActiveThreats.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsInActiveThreats.setStatus(_B)
class _CiTmsConsumerDeviceId_Type(SnmpAdminString):defaultValue=OctetString('')
_CiTmsConsumerDeviceId_Type.__name__=_Y
_CiTmsConsumerDeviceId_Object=MibScalar
ciTmsConsumerDeviceId=_CiTmsConsumerDeviceId_Object((1,3,6,1,4,1,9,9,603,1,1,3),_CiTmsConsumerDeviceId_Type())
ciTmsConsumerDeviceId.setMaxAccess(_E)
if mibBuilder.loadTexts:ciTmsConsumerDeviceId.setStatus(_B)
class _CiTmsGroupsMaxEntries_Type(Unsigned32):defaultValue=32767;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiTmsGroupsMaxEntries_Type.__name__=_D
_CiTmsGroupsMaxEntries_Object=MibScalar
ciTmsGroupsMaxEntries=_CiTmsGroupsMaxEntries_Object((1,3,6,1,4,1,9,9,603,1,1,4),_CiTmsGroupsMaxEntries_Type())
ciTmsGroupsMaxEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:ciTmsGroupsMaxEntries.setStatus(_B)
class _CiTmsThreatsMaxEntries_Type(Unsigned32):defaultValue=65535;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiTmsThreatsMaxEntries_Type.__name__=_D
_CiTmsThreatsMaxEntries_Object=MibScalar
ciTmsThreatsMaxEntries=_CiTmsThreatsMaxEntries_Object((1,3,6,1,4,1,9,9,603,1,1,5),_CiTmsThreatsMaxEntries_Type())
ciTmsThreatsMaxEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:ciTmsThreatsMaxEntries.setStatus(_B)
class _CiTmsThreatActionMaxEntries_Type(Unsigned32):defaultValue=65535;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiTmsThreatActionMaxEntries_Type.__name__=_D
_CiTmsThreatActionMaxEntries_Object=MibScalar
ciTmsThreatActionMaxEntries=_CiTmsThreatActionMaxEntries_Object((1,3,6,1,4,1,9,9,603,1,1,6),_CiTmsThreatActionMaxEntries_Type())
ciTmsThreatActionMaxEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:ciTmsThreatActionMaxEntries.setStatus(_B)
class _CiTmsInterfaceMaxEntries_Type(Unsigned32):defaultValue=65535;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiTmsInterfaceMaxEntries_Type.__name__=_D
_CiTmsInterfaceMaxEntries_Object=MibScalar
ciTmsInterfaceMaxEntries=_CiTmsInterfaceMaxEntries_Object((1,3,6,1,4,1,9,9,603,1,1,7),_CiTmsInterfaceMaxEntries_Type())
ciTmsInterfaceMaxEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:ciTmsInterfaceMaxEntries.setStatus(_B)
_CiTmsConsumerState_Type=CTmsConsumerState
_CiTmsConsumerState_Object=MibScalar
ciTmsConsumerState=_CiTmsConsumerState_Object((1,3,6,1,4,1,9,9,603,1,1,8),_CiTmsConsumerState_Type())
ciTmsConsumerState.setMaxAccess(_E)
if mibBuilder.loadTexts:ciTmsConsumerState.setStatus(_B)
_CiTmsConsumerGroup_ObjectIdentity=ObjectIdentity
ciTmsConsumerGroup=_CiTmsConsumerGroup_ObjectIdentity((1,3,6,1,4,1,9,9,603,1,2))
_CiTmsGroupTable_Object=MibTable
ciTmsGroupTable=_CiTmsGroupTable_Object((1,3,6,1,4,1,9,9,603,1,2,1))
if mibBuilder.loadTexts:ciTmsGroupTable.setStatus(_B)
_CiTmsGroupEntry_Object=MibTableRow
ciTmsGroupEntry=_CiTmsGroupEntry_Object((1,3,6,1,4,1,9,9,603,1,2,1,1))
ciTmsGroupEntry.setIndexNames((0,_A,_G),(0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:ciTmsGroupEntry.setStatus(_B)
class _CiTmsGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CiTmsGroupId_Type.__name__=_D
_CiTmsGroupId_Object=MibTableColumn
ciTmsGroupId=_CiTmsGroupId_Object((1,3,6,1,4,1,9,9,603,1,2,1,1,1),_CiTmsGroupId_Type())
ciTmsGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:ciTmsGroupId.setStatus(_B)
_CiTmsControllerIpType_Type=InetAddressType
_CiTmsControllerIpType_Object=MibTableColumn
ciTmsControllerIpType=_CiTmsControllerIpType_Object((1,3,6,1,4,1,9,9,603,1,2,1,1,2),_CiTmsControllerIpType_Type())
ciTmsControllerIpType.setMaxAccess(_F)
if mibBuilder.loadTexts:ciTmsControllerIpType.setStatus(_B)
_CiTmsControllerIp_Type=InetAddress
_CiTmsControllerIp_Object=MibTableColumn
ciTmsControllerIp=_CiTmsControllerIp_Object((1,3,6,1,4,1,9,9,603,1,2,1,1,3),_CiTmsControllerIp_Type())
ciTmsControllerIp.setMaxAccess(_F)
if mibBuilder.loadTexts:ciTmsControllerIp.setStatus(_B)
_CiTmsGroupConsumerRegStatus_Type=CTmsConsumerRegistrationStatus
_CiTmsGroupConsumerRegStatus_Object=MibTableColumn
ciTmsGroupConsumerRegStatus=_CiTmsGroupConsumerRegStatus_Object((1,3,6,1,4,1,9,9,603,1,2,1,1,4),_CiTmsGroupConsumerRegStatus_Type())
ciTmsGroupConsumerRegStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsGroupConsumerRegStatus.setStatus(_B)
class _CiTmsGroupNotifEnable_Type(TruthValue):defaultValue=2
_CiTmsGroupNotifEnable_Type.__name__=_L
_CiTmsGroupNotifEnable_Object=MibTableColumn
ciTmsGroupNotifEnable=_CiTmsGroupNotifEnable_Object((1,3,6,1,4,1,9,9,603,1,2,1,1,5),_CiTmsGroupNotifEnable_Type())
ciTmsGroupNotifEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:ciTmsGroupNotifEnable.setStatus(_B)
class _CiTmsGroupStorageType_Type(StorageType):defaultValue=3
_CiTmsGroupStorageType_Type.__name__=_Z
_CiTmsGroupStorageType_Object=MibTableColumn
ciTmsGroupStorageType=_CiTmsGroupStorageType_Object((1,3,6,1,4,1,9,9,603,1,2,1,1,6),_CiTmsGroupStorageType_Type())
ciTmsGroupStorageType.setMaxAccess(_M)
if mibBuilder.loadTexts:ciTmsGroupStorageType.setStatus(_B)
_CiTmsGroupRowStatus_Type=RowStatus
_CiTmsGroupRowStatus_Object=MibTableColumn
ciTmsGroupRowStatus=_CiTmsGroupRowStatus_Object((1,3,6,1,4,1,9,9,603,1,2,1,1,7),_CiTmsGroupRowStatus_Type())
ciTmsGroupRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:ciTmsGroupRowStatus.setStatus(_B)
_CiTmsConsumerThreat_ObjectIdentity=ObjectIdentity
ciTmsConsumerThreat=_CiTmsConsumerThreat_ObjectIdentity((1,3,6,1,4,1,9,9,603,1,3))
_CiTmsThreatTable_Object=MibTable
ciTmsThreatTable=_CiTmsThreatTable_Object((1,3,6,1,4,1,9,9,603,1,3,1))
if mibBuilder.loadTexts:ciTmsThreatTable.setStatus(_B)
_CiTmsThreatEntry_Object=MibTableRow
ciTmsThreatEntry=_CiTmsThreatEntry_Object((1,3,6,1,4,1,9,9,603,1,3,1,1))
ciTmsThreatEntry.setIndexNames((0,_A,_J),(0,_A,_K),(0,_A,_G),(0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:ciTmsThreatEntry.setStatus(_B)
class _CiTmsThreatOwner_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CiTmsThreatOwner_Type.__name__=_D
_CiTmsThreatOwner_Object=MibTableColumn
ciTmsThreatOwner=_CiTmsThreatOwner_Object((1,3,6,1,4,1,9,9,603,1,3,1,1,1),_CiTmsThreatOwner_Type())
ciTmsThreatOwner.setMaxAccess(_F)
if mibBuilder.loadTexts:ciTmsThreatOwner.setStatus(_B)
class _CiTmsThreatId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiTmsThreatId_Type.__name__=_D
_CiTmsThreatId_Object=MibTableColumn
ciTmsThreatId=_CiTmsThreatId_Object((1,3,6,1,4,1,9,9,603,1,3,1,1,2),_CiTmsThreatId_Type())
ciTmsThreatId.setMaxAccess(_F)
if mibBuilder.loadTexts:ciTmsThreatId.setStatus(_B)
class _CiTmsThreatVer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiTmsThreatVer_Type.__name__=_D
_CiTmsThreatVer_Object=MibTableColumn
ciTmsThreatVer=_CiTmsThreatVer_Object((1,3,6,1,4,1,9,9,603,1,3,1,1,3),_CiTmsThreatVer_Type())
ciTmsThreatVer.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsThreatVer.setStatus(_B)
_CiTmsThreatStatus_Type=CTmsThreatStatus
_CiTmsThreatStatus_Object=MibTableColumn
ciTmsThreatStatus=_CiTmsThreatStatus_Object((1,3,6,1,4,1,9,9,603,1,3,1,1,4),_CiTmsThreatStatus_Type())
ciTmsThreatStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsThreatStatus.setStatus(_B)
_CiTmsThreatClass_Type=SnmpAdminString
_CiTmsThreatClass_Object=MibTableColumn
ciTmsThreatClass=_CiTmsThreatClass_Object((1,3,6,1,4,1,9,9,603,1,3,1,1,5),_CiTmsThreatClass_Type())
ciTmsThreatClass.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsThreatClass.setStatus(_B)
_CiTmsThreatName_Type=SnmpAdminString
_CiTmsThreatName_Object=MibTableColumn
ciTmsThreatName=_CiTmsThreatName_Object((1,3,6,1,4,1,9,9,603,1,3,1,1,6),_CiTmsThreatName_Type())
ciTmsThreatName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsThreatName.setStatus(_B)
_CiTmsThreatActiveTimeDuration_Type=DateAndTime
_CiTmsThreatActiveTimeDuration_Object=MibTableColumn
ciTmsThreatActiveTimeDuration=_CiTmsThreatActiveTimeDuration_Object((1,3,6,1,4,1,9,9,603,1,3,1,1,7),_CiTmsThreatActiveTimeDuration_Type())
ciTmsThreatActiveTimeDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsThreatActiveTimeDuration.setStatus(_B)
class _CiTmsThreatPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CiTmsThreatPriority_Type.__name__=_D
_CiTmsThreatPriority_Object=MibTableColumn
ciTmsThreatPriority=_CiTmsThreatPriority_Object((1,3,6,1,4,1,9,9,603,1,3,1,1,8),_CiTmsThreatPriority_Type())
ciTmsThreatPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsThreatPriority.setStatus(_B)
_CiTmsThreatTcdf_Type=SnmpAdminString
_CiTmsThreatTcdf_Object=MibTableColumn
ciTmsThreatTcdf=_CiTmsThreatTcdf_Object((1,3,6,1,4,1,9,9,603,1,3,1,1,9),_CiTmsThreatTcdf_Type())
ciTmsThreatTcdf.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsThreatTcdf.setStatus(_B)
_CiTmsThreatActionTable_Object=MibTable
ciTmsThreatActionTable=_CiTmsThreatActionTable_Object((1,3,6,1,4,1,9,9,603,1,3,2))
if mibBuilder.loadTexts:ciTmsThreatActionTable.setStatus(_B)
_CiTmsThreatActionEntry_Object=MibTableRow
ciTmsThreatActionEntry=_CiTmsThreatActionEntry_Object((1,3,6,1,4,1,9,9,603,1,3,2,1))
ciTmsThreatActionEntry.setIndexNames((0,_A,_J),(0,_A,_K),(0,_A,_G),(0,_A,_H),(0,_A,_I),(0,_A,_a),(0,_A,_b))
if mibBuilder.loadTexts:ciTmsThreatActionEntry.setStatus(_B)
_CiTmsThreatAction_Type=CTmsActionType
_CiTmsThreatAction_Object=MibTableColumn
ciTmsThreatAction=_CiTmsThreatAction_Object((1,3,6,1,4,1,9,9,603,1,3,2,1,1),_CiTmsThreatAction_Type())
ciTmsThreatAction.setMaxAccess(_F)
if mibBuilder.loadTexts:ciTmsThreatAction.setStatus(_B)
_CiTmsThreatActionParamId_Type=CTmsActionParamIdType
_CiTmsThreatActionParamId_Object=MibTableColumn
ciTmsThreatActionParamId=_CiTmsThreatActionParamId_Object((1,3,6,1,4,1,9,9,603,1,3,2,1,2),_CiTmsThreatActionParamId_Type())
ciTmsThreatActionParamId.setMaxAccess(_F)
if mibBuilder.loadTexts:ciTmsThreatActionParamId.setStatus(_B)
_CiTmsThreatActionParamType_Type=CTmsActionParamType
_CiTmsThreatActionParamType_Object=MibTableColumn
ciTmsThreatActionParamType=_CiTmsThreatActionParamType_Object((1,3,6,1,4,1,9,9,603,1,3,2,1,3),_CiTmsThreatActionParamType_Type())
ciTmsThreatActionParamType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsThreatActionParamType.setStatus(_B)
class _CiTmsThreatActionParamLength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CiTmsThreatActionParamLength_Type.__name__=_D
_CiTmsThreatActionParamLength_Object=MibTableColumn
ciTmsThreatActionParamLength=_CiTmsThreatActionParamLength_Object((1,3,6,1,4,1,9,9,603,1,3,2,1,4),_CiTmsThreatActionParamLength_Type())
ciTmsThreatActionParamLength.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsThreatActionParamLength.setStatus(_B)
_CiTmsThreatActionParamValue_Type=SnmpAdminString
_CiTmsThreatActionParamValue_Object=MibTableColumn
ciTmsThreatActionParamValue=_CiTmsThreatActionParamValue_Object((1,3,6,1,4,1,9,9,603,1,3,2,1,5),_CiTmsThreatActionParamValue_Type())
ciTmsThreatActionParamValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsThreatActionParamValue.setStatus(_B)
_CiTmsThreatActionFailReason_Type=SnmpAdminString
_CiTmsThreatActionFailReason_Object=MibTableColumn
ciTmsThreatActionFailReason=_CiTmsThreatActionFailReason_Object((1,3,6,1,4,1,9,9,603,1,3,2,1,6),_CiTmsThreatActionFailReason_Type())
ciTmsThreatActionFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:ciTmsThreatActionFailReason.setStatus(_B)
_CiTmsThreatInterfaceTable_Object=MibTable
ciTmsThreatInterfaceTable=_CiTmsThreatInterfaceTable_Object((1,3,6,1,4,1,9,9,603,1,3,3))
if mibBuilder.loadTexts:ciTmsThreatInterfaceTable.setStatus(_B)
_CiTmsThreatInterfaceEntry_Object=MibTableRow
ciTmsThreatInterfaceEntry=_CiTmsThreatInterfaceEntry_Object((1,3,6,1,4,1,9,9,603,1,3,3,1))
ciTmsThreatInterfaceEntry.setIndexNames((0,_A,_K),(0,_A,_J),(0,_A,_G),(0,_A,_H),(0,_A,_I),(0,_W,_X))
if mibBuilder.loadTexts:ciTmsThreatInterfaceEntry.setStatus(_B)
_CiThreatInterfaceMitigationApplied_Type=TruthValue
_CiThreatInterfaceMitigationApplied_Object=MibTableColumn
ciThreatInterfaceMitigationApplied=_CiThreatInterfaceMitigationApplied_Object((1,3,6,1,4,1,9,9,603,1,3,3,1,1),_CiThreatInterfaceMitigationApplied_Type())
ciThreatInterfaceMitigationApplied.setMaxAccess(_C)
if mibBuilder.loadTexts:ciThreatInterfaceMitigationApplied.setStatus(_B)
_CiTiTmsConsumerNotifs_ObjectIdentity=ObjectIdentity
ciTiTmsConsumerNotifs=_CiTiTmsConsumerNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,603,1,4))
class _CiTmsConsStateChangeNotifEnable_Type(TruthValue):defaultValue=2
_CiTmsConsStateChangeNotifEnable_Type.__name__=_L
_CiTmsConsStateChangeNotifEnable_Object=MibScalar
ciTmsConsStateChangeNotifEnable=_CiTmsConsStateChangeNotifEnable_Object((1,3,6,1,4,1,9,9,603,1,4,1),_CiTmsConsStateChangeNotifEnable_Type())
ciTmsConsStateChangeNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ciTmsConsStateChangeNotifEnable.setStatus(_B)
_CiscoTmsMIBConform_ObjectIdentity=ObjectIdentity
ciscoTmsMIBConform=_CiscoTmsMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,603,2))
_CiscoTmsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoTmsMIBCompliances=_CiscoTmsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,603,2,1))
_CiscoTmsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoTmsMIBGroups=_CiscoTmsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,603,2,2))
ciscoTmsConsumerGroup=ObjectGroup((1,3,6,1,4,1,9,9,603,2,2,1))
ciscoTmsConsumerGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_N),(_A,_h),(_A,_O),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:ciscoTmsConsumerGroup.setStatus(_B)
ciscoTmsThreatGroup=ObjectGroup((1,3,6,1,4,1,9,9,603,2,2,2))
ciscoTmsThreatGroup.setObjects(*((_A,_l),(_A,_m),(_A,_P),(_A,_Q),(_A,_n),(_A,_o),(_A,_p),(_A,_R),(_A,_q)))
if mibBuilder.loadTexts:ciscoTmsThreatGroup.setStatus(_B)
ciscoTmsThreatActionGroup=ObjectGroup((1,3,6,1,4,1,9,9,603,2,2,3))
ciscoTmsThreatActionGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ciscoTmsThreatActionGroup.setStatus(_B)
ciscoTmsThreatInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,9,603,2,2,4))
ciscoTmsThreatInterfaceGroup.setObjects((_A,_r))
if mibBuilder.loadTexts:ciscoTmsThreatInterfaceGroup.setStatus(_B)
ciscoTmsConsStateChange=NotificationType((1,3,6,1,4,1,9,9,603,0,1))
ciscoTmsConsStateChange.setObjects((_A,_N))
if mibBuilder.loadTexts:ciscoTmsConsStateChange.setStatus(_B)
ciscoTmsControllerUnreachable=NotificationType((1,3,6,1,4,1,9,9,603,0,2))
ciscoTmsControllerUnreachable.setObjects((_A,_O))
if mibBuilder.loadTexts:ciscoTmsControllerUnreachable.setStatus(_B)
ciscoTmsThreatStatusChange=NotificationType((1,3,6,1,4,1,9,9,603,0,3))
ciscoTmsThreatStatusChange.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:ciscoTmsThreatStatusChange.setStatus(_B)
ciscoTmsMitigationActionFailed=NotificationType((1,3,6,1,4,1,9,9,603,0,4))
ciscoTmsMitigationActionFailed.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ciscoTmsMitigationActionFailed.setStatus(_B)
ciscoTmsNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,603,2,2,5))
ciscoTmsNotificationGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:ciscoTmsNotificationGroup.setStatus(_B)
ciscoTmsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,603,2,1,1))
ciscoTmsMIBCompliance.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:ciscoTmsMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CTmsConsumerState':CTmsConsumerState,'CTmsConsumerRegistrationStatus':CTmsConsumerRegistrationStatus,'CTmsThreatStatus':CTmsThreatStatus,'CTmsActionType':CTmsActionType,'CTmsActionParamIdType':CTmsActionParamIdType,'CTmsActionParamType':CTmsActionParamType,'ciscoThreatMitigationServiceMIB':ciscoThreatMitigationServiceMIB,'ciscoTmsMIBNotifs':ciscoTmsMIBNotifs,_s:ciscoTmsConsStateChange,_t:ciscoTmsControllerUnreachable,_u:ciscoTmsThreatStatusChange,_v:ciscoTmsMitigationActionFailed,'ciscoTmsMIBObjects':ciscoTmsMIBObjects,'ciTmsConsumerGlobals':ciTmsConsumerGlobals,_l:ciTmsActiveThreats,_m:ciTmsInActiveThreats,_c:ciTmsConsumerDeviceId,_d:ciTmsGroupsMaxEntries,_e:ciTmsThreatsMaxEntries,_f:ciTmsThreatActionMaxEntries,_g:ciTmsInterfaceMaxEntries,_N:ciTmsConsumerState,'ciTmsConsumerGroup':ciTmsConsumerGroup,'ciTmsGroupTable':ciTmsGroupTable,'ciTmsGroupEntry':ciTmsGroupEntry,_G:ciTmsGroupId,_H:ciTmsControllerIpType,_I:ciTmsControllerIp,_O:ciTmsGroupConsumerRegStatus,_i:ciTmsGroupNotifEnable,_j:ciTmsGroupStorageType,_k:ciTmsGroupRowStatus,'ciTmsConsumerThreat':ciTmsConsumerThreat,'ciTmsThreatTable':ciTmsThreatTable,'ciTmsThreatEntry':ciTmsThreatEntry,_J:ciTmsThreatOwner,_K:ciTmsThreatId,_P:ciTmsThreatVer,_Q:ciTmsThreatStatus,_n:ciTmsThreatClass,_o:ciTmsThreatName,_p:ciTmsThreatActiveTimeDuration,_R:ciTmsThreatPriority,_q:ciTmsThreatTcdf,'ciTmsThreatActionTable':ciTmsThreatActionTable,'ciTmsThreatActionEntry':ciTmsThreatActionEntry,_a:ciTmsThreatAction,_b:ciTmsThreatActionParamId,_S:ciTmsThreatActionParamType,_T:ciTmsThreatActionParamLength,_U:ciTmsThreatActionParamValue,_V:ciTmsThreatActionFailReason,'ciTmsThreatInterfaceTable':ciTmsThreatInterfaceTable,'ciTmsThreatInterfaceEntry':ciTmsThreatInterfaceEntry,_r:ciThreatInterfaceMitigationApplied,'ciTiTmsConsumerNotifs':ciTiTmsConsumerNotifs,_h:ciTmsConsStateChangeNotifEnable,'ciscoTmsMIBConform':ciscoTmsMIBConform,'ciscoTmsMIBCompliances':ciscoTmsMIBCompliances,'ciscoTmsMIBCompliance':ciscoTmsMIBCompliance,'ciscoTmsMIBGroups':ciscoTmsMIBGroups,_w:ciscoTmsConsumerGroup,_x:ciscoTmsThreatGroup,_y:ciscoTmsThreatActionGroup,_z:ciscoTmsThreatInterfaceGroup,_A0:ciscoTmsNotificationGroup})