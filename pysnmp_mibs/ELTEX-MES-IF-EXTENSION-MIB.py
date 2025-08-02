_G='eltIfDot1qIngressCvlanTag'
_F='ELTEX-MES-IF-EXTENSION-MIB'
_E='ifIndex'
_D='IF-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesIfExtensionMIB,=mibBuilder.importSymbols('ELTEX-MES-MNG-MIB','eltMesIfExtensionMIB')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndex','InterfaceIndexOrZero',_E)
PortList,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
_EltMesIfExtensionMIBObjects_ObjectIdentity=ObjectIdentity
eltMesIfExtensionMIBObjects=_EltMesIfExtensionMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,276,1))
_EltMesIfExtDot1qCustomEtherType_ObjectIdentity=ObjectIdentity
eltMesIfExtDot1qCustomEtherType=_EltMesIfExtDot1qCustomEtherType_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,276,1,3))
_EltIfDot1qCustomEgressEtherTypeTable_Object=MibTable
eltIfDot1qCustomEgressEtherTypeTable=_EltIfDot1qCustomEgressEtherTypeTable_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,1))
if mibBuilder.loadTexts:eltIfDot1qCustomEgressEtherTypeTable.setStatus(_A)
_EltIfDot1qCustomEgressEtherTypeEntry_Object=MibTableRow
eltIfDot1qCustomEgressEtherTypeEntry=_EltIfDot1qCustomEgressEtherTypeEntry_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,1,1))
eltIfDot1qCustomEgressEtherTypeEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:eltIfDot1qCustomEgressEtherTypeEntry.setStatus(_A)
class _EltIfDot1qCustomEgressEtherType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltIfDot1qCustomEgressEtherType_Type.__name__=_C
_EltIfDot1qCustomEgressEtherType_Object=MibTableColumn
eltIfDot1qCustomEgressEtherType=_EltIfDot1qCustomEgressEtherType_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,1,1,1),_EltIfDot1qCustomEgressEtherType_Type())
eltIfDot1qCustomEgressEtherType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltIfDot1qCustomEgressEtherType.setStatus(_A)
_EltIfDot1qCustomIngressEtherTypeTable_Object=MibTable
eltIfDot1qCustomIngressEtherTypeTable=_EltIfDot1qCustomIngressEtherTypeTable_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,2))
if mibBuilder.loadTexts:eltIfDot1qCustomIngressEtherTypeTable.setStatus(_A)
_EltIfDot1qCustomIngressEtherTypeEntry_Object=MibTableRow
eltIfDot1qCustomIngressEtherTypeEntry=_EltIfDot1qCustomIngressEtherTypeEntry_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,2,1))
eltIfDot1qCustomIngressEtherTypeEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:eltIfDot1qCustomIngressEtherTypeEntry.setStatus(_A)
class _EltIfDot1qCustomIngressEtherType1_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(33024,33024))
_EltIfDot1qCustomIngressEtherType1_Type.__name__=_C
_EltIfDot1qCustomIngressEtherType1_Object=MibTableColumn
eltIfDot1qCustomIngressEtherType1=_EltIfDot1qCustomIngressEtherType1_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,2,1,1),_EltIfDot1qCustomIngressEtherType1_Type())
eltIfDot1qCustomIngressEtherType1.setMaxAccess(_B)
if mibBuilder.loadTexts:eltIfDot1qCustomIngressEtherType1.setStatus(_A)
class _EltIfDot1qCustomIngressEtherType2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,33023),ValueRangeConstraint(33025,65535))
_EltIfDot1qCustomIngressEtherType2_Type.__name__=_C
_EltIfDot1qCustomIngressEtherType2_Object=MibTableColumn
eltIfDot1qCustomIngressEtherType2=_EltIfDot1qCustomIngressEtherType2_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,2,1,2),_EltIfDot1qCustomIngressEtherType2_Type())
eltIfDot1qCustomIngressEtherType2.setMaxAccess(_B)
if mibBuilder.loadTexts:eltIfDot1qCustomIngressEtherType2.setStatus(_A)
class _EltIfDot1qCustomIngressEtherType3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,33023),ValueRangeConstraint(33025,65535))
_EltIfDot1qCustomIngressEtherType3_Type.__name__=_C
_EltIfDot1qCustomIngressEtherType3_Object=MibTableColumn
eltIfDot1qCustomIngressEtherType3=_EltIfDot1qCustomIngressEtherType3_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,2,1,3),_EltIfDot1qCustomIngressEtherType3_Type())
eltIfDot1qCustomIngressEtherType3.setMaxAccess(_B)
if mibBuilder.loadTexts:eltIfDot1qCustomIngressEtherType3.setStatus(_A)
class _EltIfDot1qCustomIngressEtherType4_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,33023),ValueRangeConstraint(33025,65535))
_EltIfDot1qCustomIngressEtherType4_Type.__name__=_C
_EltIfDot1qCustomIngressEtherType4_Object=MibTableColumn
eltIfDot1qCustomIngressEtherType4=_EltIfDot1qCustomIngressEtherType4_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,2,1,4),_EltIfDot1qCustomIngressEtherType4_Type())
eltIfDot1qCustomIngressEtherType4.setMaxAccess(_B)
if mibBuilder.loadTexts:eltIfDot1qCustomIngressEtherType4.setStatus(_A)
class _EltIfDot1qCustomIngressEtherType5_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,33023),ValueRangeConstraint(33025,65535))
_EltIfDot1qCustomIngressEtherType5_Type.__name__=_C
_EltIfDot1qCustomIngressEtherType5_Object=MibTableColumn
eltIfDot1qCustomIngressEtherType5=_EltIfDot1qCustomIngressEtherType5_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,2,1,5),_EltIfDot1qCustomIngressEtherType5_Type())
eltIfDot1qCustomIngressEtherType5.setMaxAccess(_B)
if mibBuilder.loadTexts:eltIfDot1qCustomIngressEtherType5.setStatus(_A)
class _EltIfDot1qCustomIngressEtherType6_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,33023),ValueRangeConstraint(33025,65535))
_EltIfDot1qCustomIngressEtherType6_Type.__name__=_C
_EltIfDot1qCustomIngressEtherType6_Object=MibTableColumn
eltIfDot1qCustomIngressEtherType6=_EltIfDot1qCustomIngressEtherType6_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,2,1,6),_EltIfDot1qCustomIngressEtherType6_Type())
eltIfDot1qCustomIngressEtherType6.setMaxAccess(_B)
if mibBuilder.loadTexts:eltIfDot1qCustomIngressEtherType6.setStatus(_A)
class _EltIfDot1qCustomIngressEtherType7_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,33023),ValueRangeConstraint(33025,65535))
_EltIfDot1qCustomIngressEtherType7_Type.__name__=_C
_EltIfDot1qCustomIngressEtherType7_Object=MibTableColumn
eltIfDot1qCustomIngressEtherType7=_EltIfDot1qCustomIngressEtherType7_Object((1,3,6,1,4,1,35265,1,23,1,276,1,3,2,1,7),_EltIfDot1qCustomIngressEtherType7_Type())
eltIfDot1qCustomIngressEtherType7.setMaxAccess(_B)
if mibBuilder.loadTexts:eltIfDot1qCustomIngressEtherType7.setStatus(_A)
_EltMesIfExtDot1q_ObjectIdentity=ObjectIdentity
eltMesIfExtDot1q=_EltMesIfExtDot1q_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,276,1,4))
_EltIfDot1qIngressCvlanTable_Object=MibTable
eltIfDot1qIngressCvlanTable=_EltIfDot1qIngressCvlanTable_Object((1,3,6,1,4,1,35265,1,23,1,276,1,4,1))
if mibBuilder.loadTexts:eltIfDot1qIngressCvlanTable.setStatus(_A)
_EltIfDot1qIngressCvlanEntry_Object=MibTableRow
eltIfDot1qIngressCvlanEntry=_EltIfDot1qIngressCvlanEntry_Object((1,3,6,1,4,1,35265,1,23,1,276,1,4,1,1))
eltIfDot1qIngressCvlanEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:eltIfDot1qIngressCvlanEntry.setStatus(_A)
class _EltIfDot1qIngressCvlanTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_EltIfDot1qIngressCvlanTag_Type.__name__=_C
_EltIfDot1qIngressCvlanTag_Object=MibTableColumn
eltIfDot1qIngressCvlanTag=_EltIfDot1qIngressCvlanTag_Object((1,3,6,1,4,1,35265,1,23,1,276,1,4,1,1,1),_EltIfDot1qIngressCvlanTag_Type())
eltIfDot1qIngressCvlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:eltIfDot1qIngressCvlanTag.setStatus(_A)
_EltIfDot1qTr101CVlanMapTable_Object=MibTable
eltIfDot1qTr101CVlanMapTable=_EltIfDot1qTr101CVlanMapTable_Object((1,3,6,1,4,1,35265,1,23,1,276,1,4,2))
if mibBuilder.loadTexts:eltIfDot1qTr101CVlanMapTable.setStatus(_A)
_EltIfDot1qTr101CVlanMapEntry_Object=MibTableRow
eltIfDot1qTr101CVlanMapEntry=_EltIfDot1qTr101CVlanMapEntry_Object((1,3,6,1,4,1,35265,1,23,1,276,1,4,2,1))
eltIfDot1qTr101CVlanMapEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:eltIfDot1qTr101CVlanMapEntry.setStatus(_A)
_EltIfDot1qTr101CVlanMapRowStatus_Type=RowStatus
_EltIfDot1qTr101CVlanMapRowStatus_Object=MibTableColumn
eltIfDot1qTr101CVlanMapRowStatus=_EltIfDot1qTr101CVlanMapRowStatus_Object((1,3,6,1,4,1,35265,1,23,1,276,1,4,2,1,1),_EltIfDot1qTr101CVlanMapRowStatus_Type())
eltIfDot1qTr101CVlanMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltIfDot1qTr101CVlanMapRowStatus.setStatus(_A)
_EltIfDot1qTr101CVlanMapPortList_Type=PortList
_EltIfDot1qTr101CVlanMapPortList_Object=MibTableColumn
eltIfDot1qTr101CVlanMapPortList=_EltIfDot1qTr101CVlanMapPortList_Object((1,3,6,1,4,1,35265,1,23,1,276,1,4,2,1,2),_EltIfDot1qTr101CVlanMapPortList_Type())
eltIfDot1qTr101CVlanMapPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:eltIfDot1qTr101CVlanMapPortList.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'eltMesIfExtensionMIBObjects':eltMesIfExtensionMIBObjects,'eltMesIfExtDot1qCustomEtherType':eltMesIfExtDot1qCustomEtherType,'eltIfDot1qCustomEgressEtherTypeTable':eltIfDot1qCustomEgressEtherTypeTable,'eltIfDot1qCustomEgressEtherTypeEntry':eltIfDot1qCustomEgressEtherTypeEntry,'eltIfDot1qCustomEgressEtherType':eltIfDot1qCustomEgressEtherType,'eltIfDot1qCustomIngressEtherTypeTable':eltIfDot1qCustomIngressEtherTypeTable,'eltIfDot1qCustomIngressEtherTypeEntry':eltIfDot1qCustomIngressEtherTypeEntry,'eltIfDot1qCustomIngressEtherType1':eltIfDot1qCustomIngressEtherType1,'eltIfDot1qCustomIngressEtherType2':eltIfDot1qCustomIngressEtherType2,'eltIfDot1qCustomIngressEtherType3':eltIfDot1qCustomIngressEtherType3,'eltIfDot1qCustomIngressEtherType4':eltIfDot1qCustomIngressEtherType4,'eltIfDot1qCustomIngressEtherType5':eltIfDot1qCustomIngressEtherType5,'eltIfDot1qCustomIngressEtherType6':eltIfDot1qCustomIngressEtherType6,'eltIfDot1qCustomIngressEtherType7':eltIfDot1qCustomIngressEtherType7,'eltMesIfExtDot1q':eltMesIfExtDot1q,'eltIfDot1qIngressCvlanTable':eltIfDot1qIngressCvlanTable,'eltIfDot1qIngressCvlanEntry':eltIfDot1qIngressCvlanEntry,_G:eltIfDot1qIngressCvlanTag,'eltIfDot1qTr101CVlanMapTable':eltIfDot1qTr101CVlanMapTable,'eltIfDot1qTr101CVlanMapEntry':eltIfDot1qTr101CVlanMapEntry,'eltIfDot1qTr101CVlanMapRowStatus':eltIfDot1qTr101CVlanMapRowStatus,'eltIfDot1qTr101CVlanMapPortList':eltIfDot1qTr101CVlanMapPortList})