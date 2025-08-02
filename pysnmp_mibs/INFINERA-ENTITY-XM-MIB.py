_M='xmGroup'
_L='xmEccStatus'
_K='actvTimingSource'
_J='xmRowStatus'
_I='xmProvEqptType'
_H='cardRedundancyStatus'
_G='xmMoId'
_F='read-create'
_E='entLPPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='INFINERA-ENTITY-XM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,InfnOxmCardRedundancyStatus,InfnOxmEccStatus=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType','InfnOxmCardRedundancyStatus','InfnOxmEccStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
xmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,20))
_XmTable_Object=MibTable
xmTable=_XmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,20,1))
if mibBuilder.loadTexts:xmTable.setStatus(_A)
_XmEntry_Object=MibTableRow
xmEntry=_XmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,20,1,1))
xmEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:xmEntry.setStatus(_A)
_XmMoId_Type=DisplayString
_XmMoId_Object=MibTableColumn
xmMoId=_XmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,20,1,1,1),_XmMoId_Type())
xmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:xmMoId.setStatus(_A)
_CardRedundancyStatus_Type=InfnOxmCardRedundancyStatus
_CardRedundancyStatus_Object=MibTableColumn
cardRedundancyStatus=_CardRedundancyStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,20,1,1,2),_CardRedundancyStatus_Type())
cardRedundancyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cardRedundancyStatus.setStatus(_A)
_XmProvEqptType_Type=InfnEqptType
_XmProvEqptType_Object=MibTableColumn
xmProvEqptType=_XmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,20,1,1,3),_XmProvEqptType_Type())
xmProvEqptType.setMaxAccess(_F)
if mibBuilder.loadTexts:xmProvEqptType.setStatus(_A)
_XmRowStatus_Type=RowStatus
_XmRowStatus_Object=MibTableColumn
xmRowStatus=_XmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,20,1,1,4),_XmRowStatus_Type())
xmRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:xmRowStatus.setStatus(_A)
_ActvTimingSource_Type=DisplayString
_ActvTimingSource_Object=MibTableColumn
actvTimingSource=_ActvTimingSource_Object((1,3,6,1,4,1,21296,2,2,2,1,20,1,1,5),_ActvTimingSource_Type())
actvTimingSource.setMaxAccess(_C)
if mibBuilder.loadTexts:actvTimingSource.setStatus(_A)
_XmEccStatus_Type=InfnOxmEccStatus
_XmEccStatus_Object=MibTableColumn
xmEccStatus=_XmEccStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,20,1,1,6),_XmEccStatus_Type())
xmEccStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xmEccStatus.setStatus(_A)
_XmConformance_ObjectIdentity=ObjectIdentity
xmConformance=_XmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,20,3))
_XmCompliances_ObjectIdentity=ObjectIdentity
xmCompliances=_XmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,20,3,1))
_XmGroups_ObjectIdentity=ObjectIdentity
xmGroups=_XmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,20,3,2))
xmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,20,3,2,1))
xmGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:xmGroup.setStatus(_A)
xmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,20,3,1,1))
xmCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:xmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xmMIB':xmMIB,'xmTable':xmTable,'xmEntry':xmEntry,_G:xmMoId,_H:cardRedundancyStatus,_I:xmProvEqptType,_J:xmRowStatus,_K:actvTimingSource,_L:xmEccStatus,'xmConformance':xmConformance,'xmCompliances':xmCompliances,'xmCompliance':xmCompliance,'xmGroups':xmGroups,_M:xmGroup})