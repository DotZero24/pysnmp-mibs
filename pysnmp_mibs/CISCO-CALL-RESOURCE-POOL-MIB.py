_AY='ccrpCDStatisticsGroup'
_AX='ccrpDnisStatisticsGroup'
_AW='ccrpCPStatisticsGroup'
_AV='ccrpCPConfigGroup'
_AU='ccrpResourceConfigGroup'
_AT='ccrpCDConfigGroup'
_AS='ccrpDnisConfigGroup'
_AR='ccrpGeneralConfigGroup'
_AQ='ccrpCDRejected'
_AP='ccrpDnisCallTypeRejected'
_AO='ccrpDnisPeakActiveSessions'
_AN='ccrpDnisTotalSessions'
_AM='ccrpDnisActiveSessions'
_AL='ccrpDnisStatisticsGroupName'
_AK='ccrpDnisStatisticsTableLengthExceeded'
_AJ='ccrpDnisStatisticsTableSystemMax'
_AI='ccrpDnisStatisticsTableMaxEntries'
_AH='ccrpCPResourceRejected'
_AG='ccrpCPOverflowRejected'
_AF='ccrpCPPeakActiveSessions'
_AE='ccrpCPMaxStateTime'
_AD='ccrpCPOverflowTime'
_AC='ccrpCPNumberMaxState'
_AB='ccrpCPNumberOverflowState'
_AA='ccrpCPTotalOverflowSessions'
_A9='ccrpCPTotalSessions'
_A8='ccrpCPActiveOverflowSessions'
_A7='ccrpCPActiveSessions'
_A6='ccrpCPVGRowStatus'
_A5='ccrpCPVGOperStatus'
_A4='ccrpCPResourceRowStatus'
_A3='ccrpCPResourceOperStatus'
_A2='ccrpCPResourceServiceProfileName'
_A1='ccrpCPDnisGroupRowStatus'
_A0='ccrpCPDnisGroupOperStatus'
_z='ccrpCPRowStatus'
_y='ccrpCPOverflow'
_x='ccrpCPSessionLimit'
_w='ccrpResourceRangeRowStatus'
_v='ccrpResourceRangeOperStatus'
_u='ccrpResourceRangeEndPort'
_t='ccrpResourceRangeStartPort'
_s='ccrpResourceGroupRowStatus'
_r='ccrpResourceGroupOperStatus'
_q='ccrpResourceLimit'
_p='ccrpResourcePortBased'
_o='ccrpCDDiscriminatedGroupRowStatus'
_n='ccrpCDDiscriminatedGroupOperStatus'
_m='ccrpCDRowStatus'
_l='ccrpCDCallType'
_k='ccrpDnisGroupCallTypeRowStatus'
_j='ccrpDnisGroupCallTypeOperStatus'
_i='ccrpDnisGroupCallType'
_h='ccrpDnisGroupRowStatus'
_g='ccrpNoResourceCallTreatment'
_f='ccrpNoCPCallTreatment'
_e='ccrpCDStatisticsEntry'
_d='ccrpCPStatisticsEntry'
_c='ccrpDnisStatisticsDnisNumber'
_b='call attempts'
_a='occurrences'
_Z='ccrpCPVGName'
_Y='ccrpCPResourceCallType'
_X='ccrpResourceRangeIndex'
_W='ccrpCDDiscriminatedGroupType'
_V='ccrpCDDiscriminatedGroupName'
_U='CcrpPhoneNumberPattern'
_T='ccrpDnisGroupMember'
_S='TruthValue'
_R='PhysicalPosition'
_Q='ccrpCDName'
_P='speech'
_O='digital'
_N='read-write'
_M='Bits'
_L='ccrpResourceName'
_K='ccrpDnisGroupName'
_J='ccrpCPName'
_I='Unsigned32'
_H='Integer32'
_G='SnmpAdminString'
_F='sessions'
_E='not-accessible'
_D='read-create'
_C='read-only'
_B='CISCO-CALL-RESOURCE-POOL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoRowOperStatus,=mibBuilder.importSymbols('CISCO-TC','CiscoRowOperStatus')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_M,'Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_S)
ciscoCallResourcePoolMIB=ModuleIdentity((1,3,6,1,4,1,9,9,124))
if mibBuilder.loadTexts:ciscoCallResourcePoolMIB.setRevisions(('2005-11-18 00:00','1998-11-13 00:00'))
class CcrpPhoneNumber(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
class CcrpPhoneNumberPattern(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
class PhysicalPosition(TextualConvention,Unsigned32):status=_A
_CCallResourcePoolMIBObjects_ObjectIdentity=ObjectIdentity
cCallResourcePoolMIBObjects=_CCallResourcePoolMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,124,1))
_CcrpConfiguration_ObjectIdentity=ObjectIdentity
ccrpConfiguration=_CcrpConfiguration_ObjectIdentity((1,3,6,1,4,1,9,9,124,1,1))
_CcrpGeneralConfig_ObjectIdentity=ObjectIdentity
ccrpGeneralConfig=_CcrpGeneralConfig_ObjectIdentity((1,3,6,1,4,1,9,9,124,1,1,1))
class _CcrpNoCPCallTreatment_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAnswer',1),('busy',2)))
_CcrpNoCPCallTreatment_Type.__name__=_H
_CcrpNoCPCallTreatment_Object=MibScalar
ccrpNoCPCallTreatment=_CcrpNoCPCallTreatment_Object((1,3,6,1,4,1,9,9,124,1,1,1,1),_CcrpNoCPCallTreatment_Type())
ccrpNoCPCallTreatment.setMaxAccess(_N)
if mibBuilder.loadTexts:ccrpNoCPCallTreatment.setStatus(_A)
class _CcrpNoResourceCallTreatment_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('channelNotAvailable',1),('busy',2)))
_CcrpNoResourceCallTreatment_Type.__name__=_H
_CcrpNoResourceCallTreatment_Object=MibScalar
ccrpNoResourceCallTreatment=_CcrpNoResourceCallTreatment_Object((1,3,6,1,4,1,9,9,124,1,1,1,2),_CcrpNoResourceCallTreatment_Type())
ccrpNoResourceCallTreatment.setMaxAccess(_N)
if mibBuilder.loadTexts:ccrpNoResourceCallTreatment.setStatus(_A)
_CcrpDnisConfig_ObjectIdentity=ObjectIdentity
ccrpDnisConfig=_CcrpDnisConfig_ObjectIdentity((1,3,6,1,4,1,9,9,124,1,1,2))
_CcrpDnisGroupTable_Object=MibTable
ccrpDnisGroupTable=_CcrpDnisGroupTable_Object((1,3,6,1,4,1,9,9,124,1,1,2,1))
if mibBuilder.loadTexts:ccrpDnisGroupTable.setStatus(_A)
_CcrpDnisGroupEntry_Object=MibTableRow
ccrpDnisGroupEntry=_CcrpDnisGroupEntry_Object((1,3,6,1,4,1,9,9,124,1,1,2,1,1))
ccrpDnisGroupEntry.setIndexNames((0,_B,_K),(1,_B,_T))
if mibBuilder.loadTexts:ccrpDnisGroupEntry.setStatus(_A)
class _CcrpDnisGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,23))
_CcrpDnisGroupName_Type.__name__=_G
_CcrpDnisGroupName_Object=MibTableColumn
ccrpDnisGroupName=_CcrpDnisGroupName_Object((1,3,6,1,4,1,9,9,124,1,1,2,1,1,1),_CcrpDnisGroupName_Type())
ccrpDnisGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrpDnisGroupName.setStatus(_A)
class _CcrpDnisGroupMember_Type(CcrpPhoneNumberPattern):subtypeSpec=CcrpPhoneNumberPattern.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CcrpDnisGroupMember_Type.__name__=_U
_CcrpDnisGroupMember_Object=MibTableColumn
ccrpDnisGroupMember=_CcrpDnisGroupMember_Object((1,3,6,1,4,1,9,9,124,1,1,2,1,1,2),_CcrpDnisGroupMember_Type())
ccrpDnisGroupMember.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrpDnisGroupMember.setStatus(_A)
_CcrpDnisGroupRowStatus_Type=RowStatus
_CcrpDnisGroupRowStatus_Object=MibTableColumn
ccrpDnisGroupRowStatus=_CcrpDnisGroupRowStatus_Object((1,3,6,1,4,1,9,9,124,1,1,2,1,1,3),_CcrpDnisGroupRowStatus_Type())
ccrpDnisGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpDnisGroupRowStatus.setStatus(_A)
_CcrpDnisGroupCallTypeTable_Object=MibTable
ccrpDnisGroupCallTypeTable=_CcrpDnisGroupCallTypeTable_Object((1,3,6,1,4,1,9,9,124,1,1,2,2))
if mibBuilder.loadTexts:ccrpDnisGroupCallTypeTable.setStatus(_A)
_CcrpDnisGroupCallTypeEntry_Object=MibTableRow
ccrpDnisGroupCallTypeEntry=_CcrpDnisGroupCallTypeEntry_Object((1,3,6,1,4,1,9,9,124,1,1,2,2,1))
ccrpDnisGroupCallTypeEntry.setIndexNames((1,_B,_K))
if mibBuilder.loadTexts:ccrpDnisGroupCallTypeEntry.setStatus(_A)
class _CcrpDnisGroupCallType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),('undefined',3)))
_CcrpDnisGroupCallType_Type.__name__=_H
_CcrpDnisGroupCallType_Object=MibTableColumn
ccrpDnisGroupCallType=_CcrpDnisGroupCallType_Object((1,3,6,1,4,1,9,9,124,1,1,2,2,1,1),_CcrpDnisGroupCallType_Type())
ccrpDnisGroupCallType.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpDnisGroupCallType.setStatus(_A)
_CcrpDnisGroupCallTypeOperStatus_Type=CiscoRowOperStatus
_CcrpDnisGroupCallTypeOperStatus_Object=MibTableColumn
ccrpDnisGroupCallTypeOperStatus=_CcrpDnisGroupCallTypeOperStatus_Object((1,3,6,1,4,1,9,9,124,1,1,2,2,1,2),_CcrpDnisGroupCallTypeOperStatus_Type())
ccrpDnisGroupCallTypeOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpDnisGroupCallTypeOperStatus.setStatus(_A)
_CcrpDnisGroupCallTypeRowStatus_Type=RowStatus
_CcrpDnisGroupCallTypeRowStatus_Object=MibTableColumn
ccrpDnisGroupCallTypeRowStatus=_CcrpDnisGroupCallTypeRowStatus_Object((1,3,6,1,4,1,9,9,124,1,1,2,2,1,3),_CcrpDnisGroupCallTypeRowStatus_Type())
ccrpDnisGroupCallTypeRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpDnisGroupCallTypeRowStatus.setStatus(_A)
_CcrpCallDiscriminatorConfig_ObjectIdentity=ObjectIdentity
ccrpCallDiscriminatorConfig=_CcrpCallDiscriminatorConfig_ObjectIdentity((1,3,6,1,4,1,9,9,124,1,1,3))
_CcrpCallDiscriminatorTable_Object=MibTable
ccrpCallDiscriminatorTable=_CcrpCallDiscriminatorTable_Object((1,3,6,1,4,1,9,9,124,1,1,3,1))
if mibBuilder.loadTexts:ccrpCallDiscriminatorTable.setStatus(_A)
_CcrpCallDiscriminatorEntry_Object=MibTableRow
ccrpCallDiscriminatorEntry=_CcrpCallDiscriminatorEntry_Object((1,3,6,1,4,1,9,9,124,1,1,3,1,1))
ccrpCallDiscriminatorEntry.setIndexNames((1,_B,_Q))
if mibBuilder.loadTexts:ccrpCallDiscriminatorEntry.setStatus(_A)
class _CcrpCDName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,23))
_CcrpCDName_Type.__name__=_G
_CcrpCDName_Object=MibTableColumn
ccrpCDName=_CcrpCDName_Object((1,3,6,1,4,1,9,9,124,1,1,3,1,1,1),_CcrpCDName_Type())
ccrpCDName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrpCDName.setStatus(_A)
class _CcrpCDCallType_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*((_O,0),(_P,1),('v110',2),('v120',3)))
_CcrpCDCallType_Type.__name__=_M
_CcrpCDCallType_Object=MibTableColumn
ccrpCDCallType=_CcrpCDCallType_Object((1,3,6,1,4,1,9,9,124,1,1,3,1,1,2),_CcrpCDCallType_Type())
ccrpCDCallType.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpCDCallType.setStatus(_A)
_CcrpCDRowStatus_Type=RowStatus
_CcrpCDRowStatus_Object=MibTableColumn
ccrpCDRowStatus=_CcrpCDRowStatus_Object((1,3,6,1,4,1,9,9,124,1,1,3,1,1,3),_CcrpCDRowStatus_Type())
ccrpCDRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpCDRowStatus.setStatus(_A)
_CcrpCDDiscriminatedGrpTable_Object=MibTable
ccrpCDDiscriminatedGrpTable=_CcrpCDDiscriminatedGrpTable_Object((1,3,6,1,4,1,9,9,124,1,1,3,2))
if mibBuilder.loadTexts:ccrpCDDiscriminatedGrpTable.setStatus(_A)
_CcrpCDDiscriminatedGrpEntry_Object=MibTableRow
ccrpCDDiscriminatedGrpEntry=_CcrpCDDiscriminatedGrpEntry_Object((1,3,6,1,4,1,9,9,124,1,1,3,2,1))
ccrpCDDiscriminatedGrpEntry.setIndexNames((0,_B,_Q),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:ccrpCDDiscriminatedGrpEntry.setStatus(_A)
class _CcrpCDDiscriminatedGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,23))
_CcrpCDDiscriminatedGroupName_Type.__name__=_G
_CcrpCDDiscriminatedGroupName_Object=MibTableColumn
ccrpCDDiscriminatedGroupName=_CcrpCDDiscriminatedGroupName_Object((1,3,6,1,4,1,9,9,124,1,1,3,2,1,1),_CcrpCDDiscriminatedGroupName_Type())
ccrpCDDiscriminatedGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrpCDDiscriminatedGroupName.setStatus(_A)
class _CcrpCDDiscriminatedGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('dnis',1))
_CcrpCDDiscriminatedGroupType_Type.__name__=_H
_CcrpCDDiscriminatedGroupType_Object=MibTableColumn
ccrpCDDiscriminatedGroupType=_CcrpCDDiscriminatedGroupType_Object((1,3,6,1,4,1,9,9,124,1,1,3,2,1,2),_CcrpCDDiscriminatedGroupType_Type())
ccrpCDDiscriminatedGroupType.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrpCDDiscriminatedGroupType.setStatus(_A)
_CcrpCDDiscriminatedGroupOperStatus_Type=CiscoRowOperStatus
_CcrpCDDiscriminatedGroupOperStatus_Object=MibTableColumn
ccrpCDDiscriminatedGroupOperStatus=_CcrpCDDiscriminatedGroupOperStatus_Object((1,3,6,1,4,1,9,9,124,1,1,3,2,1,3),_CcrpCDDiscriminatedGroupOperStatus_Type())
ccrpCDDiscriminatedGroupOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCDDiscriminatedGroupOperStatus.setStatus(_A)
_CcrpCDDiscriminatedGroupRowStatus_Type=RowStatus
_CcrpCDDiscriminatedGroupRowStatus_Object=MibTableColumn
ccrpCDDiscriminatedGroupRowStatus=_CcrpCDDiscriminatedGroupRowStatus_Object((1,3,6,1,4,1,9,9,124,1,1,3,2,1,4),_CcrpCDDiscriminatedGroupRowStatus_Type())
ccrpCDDiscriminatedGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpCDDiscriminatedGroupRowStatus.setStatus(_A)
_CcrpResourceConfig_ObjectIdentity=ObjectIdentity
ccrpResourceConfig=_CcrpResourceConfig_ObjectIdentity((1,3,6,1,4,1,9,9,124,1,1,4))
_CcrpResourceTable_Object=MibTable
ccrpResourceTable=_CcrpResourceTable_Object((1,3,6,1,4,1,9,9,124,1,1,4,1))
if mibBuilder.loadTexts:ccrpResourceTable.setStatus(_A)
_CcrpResourceEntry_Object=MibTableRow
ccrpResourceEntry=_CcrpResourceEntry_Object((1,3,6,1,4,1,9,9,124,1,1,4,1,1))
ccrpResourceEntry.setIndexNames((1,_B,_L))
if mibBuilder.loadTexts:ccrpResourceEntry.setStatus(_A)
class _CcrpResourceName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,23))
_CcrpResourceName_Type.__name__=_G
_CcrpResourceName_Object=MibTableColumn
ccrpResourceName=_CcrpResourceName_Object((1,3,6,1,4,1,9,9,124,1,1,4,1,1,1),_CcrpResourceName_Type())
ccrpResourceName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrpResourceName.setStatus(_A)
class _CcrpResourcePortBased_Type(TruthValue):defaultValue=1
_CcrpResourcePortBased_Type.__name__=_S
_CcrpResourcePortBased_Object=MibTableColumn
ccrpResourcePortBased=_CcrpResourcePortBased_Object((1,3,6,1,4,1,9,9,124,1,1,4,1,1,2),_CcrpResourcePortBased_Type())
ccrpResourcePortBased.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpResourcePortBased.setStatus(_A)
class _CcrpResourceLimit_Type(Unsigned32):defaultValue=0
_CcrpResourceLimit_Type.__name__=_I
_CcrpResourceLimit_Object=MibTableColumn
ccrpResourceLimit=_CcrpResourceLimit_Object((1,3,6,1,4,1,9,9,124,1,1,4,1,1,3),_CcrpResourceLimit_Type())
ccrpResourceLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpResourceLimit.setStatus(_A)
_CcrpResourceGroupOperStatus_Type=CiscoRowOperStatus
_CcrpResourceGroupOperStatus_Object=MibTableColumn
ccrpResourceGroupOperStatus=_CcrpResourceGroupOperStatus_Object((1,3,6,1,4,1,9,9,124,1,1,4,1,1,4),_CcrpResourceGroupOperStatus_Type())
ccrpResourceGroupOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpResourceGroupOperStatus.setStatus(_A)
_CcrpResourceGroupRowStatus_Type=RowStatus
_CcrpResourceGroupRowStatus_Object=MibTableColumn
ccrpResourceGroupRowStatus=_CcrpResourceGroupRowStatus_Object((1,3,6,1,4,1,9,9,124,1,1,4,1,1,5),_CcrpResourceGroupRowStatus_Type())
ccrpResourceGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpResourceGroupRowStatus.setStatus(_A)
_CcrpResourceRangeTable_Object=MibTable
ccrpResourceRangeTable=_CcrpResourceRangeTable_Object((1,3,6,1,4,1,9,9,124,1,1,4,2))
if mibBuilder.loadTexts:ccrpResourceRangeTable.setStatus(_A)
_CcrpResourceRangeEntry_Object=MibTableRow
ccrpResourceRangeEntry=_CcrpResourceRangeEntry_Object((1,3,6,1,4,1,9,9,124,1,1,4,2,1))
ccrpResourceRangeEntry.setIndexNames((0,_B,_L),(0,_B,_X))
if mibBuilder.loadTexts:ccrpResourceRangeEntry.setStatus(_A)
class _CcrpResourceRangeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CcrpResourceRangeIndex_Type.__name__=_I
_CcrpResourceRangeIndex_Object=MibTableColumn
ccrpResourceRangeIndex=_CcrpResourceRangeIndex_Object((1,3,6,1,4,1,9,9,124,1,1,4,2,1,1),_CcrpResourceRangeIndex_Type())
ccrpResourceRangeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrpResourceRangeIndex.setStatus(_A)
class _CcrpResourceRangeStartPort_Type(PhysicalPosition):defaultValue=0
_CcrpResourceRangeStartPort_Type.__name__=_R
_CcrpResourceRangeStartPort_Object=MibTableColumn
ccrpResourceRangeStartPort=_CcrpResourceRangeStartPort_Object((1,3,6,1,4,1,9,9,124,1,1,4,2,1,2),_CcrpResourceRangeStartPort_Type())
ccrpResourceRangeStartPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpResourceRangeStartPort.setStatus(_A)
class _CcrpResourceRangeEndPort_Type(PhysicalPosition):defaultValue=0
_CcrpResourceRangeEndPort_Type.__name__=_R
_CcrpResourceRangeEndPort_Object=MibTableColumn
ccrpResourceRangeEndPort=_CcrpResourceRangeEndPort_Object((1,3,6,1,4,1,9,9,124,1,1,4,2,1,3),_CcrpResourceRangeEndPort_Type())
ccrpResourceRangeEndPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpResourceRangeEndPort.setStatus(_A)
_CcrpResourceRangeOperStatus_Type=CiscoRowOperStatus
_CcrpResourceRangeOperStatus_Object=MibTableColumn
ccrpResourceRangeOperStatus=_CcrpResourceRangeOperStatus_Object((1,3,6,1,4,1,9,9,124,1,1,4,2,1,4),_CcrpResourceRangeOperStatus_Type())
ccrpResourceRangeOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpResourceRangeOperStatus.setStatus(_A)
_CcrpResourceRangeRowStatus_Type=RowStatus
_CcrpResourceRangeRowStatus_Object=MibTableColumn
ccrpResourceRangeRowStatus=_CcrpResourceRangeRowStatus_Object((1,3,6,1,4,1,9,9,124,1,1,4,2,1,5),_CcrpResourceRangeRowStatus_Type())
ccrpResourceRangeRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpResourceRangeRowStatus.setStatus(_A)
_CcrpCustomerProfileConfig_ObjectIdentity=ObjectIdentity
ccrpCustomerProfileConfig=_CcrpCustomerProfileConfig_ObjectIdentity((1,3,6,1,4,1,9,9,124,1,1,5))
_CcrpCustomerProfileTable_Object=MibTable
ccrpCustomerProfileTable=_CcrpCustomerProfileTable_Object((1,3,6,1,4,1,9,9,124,1,1,5,1))
if mibBuilder.loadTexts:ccrpCustomerProfileTable.setStatus(_A)
_CcrpCustomerProfileEntry_Object=MibTableRow
ccrpCustomerProfileEntry=_CcrpCustomerProfileEntry_Object((1,3,6,1,4,1,9,9,124,1,1,5,1,1))
ccrpCustomerProfileEntry.setIndexNames((1,_B,_J))
if mibBuilder.loadTexts:ccrpCustomerProfileEntry.setStatus(_A)
class _CcrpCPName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,23))
_CcrpCPName_Type.__name__=_G
_CcrpCPName_Object=MibTableColumn
ccrpCPName=_CcrpCPName_Object((1,3,6,1,4,1,9,9,124,1,1,5,1,1,1),_CcrpCPName_Type())
ccrpCPName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrpCPName.setStatus(_A)
class _CcrpCPSessionLimit_Type(Unsigned32):defaultValue=0
_CcrpCPSessionLimit_Type.__name__=_I
_CcrpCPSessionLimit_Object=MibTableColumn
ccrpCPSessionLimit=_CcrpCPSessionLimit_Object((1,3,6,1,4,1,9,9,124,1,1,5,1,1,2),_CcrpCPSessionLimit_Type())
ccrpCPSessionLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpCPSessionLimit.setStatus(_A)
class _CcrpCPOverflow_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_CcrpCPOverflow_Type.__name__=_H
_CcrpCPOverflow_Object=MibTableColumn
ccrpCPOverflow=_CcrpCPOverflow_Object((1,3,6,1,4,1,9,9,124,1,1,5,1,1,3),_CcrpCPOverflow_Type())
ccrpCPOverflow.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpCPOverflow.setStatus(_A)
_CcrpCPRowStatus_Type=RowStatus
_CcrpCPRowStatus_Object=MibTableColumn
ccrpCPRowStatus=_CcrpCPRowStatus_Object((1,3,6,1,4,1,9,9,124,1,1,5,1,1,4),_CcrpCPRowStatus_Type())
ccrpCPRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpCPRowStatus.setStatus(_A)
_CcrpCPDnisGrpTable_Object=MibTable
ccrpCPDnisGrpTable=_CcrpCPDnisGrpTable_Object((1,3,6,1,4,1,9,9,124,1,1,5,2))
if mibBuilder.loadTexts:ccrpCPDnisGrpTable.setStatus(_A)
_CcrpCPDnisGrpEntry_Object=MibTableRow
ccrpCPDnisGrpEntry=_CcrpCPDnisGrpEntry_Object((1,3,6,1,4,1,9,9,124,1,1,5,2,1))
ccrpCPDnisGrpEntry.setIndexNames((0,_B,_J),(1,_B,_K))
if mibBuilder.loadTexts:ccrpCPDnisGrpEntry.setStatus(_A)
_CcrpCPDnisGroupOperStatus_Type=CiscoRowOperStatus
_CcrpCPDnisGroupOperStatus_Object=MibTableColumn
ccrpCPDnisGroupOperStatus=_CcrpCPDnisGroupOperStatus_Object((1,3,6,1,4,1,9,9,124,1,1,5,2,1,1),_CcrpCPDnisGroupOperStatus_Type())
ccrpCPDnisGroupOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPDnisGroupOperStatus.setStatus(_A)
_CcrpCPDnisGroupRowStatus_Type=RowStatus
_CcrpCPDnisGroupRowStatus_Object=MibTableColumn
ccrpCPDnisGroupRowStatus=_CcrpCPDnisGroupRowStatus_Object((1,3,6,1,4,1,9,9,124,1,1,5,2,1,2),_CcrpCPDnisGroupRowStatus_Type())
ccrpCPDnisGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpCPDnisGroupRowStatus.setStatus(_A)
_CcrpCPResourceGrpTable_Object=MibTable
ccrpCPResourceGrpTable=_CcrpCPResourceGrpTable_Object((1,3,6,1,4,1,9,9,124,1,1,5,3))
if mibBuilder.loadTexts:ccrpCPResourceGrpTable.setStatus(_A)
_CcrpCPResourceGrpEntry_Object=MibTableRow
ccrpCPResourceGrpEntry=_CcrpCPResourceGrpEntry_Object((1,3,6,1,4,1,9,9,124,1,1,5,3,1))
ccrpCPResourceGrpEntry.setIndexNames((0,_B,_J),(0,_B,_L),(0,_B,_Y))
if mibBuilder.loadTexts:ccrpCPResourceGrpEntry.setStatus(_A)
class _CcrpCPResourceCallType_Type(Bits):namedValues=NamedValues(*((_O,0),(_P,1),('v110',2),('v120',3)))
_CcrpCPResourceCallType_Type.__name__=_M
_CcrpCPResourceCallType_Object=MibTableColumn
ccrpCPResourceCallType=_CcrpCPResourceCallType_Object((1,3,6,1,4,1,9,9,124,1,1,5,3,1,1),_CcrpCPResourceCallType_Type())
ccrpCPResourceCallType.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrpCPResourceCallType.setStatus(_A)
class _CcrpCPResourceServiceProfileName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,23))
_CcrpCPResourceServiceProfileName_Type.__name__=_G
_CcrpCPResourceServiceProfileName_Object=MibTableColumn
ccrpCPResourceServiceProfileName=_CcrpCPResourceServiceProfileName_Object((1,3,6,1,4,1,9,9,124,1,1,5,3,1,2),_CcrpCPResourceServiceProfileName_Type())
ccrpCPResourceServiceProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpCPResourceServiceProfileName.setStatus(_A)
_CcrpCPResourceOperStatus_Type=CiscoRowOperStatus
_CcrpCPResourceOperStatus_Object=MibTableColumn
ccrpCPResourceOperStatus=_CcrpCPResourceOperStatus_Object((1,3,6,1,4,1,9,9,124,1,1,5,3,1,3),_CcrpCPResourceOperStatus_Type())
ccrpCPResourceOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPResourceOperStatus.setStatus(_A)
_CcrpCPResourceRowStatus_Type=RowStatus
_CcrpCPResourceRowStatus_Object=MibTableColumn
ccrpCPResourceRowStatus=_CcrpCPResourceRowStatus_Object((1,3,6,1,4,1,9,9,124,1,1,5,3,1,4),_CcrpCPResourceRowStatus_Type())
ccrpCPResourceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpCPResourceRowStatus.setStatus(_A)
_CcrpCPVGTable_Object=MibTable
ccrpCPVGTable=_CcrpCPVGTable_Object((1,3,6,1,4,1,9,9,124,1,1,5,4))
if mibBuilder.loadTexts:ccrpCPVGTable.setStatus(_A)
_CcrpCPVGEntry_Object=MibTableRow
ccrpCPVGEntry=_CcrpCPVGEntry_Object((1,3,6,1,4,1,9,9,124,1,1,5,4,1))
ccrpCPVGEntry.setIndexNames((0,_B,_J),(1,_B,_Z))
if mibBuilder.loadTexts:ccrpCPVGEntry.setStatus(_A)
class _CcrpCPVGName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,23))
_CcrpCPVGName_Type.__name__=_G
_CcrpCPVGName_Object=MibTableColumn
ccrpCPVGName=_CcrpCPVGName_Object((1,3,6,1,4,1,9,9,124,1,1,5,4,1,1),_CcrpCPVGName_Type())
ccrpCPVGName.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrpCPVGName.setStatus(_A)
_CcrpCPVGOperStatus_Type=CiscoRowOperStatus
_CcrpCPVGOperStatus_Object=MibTableColumn
ccrpCPVGOperStatus=_CcrpCPVGOperStatus_Object((1,3,6,1,4,1,9,9,124,1,1,5,4,1,2),_CcrpCPVGOperStatus_Type())
ccrpCPVGOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPVGOperStatus.setStatus(_A)
_CcrpCPVGRowStatus_Type=RowStatus
_CcrpCPVGRowStatus_Object=MibTableColumn
ccrpCPVGRowStatus=_CcrpCPVGRowStatus_Object((1,3,6,1,4,1,9,9,124,1,1,5,4,1,3),_CcrpCPVGRowStatus_Type())
ccrpCPVGRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ccrpCPVGRowStatus.setStatus(_A)
_CcrpStatistics_ObjectIdentity=ObjectIdentity
ccrpStatistics=_CcrpStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,124,1,2))
_CcrpCPStatistics_ObjectIdentity=ObjectIdentity
ccrpCPStatistics=_CcrpCPStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,124,1,2,1))
_CcrpCPStatisticsTable_Object=MibTable
ccrpCPStatisticsTable=_CcrpCPStatisticsTable_Object((1,3,6,1,4,1,9,9,124,1,2,1,1))
if mibBuilder.loadTexts:ccrpCPStatisticsTable.setStatus(_A)
_CcrpCPStatisticsEntry_Object=MibTableRow
ccrpCPStatisticsEntry=_CcrpCPStatisticsEntry_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1))
if mibBuilder.loadTexts:ccrpCPStatisticsEntry.setStatus(_A)
_CcrpCPActiveSessions_Type=Gauge32
_CcrpCPActiveSessions_Object=MibTableColumn
ccrpCPActiveSessions=_CcrpCPActiveSessions_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1,1),_CcrpCPActiveSessions_Type())
ccrpCPActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPActiveSessions.setStatus(_A)
if mibBuilder.loadTexts:ccrpCPActiveSessions.setUnits(_F)
_CcrpCPActiveOverflowSessions_Type=Gauge32
_CcrpCPActiveOverflowSessions_Object=MibTableColumn
ccrpCPActiveOverflowSessions=_CcrpCPActiveOverflowSessions_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1,2),_CcrpCPActiveOverflowSessions_Type())
ccrpCPActiveOverflowSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPActiveOverflowSessions.setStatus(_A)
if mibBuilder.loadTexts:ccrpCPActiveOverflowSessions.setUnits(_F)
_CcrpCPTotalSessions_Type=Counter32
_CcrpCPTotalSessions_Object=MibTableColumn
ccrpCPTotalSessions=_CcrpCPTotalSessions_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1,3),_CcrpCPTotalSessions_Type())
ccrpCPTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPTotalSessions.setStatus(_A)
if mibBuilder.loadTexts:ccrpCPTotalSessions.setUnits(_F)
_CcrpCPTotalOverflowSessions_Type=Counter32
_CcrpCPTotalOverflowSessions_Object=MibTableColumn
ccrpCPTotalOverflowSessions=_CcrpCPTotalOverflowSessions_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1,4),_CcrpCPTotalOverflowSessions_Type())
ccrpCPTotalOverflowSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPTotalOverflowSessions.setStatus(_A)
if mibBuilder.loadTexts:ccrpCPTotalOverflowSessions.setUnits(_F)
_CcrpCPNumberOverflowState_Type=Counter32
_CcrpCPNumberOverflowState_Object=MibTableColumn
ccrpCPNumberOverflowState=_CcrpCPNumberOverflowState_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1,5),_CcrpCPNumberOverflowState_Type())
ccrpCPNumberOverflowState.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPNumberOverflowState.setStatus(_A)
if mibBuilder.loadTexts:ccrpCPNumberOverflowState.setUnits(_a)
_CcrpCPNumberMaxState_Type=Counter32
_CcrpCPNumberMaxState_Object=MibTableColumn
ccrpCPNumberMaxState=_CcrpCPNumberMaxState_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1,6),_CcrpCPNumberMaxState_Type())
ccrpCPNumberMaxState.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPNumberMaxState.setStatus(_A)
if mibBuilder.loadTexts:ccrpCPNumberMaxState.setUnits(_a)
_CcrpCPOverflowTime_Type=TimeTicks
_CcrpCPOverflowTime_Object=MibTableColumn
ccrpCPOverflowTime=_CcrpCPOverflowTime_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1,7),_CcrpCPOverflowTime_Type())
ccrpCPOverflowTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPOverflowTime.setStatus(_A)
_CcrpCPMaxStateTime_Type=TimeTicks
_CcrpCPMaxStateTime_Object=MibTableColumn
ccrpCPMaxStateTime=_CcrpCPMaxStateTime_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1,8),_CcrpCPMaxStateTime_Type())
ccrpCPMaxStateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPMaxStateTime.setStatus(_A)
_CcrpCPPeakActiveSessions_Type=Gauge32
_CcrpCPPeakActiveSessions_Object=MibTableColumn
ccrpCPPeakActiveSessions=_CcrpCPPeakActiveSessions_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1,9),_CcrpCPPeakActiveSessions_Type())
ccrpCPPeakActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPPeakActiveSessions.setStatus(_A)
if mibBuilder.loadTexts:ccrpCPPeakActiveSessions.setUnits(_F)
_CcrpCPOverflowRejected_Type=Counter32
_CcrpCPOverflowRejected_Object=MibTableColumn
ccrpCPOverflowRejected=_CcrpCPOverflowRejected_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1,10),_CcrpCPOverflowRejected_Type())
ccrpCPOverflowRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPOverflowRejected.setStatus(_A)
if mibBuilder.loadTexts:ccrpCPOverflowRejected.setUnits(_b)
_CcrpCPResourceRejected_Type=Counter32
_CcrpCPResourceRejected_Object=MibTableColumn
ccrpCPResourceRejected=_CcrpCPResourceRejected_Object((1,3,6,1,4,1,9,9,124,1,2,1,1,1,11),_CcrpCPResourceRejected_Type())
ccrpCPResourceRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCPResourceRejected.setStatus(_A)
if mibBuilder.loadTexts:ccrpCPResourceRejected.setUnits(_b)
_CcrpDnisStatistics_ObjectIdentity=ObjectIdentity
ccrpDnisStatistics=_CcrpDnisStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,124,1,2,2))
class _CcrpDnisStatisticsTableMaxEntries_Type(Unsigned32):defaultValue=0
_CcrpDnisStatisticsTableMaxEntries_Type.__name__=_I
_CcrpDnisStatisticsTableMaxEntries_Object=MibScalar
ccrpDnisStatisticsTableMaxEntries=_CcrpDnisStatisticsTableMaxEntries_Object((1,3,6,1,4,1,9,9,124,1,2,2,1),_CcrpDnisStatisticsTableMaxEntries_Type())
ccrpDnisStatisticsTableMaxEntries.setMaxAccess(_N)
if mibBuilder.loadTexts:ccrpDnisStatisticsTableMaxEntries.setStatus(_A)
_CcrpDnisStatisticsTableSystemMax_Type=Unsigned32
_CcrpDnisStatisticsTableSystemMax_Object=MibScalar
ccrpDnisStatisticsTableSystemMax=_CcrpDnisStatisticsTableSystemMax_Object((1,3,6,1,4,1,9,9,124,1,2,2,2),_CcrpDnisStatisticsTableSystemMax_Type())
ccrpDnisStatisticsTableSystemMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpDnisStatisticsTableSystemMax.setStatus(_A)
_CcrpDnisStatisticsTableLengthExceeded_Type=Counter32
_CcrpDnisStatisticsTableLengthExceeded_Object=MibScalar
ccrpDnisStatisticsTableLengthExceeded=_CcrpDnisStatisticsTableLengthExceeded_Object((1,3,6,1,4,1,9,9,124,1,2,2,3),_CcrpDnisStatisticsTableLengthExceeded_Type())
ccrpDnisStatisticsTableLengthExceeded.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpDnisStatisticsTableLengthExceeded.setStatus(_A)
_CcrpDnisStatisticsTable_Object=MibTable
ccrpDnisStatisticsTable=_CcrpDnisStatisticsTable_Object((1,3,6,1,4,1,9,9,124,1,2,2,4))
if mibBuilder.loadTexts:ccrpDnisStatisticsTable.setStatus(_A)
_CcrpDnisStatisticsEntry_Object=MibTableRow
ccrpDnisStatisticsEntry=_CcrpDnisStatisticsEntry_Object((1,3,6,1,4,1,9,9,124,1,2,2,4,1))
ccrpDnisStatisticsEntry.setIndexNames((1,_B,_c))
if mibBuilder.loadTexts:ccrpDnisStatisticsEntry.setStatus(_A)
_CcrpDnisStatisticsDnisNumber_Type=CcrpPhoneNumber
_CcrpDnisStatisticsDnisNumber_Object=MibTableColumn
ccrpDnisStatisticsDnisNumber=_CcrpDnisStatisticsDnisNumber_Object((1,3,6,1,4,1,9,9,124,1,2,2,4,1,1),_CcrpDnisStatisticsDnisNumber_Type())
ccrpDnisStatisticsDnisNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:ccrpDnisStatisticsDnisNumber.setStatus(_A)
class _CcrpDnisStatisticsGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,23))
_CcrpDnisStatisticsGroupName_Type.__name__=_G
_CcrpDnisStatisticsGroupName_Object=MibTableColumn
ccrpDnisStatisticsGroupName=_CcrpDnisStatisticsGroupName_Object((1,3,6,1,4,1,9,9,124,1,2,2,4,1,2),_CcrpDnisStatisticsGroupName_Type())
ccrpDnisStatisticsGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpDnisStatisticsGroupName.setStatus(_A)
_CcrpDnisActiveSessions_Type=Gauge32
_CcrpDnisActiveSessions_Object=MibTableColumn
ccrpDnisActiveSessions=_CcrpDnisActiveSessions_Object((1,3,6,1,4,1,9,9,124,1,2,2,4,1,3),_CcrpDnisActiveSessions_Type())
ccrpDnisActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpDnisActiveSessions.setStatus(_A)
if mibBuilder.loadTexts:ccrpDnisActiveSessions.setUnits(_F)
_CcrpDnisTotalSessions_Type=Counter32
_CcrpDnisTotalSessions_Object=MibTableColumn
ccrpDnisTotalSessions=_CcrpDnisTotalSessions_Object((1,3,6,1,4,1,9,9,124,1,2,2,4,1,4),_CcrpDnisTotalSessions_Type())
ccrpDnisTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpDnisTotalSessions.setStatus(_A)
if mibBuilder.loadTexts:ccrpDnisTotalSessions.setUnits(_F)
_CcrpDnisPeakActiveSessions_Type=Gauge32
_CcrpDnisPeakActiveSessions_Object=MibTableColumn
ccrpDnisPeakActiveSessions=_CcrpDnisPeakActiveSessions_Object((1,3,6,1,4,1,9,9,124,1,2,2,4,1,5),_CcrpDnisPeakActiveSessions_Type())
ccrpDnisPeakActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpDnisPeakActiveSessions.setStatus(_A)
if mibBuilder.loadTexts:ccrpDnisPeakActiveSessions.setUnits(_F)
_CcrpDnisCallTypeRejected_Type=Counter32
_CcrpDnisCallTypeRejected_Object=MibTableColumn
ccrpDnisCallTypeRejected=_CcrpDnisCallTypeRejected_Object((1,3,6,1,4,1,9,9,124,1,2,2,4,1,6),_CcrpDnisCallTypeRejected_Type())
ccrpDnisCallTypeRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpDnisCallTypeRejected.setStatus(_A)
if mibBuilder.loadTexts:ccrpDnisCallTypeRejected.setUnits(_F)
_CcrpCDStatistics_ObjectIdentity=ObjectIdentity
ccrpCDStatistics=_CcrpCDStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,124,1,2,3))
_CcrpCDStatisticsTable_Object=MibTable
ccrpCDStatisticsTable=_CcrpCDStatisticsTable_Object((1,3,6,1,4,1,9,9,124,1,2,3,1))
if mibBuilder.loadTexts:ccrpCDStatisticsTable.setStatus(_A)
_CcrpCDStatisticsEntry_Object=MibTableRow
ccrpCDStatisticsEntry=_CcrpCDStatisticsEntry_Object((1,3,6,1,4,1,9,9,124,1,2,3,1,1))
if mibBuilder.loadTexts:ccrpCDStatisticsEntry.setStatus(_A)
_CcrpCDRejected_Type=Counter32
_CcrpCDRejected_Object=MibTableColumn
ccrpCDRejected=_CcrpCDRejected_Object((1,3,6,1,4,1,9,9,124,1,2,3,1,1,1),_CcrpCDRejected_Type())
ccrpCDRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:ccrpCDRejected.setStatus(_A)
if mibBuilder.loadTexts:ccrpCDRejected.setUnits(_F)
_CcrpMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ccrpMIBNotificationPrefix=_CcrpMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,124,2))
_CcrpMIBConformance_ObjectIdentity=ObjectIdentity
ccrpMIBConformance=_CcrpMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,124,3))
_CcrpMIBCompliances_ObjectIdentity=ObjectIdentity
ccrpMIBCompliances=_CcrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,124,3,1))
_CcrpMIBGroups_ObjectIdentity=ObjectIdentity
ccrpMIBGroups=_CcrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,124,3,2))
ccrpCustomerProfileEntry.registerAugmentions((_B,_d))
ccrpCPStatisticsEntry.setIndexNames(*ccrpCustomerProfileEntry.getIndexNames())
ccrpCallDiscriminatorEntry.registerAugmentions((_B,_e))
ccrpCDStatisticsEntry.setIndexNames(*ccrpCallDiscriminatorEntry.getIndexNames())
ccrpGeneralConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,124,3,2,1))
ccrpGeneralConfigGroup.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ccrpGeneralConfigGroup.setStatus(_A)
ccrpDnisConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,124,3,2,2))
ccrpDnisConfigGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ccrpDnisConfigGroup.setStatus(_A)
ccrpCDConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,124,3,2,3))
ccrpCDConfigGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ccrpCDConfigGroup.setStatus(_A)
ccrpResourceConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,124,3,2,4))
ccrpResourceConfigGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:ccrpResourceConfigGroup.setStatus(_A)
ccrpCPConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,124,3,2,5))
ccrpCPConfigGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ccrpCPConfigGroup.setStatus(_A)
ccrpCPStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,124,3,2,6))
ccrpCPStatisticsGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:ccrpCPStatisticsGroup.setStatus(_A)
ccrpDnisStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,124,3,2,7))
ccrpDnisStatisticsGroup.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:ccrpDnisStatisticsGroup.setStatus(_A)
ccrpCDStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,124,3,2,8))
ccrpCDStatisticsGroup.setObjects((_B,_AQ))
if mibBuilder.loadTexts:ccrpCDStatisticsGroup.setStatus(_A)
ccrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,124,3,1,1))
ccrpMIBCompliance.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:ccrpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CcrpPhoneNumber':CcrpPhoneNumber,_U:CcrpPhoneNumberPattern,_R:PhysicalPosition,'ciscoCallResourcePoolMIB':ciscoCallResourcePoolMIB,'cCallResourcePoolMIBObjects':cCallResourcePoolMIBObjects,'ccrpConfiguration':ccrpConfiguration,'ccrpGeneralConfig':ccrpGeneralConfig,_f:ccrpNoCPCallTreatment,_g:ccrpNoResourceCallTreatment,'ccrpDnisConfig':ccrpDnisConfig,'ccrpDnisGroupTable':ccrpDnisGroupTable,'ccrpDnisGroupEntry':ccrpDnisGroupEntry,_K:ccrpDnisGroupName,_T:ccrpDnisGroupMember,_h:ccrpDnisGroupRowStatus,'ccrpDnisGroupCallTypeTable':ccrpDnisGroupCallTypeTable,'ccrpDnisGroupCallTypeEntry':ccrpDnisGroupCallTypeEntry,_i:ccrpDnisGroupCallType,_j:ccrpDnisGroupCallTypeOperStatus,_k:ccrpDnisGroupCallTypeRowStatus,'ccrpCallDiscriminatorConfig':ccrpCallDiscriminatorConfig,'ccrpCallDiscriminatorTable':ccrpCallDiscriminatorTable,'ccrpCallDiscriminatorEntry':ccrpCallDiscriminatorEntry,_Q:ccrpCDName,_l:ccrpCDCallType,_m:ccrpCDRowStatus,'ccrpCDDiscriminatedGrpTable':ccrpCDDiscriminatedGrpTable,'ccrpCDDiscriminatedGrpEntry':ccrpCDDiscriminatedGrpEntry,_V:ccrpCDDiscriminatedGroupName,_W:ccrpCDDiscriminatedGroupType,_n:ccrpCDDiscriminatedGroupOperStatus,_o:ccrpCDDiscriminatedGroupRowStatus,'ccrpResourceConfig':ccrpResourceConfig,'ccrpResourceTable':ccrpResourceTable,'ccrpResourceEntry':ccrpResourceEntry,_L:ccrpResourceName,_p:ccrpResourcePortBased,_q:ccrpResourceLimit,_r:ccrpResourceGroupOperStatus,_s:ccrpResourceGroupRowStatus,'ccrpResourceRangeTable':ccrpResourceRangeTable,'ccrpResourceRangeEntry':ccrpResourceRangeEntry,_X:ccrpResourceRangeIndex,_t:ccrpResourceRangeStartPort,_u:ccrpResourceRangeEndPort,_v:ccrpResourceRangeOperStatus,_w:ccrpResourceRangeRowStatus,'ccrpCustomerProfileConfig':ccrpCustomerProfileConfig,'ccrpCustomerProfileTable':ccrpCustomerProfileTable,'ccrpCustomerProfileEntry':ccrpCustomerProfileEntry,_J:ccrpCPName,_x:ccrpCPSessionLimit,_y:ccrpCPOverflow,_z:ccrpCPRowStatus,'ccrpCPDnisGrpTable':ccrpCPDnisGrpTable,'ccrpCPDnisGrpEntry':ccrpCPDnisGrpEntry,_A0:ccrpCPDnisGroupOperStatus,_A1:ccrpCPDnisGroupRowStatus,'ccrpCPResourceGrpTable':ccrpCPResourceGrpTable,'ccrpCPResourceGrpEntry':ccrpCPResourceGrpEntry,_Y:ccrpCPResourceCallType,_A2:ccrpCPResourceServiceProfileName,_A3:ccrpCPResourceOperStatus,_A4:ccrpCPResourceRowStatus,'ccrpCPVGTable':ccrpCPVGTable,'ccrpCPVGEntry':ccrpCPVGEntry,_Z:ccrpCPVGName,_A5:ccrpCPVGOperStatus,_A6:ccrpCPVGRowStatus,'ccrpStatistics':ccrpStatistics,'ccrpCPStatistics':ccrpCPStatistics,'ccrpCPStatisticsTable':ccrpCPStatisticsTable,_d:ccrpCPStatisticsEntry,_A7:ccrpCPActiveSessions,_A8:ccrpCPActiveOverflowSessions,_A9:ccrpCPTotalSessions,_AA:ccrpCPTotalOverflowSessions,_AB:ccrpCPNumberOverflowState,_AC:ccrpCPNumberMaxState,_AD:ccrpCPOverflowTime,_AE:ccrpCPMaxStateTime,_AF:ccrpCPPeakActiveSessions,_AG:ccrpCPOverflowRejected,_AH:ccrpCPResourceRejected,'ccrpDnisStatistics':ccrpDnisStatistics,_AI:ccrpDnisStatisticsTableMaxEntries,_AJ:ccrpDnisStatisticsTableSystemMax,_AK:ccrpDnisStatisticsTableLengthExceeded,'ccrpDnisStatisticsTable':ccrpDnisStatisticsTable,'ccrpDnisStatisticsEntry':ccrpDnisStatisticsEntry,_c:ccrpDnisStatisticsDnisNumber,_AL:ccrpDnisStatisticsGroupName,_AM:ccrpDnisActiveSessions,_AN:ccrpDnisTotalSessions,_AO:ccrpDnisPeakActiveSessions,_AP:ccrpDnisCallTypeRejected,'ccrpCDStatistics':ccrpCDStatistics,'ccrpCDStatisticsTable':ccrpCDStatisticsTable,_e:ccrpCDStatisticsEntry,_AQ:ccrpCDRejected,'ccrpMIBNotificationPrefix':ccrpMIBNotificationPrefix,'ccrpMIBConformance':ccrpMIBConformance,'ccrpMIBCompliances':ccrpMIBCompliances,'ccrpMIBCompliance':ccrpMIBCompliance,'ccrpMIBGroups':ccrpMIBGroups,_AR:ccrpGeneralConfigGroup,_AS:ccrpDnisConfigGroup,_AT:ccrpCDConfigGroup,_AU:ccrpResourceConfigGroup,_AV:ccrpCPConfigGroup,_AW:ccrpCPStatisticsGroup,_AX:ccrpDnisStatisticsGroup,_AY:ccrpCDStatisticsGroup})