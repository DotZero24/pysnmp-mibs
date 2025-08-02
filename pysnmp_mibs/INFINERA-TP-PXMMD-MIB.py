_K='mdGroup'
_J='mdSenderIDTLV'
_I='mdMHFCreationCriteria'
_H='mdMDNameFormat'
_G='mdLevel'
_F='mdName'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='INFINERA-TP-PXMMD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnMDNameFormat,InfnMHFCreationCriteria,InfnSenderIDTLV=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnMDNameFormat','InfnMHFCreationCriteria','InfnSenderIDTLV')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mdMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,78))
_MdTable_Object=MibTable
mdTable=_MdTable_Object((1,3,6,1,4,1,21296,2,2,2,2,78,1))
if mibBuilder.loadTexts:mdTable.setStatus(_A)
_MdEntry_Object=MibTableRow
mdEntry=_MdEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,78,1,1))
mdEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:mdEntry.setStatus(_A)
_MdName_Type=DisplayString
_MdName_Object=MibTableColumn
mdName=_MdName_Object((1,3,6,1,4,1,21296,2,2,2,2,78,1,1,1),_MdName_Type())
mdName.setMaxAccess(_C)
if mibBuilder.loadTexts:mdName.setStatus(_A)
_MdLevel_Type=Integer32
_MdLevel_Object=MibTableColumn
mdLevel=_MdLevel_Object((1,3,6,1,4,1,21296,2,2,2,2,78,1,1,2),_MdLevel_Type())
mdLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:mdLevel.setStatus(_A)
_MdMDNameFormat_Type=InfnMDNameFormat
_MdMDNameFormat_Object=MibTableColumn
mdMDNameFormat=_MdMDNameFormat_Object((1,3,6,1,4,1,21296,2,2,2,2,78,1,1,3),_MdMDNameFormat_Type())
mdMDNameFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:mdMDNameFormat.setStatus(_A)
_MdMHFCreationCriteria_Type=InfnMHFCreationCriteria
_MdMHFCreationCriteria_Object=MibTableColumn
mdMHFCreationCriteria=_MdMHFCreationCriteria_Object((1,3,6,1,4,1,21296,2,2,2,2,78,1,1,4),_MdMHFCreationCriteria_Type())
mdMHFCreationCriteria.setMaxAccess(_C)
if mibBuilder.loadTexts:mdMHFCreationCriteria.setStatus(_A)
_MdSenderIDTLV_Type=InfnSenderIDTLV
_MdSenderIDTLV_Object=MibTableColumn
mdSenderIDTLV=_MdSenderIDTLV_Object((1,3,6,1,4,1,21296,2,2,2,2,78,1,1,5),_MdSenderIDTLV_Type())
mdSenderIDTLV.setMaxAccess(_C)
if mibBuilder.loadTexts:mdSenderIDTLV.setStatus(_A)
_MdConformance_ObjectIdentity=ObjectIdentity
mdConformance=_MdConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,78,3))
_MdCompliances_ObjectIdentity=ObjectIdentity
mdCompliances=_MdCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,78,3,1))
_MdGroups_ObjectIdentity=ObjectIdentity
mdGroups=_MdGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,78,3,2))
mdGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,78,3,2,1))
mdGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:mdGroup.setStatus(_A)
mdCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,78,3,1,1))
mdCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:mdCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mdMIB':mdMIB,'mdTable':mdTable,'mdEntry':mdEntry,_F:mdName,_G:mdLevel,_H:mdMDNameFormat,_I:mdMHFCreationCriteria,_J:mdSenderIDTLV,'mdConformance':mdConformance,'mdCompliances':mdCompliances,'mdCompliance':mdCompliance,'mdGroups':mdGroups,_K:mdGroup})