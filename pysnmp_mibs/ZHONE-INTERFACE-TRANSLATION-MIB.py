_b='zhoneIfXEntry'
_a='unavailable'
_Z='zhoneIfXDescriptionIndex'
_Y='zhoneIfTypeExtension'
_X='zhoneIfType'
_W='zhoneSubPortIndex'
_V='zhonePortIndex'
_U='ifInverseStackHigherLayer'
_T='ifInverseStackLowerLayer'
_S='ifStkDefCardType'
_R='ifStkDefLowerType'
_Q='ifStkDefUpperType'
_P='subPortIndex'
_O='pportIndex'
_N='TruthValue'
_M='OctetString'
_L='active'
_K='zhoneIfIndex'
_J='zhoneSlotIndex'
_I='zhoneShelfIndex'
_H='Zhone'
_G='deprecated'
_F='not-accessible'
_E='read-only'
_D='read-create'
_C='ZHONE-INTERFACE-TRANSLATION-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InterfaceIndex,ifEntry=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_N)
zhoneInterfaceTranslation,zhoneModules,zhoneShelfIndex,zhoneSlotIndex=mibBuilder.importSymbols(_H,'zhoneInterfaceTranslation','zhoneModules',_I,_J)
ZhoneIfType,ZhoneRowStatus,ZhoneShelfValue,ZhoneSlotValue=mibBuilder.importSymbols('Zhone-TC','ZhoneIfType','ZhoneRowStatus','ZhoneShelfValue','ZhoneSlotValue')
zhoneInterfaceTrans=ModuleIdentity((1,3,6,1,4,1,5504,6,6))
if mibBuilder.loadTexts:zhoneInterfaceTrans.setRevisions(('2011-02-24 01:38','2010-04-09 15:04','2010-04-02 14:29','2010-03-10 11:19','2008-09-28 23:15','2007-01-26 18:23','2004-05-26 15:53','2001-06-28 13:07','2001-05-23 11:02','2001-05-11 15:25','2000-09-20 12:00','2000-09-12 11:11'))
_IfIndexNext_Type=InterfaceIndex
_IfIndexNext_Object=MibScalar
ifIndexNext=_IfIndexNext_Object((1,3,6,1,4,1,5504,3,5,1),_IfIndexNext_Type())
ifIndexNext.setMaxAccess(_E)
if mibBuilder.loadTexts:ifIndexNext.setStatus(_A)
_PhysicalToIfIndexTable_Object=MibTable
physicalToIfIndexTable=_PhysicalToIfIndexTable_Object((1,3,6,1,4,1,5504,3,5,2))
if mibBuilder.loadTexts:physicalToIfIndexTable.setStatus(_G)
_PhysicalToIfIndexEntry_Object=MibTableRow
physicalToIfIndexEntry=_PhysicalToIfIndexEntry_Object((1,3,6,1,4,1,5504,3,5,2,1))
physicalToIfIndexEntry.setIndexNames((0,_H,_I),(0,_H,_J),(0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:physicalToIfIndexEntry.setStatus(_G)
class _PportIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PportIndex_Type.__name__=_B
_PportIndex_Object=MibTableColumn
pportIndex=_PportIndex_Object((1,3,6,1,4,1,5504,3,5,2,1,1),_PportIndex_Type())
pportIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pportIndex.setStatus(_G)
class _SubPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SubPortIndex_Type.__name__=_B
_SubPortIndex_Object=MibTableColumn
subPortIndex=_SubPortIndex_Object((1,3,6,1,4,1,5504,3,5,2,1,2),_SubPortIndex_Type())
subPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:subPortIndex.setStatus(_G)
_ZhoneIfIndex_Type=InterfaceIndex
_ZhoneIfIndex_Object=MibTableColumn
zhoneIfIndex=_ZhoneIfIndex_Object((1,3,6,1,4,1,5504,3,5,2,1,3),_ZhoneIfIndex_Type())
zhoneIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIfIndex.setStatus(_G)
_XxxifTypexxx_Type=IANAifType
_XxxifTypexxx_Object=MibTableColumn
xxxifTypexxx=_XxxifTypexxx_Object((1,3,6,1,4,1,5504,3,5,2,1,4),_XxxifTypexxx_Type())
xxxifTypexxx.setMaxAccess(_E)
if mibBuilder.loadTexts:xxxifTypexxx.setStatus(_G)
_IfIndexToPhysicalTable_Object=MibTable
ifIndexToPhysicalTable=_IfIndexToPhysicalTable_Object((1,3,6,1,4,1,5504,3,5,3))
if mibBuilder.loadTexts:ifIndexToPhysicalTable.setStatus(_A)
_IfIndexToPhysicalEntry_Object=MibTableRow
ifIndexToPhysicalEntry=_IfIndexToPhysicalEntry_Object((1,3,6,1,4,1,5504,3,5,3,1))
ifIndexToPhysicalEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:ifIndexToPhysicalEntry.setStatus(_A)
_ZhoneShelfNumber_Type=ZhoneShelfValue
_ZhoneShelfNumber_Object=MibTableColumn
zhoneShelfNumber=_ZhoneShelfNumber_Object((1,3,6,1,4,1,5504,3,5,3,1,1),_ZhoneShelfNumber_Type())
zhoneShelfNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneShelfNumber.setStatus(_A)
_ZhoneSlotNumber_Type=ZhoneSlotValue
_ZhoneSlotNumber_Object=MibTableColumn
zhoneSlotNumber=_ZhoneSlotNumber_Object((1,3,6,1,4,1,5504,3,5,3,1,2),_ZhoneSlotNumber_Type())
zhoneSlotNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneSlotNumber.setStatus(_A)
class _PportNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PportNumber_Type.__name__=_B
_PportNumber_Object=MibTableColumn
pportNumber=_PportNumber_Object((1,3,6,1,4,1,5504,3,5,3,1,3),_PportNumber_Type())
pportNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:pportNumber.setStatus(_A)
class _SubPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SubPortNumber_Type.__name__=_B
_SubPortNumber_Object=MibTableColumn
subPortNumber=_SubPortNumber_Object((1,3,6,1,4,1,5504,3,5,3,1,4),_SubPortNumber_Type())
subPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:subPortNumber.setStatus(_A)
_IfaceType_Type=IANAifType
_IfaceType_Object=MibTableColumn
ifaceType=_IfaceType_Object((1,3,6,1,4,1,5504,3,5,3,1,5),_IfaceType_Type())
ifaceType.setMaxAccess(_E)
if mibBuilder.loadTexts:ifaceType.setStatus(_A)
_IfaceTypeExtension_Type=ZhoneIfType
_IfaceTypeExtension_Object=MibTableColumn
ifaceTypeExtension=_IfaceTypeExtension_Object((1,3,6,1,4,1,5504,3,5,3,1,6),_IfaceTypeExtension_Type())
ifaceTypeExtension.setMaxAccess(_E)
if mibBuilder.loadTexts:ifaceTypeExtension.setStatus(_A)
_IfStackDefaultTable_Object=MibTable
ifStackDefaultTable=_IfStackDefaultTable_Object((1,3,6,1,4,1,5504,3,5,4))
if mibBuilder.loadTexts:ifStackDefaultTable.setStatus(_A)
_IfStackDefaultEntry_Object=MibTableRow
ifStackDefaultEntry=_IfStackDefaultEntry_Object((1,3,6,1,4,1,5504,3,5,4,1))
ifStackDefaultEntry.setIndexNames((0,_C,_Q),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:ifStackDefaultEntry.setStatus(_A)
class _IfStkDefCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IfStkDefCardType_Type.__name__=_B
_IfStkDefCardType_Object=MibTableColumn
ifStkDefCardType=_IfStkDefCardType_Object((1,3,6,1,4,1,5504,3,5,4,1,1),_IfStkDefCardType_Type())
ifStkDefCardType.setMaxAccess(_F)
if mibBuilder.loadTexts:ifStkDefCardType.setStatus(_A)
_IfStkDefUpperType_Type=IANAifType
_IfStkDefUpperType_Object=MibTableColumn
ifStkDefUpperType=_IfStkDefUpperType_Object((1,3,6,1,4,1,5504,3,5,4,1,2),_IfStkDefUpperType_Type())
ifStkDefUpperType.setMaxAccess(_F)
if mibBuilder.loadTexts:ifStkDefUpperType.setStatus(_A)
_IfStkDefLowerType_Type=IANAifType
_IfStkDefLowerType_Object=MibTableColumn
ifStkDefLowerType=_IfStkDefLowerType_Object((1,3,6,1,4,1,5504,3,5,4,1,3),_IfStkDefLowerType_Type())
ifStkDefLowerType.setMaxAccess(_F)
if mibBuilder.loadTexts:ifStkDefLowerType.setStatus(_A)
class _IfStkDefUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IfStkDefUnits_Type.__name__=_B
_IfStkDefUnits_Object=MibTableColumn
ifStkDefUnits=_IfStkDefUnits_Object((1,3,6,1,4,1,5504,3,5,4,1,4),_IfStkDefUnits_Type())
ifStkDefUnits.setMaxAccess(_D)
if mibBuilder.loadTexts:ifStkDefUnits.setStatus(_A)
if mibBuilder.loadTexts:ifStkDefUnits.setUnits('count')
class _IfStkDefAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_IfStkDefAdminStatus_Type.__name__=_B
_IfStkDefAdminStatus_Object=MibTableColumn
ifStkDefAdminStatus=_IfStkDefAdminStatus_Object((1,3,6,1,4,1,5504,3,5,4,1,5),_IfStkDefAdminStatus_Type())
ifStkDefAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ifStkDefAdminStatus.setStatus(_A)
_IfStkDefRowStatus_Type=ZhoneRowStatus
_IfStkDefRowStatus_Object=MibTableColumn
ifStkDefRowStatus=_IfStkDefRowStatus_Object((1,3,6,1,4,1,5504,3,5,4,1,6),_IfStkDefRowStatus_Type())
ifStkDefRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ifStkDefRowStatus.setStatus(_A)
_IfInverseStackTable_Object=MibTable
ifInverseStackTable=_IfInverseStackTable_Object((1,3,6,1,4,1,5504,3,5,5))
if mibBuilder.loadTexts:ifInverseStackTable.setStatus(_A)
_IfInverseStackEntry_Object=MibTableRow
ifInverseStackEntry=_IfInverseStackEntry_Object((1,3,6,1,4,1,5504,3,5,5,1))
ifInverseStackEntry.setIndexNames((0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:ifInverseStackEntry.setStatus(_A)
_IfInverseStackLowerLayer_Type=InterfaceIndex
_IfInverseStackLowerLayer_Object=MibTableColumn
ifInverseStackLowerLayer=_IfInverseStackLowerLayer_Object((1,3,6,1,4,1,5504,3,5,5,1,1),_IfInverseStackLowerLayer_Type())
ifInverseStackLowerLayer.setMaxAccess(_F)
if mibBuilder.loadTexts:ifInverseStackLowerLayer.setStatus(_A)
_IfInverseStackHigherLayer_Type=InterfaceIndex
_IfInverseStackHigherLayer_Object=MibTableColumn
ifInverseStackHigherLayer=_IfInverseStackHigherLayer_Object((1,3,6,1,4,1,5504,3,5,5,1,2),_IfInverseStackHigherLayer_Type())
ifInverseStackHigherLayer.setMaxAccess(_F)
if mibBuilder.loadTexts:ifInverseStackHigherLayer.setStatus(_A)
class _IfInverseStackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_IfInverseStackStatus_Type.__name__=_B
_IfInverseStackStatus_Object=MibTableColumn
ifInverseStackStatus=_IfInverseStackStatus_Object((1,3,6,1,4,1,5504,3,5,5,1,3),_IfInverseStackStatus_Type())
ifInverseStackStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ifInverseStackStatus.setStatus(_A)
_ZhoneIfXTable_Object=MibTable
zhoneIfXTable=_ZhoneIfXTable_Object((1,3,6,1,4,1,5504,3,5,6))
if mibBuilder.loadTexts:zhoneIfXTable.setStatus(_A)
_ZhoneIfXEntry_Object=MibTableRow
zhoneIfXEntry=_ZhoneIfXEntry_Object((1,3,6,1,4,1,5504,3,5,6,1))
if mibBuilder.loadTexts:zhoneIfXEntry.setStatus(_A)
class _PhysicalFlag_Type(TruthValue):defaultValue=2
_PhysicalFlag_Type.__name__=_N
_PhysicalFlag_Object=MibTableColumn
physicalFlag=_PhysicalFlag_Object((1,3,6,1,4,1,5504,3,5,6,1,1),_PhysicalFlag_Type())
physicalFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:physicalFlag.setStatus(_A)
_IfTypeExtension_Type=ZhoneIfType
_IfTypeExtension_Object=MibTableColumn
ifTypeExtension=_IfTypeExtension_Object((1,3,6,1,4,1,5504,3,5,6,1,2),_IfTypeExtension_Type())
ifTypeExtension.setMaxAccess(_D)
if mibBuilder.loadTexts:ifTypeExtension.setStatus(_A)
class _RedundancyParam1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_RedundancyParam1_Type.__name__=_B
_RedundancyParam1_Object=MibTableColumn
redundancyParam1=_RedundancyParam1_Object((1,3,6,1,4,1,5504,3,5,6,1,3),_RedundancyParam1_Type())
redundancyParam1.setMaxAccess(_D)
if mibBuilder.loadTexts:redundancyParam1.setStatus(_A)
_ZhoneIfXEntryIfTypeAlias_Type=IANAifType
_ZhoneIfXEntryIfTypeAlias_Object=MibTableColumn
zhoneIfXEntryIfTypeAlias=_ZhoneIfXEntryIfTypeAlias_Object((1,3,6,1,4,1,5504,3,5,6,1,4),_ZhoneIfXEntryIfTypeAlias_Type())
zhoneIfXEntryIfTypeAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIfXEntryIfTypeAlias.setStatus(_A)
_ZhoneIfXEntryRowStatus_Type=ZhoneRowStatus
_ZhoneIfXEntryRowStatus_Object=MibTableColumn
zhoneIfXEntryRowStatus=_ZhoneIfXEntryRowStatus_Object((1,3,6,1,4,1,5504,3,5,6,1,5),_ZhoneIfXEntryRowStatus_Type())
zhoneIfXEntryRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIfXEntryRowStatus.setStatus(_A)
class _ZhoneIfXEntryShelfAlias_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ZhoneIfXEntryShelfAlias_Type.__name__=_B
_ZhoneIfXEntryShelfAlias_Object=MibTableColumn
zhoneIfXEntryShelfAlias=_ZhoneIfXEntryShelfAlias_Object((1,3,6,1,4,1,5504,3,5,6,1,6),_ZhoneIfXEntryShelfAlias_Type())
zhoneIfXEntryShelfAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIfXEntryShelfAlias.setStatus(_A)
class _ZhoneIfXEntrySlotAlias_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,33))
_ZhoneIfXEntrySlotAlias_Type.__name__=_B
_ZhoneIfXEntrySlotAlias_Object=MibTableColumn
zhoneIfXEntrySlotAlias=_ZhoneIfXEntrySlotAlias_Object((1,3,6,1,4,1,5504,3,5,6,1,7),_ZhoneIfXEntrySlotAlias_Type())
zhoneIfXEntrySlotAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIfXEntrySlotAlias.setStatus(_A)
_ZhoneIfXEntryPortAlias_Type=Integer32
_ZhoneIfXEntryPortAlias_Object=MibTableColumn
zhoneIfXEntryPortAlias=_ZhoneIfXEntryPortAlias_Object((1,3,6,1,4,1,5504,3,5,6,1,8),_ZhoneIfXEntryPortAlias_Type())
zhoneIfXEntryPortAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIfXEntryPortAlias.setStatus(_A)
_ZhoneIfXEntrySubportAlias_Type=Integer32
_ZhoneIfXEntrySubportAlias_Object=MibTableColumn
zhoneIfXEntrySubportAlias=_ZhoneIfXEntrySubportAlias_Object((1,3,6,1,4,1,5504,3,5,6,1,9),_ZhoneIfXEntrySubportAlias_Type())
zhoneIfXEntrySubportAlias.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIfXEntrySubportAlias.setStatus(_A)
class _ZhoneIfXDescriptionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhoneIfXDescriptionIndex_Type.__name__=_B
_ZhoneIfXDescriptionIndex_Object=MibTableColumn
zhoneIfXDescriptionIndex=_ZhoneIfXDescriptionIndex_Object((1,3,6,1,4,1,5504,3,5,6,1,10),_ZhoneIfXDescriptionIndex_Type())
zhoneIfXDescriptionIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneIfXDescriptionIndex.setStatus(_A)
_ZhonePhysicalToIfIndexTable_Object=MibTable
zhonePhysicalToIfIndexTable=_ZhonePhysicalToIfIndexTable_Object((1,3,6,1,4,1,5504,3,5,7))
if mibBuilder.loadTexts:zhonePhysicalToIfIndexTable.setStatus(_A)
_ZhonePhysicalToIfIndexEntry_Object=MibTableRow
zhonePhysicalToIfIndexEntry=_ZhonePhysicalToIfIndexEntry_Object((1,3,6,1,4,1,5504,3,5,7,1))
zhonePhysicalToIfIndexEntry.setIndexNames((0,_H,_I),(0,_H,_J),(0,_C,_V),(0,_C,_W),(0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:zhonePhysicalToIfIndexEntry.setStatus(_A)
class _ZhonePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhonePortIndex_Type.__name__=_B
_ZhonePortIndex_Object=MibTableColumn
zhonePortIndex=_ZhonePortIndex_Object((1,3,6,1,4,1,5504,3,5,7,1,1),_ZhonePortIndex_Type())
zhonePortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhonePortIndex.setStatus(_A)
class _ZhoneSubPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhoneSubPortIndex_Type.__name__=_B
_ZhoneSubPortIndex_Object=MibTableColumn
zhoneSubPortIndex=_ZhoneSubPortIndex_Object((1,3,6,1,4,1,5504,3,5,7,1,2),_ZhoneSubPortIndex_Type())
zhoneSubPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneSubPortIndex.setStatus(_A)
_ZhoneIfType_Type=IANAifType
_ZhoneIfType_Object=MibTableColumn
zhoneIfType=_ZhoneIfType_Object((1,3,6,1,4,1,5504,3,5,7,1,4),_ZhoneIfType_Type())
zhoneIfType.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIfType.setStatus(_A)
_ZhoneIfTypeExtension_Type=ZhoneIfType
_ZhoneIfTypeExtension_Object=MibTableColumn
zhoneIfTypeExtension=_ZhoneIfTypeExtension_Object((1,3,6,1,4,1,5504,3,5,7,1,5),_ZhoneIfTypeExtension_Type())
zhoneIfTypeExtension.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneIfTypeExtension.setStatus(_A)
_ZhonePhysicalIfIndex_Type=InterfaceIndex
_ZhonePhysicalIfIndex_Object=MibTableColumn
zhonePhysicalIfIndex=_ZhonePhysicalIfIndex_Object((1,3,6,1,4,1,5504,3,5,7,1,6),_ZhonePhysicalIfIndex_Type())
zhonePhysicalIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zhonePhysicalIfIndex.setStatus(_A)
_ZhoneDescriptionTable_Object=MibTable
zhoneDescriptionTable=_ZhoneDescriptionTable_Object((1,3,6,1,4,1,5504,3,5,8))
if mibBuilder.loadTexts:zhoneDescriptionTable.setStatus(_A)
_ZhoneDescriptionEntry_Object=MibTableRow
zhoneDescriptionEntry=_ZhoneDescriptionEntry_Object((1,3,6,1,4,1,5504,3,5,8,1))
zhoneDescriptionEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:zhoneDescriptionEntry.setStatus(_A)
_ZhoneDescriptionRowStatus_Type=ZhoneRowStatus
_ZhoneDescriptionRowStatus_Object=MibTableColumn
zhoneDescriptionRowStatus=_ZhoneDescriptionRowStatus_Object((1,3,6,1,4,1,5504,3,5,8,1,1),_ZhoneDescriptionRowStatus_Type())
zhoneDescriptionRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDescriptionRowStatus.setStatus(_A)
class _ZhoneDescriptionText_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZhoneDescriptionText_Type.__name__=_M
_ZhoneDescriptionText_Object=MibTableColumn
zhoneDescriptionText=_ZhoneDescriptionText_Object((1,3,6,1,4,1,5504,3,5,8,1,2),_ZhoneDescriptionText_Type())
zhoneDescriptionText.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneDescriptionText.setStatus(_A)
_ZhoneIfXDescriptionIndexNext_Type=Unsigned32
_ZhoneIfXDescriptionIndexNext_Object=MibScalar
zhoneIfXDescriptionIndexNext=_ZhoneIfXDescriptionIndexNext_Object((1,3,6,1,4,1,5504,3,5,9),_ZhoneIfXDescriptionIndexNext_Type())
zhoneIfXDescriptionIndexNext.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneIfXDescriptionIndexNext.setStatus(_A)
_ZhoneLineRedStatusTable_Object=MibTable
zhoneLineRedStatusTable=_ZhoneLineRedStatusTable_Object((1,3,6,1,4,1,5504,3,5,10))
if mibBuilder.loadTexts:zhoneLineRedStatusTable.setStatus(_A)
_ZhoneLineRedStatusEntry_Object=MibTableRow
zhoneLineRedStatusEntry=_ZhoneLineRedStatusEntry_Object((1,3,6,1,4,1,5504,3,5,10,1))
zhoneLineRedStatusEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:zhoneLineRedStatusEntry.setStatus(_A)
class _ZhoneLineRedStatusFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inactive',1),('standby',2),(_L,3),(_a,4)))
_ZhoneLineRedStatusFunction_Type.__name__=_B
_ZhoneLineRedStatusFunction_Object=MibTableColumn
zhoneLineRedStatusFunction=_ZhoneLineRedStatusFunction_Object((1,3,6,1,4,1,5504,3,5,10,1,1),_ZhoneLineRedStatusFunction_Type())
zhoneLineRedStatusFunction.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneLineRedStatusFunction.setStatus(_A)
class _ZhoneLineRedOpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('oos',2),('trafficDisabled',3),(_a,4)))
_ZhoneLineRedOpStatus_Type.__name__=_B
_ZhoneLineRedOpStatus_Object=MibTableColumn
zhoneLineRedOpStatus=_ZhoneLineRedOpStatus_Object((1,3,6,1,4,1,5504,3,5,10,1,2),_ZhoneLineRedOpStatus_Type())
zhoneLineRedOpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneLineRedOpStatus.setStatus(_A)
_ZhoneLineRedTraps_ObjectIdentity=ObjectIdentity
zhoneLineRedTraps=_ZhoneLineRedTraps_ObjectIdentity((1,3,6,1,4,1,5504,3,5,11))
if mibBuilder.loadTexts:zhoneLineRedTraps.setStatus(_A)
_ZhoneLineRedTrapsPrefix_ObjectIdentity=ObjectIdentity
zhoneLineRedTrapsPrefix=_ZhoneLineRedTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,5504,3,5,11,0))
if mibBuilder.loadTexts:zhoneLineRedTrapsPrefix.setStatus(_A)
ifEntry.registerAugmentions((_C,_b))
zhoneIfXEntry.setIndexNames(*ifEntry.getIndexNames())
zhoneLineRedundancyUnsafe=NotificationType((1,3,6,1,4,1,5504,3,5,11,0,1))
if mibBuilder.loadTexts:zhoneLineRedundancyUnsafe.setStatus(_A)
zhoneLineRedundancySafe=NotificationType((1,3,6,1,4,1,5504,3,5,11,0,2))
if mibBuilder.loadTexts:zhoneLineRedundancySafe.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ifIndexNext':ifIndexNext,'physicalToIfIndexTable':physicalToIfIndexTable,'physicalToIfIndexEntry':physicalToIfIndexEntry,_O:pportIndex,_P:subPortIndex,_K:zhoneIfIndex,'xxxifTypexxx':xxxifTypexxx,'ifIndexToPhysicalTable':ifIndexToPhysicalTable,'ifIndexToPhysicalEntry':ifIndexToPhysicalEntry,'zhoneShelfNumber':zhoneShelfNumber,'zhoneSlotNumber':zhoneSlotNumber,'pportNumber':pportNumber,'subPortNumber':subPortNumber,'ifaceType':ifaceType,'ifaceTypeExtension':ifaceTypeExtension,'ifStackDefaultTable':ifStackDefaultTable,'ifStackDefaultEntry':ifStackDefaultEntry,_S:ifStkDefCardType,_Q:ifStkDefUpperType,_R:ifStkDefLowerType,'ifStkDefUnits':ifStkDefUnits,'ifStkDefAdminStatus':ifStkDefAdminStatus,'ifStkDefRowStatus':ifStkDefRowStatus,'ifInverseStackTable':ifInverseStackTable,'ifInverseStackEntry':ifInverseStackEntry,_T:ifInverseStackLowerLayer,_U:ifInverseStackHigherLayer,'ifInverseStackStatus':ifInverseStackStatus,'zhoneIfXTable':zhoneIfXTable,_b:zhoneIfXEntry,'physicalFlag':physicalFlag,'ifTypeExtension':ifTypeExtension,'redundancyParam1':redundancyParam1,'zhoneIfXEntryIfTypeAlias':zhoneIfXEntryIfTypeAlias,'zhoneIfXEntryRowStatus':zhoneIfXEntryRowStatus,'zhoneIfXEntryShelfAlias':zhoneIfXEntryShelfAlias,'zhoneIfXEntrySlotAlias':zhoneIfXEntrySlotAlias,'zhoneIfXEntryPortAlias':zhoneIfXEntryPortAlias,'zhoneIfXEntrySubportAlias':zhoneIfXEntrySubportAlias,_Z:zhoneIfXDescriptionIndex,'zhonePhysicalToIfIndexTable':zhonePhysicalToIfIndexTable,'zhonePhysicalToIfIndexEntry':zhonePhysicalToIfIndexEntry,_V:zhonePortIndex,_W:zhoneSubPortIndex,_X:zhoneIfType,_Y:zhoneIfTypeExtension,'zhonePhysicalIfIndex':zhonePhysicalIfIndex,'zhoneDescriptionTable':zhoneDescriptionTable,'zhoneDescriptionEntry':zhoneDescriptionEntry,'zhoneDescriptionRowStatus':zhoneDescriptionRowStatus,'zhoneDescriptionText':zhoneDescriptionText,'zhoneIfXDescriptionIndexNext':zhoneIfXDescriptionIndexNext,'zhoneLineRedStatusTable':zhoneLineRedStatusTable,'zhoneLineRedStatusEntry':zhoneLineRedStatusEntry,'zhoneLineRedStatusFunction':zhoneLineRedStatusFunction,'zhoneLineRedOpStatus':zhoneLineRedOpStatus,'zhoneLineRedTraps':zhoneLineRedTraps,'zhoneLineRedTrapsPrefix':zhoneLineRedTrapsPrefix,'zhoneLineRedundancyUnsafe':zhoneLineRedundancyUnsafe,'zhoneLineRedundancySafe':zhoneLineRedundancySafe,'zhoneInterfaceTrans':zhoneInterfaceTrans})