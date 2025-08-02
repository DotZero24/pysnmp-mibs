_P='clearChannelCtpGroup'
_O='clearChannelCtpServiceModeQualifier'
_N='clearChannelCtpServiceMode'
_M='clearChannelCtpConfiguredServiceType'
_L='clearChannelCtpPmHistStatsEnable'
_K='clearChannelCtpLoopback'
_J='clearChannelCtpSupportingCircuitIdList'
_I='read-write'
_H='InfnServiceMode'
_G='InfnSMQ'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='INFINERA-TP-CLEARCHANNELCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnSMQ,InfnServiceMode,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths',_G,_H,'InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
clearChannelCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,9))
if mibBuilder.loadTexts:clearChannelCtpMIB.setRevisions(('2008-02-18 00:00',))
_ClearChannelCtpTable_Object=MibTable
clearChannelCtpTable=_ClearChannelCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,9,1))
if mibBuilder.loadTexts:clearChannelCtpTable.setStatus(_A)
_ClearChannelCtpEntry_Object=MibTableRow
clearChannelCtpEntry=_ClearChannelCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,9,1,1))
clearChannelCtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:clearChannelCtpEntry.setStatus(_A)
_ClearChannelCtpSupportingCircuitIdList_Type=DisplayString
_ClearChannelCtpSupportingCircuitIdList_Object=MibTableColumn
clearChannelCtpSupportingCircuitIdList=_ClearChannelCtpSupportingCircuitIdList_Object((1,3,6,1,4,1,21296,2,2,2,2,9,1,1,1),_ClearChannelCtpSupportingCircuitIdList_Type())
clearChannelCtpSupportingCircuitIdList.setMaxAccess(_C)
if mibBuilder.loadTexts:clearChannelCtpSupportingCircuitIdList.setStatus(_A)
class _ClearChannelCtpLoopback_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('terminal',2),('facility',3)))
_ClearChannelCtpLoopback_Type.__name__=_D
_ClearChannelCtpLoopback_Object=MibTableColumn
clearChannelCtpLoopback=_ClearChannelCtpLoopback_Object((1,3,6,1,4,1,21296,2,2,2,2,9,1,1,2),_ClearChannelCtpLoopback_Type())
clearChannelCtpLoopback.setMaxAccess(_I)
if mibBuilder.loadTexts:clearChannelCtpLoopback.setStatus(_A)
class _ClearChannelCtpPmHistStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ClearChannelCtpPmHistStatsEnable_Type.__name__=_D
_ClearChannelCtpPmHistStatsEnable_Object=MibTableColumn
clearChannelCtpPmHistStatsEnable=_ClearChannelCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,9,1,1,3),_ClearChannelCtpPmHistStatsEnable_Type())
clearChannelCtpPmHistStatsEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:clearChannelCtpPmHistStatsEnable.setStatus('obsolete')
_ClearChannelCtpConfiguredServiceType_Type=InfnServiceType
_ClearChannelCtpConfiguredServiceType_Object=MibTableColumn
clearChannelCtpConfiguredServiceType=_ClearChannelCtpConfiguredServiceType_Object((1,3,6,1,4,1,21296,2,2,2,2,9,1,1,4),_ClearChannelCtpConfiguredServiceType_Type())
clearChannelCtpConfiguredServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:clearChannelCtpConfiguredServiceType.setStatus(_A)
class _ClearChannelCtpServiceMode_Type(InfnServiceMode):defaultValue=1
_ClearChannelCtpServiceMode_Type.__name__=_H
_ClearChannelCtpServiceMode_Object=MibTableColumn
clearChannelCtpServiceMode=_ClearChannelCtpServiceMode_Object((1,3,6,1,4,1,21296,2,2,2,2,9,1,1,5),_ClearChannelCtpServiceMode_Type())
clearChannelCtpServiceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:clearChannelCtpServiceMode.setStatus(_A)
class _ClearChannelCtpServiceModeQualifier_Type(InfnSMQ):defaultValue=1
_ClearChannelCtpServiceModeQualifier_Type.__name__=_G
_ClearChannelCtpServiceModeQualifier_Object=MibTableColumn
clearChannelCtpServiceModeQualifier=_ClearChannelCtpServiceModeQualifier_Object((1,3,6,1,4,1,21296,2,2,2,2,9,1,1,6),_ClearChannelCtpServiceModeQualifier_Type())
clearChannelCtpServiceModeQualifier.setMaxAccess(_C)
if mibBuilder.loadTexts:clearChannelCtpServiceModeQualifier.setStatus(_A)
_ClearChannelCtpConformance_ObjectIdentity=ObjectIdentity
clearChannelCtpConformance=_ClearChannelCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,9,3))
_ClearChannelCtpCompliances_ObjectIdentity=ObjectIdentity
clearChannelCtpCompliances=_ClearChannelCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,9,3,1))
_ClearChannelCtpGroups_ObjectIdentity=ObjectIdentity
clearChannelCtpGroups=_ClearChannelCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,9,3,2))
clearChannelCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,9,3,2,1))
clearChannelCtpGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:clearChannelCtpGroup.setStatus(_A)
clearChannelCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,9,3,1,1))
clearChannelCtpCompliance.setObjects((_B,_P))
if mibBuilder.loadTexts:clearChannelCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'clearChannelCtpMIB':clearChannelCtpMIB,'clearChannelCtpTable':clearChannelCtpTable,'clearChannelCtpEntry':clearChannelCtpEntry,_J:clearChannelCtpSupportingCircuitIdList,_K:clearChannelCtpLoopback,_L:clearChannelCtpPmHistStatsEnable,_M:clearChannelCtpConfiguredServiceType,_N:clearChannelCtpServiceMode,_O:clearChannelCtpServiceModeQualifier,'clearChannelCtpConformance':clearChannelCtpConformance,'clearChannelCtpCompliances':clearChannelCtpCompliances,'clearChannelCtpCompliance':clearChannelCtpCompliance,'clearChannelCtpGroups':clearChannelCtpGroups,_P:clearChannelCtpGroup})