_Z='ciscoSanTapDVTConfigGroup1'
_Y='ciscoSanTapDVTConfigGroup'
_X='ciscoSanTapServiceConfigGroup'
_W='cstDVTIOTimeout'
_V='cstDVTLunSizeHandling'
_U='cstCVTName'
_T='cstDVTPortWwn'
_S='TruthValue'
_R='Unsigned32'
_Q='ciscoSanTapServiceConfigGroupRev1'
_P='cstDVTRowStatus'
_O='cstDVTName'
_N='cstDVTPort'
_M='cstDVTTargetVsan'
_L='cstServiceConfigRowStatus'
_K='cstCVTPortWwn'
_J='cstCVTNodeWwn'
_I='read-only'
_H='SnmpAdminString'
_G='vsanIndex'
_F='CISCO-VSAN-MIB'
_E='deprecated'
_D='cstModuleId'
_C='read-create'
_B='current'
_A='CISCO-SANTAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcNameId,FcNameIdOrZero,VsanIndex=mibBuilder.importSymbols('CISCO-ST-TC','FcNameId','FcNameIdOrZero','VsanIndex')
vsanIndex,=mibBuilder.importSymbols(_F,_G)
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_R,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_S)
ciscoSanTapMIB=ModuleIdentity((1,3,6,1,4,1,9,9,463))
if mibBuilder.loadTexts:ciscoSanTapMIB.setRevisions(('2006-03-16 00:00','2005-10-27 00:00','2005-02-02 00:00'))
_CiscoSanTapMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSanTapMIBObjects=_CiscoSanTapMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,463,1))
_CstModuleTable_Object=MibTable
cstModuleTable=_CstModuleTable_Object((1,3,6,1,4,1,9,9,463,1,1))
if mibBuilder.loadTexts:cstModuleTable.setStatus(_B)
_CstModuleEntry_Object=MibTableRow
cstModuleEntry=_CstModuleEntry_Object((1,3,6,1,4,1,9,9,463,1,1,1))
cstModuleEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:cstModuleEntry.setStatus(_B)
_CstModuleId_Type=PhysicalIndex
_CstModuleId_Object=MibTableColumn
cstModuleId=_CstModuleId_Object((1,3,6,1,4,1,9,9,463,1,1,1,1),_CstModuleId_Type())
cstModuleId.setMaxAccess(_I)
if mibBuilder.loadTexts:cstModuleId.setStatus(_B)
_CstServiceConfigTable_Object=MibTable
cstServiceConfigTable=_CstServiceConfigTable_Object((1,3,6,1,4,1,9,9,463,1,2))
if mibBuilder.loadTexts:cstServiceConfigTable.setStatus(_B)
_CstServiceConfigEntry_Object=MibTableRow
cstServiceConfigEntry=_CstServiceConfigEntry_Object((1,3,6,1,4,1,9,9,463,1,2,1))
cstServiceConfigEntry.setIndexNames((0,_A,_D),(0,_F,_G))
if mibBuilder.loadTexts:cstServiceConfigEntry.setStatus(_B)
_CstCVTNodeWwn_Type=FcNameIdOrZero
_CstCVTNodeWwn_Object=MibTableColumn
cstCVTNodeWwn=_CstCVTNodeWwn_Object((1,3,6,1,4,1,9,9,463,1,2,1,1),_CstCVTNodeWwn_Type())
cstCVTNodeWwn.setMaxAccess(_I)
if mibBuilder.loadTexts:cstCVTNodeWwn.setStatus(_B)
_CstCVTPortWwn_Type=FcNameIdOrZero
_CstCVTPortWwn_Object=MibTableColumn
cstCVTPortWwn=_CstCVTPortWwn_Object((1,3,6,1,4,1,9,9,463,1,2,1,2),_CstCVTPortWwn_Type())
cstCVTPortWwn.setMaxAccess(_I)
if mibBuilder.loadTexts:cstCVTPortWwn.setStatus(_B)
_CstServiceConfigRowStatus_Type=RowStatus
_CstServiceConfigRowStatus_Object=MibTableColumn
cstServiceConfigRowStatus=_CstServiceConfigRowStatus_Object((1,3,6,1,4,1,9,9,463,1,2,1,3),_CstServiceConfigRowStatus_Type())
cstServiceConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cstServiceConfigRowStatus.setStatus(_B)
class _CstCVTName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CstCVTName_Type.__name__=_H
_CstCVTName_Object=MibTableColumn
cstCVTName=_CstCVTName_Object((1,3,6,1,4,1,9,9,463,1,2,1,4),_CstCVTName_Type())
cstCVTName.setMaxAccess(_C)
if mibBuilder.loadTexts:cstCVTName.setStatus(_B)
_CstDVTConfigTable_Object=MibTable
cstDVTConfigTable=_CstDVTConfigTable_Object((1,3,6,1,4,1,9,9,463,1,3))
if mibBuilder.loadTexts:cstDVTConfigTable.setStatus(_B)
_CstDVTConfigEntry_Object=MibTableRow
cstDVTConfigEntry=_CstDVTConfigEntry_Object((1,3,6,1,4,1,9,9,463,1,3,1))
cstDVTConfigEntry.setIndexNames((0,_F,_G),(0,_A,_T))
if mibBuilder.loadTexts:cstDVTConfigEntry.setStatus(_B)
_CstDVTPortWwn_Type=FcNameId
_CstDVTPortWwn_Object=MibTableColumn
cstDVTPortWwn=_CstDVTPortWwn_Object((1,3,6,1,4,1,9,9,463,1,3,1,1),_CstDVTPortWwn_Type())
cstDVTPortWwn.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cstDVTPortWwn.setStatus(_B)
_CstDVTTargetVsan_Type=VsanIndex
_CstDVTTargetVsan_Object=MibTableColumn
cstDVTTargetVsan=_CstDVTTargetVsan_Object((1,3,6,1,4,1,9,9,463,1,3,1,2),_CstDVTTargetVsan_Type())
cstDVTTargetVsan.setMaxAccess(_C)
if mibBuilder.loadTexts:cstDVTTargetVsan.setStatus(_B)
_CstDVTPort_Type=InterfaceIndex
_CstDVTPort_Object=MibTableColumn
cstDVTPort=_CstDVTPort_Object((1,3,6,1,4,1,9,9,463,1,3,1,3),_CstDVTPort_Type())
cstDVTPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cstDVTPort.setStatus(_B)
class _CstDVTName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CstDVTName_Type.__name__=_H
_CstDVTName_Object=MibTableColumn
cstDVTName=_CstDVTName_Object((1,3,6,1,4,1,9,9,463,1,3,1,4),_CstDVTName_Type())
cstDVTName.setMaxAccess(_C)
if mibBuilder.loadTexts:cstDVTName.setStatus(_B)
_CstDVTRowStatus_Type=RowStatus
_CstDVTRowStatus_Object=MibTableColumn
cstDVTRowStatus=_CstDVTRowStatus_Object((1,3,6,1,4,1,9,9,463,1,3,1,5),_CstDVTRowStatus_Type())
cstDVTRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cstDVTRowStatus.setStatus(_B)
class _CstDVTLunSizeHandling_Type(TruthValue):defaultValue=1
_CstDVTLunSizeHandling_Type.__name__=_S
_CstDVTLunSizeHandling_Object=MibTableColumn
cstDVTLunSizeHandling=_CstDVTLunSizeHandling_Object((1,3,6,1,4,1,9,9,463,1,3,1,6),_CstDVTLunSizeHandling_Type())
cstDVTLunSizeHandling.setMaxAccess(_C)
if mibBuilder.loadTexts:cstDVTLunSizeHandling.setStatus(_B)
class _CstDVTIOTimeout_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,200))
_CstDVTIOTimeout_Type.__name__=_R
_CstDVTIOTimeout_Object=MibTableColumn
cstDVTIOTimeout=_CstDVTIOTimeout_Object((1,3,6,1,4,1,9,9,463,1,3,1,7),_CstDVTIOTimeout_Type())
cstDVTIOTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cstDVTIOTimeout.setStatus(_B)
if mibBuilder.loadTexts:cstDVTIOTimeout.setUnits('seconds')
_CiscoSanTapMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSanTapMIBConformance=_CiscoSanTapMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,463,2))
_CiscoSanTapMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSanTapMIBCompliances=_CiscoSanTapMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,463,2,1))
_CiscoSanTapMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSanTapMIBGroups=_CiscoSanTapMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,463,2,2))
_CiscoSanTapNotifications_ObjectIdentity=ObjectIdentity
ciscoSanTapNotifications=_CiscoSanTapNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,463,3))
ciscoSanTapServiceConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,463,2,2,1))
ciscoSanTapServiceConfigGroup.setObjects(*((_A,_D),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoSanTapServiceConfigGroup.setStatus(_E)
ciscoSanTapServiceConfigGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,463,2,2,2))
ciscoSanTapServiceConfigGroupRev1.setObjects(*((_A,_D),(_A,_J),(_A,_K),(_A,_L),(_A,_U)))
if mibBuilder.loadTexts:ciscoSanTapServiceConfigGroupRev1.setStatus(_B)
ciscoSanTapDVTConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,463,2,2,3))
ciscoSanTapDVTConfigGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoSanTapDVTConfigGroup.setStatus(_E)
ciscoSanTapDVTConfigGroup1=ObjectGroup((1,3,6,1,4,1,9,9,463,2,2,4))
ciscoSanTapDVTConfigGroup1.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:ciscoSanTapDVTConfigGroup1.setStatus(_B)
ciscoSanTapMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,463,2,1,1))
ciscoSanTapMIBCompliance.setObjects((_A,_X))
if mibBuilder.loadTexts:ciscoSanTapMIBCompliance.setStatus(_E)
ciscoSanTapMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,463,2,1,2))
ciscoSanTapMIBComplianceRev1.setObjects(*((_A,_Q),(_A,_Y)))
if mibBuilder.loadTexts:ciscoSanTapMIBComplianceRev1.setStatus(_E)
ciscoSanTapMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,463,2,1,3))
ciscoSanTapMIBComplianceRev2.setObjects(*((_A,_Q),(_A,_Z)))
if mibBuilder.loadTexts:ciscoSanTapMIBComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoSanTapMIB':ciscoSanTapMIB,'ciscoSanTapMIBObjects':ciscoSanTapMIBObjects,'cstModuleTable':cstModuleTable,'cstModuleEntry':cstModuleEntry,_D:cstModuleId,'cstServiceConfigTable':cstServiceConfigTable,'cstServiceConfigEntry':cstServiceConfigEntry,_J:cstCVTNodeWwn,_K:cstCVTPortWwn,_L:cstServiceConfigRowStatus,_U:cstCVTName,'cstDVTConfigTable':cstDVTConfigTable,'cstDVTConfigEntry':cstDVTConfigEntry,_T:cstDVTPortWwn,_M:cstDVTTargetVsan,_N:cstDVTPort,_O:cstDVTName,_P:cstDVTRowStatus,_V:cstDVTLunSizeHandling,_W:cstDVTIOTimeout,'ciscoSanTapMIBConformance':ciscoSanTapMIBConformance,'ciscoSanTapMIBCompliances':ciscoSanTapMIBCompliances,'ciscoSanTapMIBCompliance':ciscoSanTapMIBCompliance,'ciscoSanTapMIBComplianceRev1':ciscoSanTapMIBComplianceRev1,'ciscoSanTapMIBComplianceRev2':ciscoSanTapMIBComplianceRev2,'ciscoSanTapMIBGroups':ciscoSanTapMIBGroups,_X:ciscoSanTapServiceConfigGroup,_Q:ciscoSanTapServiceConfigGroupRev1,_Y:ciscoSanTapDVTConfigGroup,_Z:ciscoSanTapDVTConfigGroup1,'ciscoSanTapNotifications':ciscoSanTapNotifications})