_V='csCugMIBGroup'
_U='csCugRowStatus'
_T='csCugDenySameGroupFromUser'
_S='csCugDenySameGroupToUser'
_R='csCugPreferential'
_Q='csCugIndex'
_P='csCugIfRowStatus'
_O='csCugIfPermitUnknownCugsFromUser'
_N='csCugIfPermitUnknownCugsToUser'
_M='csCugIfAccessEnable'
_L='csCugInterlockCodeRowStatus'
_K='csCugInterlockCodeAliasName'
_J='DisplayString'
_I='Integer32'
_H='csCugInterlockCode'
_G='Unsigned32'
_F='ifIndex'
_E='IF-MIB'
_D='TruthValue'
_C='read-create'
_B='CISCO-ATM-SWITCH-CUG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention',_D)
csCugMIB=ModuleIdentity((1,3,6,1,4,1,9,9,89))
class CsCugInterlockCode(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(24,24))
class Unsigned32(TextualConvention,Gauge32):status=_A
_CsCugMIBObjects_ObjectIdentity=ObjectIdentity
csCugMIBObjects=_CsCugMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,89,1))
_CsCugInterlockCodeTable_Object=MibTable
csCugInterlockCodeTable=_CsCugInterlockCodeTable_Object((1,3,6,1,4,1,9,9,89,1,1))
if mibBuilder.loadTexts:csCugInterlockCodeTable.setStatus(_A)
_CsCugInterlockCodeEntry_Object=MibTableRow
csCugInterlockCodeEntry=_CsCugInterlockCodeEntry_Object((1,3,6,1,4,1,9,9,89,1,1,1))
csCugInterlockCodeEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:csCugInterlockCodeEntry.setStatus(_A)
_CsCugInterlockCode_Type=CsCugInterlockCode
_CsCugInterlockCode_Object=MibTableColumn
csCugInterlockCode=_CsCugInterlockCode_Object((1,3,6,1,4,1,9,9,89,1,1,1,1),_CsCugInterlockCode_Type())
csCugInterlockCode.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:csCugInterlockCode.setStatus(_A)
class _CsCugInterlockCodeAliasName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_CsCugInterlockCodeAliasName_Type.__name__=_J
_CsCugInterlockCodeAliasName_Object=MibTableColumn
csCugInterlockCodeAliasName=_CsCugInterlockCodeAliasName_Object((1,3,6,1,4,1,9,9,89,1,1,1,2),_CsCugInterlockCodeAliasName_Type())
csCugInterlockCodeAliasName.setMaxAccess(_C)
if mibBuilder.loadTexts:csCugInterlockCodeAliasName.setStatus(_A)
_CsCugInterlockCodeRowStatus_Type=RowStatus
_CsCugInterlockCodeRowStatus_Object=MibTableColumn
csCugInterlockCodeRowStatus=_CsCugInterlockCodeRowStatus_Object((1,3,6,1,4,1,9,9,89,1,1,1,3),_CsCugInterlockCodeRowStatus_Type())
csCugInterlockCodeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:csCugInterlockCodeRowStatus.setStatus(_A)
_CsCugIfTable_Object=MibTable
csCugIfTable=_CsCugIfTable_Object((1,3,6,1,4,1,9,9,89,1,2))
if mibBuilder.loadTexts:csCugIfTable.setStatus(_A)
_CsCugIfEntry_Object=MibTableRow
csCugIfEntry=_CsCugIfEntry_Object((1,3,6,1,4,1,9,9,89,1,2,1))
csCugIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:csCugIfEntry.setStatus(_A)
class _CsCugIfAccessEnable_Type(TruthValue):defaultValue=1
_CsCugIfAccessEnable_Type.__name__=_D
_CsCugIfAccessEnable_Object=MibTableColumn
csCugIfAccessEnable=_CsCugIfAccessEnable_Object((1,3,6,1,4,1,9,9,89,1,2,1,1),_CsCugIfAccessEnable_Type())
csCugIfAccessEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:csCugIfAccessEnable.setStatus(_A)
class _CsCugIfPermitUnknownCugsToUser_Type(TruthValue):defaultValue=2
_CsCugIfPermitUnknownCugsToUser_Type.__name__=_D
_CsCugIfPermitUnknownCugsToUser_Object=MibTableColumn
csCugIfPermitUnknownCugsToUser=_CsCugIfPermitUnknownCugsToUser_Object((1,3,6,1,4,1,9,9,89,1,2,1,2),_CsCugIfPermitUnknownCugsToUser_Type())
csCugIfPermitUnknownCugsToUser.setMaxAccess(_C)
if mibBuilder.loadTexts:csCugIfPermitUnknownCugsToUser.setStatus(_A)
class _CsCugIfPermitUnknownCugsFromUser_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('deny',1),('permitPerCall',2),('permitPermanently',3)))
_CsCugIfPermitUnknownCugsFromUser_Type.__name__=_I
_CsCugIfPermitUnknownCugsFromUser_Object=MibTableColumn
csCugIfPermitUnknownCugsFromUser=_CsCugIfPermitUnknownCugsFromUser_Object((1,3,6,1,4,1,9,9,89,1,2,1,3),_CsCugIfPermitUnknownCugsFromUser_Type())
csCugIfPermitUnknownCugsFromUser.setMaxAccess(_C)
if mibBuilder.loadTexts:csCugIfPermitUnknownCugsFromUser.setStatus(_A)
_CsCugIfRowStatus_Type=RowStatus
_CsCugIfRowStatus_Object=MibTableColumn
csCugIfRowStatus=_CsCugIfRowStatus_Object((1,3,6,1,4,1,9,9,89,1,2,1,4),_CsCugIfRowStatus_Type())
csCugIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:csCugIfRowStatus.setStatus(_A)
_CsCugTable_Object=MibTable
csCugTable=_CsCugTable_Object((1,3,6,1,4,1,9,9,89,1,3))
if mibBuilder.loadTexts:csCugTable.setStatus(_A)
_CsCugEntry_Object=MibTableRow
csCugEntry=_CsCugEntry_Object((1,3,6,1,4,1,9,9,89,1,3,1))
csCugEntry.setIndexNames((0,_E,_F),(0,_B,_H))
if mibBuilder.loadTexts:csCugEntry.setStatus(_A)
class _CsCugIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CsCugIndex_Type.__name__=_G
_CsCugIndex_Object=MibTableColumn
csCugIndex=_CsCugIndex_Object((1,3,6,1,4,1,9,9,89,1,3,1,1),_CsCugIndex_Type())
csCugIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:csCugIndex.setStatus(_A)
class _CsCugPreferential_Type(TruthValue):defaultValue=2
_CsCugPreferential_Type.__name__=_D
_CsCugPreferential_Object=MibTableColumn
csCugPreferential=_CsCugPreferential_Object((1,3,6,1,4,1,9,9,89,1,3,1,2),_CsCugPreferential_Type())
csCugPreferential.setMaxAccess(_C)
if mibBuilder.loadTexts:csCugPreferential.setStatus(_A)
class _CsCugDenySameGroupToUser_Type(TruthValue):defaultValue=2
_CsCugDenySameGroupToUser_Type.__name__=_D
_CsCugDenySameGroupToUser_Object=MibTableColumn
csCugDenySameGroupToUser=_CsCugDenySameGroupToUser_Object((1,3,6,1,4,1,9,9,89,1,3,1,3),_CsCugDenySameGroupToUser_Type())
csCugDenySameGroupToUser.setMaxAccess(_C)
if mibBuilder.loadTexts:csCugDenySameGroupToUser.setStatus(_A)
class _CsCugDenySameGroupFromUser_Type(TruthValue):defaultValue=2
_CsCugDenySameGroupFromUser_Type.__name__=_D
_CsCugDenySameGroupFromUser_Object=MibTableColumn
csCugDenySameGroupFromUser=_CsCugDenySameGroupFromUser_Object((1,3,6,1,4,1,9,9,89,1,3,1,4),_CsCugDenySameGroupFromUser_Type())
csCugDenySameGroupFromUser.setMaxAccess(_C)
if mibBuilder.loadTexts:csCugDenySameGroupFromUser.setStatus(_A)
_CsCugRowStatus_Type=RowStatus
_CsCugRowStatus_Object=MibTableColumn
csCugRowStatus=_CsCugRowStatus_Object((1,3,6,1,4,1,9,9,89,1,3,1,5),_CsCugRowStatus_Type())
csCugRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:csCugRowStatus.setStatus(_A)
_CsCugMIBConformance_ObjectIdentity=ObjectIdentity
csCugMIBConformance=_CsCugMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,89,3))
_CsCugMIBCompliances_ObjectIdentity=ObjectIdentity
csCugMIBCompliances=_CsCugMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,89,3,1))
_CsCugMIBGroups_ObjectIdentity=ObjectIdentity
csCugMIBGroups=_CsCugMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,89,3,2))
csCugMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,89,3,2,1))
csCugMIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:csCugMIBGroup.setStatus(_A)
csCugMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,89,3,1,1))
csCugMIBCompliance.setObjects((_B,_V))
if mibBuilder.loadTexts:csCugMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CsCugInterlockCode':CsCugInterlockCode,_G:Unsigned32,'csCugMIB':csCugMIB,'csCugMIBObjects':csCugMIBObjects,'csCugInterlockCodeTable':csCugInterlockCodeTable,'csCugInterlockCodeEntry':csCugInterlockCodeEntry,_H:csCugInterlockCode,_K:csCugInterlockCodeAliasName,_L:csCugInterlockCodeRowStatus,'csCugIfTable':csCugIfTable,'csCugIfEntry':csCugIfEntry,_M:csCugIfAccessEnable,_N:csCugIfPermitUnknownCugsToUser,_O:csCugIfPermitUnknownCugsFromUser,_P:csCugIfRowStatus,'csCugTable':csCugTable,'csCugEntry':csCugEntry,_Q:csCugIndex,_R:csCugPreferential,_S:csCugDenySameGroupToUser,_T:csCugDenySameGroupFromUser,_U:csCugRowStatus,'csCugMIBConformance':csCugMIBConformance,'csCugMIBCompliances':csCugMIBCompliances,'csCugMIBCompliance':csCugMIBCompliance,'csCugMIBGroups':csCugMIBGroups,_V:csCugMIBGroup})