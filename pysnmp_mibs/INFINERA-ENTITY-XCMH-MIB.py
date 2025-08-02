_L='xcmhGroup'
_K='xcmhRowStatus'
_J='xcmhRedundancyStatus'
_I='xcmhProvType'
_H='xcmhMoId'
_G='read-only'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='xcmhBrandingFault'
_C='read-create'
_B='INFINERA-ENTITY-XCMH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnCorrelatedRedunStatus,InfnEqptType=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnCorrelatedRedunStatus','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
xcmhMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,31))
_XcmhTable_Object=MibTable
xcmhTable=_XcmhTable_Object((1,3,6,1,4,1,21296,2,2,2,1,31,1))
if mibBuilder.loadTexts:xcmhTable.setStatus(_A)
_XcmhEntry_Object=MibTableRow
xcmhEntry=_XcmhEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,31,1,1))
xcmhEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:xcmhEntry.setStatus(_A)
_XcmhMoId_Type=DisplayString
_XcmhMoId_Object=MibTableColumn
xcmhMoId=_XcmhMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,31,1,1,1),_XcmhMoId_Type())
xcmhMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:xcmhMoId.setStatus(_A)
_XcmhProvType_Type=InfnEqptType
_XcmhProvType_Object=MibTableColumn
xcmhProvType=_XcmhProvType_Object((1,3,6,1,4,1,21296,2,2,2,1,31,1,1,2),_XcmhProvType_Type())
xcmhProvType.setMaxAccess(_C)
if mibBuilder.loadTexts:xcmhProvType.setStatus(_A)
_XcmhRedundancyStatus_Type=InfnCorrelatedRedunStatus
_XcmhRedundancyStatus_Object=MibTableColumn
xcmhRedundancyStatus=_XcmhRedundancyStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,31,1,1,3),_XcmhRedundancyStatus_Type())
xcmhRedundancyStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:xcmhRedundancyStatus.setStatus(_A)
_XcmhBrandingFault_Type=TruthValue
_XcmhBrandingFault_Object=MibTableColumn
xcmhBrandingFault=_XcmhBrandingFault_Object((1,3,6,1,4,1,21296,2,2,2,1,31,1,1,4),_XcmhBrandingFault_Type())
xcmhBrandingFault.setMaxAccess(_G)
if mibBuilder.loadTexts:xcmhBrandingFault.setStatus(_A)
_XcmhRowStatus_Type=RowStatus
_XcmhRowStatus_Object=MibTableColumn
xcmhRowStatus=_XcmhRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,31,1,1,5),_XcmhRowStatus_Type())
xcmhRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xcmhRowStatus.setStatus(_A)
_XcmhConformance_ObjectIdentity=ObjectIdentity
xcmhConformance=_XcmhConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,31,3))
_XcmhCompliances_ObjectIdentity=ObjectIdentity
xcmhCompliances=_XcmhCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,31,3,1))
_XcmhGroups_ObjectIdentity=ObjectIdentity
xcmhGroups=_XcmhGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,31,3,2))
xcmhGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,31,3,2,1))
xcmhGroup.setObjects(*((_B,_D),(_B,_H),(_B,_I),(_B,_J),(_B,_D),(_B,_K)))
if mibBuilder.loadTexts:xcmhGroup.setStatus(_A)
xcmhCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,31,3,1,1))
xcmhCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:xcmhCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xcmhMIB':xcmhMIB,'xcmhTable':xcmhTable,'xcmhEntry':xcmhEntry,_H:xcmhMoId,_I:xcmhProvType,_J:xcmhRedundancyStatus,_D:xcmhBrandingFault,_K:xcmhRowStatus,'xcmhConformance':xcmhConformance,'xcmhCompliances':xcmhCompliances,'xcmhCompliance':xcmhCompliance,'xcmhGroups':xcmhGroups,_L:xcmhGroup})