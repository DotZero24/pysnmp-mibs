_B7='ciscoErmPolicyViolationNotifGroup'
_B6='ciscoErmNotifControlObjectsGroup'
_B5='ciscoErmNotifObjectsGroup'
_B4='ciscoErmResGroupConfigGroup'
_B3='ciscoErmPolicyConfigGroup'
_B2='ciscoErmResMonitorGroup'
_B1='ciscoErmResOwnerResUserOrGroupRelationGroup'
_B0='ciscoErmResGroupGroup'
_A_='ciscoErmResUserGroup'
_Az='ciscoErmResUserTypeGroup'
_Ay='ciscoErmResOwnerGroup'
_Ax='ciscoErmLocalPolicyViolation'
_Aw='ciscoErmGlobalPolicyViolation'
_Av='cermNotifsEnabled'
_Au='cermConfigResGroupUserRowStatus'
_At='cermConfigResGroupUserStorageType'
_As='cermConfigResGroupRowStatus'
_Ar='cermConfigResGroupStorageType'
_Aq='cermConfigResGroupUserTypeName'
_Ap='cermPolicyApplyRowStatus'
_Ao='cermPolicyApplyStorageType'
_An='cermPolicyApplyPolicyName'
_Am='cermPolicyResOwnerThreshRowStatus'
_Al='cermPolicyResOwnerThreshStorageType'
_Ak='cermPolicyFallingInterval'
_Aj='cermPolicyFallingThreshold'
_Ai='cermPolicyRisingInterval'
_Ah='cermPolicyRisingThreshold'
_Ag='cermPolicyRowStatus'
_Af='cermPolicyStorageType'
_Ae='cermPolicySnmpNotifEnabled'
_Ad='cermPolicyLoggingEnabled'
_Ac='cermPolicyUserTypeName'
_Ab='cermPolicyIsGlobal'
_Aa='cermScalarsGlobalPolicyName'
_AZ='cermResMonitorResPolicyName'
_AY='cermResMonitorName'
_AX='cermResUserOrGroupFallingInterval'
_AW='cermResUserOrGroupFallingThresh'
_AV='cermResUserOrGroupRisingInterval'
_AU='cermResUserOrGroupRisingThresh'
_AT='cermResUserOrGroupGlobNotifSeverity'
_AS='cermResUserOrGroupNotifSeverity'
_AR='cermResUserOrGroupMaxUsage'
_AQ='cermResUserOrGroupUsage'
_AP='cermResUserOrGroupUsagePct'
_AO='cermResUserOrGroupFlag'
_AN='cermResGroupUserInstanceCount'
_AM='cermResGroupName'
_AL='cermResUserResGroupId'
_AK='cermResUserPriority'
_AJ='cermResUserTypeResGroupCount'
_AI='cermResUserTypeResUserCount'
_AH='cermResUserTypeResOwnerCount'
_AG='cermResOwnerSubTypeFallingInterval'
_AF='cermResOwnerSubTypeFallingThresh'
_AE='cermResOwnerSubTypeRisingInterval'
_AD='cermResOwnerSubTypeRisingThresh'
_AC='cermResOwnerSubTypeGlobNotifSeverity'
_AB='cermResOwnerSubTypeMaxUsage'
_AA='cermResOwnerSubTypeUsage'
_A9='cermResOwnerSubTypeUsagePct'
_A8='cermResOwnerResGroupCount'
_A7='cermResOwnerResUserCount'
_A6='cermResOwnerThreshIsConfigurable'
_A5='cermResOwnerMeasurementUnit'
_A4='cermPolicyApplyUserOrGroupFlag'
_A3='cermPolicyApplyUserOrGroupName'
_A2='cermConfigResGroupUserName'
_A1='CermThresholdOrZero'
_A0='cermPolicyThresholdSeverity'
_z='cermPolicyIsUserGlobal'
_y='cermPolicyResOwnerSubTypeId'
_x='cermPolicyResOwnerId'
_w='cermPolicyResOwnerSubEntityId'
_v='cermPolicyPhysicalIndex'
_u='cermResMonitorResUserId'
_t='cermResMonitorResUserTypeId'
_s='cermResMonitorResOwnerId'
_r='cermResUserOrGroupThreshSeverity'
_q='cermResUserOrGroupThreshIsUserGlob'
_p='cermResUserId'
_o='cermResOwnerSubTypeThreshSeverity'
_n='percentage'
_m='read-write'
_l='critical'
_k='cermNotifsThresholdIsUserGlob'
_j='cermResUserOrGroupThreshFlag'
_i='cermResUserName'
_h='cermResUserTypeName'
_g='cermConfigResGroupName'
_f='CermDampenInterval'
_e='cermPolicyName'
_d='cermResMonitorPolicyName'
_c='cermResUserTypeResOwnerId'
_b='cermResOwnerResUserOrGroupId'
_a='cermResOwnerResUserTypeId'
_Z='cermResGroupResUserId'
_Y='cermResGroupId'
_X='cermNotifsPolicyName'
_W='cermNotifsDirection'
_V='cermNotifsThresholdValue'
_U='cermNotifsThresholdSeverity'
_T='cermResOwnerSubTypeName'
_S='cermResOwnerName'
_R='cermResMonitorId'
_Q='cermResMonitorSubEntityId'
_P='cermResOwnerSubTypeId'
_O='TruthValue'
_N='cermResUserTypeId'
_M='cermResUserTypeSubEntityId'
_L='seconds'
_K='cermResOwnerId'
_J='cermResOwnerSubEntityId'
_I='StorageType'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='SnmpAdminString'
_E='read-create'
_D='not-accessible'
_C='read-only'
_B='CISCO-ERM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PhysicalIndex,entPhysicalIndex=mibBuilder.importSymbols(_G,'PhysicalIndex',_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_I,'TextualConvention',_O)
ciscoErmMIB=ModuleIdentity((1,3,6,1,4,1,9,9,510))
if mibBuilder.loadTexts:ciscoErmMIB.setRevisions(('2006-02-11 00:00',))
class CermSubEntityId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class CermUserTypeId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
class CermUserTypeIdOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class CermUserId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CermUserIdOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class CermGroupId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CermOwnerId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CermOwnerIdOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class CermMonitorId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CermUserOrGroup(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('group',1),('user',2)))
class CermResUsagePct(TextualConvention,Unsigned32):status=_A
class CermThreshold(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class CermThresholdOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class CermDampenInterval(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2592000))
class CermThresholdSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('minor',1),('major',2),(_l,3)))
class CermNotificationSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('minor',2),('major',3),(_l,4)))
class CermNotificationDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CiscoErmMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoErmMIBNotifs=_CiscoErmMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,510,0))
_CiscoErmMIBObjects_ObjectIdentity=ObjectIdentity
ciscoErmMIBObjects=_CiscoErmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,510,1))
_CermScalars_ObjectIdentity=ObjectIdentity
cermScalars=_CermScalars_ObjectIdentity((1,3,6,1,4,1,9,9,510,1,1))
class _CermScalarsGlobalPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CermScalarsGlobalPolicyName_Type.__name__=_F
_CermScalarsGlobalPolicyName_Object=MibScalar
cermScalarsGlobalPolicyName=_CermScalarsGlobalPolicyName_Object((1,3,6,1,4,1,9,9,510,1,1,1),_CermScalarsGlobalPolicyName_Type())
cermScalarsGlobalPolicyName.setMaxAccess(_m)
if mibBuilder.loadTexts:cermScalarsGlobalPolicyName.setStatus(_A)
_CermStats_ObjectIdentity=ObjectIdentity
cermStats=_CermStats_ObjectIdentity((1,3,6,1,4,1,9,9,510,1,2))
_CermResOwnerTable_Object=MibTable
cermResOwnerTable=_CermResOwnerTable_Object((1,3,6,1,4,1,9,9,510,1,2,1))
if mibBuilder.loadTexts:cermResOwnerTable.setStatus(_A)
_CermResOwnerEntry_Object=MibTableRow
cermResOwnerEntry=_CermResOwnerEntry_Object((1,3,6,1,4,1,9,9,510,1,2,1,1))
cermResOwnerEntry.setIndexNames((0,_G,_H),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:cermResOwnerEntry.setStatus(_A)
_CermResOwnerSubEntityId_Type=CermSubEntityId
_CermResOwnerSubEntityId_Object=MibTableColumn
cermResOwnerSubEntityId=_CermResOwnerSubEntityId_Object((1,3,6,1,4,1,9,9,510,1,2,1,1,1),_CermResOwnerSubEntityId_Type())
cermResOwnerSubEntityId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResOwnerSubEntityId.setStatus(_A)
_CermResOwnerId_Type=CermOwnerId
_CermResOwnerId_Object=MibTableColumn
cermResOwnerId=_CermResOwnerId_Object((1,3,6,1,4,1,9,9,510,1,2,1,1,2),_CermResOwnerId_Type())
cermResOwnerId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResOwnerId.setStatus(_A)
class _CermResOwnerName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermResOwnerName_Type.__name__=_F
_CermResOwnerName_Object=MibTableColumn
cermResOwnerName=_CermResOwnerName_Object((1,3,6,1,4,1,9,9,510,1,2,1,1,3),_CermResOwnerName_Type())
cermResOwnerName.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerName.setStatus(_A)
class _CermResOwnerMeasurementUnit_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermResOwnerMeasurementUnit_Type.__name__=_F
_CermResOwnerMeasurementUnit_Object=MibTableColumn
cermResOwnerMeasurementUnit=_CermResOwnerMeasurementUnit_Object((1,3,6,1,4,1,9,9,510,1,2,1,1,4),_CermResOwnerMeasurementUnit_Type())
cermResOwnerMeasurementUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerMeasurementUnit.setStatus(_A)
_CermResOwnerThreshIsConfigurable_Type=TruthValue
_CermResOwnerThreshIsConfigurable_Object=MibTableColumn
cermResOwnerThreshIsConfigurable=_CermResOwnerThreshIsConfigurable_Object((1,3,6,1,4,1,9,9,510,1,2,1,1,5),_CermResOwnerThreshIsConfigurable_Type())
cermResOwnerThreshIsConfigurable.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerThreshIsConfigurable.setStatus(_A)
_CermResOwnerResUserCount_Type=Unsigned32
_CermResOwnerResUserCount_Object=MibTableColumn
cermResOwnerResUserCount=_CermResOwnerResUserCount_Object((1,3,6,1,4,1,9,9,510,1,2,1,1,6),_CermResOwnerResUserCount_Type())
cermResOwnerResUserCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerResUserCount.setStatus(_A)
_CermResOwnerResGroupCount_Type=Unsigned32
_CermResOwnerResGroupCount_Object=MibTableColumn
cermResOwnerResGroupCount=_CermResOwnerResGroupCount_Object((1,3,6,1,4,1,9,9,510,1,2,1,1,7),_CermResOwnerResGroupCount_Type())
cermResOwnerResGroupCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerResGroupCount.setStatus(_A)
_CermResOwnerSubTypeTable_Object=MibTable
cermResOwnerSubTypeTable=_CermResOwnerSubTypeTable_Object((1,3,6,1,4,1,9,9,510,1,2,2))
if mibBuilder.loadTexts:cermResOwnerSubTypeTable.setStatus(_A)
_CermResOwnerSubTypeEntry_Object=MibTableRow
cermResOwnerSubTypeEntry=_CermResOwnerSubTypeEntry_Object((1,3,6,1,4,1,9,9,510,1,2,2,1))
cermResOwnerSubTypeEntry.setIndexNames((0,_G,_H),(0,_B,_J),(0,_B,_K),(0,_B,_P))
if mibBuilder.loadTexts:cermResOwnerSubTypeEntry.setStatus(_A)
_CermResOwnerSubTypeId_Type=Unsigned32
_CermResOwnerSubTypeId_Object=MibTableColumn
cermResOwnerSubTypeId=_CermResOwnerSubTypeId_Object((1,3,6,1,4,1,9,9,510,1,2,2,1,1),_CermResOwnerSubTypeId_Type())
cermResOwnerSubTypeId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResOwnerSubTypeId.setStatus(_A)
class _CermResOwnerSubTypeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CermResOwnerSubTypeName_Type.__name__=_F
_CermResOwnerSubTypeName_Object=MibTableColumn
cermResOwnerSubTypeName=_CermResOwnerSubTypeName_Object((1,3,6,1,4,1,9,9,510,1,2,2,1,2),_CermResOwnerSubTypeName_Type())
cermResOwnerSubTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerSubTypeName.setStatus(_A)
_CermResOwnerSubTypeUsagePct_Type=CermResUsagePct
_CermResOwnerSubTypeUsagePct_Object=MibTableColumn
cermResOwnerSubTypeUsagePct=_CermResOwnerSubTypeUsagePct_Object((1,3,6,1,4,1,9,9,510,1,2,2,1,3),_CermResOwnerSubTypeUsagePct_Type())
cermResOwnerSubTypeUsagePct.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerSubTypeUsagePct.setStatus(_A)
if mibBuilder.loadTexts:cermResOwnerSubTypeUsagePct.setUnits(_n)
_CermResOwnerSubTypeUsage_Type=Unsigned32
_CermResOwnerSubTypeUsage_Object=MibTableColumn
cermResOwnerSubTypeUsage=_CermResOwnerSubTypeUsage_Object((1,3,6,1,4,1,9,9,510,1,2,2,1,4),_CermResOwnerSubTypeUsage_Type())
cermResOwnerSubTypeUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerSubTypeUsage.setStatus(_A)
_CermResOwnerSubTypeMaxUsage_Type=Unsigned32
_CermResOwnerSubTypeMaxUsage_Object=MibTableColumn
cermResOwnerSubTypeMaxUsage=_CermResOwnerSubTypeMaxUsage_Object((1,3,6,1,4,1,9,9,510,1,2,2,1,5),_CermResOwnerSubTypeMaxUsage_Type())
cermResOwnerSubTypeMaxUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerSubTypeMaxUsage.setStatus(_A)
_CermResOwnerSubTypeGlobNotifSeverity_Type=CermNotificationSeverity
_CermResOwnerSubTypeGlobNotifSeverity_Object=MibTableColumn
cermResOwnerSubTypeGlobNotifSeverity=_CermResOwnerSubTypeGlobNotifSeverity_Object((1,3,6,1,4,1,9,9,510,1,2,2,1,6),_CermResOwnerSubTypeGlobNotifSeverity_Type())
cermResOwnerSubTypeGlobNotifSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerSubTypeGlobNotifSeverity.setStatus(_A)
_CermResOwnerSubTypeThresholdTable_Object=MibTable
cermResOwnerSubTypeThresholdTable=_CermResOwnerSubTypeThresholdTable_Object((1,3,6,1,4,1,9,9,510,1,2,3))
if mibBuilder.loadTexts:cermResOwnerSubTypeThresholdTable.setStatus(_A)
_CermResOwnerSubTypeThresholdEntry_Object=MibTableRow
cermResOwnerSubTypeThresholdEntry=_CermResOwnerSubTypeThresholdEntry_Object((1,3,6,1,4,1,9,9,510,1,2,3,1))
cermResOwnerSubTypeThresholdEntry.setIndexNames((0,_G,_H),(0,_B,_J),(0,_B,_K),(0,_B,_P),(0,_B,_o))
if mibBuilder.loadTexts:cermResOwnerSubTypeThresholdEntry.setStatus(_A)
_CermResOwnerSubTypeThreshSeverity_Type=CermThresholdSeverity
_CermResOwnerSubTypeThreshSeverity_Object=MibTableColumn
cermResOwnerSubTypeThreshSeverity=_CermResOwnerSubTypeThreshSeverity_Object((1,3,6,1,4,1,9,9,510,1,2,3,1,1),_CermResOwnerSubTypeThreshSeverity_Type())
cermResOwnerSubTypeThreshSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResOwnerSubTypeThreshSeverity.setStatus(_A)
_CermResOwnerSubTypeRisingThresh_Type=CermThreshold
_CermResOwnerSubTypeRisingThresh_Object=MibTableColumn
cermResOwnerSubTypeRisingThresh=_CermResOwnerSubTypeRisingThresh_Object((1,3,6,1,4,1,9,9,510,1,2,3,1,2),_CermResOwnerSubTypeRisingThresh_Type())
cermResOwnerSubTypeRisingThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerSubTypeRisingThresh.setStatus(_A)
_CermResOwnerSubTypeRisingInterval_Type=CermDampenInterval
_CermResOwnerSubTypeRisingInterval_Object=MibTableColumn
cermResOwnerSubTypeRisingInterval=_CermResOwnerSubTypeRisingInterval_Object((1,3,6,1,4,1,9,9,510,1,2,3,1,3),_CermResOwnerSubTypeRisingInterval_Type())
cermResOwnerSubTypeRisingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerSubTypeRisingInterval.setStatus(_A)
if mibBuilder.loadTexts:cermResOwnerSubTypeRisingInterval.setUnits(_L)
_CermResOwnerSubTypeFallingThresh_Type=CermThreshold
_CermResOwnerSubTypeFallingThresh_Object=MibTableColumn
cermResOwnerSubTypeFallingThresh=_CermResOwnerSubTypeFallingThresh_Object((1,3,6,1,4,1,9,9,510,1,2,3,1,4),_CermResOwnerSubTypeFallingThresh_Type())
cermResOwnerSubTypeFallingThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerSubTypeFallingThresh.setStatus(_A)
_CermResOwnerSubTypeFallingInterval_Type=CermDampenInterval
_CermResOwnerSubTypeFallingInterval_Object=MibTableColumn
cermResOwnerSubTypeFallingInterval=_CermResOwnerSubTypeFallingInterval_Object((1,3,6,1,4,1,9,9,510,1,2,3,1,5),_CermResOwnerSubTypeFallingInterval_Type())
cermResOwnerSubTypeFallingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResOwnerSubTypeFallingInterval.setStatus(_A)
if mibBuilder.loadTexts:cermResOwnerSubTypeFallingInterval.setUnits(_L)
_CermResUserTypeTable_Object=MibTable
cermResUserTypeTable=_CermResUserTypeTable_Object((1,3,6,1,4,1,9,9,510,1,2,4))
if mibBuilder.loadTexts:cermResUserTypeTable.setStatus(_A)
_CermResUserTypeEntry_Object=MibTableRow
cermResUserTypeEntry=_CermResUserTypeEntry_Object((1,3,6,1,4,1,9,9,510,1,2,4,1))
cermResUserTypeEntry.setIndexNames((0,_G,_H),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:cermResUserTypeEntry.setStatus(_A)
_CermResUserTypeSubEntityId_Type=CermSubEntityId
_CermResUserTypeSubEntityId_Object=MibTableColumn
cermResUserTypeSubEntityId=_CermResUserTypeSubEntityId_Object((1,3,6,1,4,1,9,9,510,1,2,4,1,1),_CermResUserTypeSubEntityId_Type())
cermResUserTypeSubEntityId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResUserTypeSubEntityId.setStatus(_A)
_CermResUserTypeId_Type=CermUserTypeId
_CermResUserTypeId_Object=MibTableColumn
cermResUserTypeId=_CermResUserTypeId_Object((1,3,6,1,4,1,9,9,510,1,2,4,1,2),_CermResUserTypeId_Type())
cermResUserTypeId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResUserTypeId.setStatus(_A)
class _CermResUserTypeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermResUserTypeName_Type.__name__=_F
_CermResUserTypeName_Object=MibTableColumn
cermResUserTypeName=_CermResUserTypeName_Object((1,3,6,1,4,1,9,9,510,1,2,4,1,3),_CermResUserTypeName_Type())
cermResUserTypeName.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserTypeName.setStatus(_A)
_CermResUserTypeResOwnerCount_Type=Unsigned32
_CermResUserTypeResOwnerCount_Object=MibTableColumn
cermResUserTypeResOwnerCount=_CermResUserTypeResOwnerCount_Object((1,3,6,1,4,1,9,9,510,1,2,4,1,4),_CermResUserTypeResOwnerCount_Type())
cermResUserTypeResOwnerCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserTypeResOwnerCount.setStatus(_A)
_CermResUserTypeResUserCount_Type=Unsigned32
_CermResUserTypeResUserCount_Object=MibTableColumn
cermResUserTypeResUserCount=_CermResUserTypeResUserCount_Object((1,3,6,1,4,1,9,9,510,1,2,4,1,5),_CermResUserTypeResUserCount_Type())
cermResUserTypeResUserCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserTypeResUserCount.setStatus(_A)
_CermResUserTypeResGroupCount_Type=Unsigned32
_CermResUserTypeResGroupCount_Object=MibTableColumn
cermResUserTypeResGroupCount=_CermResUserTypeResGroupCount_Object((1,3,6,1,4,1,9,9,510,1,2,4,1,6),_CermResUserTypeResGroupCount_Type())
cermResUserTypeResGroupCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserTypeResGroupCount.setStatus(_A)
_CermResUserTable_Object=MibTable
cermResUserTable=_CermResUserTable_Object((1,3,6,1,4,1,9,9,510,1,2,5))
if mibBuilder.loadTexts:cermResUserTable.setStatus(_A)
_CermResUserEntry_Object=MibTableRow
cermResUserEntry=_CermResUserEntry_Object((1,3,6,1,4,1,9,9,510,1,2,5,1))
cermResUserEntry.setIndexNames((0,_G,_H),(0,_B,_M),(0,_B,_N),(0,_B,_p))
if mibBuilder.loadTexts:cermResUserEntry.setStatus(_A)
_CermResUserId_Type=CermUserId
_CermResUserId_Object=MibTableColumn
cermResUserId=_CermResUserId_Object((1,3,6,1,4,1,9,9,510,1,2,5,1,1),_CermResUserId_Type())
cermResUserId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResUserId.setStatus(_A)
class _CermResUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermResUserName_Type.__name__=_F
_CermResUserName_Object=MibTableColumn
cermResUserName=_CermResUserName_Object((1,3,6,1,4,1,9,9,510,1,2,5,1,2),_CermResUserName_Type())
cermResUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserName.setStatus(_A)
_CermResUserPriority_Type=Unsigned32
_CermResUserPriority_Object=MibTableColumn
cermResUserPriority=_CermResUserPriority_Object((1,3,6,1,4,1,9,9,510,1,2,5,1,3),_CermResUserPriority_Type())
cermResUserPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserPriority.setStatus(_A)
_CermResUserResGroupId_Type=CermGroupId
_CermResUserResGroupId_Object=MibTableColumn
cermResUserResGroupId=_CermResUserResGroupId_Object((1,3,6,1,4,1,9,9,510,1,2,5,1,4),_CermResUserResGroupId_Type())
cermResUserResGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserResGroupId.setStatus(_A)
_CermResGroupTable_Object=MibTable
cermResGroupTable=_CermResGroupTable_Object((1,3,6,1,4,1,9,9,510,1,2,6))
if mibBuilder.loadTexts:cermResGroupTable.setStatus(_A)
_CermResGroupEntry_Object=MibTableRow
cermResGroupEntry=_CermResGroupEntry_Object((1,3,6,1,4,1,9,9,510,1,2,6,1))
cermResGroupEntry.setIndexNames((0,_G,_H),(0,_B,_M),(0,_B,_N),(0,_B,_Y))
if mibBuilder.loadTexts:cermResGroupEntry.setStatus(_A)
_CermResGroupId_Type=CermGroupId
_CermResGroupId_Object=MibTableColumn
cermResGroupId=_CermResGroupId_Object((1,3,6,1,4,1,9,9,510,1,2,6,1,1),_CermResGroupId_Type())
cermResGroupId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResGroupId.setStatus(_A)
class _CermResGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermResGroupName_Type.__name__=_F
_CermResGroupName_Object=MibTableColumn
cermResGroupName=_CermResGroupName_Object((1,3,6,1,4,1,9,9,510,1,2,6,1,2),_CermResGroupName_Type())
cermResGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResGroupName.setStatus(_A)
_CermResGroupUserInstanceCount_Type=Unsigned32
_CermResGroupUserInstanceCount_Object=MibTableColumn
cermResGroupUserInstanceCount=_CermResGroupUserInstanceCount_Object((1,3,6,1,4,1,9,9,510,1,2,6,1,3),_CermResGroupUserInstanceCount_Type())
cermResGroupUserInstanceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResGroupUserInstanceCount.setStatus(_A)
_CermResGroupResUserTable_Object=MibTable
cermResGroupResUserTable=_CermResGroupResUserTable_Object((1,3,6,1,4,1,9,9,510,1,2,7))
if mibBuilder.loadTexts:cermResGroupResUserTable.setStatus(_A)
_CermResGroupResUserEntry_Object=MibTableRow
cermResGroupResUserEntry=_CermResGroupResUserEntry_Object((1,3,6,1,4,1,9,9,510,1,2,7,1))
cermResGroupResUserEntry.setIndexNames((0,_G,_H),(0,_B,_M),(0,_B,_N),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:cermResGroupResUserEntry.setStatus(_A)
_CermResGroupResUserId_Type=CermUserId
_CermResGroupResUserId_Object=MibTableColumn
cermResGroupResUserId=_CermResGroupResUserId_Object((1,3,6,1,4,1,9,9,510,1,2,7,1,1),_CermResGroupResUserId_Type())
cermResGroupResUserId.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResGroupResUserId.setStatus(_A)
_CermResOwnerResUserOrGroupTable_Object=MibTable
cermResOwnerResUserOrGroupTable=_CermResOwnerResUserOrGroupTable_Object((1,3,6,1,4,1,9,9,510,1,2,8))
if mibBuilder.loadTexts:cermResOwnerResUserOrGroupTable.setStatus(_A)
_CermResOwnerResUserOrGroupEntry_Object=MibTableRow
cermResOwnerResUserOrGroupEntry=_CermResOwnerResUserOrGroupEntry_Object((1,3,6,1,4,1,9,9,510,1,2,8,1))
cermResOwnerResUserOrGroupEntry.setIndexNames((0,_G,_H),(0,_B,_J),(0,_B,_K),(0,_B,_P),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:cermResOwnerResUserOrGroupEntry.setStatus(_A)
_CermResOwnerResUserTypeId_Type=CermUserTypeId
_CermResOwnerResUserTypeId_Object=MibTableColumn
cermResOwnerResUserTypeId=_CermResOwnerResUserTypeId_Object((1,3,6,1,4,1,9,9,510,1,2,8,1,1),_CermResOwnerResUserTypeId_Type())
cermResOwnerResUserTypeId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResOwnerResUserTypeId.setStatus(_A)
_CermResOwnerResUserOrGroupId_Type=CermUserId
_CermResOwnerResUserOrGroupId_Object=MibTableColumn
cermResOwnerResUserOrGroupId=_CermResOwnerResUserOrGroupId_Object((1,3,6,1,4,1,9,9,510,1,2,8,1,2),_CermResOwnerResUserOrGroupId_Type())
cermResOwnerResUserOrGroupId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResOwnerResUserOrGroupId.setStatus(_A)
_CermResUserOrGroupFlag_Type=CermUserOrGroup
_CermResUserOrGroupFlag_Object=MibTableColumn
cermResUserOrGroupFlag=_CermResUserOrGroupFlag_Object((1,3,6,1,4,1,9,9,510,1,2,8,1,3),_CermResUserOrGroupFlag_Type())
cermResUserOrGroupFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserOrGroupFlag.setStatus(_A)
_CermResUserOrGroupUsagePct_Type=CermResUsagePct
_CermResUserOrGroupUsagePct_Object=MibTableColumn
cermResUserOrGroupUsagePct=_CermResUserOrGroupUsagePct_Object((1,3,6,1,4,1,9,9,510,1,2,8,1,4),_CermResUserOrGroupUsagePct_Type())
cermResUserOrGroupUsagePct.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserOrGroupUsagePct.setStatus(_A)
if mibBuilder.loadTexts:cermResUserOrGroupUsagePct.setUnits(_n)
_CermResUserOrGroupUsage_Type=Unsigned32
_CermResUserOrGroupUsage_Object=MibTableColumn
cermResUserOrGroupUsage=_CermResUserOrGroupUsage_Object((1,3,6,1,4,1,9,9,510,1,2,8,1,5),_CermResUserOrGroupUsage_Type())
cermResUserOrGroupUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserOrGroupUsage.setStatus(_A)
_CermResUserOrGroupMaxUsage_Type=Unsigned32
_CermResUserOrGroupMaxUsage_Object=MibTableColumn
cermResUserOrGroupMaxUsage=_CermResUserOrGroupMaxUsage_Object((1,3,6,1,4,1,9,9,510,1,2,8,1,6),_CermResUserOrGroupMaxUsage_Type())
cermResUserOrGroupMaxUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserOrGroupMaxUsage.setStatus(_A)
_CermResUserOrGroupNotifSeverity_Type=CermNotificationSeverity
_CermResUserOrGroupNotifSeverity_Object=MibTableColumn
cermResUserOrGroupNotifSeverity=_CermResUserOrGroupNotifSeverity_Object((1,3,6,1,4,1,9,9,510,1,2,8,1,7),_CermResUserOrGroupNotifSeverity_Type())
cermResUserOrGroupNotifSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserOrGroupNotifSeverity.setStatus(_A)
_CermResUserOrGroupGlobNotifSeverity_Type=CermNotificationSeverity
_CermResUserOrGroupGlobNotifSeverity_Object=MibTableColumn
cermResUserOrGroupGlobNotifSeverity=_CermResUserOrGroupGlobNotifSeverity_Object((1,3,6,1,4,1,9,9,510,1,2,8,1,8),_CermResUserOrGroupGlobNotifSeverity_Type())
cermResUserOrGroupGlobNotifSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserOrGroupGlobNotifSeverity.setStatus(_A)
_CermResOwnerResUserOrGroupThresholdTable_Object=MibTable
cermResOwnerResUserOrGroupThresholdTable=_CermResOwnerResUserOrGroupThresholdTable_Object((1,3,6,1,4,1,9,9,510,1,2,9))
if mibBuilder.loadTexts:cermResOwnerResUserOrGroupThresholdTable.setStatus(_A)
_CermResOwnerResUserOrGroupThresholdEntry_Object=MibTableRow
cermResOwnerResUserOrGroupThresholdEntry=_CermResOwnerResUserOrGroupThresholdEntry_Object((1,3,6,1,4,1,9,9,510,1,2,9,1))
cermResOwnerResUserOrGroupThresholdEntry.setIndexNames((0,_G,_H),(0,_B,_J),(0,_B,_K),(0,_B,_P),(0,_B,_a),(0,_B,_b),(0,_B,_q),(0,_B,_r))
if mibBuilder.loadTexts:cermResOwnerResUserOrGroupThresholdEntry.setStatus(_A)
_CermResUserOrGroupThreshIsUserGlob_Type=TruthValue
_CermResUserOrGroupThreshIsUserGlob_Object=MibTableColumn
cermResUserOrGroupThreshIsUserGlob=_CermResUserOrGroupThreshIsUserGlob_Object((1,3,6,1,4,1,9,9,510,1,2,9,1,1),_CermResUserOrGroupThreshIsUserGlob_Type())
cermResUserOrGroupThreshIsUserGlob.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResUserOrGroupThreshIsUserGlob.setStatus(_A)
_CermResUserOrGroupThreshSeverity_Type=CermThresholdSeverity
_CermResUserOrGroupThreshSeverity_Object=MibTableColumn
cermResUserOrGroupThreshSeverity=_CermResUserOrGroupThreshSeverity_Object((1,3,6,1,4,1,9,9,510,1,2,9,1,2),_CermResUserOrGroupThreshSeverity_Type())
cermResUserOrGroupThreshSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResUserOrGroupThreshSeverity.setStatus(_A)
_CermResUserOrGroupThreshFlag_Type=CermUserOrGroup
_CermResUserOrGroupThreshFlag_Object=MibTableColumn
cermResUserOrGroupThreshFlag=_CermResUserOrGroupThreshFlag_Object((1,3,6,1,4,1,9,9,510,1,2,9,1,3),_CermResUserOrGroupThreshFlag_Type())
cermResUserOrGroupThreshFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserOrGroupThreshFlag.setStatus(_A)
_CermResUserOrGroupRisingThresh_Type=CermThreshold
_CermResUserOrGroupRisingThresh_Object=MibTableColumn
cermResUserOrGroupRisingThresh=_CermResUserOrGroupRisingThresh_Object((1,3,6,1,4,1,9,9,510,1,2,9,1,4),_CermResUserOrGroupRisingThresh_Type())
cermResUserOrGroupRisingThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserOrGroupRisingThresh.setStatus(_A)
_CermResUserOrGroupRisingInterval_Type=CermDampenInterval
_CermResUserOrGroupRisingInterval_Object=MibTableColumn
cermResUserOrGroupRisingInterval=_CermResUserOrGroupRisingInterval_Object((1,3,6,1,4,1,9,9,510,1,2,9,1,5),_CermResUserOrGroupRisingInterval_Type())
cermResUserOrGroupRisingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserOrGroupRisingInterval.setStatus(_A)
if mibBuilder.loadTexts:cermResUserOrGroupRisingInterval.setUnits(_L)
_CermResUserOrGroupFallingThresh_Type=CermThreshold
_CermResUserOrGroupFallingThresh_Object=MibTableColumn
cermResUserOrGroupFallingThresh=_CermResUserOrGroupFallingThresh_Object((1,3,6,1,4,1,9,9,510,1,2,9,1,6),_CermResUserOrGroupFallingThresh_Type())
cermResUserOrGroupFallingThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserOrGroupFallingThresh.setStatus(_A)
_CermResUserOrGroupFallingInterval_Type=CermDampenInterval
_CermResUserOrGroupFallingInterval_Object=MibTableColumn
cermResUserOrGroupFallingInterval=_CermResUserOrGroupFallingInterval_Object((1,3,6,1,4,1,9,9,510,1,2,9,1,7),_CermResUserOrGroupFallingInterval_Type())
cermResUserOrGroupFallingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserOrGroupFallingInterval.setStatus(_A)
if mibBuilder.loadTexts:cermResUserOrGroupFallingInterval.setUnits(_L)
_CermResUserTypeResOwnerTable_Object=MibTable
cermResUserTypeResOwnerTable=_CermResUserTypeResOwnerTable_Object((1,3,6,1,4,1,9,9,510,1,2,10))
if mibBuilder.loadTexts:cermResUserTypeResOwnerTable.setStatus(_A)
_CermResUserTypeResOwnerEntry_Object=MibTableRow
cermResUserTypeResOwnerEntry=_CermResUserTypeResOwnerEntry_Object((1,3,6,1,4,1,9,9,510,1,2,10,1))
cermResUserTypeResOwnerEntry.setIndexNames((0,_G,_H),(0,_B,_M),(0,_B,_N),(0,_B,_c))
if mibBuilder.loadTexts:cermResUserTypeResOwnerEntry.setStatus(_A)
_CermResUserTypeResOwnerId_Type=CermOwnerId
_CermResUserTypeResOwnerId_Object=MibTableColumn
cermResUserTypeResOwnerId=_CermResUserTypeResOwnerId_Object((1,3,6,1,4,1,9,9,510,1,2,10,1,1),_CermResUserTypeResOwnerId_Type())
cermResUserTypeResOwnerId.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResUserTypeResOwnerId.setStatus(_A)
_CermResMonitorTable_Object=MibTable
cermResMonitorTable=_CermResMonitorTable_Object((1,3,6,1,4,1,9,9,510,1,2,11))
if mibBuilder.loadTexts:cermResMonitorTable.setStatus(_A)
_CermResMonitorEntry_Object=MibTableRow
cermResMonitorEntry=_CermResMonitorEntry_Object((1,3,6,1,4,1,9,9,510,1,2,11,1))
cermResMonitorEntry.setIndexNames((0,_G,_H),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:cermResMonitorEntry.setStatus(_A)
_CermResMonitorSubEntityId_Type=CermSubEntityId
_CermResMonitorSubEntityId_Object=MibTableColumn
cermResMonitorSubEntityId=_CermResMonitorSubEntityId_Object((1,3,6,1,4,1,9,9,510,1,2,11,1,1),_CermResMonitorSubEntityId_Type())
cermResMonitorSubEntityId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResMonitorSubEntityId.setStatus(_A)
_CermResMonitorId_Type=CermMonitorId
_CermResMonitorId_Object=MibTableColumn
cermResMonitorId=_CermResMonitorId_Object((1,3,6,1,4,1,9,9,510,1,2,11,1,2),_CermResMonitorId_Type())
cermResMonitorId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResMonitorId.setStatus(_A)
class _CermResMonitorName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermResMonitorName_Type.__name__=_F
_CermResMonitorName_Object=MibTableColumn
cermResMonitorName=_CermResMonitorName_Object((1,3,6,1,4,1,9,9,510,1,2,11,1,3),_CermResMonitorName_Type())
cermResMonitorName.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResMonitorName.setStatus(_A)
_CermResMonitorResOwnerResUserTable_Object=MibTable
cermResMonitorResOwnerResUserTable=_CermResMonitorResOwnerResUserTable_Object((1,3,6,1,4,1,9,9,510,1,2,12))
if mibBuilder.loadTexts:cermResMonitorResOwnerResUserTable.setStatus(_A)
_CermResMonitorResOwnerResUserEntry_Object=MibTableRow
cermResMonitorResOwnerResUserEntry=_CermResMonitorResOwnerResUserEntry_Object((1,3,6,1,4,1,9,9,510,1,2,12,1))
cermResMonitorResOwnerResUserEntry.setIndexNames((0,_G,_H),(0,_B,_Q),(0,_B,_R),(0,_B,_s),(0,_B,_t),(0,_B,_u))
if mibBuilder.loadTexts:cermResMonitorResOwnerResUserEntry.setStatus(_A)
_CermResMonitorResOwnerId_Type=CermOwnerIdOrZero
_CermResMonitorResOwnerId_Object=MibTableColumn
cermResMonitorResOwnerId=_CermResMonitorResOwnerId_Object((1,3,6,1,4,1,9,9,510,1,2,12,1,1),_CermResMonitorResOwnerId_Type())
cermResMonitorResOwnerId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResMonitorResOwnerId.setStatus(_A)
_CermResMonitorResUserTypeId_Type=CermUserTypeIdOrZero
_CermResMonitorResUserTypeId_Object=MibTableColumn
cermResMonitorResUserTypeId=_CermResMonitorResUserTypeId_Object((1,3,6,1,4,1,9,9,510,1,2,12,1,2),_CermResMonitorResUserTypeId_Type())
cermResMonitorResUserTypeId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResMonitorResUserTypeId.setStatus(_A)
_CermResMonitorResUserId_Type=CermUserIdOrZero
_CermResMonitorResUserId_Object=MibTableColumn
cermResMonitorResUserId=_CermResMonitorResUserId_Object((1,3,6,1,4,1,9,9,510,1,2,12,1,3),_CermResMonitorResUserId_Type())
cermResMonitorResUserId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermResMonitorResUserId.setStatus(_A)
class _CermResMonitorResPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CermResMonitorResPolicyName_Type.__name__=_F
_CermResMonitorResPolicyName_Object=MibTableColumn
cermResMonitorResPolicyName=_CermResMonitorResPolicyName_Object((1,3,6,1,4,1,9,9,510,1,2,12,1,4),_CermResMonitorResPolicyName_Type())
cermResMonitorResPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResMonitorResPolicyName.setStatus(_A)
_CermResMonitorPolicyTable_Object=MibTable
cermResMonitorPolicyTable=_CermResMonitorPolicyTable_Object((1,3,6,1,4,1,9,9,510,1,2,13))
if mibBuilder.loadTexts:cermResMonitorPolicyTable.setStatus(_A)
_CermResMonitorPolicyEntry_Object=MibTableRow
cermResMonitorPolicyEntry=_CermResMonitorPolicyEntry_Object((1,3,6,1,4,1,9,9,510,1,2,13,1))
cermResMonitorPolicyEntry.setIndexNames((0,_G,_H),(0,_B,_Q),(0,_B,_R),(0,_B,_d))
if mibBuilder.loadTexts:cermResMonitorPolicyEntry.setStatus(_A)
class _CermResMonitorPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermResMonitorPolicyName_Type.__name__=_F
_CermResMonitorPolicyName_Object=MibTableColumn
cermResMonitorPolicyName=_CermResMonitorPolicyName_Object((1,3,6,1,4,1,9,9,510,1,2,13,1,1),_CermResMonitorPolicyName_Type())
cermResMonitorPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:cermResMonitorPolicyName.setStatus(_A)
_CermConfig_ObjectIdentity=ObjectIdentity
cermConfig=_CermConfig_ObjectIdentity((1,3,6,1,4,1,9,9,510,1,3))
_CermConfigPolicyTable_Object=MibTable
cermConfigPolicyTable=_CermConfigPolicyTable_Object((1,3,6,1,4,1,9,9,510,1,3,1))
if mibBuilder.loadTexts:cermConfigPolicyTable.setStatus(_A)
_CermConfigPolicyEntry_Object=MibTableRow
cermConfigPolicyEntry=_CermConfigPolicyEntry_Object((1,3,6,1,4,1,9,9,510,1,3,1,1))
cermConfigPolicyEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:cermConfigPolicyEntry.setStatus(_A)
class _CermPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermPolicyName_Type.__name__=_F
_CermPolicyName_Object=MibTableColumn
cermPolicyName=_CermPolicyName_Object((1,3,6,1,4,1,9,9,510,1,3,1,1,1),_CermPolicyName_Type())
cermPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:cermPolicyName.setStatus(_A)
class _CermPolicyIsGlobal_Type(TruthValue):defaultValue=2
_CermPolicyIsGlobal_Type.__name__=_O
_CermPolicyIsGlobal_Object=MibTableColumn
cermPolicyIsGlobal=_CermPolicyIsGlobal_Object((1,3,6,1,4,1,9,9,510,1,3,1,1,2),_CermPolicyIsGlobal_Type())
cermPolicyIsGlobal.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyIsGlobal.setStatus(_A)
class _CermPolicyUserTypeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CermPolicyUserTypeName_Type.__name__=_F
_CermPolicyUserTypeName_Object=MibTableColumn
cermPolicyUserTypeName=_CermPolicyUserTypeName_Object((1,3,6,1,4,1,9,9,510,1,3,1,1,3),_CermPolicyUserTypeName_Type())
cermPolicyUserTypeName.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyUserTypeName.setStatus(_A)
class _CermPolicyLoggingEnabled_Type(TruthValue):defaultValue=1
_CermPolicyLoggingEnabled_Type.__name__=_O
_CermPolicyLoggingEnabled_Object=MibTableColumn
cermPolicyLoggingEnabled=_CermPolicyLoggingEnabled_Object((1,3,6,1,4,1,9,9,510,1,3,1,1,4),_CermPolicyLoggingEnabled_Type())
cermPolicyLoggingEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyLoggingEnabled.setStatus(_A)
class _CermPolicySnmpNotifEnabled_Type(TruthValue):defaultValue=1
_CermPolicySnmpNotifEnabled_Type.__name__=_O
_CermPolicySnmpNotifEnabled_Object=MibTableColumn
cermPolicySnmpNotifEnabled=_CermPolicySnmpNotifEnabled_Object((1,3,6,1,4,1,9,9,510,1,3,1,1,5),_CermPolicySnmpNotifEnabled_Type())
cermPolicySnmpNotifEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicySnmpNotifEnabled.setStatus(_A)
class _CermPolicyStorageType_Type(StorageType):defaultValue=3
_CermPolicyStorageType_Type.__name__=_I
_CermPolicyStorageType_Object=MibTableColumn
cermPolicyStorageType=_CermPolicyStorageType_Object((1,3,6,1,4,1,9,9,510,1,3,1,1,6),_CermPolicyStorageType_Type())
cermPolicyStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyStorageType.setStatus(_A)
_CermPolicyRowStatus_Type=RowStatus
_CermPolicyRowStatus_Object=MibTableColumn
cermPolicyRowStatus=_CermPolicyRowStatus_Object((1,3,6,1,4,1,9,9,510,1,3,1,1,7),_CermPolicyRowStatus_Type())
cermPolicyRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyRowStatus.setStatus(_A)
_CermConfigPolicyResOwnerThreshTable_Object=MibTable
cermConfigPolicyResOwnerThreshTable=_CermConfigPolicyResOwnerThreshTable_Object((1,3,6,1,4,1,9,9,510,1,3,2))
if mibBuilder.loadTexts:cermConfigPolicyResOwnerThreshTable.setStatus(_A)
_CermConfigPolicyResOwnerThreshEntry_Object=MibTableRow
cermConfigPolicyResOwnerThreshEntry=_CermConfigPolicyResOwnerThreshEntry_Object((1,3,6,1,4,1,9,9,510,1,3,2,1))
cermConfigPolicyResOwnerThreshEntry.setIndexNames((0,_B,_e),(0,_B,_v),(0,_B,_w),(0,_B,_x),(0,_B,_y),(0,_B,_z),(0,_B,_A0))
if mibBuilder.loadTexts:cermConfigPolicyResOwnerThreshEntry.setStatus(_A)
_CermPolicyPhysicalIndex_Type=PhysicalIndex
_CermPolicyPhysicalIndex_Object=MibTableColumn
cermPolicyPhysicalIndex=_CermPolicyPhysicalIndex_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,1),_CermPolicyPhysicalIndex_Type())
cermPolicyPhysicalIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cermPolicyPhysicalIndex.setStatus(_A)
_CermPolicyResOwnerSubEntityId_Type=CermSubEntityId
_CermPolicyResOwnerSubEntityId_Object=MibTableColumn
cermPolicyResOwnerSubEntityId=_CermPolicyResOwnerSubEntityId_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,2),_CermPolicyResOwnerSubEntityId_Type())
cermPolicyResOwnerSubEntityId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermPolicyResOwnerSubEntityId.setStatus(_A)
_CermPolicyResOwnerId_Type=CermOwnerId
_CermPolicyResOwnerId_Object=MibTableColumn
cermPolicyResOwnerId=_CermPolicyResOwnerId_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,3),_CermPolicyResOwnerId_Type())
cermPolicyResOwnerId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermPolicyResOwnerId.setStatus(_A)
_CermPolicyResOwnerSubTypeId_Type=Unsigned32
_CermPolicyResOwnerSubTypeId_Object=MibTableColumn
cermPolicyResOwnerSubTypeId=_CermPolicyResOwnerSubTypeId_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,4),_CermPolicyResOwnerSubTypeId_Type())
cermPolicyResOwnerSubTypeId.setMaxAccess(_D)
if mibBuilder.loadTexts:cermPolicyResOwnerSubTypeId.setStatus(_A)
_CermPolicyIsUserGlobal_Type=TruthValue
_CermPolicyIsUserGlobal_Object=MibTableColumn
cermPolicyIsUserGlobal=_CermPolicyIsUserGlobal_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,5),_CermPolicyIsUserGlobal_Type())
cermPolicyIsUserGlobal.setMaxAccess(_D)
if mibBuilder.loadTexts:cermPolicyIsUserGlobal.setStatus(_A)
_CermPolicyThresholdSeverity_Type=CermThresholdSeverity
_CermPolicyThresholdSeverity_Object=MibTableColumn
cermPolicyThresholdSeverity=_CermPolicyThresholdSeverity_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,6),_CermPolicyThresholdSeverity_Type())
cermPolicyThresholdSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cermPolicyThresholdSeverity.setStatus(_A)
_CermPolicyRisingThreshold_Type=CermThreshold
_CermPolicyRisingThreshold_Object=MibTableColumn
cermPolicyRisingThreshold=_CermPolicyRisingThreshold_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,7),_CermPolicyRisingThreshold_Type())
cermPolicyRisingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyRisingThreshold.setStatus(_A)
class _CermPolicyRisingInterval_Type(CermDampenInterval):defaultValue=0
_CermPolicyRisingInterval_Type.__name__=_f
_CermPolicyRisingInterval_Object=MibTableColumn
cermPolicyRisingInterval=_CermPolicyRisingInterval_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,8),_CermPolicyRisingInterval_Type())
cermPolicyRisingInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyRisingInterval.setStatus(_A)
if mibBuilder.loadTexts:cermPolicyRisingInterval.setUnits(_L)
class _CermPolicyFallingThreshold_Type(CermThresholdOrZero):defaultValue=0
_CermPolicyFallingThreshold_Type.__name__=_A1
_CermPolicyFallingThreshold_Object=MibTableColumn
cermPolicyFallingThreshold=_CermPolicyFallingThreshold_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,9),_CermPolicyFallingThreshold_Type())
cermPolicyFallingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyFallingThreshold.setStatus(_A)
class _CermPolicyFallingInterval_Type(CermDampenInterval):defaultValue=0
_CermPolicyFallingInterval_Type.__name__=_f
_CermPolicyFallingInterval_Object=MibTableColumn
cermPolicyFallingInterval=_CermPolicyFallingInterval_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,10),_CermPolicyFallingInterval_Type())
cermPolicyFallingInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyFallingInterval.setStatus(_A)
if mibBuilder.loadTexts:cermPolicyFallingInterval.setUnits(_L)
class _CermPolicyResOwnerThreshStorageType_Type(StorageType):defaultValue=3
_CermPolicyResOwnerThreshStorageType_Type.__name__=_I
_CermPolicyResOwnerThreshStorageType_Object=MibTableColumn
cermPolicyResOwnerThreshStorageType=_CermPolicyResOwnerThreshStorageType_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,11),_CermPolicyResOwnerThreshStorageType_Type())
cermPolicyResOwnerThreshStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyResOwnerThreshStorageType.setStatus(_A)
_CermPolicyResOwnerThreshRowStatus_Type=RowStatus
_CermPolicyResOwnerThreshRowStatus_Object=MibTableColumn
cermPolicyResOwnerThreshRowStatus=_CermPolicyResOwnerThreshRowStatus_Object((1,3,6,1,4,1,9,9,510,1,3,2,1,12),_CermPolicyResOwnerThreshRowStatus_Type())
cermPolicyResOwnerThreshRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyResOwnerThreshRowStatus.setStatus(_A)
_CermConfigResGroupTable_Object=MibTable
cermConfigResGroupTable=_CermConfigResGroupTable_Object((1,3,6,1,4,1,9,9,510,1,3,3))
if mibBuilder.loadTexts:cermConfigResGroupTable.setStatus(_A)
_CermConfigResGroupEntry_Object=MibTableRow
cermConfigResGroupEntry=_CermConfigResGroupEntry_Object((1,3,6,1,4,1,9,9,510,1,3,3,1))
cermConfigResGroupEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:cermConfigResGroupEntry.setStatus(_A)
class _CermConfigResGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_CermConfigResGroupName_Type.__name__=_F
_CermConfigResGroupName_Object=MibTableColumn
cermConfigResGroupName=_CermConfigResGroupName_Object((1,3,6,1,4,1,9,9,510,1,3,3,1,1),_CermConfigResGroupName_Type())
cermConfigResGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:cermConfigResGroupName.setStatus(_A)
class _CermConfigResGroupUserTypeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermConfigResGroupUserTypeName_Type.__name__=_F
_CermConfigResGroupUserTypeName_Object=MibTableColumn
cermConfigResGroupUserTypeName=_CermConfigResGroupUserTypeName_Object((1,3,6,1,4,1,9,9,510,1,3,3,1,2),_CermConfigResGroupUserTypeName_Type())
cermConfigResGroupUserTypeName.setMaxAccess(_E)
if mibBuilder.loadTexts:cermConfigResGroupUserTypeName.setStatus(_A)
class _CermConfigResGroupStorageType_Type(StorageType):defaultValue=3
_CermConfigResGroupStorageType_Type.__name__=_I
_CermConfigResGroupStorageType_Object=MibTableColumn
cermConfigResGroupStorageType=_CermConfigResGroupStorageType_Object((1,3,6,1,4,1,9,9,510,1,3,3,1,3),_CermConfigResGroupStorageType_Type())
cermConfigResGroupStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cermConfigResGroupStorageType.setStatus(_A)
_CermConfigResGroupRowStatus_Type=RowStatus
_CermConfigResGroupRowStatus_Object=MibTableColumn
cermConfigResGroupRowStatus=_CermConfigResGroupRowStatus_Object((1,3,6,1,4,1,9,9,510,1,3,3,1,4),_CermConfigResGroupRowStatus_Type())
cermConfigResGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cermConfigResGroupRowStatus.setStatus(_A)
_CermConfigResGroupUserTable_Object=MibTable
cermConfigResGroupUserTable=_CermConfigResGroupUserTable_Object((1,3,6,1,4,1,9,9,510,1,3,4))
if mibBuilder.loadTexts:cermConfigResGroupUserTable.setStatus(_A)
_CermConfigResGroupUserEntry_Object=MibTableRow
cermConfigResGroupUserEntry=_CermConfigResGroupUserEntry_Object((1,3,6,1,4,1,9,9,510,1,3,4,1))
cermConfigResGroupUserEntry.setIndexNames((0,_B,_g),(0,_B,_A2))
if mibBuilder.loadTexts:cermConfigResGroupUserEntry.setStatus(_A)
class _CermConfigResGroupUserName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermConfigResGroupUserName_Type.__name__=_F
_CermConfigResGroupUserName_Object=MibTableColumn
cermConfigResGroupUserName=_CermConfigResGroupUserName_Object((1,3,6,1,4,1,9,9,510,1,3,4,1,1),_CermConfigResGroupUserName_Type())
cermConfigResGroupUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:cermConfigResGroupUserName.setStatus(_A)
class _CermConfigResGroupUserStorageType_Type(StorageType):defaultValue=3
_CermConfigResGroupUserStorageType_Type.__name__=_I
_CermConfigResGroupUserStorageType_Object=MibTableColumn
cermConfigResGroupUserStorageType=_CermConfigResGroupUserStorageType_Object((1,3,6,1,4,1,9,9,510,1,3,4,1,2),_CermConfigResGroupUserStorageType_Type())
cermConfigResGroupUserStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cermConfigResGroupUserStorageType.setStatus(_A)
_CermConfigResGroupUserRowStatus_Type=RowStatus
_CermConfigResGroupUserRowStatus_Object=MibTableColumn
cermConfigResGroupUserRowStatus=_CermConfigResGroupUserRowStatus_Object((1,3,6,1,4,1,9,9,510,1,3,4,1,3),_CermConfigResGroupUserRowStatus_Type())
cermConfigResGroupUserRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cermConfigResGroupUserRowStatus.setStatus(_A)
_CermConfigPolicyApplyTable_Object=MibTable
cermConfigPolicyApplyTable=_CermConfigPolicyApplyTable_Object((1,3,6,1,4,1,9,9,510,1,3,5))
if mibBuilder.loadTexts:cermConfigPolicyApplyTable.setStatus(_A)
_CermConfigPolicyApplyEntry_Object=MibTableRow
cermConfigPolicyApplyEntry=_CermConfigPolicyApplyEntry_Object((1,3,6,1,4,1,9,9,510,1,3,5,1))
cermConfigPolicyApplyEntry.setIndexNames((0,_B,_A3),(0,_B,_A4))
if mibBuilder.loadTexts:cermConfigPolicyApplyEntry.setStatus(_A)
class _CermPolicyApplyUserOrGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermPolicyApplyUserOrGroupName_Type.__name__=_F
_CermPolicyApplyUserOrGroupName_Object=MibTableColumn
cermPolicyApplyUserOrGroupName=_CermPolicyApplyUserOrGroupName_Object((1,3,6,1,4,1,9,9,510,1,3,5,1,1),_CermPolicyApplyUserOrGroupName_Type())
cermPolicyApplyUserOrGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:cermPolicyApplyUserOrGroupName.setStatus(_A)
_CermPolicyApplyUserOrGroupFlag_Type=CermUserOrGroup
_CermPolicyApplyUserOrGroupFlag_Object=MibTableColumn
cermPolicyApplyUserOrGroupFlag=_CermPolicyApplyUserOrGroupFlag_Object((1,3,6,1,4,1,9,9,510,1,3,5,1,2),_CermPolicyApplyUserOrGroupFlag_Type())
cermPolicyApplyUserOrGroupFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:cermPolicyApplyUserOrGroupFlag.setStatus(_A)
class _CermPolicyApplyPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CermPolicyApplyPolicyName_Type.__name__=_F
_CermPolicyApplyPolicyName_Object=MibTableColumn
cermPolicyApplyPolicyName=_CermPolicyApplyPolicyName_Object((1,3,6,1,4,1,9,9,510,1,3,5,1,3),_CermPolicyApplyPolicyName_Type())
cermPolicyApplyPolicyName.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyApplyPolicyName.setStatus(_A)
class _CermPolicyApplyStorageType_Type(StorageType):defaultValue=3
_CermPolicyApplyStorageType_Type.__name__=_I
_CermPolicyApplyStorageType_Object=MibTableColumn
cermPolicyApplyStorageType=_CermPolicyApplyStorageType_Object((1,3,6,1,4,1,9,9,510,1,3,5,1,4),_CermPolicyApplyStorageType_Type())
cermPolicyApplyStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyApplyStorageType.setStatus(_A)
_CermPolicyApplyRowStatus_Type=RowStatus
_CermPolicyApplyRowStatus_Object=MibTableColumn
cermPolicyApplyRowStatus=_CermPolicyApplyRowStatus_Object((1,3,6,1,4,1,9,9,510,1,3,5,1,5),_CermPolicyApplyRowStatus_Type())
cermPolicyApplyRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cermPolicyApplyRowStatus.setStatus(_A)
_CermNotifObjects_ObjectIdentity=ObjectIdentity
cermNotifObjects=_CermNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,510,1,4))
_CermNotifsThresholdSeverity_Type=CermThresholdSeverity
_CermNotifsThresholdSeverity_Object=MibScalar
cermNotifsThresholdSeverity=_CermNotifsThresholdSeverity_Object((1,3,6,1,4,1,9,9,510,1,4,1),_CermNotifsThresholdSeverity_Type())
cermNotifsThresholdSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cermNotifsThresholdSeverity.setStatus(_A)
_CermNotifsThresholdIsUserGlob_Type=TruthValue
_CermNotifsThresholdIsUserGlob_Object=MibScalar
cermNotifsThresholdIsUserGlob=_CermNotifsThresholdIsUserGlob_Object((1,3,6,1,4,1,9,9,510,1,4,2),_CermNotifsThresholdIsUserGlob_Type())
cermNotifsThresholdIsUserGlob.setMaxAccess(_C)
if mibBuilder.loadTexts:cermNotifsThresholdIsUserGlob.setStatus(_A)
_CermNotifsThresholdValue_Type=CermThreshold
_CermNotifsThresholdValue_Object=MibScalar
cermNotifsThresholdValue=_CermNotifsThresholdValue_Object((1,3,6,1,4,1,9,9,510,1,4,3),_CermNotifsThresholdValue_Type())
cermNotifsThresholdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cermNotifsThresholdValue.setStatus(_A)
_CermNotifsDirection_Type=CermNotificationDirection
_CermNotifsDirection_Object=MibScalar
cermNotifsDirection=_CermNotifsDirection_Object((1,3,6,1,4,1,9,9,510,1,4,4),_CermNotifsDirection_Type())
cermNotifsDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cermNotifsDirection.setStatus(_A)
_CermNotifsPolicyName_Type=SnmpAdminString
_CermNotifsPolicyName_Object=MibScalar
cermNotifsPolicyName=_CermNotifsPolicyName_Object((1,3,6,1,4,1,9,9,510,1,4,5),_CermNotifsPolicyName_Type())
cermNotifsPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:cermNotifsPolicyName.setStatus(_A)
_CermNotifControlObjects_ObjectIdentity=ObjectIdentity
cermNotifControlObjects=_CermNotifControlObjects_ObjectIdentity((1,3,6,1,4,1,9,9,510,1,5))
class _CermNotifsEnabled_Type(TruthValue):defaultValue=2
_CermNotifsEnabled_Type.__name__=_O
_CermNotifsEnabled_Object=MibScalar
cermNotifsEnabled=_CermNotifsEnabled_Object((1,3,6,1,4,1,9,9,510,1,5,1),_CermNotifsEnabled_Type())
cermNotifsEnabled.setMaxAccess(_m)
if mibBuilder.loadTexts:cermNotifsEnabled.setStatus(_A)
_CiscoErmMIBConform_ObjectIdentity=ObjectIdentity
ciscoErmMIBConform=_CiscoErmMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,510,2))
_CiscoErmMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoErmMIBCompliances=_CiscoErmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,510,2,1))
_CiscoErmMIBGroups_ObjectIdentity=ObjectIdentity
ciscoErmMIBGroups=_CiscoErmMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,510,2,2))
ciscoErmResOwnerGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,1))
ciscoErmResOwnerGroup.setObjects(*((_B,_S),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_T),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:ciscoErmResOwnerGroup.setStatus(_A)
ciscoErmResUserTypeGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,2))
ciscoErmResUserTypeGroup.setObjects(*((_B,_h),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_c)))
if mibBuilder.loadTexts:ciscoErmResUserTypeGroup.setStatus(_A)
ciscoErmResUserGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,3))
ciscoErmResUserGroup.setObjects(*((_B,_i),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:ciscoErmResUserGroup.setStatus(_A)
ciscoErmResGroupGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,4))
ciscoErmResGroupGroup.setObjects(*((_B,_AM),(_B,_AN),(_B,_Z)))
if mibBuilder.loadTexts:ciscoErmResGroupGroup.setStatus(_A)
ciscoErmResOwnerResUserOrGroupRelationGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,5))
ciscoErmResOwnerResUserOrGroupRelationGroup.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_j),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:ciscoErmResOwnerResUserOrGroupRelationGroup.setStatus(_A)
ciscoErmResMonitorGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,6))
ciscoErmResMonitorGroup.setObjects(*((_B,_AY),(_B,_AZ),(_B,_d)))
if mibBuilder.loadTexts:ciscoErmResMonitorGroup.setStatus(_A)
ciscoErmPolicyConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,7))
ciscoErmPolicyConfigGroup.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap)))
if mibBuilder.loadTexts:ciscoErmPolicyConfigGroup.setStatus(_A)
ciscoErmResGroupConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,8))
ciscoErmResGroupConfigGroup.setObjects(*((_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au)))
if mibBuilder.loadTexts:ciscoErmResGroupConfigGroup.setStatus(_A)
ciscoErmNotifControlObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,9))
ciscoErmNotifControlObjectsGroup.setObjects((_B,_Av))
if mibBuilder.loadTexts:ciscoErmNotifControlObjectsGroup.setStatus(_A)
ciscoErmNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,510,2,2,10))
ciscoErmNotifObjectsGroup.setObjects(*((_B,_U),(_B,_k),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoErmNotifObjectsGroup.setStatus(_A)
ciscoErmGlobalPolicyViolation=NotificationType((1,3,6,1,4,1,9,9,510,0,1))
ciscoErmGlobalPolicyViolation.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoErmGlobalPolicyViolation.setStatus(_A)
ciscoErmLocalPolicyViolation=NotificationType((1,3,6,1,4,1,9,9,510,0,2))
ciscoErmLocalPolicyViolation.setObjects(*((_B,_S),(_B,_T),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoErmLocalPolicyViolation.setStatus(_A)
ciscoErmPolicyViolationNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,510,2,2,11))
ciscoErmPolicyViolationNotifGroup.setObjects(*((_B,_Aw),(_B,_Ax)))
if mibBuilder.loadTexts:ciscoErmPolicyViolationNotifGroup.setStatus(_A)
ciscoErmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,510,2,1,1))
ciscoErmMIBCompliance.setObjects(*((_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7)))
if mibBuilder.loadTexts:ciscoErmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CermSubEntityId':CermSubEntityId,'CermUserTypeId':CermUserTypeId,'CermUserTypeIdOrZero':CermUserTypeIdOrZero,'CermUserId':CermUserId,'CermUserIdOrZero':CermUserIdOrZero,'CermGroupId':CermGroupId,'CermOwnerId':CermOwnerId,'CermOwnerIdOrZero':CermOwnerIdOrZero,'CermMonitorId':CermMonitorId,'CermUserOrGroup':CermUserOrGroup,'CermResUsagePct':CermResUsagePct,'CermThreshold':CermThreshold,_A1:CermThresholdOrZero,_f:CermDampenInterval,'CermThresholdSeverity':CermThresholdSeverity,'CermNotificationSeverity':CermNotificationSeverity,'CermNotificationDirection':CermNotificationDirection,'ciscoErmMIB':ciscoErmMIB,'ciscoErmMIBNotifs':ciscoErmMIBNotifs,_Aw:ciscoErmGlobalPolicyViolation,_Ax:ciscoErmLocalPolicyViolation,'ciscoErmMIBObjects':ciscoErmMIBObjects,'cermScalars':cermScalars,_Aa:cermScalarsGlobalPolicyName,'cermStats':cermStats,'cermResOwnerTable':cermResOwnerTable,'cermResOwnerEntry':cermResOwnerEntry,_J:cermResOwnerSubEntityId,_K:cermResOwnerId,_S:cermResOwnerName,_A5:cermResOwnerMeasurementUnit,_A6:cermResOwnerThreshIsConfigurable,_A7:cermResOwnerResUserCount,_A8:cermResOwnerResGroupCount,'cermResOwnerSubTypeTable':cermResOwnerSubTypeTable,'cermResOwnerSubTypeEntry':cermResOwnerSubTypeEntry,_P:cermResOwnerSubTypeId,_T:cermResOwnerSubTypeName,_A9:cermResOwnerSubTypeUsagePct,_AA:cermResOwnerSubTypeUsage,_AB:cermResOwnerSubTypeMaxUsage,_AC:cermResOwnerSubTypeGlobNotifSeverity,'cermResOwnerSubTypeThresholdTable':cermResOwnerSubTypeThresholdTable,'cermResOwnerSubTypeThresholdEntry':cermResOwnerSubTypeThresholdEntry,_o:cermResOwnerSubTypeThreshSeverity,_AD:cermResOwnerSubTypeRisingThresh,_AE:cermResOwnerSubTypeRisingInterval,_AF:cermResOwnerSubTypeFallingThresh,_AG:cermResOwnerSubTypeFallingInterval,'cermResUserTypeTable':cermResUserTypeTable,'cermResUserTypeEntry':cermResUserTypeEntry,_M:cermResUserTypeSubEntityId,_N:cermResUserTypeId,_h:cermResUserTypeName,_AH:cermResUserTypeResOwnerCount,_AI:cermResUserTypeResUserCount,_AJ:cermResUserTypeResGroupCount,'cermResUserTable':cermResUserTable,'cermResUserEntry':cermResUserEntry,_p:cermResUserId,_i:cermResUserName,_AK:cermResUserPriority,_AL:cermResUserResGroupId,'cermResGroupTable':cermResGroupTable,'cermResGroupEntry':cermResGroupEntry,_Y:cermResGroupId,_AM:cermResGroupName,_AN:cermResGroupUserInstanceCount,'cermResGroupResUserTable':cermResGroupResUserTable,'cermResGroupResUserEntry':cermResGroupResUserEntry,_Z:cermResGroupResUserId,'cermResOwnerResUserOrGroupTable':cermResOwnerResUserOrGroupTable,'cermResOwnerResUserOrGroupEntry':cermResOwnerResUserOrGroupEntry,_a:cermResOwnerResUserTypeId,_b:cermResOwnerResUserOrGroupId,_AO:cermResUserOrGroupFlag,_AP:cermResUserOrGroupUsagePct,_AQ:cermResUserOrGroupUsage,_AR:cermResUserOrGroupMaxUsage,_AS:cermResUserOrGroupNotifSeverity,_AT:cermResUserOrGroupGlobNotifSeverity,'cermResOwnerResUserOrGroupThresholdTable':cermResOwnerResUserOrGroupThresholdTable,'cermResOwnerResUserOrGroupThresholdEntry':cermResOwnerResUserOrGroupThresholdEntry,_q:cermResUserOrGroupThreshIsUserGlob,_r:cermResUserOrGroupThreshSeverity,_j:cermResUserOrGroupThreshFlag,_AU:cermResUserOrGroupRisingThresh,_AV:cermResUserOrGroupRisingInterval,_AW:cermResUserOrGroupFallingThresh,_AX:cermResUserOrGroupFallingInterval,'cermResUserTypeResOwnerTable':cermResUserTypeResOwnerTable,'cermResUserTypeResOwnerEntry':cermResUserTypeResOwnerEntry,_c:cermResUserTypeResOwnerId,'cermResMonitorTable':cermResMonitorTable,'cermResMonitorEntry':cermResMonitorEntry,_Q:cermResMonitorSubEntityId,_R:cermResMonitorId,_AY:cermResMonitorName,'cermResMonitorResOwnerResUserTable':cermResMonitorResOwnerResUserTable,'cermResMonitorResOwnerResUserEntry':cermResMonitorResOwnerResUserEntry,_s:cermResMonitorResOwnerId,_t:cermResMonitorResUserTypeId,_u:cermResMonitorResUserId,_AZ:cermResMonitorResPolicyName,'cermResMonitorPolicyTable':cermResMonitorPolicyTable,'cermResMonitorPolicyEntry':cermResMonitorPolicyEntry,_d:cermResMonitorPolicyName,'cermConfig':cermConfig,'cermConfigPolicyTable':cermConfigPolicyTable,'cermConfigPolicyEntry':cermConfigPolicyEntry,_e:cermPolicyName,_Ab:cermPolicyIsGlobal,_Ac:cermPolicyUserTypeName,_Ad:cermPolicyLoggingEnabled,_Ae:cermPolicySnmpNotifEnabled,_Af:cermPolicyStorageType,_Ag:cermPolicyRowStatus,'cermConfigPolicyResOwnerThreshTable':cermConfigPolicyResOwnerThreshTable,'cermConfigPolicyResOwnerThreshEntry':cermConfigPolicyResOwnerThreshEntry,_v:cermPolicyPhysicalIndex,_w:cermPolicyResOwnerSubEntityId,_x:cermPolicyResOwnerId,_y:cermPolicyResOwnerSubTypeId,_z:cermPolicyIsUserGlobal,_A0:cermPolicyThresholdSeverity,_Ah:cermPolicyRisingThreshold,_Ai:cermPolicyRisingInterval,_Aj:cermPolicyFallingThreshold,_Ak:cermPolicyFallingInterval,_Al:cermPolicyResOwnerThreshStorageType,_Am:cermPolicyResOwnerThreshRowStatus,'cermConfigResGroupTable':cermConfigResGroupTable,'cermConfigResGroupEntry':cermConfigResGroupEntry,_g:cermConfigResGroupName,_Aq:cermConfigResGroupUserTypeName,_Ar:cermConfigResGroupStorageType,_As:cermConfigResGroupRowStatus,'cermConfigResGroupUserTable':cermConfigResGroupUserTable,'cermConfigResGroupUserEntry':cermConfigResGroupUserEntry,_A2:cermConfigResGroupUserName,_At:cermConfigResGroupUserStorageType,_Au:cermConfigResGroupUserRowStatus,'cermConfigPolicyApplyTable':cermConfigPolicyApplyTable,'cermConfigPolicyApplyEntry':cermConfigPolicyApplyEntry,_A3:cermPolicyApplyUserOrGroupName,_A4:cermPolicyApplyUserOrGroupFlag,_An:cermPolicyApplyPolicyName,_Ao:cermPolicyApplyStorageType,_Ap:cermPolicyApplyRowStatus,'cermNotifObjects':cermNotifObjects,_U:cermNotifsThresholdSeverity,_k:cermNotifsThresholdIsUserGlob,_V:cermNotifsThresholdValue,_W:cermNotifsDirection,_X:cermNotifsPolicyName,'cermNotifControlObjects':cermNotifControlObjects,_Av:cermNotifsEnabled,'ciscoErmMIBConform':ciscoErmMIBConform,'ciscoErmMIBCompliances':ciscoErmMIBCompliances,'ciscoErmMIBCompliance':ciscoErmMIBCompliance,'ciscoErmMIBGroups':ciscoErmMIBGroups,_Ay:ciscoErmResOwnerGroup,_Az:ciscoErmResUserTypeGroup,_A_:ciscoErmResUserGroup,_B0:ciscoErmResGroupGroup,_B1:ciscoErmResOwnerResUserOrGroupRelationGroup,_B2:ciscoErmResMonitorGroup,_B3:ciscoErmPolicyConfigGroup,_B4:ciscoErmResGroupConfigGroup,_B6:ciscoErmNotifControlObjectsGroup,_B5:ciscoErmNotifObjectsGroup,_B7:ciscoErmPolicyViolationNotifGroup})