_a='cpwVcFrPMStorageType'
_Z='cpwVcFrPMRowStatus'
_Y='cpwVcFrPMPw2FrOperStatus'
_X='cpwVcFrPMOperStatus'
_W='cpwVcFrPMAdminStatus'
_V='cpwVcFrPMIfIndex'
_U='cpwVcFrStorageType'
_T='cpwVcFrRowStatus'
_S='cpwVcFrPw2FrOperStatus'
_R='cpwVcFrOperStatus'
_Q='cpwVcFrAdminStatus'
_P='cpwVcFrDlci'
_O='cpwVcFrIfIndex'
_N='cpwVcFrPMPwVcIndex'
_M='not-accessible'
_L='cpwVcFrPwVcIndex'
_K='InterfaceIndexOrZero'
_J='cpwVcFrPMGroup'
_I='cpwVcFrGroup'
_H='read-only'
_G='unknown'
_F='inactive'
_E='active'
_D='Integer32'
_C='read-create'
_B='CISCO-IETF-PW-FR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DlciNumber,=mibBuilder.importSymbols('CISCO-FRAME-RELAY-MIB','DlciNumber')
CpwVcIndexType,=mibBuilder.importSymbols('CISCO-IETF-PW-TC-MIB','CpwVcIndexType')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
cpwVcFrMIB=ModuleIdentity((1,3,6,1,4,1,9,10,112))
if mibBuilder.loadTexts:cpwVcFrMIB.setRevisions(('2003-12-16 00:00',))
_CpwVcFrNotifications_ObjectIdentity=ObjectIdentity
cpwVcFrNotifications=_CpwVcFrNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,112,0))
_CpwVcFrObjects_ObjectIdentity=ObjectIdentity
cpwVcFrObjects=_CpwVcFrObjects_ObjectIdentity((1,3,6,1,4,1,9,10,112,1))
_CpwVcFrTable_Object=MibTable
cpwVcFrTable=_CpwVcFrTable_Object((1,3,6,1,4,1,9,10,112,1,1))
if mibBuilder.loadTexts:cpwVcFrTable.setStatus(_A)
_CpwVcFrEntry_Object=MibTableRow
cpwVcFrEntry=_CpwVcFrEntry_Object((1,3,6,1,4,1,9,10,112,1,1,1))
cpwVcFrEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cpwVcFrEntry.setStatus(_A)
_CpwVcFrPwVcIndex_Type=CpwVcIndexType
_CpwVcFrPwVcIndex_Object=MibTableColumn
cpwVcFrPwVcIndex=_CpwVcFrPwVcIndex_Object((1,3,6,1,4,1,9,10,112,1,1,1,1),_CpwVcFrPwVcIndex_Type())
cpwVcFrPwVcIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:cpwVcFrPwVcIndex.setStatus(_A)
class _CpwVcFrIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_CpwVcFrIfIndex_Type.__name__=_K
_CpwVcFrIfIndex_Object=MibTableColumn
cpwVcFrIfIndex=_CpwVcFrIfIndex_Object((1,3,6,1,4,1,9,10,112,1,1,1,2),_CpwVcFrIfIndex_Type())
cpwVcFrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcFrIfIndex.setStatus(_A)
_CpwVcFrDlci_Type=DlciNumber
_CpwVcFrDlci_Object=MibTableColumn
cpwVcFrDlci=_CpwVcFrDlci_Object((1,3,6,1,4,1,9,10,112,1,1,1,3),_CpwVcFrDlci_Type())
cpwVcFrDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcFrDlci.setStatus(_A)
class _CpwVcFrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CpwVcFrAdminStatus_Type.__name__=_D
_CpwVcFrAdminStatus_Object=MibTableColumn
cpwVcFrAdminStatus=_CpwVcFrAdminStatus_Object((1,3,6,1,4,1,9,10,112,1,1,1,4),_CpwVcFrAdminStatus_Type())
cpwVcFrAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcFrAdminStatus.setStatus(_A)
class _CpwVcFrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_CpwVcFrOperStatus_Type.__name__=_D
_CpwVcFrOperStatus_Object=MibTableColumn
cpwVcFrOperStatus=_CpwVcFrOperStatus_Object((1,3,6,1,4,1,9,10,112,1,1,1,5),_CpwVcFrOperStatus_Type())
cpwVcFrOperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cpwVcFrOperStatus.setStatus(_A)
class _CpwVcFrPw2FrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_CpwVcFrPw2FrOperStatus_Type.__name__=_D
_CpwVcFrPw2FrOperStatus_Object=MibTableColumn
cpwVcFrPw2FrOperStatus=_CpwVcFrPw2FrOperStatus_Object((1,3,6,1,4,1,9,10,112,1,1,1,6),_CpwVcFrPw2FrOperStatus_Type())
cpwVcFrPw2FrOperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cpwVcFrPw2FrOperStatus.setStatus(_A)
_CpwVcFrRowStatus_Type=RowStatus
_CpwVcFrRowStatus_Object=MibTableColumn
cpwVcFrRowStatus=_CpwVcFrRowStatus_Object((1,3,6,1,4,1,9,10,112,1,1,1,7),_CpwVcFrRowStatus_Type())
cpwVcFrRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcFrRowStatus.setStatus(_A)
_CpwVcFrStorageType_Type=StorageType
_CpwVcFrStorageType_Object=MibTableColumn
cpwVcFrStorageType=_CpwVcFrStorageType_Object((1,3,6,1,4,1,9,10,112,1,1,1,8),_CpwVcFrStorageType_Type())
cpwVcFrStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcFrStorageType.setStatus(_A)
_CpwVcFrPMTable_Object=MibTable
cpwVcFrPMTable=_CpwVcFrPMTable_Object((1,3,6,1,4,1,9,10,112,1,2))
if mibBuilder.loadTexts:cpwVcFrPMTable.setStatus(_A)
_CpwVcFrPMEntry_Object=MibTableRow
cpwVcFrPMEntry=_CpwVcFrPMEntry_Object((1,3,6,1,4,1,9,10,112,1,2,1))
cpwVcFrPMEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cpwVcFrPMEntry.setStatus(_A)
_CpwVcFrPMPwVcIndex_Type=CpwVcIndexType
_CpwVcFrPMPwVcIndex_Object=MibTableColumn
cpwVcFrPMPwVcIndex=_CpwVcFrPMPwVcIndex_Object((1,3,6,1,4,1,9,10,112,1,2,1,1),_CpwVcFrPMPwVcIndex_Type())
cpwVcFrPMPwVcIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:cpwVcFrPMPwVcIndex.setStatus(_A)
_CpwVcFrPMIfIndex_Type=InterfaceIndexOrZero
_CpwVcFrPMIfIndex_Object=MibTableColumn
cpwVcFrPMIfIndex=_CpwVcFrPMIfIndex_Object((1,3,6,1,4,1,9,10,112,1,2,1,2),_CpwVcFrPMIfIndex_Type())
cpwVcFrPMIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcFrPMIfIndex.setStatus(_A)
class _CpwVcFrPMAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CpwVcFrPMAdminStatus_Type.__name__=_D
_CpwVcFrPMAdminStatus_Object=MibTableColumn
cpwVcFrPMAdminStatus=_CpwVcFrPMAdminStatus_Object((1,3,6,1,4,1,9,10,112,1,2,1,3),_CpwVcFrPMAdminStatus_Type())
cpwVcFrPMAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcFrPMAdminStatus.setStatus(_A)
class _CpwVcFrPMOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_CpwVcFrPMOperStatus_Type.__name__=_D
_CpwVcFrPMOperStatus_Object=MibTableColumn
cpwVcFrPMOperStatus=_CpwVcFrPMOperStatus_Object((1,3,6,1,4,1,9,10,112,1,2,1,4),_CpwVcFrPMOperStatus_Type())
cpwVcFrPMOperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cpwVcFrPMOperStatus.setStatus(_A)
class _CpwVcFrPMPw2FrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_CpwVcFrPMPw2FrOperStatus_Type.__name__=_D
_CpwVcFrPMPw2FrOperStatus_Object=MibTableColumn
cpwVcFrPMPw2FrOperStatus=_CpwVcFrPMPw2FrOperStatus_Object((1,3,6,1,4,1,9,10,112,1,2,1,5),_CpwVcFrPMPw2FrOperStatus_Type())
cpwVcFrPMPw2FrOperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cpwVcFrPMPw2FrOperStatus.setStatus(_A)
_CpwVcFrPMRowStatus_Type=RowStatus
_CpwVcFrPMRowStatus_Object=MibTableColumn
cpwVcFrPMRowStatus=_CpwVcFrPMRowStatus_Object((1,3,6,1,4,1,9,10,112,1,2,1,6),_CpwVcFrPMRowStatus_Type())
cpwVcFrPMRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcFrPMRowStatus.setStatus(_A)
_CpwVcFrPMStorageType_Type=StorageType
_CpwVcFrPMStorageType_Object=MibTableColumn
cpwVcFrPMStorageType=_CpwVcFrPMStorageType_Object((1,3,6,1,4,1,9,10,112,1,2,1,7),_CpwVcFrPMStorageType_Type())
cpwVcFrPMStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcFrPMStorageType.setStatus(_A)
_CpwVcFrConformance_ObjectIdentity=ObjectIdentity
cpwVcFrConformance=_CpwVcFrConformance_ObjectIdentity((1,3,6,1,4,1,9,10,112,2))
_CpwVcFrCompliances_ObjectIdentity=ObjectIdentity
cpwVcFrCompliances=_CpwVcFrCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,112,2,1))
_CpwVcFrGroups_ObjectIdentity=ObjectIdentity
cpwVcFrGroups=_CpwVcFrGroups_ObjectIdentity((1,3,6,1,4,1,9,10,112,2,2))
cpwVcFrGroup=ObjectGroup((1,3,6,1,4,1,9,10,112,2,2,1))
cpwVcFrGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cpwVcFrGroup.setStatus(_A)
cpwVcFrPMGroup=ObjectGroup((1,3,6,1,4,1,9,10,112,2,2,2))
cpwVcFrPMGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cpwVcFrPMGroup.setStatus(_A)
cpwVcFrFullCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,112,2,1,1))
cpwVcFrFullCompliance.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cpwVcFrFullCompliance.setStatus(_A)
cpwVcFrReadOnlyCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,112,2,1,2))
cpwVcFrReadOnlyCompliance.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cpwVcFrReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cpwVcFrMIB':cpwVcFrMIB,'cpwVcFrNotifications':cpwVcFrNotifications,'cpwVcFrObjects':cpwVcFrObjects,'cpwVcFrTable':cpwVcFrTable,'cpwVcFrEntry':cpwVcFrEntry,_L:cpwVcFrPwVcIndex,_O:cpwVcFrIfIndex,_P:cpwVcFrDlci,_Q:cpwVcFrAdminStatus,_R:cpwVcFrOperStatus,_S:cpwVcFrPw2FrOperStatus,_T:cpwVcFrRowStatus,_U:cpwVcFrStorageType,'cpwVcFrPMTable':cpwVcFrPMTable,'cpwVcFrPMEntry':cpwVcFrPMEntry,_N:cpwVcFrPMPwVcIndex,_V:cpwVcFrPMIfIndex,_W:cpwVcFrPMAdminStatus,_X:cpwVcFrPMOperStatus,_Y:cpwVcFrPMPw2FrOperStatus,_Z:cpwVcFrPMRowStatus,_a:cpwVcFrPMStorageType,'cpwVcFrConformance':cpwVcFrConformance,'cpwVcFrCompliances':cpwVcFrCompliances,'cpwVcFrFullCompliance':cpwVcFrFullCompliance,'cpwVcFrReadOnlyCompliance':cpwVcFrReadOnlyCompliance,'cpwVcFrGroups':cpwVcFrGroups,_I:cpwVcFrGroup,_J:cpwVcFrPMGroup})