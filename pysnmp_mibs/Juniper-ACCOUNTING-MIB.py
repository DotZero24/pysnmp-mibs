_A4='juniAcctngBasicGroup6'
_A3='juniAcctngBasicGroup5'
_A2='juniAcctngBasicGroup4'
_A1='juniAcctngBasicGroup3'
_A0='juniAcctngBasicGroup2'
_z='juniAcctngBasicGroup'
_y='juniAcctngVirtualRouterTableRowStatus'
_x='juniAcctngVirtualRouterTableVRName'
_w='juniAcctngIfFinalStatsXferStatsDropped'
_v='juniAcctngIfFinalStatsXferStatsTransferred'
_u='juniAcctngIfFinalStatsXferStatsReceived'
_t='juniAcctngSelectionIfCreateDeleteStatsIfTypes'
_s='juniAcctngSelectionIfCreateDeleteStats'
_r='juniAcctngFileEntry'
_q='juniAcctngSelectionEntry'
_p='juniAcctngIfFinalStatsXferStatsSlotNumber'
_o='juniAcctngInterfaceLocation'
_n='juniAcctngInterfaceFileIndex'
_m='juniAcctngSelectionIfStackIfIndex'
_l='deprecated'
_k='JuniEnable'
_j='JuniPolicyAttachmentType'
_i='acctngSelectionIndex'
_h='ACCOUNTING-CONTROL-MIB'
_g='juniAcctngInterfaceRowStatus'
_f='juniAcctngInterfaceOperStatus'
_e='juniAcctngInterfaceAdminStatus'
_d='juniAcctngFileFormat'
_c='juniAcctngInterfaceNumberingMode'
_b='juniAcctngInterfaceDescrFormat'
_a='juniAcctngSelectionSubtreeType'
_Z='juniAcctngVirtualRouterTableIndex'
_Y='DisplayString'
_X='Bits'
_W='juniIfType'
_V='Juniper-UNI-IF-MIB'
_U='juniAcctngSelectionPolicyType'
_T='juniAcctngSelectionPolicyName'
_S='juniAcctngObsInterfaceAccntgFileIndex'
_R='juniAcctngObsInterfaceRowStatus'
_Q='juniAcctngObsInterfaceOperStatus'
_P='juniAcctngObsInterfaceAdminStatus'
_O='not-accessible'
_N='juniAcctngFileXferSecondaryIndex'
_M='juniAcctngFileXferIndex'
_L='juniAcctngFileXferMode'
_K='juniAcctngSelectionIfStackRowStatus'
_J='juniAcctngSelectionMaxIfStackLevels'
_I='juniAcctngSelectionMode'
_H='juniAcctngSelectionType'
_G='read-only'
_F='read-create'
_E='Integer32'
_D='obsolete'
_C='read-write'
_B='current'
_A='Juniper-ACCOUNTING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acctngFileEntry,acctngSelectionEntry,acctngSelectionIndex=mibBuilder.importSymbols(_h,'acctngFileEntry','acctngSelectionEntry',_i)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniPolicyAttachmentType,=mibBuilder.importSymbols('Juniper-POLICY-MIB',_j)
JuniAcctngAdminType,JuniAcctngOperType,JuniEnable,JuniInterfaceDescrFormat,JuniInterfaceLocation=mibBuilder.importSymbols('Juniper-TC','JuniAcctngAdminType','JuniAcctngOperType',_k,'JuniInterfaceDescrFormat','JuniInterfaceLocation')
juniIfType,=mibBuilder.importSymbols(_V,_W)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_X,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_Y,'PhysAddress','RowStatus','TextualConvention')
juniAcctngMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,24))
if mibBuilder.loadTexts:juniAcctngMIB.setRevisions(('2009-07-16 15:00','2005-04-26 15:00','2003-02-28 15:00','2002-12-17 15:37','2001-12-05 14:16','2001-11-19 19:00','2001-03-26 13:22','2000-11-07 19:00','2000-07-21 00:00','2000-03-20 00:00','2000-01-17 00:00','1999-10-18 00:00'))
_JuniAcctngMIBObjects_ObjectIdentity=ObjectIdentity
juniAcctngMIBObjects=_JuniAcctngMIBObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,1))
_JuniAcctngSelectionControl_ObjectIdentity=ObjectIdentity
juniAcctngSelectionControl=_JuniAcctngSelectionControl_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,1,1))
_JuniAcctngSelectionTable_Object=MibTable
juniAcctngSelectionTable=_JuniAcctngSelectionTable_Object((1,3,6,1,4,1,4874,2,2,24,1,1,1))
if mibBuilder.loadTexts:juniAcctngSelectionTable.setStatus(_B)
_JuniAcctngSelectionEntry_Object=MibTableRow
juniAcctngSelectionEntry=_JuniAcctngSelectionEntry_Object((1,3,6,1,4,1,4874,2,2,24,1,1,1,1))
if mibBuilder.loadTexts:juniAcctngSelectionEntry.setStatus(_B)
class _JuniAcctngSelectionType_Type(Bits):namedValues=NamedValues(*(('ietfAccountControl',0),('connectionLessLayer2',1)))
_JuniAcctngSelectionType_Type.__name__=_X
_JuniAcctngSelectionType_Object=MibTableColumn
juniAcctngSelectionType=_JuniAcctngSelectionType_Object((1,3,6,1,4,1,4874,2,2,24,1,1,1,1,1),_JuniAcctngSelectionType_Type())
juniAcctngSelectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngSelectionType.setStatus(_B)
class _JuniAcctngSelectionMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absoluteCounterValues',1),('deltaCounterValues',2)))
_JuniAcctngSelectionMode_Type.__name__=_E
_JuniAcctngSelectionMode_Object=MibTableColumn
juniAcctngSelectionMode=_JuniAcctngSelectionMode_Object((1,3,6,1,4,1,4874,2,2,24,1,1,1,1,2),_JuniAcctngSelectionMode_Type())
juniAcctngSelectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngSelectionMode.setStatus(_B)
class _JuniAcctngSelectionSubtreeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('lineCard',1),('systemController',2)))
_JuniAcctngSelectionSubtreeType_Type.__name__=_E
_JuniAcctngSelectionSubtreeType_Object=MibTableColumn
juniAcctngSelectionSubtreeType=_JuniAcctngSelectionSubtreeType_Object((1,3,6,1,4,1,4874,2,2,24,1,1,1,1,3),_JuniAcctngSelectionSubtreeType_Type())
juniAcctngSelectionSubtreeType.setMaxAccess(_G)
if mibBuilder.loadTexts:juniAcctngSelectionSubtreeType.setStatus(_l)
class _JuniAcctngSelectionMaxIfStackLevels_Type(Integer32):defaultValue=0
_JuniAcctngSelectionMaxIfStackLevels_Type.__name__=_E
_JuniAcctngSelectionMaxIfStackLevels_Object=MibTableColumn
juniAcctngSelectionMaxIfStackLevels=_JuniAcctngSelectionMaxIfStackLevels_Object((1,3,6,1,4,1,4874,2,2,24,1,1,1,1,4),_JuniAcctngSelectionMaxIfStackLevels_Type())
juniAcctngSelectionMaxIfStackLevels.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngSelectionMaxIfStackLevels.setStatus(_B)
class _JuniAcctngSelectionPolicyName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_JuniAcctngSelectionPolicyName_Type.__name__=_Y
_JuniAcctngSelectionPolicyName_Object=MibTableColumn
juniAcctngSelectionPolicyName=_JuniAcctngSelectionPolicyName_Object((1,3,6,1,4,1,4874,2,2,24,1,1,1,1,5),_JuniAcctngSelectionPolicyName_Type())
juniAcctngSelectionPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngSelectionPolicyName.setStatus(_B)
class _JuniAcctngSelectionPolicyType_Type(JuniPolicyAttachmentType):defaultValue=0
_JuniAcctngSelectionPolicyType_Type.__name__=_j
_JuniAcctngSelectionPolicyType_Object=MibTableColumn
juniAcctngSelectionPolicyType=_JuniAcctngSelectionPolicyType_Object((1,3,6,1,4,1,4874,2,2,24,1,1,1,1,6),_JuniAcctngSelectionPolicyType_Type())
juniAcctngSelectionPolicyType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngSelectionPolicyType.setStatus(_B)
class _JuniAcctngSelectionIfCreateDeleteStats_Type(JuniEnable):defaultValue=0
_JuniAcctngSelectionIfCreateDeleteStats_Type.__name__=_k
_JuniAcctngSelectionIfCreateDeleteStats_Object=MibTableColumn
juniAcctngSelectionIfCreateDeleteStats=_JuniAcctngSelectionIfCreateDeleteStats_Object((1,3,6,1,4,1,4874,2,2,24,1,1,1,1,7),_JuniAcctngSelectionIfCreateDeleteStats_Type())
juniAcctngSelectionIfCreateDeleteStats.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngSelectionIfCreateDeleteStats.setStatus(_B)
class _JuniAcctngSelectionIfCreateDeleteStatsIfTypes_Type(Bits):namedValues=NamedValues(*(('ip',0),('ppp',1),('atm1483',2),('vlan',3),('mplsMajor',4),('mplsL2Shim',5),('mplsMinor',6)))
_JuniAcctngSelectionIfCreateDeleteStatsIfTypes_Type.__name__=_X
_JuniAcctngSelectionIfCreateDeleteStatsIfTypes_Object=MibTableColumn
juniAcctngSelectionIfCreateDeleteStatsIfTypes=_JuniAcctngSelectionIfCreateDeleteStatsIfTypes_Object((1,3,6,1,4,1,4874,2,2,24,1,1,1,1,8),_JuniAcctngSelectionIfCreateDeleteStatsIfTypes_Type())
juniAcctngSelectionIfCreateDeleteStatsIfTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngSelectionIfCreateDeleteStatsIfTypes.setStatus(_B)
_JuniAcctngSelectionIfStackStartTable_Object=MibTable
juniAcctngSelectionIfStackStartTable=_JuniAcctngSelectionIfStackStartTable_Object((1,3,6,1,4,1,4874,2,2,24,1,1,3))
if mibBuilder.loadTexts:juniAcctngSelectionIfStackStartTable.setStatus(_B)
_JuniAcctngSelectionIfStackStartEntry_Object=MibTableRow
juniAcctngSelectionIfStackStartEntry=_JuniAcctngSelectionIfStackStartEntry_Object((1,3,6,1,4,1,4874,2,2,24,1,1,3,1))
juniAcctngSelectionIfStackStartEntry.setIndexNames((0,_h,_i),(0,_A,_m))
if mibBuilder.loadTexts:juniAcctngSelectionIfStackStartEntry.setStatus(_B)
_JuniAcctngSelectionIfStackIfIndex_Type=InterfaceIndex
_JuniAcctngSelectionIfStackIfIndex_Object=MibTableColumn
juniAcctngSelectionIfStackIfIndex=_JuniAcctngSelectionIfStackIfIndex_Object((1,3,6,1,4,1,4874,2,2,24,1,1,3,1,1),_JuniAcctngSelectionIfStackIfIndex_Type())
juniAcctngSelectionIfStackIfIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:juniAcctngSelectionIfStackIfIndex.setStatus(_B)
_JuniAcctngSelectionIfStackRowStatus_Type=RowStatus
_JuniAcctngSelectionIfStackRowStatus_Object=MibTableColumn
juniAcctngSelectionIfStackRowStatus=_JuniAcctngSelectionIfStackRowStatus_Object((1,3,6,1,4,1,4874,2,2,24,1,1,3,1,2),_JuniAcctngSelectionIfStackRowStatus_Type())
juniAcctngSelectionIfStackRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAcctngSelectionIfStackRowStatus.setStatus(_B)
_JuniAcctngFileControl_ObjectIdentity=ObjectIdentity
juniAcctngFileControl=_JuniAcctngFileControl_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,1,2))
_JuniAcctngFileTable_Object=MibTable
juniAcctngFileTable=_JuniAcctngFileTable_Object((1,3,6,1,4,1,4874,2,2,24,1,2,1))
if mibBuilder.loadTexts:juniAcctngFileTable.setStatus(_B)
_JuniAcctngFileEntry_Object=MibTableRow
juniAcctngFileEntry=_JuniAcctngFileEntry_Object((1,3,6,1,4,1,4874,2,2,24,1,2,1,1))
if mibBuilder.loadTexts:juniAcctngFileEntry.setStatus(_B)
class _JuniAcctngFileXferMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('juniAcctngManualTransfer',1),('juniAcctngAutomatedTransfer',2),('juniAcctngTransferOnFileFull',3),('juniAcctngRedundantTransfer',4)))
_JuniAcctngFileXferMode_Type.__name__=_E
_JuniAcctngFileXferMode_Object=MibTableColumn
juniAcctngFileXferMode=_JuniAcctngFileXferMode_Object((1,3,6,1,4,1,4874,2,2,24,1,2,1,1,1),_JuniAcctngFileXferMode_Type())
juniAcctngFileXferMode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngFileXferMode.setStatus(_B)
class _JuniAcctngFileXferIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JuniAcctngFileXferIndex_Type.__name__=_E
_JuniAcctngFileXferIndex_Object=MibTableColumn
juniAcctngFileXferIndex=_JuniAcctngFileXferIndex_Object((1,3,6,1,4,1,4874,2,2,24,1,2,1,1,2),_JuniAcctngFileXferIndex_Type())
juniAcctngFileXferIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngFileXferIndex.setStatus(_B)
class _JuniAcctngFileXferSecondaryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_JuniAcctngFileXferSecondaryIndex_Type.__name__=_E
_JuniAcctngFileXferSecondaryIndex_Object=MibTableColumn
juniAcctngFileXferSecondaryIndex=_JuniAcctngFileXferSecondaryIndex_Object((1,3,6,1,4,1,4874,2,2,24,1,2,1,1,3),_JuniAcctngFileXferSecondaryIndex_Type())
juniAcctngFileXferSecondaryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngFileXferSecondaryIndex.setStatus(_B)
_JuniAcctngInterfaceControl_ObjectIdentity=ObjectIdentity
juniAcctngInterfaceControl=_JuniAcctngInterfaceControl_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,1,3))
_JuniAcctngObsInterfaceTable_Object=MibTable
juniAcctngObsInterfaceTable=_JuniAcctngObsInterfaceTable_Object((1,3,6,1,4,1,4874,2,2,24,1,3,1))
if mibBuilder.loadTexts:juniAcctngObsInterfaceTable.setStatus(_D)
_JuniAcctngObsInterfaceEntry_Object=MibTableRow
juniAcctngObsInterfaceEntry=_JuniAcctngObsInterfaceEntry_Object((1,3,6,1,4,1,4874,2,2,24,1,3,1,1))
juniAcctngObsInterfaceEntry.setIndexNames((0,_V,_W))
if mibBuilder.loadTexts:juniAcctngObsInterfaceEntry.setStatus(_D)
_JuniAcctngObsInterfaceAdminStatus_Type=JuniAcctngAdminType
_JuniAcctngObsInterfaceAdminStatus_Object=MibTableColumn
juniAcctngObsInterfaceAdminStatus=_JuniAcctngObsInterfaceAdminStatus_Object((1,3,6,1,4,1,4874,2,2,24,1,3,1,1,1),_JuniAcctngObsInterfaceAdminStatus_Type())
juniAcctngObsInterfaceAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAcctngObsInterfaceAdminStatus.setStatus(_D)
_JuniAcctngObsInterfaceOperStatus_Type=JuniAcctngOperType
_JuniAcctngObsInterfaceOperStatus_Object=MibTableColumn
juniAcctngObsInterfaceOperStatus=_JuniAcctngObsInterfaceOperStatus_Object((1,3,6,1,4,1,4874,2,2,24,1,3,1,1,2),_JuniAcctngObsInterfaceOperStatus_Type())
juniAcctngObsInterfaceOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:juniAcctngObsInterfaceOperStatus.setStatus(_D)
_JuniAcctngObsInterfaceRowStatus_Type=RowStatus
_JuniAcctngObsInterfaceRowStatus_Object=MibTableColumn
juniAcctngObsInterfaceRowStatus=_JuniAcctngObsInterfaceRowStatus_Object((1,3,6,1,4,1,4874,2,2,24,1,3,1,1,3),_JuniAcctngObsInterfaceRowStatus_Type())
juniAcctngObsInterfaceRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAcctngObsInterfaceRowStatus.setStatus(_D)
class _JuniAcctngObsInterfaceAccntgFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniAcctngObsInterfaceAccntgFileIndex_Type.__name__=_E
_JuniAcctngObsInterfaceAccntgFileIndex_Object=MibTableColumn
juniAcctngObsInterfaceAccntgFileIndex=_JuniAcctngObsInterfaceAccntgFileIndex_Object((1,3,6,1,4,1,4874,2,2,24,1,3,1,1,4),_JuniAcctngObsInterfaceAccntgFileIndex_Type())
juniAcctngObsInterfaceAccntgFileIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAcctngObsInterfaceAccntgFileIndex.setStatus(_D)
_JuniAcctngInterfaceTable_Object=MibTable
juniAcctngInterfaceTable=_JuniAcctngInterfaceTable_Object((1,3,6,1,4,1,4874,2,2,24,1,3,2))
if mibBuilder.loadTexts:juniAcctngInterfaceTable.setStatus(_B)
_JuniAcctngInterfaceEntry_Object=MibTableRow
juniAcctngInterfaceEntry=_JuniAcctngInterfaceEntry_Object((1,3,6,1,4,1,4874,2,2,24,1,3,2,1))
juniAcctngInterfaceEntry.setIndexNames((0,_V,_W),(0,_A,_n),(0,_A,_o))
if mibBuilder.loadTexts:juniAcctngInterfaceEntry.setStatus(_B)
class _JuniAcctngInterfaceFileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JuniAcctngInterfaceFileIndex_Type.__name__=_E
_JuniAcctngInterfaceFileIndex_Object=MibTableColumn
juniAcctngInterfaceFileIndex=_JuniAcctngInterfaceFileIndex_Object((1,3,6,1,4,1,4874,2,2,24,1,3,2,1,1),_JuniAcctngInterfaceFileIndex_Type())
juniAcctngInterfaceFileIndex.setMaxAccess(_O)
if mibBuilder.loadTexts:juniAcctngInterfaceFileIndex.setStatus(_B)
_JuniAcctngInterfaceLocation_Type=JuniInterfaceLocation
_JuniAcctngInterfaceLocation_Object=MibTableColumn
juniAcctngInterfaceLocation=_JuniAcctngInterfaceLocation_Object((1,3,6,1,4,1,4874,2,2,24,1,3,2,1,2),_JuniAcctngInterfaceLocation_Type())
juniAcctngInterfaceLocation.setMaxAccess(_O)
if mibBuilder.loadTexts:juniAcctngInterfaceLocation.setStatus(_B)
_JuniAcctngInterfaceAdminStatus_Type=JuniAcctngAdminType
_JuniAcctngInterfaceAdminStatus_Object=MibTableColumn
juniAcctngInterfaceAdminStatus=_JuniAcctngInterfaceAdminStatus_Object((1,3,6,1,4,1,4874,2,2,24,1,3,2,1,3),_JuniAcctngInterfaceAdminStatus_Type())
juniAcctngInterfaceAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAcctngInterfaceAdminStatus.setStatus(_B)
_JuniAcctngInterfaceOperStatus_Type=JuniAcctngOperType
_JuniAcctngInterfaceOperStatus_Object=MibTableColumn
juniAcctngInterfaceOperStatus=_JuniAcctngInterfaceOperStatus_Object((1,3,6,1,4,1,4874,2,2,24,1,3,2,1,4),_JuniAcctngInterfaceOperStatus_Type())
juniAcctngInterfaceOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:juniAcctngInterfaceOperStatus.setStatus(_B)
_JuniAcctngInterfaceRowStatus_Type=RowStatus
_JuniAcctngInterfaceRowStatus_Object=MibTableColumn
juniAcctngInterfaceRowStatus=_JuniAcctngInterfaceRowStatus_Object((1,3,6,1,4,1,4874,2,2,24,1,3,2,1,5),_JuniAcctngInterfaceRowStatus_Type())
juniAcctngInterfaceRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAcctngInterfaceRowStatus.setStatus(_B)
_JuniAcctngIfFinalStatsXferStatsTable_Object=MibTable
juniAcctngIfFinalStatsXferStatsTable=_JuniAcctngIfFinalStatsXferStatsTable_Object((1,3,6,1,4,1,4874,2,2,24,1,3,3))
if mibBuilder.loadTexts:juniAcctngIfFinalStatsXferStatsTable.setStatus(_B)
_JuniAcctngIfFinalStatsXferStatsEntry_Object=MibTableRow
juniAcctngIfFinalStatsXferStatsEntry=_JuniAcctngIfFinalStatsXferStatsEntry_Object((1,3,6,1,4,1,4874,2,2,24,1,3,3,1))
juniAcctngIfFinalStatsXferStatsEntry.setIndexNames((0,_A,_p))
if mibBuilder.loadTexts:juniAcctngIfFinalStatsXferStatsEntry.setStatus(_B)
class _JuniAcctngIfFinalStatsXferStatsSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_JuniAcctngIfFinalStatsXferStatsSlotNumber_Type.__name__=_E
_JuniAcctngIfFinalStatsXferStatsSlotNumber_Object=MibTableColumn
juniAcctngIfFinalStatsXferStatsSlotNumber=_JuniAcctngIfFinalStatsXferStatsSlotNumber_Object((1,3,6,1,4,1,4874,2,2,24,1,3,3,1,1),_JuniAcctngIfFinalStatsXferStatsSlotNumber_Type())
juniAcctngIfFinalStatsXferStatsSlotNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:juniAcctngIfFinalStatsXferStatsSlotNumber.setStatus(_B)
_JuniAcctngIfFinalStatsXferStatsReceived_Type=Unsigned32
_JuniAcctngIfFinalStatsXferStatsReceived_Object=MibTableColumn
juniAcctngIfFinalStatsXferStatsReceived=_JuniAcctngIfFinalStatsXferStatsReceived_Object((1,3,6,1,4,1,4874,2,2,24,1,3,3,1,2),_JuniAcctngIfFinalStatsXferStatsReceived_Type())
juniAcctngIfFinalStatsXferStatsReceived.setMaxAccess(_G)
if mibBuilder.loadTexts:juniAcctngIfFinalStatsXferStatsReceived.setStatus(_B)
_JuniAcctngIfFinalStatsXferStatsTransferred_Type=Unsigned32
_JuniAcctngIfFinalStatsXferStatsTransferred_Object=MibTableColumn
juniAcctngIfFinalStatsXferStatsTransferred=_JuniAcctngIfFinalStatsXferStatsTransferred_Object((1,3,6,1,4,1,4874,2,2,24,1,3,3,1,3),_JuniAcctngIfFinalStatsXferStatsTransferred_Type())
juniAcctngIfFinalStatsXferStatsTransferred.setMaxAccess(_G)
if mibBuilder.loadTexts:juniAcctngIfFinalStatsXferStatsTransferred.setStatus(_B)
_JuniAcctngIfFinalStatsXferStatsDropped_Type=Unsigned32
_JuniAcctngIfFinalStatsXferStatsDropped_Object=MibTableColumn
juniAcctngIfFinalStatsXferStatsDropped=_JuniAcctngIfFinalStatsXferStatsDropped_Object((1,3,6,1,4,1,4874,2,2,24,1,3,3,1,4),_JuniAcctngIfFinalStatsXferStatsDropped_Type())
juniAcctngIfFinalStatsXferStatsDropped.setMaxAccess(_G)
if mibBuilder.loadTexts:juniAcctngIfFinalStatsXferStatsDropped.setStatus(_B)
_JuniAcctngScalarGroup_ObjectIdentity=ObjectIdentity
juniAcctngScalarGroup=_JuniAcctngScalarGroup_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,1,4))
_JuniAcctngInterfaceDescrFormat_Type=JuniInterfaceDescrFormat
_JuniAcctngInterfaceDescrFormat_Object=MibScalar
juniAcctngInterfaceDescrFormat=_JuniAcctngInterfaceDescrFormat_Object((1,3,6,1,4,1,4874,2,2,24,1,4,1),_JuniAcctngInterfaceDescrFormat_Type())
juniAcctngInterfaceDescrFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngInterfaceDescrFormat.setStatus(_B)
class _JuniAcctngInterfaceNumberingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('proprietaryNumbering',0),('rfc1213Number',1)))
_JuniAcctngInterfaceNumberingMode_Type.__name__=_E
_JuniAcctngInterfaceNumberingMode_Object=MibScalar
juniAcctngInterfaceNumberingMode=_JuniAcctngInterfaceNumberingMode_Object((1,3,6,1,4,1,4874,2,2,24,1,4,2),_JuniAcctngInterfaceNumberingMode_Type())
juniAcctngInterfaceNumberingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngInterfaceNumberingMode.setStatus(_B)
class _JuniAcctngFileFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('includeCR',0),('includeCRLF',1)))
_JuniAcctngFileFormat_Type.__name__=_E
_JuniAcctngFileFormat_Object=MibScalar
juniAcctngFileFormat=_JuniAcctngFileFormat_Object((1,3,6,1,4,1,4874,2,2,24,1,4,3),_JuniAcctngFileFormat_Type())
juniAcctngFileFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:juniAcctngFileFormat.setStatus(_B)
_JuniAcctngVirtualRouterControl_ObjectIdentity=ObjectIdentity
juniAcctngVirtualRouterControl=_JuniAcctngVirtualRouterControl_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,1,5))
_JuniAcctngVirtualRouterTable_Object=MibTable
juniAcctngVirtualRouterTable=_JuniAcctngVirtualRouterTable_Object((1,3,6,1,4,1,4874,2,2,24,1,5,1))
if mibBuilder.loadTexts:juniAcctngVirtualRouterTable.setStatus(_B)
_JuniAcctngVirtualRouterTableEntry_Object=MibTableRow
juniAcctngVirtualRouterTableEntry=_JuniAcctngVirtualRouterTableEntry_Object((1,3,6,1,4,1,4874,2,2,24,1,5,1,1))
juniAcctngVirtualRouterTableEntry.setIndexNames((0,_A,_Z))
if mibBuilder.loadTexts:juniAcctngVirtualRouterTableEntry.setStatus(_B)
_JuniAcctngVirtualRouterTableIndex_Type=Integer32
_JuniAcctngVirtualRouterTableIndex_Object=MibTableColumn
juniAcctngVirtualRouterTableIndex=_JuniAcctngVirtualRouterTableIndex_Object((1,3,6,1,4,1,4874,2,2,24,1,5,1,1,1),_JuniAcctngVirtualRouterTableIndex_Type())
juniAcctngVirtualRouterTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:juniAcctngVirtualRouterTableIndex.setStatus(_B)
class _JuniAcctngVirtualRouterTableVRName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_JuniAcctngVirtualRouterTableVRName_Type.__name__=_Y
_JuniAcctngVirtualRouterTableVRName_Object=MibTableColumn
juniAcctngVirtualRouterTableVRName=_JuniAcctngVirtualRouterTableVRName_Object((1,3,6,1,4,1,4874,2,2,24,1,5,1,1,2),_JuniAcctngVirtualRouterTableVRName_Type())
juniAcctngVirtualRouterTableVRName.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAcctngVirtualRouterTableVRName.setStatus(_B)
_JuniAcctngVirtualRouterTableRowStatus_Type=RowStatus
_JuniAcctngVirtualRouterTableRowStatus_Object=MibTableColumn
juniAcctngVirtualRouterTableRowStatus=_JuniAcctngVirtualRouterTableRowStatus_Object((1,3,6,1,4,1,4874,2,2,24,1,5,1,1,3),_JuniAcctngVirtualRouterTableRowStatus_Type())
juniAcctngVirtualRouterTableRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:juniAcctngVirtualRouterTableRowStatus.setStatus(_B)
_JuniAcctngSelectionSchema_ObjectIdentity=ObjectIdentity
juniAcctngSelectionSchema=_JuniAcctngSelectionSchema_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2))
if mibBuilder.loadTexts:juniAcctngSelectionSchema.setStatus(_B)
_JuniAcctngSelectionSchemaIf_ObjectIdentity=ObjectIdentity
juniAcctngSelectionSchemaIf=_JuniAcctngSelectionSchemaIf_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1))
_JuniAcctngIfInOctets_ObjectIdentity=ObjectIdentity
juniAcctngIfInOctets=_JuniAcctngIfInOctets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,1))
_JuniAcctngIfInUcastPkts_ObjectIdentity=ObjectIdentity
juniAcctngIfInUcastPkts=_JuniAcctngIfInUcastPkts_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,2))
_JuniAcctngIfInDiscards_ObjectIdentity=ObjectIdentity
juniAcctngIfInDiscards=_JuniAcctngIfInDiscards_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,3))
_JuniAcctngIfInErrors_ObjectIdentity=ObjectIdentity
juniAcctngIfInErrors=_JuniAcctngIfInErrors_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,4))
_JuniAcctngIfInUnknownProtos_ObjectIdentity=ObjectIdentity
juniAcctngIfInUnknownProtos=_JuniAcctngIfInUnknownProtos_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,5))
_JuniAcctngIfOutOctets_ObjectIdentity=ObjectIdentity
juniAcctngIfOutOctets=_JuniAcctngIfOutOctets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,6))
_JuniAcctngIfOutUcastPkts_ObjectIdentity=ObjectIdentity
juniAcctngIfOutUcastPkts=_JuniAcctngIfOutUcastPkts_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,7))
_JuniAcctngIfOutDiscards_ObjectIdentity=ObjectIdentity
juniAcctngIfOutDiscards=_JuniAcctngIfOutDiscards_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,8))
_JuniAcctngIfOutErrors_ObjectIdentity=ObjectIdentity
juniAcctngIfOutErrors=_JuniAcctngIfOutErrors_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,9))
_JuniAcctngIfCorrelator_ObjectIdentity=ObjectIdentity
juniAcctngIfCorrelator=_JuniAcctngIfCorrelator_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,10))
_JuniAcctngIfInPolicedOctets_ObjectIdentity=ObjectIdentity
juniAcctngIfInPolicedOctets=_JuniAcctngIfInPolicedOctets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,11))
_JuniAcctngIfInPolicedPkts_ObjectIdentity=ObjectIdentity
juniAcctngIfInPolicedPkts=_JuniAcctngIfInPolicedPkts_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,12))
_JuniAcctngIfInSpoofedPkts_ObjectIdentity=ObjectIdentity
juniAcctngIfInSpoofedPkts=_JuniAcctngIfInSpoofedPkts_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,13))
_JuniAcctngIfOutPolicedOctets_ObjectIdentity=ObjectIdentity
juniAcctngIfOutPolicedOctets=_JuniAcctngIfOutPolicedOctets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,14))
_JuniAcctngIfOutPolicedPkts_ObjectIdentity=ObjectIdentity
juniAcctngIfOutPolicedPkts=_JuniAcctngIfOutPolicedPkts_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,15))
_JuniAcctngIfOutSchedulerDropOctets_ObjectIdentity=ObjectIdentity
juniAcctngIfOutSchedulerDropOctets=_JuniAcctngIfOutSchedulerDropOctets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,16))
_JuniAcctngIfOutSchedulerDropPkts_ObjectIdentity=ObjectIdentity
juniAcctngIfOutSchedulerDropPkts=_JuniAcctngIfOutSchedulerDropPkts_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,17))
_JuniAcctngIfLowerInterface_ObjectIdentity=ObjectIdentity
juniAcctngIfLowerInterface=_JuniAcctngIfLowerInterface_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,18))
_JuniAcctngIfTimeOffset_ObjectIdentity=ObjectIdentity
juniAcctngIfTimeOffset=_JuniAcctngIfTimeOffset_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,19))
_JuniAcctngifInMulticastPkts_ObjectIdentity=ObjectIdentity
juniAcctngifInMulticastPkts=_JuniAcctngifInMulticastPkts_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,20))
_JuniAcctngifInBroadcastPkts_ObjectIdentity=ObjectIdentity
juniAcctngifInBroadcastPkts=_JuniAcctngifInBroadcastPkts_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,21))
_JuniAcctngifOutMulticastPkts_ObjectIdentity=ObjectIdentity
juniAcctngifOutMulticastPkts=_JuniAcctngifOutMulticastPkts_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,22))
_JuniAcctngifOutBroadcastPkts_ObjectIdentity=ObjectIdentity
juniAcctngifOutBroadcastPkts=_JuniAcctngifOutBroadcastPkts_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,1,23))
_JuniAcctngSelectionSchemaIfStack_ObjectIdentity=ObjectIdentity
juniAcctngSelectionSchemaIfStack=_JuniAcctngSelectionSchemaIfStack_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,3))
_JuniAcctngSelectionSchemaSystem_ObjectIdentity=ObjectIdentity
juniAcctngSelectionSchemaSystem=_JuniAcctngSelectionSchemaSystem_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,4))
_JuniAcctngSelectionSchemaPolicy_ObjectIdentity=ObjectIdentity
juniAcctngSelectionSchemaPolicy=_JuniAcctngSelectionSchemaPolicy_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5))
_JuniAcctngGreenPackets_ObjectIdentity=ObjectIdentity
juniAcctngGreenPackets=_JuniAcctngGreenPackets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,1))
_JuniAcctngUpperGreenPackets_ObjectIdentity=ObjectIdentity
juniAcctngUpperGreenPackets=_JuniAcctngUpperGreenPackets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,2))
_JuniAcctngYellowPackets_ObjectIdentity=ObjectIdentity
juniAcctngYellowPackets=_JuniAcctngYellowPackets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,3))
_JuniAcctngUpperYellowPackets_ObjectIdentity=ObjectIdentity
juniAcctngUpperYellowPackets=_JuniAcctngUpperYellowPackets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,4))
_JuniAcctngRedPackets_ObjectIdentity=ObjectIdentity
juniAcctngRedPackets=_JuniAcctngRedPackets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,5))
_JuniAcctngUpperRedPackets_ObjectIdentity=ObjectIdentity
juniAcctngUpperRedPackets=_JuniAcctngUpperRedPackets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,6))
_JuniAcctngGreenBytes_ObjectIdentity=ObjectIdentity
juniAcctngGreenBytes=_JuniAcctngGreenBytes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,7))
_JuniAcctngUpperGreenBytes_ObjectIdentity=ObjectIdentity
juniAcctngUpperGreenBytes=_JuniAcctngUpperGreenBytes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,8))
_JuniAcctngYellowBytes_ObjectIdentity=ObjectIdentity
juniAcctngYellowBytes=_JuniAcctngYellowBytes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,9))
_JuniAcctngUpperYellowBytes_ObjectIdentity=ObjectIdentity
juniAcctngUpperYellowBytes=_JuniAcctngUpperYellowBytes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,10))
_JuniAcctngRedBytes_ObjectIdentity=ObjectIdentity
juniAcctngRedBytes=_JuniAcctngRedBytes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,11))
_JuniAcctngUpperRedBytes_ObjectIdentity=ObjectIdentity
juniAcctngUpperRedBytes=_JuniAcctngUpperRedBytes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,5,12))
_JuniAcctngSelectionSchemaIgmp_ObjectIdentity=ObjectIdentity
juniAcctngSelectionSchemaIgmp=_JuniAcctngSelectionSchemaIgmp_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,6))
_JuniAcctngIgmpLowerIndex_ObjectIdentity=ObjectIdentity
juniAcctngIgmpLowerIndex=_JuniAcctngIgmpLowerIndex_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,6,1))
_JuniAcctngIgmpRouterIndex_ObjectIdentity=ObjectIdentity
juniAcctngIgmpRouterIndex=_JuniAcctngIgmpRouterIndex_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,6,2))
_JuniAcctngIgmpDestAddr_ObjectIdentity=ObjectIdentity
juniAcctngIgmpDestAddr=_JuniAcctngIgmpDestAddr_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,6,3))
_JuniAcctngIgmpSourceIndex_ObjectIdentity=ObjectIdentity
juniAcctngIgmpSourceIndex=_JuniAcctngIgmpSourceIndex_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,6,4))
_JuniAcctngIgmpMulticastGroup_ObjectIdentity=ObjectIdentity
juniAcctngIgmpMulticastGroup=_JuniAcctngIgmpMulticastGroup_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,6,5))
_JuniAcctngIgmpLowerIgmpCommand_ObjectIdentity=ObjectIdentity
juniAcctngIgmpLowerIgmpCommand=_JuniAcctngIgmpLowerIgmpCommand_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,6,6))
_JuniAcctngIgmpLowerTimeStamp_ObjectIdentity=ObjectIdentity
juniAcctngIgmpLowerTimeStamp=_JuniAcctngIgmpLowerTimeStamp_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,6,7))
_JuniAcctngSelectionSchemaQos_ObjectIdentity=ObjectIdentity
juniAcctngSelectionSchemaQos=_JuniAcctngSelectionSchemaQos_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7))
_JuniAcctngParentShapingRate_ObjectIdentity=ObjectIdentity
juniAcctngParentShapingRate=_JuniAcctngParentShapingRate_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,1))
_JuniAcctngParentSharedShapRate_ObjectIdentity=ObjectIdentity
juniAcctngParentSharedShapRate=_JuniAcctngParentSharedShapRate_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,2))
_JuniAcctngParentChildWeight_ObjectIdentity=ObjectIdentity
juniAcctngParentChildWeight=_JuniAcctngParentChildWeight_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,3))
_JuniAcctngQueueLength_ObjectIdentity=ObjectIdentity
juniAcctngQueueLength=_JuniAcctngQueueLength_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,4))
_JuniAcctngForwardedRate_ObjectIdentity=ObjectIdentity
juniAcctngForwardedRate=_JuniAcctngForwardedRate_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,5))
_JuniAcctngAggDropRate_ObjectIdentity=ObjectIdentity
juniAcctngAggDropRate=_JuniAcctngAggDropRate_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,6))
_JuniAcctngForwardedPackets_ObjectIdentity=ObjectIdentity
juniAcctngForwardedPackets=_JuniAcctngForwardedPackets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,7))
_JuniAcctngForwardedBytes_ObjectIdentity=ObjectIdentity
juniAcctngForwardedBytes=_JuniAcctngForwardedBytes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,8))
_JuniAcctngGreenDropPackets_ObjectIdentity=ObjectIdentity
juniAcctngGreenDropPackets=_JuniAcctngGreenDropPackets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,9))
_JuniAcctngGreenDropBytes_ObjectIdentity=ObjectIdentity
juniAcctngGreenDropBytes=_JuniAcctngGreenDropBytes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,10))
_JuniAcctngYellowDropPackets_ObjectIdentity=ObjectIdentity
juniAcctngYellowDropPackets=_JuniAcctngYellowDropPackets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,11))
_JuniAcctngYellowDropBytes_ObjectIdentity=ObjectIdentity
juniAcctngYellowDropBytes=_JuniAcctngYellowDropBytes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,12))
_JuniAcctngRedDropPackets_ObjectIdentity=ObjectIdentity
juniAcctngRedDropPackets=_JuniAcctngRedDropPackets_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,13))
_JuniAcctngRedDropBytes_ObjectIdentity=ObjectIdentity
juniAcctngRedDropBytes=_JuniAcctngRedDropBytes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,14))
_JuniAcctngDropProfile_ObjectIdentity=ObjectIdentity
juniAcctngDropProfile=_JuniAcctngDropProfile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,15))
_JuniAcctngQueueProfile_ObjectIdentity=ObjectIdentity
juniAcctngQueueProfile=_JuniAcctngQueueProfile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,16))
_JuniAcctngSchedulerProfile_ObjectIdentity=ObjectIdentity
juniAcctngSchedulerProfile=_JuniAcctngSchedulerProfile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,17))
_JuniAcctngStatisticsProfile_ObjectIdentity=ObjectIdentity
juniAcctngStatisticsProfile=_JuniAcctngStatisticsProfile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,18))
_JuniAcctngShapingMode_ObjectIdentity=ObjectIdentity
juniAcctngShapingMode=_JuniAcctngShapingMode_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,19))
_JuniAcctngShapingRate_ObjectIdentity=ObjectIdentity
juniAcctngShapingRate=_JuniAcctngShapingRate_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,20))
_JuniAcctngBurst_ObjectIdentity=ObjectIdentity
juniAcctngBurst=_JuniAcctngBurst_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,21))
_JuniAcctngAssuredRate_ObjectIdentity=ObjectIdentity
juniAcctngAssuredRate=_JuniAcctngAssuredRate_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,22))
_JuniAcctngWeight_ObjectIdentity=ObjectIdentity
juniAcctngWeight=_JuniAcctngWeight_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,23))
_JuniAcctngRedEnabled_ObjectIdentity=ObjectIdentity
juniAcctngRedEnabled=_JuniAcctngRedEnabled_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,24))
_JuniAcctngSharedShapingMode_ObjectIdentity=ObjectIdentity
juniAcctngSharedShapingMode=_JuniAcctngSharedShapingMode_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,25))
_JuniAcctngSharedShapingRate_ObjectIdentity=ObjectIdentity
juniAcctngSharedShapingRate=_JuniAcctngSharedShapingRate_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,26))
_JuniAcctngByteAdjType_ObjectIdentity=ObjectIdentity
juniAcctngByteAdjType=_JuniAcctngByteAdjType_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,27))
_JuniAcctngByteAdjBytes_ObjectIdentity=ObjectIdentity
juniAcctngByteAdjBytes=_JuniAcctngByteAdjBytes_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,2,7,28))
_JuniAcctngConformance_ObjectIdentity=ObjectIdentity
juniAcctngConformance=_JuniAcctngConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,3))
_JuniAcctngGroups_ObjectIdentity=ObjectIdentity
juniAcctngGroups=_JuniAcctngGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,3,1))
_JuniAcctngCompliances_ObjectIdentity=ObjectIdentity
juniAcctngCompliances=_JuniAcctngCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,24,3,2))
acctngSelectionEntry.registerAugmentions((_A,_q))
juniAcctngSelectionEntry.setIndexNames(*acctngSelectionEntry.getIndexNames())
acctngFileEntry.registerAugmentions((_A,_r))
juniAcctngFileEntry.setIndexNames(*acctngFileEntry.getIndexNames())
juniAcctngBasicGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,24,3,1,1))
juniAcctngBasicGroup.setObjects(*((_A,_H),(_A,_I),(_A,_a),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniAcctngBasicGroup.setStatus(_D)
juniAcctngBasicGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,24,3,1,2))
juniAcctngBasicGroup2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniAcctngBasicGroup2.setStatus(_D)
juniAcctngBasicGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,24,3,1,3))
juniAcctngBasicGroup3.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_T),(_A,_U),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniAcctngBasicGroup3.setStatus(_D)
juniAcctngDeprecatedGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,24,3,1,4))
juniAcctngDeprecatedGroup.setObjects((_A,_a))
if mibBuilder.loadTexts:juniAcctngDeprecatedGroup.setStatus(_l)
juniAcctngBasicGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,24,3,1,5))
juniAcctngBasicGroup4.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_H),(_A,_I),(_A,_J),(_A,_T),(_A,_U),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_e),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:juniAcctngBasicGroup4.setStatus(_B)
juniAcctngBasicGroup5=ObjectGroup((1,3,6,1,4,1,4874,2,2,24,3,1,6))
juniAcctngBasicGroup5.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_H),(_A,_I),(_A,_J),(_A,_T),(_A,_U),(_A,_K),(_A,_s),(_A,_t),(_A,_L),(_A,_M),(_A,_N),(_A,_e),(_A,_f),(_A,_g),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:juniAcctngBasicGroup5.setStatus(_D)
juniAcctngBasicGroup6=ObjectGroup((1,3,6,1,4,1,4874,2,2,24,3,1,7))
juniAcctngBasicGroup6.setObjects(*((_A,_Z),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:juniAcctngBasicGroup6.setStatus(_B)
juniAcctngCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,24,3,2,1))
juniAcctngCompliance.setObjects((_A,_z))
if mibBuilder.loadTexts:juniAcctngCompliance.setStatus(_D)
juniAcctngCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,24,3,2,2))
juniAcctngCompliance2.setObjects((_A,_A0))
if mibBuilder.loadTexts:juniAcctngCompliance2.setStatus(_D)
juniAcctngCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,24,3,2,3))
juniAcctngCompliance3.setObjects((_A,_A1))
if mibBuilder.loadTexts:juniAcctngCompliance3.setStatus(_D)
juniAcctngCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,24,3,2,4))
juniAcctngCompliance4.setObjects((_A,_A2))
if mibBuilder.loadTexts:juniAcctngCompliance4.setStatus(_B)
juniAcctngCompliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,24,3,2,5))
juniAcctngCompliance5.setObjects((_A,_A3))
if mibBuilder.loadTexts:juniAcctngCompliance5.setStatus(_B)
juniAcctngCompliance6=ModuleCompliance((1,3,6,1,4,1,4874,2,2,24,3,2,6))
juniAcctngCompliance6.setObjects((_A,_A4))
if mibBuilder.loadTexts:juniAcctngCompliance6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniAcctngMIB':juniAcctngMIB,'juniAcctngMIBObjects':juniAcctngMIBObjects,'juniAcctngSelectionControl':juniAcctngSelectionControl,'juniAcctngSelectionTable':juniAcctngSelectionTable,_q:juniAcctngSelectionEntry,_H:juniAcctngSelectionType,_I:juniAcctngSelectionMode,_a:juniAcctngSelectionSubtreeType,_J:juniAcctngSelectionMaxIfStackLevels,_T:juniAcctngSelectionPolicyName,_U:juniAcctngSelectionPolicyType,_s:juniAcctngSelectionIfCreateDeleteStats,_t:juniAcctngSelectionIfCreateDeleteStatsIfTypes,'juniAcctngSelectionIfStackStartTable':juniAcctngSelectionIfStackStartTable,'juniAcctngSelectionIfStackStartEntry':juniAcctngSelectionIfStackStartEntry,_m:juniAcctngSelectionIfStackIfIndex,_K:juniAcctngSelectionIfStackRowStatus,'juniAcctngFileControl':juniAcctngFileControl,'juniAcctngFileTable':juniAcctngFileTable,_r:juniAcctngFileEntry,_L:juniAcctngFileXferMode,_M:juniAcctngFileXferIndex,_N:juniAcctngFileXferSecondaryIndex,'juniAcctngInterfaceControl':juniAcctngInterfaceControl,'juniAcctngObsInterfaceTable':juniAcctngObsInterfaceTable,'juniAcctngObsInterfaceEntry':juniAcctngObsInterfaceEntry,_P:juniAcctngObsInterfaceAdminStatus,_Q:juniAcctngObsInterfaceOperStatus,_R:juniAcctngObsInterfaceRowStatus,_S:juniAcctngObsInterfaceAccntgFileIndex,'juniAcctngInterfaceTable':juniAcctngInterfaceTable,'juniAcctngInterfaceEntry':juniAcctngInterfaceEntry,_n:juniAcctngInterfaceFileIndex,_o:juniAcctngInterfaceLocation,_e:juniAcctngInterfaceAdminStatus,_f:juniAcctngInterfaceOperStatus,_g:juniAcctngInterfaceRowStatus,'juniAcctngIfFinalStatsXferStatsTable':juniAcctngIfFinalStatsXferStatsTable,'juniAcctngIfFinalStatsXferStatsEntry':juniAcctngIfFinalStatsXferStatsEntry,_p:juniAcctngIfFinalStatsXferStatsSlotNumber,_u:juniAcctngIfFinalStatsXferStatsReceived,_v:juniAcctngIfFinalStatsXferStatsTransferred,_w:juniAcctngIfFinalStatsXferStatsDropped,'juniAcctngScalarGroup':juniAcctngScalarGroup,_b:juniAcctngInterfaceDescrFormat,_c:juniAcctngInterfaceNumberingMode,_d:juniAcctngFileFormat,'juniAcctngVirtualRouterControl':juniAcctngVirtualRouterControl,'juniAcctngVirtualRouterTable':juniAcctngVirtualRouterTable,'juniAcctngVirtualRouterTableEntry':juniAcctngVirtualRouterTableEntry,_Z:juniAcctngVirtualRouterTableIndex,_x:juniAcctngVirtualRouterTableVRName,_y:juniAcctngVirtualRouterTableRowStatus,'juniAcctngSelectionSchema':juniAcctngSelectionSchema,'juniAcctngSelectionSchemaIf':juniAcctngSelectionSchemaIf,'juniAcctngIfInOctets':juniAcctngIfInOctets,'juniAcctngIfInUcastPkts':juniAcctngIfInUcastPkts,'juniAcctngIfInDiscards':juniAcctngIfInDiscards,'juniAcctngIfInErrors':juniAcctngIfInErrors,'juniAcctngIfInUnknownProtos':juniAcctngIfInUnknownProtos,'juniAcctngIfOutOctets':juniAcctngIfOutOctets,'juniAcctngIfOutUcastPkts':juniAcctngIfOutUcastPkts,'juniAcctngIfOutDiscards':juniAcctngIfOutDiscards,'juniAcctngIfOutErrors':juniAcctngIfOutErrors,'juniAcctngIfCorrelator':juniAcctngIfCorrelator,'juniAcctngIfInPolicedOctets':juniAcctngIfInPolicedOctets,'juniAcctngIfInPolicedPkts':juniAcctngIfInPolicedPkts,'juniAcctngIfInSpoofedPkts':juniAcctngIfInSpoofedPkts,'juniAcctngIfOutPolicedOctets':juniAcctngIfOutPolicedOctets,'juniAcctngIfOutPolicedPkts':juniAcctngIfOutPolicedPkts,'juniAcctngIfOutSchedulerDropOctets':juniAcctngIfOutSchedulerDropOctets,'juniAcctngIfOutSchedulerDropPkts':juniAcctngIfOutSchedulerDropPkts,'juniAcctngIfLowerInterface':juniAcctngIfLowerInterface,'juniAcctngIfTimeOffset':juniAcctngIfTimeOffset,'juniAcctngifInMulticastPkts':juniAcctngifInMulticastPkts,'juniAcctngifInBroadcastPkts':juniAcctngifInBroadcastPkts,'juniAcctngifOutMulticastPkts':juniAcctngifOutMulticastPkts,'juniAcctngifOutBroadcastPkts':juniAcctngifOutBroadcastPkts,'juniAcctngSelectionSchemaIfStack':juniAcctngSelectionSchemaIfStack,'juniAcctngSelectionSchemaSystem':juniAcctngSelectionSchemaSystem,'juniAcctngSelectionSchemaPolicy':juniAcctngSelectionSchemaPolicy,'juniAcctngGreenPackets':juniAcctngGreenPackets,'juniAcctngUpperGreenPackets':juniAcctngUpperGreenPackets,'juniAcctngYellowPackets':juniAcctngYellowPackets,'juniAcctngUpperYellowPackets':juniAcctngUpperYellowPackets,'juniAcctngRedPackets':juniAcctngRedPackets,'juniAcctngUpperRedPackets':juniAcctngUpperRedPackets,'juniAcctngGreenBytes':juniAcctngGreenBytes,'juniAcctngUpperGreenBytes':juniAcctngUpperGreenBytes,'juniAcctngYellowBytes':juniAcctngYellowBytes,'juniAcctngUpperYellowBytes':juniAcctngUpperYellowBytes,'juniAcctngRedBytes':juniAcctngRedBytes,'juniAcctngUpperRedBytes':juniAcctngUpperRedBytes,'juniAcctngSelectionSchemaIgmp':juniAcctngSelectionSchemaIgmp,'juniAcctngIgmpLowerIndex':juniAcctngIgmpLowerIndex,'juniAcctngIgmpRouterIndex':juniAcctngIgmpRouterIndex,'juniAcctngIgmpDestAddr':juniAcctngIgmpDestAddr,'juniAcctngIgmpSourceIndex':juniAcctngIgmpSourceIndex,'juniAcctngIgmpMulticastGroup':juniAcctngIgmpMulticastGroup,'juniAcctngIgmpLowerIgmpCommand':juniAcctngIgmpLowerIgmpCommand,'juniAcctngIgmpLowerTimeStamp':juniAcctngIgmpLowerTimeStamp,'juniAcctngSelectionSchemaQos':juniAcctngSelectionSchemaQos,'juniAcctngParentShapingRate':juniAcctngParentShapingRate,'juniAcctngParentSharedShapRate':juniAcctngParentSharedShapRate,'juniAcctngParentChildWeight':juniAcctngParentChildWeight,'juniAcctngQueueLength':juniAcctngQueueLength,'juniAcctngForwardedRate':juniAcctngForwardedRate,'juniAcctngAggDropRate':juniAcctngAggDropRate,'juniAcctngForwardedPackets':juniAcctngForwardedPackets,'juniAcctngForwardedBytes':juniAcctngForwardedBytes,'juniAcctngGreenDropPackets':juniAcctngGreenDropPackets,'juniAcctngGreenDropBytes':juniAcctngGreenDropBytes,'juniAcctngYellowDropPackets':juniAcctngYellowDropPackets,'juniAcctngYellowDropBytes':juniAcctngYellowDropBytes,'juniAcctngRedDropPackets':juniAcctngRedDropPackets,'juniAcctngRedDropBytes':juniAcctngRedDropBytes,'juniAcctngDropProfile':juniAcctngDropProfile,'juniAcctngQueueProfile':juniAcctngQueueProfile,'juniAcctngSchedulerProfile':juniAcctngSchedulerProfile,'juniAcctngStatisticsProfile':juniAcctngStatisticsProfile,'juniAcctngShapingMode':juniAcctngShapingMode,'juniAcctngShapingRate':juniAcctngShapingRate,'juniAcctngBurst':juniAcctngBurst,'juniAcctngAssuredRate':juniAcctngAssuredRate,'juniAcctngWeight':juniAcctngWeight,'juniAcctngRedEnabled':juniAcctngRedEnabled,'juniAcctngSharedShapingMode':juniAcctngSharedShapingMode,'juniAcctngSharedShapingRate':juniAcctngSharedShapingRate,'juniAcctngByteAdjType':juniAcctngByteAdjType,'juniAcctngByteAdjBytes':juniAcctngByteAdjBytes,'juniAcctngConformance':juniAcctngConformance,'juniAcctngGroups':juniAcctngGroups,_z:juniAcctngBasicGroup,_A0:juniAcctngBasicGroup2,_A1:juniAcctngBasicGroup3,'juniAcctngDeprecatedGroup':juniAcctngDeprecatedGroup,_A2:juniAcctngBasicGroup4,_A3:juniAcctngBasicGroup5,_A4:juniAcctngBasicGroup6,'juniAcctngCompliances':juniAcctngCompliances,'juniAcctngCompliance':juniAcctngCompliance,'juniAcctngCompliance2':juniAcctngCompliance2,'juniAcctngCompliance3':juniAcctngCompliance3,'juniAcctngCompliance4':juniAcctngCompliance4,'juniAcctngCompliance5':juniAcctngCompliance5,'juniAcctngCompliance6':juniAcctngCompliance6})