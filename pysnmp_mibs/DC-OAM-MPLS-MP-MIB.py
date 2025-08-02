_O='mplsMpLoopback'
_N='mplsMpProactiveBfdConnVerif'
_M='mplsMpProactiveBfdContCheck'
_L='mplsMpOperStatus'
_K='mplsMpAdminStatus'
_J='mplsMpRowStatus'
_I='mplsMpIndex'
_H='oammEntApplIndex'
_G='DC-OAMM-MIB'
_F='AdminStatus'
_E='mplsMpGeneralGroup'
_D='TruthValue'
_C='read-create'
_B='DC-OAM-MPLS-MP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AdminStatus,BaseOperStatus,NumericIndex=mibBuilder.importSymbols('DC-MASTER-TC',_F,'BaseOperStatus','NumericIndex')
oammEntApplIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
mplsMpMib=ModuleIdentity((1,3,6,1,4,1,629,10,16))
if mibBuilder.loadTexts:mplsMpMib.setRevisions(('2014-12-21 00:00',))
_Nbase_ObjectIdentity=ObjectIdentity
nbase=_Nbase_ObjectIdentity((1,3,6,1,4,1,629))
_Opx_ObjectIdentity=ObjectIdentity
opx=_Opx_ObjectIdentity((1,3,6,1,4,1,629,10))
_MplsMpObjects_ObjectIdentity=ObjectIdentity
mplsMpObjects=_MplsMpObjects_ObjectIdentity((1,3,6,1,4,1,629,10,16,1))
_MplsMpTable_Object=MibTable
mplsMpTable=_MplsMpTable_Object((1,3,6,1,4,1,629,10,16,1,2))
if mibBuilder.loadTexts:mplsMpTable.setStatus(_A)
_MplsMpEntry_Object=MibTableRow
mplsMpEntry=_MplsMpEntry_Object((1,3,6,1,4,1,629,10,16,1,2,1))
mplsMpEntry.setIndexNames((0,_G,_H),(0,_B,_I))
if mibBuilder.loadTexts:mplsMpEntry.setStatus(_A)
_MplsMpIndex_Type=NumericIndex
_MplsMpIndex_Object=MibTableColumn
mplsMpIndex=_MplsMpIndex_Object((1,3,6,1,4,1,629,10,16,1,2,1,1),_MplsMpIndex_Type())
mplsMpIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:mplsMpIndex.setStatus(_A)
_MplsMpRowStatus_Type=RowStatus
_MplsMpRowStatus_Object=MibTableColumn
mplsMpRowStatus=_MplsMpRowStatus_Object((1,3,6,1,4,1,629,10,16,1,2,1,2),_MplsMpRowStatus_Type())
mplsMpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpRowStatus.setStatus(_A)
class _MplsMpAdminStatus_Type(AdminStatus):defaultValue=1
_MplsMpAdminStatus_Type.__name__=_F
_MplsMpAdminStatus_Object=MibTableColumn
mplsMpAdminStatus=_MplsMpAdminStatus_Object((1,3,6,1,4,1,629,10,16,1,2,1,3),_MplsMpAdminStatus_Type())
mplsMpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpAdminStatus.setStatus(_A)
_MplsMpOperStatus_Type=BaseOperStatus
_MplsMpOperStatus_Object=MibTableColumn
mplsMpOperStatus=_MplsMpOperStatus_Object((1,3,6,1,4,1,629,10,16,1,2,1,4),_MplsMpOperStatus_Type())
mplsMpOperStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:mplsMpOperStatus.setStatus(_A)
class _MplsMpProactiveBfdContCheck_Type(TruthValue):defaultValue=2
_MplsMpProactiveBfdContCheck_Type.__name__=_D
_MplsMpProactiveBfdContCheck_Object=MibTableColumn
mplsMpProactiveBfdContCheck=_MplsMpProactiveBfdContCheck_Object((1,3,6,1,4,1,629,10,16,1,2,1,5),_MplsMpProactiveBfdContCheck_Type())
mplsMpProactiveBfdContCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpProactiveBfdContCheck.setStatus(_A)
class _MplsMpProactiveBfdConnVerif_Type(TruthValue):defaultValue=2
_MplsMpProactiveBfdConnVerif_Type.__name__=_D
_MplsMpProactiveBfdConnVerif_Object=MibTableColumn
mplsMpProactiveBfdConnVerif=_MplsMpProactiveBfdConnVerif_Object((1,3,6,1,4,1,629,10,16,1,2,1,6),_MplsMpProactiveBfdConnVerif_Type())
mplsMpProactiveBfdConnVerif.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpProactiveBfdConnVerif.setStatus(_A)
class _MplsMpLoopback_Type(TruthValue):defaultValue=2
_MplsMpLoopback_Type.__name__=_D
_MplsMpLoopback_Object=MibTableColumn
mplsMpLoopback=_MplsMpLoopback_Object((1,3,6,1,4,1,629,10,16,1,2,1,100),_MplsMpLoopback_Type())
mplsMpLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsMpLoopback.setStatus(_A)
_MplsMpConformance_ObjectIdentity=ObjectIdentity
mplsMpConformance=_MplsMpConformance_ObjectIdentity((1,3,6,1,4,1,629,10,16,2))
_MplsMpGroups_ObjectIdentity=ObjectIdentity
mplsMpGroups=_MplsMpGroups_ObjectIdentity((1,3,6,1,4,1,629,10,16,2,1))
_MplsMpCompliances_ObjectIdentity=ObjectIdentity
mplsMpCompliances=_MplsMpCompliances_ObjectIdentity((1,3,6,1,4,1,629,10,16,2,2))
mplsMpGeneralGroup=ObjectGroup((1,3,6,1,4,1,629,10,16,2,1,1))
mplsMpGeneralGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:mplsMpGeneralGroup.setStatus(_A)
mplsMpModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,629,10,16,2,2,1))
mplsMpModuleFullCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:mplsMpModuleFullCompliance.setStatus(_A)
mplsMpModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,629,10,16,2,2,2))
mplsMpModuleReadOnlyCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:mplsMpModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'nbase':nbase,'opx':opx,'mplsMpMib':mplsMpMib,'mplsMpObjects':mplsMpObjects,'mplsMpTable':mplsMpTable,'mplsMpEntry':mplsMpEntry,_I:mplsMpIndex,_J:mplsMpRowStatus,_K:mplsMpAdminStatus,_L:mplsMpOperStatus,_M:mplsMpProactiveBfdContCheck,_N:mplsMpProactiveBfdConnVerif,_O:mplsMpLoopback,'mplsMpConformance':mplsMpConformance,'mplsMpGroups':mplsMpGroups,_E:mplsMpGeneralGroup,'mplsMpCompliances':mplsMpCompliances,'mplsMpModuleFullCompliance':mplsMpModuleFullCompliance,'mplsMpModuleReadOnlyCompliance':mplsMpModuleReadOnlyCompliance})