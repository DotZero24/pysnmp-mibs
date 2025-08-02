_O='hpicfSflowInfoGroup1'
_N='hpicfSflowInfoGroup'
_M='hpicfSflowRcvrOobm'
_L='hpicfSflowPortStatus'
_K='hpicfSflowPortMode'
_J='hpicfSflowRcvrEntry'
_I='read-only'
_H='invalid'
_G='TruthValue'
_F='sFlowFsInstance'
_E='sFlowFsDataSource'
_D='Integer32'
_C='SFLOW-MIB'
_B='HP-ICF-SFLOW-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
sFlowFsDataSource,sFlowFsInstance,sFlowRcvrEntry=mibBuilder.importSymbols(_C,_E,_F,'sFlowRcvrEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G)
hpicfSflowMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,92))
if mibBuilder.loadTexts:hpicfSflowMIB.setRevisions(('2012-08-22 00:00','2012-04-30 00:00'))
_HpicfSflowNotifications_ObjectIdentity=ObjectIdentity
hpicfSflowNotifications=_HpicfSflowNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,92,0))
_HpicfSflowObjects_ObjectIdentity=ObjectIdentity
hpicfSflowObjects=_HpicfSflowObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,92,1))
_HpicfSflowInfo_ObjectIdentity=ObjectIdentity
hpicfSflowInfo=_HpicfSflowInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,92,1,1))
_HpicfSflowPortInfoTable_Object=MibTable
hpicfSflowPortInfoTable=_HpicfSflowPortInfoTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,92,1,1,1))
if mibBuilder.loadTexts:hpicfSflowPortInfoTable.setStatus(_A)
_HpicfSflowPortInfoEntry_Object=MibTableRow
hpicfSflowPortInfoEntry=_HpicfSflowPortInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,92,1,1,1,1))
hpicfSflowPortInfoEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:hpicfSflowPortInfoEntry.setStatus(_A)
class _HpicfSflowPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('determine',2),('random',3)))
_HpicfSflowPortMode_Type.__name__=_D
_HpicfSflowPortMode_Object=MibTableColumn
hpicfSflowPortMode=_HpicfSflowPortMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,92,1,1,1,1,1),_HpicfSflowPortMode_Type())
hpicfSflowPortMode.setMaxAccess(_I)
if mibBuilder.loadTexts:hpicfSflowPortMode.setStatus(_A)
class _HpicfSflowPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('active',2),('inactive',3)))
_HpicfSflowPortStatus_Type.__name__=_D
_HpicfSflowPortStatus_Object=MibTableColumn
hpicfSflowPortStatus=_HpicfSflowPortStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,92,1,1,1,1,2),_HpicfSflowPortStatus_Type())
hpicfSflowPortStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpicfSflowPortStatus.setStatus(_A)
_HpicfSflowRcvrTable_Object=MibTable
hpicfSflowRcvrTable=_HpicfSflowRcvrTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,92,1,1,2))
if mibBuilder.loadTexts:hpicfSflowRcvrTable.setStatus(_A)
_HpicfSflowRcvrEntry_Object=MibTableRow
hpicfSflowRcvrEntry=_HpicfSflowRcvrEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,92,1,1,2,1))
if mibBuilder.loadTexts:hpicfSflowRcvrEntry.setStatus(_A)
class _HpicfSflowRcvrOobm_Type(TruthValue):defaultValue=2
_HpicfSflowRcvrOobm_Type.__name__=_G
_HpicfSflowRcvrOobm_Object=MibTableColumn
hpicfSflowRcvrOobm=_HpicfSflowRcvrOobm_Object((1,3,6,1,4,1,11,2,14,11,5,1,92,1,1,2,1,1),_HpicfSflowRcvrOobm_Type())
hpicfSflowRcvrOobm.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfSflowRcvrOobm.setStatus(_A)
_HpicfSflowConformance_ObjectIdentity=ObjectIdentity
hpicfSflowConformance=_HpicfSflowConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,92,2))
_HpicfSflowGroups_ObjectIdentity=ObjectIdentity
hpicfSflowGroups=_HpicfSflowGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,92,2,1))
_HpicfSflowCompliances_ObjectIdentity=ObjectIdentity
hpicfSflowCompliances=_HpicfSflowCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,92,2,2))
sFlowRcvrEntry.registerAugmentions((_B,_J))
hpicfSflowRcvrEntry.setIndexNames(*sFlowRcvrEntry.getIndexNames())
hpicfSflowInfoGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,92,2,1,1))
hpicfSflowInfoGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:hpicfSflowInfoGroup.setStatus(_A)
hpicfSflowInfoGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,92,2,1,2))
hpicfSflowInfoGroup1.setObjects((_B,_M))
if mibBuilder.loadTexts:hpicfSflowInfoGroup1.setStatus(_A)
hpicfSflowCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,92,2,2,1))
hpicfSflowCompliance.setObjects((_B,_N))
if mibBuilder.loadTexts:hpicfSflowCompliance.setStatus(_A)
hpicfSflowCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,92,2,2,2))
hpicfSflowCompliance1.setObjects((_B,_O))
if mibBuilder.loadTexts:hpicfSflowCompliance1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfSflowMIB':hpicfSflowMIB,'hpicfSflowNotifications':hpicfSflowNotifications,'hpicfSflowObjects':hpicfSflowObjects,'hpicfSflowInfo':hpicfSflowInfo,'hpicfSflowPortInfoTable':hpicfSflowPortInfoTable,'hpicfSflowPortInfoEntry':hpicfSflowPortInfoEntry,_K:hpicfSflowPortMode,_L:hpicfSflowPortStatus,'hpicfSflowRcvrTable':hpicfSflowRcvrTable,_J:hpicfSflowRcvrEntry,_M:hpicfSflowRcvrOobm,'hpicfSflowConformance':hpicfSflowConformance,'hpicfSflowGroups':hpicfSflowGroups,_N:hpicfSflowInfoGroup,_O:hpicfSflowInfoGroup1,'hpicfSflowCompliances':hpicfSflowCompliances,'hpicfSflowCompliance':hpicfSflowCompliance,'hpicfSflowCompliance1':hpicfSflowCompliance1})