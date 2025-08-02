_a='ciscoWanCesPortsUsedGroup'
_Z='ciscoWanCesPortDs0InDs1Group'
_Y='ciscoWanCesPortConfGroup'
_X='cesPortsUsedLine8'
_W='cesPortsUsedLine7'
_V='cesPortsUsedLine6'
_U='cesPortsUsedLine5'
_T='cesPortsUsedLine4'
_S='cesPortsUsedLine3'
_R='cesPortsUsedLine2'
_Q='cesPortsUsedLine1'
_P='cesPortBERTEnable'
_O='cesPortState'
_N='cesPortSpeed'
_M='cesPortNumOfSCIPerDS0'
_L='cesPortNumOfDs0Slot'
_K='cesPortDs0ConfigBitMap'
_J='cesPortType'
_I='cesPortLineNum'
_H='cesPortRowStatus'
_G='cesPortNextAvailable'
_F='cesPortNum'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='CISCO-WAN-CES-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
circuitEmulation,=mibBuilder.importSymbols('BASIS-MIB','circuitEmulation')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanCesPortMIB=ModuleIdentity((1,3,6,1,4,1,351,150,40))
if mibBuilder.loadTexts:ciscoWanCesPortMIB.setRevisions(('2002-11-13 00:00',))
_CesmPort_ObjectIdentity=ObjectIdentity
cesmPort=_CesmPort_ObjectIdentity((1,3,6,1,4,1,351,110,5,3,1))
_CesmPortCnfGrp_ObjectIdentity=ObjectIdentity
cesmPortCnfGrp=_CesmPortCnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,3,1,1))
_CesmPortCnfGrpTable_Object=MibTable
cesmPortCnfGrpTable=_CesmPortCnfGrpTable_Object((1,3,6,1,4,1,351,110,5,3,1,1,1))
if mibBuilder.loadTexts:cesmPortCnfGrpTable.setStatus(_A)
_CesmPortCnfGrpEntry_Object=MibTableRow
cesmPortCnfGrpEntry=_CesmPortCnfGrpEntry_Object((1,3,6,1,4,1,351,110,5,3,1,1,1,1))
cesmPortCnfGrpEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cesmPortCnfGrpEntry.setStatus(_A)
class _CesPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_CesPortNum_Type.__name__=_C
_CesPortNum_Object=MibTableColumn
cesPortNum=_CesPortNum_Object((1,3,6,1,4,1,351,110,5,3,1,1,1,1,1),_CesPortNum_Type())
cesPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortNum.setStatus(_A)
class _CesPortRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_CesPortRowStatus_Type.__name__=_C
_CesPortRowStatus_Object=MibTableColumn
cesPortRowStatus=_CesPortRowStatus_Object((1,3,6,1,4,1,351,110,5,3,1,1,1,1,2),_CesPortRowStatus_Type())
cesPortRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cesPortRowStatus.setStatus(_A)
class _CesPortLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_CesPortLineNum_Type.__name__=_C
_CesPortLineNum_Object=MibTableColumn
cesPortLineNum=_CesPortLineNum_Object((1,3,6,1,4,1,351,110,5,3,1,1,1,1,3),_CesPortLineNum_Type())
cesPortLineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:cesPortLineNum.setStatus(_A)
class _CesPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('structured',1),('unstructured',2),('framingOnVcDisconnect',3),('strau',4)))
_CesPortType_Type.__name__=_C
_CesPortType_Object=MibTableColumn
cesPortType=_CesPortType_Object((1,3,6,1,4,1,351,110,5,3,1,1,1,1,4),_CesPortType_Type())
cesPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:cesPortType.setStatus(_A)
class _CesPortDs0ConfigBitMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CesPortDs0ConfigBitMap_Type.__name__=_C
_CesPortDs0ConfigBitMap_Object=MibTableColumn
cesPortDs0ConfigBitMap=_CesPortDs0ConfigBitMap_Object((1,3,6,1,4,1,351,110,5,3,1,1,1,1,5),_CesPortDs0ConfigBitMap_Type())
cesPortDs0ConfigBitMap.setMaxAccess(_E)
if mibBuilder.loadTexts:cesPortDs0ConfigBitMap.setStatus(_A)
class _CesPortNumOfDs0Slot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CesPortNumOfDs0Slot_Type.__name__=_C
_CesPortNumOfDs0Slot_Object=MibTableColumn
cesPortNumOfDs0Slot=_CesPortNumOfDs0Slot_Object((1,3,6,1,4,1,351,110,5,3,1,1,1,1,6),_CesPortNumOfDs0Slot_Type())
cesPortNumOfDs0Slot.setMaxAccess(_E)
if mibBuilder.loadTexts:cesPortNumOfDs0Slot.setStatus(_A)
class _CesPortNumOfSCIPerDS0_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CesPortNumOfSCIPerDS0_Type.__name__=_C
_CesPortNumOfSCIPerDS0_Object=MibTableColumn
cesPortNumOfSCIPerDS0=_CesPortNumOfSCIPerDS0_Object((1,3,6,1,4,1,351,110,5,3,1,1,1,1,7),_CesPortNumOfSCIPerDS0_Type())
cesPortNumOfSCIPerDS0.setMaxAccess(_E)
if mibBuilder.loadTexts:cesPortNumOfSCIPerDS0.setStatus(_A)
class _CesPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,44736))
_CesPortSpeed_Type.__name__=_C
_CesPortSpeed_Object=MibTableColumn
cesPortSpeed=_CesPortSpeed_Object((1,3,6,1,4,1,351,110,5,3,1,1,1,1,8),_CesPortSpeed_Type())
cesPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortSpeed.setStatus(_A)
if mibBuilder.loadTexts:cesPortSpeed.setUnits('kbps')
class _CesPortState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('notConfigured',1),('active',2),('remoteLoopback',3),('failedDueToLine',4),('failedDueToSignalling',5),('inactive',6),('inBert',7),('farEndRemoteLoopback',8)))
_CesPortState_Type.__name__=_C
_CesPortState_Object=MibTableColumn
cesPortState=_CesPortState_Object((1,3,6,1,4,1,351,110,5,3,1,1,1,1,9),_CesPortState_Type())
cesPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortState.setStatus(_A)
class _CesPortBERTEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_CesPortBERTEnable_Type.__name__=_C
_CesPortBERTEnable_Object=MibTableColumn
cesPortBERTEnable=_CesPortBERTEnable_Object((1,3,6,1,4,1,351,110,5,3,1,1,1,1,10),_CesPortBERTEnable_Type())
cesPortBERTEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cesPortBERTEnable.setStatus(_A)
class _CesPortNextAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2048))
_CesPortNextAvailable_Type.__name__=_C
_CesPortNextAvailable_Object=MibScalar
cesPortNextAvailable=_CesPortNextAvailable_Object((1,3,6,1,4,1,351,110,5,3,1,1,2),_CesPortNextAvailable_Type())
cesPortNextAvailable.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortNextAvailable.setStatus(_A)
class _CesPortsUsedLine1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CesPortsUsedLine1_Type.__name__=_C
_CesPortsUsedLine1_Object=MibScalar
cesPortsUsedLine1=_CesPortsUsedLine1_Object((1,3,6,1,4,1,351,110,5,3,1,1,3),_CesPortsUsedLine1_Type())
cesPortsUsedLine1.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortsUsedLine1.setStatus(_A)
class _CesPortsUsedLine2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CesPortsUsedLine2_Type.__name__=_C
_CesPortsUsedLine2_Object=MibScalar
cesPortsUsedLine2=_CesPortsUsedLine2_Object((1,3,6,1,4,1,351,110,5,3,1,1,4),_CesPortsUsedLine2_Type())
cesPortsUsedLine2.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortsUsedLine2.setStatus(_A)
class _CesPortsUsedLine3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CesPortsUsedLine3_Type.__name__=_C
_CesPortsUsedLine3_Object=MibScalar
cesPortsUsedLine3=_CesPortsUsedLine3_Object((1,3,6,1,4,1,351,110,5,3,1,1,5),_CesPortsUsedLine3_Type())
cesPortsUsedLine3.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortsUsedLine3.setStatus(_A)
class _CesPortsUsedLine4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CesPortsUsedLine4_Type.__name__=_C
_CesPortsUsedLine4_Object=MibScalar
cesPortsUsedLine4=_CesPortsUsedLine4_Object((1,3,6,1,4,1,351,110,5,3,1,1,6),_CesPortsUsedLine4_Type())
cesPortsUsedLine4.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortsUsedLine4.setStatus(_A)
class _CesPortsUsedLine5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CesPortsUsedLine5_Type.__name__=_C
_CesPortsUsedLine5_Object=MibScalar
cesPortsUsedLine5=_CesPortsUsedLine5_Object((1,3,6,1,4,1,351,110,5,3,1,1,7),_CesPortsUsedLine5_Type())
cesPortsUsedLine5.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortsUsedLine5.setStatus(_A)
class _CesPortsUsedLine6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CesPortsUsedLine6_Type.__name__=_C
_CesPortsUsedLine6_Object=MibScalar
cesPortsUsedLine6=_CesPortsUsedLine6_Object((1,3,6,1,4,1,351,110,5,3,1,1,8),_CesPortsUsedLine6_Type())
cesPortsUsedLine6.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortsUsedLine6.setStatus(_A)
class _CesPortsUsedLine7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CesPortsUsedLine7_Type.__name__=_C
_CesPortsUsedLine7_Object=MibScalar
cesPortsUsedLine7=_CesPortsUsedLine7_Object((1,3,6,1,4,1,351,110,5,3,1,1,9),_CesPortsUsedLine7_Type())
cesPortsUsedLine7.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortsUsedLine7.setStatus(_A)
class _CesPortsUsedLine8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CesPortsUsedLine8_Type.__name__=_C
_CesPortsUsedLine8_Object=MibScalar
cesPortsUsedLine8=_CesPortsUsedLine8_Object((1,3,6,1,4,1,351,110,5,3,1,1,10),_CesPortsUsedLine8_Type())
cesPortsUsedLine8.setMaxAccess(_D)
if mibBuilder.loadTexts:cesPortsUsedLine8.setStatus(_A)
_CiscoWanCesPortMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanCesPortMIBConformance=_CiscoWanCesPortMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,40,2))
_CiscoWanCesPortMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanCesPortMIBGroups=_CiscoWanCesPortMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,40,2,1))
_CiscoWanCesPortMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanCesPortMIBCompliances=_CiscoWanCesPortMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,40,2,2))
ciscoWanCesPortsUsedGroup=ObjectGroup((1,3,6,1,4,1,351,150,40,2,1,1))
ciscoWanCesPortsUsedGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:ciscoWanCesPortsUsedGroup.setStatus(_A)
ciscoWanCesPortConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,40,2,1,2))
ciscoWanCesPortConfGroup.setObjects(*((_B,_F),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ciscoWanCesPortConfGroup.setStatus(_A)
ciscoWanCesPortDs0InDs1Group=ObjectGroup((1,3,6,1,4,1,351,150,40,2,1,3))
ciscoWanCesPortDs0InDs1Group.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoWanCesPortDs0InDs1Group.setStatus(_A)
ciscoWanCesPortCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,40,2,2,1))
ciscoWanCesPortCompliance.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ciscoWanCesPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cesmPort':cesmPort,'cesmPortCnfGrp':cesmPortCnfGrp,'cesmPortCnfGrpTable':cesmPortCnfGrpTable,'cesmPortCnfGrpEntry':cesmPortCnfGrpEntry,_F:cesPortNum,_H:cesPortRowStatus,_I:cesPortLineNum,_J:cesPortType,_K:cesPortDs0ConfigBitMap,_L:cesPortNumOfDs0Slot,_M:cesPortNumOfSCIPerDS0,_N:cesPortSpeed,_O:cesPortState,_P:cesPortBERTEnable,_G:cesPortNextAvailable,_Q:cesPortsUsedLine1,_R:cesPortsUsedLine2,_S:cesPortsUsedLine3,_T:cesPortsUsedLine4,_U:cesPortsUsedLine5,_V:cesPortsUsedLine6,_W:cesPortsUsedLine7,_X:cesPortsUsedLine8,'ciscoWanCesPortMIB':ciscoWanCesPortMIB,'ciscoWanCesPortMIBConformance':ciscoWanCesPortMIBConformance,'ciscoWanCesPortMIBGroups':ciscoWanCesPortMIBGroups,_a:ciscoWanCesPortsUsedGroup,_Y:ciscoWanCesPortConfGroup,_Z:ciscoWanCesPortDs0InDs1Group,'ciscoWanCesPortMIBCompliances':ciscoWanCesPortMIBCompliances,'ciscoWanCesPortCompliance':ciscoWanCesPortCompliance})