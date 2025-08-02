_B0='vcManagedStatusNotificationsGroup2'
_A_='vcManagedStatusNotificationsGroup'
_Az='vcProfileFcFabricMapGroup'
_Ay='vcProfileNetworkMapGroup'
_Ax='vcFcFabricVcPortMapGroup'
_Aw='vcEnetNetworkVcPortMapGroup'
_Av='vcProfileGroup'
_Au='vcEnetNetworkGroup'
_At='vcFcFabricGroup'
_As='vcPhysicalServerGroup'
_Ar='vcPortGroup'
_Aq='vcModuleGroup'
_Ap='vcEnclosureGroup'
_Ao='vcDomainGroup'
_An='vcProfileManagedStatusChanged'
_Am='vcPhysicalServerManagedStatusChanged'
_Al='vcEnclosureManagedStatusChanged'
_Ak='vcModuleManagedStatusChanged'
_Aj='vcFcFabricManagedStatusChanged'
_Ai='vcEnetNetworkManagedStatusChanged'
_Ah='vcDomainManagedStatusChanged'
_Ag='vcProfileManagedStatusChange'
_Af='vcPhysicalServerManagedStatusChange'
_Ae='vcEnclosureManagedStatusChange'
_Ad='vcModuleManagedStatusChange'
_Ac='vcFcFabricManagedStatusChange'
_Ab='vcEnetNetworkManagedStatusChange'
_Aa='vcDomainManagedStatusChange'
_AZ='vcProfileFcFabricMapFcFabricIndex'
_AY='vcProfileNetworkMapNetworkIndex'
_AX='vcProfileLogicalSerialNumber'
_AW='vcProfilePhysicalServerIndex'
_AV='vcEnetNetworkUplinkVlanId'
_AU='vcPhysicalServerLocation'
_AT='vcPhysicalServerEnclosureIndex'
_AS='vcPortPhysicalPortPointer'
_AR='vcPortContainerPointer'
_AQ='vcPortManagerAddress'
_AP='vcPortManagerAddressType'
_AO='vcPortManagedStatus'
_AN='vcPortType'
_AM='vcModuleAddressIpv6'
_AL='vcModuleID'
_AK='vcModuleAddress'
_AJ='vcModuleAddressType'
_AI='vcModuleLocation'
_AH='vcModuleEnclosurePointer'
_AG='vcModuleFwRev'
_AF='vcModulePartNumber'
_AE='vcModuleType'
_AD='vcEnclosureAddressIpv6'
_AC='vcEnclosureUUID'
_AB='vcEnclosureAddress'
_AA='vcEnclosureAddressType'
_A9='vcDomainPrimaryAddressIpv6'
_A8='vcDomainPrimaryAddress'
_A7='vcDomainPrimaryAddressType'
_A6='vcProfileFcFabricMapConnectionIndex'
_A5='vcProfileNetworkMapConnectionIndex'
_A4='vcDomainStackingLinkRendundancyStatusChange'
_A3='vcTestTrap'
_A2='vcCheckpointCompleted'
_A1='vcCheckpointTimeout'
_A0='vcProfileReasonCode'
_z='vcProfileCause'
_y='vcProfileRootCause'
_x='vcProfileName'
_w='vcEnetNetworkReasonCode'
_v='vcEnetNetworkCause'
_u='vcEnetNetworkRootCause'
_t='vcEnetNetworkName'
_s='vcFcFabricReasonCode'
_r='vcFcFabricCause'
_q='vcFcFabricRootCause'
_p='vcFcFabricName'
_o='vcPhysicalServerReasonCode'
_n='vcPhysicalServerCause'
_m='vcPhysicalServerRootCause'
_l='vcModuleReasonCode'
_k='vcModuleCause'
_j='vcModuleRootCause'
_i='vcEnclosureReasonCode'
_h='vcEnclosureCause'
_g='vcEnclosureRootCause'
_f='vcEnclosureName'
_e='vcDomainReasonCode'
_d='vcDomainCause'
_c='vcDomainRootCause'
_b='vcDomainStackingLinkRedundant'
_a='vcDomainLastCheckpointTime'
_Z='vcDomainName'
_Y='vcProfileFcFabricMapProfileIndex'
_X='vcProfileNetworkMapProfileIndex'
_W='vcFcFabricVcPortMapVcPortIndex'
_V='vcFcFabricVcPortMapFcFabricIndex'
_U='vcEnetNetworkVcPortMapVcPortIndex'
_T='vcEnetNetworkVcPortMapNetworkIndex'
_S='vcPortIndex'
_R='vcProfileManagedStatus'
_Q='vcEnetNetworkManagedStatus'
_P='vcFcFabricManagedStatus'
_O='vcPhysicalServerManagedStatus'
_N='vcModuleManagedStatus'
_M='vcEnclosureManagedStatus'
_L='vcDomainCheckpointValid'
_K='vcDomainManagedStatus'
_J='vcProfileIndex'
_I='vcFcFabricIndex'
_H='vcEnetNetworkIndex'
_G='vcPhysicalServerIndex'
_F='vcModuleIndex'
_E='vcEnclosureIndex'
_D='deprecated'
_C='read-only'
_B='current'
_A='HPVC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2','zeroDotZero')
DisplayString,PhysAddress,RowPointer,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention','TimeStamp','TruthValue')
TransportAddress,TransportAddressType=mibBuilder.importSymbols('TRANSPORT-ADDRESS-MIB','TransportAddress','TransportAddressType')
vcDomainMIB=ModuleIdentity((1,3,6,1,4,1,11,5,7,5,2,1))
if mibBuilder.loadTexts:vcDomainMIB.setRevisions(('2017-04-05 00:00','2017-02-28 00:00','2016-08-10 00:00','2016-03-21 00:00','2014-03-05 00:00','2013-10-25 00:00','2012-12-12 00:00','2012-06-27 00:00','2010-03-08 00:00','2009-06-27 00:00','2009-02-17 00:00','2009-01-08 00:00','2008-12-08 00:00'))
class VcManagedStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('normal',2),('warning',3),('minor',4),('major',5),('critical',6),('disabled',7),('info',8)))
class VcDomainModuleRole(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unintegrated',1),('primaryProtected',2),('primaryUnprotected',3),('standby',4),('other',5)))
class VcModuleType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vcModuleEnet',1),('vcModuleFC',2),('vcModuleOther',3)))
class VcPortType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vcEnetPhysicalPort',1),('vcEnetLogicallPort',2),('vcFCPort',3)))
class VcDomainReasonCodeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(700,701,702,703,706,707,709,712,713,714,715,801,802,803,901)));namedValues=NamedValues(*(('vcDomainOk',700),('vcDomainAbnormalEnclosuresAndProfiles',701),('vcDomainSomeEnclosuresAbnormal',702),('vcDomainUnmappedProfileConnections',703),('vcDomainStackingFailed',706),('vcDomainStackingNotRedundant',707),('vcDomainSomeProfilesAbnormal',709),('vcDomainUnknown',712),('vcDomainOverProvisioned',713),('vcDomainMixedTAA',714),('vcDomainInvalidPXEBootOrderProfileConnection',715),('vcDomainSflowIndirectlyDisabled',801),('vcDomainSflowFailed',802),('vcDomainSflowDegraded',803),('vcDomainPortMonitorIndirectlyDisabled',901)))
class VcEnclosureReasonCodeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(600,601,602,603,604,605,606,607)));namedValues=NamedValues(*(('vcEnclosureOk',600),('vcEnclosureAllEnetModulesFailed',601),('vcEnclosureSomeEnetModulesAbnormal',602),('vcEnclosureSomeModulesOrServersIncompatible',603),('vcEnclosureSomeFcModulesAbnormal',604),('vcEnclosureSomeServersAbnormal',605),('vcEnclosureUnknown',606),('vcEnclosureMixedTAAModules',607)))
class VcModuleReasonCodeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(400,401,402,404,405,406,407,408,409,410,412,413,414)));namedValues=NamedValues(*(('vcEnetmoduleOk',400),('vcEnetmoduleEnclosureDown',401),('vcEnetmoduleModuleMissing',402),('vcEnetmodulePortprotect',404),('vcEnetmoduleIncompatible',405),('vcEnetmoduleHwDegraded',406),('vcEnetmoduleUnknown',407),('vcFcmoduleOk',408),('vcFcmoduleEnclosureDown',409),('vcFcmoduleModuleMissing',410),('vcFcmoduleHwDegraded',412),('vcFcmoduleIncompatible',413),('vcFcmoduleUnknown',414)))
class VcPortReasonCodeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('vcEnetPortOK',1))
class VcPhysicalServerReasonCodeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(500,501,502,503,504)));namedValues=NamedValues(*(('vcPhysicalServerOk',500),('vcPhysicalServerEnclosureDown',501),('vcPhysicalServerFailed',502),('vcPhysicalServerDegraded',503),('vcPhysicalServerUnknown',504)))
class VcFcFabricReasonCodeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(200,202,203,204,205,206)));namedValues=NamedValues(*(('vcFabricOk',200),('vcFabricNoPortsConfigured',202),('vcFabricSomePortsAbnormal',203),('vcFabricAllPortsAbnormal',204),('vcFabricWwnMismatch',205),('vcFabricUnknown',206)))
class VcEnetNetworkReasonCodeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,101,102,104,105,106,109)));namedValues=NamedValues(*(('vcNetworkOk',100),('vcNetworkUnknown',101),('vcNetworkDisabled',102),('vcNetworkAbnormal',104),('vcNetworkFailed',105),('vcNetworkDegraded',106),('vcNetworkNoPortsAssignedToPrivateNetwork',109)))
class VcProfileReasonCodeType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(300,301,304,309,310,311,312,313,314,315,316,317)));namedValues=NamedValues(*(('vcProfileOk',300),('vcProfileServerAbnormal',301),('vcProfileAllConnectionsFailed',304),('vcProfileSomeConnectionsUnmapped',309),('vcProfileAllConnectionsAbnormal',310),('vcProfileSomeConnectionsAbnormal',311),('vcProfileUEFIBootmodeIncompatibleWithServer',312),('vcProfileUnknown',313),('vcProfileConnectionInvalidPXEBootOrder',314),('vcProfileConnectionDuplicateIscsiInitiatorIP',315),('vcProfileConnectionDuplicateIscsiInitiatorName',316),('vcProfileConnectionDuplicateIscsiInitiatorNameIP',317)))
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_HpSysMgt_ObjectIdentity=ObjectIdentity
hpSysMgt=_HpSysMgt_ObjectIdentity((1,3,6,1,4,1,11,5))
_HpEmbeddedServerMgt_ObjectIdentity=ObjectIdentity
hpEmbeddedServerMgt=_HpEmbeddedServerMgt_ObjectIdentity((1,3,6,1,4,1,11,5,7))
_HpModuleMgmtProc_ObjectIdentity=ObjectIdentity
hpModuleMgmtProc=_HpModuleMgmtProc_ObjectIdentity((1,3,6,1,4,1,11,5,7,5))
_VirtualConnect_ObjectIdentity=ObjectIdentity
virtualConnect=_VirtualConnect_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2))
_VcDomainMIBObjects_ObjectIdentity=ObjectIdentity
vcDomainMIBObjects=_VcDomainMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1))
_VcDomain_ObjectIdentity=ObjectIdentity
vcDomain=_VcDomain_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,1))
_VcDomainName_Type=SnmpAdminString
_VcDomainName_Object=MibScalar
vcDomainName=_VcDomainName_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,1,1),_VcDomainName_Type())
vcDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:vcDomainName.setStatus(_B)
_VcDomainManagedStatus_Type=VcManagedStatus
_VcDomainManagedStatus_Object=MibScalar
vcDomainManagedStatus=_VcDomainManagedStatus_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,1,2),_VcDomainManagedStatus_Type())
vcDomainManagedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vcDomainManagedStatus.setStatus(_B)
_VcDomainPrimaryAddressType_Type=TransportAddressType
_VcDomainPrimaryAddressType_Object=MibScalar
vcDomainPrimaryAddressType=_VcDomainPrimaryAddressType_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,1,3),_VcDomainPrimaryAddressType_Type())
vcDomainPrimaryAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:vcDomainPrimaryAddressType.setStatus(_B)
_VcDomainPrimaryAddress_Type=TransportAddress
_VcDomainPrimaryAddress_Object=MibScalar
vcDomainPrimaryAddress=_VcDomainPrimaryAddress_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,1,4),_VcDomainPrimaryAddress_Type())
vcDomainPrimaryAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vcDomainPrimaryAddress.setStatus(_B)
_VcDomainCheckpointValid_Type=TruthValue
_VcDomainCheckpointValid_Object=MibScalar
vcDomainCheckpointValid=_VcDomainCheckpointValid_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,1,5),_VcDomainCheckpointValid_Type())
vcDomainCheckpointValid.setMaxAccess(_C)
if mibBuilder.loadTexts:vcDomainCheckpointValid.setStatus(_B)
_VcDomainLastCheckpointTime_Type=SnmpAdminString
_VcDomainLastCheckpointTime_Object=MibScalar
vcDomainLastCheckpointTime=_VcDomainLastCheckpointTime_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,1,6),_VcDomainLastCheckpointTime_Type())
vcDomainLastCheckpointTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vcDomainLastCheckpointTime.setStatus(_B)
_VcDomainStackingLinkRedundant_Type=TruthValue
_VcDomainStackingLinkRedundant_Object=MibScalar
vcDomainStackingLinkRedundant=_VcDomainStackingLinkRedundant_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,1,7),_VcDomainStackingLinkRedundant_Type())
vcDomainStackingLinkRedundant.setMaxAccess(_C)
if mibBuilder.loadTexts:vcDomainStackingLinkRedundant.setStatus(_B)
_VcDomainRootCause_Type=SnmpAdminString
_VcDomainRootCause_Object=MibScalar
vcDomainRootCause=_VcDomainRootCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,1,8),_VcDomainRootCause_Type())
vcDomainRootCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcDomainRootCause.setStatus(_B)
_VcDomainCause_Type=SnmpAdminString
_VcDomainCause_Object=MibScalar
vcDomainCause=_VcDomainCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,1,9),_VcDomainCause_Type())
vcDomainCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcDomainCause.setStatus(_B)
_VcDomainReasonCode_Type=VcDomainReasonCodeType
_VcDomainReasonCode_Object=MibScalar
vcDomainReasonCode=_VcDomainReasonCode_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,1,10),_VcDomainReasonCode_Type())
vcDomainReasonCode.setMaxAccess(_C)
if mibBuilder.loadTexts:vcDomainReasonCode.setStatus(_B)
_VcDomainPrimaryAddressIpv6_Type=TransportAddress
_VcDomainPrimaryAddressIpv6_Object=MibScalar
vcDomainPrimaryAddressIpv6=_VcDomainPrimaryAddressIpv6_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,1,11),_VcDomainPrimaryAddressIpv6_Type())
vcDomainPrimaryAddressIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:vcDomainPrimaryAddressIpv6.setStatus(_B)
_VcEnclosure_ObjectIdentity=ObjectIdentity
vcEnclosure=_VcEnclosure_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,2))
_VcEnclosureTable_Object=MibTable
vcEnclosureTable=_VcEnclosureTable_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1))
if mibBuilder.loadTexts:vcEnclosureTable.setStatus(_B)
_VcEnclosureEntry_Object=MibTableRow
vcEnclosureEntry=_VcEnclosureEntry_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1,1))
vcEnclosureEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:vcEnclosureEntry.setStatus(_B)
_VcEnclosureIndex_Type=Integer32
_VcEnclosureIndex_Object=MibTableColumn
vcEnclosureIndex=_VcEnclosureIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1,1,1),_VcEnclosureIndex_Type())
vcEnclosureIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnclosureIndex.setStatus(_B)
_VcEnclosureName_Type=SnmpAdminString
_VcEnclosureName_Object=MibTableColumn
vcEnclosureName=_VcEnclosureName_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1,1,2),_VcEnclosureName_Type())
vcEnclosureName.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnclosureName.setStatus(_B)
_VcEnclosureManagedStatus_Type=VcManagedStatus
_VcEnclosureManagedStatus_Object=MibTableColumn
vcEnclosureManagedStatus=_VcEnclosureManagedStatus_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1,1,3),_VcEnclosureManagedStatus_Type())
vcEnclosureManagedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnclosureManagedStatus.setStatus(_B)
_VcEnclosureAddressType_Type=TransportAddressType
_VcEnclosureAddressType_Object=MibTableColumn
vcEnclosureAddressType=_VcEnclosureAddressType_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1,1,4),_VcEnclosureAddressType_Type())
vcEnclosureAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnclosureAddressType.setStatus(_B)
_VcEnclosureAddress_Type=TransportAddress
_VcEnclosureAddress_Object=MibTableColumn
vcEnclosureAddress=_VcEnclosureAddress_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1,1,5),_VcEnclosureAddress_Type())
vcEnclosureAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnclosureAddress.setStatus(_B)
_VcEnclosureUUID_Type=SnmpAdminString
_VcEnclosureUUID_Object=MibTableColumn
vcEnclosureUUID=_VcEnclosureUUID_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1,1,6),_VcEnclosureUUID_Type())
vcEnclosureUUID.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnclosureUUID.setStatus(_B)
_VcEnclosureRootCause_Type=SnmpAdminString
_VcEnclosureRootCause_Object=MibTableColumn
vcEnclosureRootCause=_VcEnclosureRootCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1,1,7),_VcEnclosureRootCause_Type())
vcEnclosureRootCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnclosureRootCause.setStatus(_B)
_VcEnclosureCause_Type=SnmpAdminString
_VcEnclosureCause_Object=MibTableColumn
vcEnclosureCause=_VcEnclosureCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1,1,8),_VcEnclosureCause_Type())
vcEnclosureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnclosureCause.setStatus(_B)
_VcEnclosureReasonCode_Type=VcEnclosureReasonCodeType
_VcEnclosureReasonCode_Object=MibTableColumn
vcEnclosureReasonCode=_VcEnclosureReasonCode_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1,1,9),_VcEnclosureReasonCode_Type())
vcEnclosureReasonCode.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnclosureReasonCode.setStatus(_B)
_VcEnclosureAddressIpv6_Type=TransportAddress
_VcEnclosureAddressIpv6_Object=MibTableColumn
vcEnclosureAddressIpv6=_VcEnclosureAddressIpv6_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,2,1,1,10),_VcEnclosureAddressIpv6_Type())
vcEnclosureAddressIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnclosureAddressIpv6.setStatus(_B)
_VcModule_ObjectIdentity=ObjectIdentity
vcModule=_VcModule_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,3))
_VcModuleTable_Object=MibTable
vcModuleTable=_VcModuleTable_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1))
if mibBuilder.loadTexts:vcModuleTable.setStatus(_B)
_VcModuleEntry_Object=MibTableRow
vcModuleEntry=_VcModuleEntry_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1))
vcModuleEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:vcModuleEntry.setStatus(_B)
_VcModuleIndex_Type=Integer32
_VcModuleIndex_Object=MibTableColumn
vcModuleIndex=_VcModuleIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,1),_VcModuleIndex_Type())
vcModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleIndex.setStatus(_B)
_VcModuleType_Type=VcModuleType
_VcModuleType_Object=MibTableColumn
vcModuleType=_VcModuleType_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,2),_VcModuleType_Type())
vcModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleType.setStatus(_B)
_VcModuleManagedStatus_Type=VcManagedStatus
_VcModuleManagedStatus_Object=MibTableColumn
vcModuleManagedStatus=_VcModuleManagedStatus_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,3),_VcModuleManagedStatus_Type())
vcModuleManagedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleManagedStatus.setStatus(_B)
_VcModulePartNumber_Type=SnmpAdminString
_VcModulePartNumber_Object=MibTableColumn
vcModulePartNumber=_VcModulePartNumber_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,4),_VcModulePartNumber_Type())
vcModulePartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModulePartNumber.setStatus(_B)
_VcModuleSerialNumber_Type=SnmpAdminString
_VcModuleSerialNumber_Object=MibTableColumn
vcModuleSerialNumber=_VcModuleSerialNumber_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,5),_VcModuleSerialNumber_Type())
vcModuleSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleSerialNumber.setStatus(_B)
_VcModuleProductName_Type=SnmpAdminString
_VcModuleProductName_Object=MibTableColumn
vcModuleProductName=_VcModuleProductName_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,6),_VcModuleProductName_Type())
vcModuleProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleProductName.setStatus(_B)
_VcModuleFwRev_Type=SnmpAdminString
_VcModuleFwRev_Object=MibTableColumn
vcModuleFwRev=_VcModuleFwRev_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,7),_VcModuleFwRev_Type())
vcModuleFwRev.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleFwRev.setStatus(_B)
_VcModuleEnclosurePointer_Type=RowPointer
_VcModuleEnclosurePointer_Object=MibTableColumn
vcModuleEnclosurePointer=_VcModuleEnclosurePointer_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,8),_VcModuleEnclosurePointer_Type())
vcModuleEnclosurePointer.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleEnclosurePointer.setStatus(_B)
_VcModuleLocation_Type=Unsigned32
_VcModuleLocation_Object=MibTableColumn
vcModuleLocation=_VcModuleLocation_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,9),_VcModuleLocation_Type())
vcModuleLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleLocation.setStatus(_B)
_VcModuleAddressType_Type=TransportAddressType
_VcModuleAddressType_Object=MibTableColumn
vcModuleAddressType=_VcModuleAddressType_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,10),_VcModuleAddressType_Type())
vcModuleAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleAddressType.setStatus(_B)
_VcModuleAddress_Type=TransportAddress
_VcModuleAddress_Object=MibTableColumn
vcModuleAddress=_VcModuleAddress_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,11),_VcModuleAddress_Type())
vcModuleAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleAddress.setStatus(_B)
_VcModuleID_Type=SnmpAdminString
_VcModuleID_Object=MibTableColumn
vcModuleID=_VcModuleID_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,12),_VcModuleID_Type())
vcModuleID.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleID.setStatus(_B)
_VcModuleRootCause_Type=SnmpAdminString
_VcModuleRootCause_Object=MibTableColumn
vcModuleRootCause=_VcModuleRootCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,13),_VcModuleRootCause_Type())
vcModuleRootCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleRootCause.setStatus(_B)
_VcModuleCause_Type=SnmpAdminString
_VcModuleCause_Object=MibTableColumn
vcModuleCause=_VcModuleCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,14),_VcModuleCause_Type())
vcModuleCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleCause.setStatus(_B)
_VcModuleReasonCode_Type=VcModuleReasonCodeType
_VcModuleReasonCode_Object=MibTableColumn
vcModuleReasonCode=_VcModuleReasonCode_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,15),_VcModuleReasonCode_Type())
vcModuleReasonCode.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleReasonCode.setStatus(_B)
_VcModuleAddressIpv6_Type=TransportAddress
_VcModuleAddressIpv6_Object=MibTableColumn
vcModuleAddressIpv6=_VcModuleAddressIpv6_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,3,1,1,16),_VcModuleAddressIpv6_Type())
vcModuleAddressIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:vcModuleAddressIpv6.setStatus(_B)
_VcPort_ObjectIdentity=ObjectIdentity
vcPort=_VcPort_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,4))
_VcPortTable_Object=MibTable
vcPortTable=_VcPortTable_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,4,1))
if mibBuilder.loadTexts:vcPortTable.setStatus(_B)
_VcPortEntry_Object=MibTableRow
vcPortEntry=_VcPortEntry_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,4,1,1))
vcPortEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:vcPortEntry.setStatus(_B)
_VcPortIndex_Type=Integer32
_VcPortIndex_Object=MibTableColumn
vcPortIndex=_VcPortIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,4,1,1,1),_VcPortIndex_Type())
vcPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPortIndex.setStatus(_B)
_VcPortType_Type=VcPortType
_VcPortType_Object=MibTableColumn
vcPortType=_VcPortType_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,4,1,1,2),_VcPortType_Type())
vcPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPortType.setStatus(_B)
_VcPortManagedStatus_Type=VcManagedStatus
_VcPortManagedStatus_Object=MibTableColumn
vcPortManagedStatus=_VcPortManagedStatus_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,4,1,1,3),_VcPortManagedStatus_Type())
vcPortManagedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPortManagedStatus.setStatus(_B)
_VcPortManagerAddressType_Type=TransportAddressType
_VcPortManagerAddressType_Object=MibTableColumn
vcPortManagerAddressType=_VcPortManagerAddressType_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,4,1,1,4),_VcPortManagerAddressType_Type())
vcPortManagerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPortManagerAddressType.setStatus(_B)
_VcPortManagerAddress_Type=TransportAddress
_VcPortManagerAddress_Object=MibTableColumn
vcPortManagerAddress=_VcPortManagerAddress_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,4,1,1,5),_VcPortManagerAddress_Type())
vcPortManagerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPortManagerAddress.setStatus(_B)
_VcPortPhysicalPortPointer_Type=RowPointer
_VcPortPhysicalPortPointer_Object=MibTableColumn
vcPortPhysicalPortPointer=_VcPortPhysicalPortPointer_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,4,1,1,6),_VcPortPhysicalPortPointer_Type())
vcPortPhysicalPortPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPortPhysicalPortPointer.setStatus(_B)
_VcPortContainerPointer_Type=RowPointer
_VcPortContainerPointer_Object=MibTableColumn
vcPortContainerPointer=_VcPortContainerPointer_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,4,1,1,7),_VcPortContainerPointer_Type())
vcPortContainerPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPortContainerPointer.setStatus(_B)
_VcPhysicalServer_ObjectIdentity=ObjectIdentity
vcPhysicalServer=_VcPhysicalServer_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,5))
_VcPhysicalServerTable_Object=MibTable
vcPhysicalServerTable=_VcPhysicalServerTable_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1))
if mibBuilder.loadTexts:vcPhysicalServerTable.setStatus(_B)
_VcPhysicalServerEntry_Object=MibTableRow
vcPhysicalServerEntry=_VcPhysicalServerEntry_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1,1))
vcPhysicalServerEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:vcPhysicalServerEntry.setStatus(_B)
_VcPhysicalServerIndex_Type=Integer32
_VcPhysicalServerIndex_Object=MibTableColumn
vcPhysicalServerIndex=_VcPhysicalServerIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1,1,1),_VcPhysicalServerIndex_Type())
vcPhysicalServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPhysicalServerIndex.setStatus(_B)
_VcPhysicalServerEnclosureIndex_Type=Integer32
_VcPhysicalServerEnclosureIndex_Object=MibTableColumn
vcPhysicalServerEnclosureIndex=_VcPhysicalServerEnclosureIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1,1,2),_VcPhysicalServerEnclosureIndex_Type())
vcPhysicalServerEnclosureIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPhysicalServerEnclosureIndex.setStatus(_B)
_VcPhysicalServerManagedStatus_Type=VcManagedStatus
_VcPhysicalServerManagedStatus_Object=MibTableColumn
vcPhysicalServerManagedStatus=_VcPhysicalServerManagedStatus_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1,1,3),_VcPhysicalServerManagedStatus_Type())
vcPhysicalServerManagedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPhysicalServerManagedStatus.setStatus(_B)
_VcPhysicalServerPartNumber_Type=SnmpAdminString
_VcPhysicalServerPartNumber_Object=MibTableColumn
vcPhysicalServerPartNumber=_VcPhysicalServerPartNumber_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1,1,4),_VcPhysicalServerPartNumber_Type())
vcPhysicalServerPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPhysicalServerPartNumber.setStatus(_B)
_VcPhysicalServerSerialNumber_Type=SnmpAdminString
_VcPhysicalServerSerialNumber_Object=MibTableColumn
vcPhysicalServerSerialNumber=_VcPhysicalServerSerialNumber_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1,1,5),_VcPhysicalServerSerialNumber_Type())
vcPhysicalServerSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPhysicalServerSerialNumber.setStatus(_B)
_VcPhysicalServerProductName_Type=SnmpAdminString
_VcPhysicalServerProductName_Object=MibTableColumn
vcPhysicalServerProductName=_VcPhysicalServerProductName_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1,1,6),_VcPhysicalServerProductName_Type())
vcPhysicalServerProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPhysicalServerProductName.setStatus(_B)
_VcPhysicalServerLocation_Type=Unsigned32
_VcPhysicalServerLocation_Object=MibTableColumn
vcPhysicalServerLocation=_VcPhysicalServerLocation_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1,1,7),_VcPhysicalServerLocation_Type())
vcPhysicalServerLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPhysicalServerLocation.setStatus(_B)
_VcPhysicalServerRootCause_Type=SnmpAdminString
_VcPhysicalServerRootCause_Object=MibTableColumn
vcPhysicalServerRootCause=_VcPhysicalServerRootCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1,1,8),_VcPhysicalServerRootCause_Type())
vcPhysicalServerRootCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPhysicalServerRootCause.setStatus(_B)
_VcPhysicalServerCause_Type=SnmpAdminString
_VcPhysicalServerCause_Object=MibTableColumn
vcPhysicalServerCause=_VcPhysicalServerCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1,1,9),_VcPhysicalServerCause_Type())
vcPhysicalServerCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPhysicalServerCause.setStatus(_B)
_VcPhysicalServerReasonCode_Type=VcPhysicalServerReasonCodeType
_VcPhysicalServerReasonCode_Object=MibTableColumn
vcPhysicalServerReasonCode=_VcPhysicalServerReasonCode_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,5,1,1,10),_VcPhysicalServerReasonCode_Type())
vcPhysicalServerReasonCode.setMaxAccess(_C)
if mibBuilder.loadTexts:vcPhysicalServerReasonCode.setStatus(_B)
_VcEnetNetwork_ObjectIdentity=ObjectIdentity
vcEnetNetwork=_VcEnetNetwork_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,6))
_VcEnetNetworkTable_Object=MibTable
vcEnetNetworkTable=_VcEnetNetworkTable_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,6,1))
if mibBuilder.loadTexts:vcEnetNetworkTable.setStatus(_B)
_VcEnetNetworkEntry_Object=MibTableRow
vcEnetNetworkEntry=_VcEnetNetworkEntry_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,6,1,1))
vcEnetNetworkEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:vcEnetNetworkEntry.setStatus(_B)
_VcEnetNetworkIndex_Type=Integer32
_VcEnetNetworkIndex_Object=MibTableColumn
vcEnetNetworkIndex=_VcEnetNetworkIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,6,1,1,1),_VcEnetNetworkIndex_Type())
vcEnetNetworkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnetNetworkIndex.setStatus(_B)
_VcEnetNetworkName_Type=SnmpAdminString
_VcEnetNetworkName_Object=MibTableColumn
vcEnetNetworkName=_VcEnetNetworkName_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,6,1,1,2),_VcEnetNetworkName_Type())
vcEnetNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnetNetworkName.setStatus(_B)
_VcEnetNetworkManagedStatus_Type=VcManagedStatus
_VcEnetNetworkManagedStatus_Object=MibTableColumn
vcEnetNetworkManagedStatus=_VcEnetNetworkManagedStatus_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,6,1,1,3),_VcEnetNetworkManagedStatus_Type())
vcEnetNetworkManagedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnetNetworkManagedStatus.setStatus(_B)
_VcEnetNetworkUplinkVlanId_Type=Unsigned32
_VcEnetNetworkUplinkVlanId_Object=MibTableColumn
vcEnetNetworkUplinkVlanId=_VcEnetNetworkUplinkVlanId_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,6,1,1,4),_VcEnetNetworkUplinkVlanId_Type())
vcEnetNetworkUplinkVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnetNetworkUplinkVlanId.setStatus(_B)
_VcEnetNetworkRootCause_Type=SnmpAdminString
_VcEnetNetworkRootCause_Object=MibTableColumn
vcEnetNetworkRootCause=_VcEnetNetworkRootCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,6,1,1,5),_VcEnetNetworkRootCause_Type())
vcEnetNetworkRootCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnetNetworkRootCause.setStatus(_B)
_VcEnetNetworkCause_Type=SnmpAdminString
_VcEnetNetworkCause_Object=MibTableColumn
vcEnetNetworkCause=_VcEnetNetworkCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,6,1,1,6),_VcEnetNetworkCause_Type())
vcEnetNetworkCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnetNetworkCause.setStatus(_B)
_VcEnetNetworkReasonCode_Type=VcEnetNetworkReasonCodeType
_VcEnetNetworkReasonCode_Object=MibTableColumn
vcEnetNetworkReasonCode=_VcEnetNetworkReasonCode_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,6,1,1,7),_VcEnetNetworkReasonCode_Type())
vcEnetNetworkReasonCode.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnetNetworkReasonCode.setStatus(_B)
_VcFcFabric_ObjectIdentity=ObjectIdentity
vcFcFabric=_VcFcFabric_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,7))
_VcFcFabricTable_Object=MibTable
vcFcFabricTable=_VcFcFabricTable_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,7,1))
if mibBuilder.loadTexts:vcFcFabricTable.setStatus(_B)
_VcFcFabricEntry_Object=MibTableRow
vcFcFabricEntry=_VcFcFabricEntry_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,7,1,1))
vcFcFabricEntry.setIndexNames((0,_A,_I))
if mibBuilder.loadTexts:vcFcFabricEntry.setStatus(_B)
_VcFcFabricIndex_Type=Integer32
_VcFcFabricIndex_Object=MibTableColumn
vcFcFabricIndex=_VcFcFabricIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,7,1,1,1),_VcFcFabricIndex_Type())
vcFcFabricIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcFcFabricIndex.setStatus(_B)
_VcFcFabricName_Type=SnmpAdminString
_VcFcFabricName_Object=MibTableColumn
vcFcFabricName=_VcFcFabricName_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,7,1,1,2),_VcFcFabricName_Type())
vcFcFabricName.setMaxAccess(_C)
if mibBuilder.loadTexts:vcFcFabricName.setStatus(_B)
_VcFcFabricManagedStatus_Type=VcManagedStatus
_VcFcFabricManagedStatus_Object=MibTableColumn
vcFcFabricManagedStatus=_VcFcFabricManagedStatus_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,7,1,1,3),_VcFcFabricManagedStatus_Type())
vcFcFabricManagedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vcFcFabricManagedStatus.setStatus(_B)
_VcFcFabricRootCause_Type=SnmpAdminString
_VcFcFabricRootCause_Object=MibTableColumn
vcFcFabricRootCause=_VcFcFabricRootCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,7,1,1,4),_VcFcFabricRootCause_Type())
vcFcFabricRootCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcFcFabricRootCause.setStatus(_B)
_VcFcFabricCause_Type=SnmpAdminString
_VcFcFabricCause_Object=MibTableColumn
vcFcFabricCause=_VcFcFabricCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,7,1,1,5),_VcFcFabricCause_Type())
vcFcFabricCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcFcFabricCause.setStatus(_B)
_VcFcFabricReasonCode_Type=VcFcFabricReasonCodeType
_VcFcFabricReasonCode_Object=MibTableColumn
vcFcFabricReasonCode=_VcFcFabricReasonCode_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,7,1,1,6),_VcFcFabricReasonCode_Type())
vcFcFabricReasonCode.setMaxAccess(_C)
if mibBuilder.loadTexts:vcFcFabricReasonCode.setStatus(_B)
_VcProfile_ObjectIdentity=ObjectIdentity
vcProfile=_VcProfile_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,8))
_VcProfileTable_Object=MibTable
vcProfileTable=_VcProfileTable_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,8,1))
if mibBuilder.loadTexts:vcProfileTable.setStatus(_B)
_VcProfileEntry_Object=MibTableRow
vcProfileEntry=_VcProfileEntry_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,8,1,1))
vcProfileEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:vcProfileEntry.setStatus(_B)
_VcProfileIndex_Type=Integer32
_VcProfileIndex_Object=MibTableColumn
vcProfileIndex=_VcProfileIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,8,1,1,1),_VcProfileIndex_Type())
vcProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileIndex.setStatus(_B)
_VcProfileName_Type=SnmpAdminString
_VcProfileName_Object=MibTableColumn
vcProfileName=_VcProfileName_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,8,1,1,2),_VcProfileName_Type())
vcProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileName.setStatus(_B)
_VcProfileManagedStatus_Type=VcManagedStatus
_VcProfileManagedStatus_Object=MibTableColumn
vcProfileManagedStatus=_VcProfileManagedStatus_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,8,1,1,3),_VcProfileManagedStatus_Type())
vcProfileManagedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileManagedStatus.setStatus(_B)
_VcProfilePhysicalServerIndex_Type=Unsigned32
_VcProfilePhysicalServerIndex_Object=MibTableColumn
vcProfilePhysicalServerIndex=_VcProfilePhysicalServerIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,8,1,1,4),_VcProfilePhysicalServerIndex_Type())
vcProfilePhysicalServerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfilePhysicalServerIndex.setStatus(_B)
_VcProfileLogicalSerialNumber_Type=SnmpAdminString
_VcProfileLogicalSerialNumber_Object=MibTableColumn
vcProfileLogicalSerialNumber=_VcProfileLogicalSerialNumber_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,8,1,1,5),_VcProfileLogicalSerialNumber_Type())
vcProfileLogicalSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileLogicalSerialNumber.setStatus(_B)
_VcProfileRootCause_Type=SnmpAdminString
_VcProfileRootCause_Object=MibTableColumn
vcProfileRootCause=_VcProfileRootCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,8,1,1,6),_VcProfileRootCause_Type())
vcProfileRootCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileRootCause.setStatus(_B)
_VcProfileCause_Type=SnmpAdminString
_VcProfileCause_Object=MibTableColumn
vcProfileCause=_VcProfileCause_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,8,1,1,7),_VcProfileCause_Type())
vcProfileCause.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileCause.setStatus(_B)
_VcProfileReasonCode_Type=VcProfileReasonCodeType
_VcProfileReasonCode_Object=MibTableColumn
vcProfileReasonCode=_VcProfileReasonCode_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,8,1,1,8),_VcProfileReasonCode_Type())
vcProfileReasonCode.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileReasonCode.setStatus(_B)
_VcEnetNetworkVcPortMap_ObjectIdentity=ObjectIdentity
vcEnetNetworkVcPortMap=_VcEnetNetworkVcPortMap_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,9))
_VcEnetNetworkVcPortMapTable_Object=MibTable
vcEnetNetworkVcPortMapTable=_VcEnetNetworkVcPortMapTable_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,9,1))
if mibBuilder.loadTexts:vcEnetNetworkVcPortMapTable.setStatus(_B)
_VcEnetNetworkVcPortMapEntry_Object=MibTableRow
vcEnetNetworkVcPortMapEntry=_VcEnetNetworkVcPortMapEntry_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,9,1,1))
vcEnetNetworkVcPortMapEntry.setIndexNames((0,_A,_T),(0,_A,_U))
if mibBuilder.loadTexts:vcEnetNetworkVcPortMapEntry.setStatus(_B)
_VcEnetNetworkVcPortMapNetworkIndex_Type=Integer32
_VcEnetNetworkVcPortMapNetworkIndex_Object=MibTableColumn
vcEnetNetworkVcPortMapNetworkIndex=_VcEnetNetworkVcPortMapNetworkIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,9,1,1,1),_VcEnetNetworkVcPortMapNetworkIndex_Type())
vcEnetNetworkVcPortMapNetworkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnetNetworkVcPortMapNetworkIndex.setStatus(_B)
_VcEnetNetworkVcPortMapVcPortIndex_Type=Integer32
_VcEnetNetworkVcPortMapVcPortIndex_Object=MibTableColumn
vcEnetNetworkVcPortMapVcPortIndex=_VcEnetNetworkVcPortMapVcPortIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,9,1,1,2),_VcEnetNetworkVcPortMapVcPortIndex_Type())
vcEnetNetworkVcPortMapVcPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcEnetNetworkVcPortMapVcPortIndex.setStatus(_B)
_VcFcFabricVcPortMap_ObjectIdentity=ObjectIdentity
vcFcFabricVcPortMap=_VcFcFabricVcPortMap_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,10))
_VcFcFabricVcPortMapTable_Object=MibTable
vcFcFabricVcPortMapTable=_VcFcFabricVcPortMapTable_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,10,1))
if mibBuilder.loadTexts:vcFcFabricVcPortMapTable.setStatus(_B)
_VcFcFabricVcPortMapEntry_Object=MibTableRow
vcFcFabricVcPortMapEntry=_VcFcFabricVcPortMapEntry_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,10,1,1))
vcFcFabricVcPortMapEntry.setIndexNames((0,_A,_V),(0,_A,_W))
if mibBuilder.loadTexts:vcFcFabricVcPortMapEntry.setStatus(_B)
_VcFcFabricVcPortMapFcFabricIndex_Type=Integer32
_VcFcFabricVcPortMapFcFabricIndex_Object=MibTableColumn
vcFcFabricVcPortMapFcFabricIndex=_VcFcFabricVcPortMapFcFabricIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,10,1,1,1),_VcFcFabricVcPortMapFcFabricIndex_Type())
vcFcFabricVcPortMapFcFabricIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcFcFabricVcPortMapFcFabricIndex.setStatus(_B)
_VcFcFabricVcPortMapVcPortIndex_Type=Integer32
_VcFcFabricVcPortMapVcPortIndex_Object=MibTableColumn
vcFcFabricVcPortMapVcPortIndex=_VcFcFabricVcPortMapVcPortIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,10,1,1,2),_VcFcFabricVcPortMapVcPortIndex_Type())
vcFcFabricVcPortMapVcPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcFcFabricVcPortMapVcPortIndex.setStatus(_B)
_VcProfileNetworkMap_ObjectIdentity=ObjectIdentity
vcProfileNetworkMap=_VcProfileNetworkMap_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,11))
_VcProfileNetworkMapTable_Object=MibTable
vcProfileNetworkMapTable=_VcProfileNetworkMapTable_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,11,1))
if mibBuilder.loadTexts:vcProfileNetworkMapTable.setStatus(_B)
_VcProfileNetworkMapEntry_Object=MibTableRow
vcProfileNetworkMapEntry=_VcProfileNetworkMapEntry_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,11,1,1))
vcProfileNetworkMapEntry.setIndexNames((0,_A,_X),(0,_A,_A5))
if mibBuilder.loadTexts:vcProfileNetworkMapEntry.setStatus(_B)
_VcProfileNetworkMapProfileIndex_Type=Integer32
_VcProfileNetworkMapProfileIndex_Object=MibTableColumn
vcProfileNetworkMapProfileIndex=_VcProfileNetworkMapProfileIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,11,1,1,1),_VcProfileNetworkMapProfileIndex_Type())
vcProfileNetworkMapProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileNetworkMapProfileIndex.setStatus(_B)
_VcProfileNetworkMapConnectionIndex_Type=Integer32
_VcProfileNetworkMapConnectionIndex_Object=MibTableColumn
vcProfileNetworkMapConnectionIndex=_VcProfileNetworkMapConnectionIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,11,1,1,2),_VcProfileNetworkMapConnectionIndex_Type())
vcProfileNetworkMapConnectionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileNetworkMapConnectionIndex.setStatus(_B)
_VcProfileNetworkMapNetworkIndex_Type=Integer32
_VcProfileNetworkMapNetworkIndex_Object=MibTableColumn
vcProfileNetworkMapNetworkIndex=_VcProfileNetworkMapNetworkIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,11,1,1,3),_VcProfileNetworkMapNetworkIndex_Type())
vcProfileNetworkMapNetworkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileNetworkMapNetworkIndex.setStatus(_B)
_VcProfileFcFabricMap_ObjectIdentity=ObjectIdentity
vcProfileFcFabricMap=_VcProfileFcFabricMap_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,1,12))
_VcProfileFcFabricMapTable_Object=MibTable
vcProfileFcFabricMapTable=_VcProfileFcFabricMapTable_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,12,1))
if mibBuilder.loadTexts:vcProfileFcFabricMapTable.setStatus(_B)
_VcProfileFcFabricMapEntry_Object=MibTableRow
vcProfileFcFabricMapEntry=_VcProfileFcFabricMapEntry_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,12,1,1))
vcProfileFcFabricMapEntry.setIndexNames((0,_A,_Y),(0,_A,_A6))
if mibBuilder.loadTexts:vcProfileFcFabricMapEntry.setStatus(_B)
_VcProfileFcFabricMapProfileIndex_Type=Integer32
_VcProfileFcFabricMapProfileIndex_Object=MibTableColumn
vcProfileFcFabricMapProfileIndex=_VcProfileFcFabricMapProfileIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,12,1,1,1),_VcProfileFcFabricMapProfileIndex_Type())
vcProfileFcFabricMapProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileFcFabricMapProfileIndex.setStatus(_B)
_VcProfileFcFabricMapConnectionIndex_Type=Integer32
_VcProfileFcFabricMapConnectionIndex_Object=MibTableColumn
vcProfileFcFabricMapConnectionIndex=_VcProfileFcFabricMapConnectionIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,12,1,1,2),_VcProfileFcFabricMapConnectionIndex_Type())
vcProfileFcFabricMapConnectionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileFcFabricMapConnectionIndex.setStatus(_B)
_VcProfileFcFabricMapFcFabricIndex_Type=Integer32
_VcProfileFcFabricMapFcFabricIndex_Object=MibTableColumn
vcProfileFcFabricMapFcFabricIndex=_VcProfileFcFabricMapFcFabricIndex_Object((1,3,6,1,4,1,11,5,7,5,2,1,1,12,1,1,3),_VcProfileFcFabricMapFcFabricIndex_Type())
vcProfileFcFabricMapFcFabricIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:vcProfileFcFabricMapFcFabricIndex.setStatus(_B)
_VcDomainMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
vcDomainMIBNotificationPrefix=_VcDomainMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,2))
_VcDomainMIBNotifications_ObjectIdentity=ObjectIdentity
vcDomainMIBNotifications=_VcDomainMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,2,0))
_VcDomainMIBNotificationObjects_ObjectIdentity=ObjectIdentity
vcDomainMIBNotificationObjects=_VcDomainMIBNotificationObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,2,1))
_VcDomainMIBConformance_ObjectIdentity=ObjectIdentity
vcDomainMIBConformance=_VcDomainMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,3))
_VcDomainMIBCompliances_ObjectIdentity=ObjectIdentity
vcDomainMIBCompliances=_VcDomainMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,3,1))
_VcDomainMIBGroups_ObjectIdentity=ObjectIdentity
vcDomainMIBGroups=_VcDomainMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,1,3,2))
vcDomainGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,1))
vcDomainGroup.setObjects(*((_A,_Z),(_A,_K),(_A,_A7),(_A,_A8),(_A,_L),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_A9)))
if mibBuilder.loadTexts:vcDomainGroup.setStatus(_B)
vcEnclosureGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,2))
vcEnclosureGroup.setObjects(*((_A,_E),(_A,_f),(_A,_M),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_g),(_A,_h),(_A,_i),(_A,_AD)))
if mibBuilder.loadTexts:vcEnclosureGroup.setStatus(_B)
vcModuleGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,3))
vcModuleGroup.setObjects(*((_A,_F),(_A,_AE),(_A,_N),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_j),(_A,_k),(_A,_l),(_A,_AM)))
if mibBuilder.loadTexts:vcModuleGroup.setStatus(_B)
vcPortGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,4))
vcPortGroup.setObjects(*((_A,_S),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:vcPortGroup.setStatus(_B)
vcPhysicalServerGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,5))
vcPhysicalServerGroup.setObjects(*((_A,_G),(_A,_AT),(_A,_O),(_A,_AU),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:vcPhysicalServerGroup.setStatus(_B)
vcFcFabricGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,6))
vcFcFabricGroup.setObjects(*((_A,_I),(_A,_p),(_A,_P),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:vcFcFabricGroup.setStatus(_B)
vcEnetNetworkGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,7))
vcEnetNetworkGroup.setObjects(*((_A,_H),(_A,_t),(_A,_Q),(_A,_AV),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:vcEnetNetworkGroup.setStatus(_B)
vcProfileGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,8))
vcProfileGroup.setObjects(*((_A,_J),(_A,_x),(_A,_R),(_A,_AW),(_A,_AX),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:vcProfileGroup.setStatus(_B)
vcEnetNetworkVcPortMapGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,9))
vcEnetNetworkVcPortMapGroup.setObjects(*((_A,_T),(_A,_U)))
if mibBuilder.loadTexts:vcEnetNetworkVcPortMapGroup.setStatus(_B)
vcFcFabricVcPortMapGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,10))
vcFcFabricVcPortMapGroup.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:vcFcFabricVcPortMapGroup.setStatus(_B)
vcProfileNetworkMapGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,11))
vcProfileNetworkMapGroup.setObjects(*((_A,_X),(_A,_AY)))
if mibBuilder.loadTexts:vcProfileNetworkMapGroup.setStatus(_B)
vcProfileFcFabricMapGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,12))
vcProfileFcFabricMapGroup.setObjects(*((_A,_Y),(_A,_AZ)))
if mibBuilder.loadTexts:vcProfileFcFabricMapGroup.setStatus(_B)
vcDomainManagedStatusChange=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,1))
vcDomainManagedStatusChange.setObjects((_A,_K))
if mibBuilder.loadTexts:vcDomainManagedStatusChange.setStatus(_D)
vcCheckpointTimeout=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,2))
vcCheckpointTimeout.setObjects(*((_A,_L),(_A,_a)))
if mibBuilder.loadTexts:vcCheckpointTimeout.setStatus(_B)
vcCheckpointCompleted=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,3))
vcCheckpointCompleted.setObjects((_A,_L))
if mibBuilder.loadTexts:vcCheckpointCompleted.setStatus(_B)
vcEnetNetworkManagedStatusChange=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,4))
vcEnetNetworkManagedStatusChange.setObjects(*((_A,_Q),(_A,_H)))
if mibBuilder.loadTexts:vcEnetNetworkManagedStatusChange.setStatus(_D)
vcFcFabricManagedStatusChange=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,5))
vcFcFabricManagedStatusChange.setObjects(*((_A,_P),(_A,_I)))
if mibBuilder.loadTexts:vcFcFabricManagedStatusChange.setStatus(_D)
vcModuleManagedStatusChange=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,6))
vcModuleManagedStatusChange.setObjects(*((_A,_N),(_A,_F)))
if mibBuilder.loadTexts:vcModuleManagedStatusChange.setStatus(_D)
vcEnclosureManagedStatusChange=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,7))
vcEnclosureManagedStatusChange.setObjects(*((_A,_M),(_A,_E)))
if mibBuilder.loadTexts:vcEnclosureManagedStatusChange.setStatus(_D)
vcPhysicalServerManagedStatusChange=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,8))
vcPhysicalServerManagedStatusChange.setObjects(*((_A,_O),(_A,_G)))
if mibBuilder.loadTexts:vcPhysicalServerManagedStatusChange.setStatus(_D)
vcProfileManagedStatusChange=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,9))
vcProfileManagedStatusChange.setObjects(*((_A,_R),(_A,_J)))
if mibBuilder.loadTexts:vcProfileManagedStatusChange.setStatus(_D)
vcTestTrap=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,10))
vcTestTrap.setObjects((_A,_Z))
if mibBuilder.loadTexts:vcTestTrap.setStatus(_B)
vcDomainStackingLinkRendundancyStatusChange=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,11))
vcDomainStackingLinkRendundancyStatusChange.setObjects((_A,_b))
if mibBuilder.loadTexts:vcDomainStackingLinkRendundancyStatusChange.setStatus(_B)
vcDomainManagedStatusChanged=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,12))
vcDomainManagedStatusChanged.setObjects(*((_A,_K),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:vcDomainManagedStatusChanged.setStatus(_B)
vcEnclosureManagedStatusChanged=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,13))
vcEnclosureManagedStatusChanged.setObjects(*((_A,_E),(_A,_f),(_A,_M),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:vcEnclosureManagedStatusChanged.setStatus(_B)
vcModuleManagedStatusChanged=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,14))
vcModuleManagedStatusChanged.setObjects(*((_A,_F),(_A,_N),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:vcModuleManagedStatusChanged.setStatus(_B)
vcPhysicalServerManagedStatusChanged=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,16))
vcPhysicalServerManagedStatusChanged.setObjects(*((_A,_G),(_A,_O),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:vcPhysicalServerManagedStatusChanged.setStatus(_B)
vcFcFabricManagedStatusChanged=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,17))
vcFcFabricManagedStatusChanged.setObjects(*((_A,_I),(_A,_p),(_A,_P),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:vcFcFabricManagedStatusChanged.setStatus(_B)
vcEnetNetworkManagedStatusChanged=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,18))
vcEnetNetworkManagedStatusChanged.setObjects(*((_A,_H),(_A,_t),(_A,_Q),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:vcEnetNetworkManagedStatusChanged.setStatus(_B)
vcProfileManagedStatusChanged=NotificationType((1,3,6,1,4,1,11,5,7,5,2,1,2,0,19))
vcProfileManagedStatusChanged.setObjects(*((_A,_J),(_A,_x),(_A,_R),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:vcProfileManagedStatusChanged.setStatus(_B)
vcManagedStatusNotificationsGroup=NotificationGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,13))
vcManagedStatusNotificationsGroup.setObjects(*((_A,_Aa),(_A,_A1),(_A,_A2),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:vcManagedStatusNotificationsGroup.setStatus(_D)
vcManagedStatusNotificationsGroup2=NotificationGroup((1,3,6,1,4,1,11,5,7,5,2,1,3,2,14))
vcManagedStatusNotificationsGroup2.setObjects(*((_A,_Ah),(_A,_A1),(_A,_A2),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:vcManagedStatusNotificationsGroup2.setStatus(_B)
vcDomainMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,5,7,5,2,1,3,1,1))
vcDomainMIBCompliance.setObjects(*((_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0)))
if mibBuilder.loadTexts:vcDomainMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VcManagedStatus':VcManagedStatus,'VcDomainModuleRole':VcDomainModuleRole,'VcModuleType':VcModuleType,'VcPortType':VcPortType,'VcDomainReasonCodeType':VcDomainReasonCodeType,'VcEnclosureReasonCodeType':VcEnclosureReasonCodeType,'VcModuleReasonCodeType':VcModuleReasonCodeType,'VcPortReasonCodeType':VcPortReasonCodeType,'VcPhysicalServerReasonCodeType':VcPhysicalServerReasonCodeType,'VcFcFabricReasonCodeType':VcFcFabricReasonCodeType,'VcEnetNetworkReasonCodeType':VcEnetNetworkReasonCodeType,'VcProfileReasonCodeType':VcProfileReasonCodeType,'hp':hp,'hpSysMgt':hpSysMgt,'hpEmbeddedServerMgt':hpEmbeddedServerMgt,'hpModuleMgmtProc':hpModuleMgmtProc,'virtualConnect':virtualConnect,'vcDomainMIB':vcDomainMIB,'vcDomainMIBObjects':vcDomainMIBObjects,'vcDomain':vcDomain,_Z:vcDomainName,_K:vcDomainManagedStatus,_A7:vcDomainPrimaryAddressType,_A8:vcDomainPrimaryAddress,_L:vcDomainCheckpointValid,_a:vcDomainLastCheckpointTime,_b:vcDomainStackingLinkRedundant,_c:vcDomainRootCause,_d:vcDomainCause,_e:vcDomainReasonCode,_A9:vcDomainPrimaryAddressIpv6,'vcEnclosure':vcEnclosure,'vcEnclosureTable':vcEnclosureTable,'vcEnclosureEntry':vcEnclosureEntry,_E:vcEnclosureIndex,_f:vcEnclosureName,_M:vcEnclosureManagedStatus,_AA:vcEnclosureAddressType,_AB:vcEnclosureAddress,_AC:vcEnclosureUUID,_g:vcEnclosureRootCause,_h:vcEnclosureCause,_i:vcEnclosureReasonCode,_AD:vcEnclosureAddressIpv6,'vcModule':vcModule,'vcModuleTable':vcModuleTable,'vcModuleEntry':vcModuleEntry,_F:vcModuleIndex,_AE:vcModuleType,_N:vcModuleManagedStatus,_AF:vcModulePartNumber,'vcModuleSerialNumber':vcModuleSerialNumber,'vcModuleProductName':vcModuleProductName,_AG:vcModuleFwRev,_AH:vcModuleEnclosurePointer,_AI:vcModuleLocation,_AJ:vcModuleAddressType,_AK:vcModuleAddress,_AL:vcModuleID,_j:vcModuleRootCause,_k:vcModuleCause,_l:vcModuleReasonCode,_AM:vcModuleAddressIpv6,'vcPort':vcPort,'vcPortTable':vcPortTable,'vcPortEntry':vcPortEntry,_S:vcPortIndex,_AN:vcPortType,_AO:vcPortManagedStatus,_AP:vcPortManagerAddressType,_AQ:vcPortManagerAddress,_AS:vcPortPhysicalPortPointer,_AR:vcPortContainerPointer,'vcPhysicalServer':vcPhysicalServer,'vcPhysicalServerTable':vcPhysicalServerTable,'vcPhysicalServerEntry':vcPhysicalServerEntry,_G:vcPhysicalServerIndex,_AT:vcPhysicalServerEnclosureIndex,_O:vcPhysicalServerManagedStatus,'vcPhysicalServerPartNumber':vcPhysicalServerPartNumber,'vcPhysicalServerSerialNumber':vcPhysicalServerSerialNumber,'vcPhysicalServerProductName':vcPhysicalServerProductName,_AU:vcPhysicalServerLocation,_m:vcPhysicalServerRootCause,_n:vcPhysicalServerCause,_o:vcPhysicalServerReasonCode,'vcEnetNetwork':vcEnetNetwork,'vcEnetNetworkTable':vcEnetNetworkTable,'vcEnetNetworkEntry':vcEnetNetworkEntry,_H:vcEnetNetworkIndex,_t:vcEnetNetworkName,_Q:vcEnetNetworkManagedStatus,_AV:vcEnetNetworkUplinkVlanId,_u:vcEnetNetworkRootCause,_v:vcEnetNetworkCause,_w:vcEnetNetworkReasonCode,'vcFcFabric':vcFcFabric,'vcFcFabricTable':vcFcFabricTable,'vcFcFabricEntry':vcFcFabricEntry,_I:vcFcFabricIndex,_p:vcFcFabricName,_P:vcFcFabricManagedStatus,_q:vcFcFabricRootCause,_r:vcFcFabricCause,_s:vcFcFabricReasonCode,'vcProfile':vcProfile,'vcProfileTable':vcProfileTable,'vcProfileEntry':vcProfileEntry,_J:vcProfileIndex,_x:vcProfileName,_R:vcProfileManagedStatus,_AW:vcProfilePhysicalServerIndex,_AX:vcProfileLogicalSerialNumber,_y:vcProfileRootCause,_z:vcProfileCause,_A0:vcProfileReasonCode,'vcEnetNetworkVcPortMap':vcEnetNetworkVcPortMap,'vcEnetNetworkVcPortMapTable':vcEnetNetworkVcPortMapTable,'vcEnetNetworkVcPortMapEntry':vcEnetNetworkVcPortMapEntry,_T:vcEnetNetworkVcPortMapNetworkIndex,_U:vcEnetNetworkVcPortMapVcPortIndex,'vcFcFabricVcPortMap':vcFcFabricVcPortMap,'vcFcFabricVcPortMapTable':vcFcFabricVcPortMapTable,'vcFcFabricVcPortMapEntry':vcFcFabricVcPortMapEntry,_V:vcFcFabricVcPortMapFcFabricIndex,_W:vcFcFabricVcPortMapVcPortIndex,'vcProfileNetworkMap':vcProfileNetworkMap,'vcProfileNetworkMapTable':vcProfileNetworkMapTable,'vcProfileNetworkMapEntry':vcProfileNetworkMapEntry,_X:vcProfileNetworkMapProfileIndex,_A5:vcProfileNetworkMapConnectionIndex,_AY:vcProfileNetworkMapNetworkIndex,'vcProfileFcFabricMap':vcProfileFcFabricMap,'vcProfileFcFabricMapTable':vcProfileFcFabricMapTable,'vcProfileFcFabricMapEntry':vcProfileFcFabricMapEntry,_Y:vcProfileFcFabricMapProfileIndex,_A6:vcProfileFcFabricMapConnectionIndex,_AZ:vcProfileFcFabricMapFcFabricIndex,'vcDomainMIBNotificationPrefix':vcDomainMIBNotificationPrefix,'vcDomainMIBNotifications':vcDomainMIBNotifications,_Aa:vcDomainManagedStatusChange,_A1:vcCheckpointTimeout,_A2:vcCheckpointCompleted,_Ab:vcEnetNetworkManagedStatusChange,_Ac:vcFcFabricManagedStatusChange,_Ad:vcModuleManagedStatusChange,_Ae:vcEnclosureManagedStatusChange,_Af:vcPhysicalServerManagedStatusChange,_Ag:vcProfileManagedStatusChange,_A3:vcTestTrap,_A4:vcDomainStackingLinkRendundancyStatusChange,_Ah:vcDomainManagedStatusChanged,_Al:vcEnclosureManagedStatusChanged,_Ak:vcModuleManagedStatusChanged,_Am:vcPhysicalServerManagedStatusChanged,_Aj:vcFcFabricManagedStatusChanged,_Ai:vcEnetNetworkManagedStatusChanged,_An:vcProfileManagedStatusChanged,'vcDomainMIBNotificationObjects':vcDomainMIBNotificationObjects,'vcDomainMIBConformance':vcDomainMIBConformance,'vcDomainMIBCompliances':vcDomainMIBCompliances,'vcDomainMIBCompliance':vcDomainMIBCompliance,'vcDomainMIBGroups':vcDomainMIBGroups,_Ao:vcDomainGroup,_Ap:vcEnclosureGroup,_Aq:vcModuleGroup,_Ar:vcPortGroup,_As:vcPhysicalServerGroup,_At:vcFcFabricGroup,_Au:vcEnetNetworkGroup,_Av:vcProfileGroup,_Aw:vcEnetNetworkVcPortMapGroup,_Ax:vcFcFabricVcPortMapGroup,_Ay:vcProfileNetworkMapGroup,_Az:vcProfileFcFabricMapGroup,_A_:vcManagedStatusNotificationsGroup,_B0:vcManagedStatusNotificationsGroup2})