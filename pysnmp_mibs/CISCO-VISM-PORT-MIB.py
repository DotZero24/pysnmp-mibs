_M='ciscoVismPortGroup'
_L='vismPortState'
_K='vismPortSpeed'
_J='vismPortDs0ConfigBitMap'
_I='vismPortType'
_H='vismPortLineNum'
_G='vismPortRowStatus'
_F='read-only'
_E='vismPortNum'
_D='read-create'
_C='Integer32'
_B='CISCO-VISM-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
vismPort,=mibBuilder.importSymbols('BASIS-MIB','vismPort')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoVismPortMIB=ModuleIdentity((1,3,6,1,4,1,351,150,92))
if mibBuilder.loadTexts:ciscoVismPortMIB.setRevisions(('2003-10-16 00:00',))
_VismPortCnfGrp_ObjectIdentity=ObjectIdentity
vismPortCnfGrp=_VismPortCnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,2,1))
_VismPortCnfGrpTable_Object=MibTable
vismPortCnfGrpTable=_VismPortCnfGrpTable_Object((1,3,6,1,4,1,351,110,5,5,2,1,1))
if mibBuilder.loadTexts:vismPortCnfGrpTable.setStatus(_A)
_VismPortCnfGrpEntry_Object=MibTableRow
vismPortCnfGrpEntry=_VismPortCnfGrpEntry_Object((1,3,6,1,4,1,351,110,5,5,2,1,1,1))
vismPortCnfGrpEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:vismPortCnfGrpEntry.setStatus(_A)
class _VismPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismPortNum_Type.__name__=_C
_VismPortNum_Object=MibTableColumn
vismPortNum=_VismPortNum_Object((1,3,6,1,4,1,351,110,5,5,2,1,1,1,1),_VismPortNum_Type())
vismPortNum.setMaxAccess(_F)
if mibBuilder.loadTexts:vismPortNum.setStatus(_A)
class _VismPortRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_VismPortRowStatus_Type.__name__=_C
_VismPortRowStatus_Object=MibTableColumn
vismPortRowStatus=_VismPortRowStatus_Object((1,3,6,1,4,1,351,110,5,5,2,1,1,1,2),_VismPortRowStatus_Type())
vismPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vismPortRowStatus.setStatus(_A)
class _VismPortLineNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_VismPortLineNum_Type.__name__=_C
_VismPortLineNum_Object=MibTableColumn
vismPortLineNum=_VismPortLineNum_Object((1,3,6,1,4,1,351,110,5,5,2,1,1,1,3),_VismPortLineNum_Type())
vismPortLineNum.setMaxAccess(_D)
if mibBuilder.loadTexts:vismPortLineNum.setStatus(_A)
class _VismPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('voIP',1),('userPort',2)))
_VismPortType_Type.__name__=_C
_VismPortType_Object=MibTableColumn
vismPortType=_VismPortType_Object((1,3,6,1,4,1,351,110,5,5,2,1,1,1,4),_VismPortType_Type())
vismPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:vismPortType.setStatus(_A)
class _VismPortDs0ConfigBitMap_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_VismPortDs0ConfigBitMap_Type.__name__=_C
_VismPortDs0ConfigBitMap_Object=MibTableColumn
vismPortDs0ConfigBitMap=_VismPortDs0ConfigBitMap_Object((1,3,6,1,4,1,351,110,5,5,2,1,1,1,5),_VismPortDs0ConfigBitMap_Type())
vismPortDs0ConfigBitMap.setMaxAccess(_D)
if mibBuilder.loadTexts:vismPortDs0ConfigBitMap.setStatus(_A)
class _VismPortSpeed_Type(Integer32):defaultValue=5651320;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5651320))
_VismPortSpeed_Type.__name__=_C
_VismPortSpeed_Object=MibTableColumn
vismPortSpeed=_VismPortSpeed_Object((1,3,6,1,4,1,351,110,5,5,2,1,1,1,6),_VismPortSpeed_Type())
vismPortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:vismPortSpeed.setStatus(_A)
class _VismPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notConfigured',1),('active',2)))
_VismPortState_Type.__name__=_C
_VismPortState_Object=MibTableColumn
vismPortState=_VismPortState_Object((1,3,6,1,4,1,351,110,5,5,2,1,1,1,7),_VismPortState_Type())
vismPortState.setMaxAccess(_F)
if mibBuilder.loadTexts:vismPortState.setStatus(_A)
_CiscoVismPortMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVismPortMIBConformance=_CiscoVismPortMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,92,2))
_CiscoVismPortMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVismPortMIBGroups=_CiscoVismPortMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,92,2,1))
_CiscoVismPortMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVismPortMIBCompliances=_CiscoVismPortMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,92,2,2))
ciscoVismPortGroup=ObjectGroup((1,3,6,1,4,1,351,150,92,2,1,1))
ciscoVismPortGroup.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ciscoVismPortGroup.setStatus(_A)
ciscoVismPortCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,92,2,2,1))
ciscoVismPortCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:ciscoVismPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vismPortCnfGrp':vismPortCnfGrp,'vismPortCnfGrpTable':vismPortCnfGrpTable,'vismPortCnfGrpEntry':vismPortCnfGrpEntry,_E:vismPortNum,_G:vismPortRowStatus,_H:vismPortLineNum,_I:vismPortType,_J:vismPortDs0ConfigBitMap,_K:vismPortSpeed,_L:vismPortState,'ciscoVismPortMIB':ciscoVismPortMIB,'ciscoVismPortMIBConformance':ciscoVismPortMIBConformance,'ciscoVismPortMIBGroups':ciscoVismPortMIBGroups,_M:ciscoVismPortGroup,'ciscoVismPortMIBCompliances':ciscoVismPortMIBCompliances,'ciscoVismPortCompliance':ciscoVismPortCompliance})