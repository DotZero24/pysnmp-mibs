_G='cmplsIcc'
_F='cmplsNodeId'
_E='cmplsGlobalId'
_D='cmplsIdScalarGroup'
_C='read-write'
_B='CISCO-IETF-MPLS-ID-STD-03-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CMplsGlobalId,CMplsIccId,CMplsNodeId=mibBuilder.importSymbols('CISCO-MPLS-TC-EXT-STD-MIB','CMplsGlobalId','CMplsIccId','CMplsNodeId')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
mplsStdMIB,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','mplsStdMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cmplsIdStdMIB=ModuleIdentity((1,3,6,1,4,1,9,10,147))
if mibBuilder.loadTexts:cmplsIdStdMIB.setRevisions(('2012-04-08 00:00',))
_CmplsIdNotifications_ObjectIdentity=ObjectIdentity
cmplsIdNotifications=_CmplsIdNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,147,0))
_CmplsIdObjects_ObjectIdentity=ObjectIdentity
cmplsIdObjects=_CmplsIdObjects_ObjectIdentity((1,3,6,1,4,1,9,10,147,1))
_CmplsGlobalId_Type=CMplsGlobalId
_CmplsGlobalId_Object=MibScalar
cmplsGlobalId=_CmplsGlobalId_Object((1,3,6,1,4,1,9,10,147,1,1),_CmplsGlobalId_Type())
cmplsGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsGlobalId.setStatus(_A)
_CmplsIcc_Type=CMplsIccId
_CmplsIcc_Object=MibScalar
cmplsIcc=_CmplsIcc_Object((1,3,6,1,4,1,9,10,147,1,2),_CmplsIcc_Type())
cmplsIcc.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsIcc.setStatus(_A)
_CmplsNodeId_Type=CMplsNodeId
_CmplsNodeId_Object=MibScalar
cmplsNodeId=_CmplsNodeId_Object((1,3,6,1,4,1,9,10,147,1,3),_CmplsNodeId_Type())
cmplsNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmplsNodeId.setStatus(_A)
_CmplsIdConformance_ObjectIdentity=ObjectIdentity
cmplsIdConformance=_CmplsIdConformance_ObjectIdentity((1,3,6,1,4,1,9,10,147,2))
_CmplsIdGroups_ObjectIdentity=ObjectIdentity
cmplsIdGroups=_CmplsIdGroups_ObjectIdentity((1,3,6,1,4,1,9,10,147,2,1))
_CmplsIdCompliances_ObjectIdentity=ObjectIdentity
cmplsIdCompliances=_CmplsIdCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,147,2,2))
cmplsIdScalarGroup=ObjectGroup((1,3,6,1,4,1,9,10,147,2,1,1))
cmplsIdScalarGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:cmplsIdScalarGroup.setStatus(_A)
cmplsIdModuleFullCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,147,2,2,1))
cmplsIdModuleFullCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:cmplsIdModuleFullCompliance.setStatus(_A)
cmplsIdModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,147,2,2,2))
cmplsIdModuleReadOnlyCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:cmplsIdModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cmplsIdStdMIB':cmplsIdStdMIB,'cmplsIdNotifications':cmplsIdNotifications,'cmplsIdObjects':cmplsIdObjects,_E:cmplsGlobalId,_G:cmplsIcc,_F:cmplsNodeId,'cmplsIdConformance':cmplsIdConformance,'cmplsIdGroups':cmplsIdGroups,_D:cmplsIdScalarGroup,'cmplsIdCompliances':cmplsIdCompliances,'cmplsIdModuleFullCompliance':cmplsIdModuleFullCompliance,'cmplsIdModuleReadOnlyCompliance':cmplsIdModuleReadOnlyCompliance})