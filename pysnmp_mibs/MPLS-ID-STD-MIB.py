_I='mplsIdIcc'
_H='mplsIdCc'
_G='mplsIdGlobalId'
_F='mplsIdIccOperatorGroup'
_E='mplsIdIpOperatorGroup'
_D='mplsIdNodeId'
_C='read-write'
_B='current'
_A='MPLS-ID-STD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MplsCcId,MplsGlobalId,MplsIccId,MplsNodeId=mibBuilder.importSymbols('MPLS-TC-EXT-STD-MIB','MplsCcId','MplsGlobalId','MplsIccId','MplsNodeId')
mplsStdMIB,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','mplsStdMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mplsIdStdMIB=ModuleIdentity((1,3,6,1,2,1,10,166,18))
if mibBuilder.loadTexts:mplsIdStdMIB.setRevisions(('2015-02-02 00:00',))
_MplsIdNotifications_ObjectIdentity=ObjectIdentity
mplsIdNotifications=_MplsIdNotifications_ObjectIdentity((1,3,6,1,2,1,10,166,18,0))
_MplsIdObjects_ObjectIdentity=ObjectIdentity
mplsIdObjects=_MplsIdObjects_ObjectIdentity((1,3,6,1,2,1,10,166,18,1))
_MplsIdGlobalId_Type=MplsGlobalId
_MplsIdGlobalId_Object=MibScalar
mplsIdGlobalId=_MplsIdGlobalId_Object((1,3,6,1,2,1,10,166,18,1,1),_MplsIdGlobalId_Type())
mplsIdGlobalId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsIdGlobalId.setStatus(_B)
_MplsIdNodeId_Type=MplsNodeId
_MplsIdNodeId_Object=MibScalar
mplsIdNodeId=_MplsIdNodeId_Object((1,3,6,1,2,1,10,166,18,1,2),_MplsIdNodeId_Type())
mplsIdNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsIdNodeId.setStatus(_B)
_MplsIdCc_Type=MplsCcId
_MplsIdCc_Object=MibScalar
mplsIdCc=_MplsIdCc_Object((1,3,6,1,2,1,10,166,18,1,3),_MplsIdCc_Type())
mplsIdCc.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsIdCc.setStatus(_B)
_MplsIdIcc_Type=MplsIccId
_MplsIdIcc_Object=MibScalar
mplsIdIcc=_MplsIdIcc_Object((1,3,6,1,2,1,10,166,18,1,4),_MplsIdIcc_Type())
mplsIdIcc.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsIdIcc.setStatus(_B)
_MplsIdConformance_ObjectIdentity=ObjectIdentity
mplsIdConformance=_MplsIdConformance_ObjectIdentity((1,3,6,1,2,1,10,166,18,2))
_MplsIdCompliances_ObjectIdentity=ObjectIdentity
mplsIdCompliances=_MplsIdCompliances_ObjectIdentity((1,3,6,1,2,1,10,166,18,2,1))
_MplsIdGroups_ObjectIdentity=ObjectIdentity
mplsIdGroups=_MplsIdGroups_ObjectIdentity((1,3,6,1,2,1,10,166,18,2,2))
mplsIdIpOperatorGroup=ObjectGroup((1,3,6,1,2,1,10,166,18,2,2,1))
mplsIdIpOperatorGroup.setObjects(*((_A,_G),(_A,_D)))
if mibBuilder.loadTexts:mplsIdIpOperatorGroup.setStatus(_B)
mplsIdIccOperatorGroup=ObjectGroup((1,3,6,1,2,1,10,166,18,2,2,2))
mplsIdIccOperatorGroup.setObjects(*((_A,_D),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:mplsIdIccOperatorGroup.setStatus(_B)
mplsIdModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,18,2,1,1))
mplsIdModuleFullCompliance.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:mplsIdModuleFullCompliance.setStatus(_B)
mplsIdModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,18,2,1,2))
mplsIdModuleReadOnlyCompliance.setObjects(*((_A,_E),(_A,_F)))
if mibBuilder.loadTexts:mplsIdModuleReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'mplsIdStdMIB':mplsIdStdMIB,'mplsIdNotifications':mplsIdNotifications,'mplsIdObjects':mplsIdObjects,_G:mplsIdGlobalId,_D:mplsIdNodeId,_H:mplsIdCc,_I:mplsIdIcc,'mplsIdConformance':mplsIdConformance,'mplsIdCompliances':mplsIdCompliances,'mplsIdModuleFullCompliance':mplsIdModuleFullCompliance,'mplsIdModuleReadOnlyCompliance':mplsIdModuleReadOnlyCompliance,'mplsIdGroups':mplsIdGroups,_E:mplsIdIpOperatorGroup,_F:mplsIdIccOperatorGroup})