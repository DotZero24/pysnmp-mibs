_M='scmGroup'
_L='scmAssociatedDegree'
_K='scmProvisionedRemoteSCM'
_J='scmIdlerVoaAttenuation'
_I='scmRowStatus'
_H='scmProvEqptType'
_G='scmMoId'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='read-write'
_C='read-create'
_B='INFINERA-ENTITY-SCM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,InfnEqptType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
scmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,18))
_ScmTable_Object=MibTable
scmTable=_ScmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,18,1))
if mibBuilder.loadTexts:scmTable.setStatus(_A)
_ScmEntry_Object=MibTableRow
scmEntry=_ScmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,18,1,1))
scmEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:scmEntry.setStatus(_A)
_ScmMoId_Type=DisplayString
_ScmMoId_Object=MibTableColumn
scmMoId=_ScmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,18,1,1,1),_ScmMoId_Type())
scmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:scmMoId.setStatus(_A)
_ScmProvEqptType_Type=InfnEqptType
_ScmProvEqptType_Object=MibTableColumn
scmProvEqptType=_ScmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,18,1,1,2),_ScmProvEqptType_Type())
scmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:scmProvEqptType.setStatus(_A)
_ScmIdlerVoaAttenuation_Type=FloatTenths
_ScmIdlerVoaAttenuation_Object=MibTableColumn
scmIdlerVoaAttenuation=_ScmIdlerVoaAttenuation_Object((1,3,6,1,4,1,21296,2,2,2,1,18,1,1,3),_ScmIdlerVoaAttenuation_Type())
scmIdlerVoaAttenuation.setMaxAccess(_D)
if mibBuilder.loadTexts:scmIdlerVoaAttenuation.setStatus(_A)
_ScmProvisionedRemoteSCM_Type=DisplayString
_ScmProvisionedRemoteSCM_Object=MibTableColumn
scmProvisionedRemoteSCM=_ScmProvisionedRemoteSCM_Object((1,3,6,1,4,1,21296,2,2,2,1,18,1,1,4),_ScmProvisionedRemoteSCM_Type())
scmProvisionedRemoteSCM.setMaxAccess(_D)
if mibBuilder.loadTexts:scmProvisionedRemoteSCM.setStatus(_A)
_ScmAssociatedDegree_Type=DisplayString
_ScmAssociatedDegree_Object=MibTableColumn
scmAssociatedDegree=_ScmAssociatedDegree_Object((1,3,6,1,4,1,21296,2,2,2,1,18,1,1,5),_ScmAssociatedDegree_Type())
scmAssociatedDegree.setMaxAccess(_D)
if mibBuilder.loadTexts:scmAssociatedDegree.setStatus(_A)
_ScmRowStatus_Type=RowStatus
_ScmRowStatus_Object=MibTableColumn
scmRowStatus=_ScmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,18,1,1,6),_ScmRowStatus_Type())
scmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:scmRowStatus.setStatus(_A)
_ScmConformance_ObjectIdentity=ObjectIdentity
scmConformance=_ScmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,18,3))
_ScmCompliances_ObjectIdentity=ObjectIdentity
scmCompliances=_ScmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,18,3,1))
_ScmGroups_ObjectIdentity=ObjectIdentity
scmGroups=_ScmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,18,3,2))
scmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,18,3,2,1))
scmGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:scmGroup.setStatus(_A)
scmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,18,3,1,1))
scmCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:scmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'scmMIB':scmMIB,'scmTable':scmTable,'scmEntry':scmEntry,_G:scmMoId,_H:scmProvEqptType,_J:scmIdlerVoaAttenuation,_K:scmProvisionedRemoteSCM,_L:scmAssociatedDegree,_I:scmRowStatus,'scmConformance':scmConformance,'scmCompliances':scmCompliances,'scmCompliance':scmCompliance,'scmGroups':scmGroups,_M:scmGroup})