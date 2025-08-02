_N='ieee8021PreemptionGroup'
_M='ieee8021FramePreemptionHoldRequest'
_L='ieee8021FramePreemptionActive'
_K='ieee8021FramePreemptionReleaseAdvance'
_J='ieee8021FramePreemptionHoldAdvance'
_I='ieee8021FramePreemptionAdminStatus'
_H='ieee8021PreemptionPriority'
_G='ieee8021BridgeBasePort'
_F='ieee8021BridgeBaseComponentId'
_E='read-only'
_D='Integer32'
_C='IEEE8021-BRIDGE-MIB'
_B='IEEE8021-Preemption-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ieee8021BridgeBaseComponentId,ieee8021BridgeBasePort=mibBuilder.importSymbols(_C,_F,_G)
IEEE8021PriorityValue,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PriorityValue','ieee802dot1mibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ieee8021PreemptionMib=ModuleIdentity((1,3,111,2,802,1,1,29))
if mibBuilder.loadTexts:ieee8021PreemptionMib.setRevisions(('2018-06-21 00:00','2016-08-15 00:00'))
_Ieee8021PreemptionNotifications_ObjectIdentity=ObjectIdentity
ieee8021PreemptionNotifications=_Ieee8021PreemptionNotifications_ObjectIdentity((1,3,111,2,802,1,1,29,0))
_Ieee8021PreemptionObjects_ObjectIdentity=ObjectIdentity
ieee8021PreemptionObjects=_Ieee8021PreemptionObjects_ObjectIdentity((1,3,111,2,802,1,1,29,1))
_Ieee8021PreemptionParameters_ObjectIdentity=ObjectIdentity
ieee8021PreemptionParameters=_Ieee8021PreemptionParameters_ObjectIdentity((1,3,111,2,802,1,1,29,1,1))
_Ieee8021PreemptionParameterTable_Object=MibTable
ieee8021PreemptionParameterTable=_Ieee8021PreemptionParameterTable_Object((1,3,111,2,802,1,1,29,1,1,1))
if mibBuilder.loadTexts:ieee8021PreemptionParameterTable.setStatus(_A)
_Ieee8021PreemptionParameterEntry_Object=MibTableRow
ieee8021PreemptionParameterEntry=_Ieee8021PreemptionParameterEntry_Object((1,3,111,2,802,1,1,29,1,1,1,1))
ieee8021PreemptionParameterEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_B,_H))
if mibBuilder.loadTexts:ieee8021PreemptionParameterEntry.setStatus(_A)
_Ieee8021PreemptionPriority_Type=IEEE8021PriorityValue
_Ieee8021PreemptionPriority_Object=MibTableColumn
ieee8021PreemptionPriority=_Ieee8021PreemptionPriority_Object((1,3,111,2,802,1,1,29,1,1,1,1,1),_Ieee8021PreemptionPriority_Type())
ieee8021PreemptionPriority.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ieee8021PreemptionPriority.setStatus(_A)
class _Ieee8021FramePreemptionAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('express',1),('preemptible',2)))
_Ieee8021FramePreemptionAdminStatus_Type.__name__=_D
_Ieee8021FramePreemptionAdminStatus_Object=MibTableColumn
ieee8021FramePreemptionAdminStatus=_Ieee8021FramePreemptionAdminStatus_Object((1,3,111,2,802,1,1,29,1,1,1,1,2),_Ieee8021FramePreemptionAdminStatus_Type())
ieee8021FramePreemptionAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:ieee8021FramePreemptionAdminStatus.setStatus(_A)
_Ieee8021PreemptionConfigTable_Object=MibTable
ieee8021PreemptionConfigTable=_Ieee8021PreemptionConfigTable_Object((1,3,111,2,802,1,1,29,1,1,2))
if mibBuilder.loadTexts:ieee8021PreemptionConfigTable.setStatus(_A)
_Ieee8021PreemptionConfigEntry_Object=MibTableRow
ieee8021PreemptionConfigEntry=_Ieee8021PreemptionConfigEntry_Object((1,3,111,2,802,1,1,29,1,1,2,1))
ieee8021PreemptionConfigEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:ieee8021PreemptionConfigEntry.setStatus(_A)
_Ieee8021FramePreemptionHoldAdvance_Type=Unsigned32
_Ieee8021FramePreemptionHoldAdvance_Object=MibTableColumn
ieee8021FramePreemptionHoldAdvance=_Ieee8021FramePreemptionHoldAdvance_Object((1,3,111,2,802,1,1,29,1,1,2,1,1),_Ieee8021FramePreemptionHoldAdvance_Type())
ieee8021FramePreemptionHoldAdvance.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021FramePreemptionHoldAdvance.setStatus(_A)
_Ieee8021FramePreemptionReleaseAdvance_Type=Unsigned32
_Ieee8021FramePreemptionReleaseAdvance_Object=MibTableColumn
ieee8021FramePreemptionReleaseAdvance=_Ieee8021FramePreemptionReleaseAdvance_Object((1,3,111,2,802,1,1,29,1,1,2,1,2),_Ieee8021FramePreemptionReleaseAdvance_Type())
ieee8021FramePreemptionReleaseAdvance.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021FramePreemptionReleaseAdvance.setStatus(_A)
class _Ieee8021FramePreemptionActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('active',2)))
_Ieee8021FramePreemptionActive_Type.__name__=_D
_Ieee8021FramePreemptionActive_Object=MibTableColumn
ieee8021FramePreemptionActive=_Ieee8021FramePreemptionActive_Object((1,3,111,2,802,1,1,29,1,1,2,1,3),_Ieee8021FramePreemptionActive_Type())
ieee8021FramePreemptionActive.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021FramePreemptionActive.setStatus(_A)
class _Ieee8021FramePreemptionHoldRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hold',1),('release',2)))
_Ieee8021FramePreemptionHoldRequest_Type.__name__=_D
_Ieee8021FramePreemptionHoldRequest_Object=MibTableColumn
ieee8021FramePreemptionHoldRequest=_Ieee8021FramePreemptionHoldRequest_Object((1,3,111,2,802,1,1,29,1,1,2,1,4),_Ieee8021FramePreemptionHoldRequest_Type())
ieee8021FramePreemptionHoldRequest.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021FramePreemptionHoldRequest.setStatus(_A)
_Ieee8021PreemptionConformance_ObjectIdentity=ObjectIdentity
ieee8021PreemptionConformance=_Ieee8021PreemptionConformance_ObjectIdentity((1,3,111,2,802,1,1,29,2))
_Ieee8021PreemptionCompliances_ObjectIdentity=ObjectIdentity
ieee8021PreemptionCompliances=_Ieee8021PreemptionCompliances_ObjectIdentity((1,3,111,2,802,1,1,29,2,1))
_Ieee8021PreemptionGroups_ObjectIdentity=ObjectIdentity
ieee8021PreemptionGroups=_Ieee8021PreemptionGroups_ObjectIdentity((1,3,111,2,802,1,1,29,2,2))
ieee8021PreemptionGroup=ObjectGroup((1,3,111,2,802,1,1,29,2,2,1))
ieee8021PreemptionGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ieee8021PreemptionGroup.setStatus(_A)
ieee8021PreemptionCompliance=ModuleCompliance((1,3,111,2,802,1,1,29,2,1,1))
ieee8021PreemptionCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:ieee8021PreemptionCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8021PreemptionMib':ieee8021PreemptionMib,'ieee8021PreemptionNotifications':ieee8021PreemptionNotifications,'ieee8021PreemptionObjects':ieee8021PreemptionObjects,'ieee8021PreemptionParameters':ieee8021PreemptionParameters,'ieee8021PreemptionParameterTable':ieee8021PreemptionParameterTable,'ieee8021PreemptionParameterEntry':ieee8021PreemptionParameterEntry,_H:ieee8021PreemptionPriority,_I:ieee8021FramePreemptionAdminStatus,'ieee8021PreemptionConfigTable':ieee8021PreemptionConfigTable,'ieee8021PreemptionConfigEntry':ieee8021PreemptionConfigEntry,_J:ieee8021FramePreemptionHoldAdvance,_K:ieee8021FramePreemptionReleaseAdvance,_L:ieee8021FramePreemptionActive,_M:ieee8021FramePreemptionHoldRequest,'ieee8021PreemptionConformance':ieee8021PreemptionConformance,'ieee8021PreemptionCompliances':ieee8021PreemptionCompliances,'ieee8021PreemptionCompliance':ieee8021PreemptionCompliance,'ieee8021PreemptionGroups':ieee8021PreemptionGroups,_N:ieee8021PreemptionGroup})