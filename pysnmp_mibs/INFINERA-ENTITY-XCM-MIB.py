_M='xcmGroup'
_L='timingSrcRedunState'
_K='xcmRowStatus'
_J='xcmRedundancyStatus'
_I='xcmProvType'
_H='xcmMoId'
_G='xcmBrandingFault'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='read-create'
_B='INFINERA-ENTITY-XCM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnCorrelatedRedunStatus,InfnEqptType,InfnXcmTimingSrcRedunState=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnCorrelatedRedunStatus','InfnEqptType','InfnXcmTimingSrcRedunState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
xcmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,21))
_XcmTable_Object=MibTable
xcmTable=_XcmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,21,1))
if mibBuilder.loadTexts:xcmTable.setStatus(_A)
_XcmEntry_Object=MibTableRow
xcmEntry=_XcmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,21,1,1))
xcmEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:xcmEntry.setStatus(_A)
_XcmMoId_Type=DisplayString
_XcmMoId_Object=MibTableColumn
xcmMoId=_XcmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,21,1,1,1),_XcmMoId_Type())
xcmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:xcmMoId.setStatus(_A)
_XcmProvType_Type=InfnEqptType
_XcmProvType_Object=MibTableColumn
xcmProvType=_XcmProvType_Object((1,3,6,1,4,1,21296,2,2,2,1,21,1,1,2),_XcmProvType_Type())
xcmProvType.setMaxAccess(_C)
if mibBuilder.loadTexts:xcmProvType.setStatus(_A)
_XcmRedundancyStatus_Type=InfnCorrelatedRedunStatus
_XcmRedundancyStatus_Object=MibTableColumn
xcmRedundancyStatus=_XcmRedundancyStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,21,1,1,3),_XcmRedundancyStatus_Type())
xcmRedundancyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:xcmRedundancyStatus.setStatus(_A)
_XcmBrandingFault_Type=TruthValue
_XcmBrandingFault_Object=MibTableColumn
xcmBrandingFault=_XcmBrandingFault_Object((1,3,6,1,4,1,21296,2,2,2,1,21,1,1,4),_XcmBrandingFault_Type())
xcmBrandingFault.setMaxAccess(_D)
if mibBuilder.loadTexts:xcmBrandingFault.setStatus(_A)
_XcmRowStatus_Type=RowStatus
_XcmRowStatus_Object=MibTableColumn
xcmRowStatus=_XcmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,21,1,1,5),_XcmRowStatus_Type())
xcmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xcmRowStatus.setStatus(_A)
_TimingSrcRedunState_Type=InfnXcmTimingSrcRedunState
_TimingSrcRedunState_Object=MibTableColumn
timingSrcRedunState=_TimingSrcRedunState_Object((1,3,6,1,4,1,21296,2,2,2,1,21,1,1,6),_TimingSrcRedunState_Type())
timingSrcRedunState.setMaxAccess(_D)
if mibBuilder.loadTexts:timingSrcRedunState.setStatus(_A)
_XcmConformance_ObjectIdentity=ObjectIdentity
xcmConformance=_XcmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,21,3))
_XcmCompliances_ObjectIdentity=ObjectIdentity
xcmCompliances=_XcmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,21,3,1))
_XcmGroups_ObjectIdentity=ObjectIdentity
xcmGroups=_XcmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,21,3,2))
xcmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,21,3,2,1))
xcmGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:xcmGroup.setStatus(_A)
xcmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,21,3,1,1))
xcmCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:xcmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xcmMIB':xcmMIB,'xcmTable':xcmTable,'xcmEntry':xcmEntry,_H:xcmMoId,_I:xcmProvType,_J:xcmRedundancyStatus,_G:xcmBrandingFault,_K:xcmRowStatus,_L:timingSrcRedunState,'xcmConformance':xcmConformance,'xcmCompliances':xcmCompliances,'xcmCompliance':xcmCompliance,'xcmGroups':xcmGroups,_M:xcmGroup})