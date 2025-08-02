_R='ceDisplayBeaconGroup'
_Q='ceDisplayBeaconEnabled'
_P='ceDisplayText'
_O='ceDisplayColor'
_N='ceDisplayState'
_M='ceDisplayName'
_L='ceDisplayType'
_K='unknown'
_J='Unsigned32'
_I='ceDisplayAlphaNumericGroup'
_H='ceDisplayLEDGroup'
_G='ceDisplayGroup'
_F='ceDisplayIndex'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='CISCO-ENTITY-DISPLAY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoEntityDisplayMIB=ModuleIdentity((1,3,6,1,4,1,9,9,344))
if mibBuilder.loadTexts:ciscoEntityDisplayMIB.setRevisions(('2009-10-05 00:00','2003-03-20 00:00'))
class CDisplayType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('led',1),('alphanumeric',2)))
class CDisplayColor(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),('white',2),('red',3),('green',4),('yellow',5),('amber',6),('blue',7),('greenAndAmber',8)))
class CDisplayState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('off',2),('on',3),('blinking',4)))
_CiscoEntityDisplayMIBObjects_ObjectIdentity=ObjectIdentity
ciscoEntityDisplayMIBObjects=_CiscoEntityDisplayMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,344,1))
_CeDisplayTable_Object=MibTable
ceDisplayTable=_CeDisplayTable_Object((1,3,6,1,4,1,9,9,344,1,1))
if mibBuilder.loadTexts:ceDisplayTable.setStatus(_A)
_CeDisplayEntry_Object=MibTableRow
ceDisplayEntry=_CeDisplayEntry_Object((1,3,6,1,4,1,9,9,344,1,1,1))
ceDisplayEntry.setIndexNames((0,_D,_E),(0,_B,_F))
if mibBuilder.loadTexts:ceDisplayEntry.setStatus(_A)
class _CeDisplayIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CeDisplayIndex_Type.__name__=_J
_CeDisplayIndex_Object=MibTableColumn
ceDisplayIndex=_CeDisplayIndex_Object((1,3,6,1,4,1,9,9,344,1,1,1,1),_CeDisplayIndex_Type())
ceDisplayIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ceDisplayIndex.setStatus(_A)
_CeDisplayType_Type=CDisplayType
_CeDisplayType_Object=MibTableColumn
ceDisplayType=_CeDisplayType_Object((1,3,6,1,4,1,9,9,344,1,1,1,2),_CeDisplayType_Type())
ceDisplayType.setMaxAccess(_C)
if mibBuilder.loadTexts:ceDisplayType.setStatus(_A)
_CeDisplayName_Type=SnmpAdminString
_CeDisplayName_Object=MibTableColumn
ceDisplayName=_CeDisplayName_Object((1,3,6,1,4,1,9,9,344,1,1,1,3),_CeDisplayName_Type())
ceDisplayName.setMaxAccess(_C)
if mibBuilder.loadTexts:ceDisplayName.setStatus(_A)
_CeDisplayState_Type=CDisplayState
_CeDisplayState_Object=MibTableColumn
ceDisplayState=_CeDisplayState_Object((1,3,6,1,4,1,9,9,344,1,1,1,4),_CeDisplayState_Type())
ceDisplayState.setMaxAccess(_C)
if mibBuilder.loadTexts:ceDisplayState.setStatus(_A)
_CeDisplayColor_Type=CDisplayColor
_CeDisplayColor_Object=MibTableColumn
ceDisplayColor=_CeDisplayColor_Object((1,3,6,1,4,1,9,9,344,1,1,1,5),_CeDisplayColor_Type())
ceDisplayColor.setMaxAccess(_C)
if mibBuilder.loadTexts:ceDisplayColor.setStatus(_A)
_CeDisplayText_Type=SnmpAdminString
_CeDisplayText_Object=MibTableColumn
ceDisplayText=_CeDisplayText_Object((1,3,6,1,4,1,9,9,344,1,1,1,6),_CeDisplayText_Type())
ceDisplayText.setMaxAccess(_C)
if mibBuilder.loadTexts:ceDisplayText.setStatus(_A)
_CeDisplayBeaconTable_Object=MibTable
ceDisplayBeaconTable=_CeDisplayBeaconTable_Object((1,3,6,1,4,1,9,9,344,1,2))
if mibBuilder.loadTexts:ceDisplayBeaconTable.setStatus(_A)
_CeDisplayBeaconEntry_Object=MibTableRow
ceDisplayBeaconEntry=_CeDisplayBeaconEntry_Object((1,3,6,1,4,1,9,9,344,1,2,1))
ceDisplayBeaconEntry.setIndexNames((0,_D,_E),(0,_B,_F))
if mibBuilder.loadTexts:ceDisplayBeaconEntry.setStatus(_A)
_CeDisplayBeaconEnabled_Type=TruthValue
_CeDisplayBeaconEnabled_Object=MibTableColumn
ceDisplayBeaconEnabled=_CeDisplayBeaconEnabled_Object((1,3,6,1,4,1,9,9,344,1,2,1,1),_CeDisplayBeaconEnabled_Type())
ceDisplayBeaconEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:ceDisplayBeaconEnabled.setStatus(_A)
_CeDisplayMIBConformance_ObjectIdentity=ObjectIdentity
ceDisplayMIBConformance=_CeDisplayMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,344,2))
_CeDisplayMIBCompliances_ObjectIdentity=ObjectIdentity
ceDisplayMIBCompliances=_CeDisplayMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,344,2,1))
_CeDisplayMIBGroups_ObjectIdentity=ObjectIdentity
ceDisplayMIBGroups=_CeDisplayMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,344,2,2))
ceDisplayGroup=ObjectGroup((1,3,6,1,4,1,9,9,344,2,2,1))
ceDisplayGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ceDisplayGroup.setStatus(_A)
ceDisplayLEDGroup=ObjectGroup((1,3,6,1,4,1,9,9,344,2,2,2))
ceDisplayLEDGroup.setObjects((_B,_O))
if mibBuilder.loadTexts:ceDisplayLEDGroup.setStatus(_A)
ceDisplayAlphaNumericGroup=ObjectGroup((1,3,6,1,4,1,9,9,344,2,2,3))
ceDisplayAlphaNumericGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:ceDisplayAlphaNumericGroup.setStatus(_A)
ceDisplayBeaconGroup=ObjectGroup((1,3,6,1,4,1,9,9,344,2,2,4))
ceDisplayBeaconGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:ceDisplayBeaconGroup.setStatus(_A)
ceDisplayMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,344,2,1,1))
ceDisplayMIBCompliance.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:ceDisplayMIBCompliance.setStatus('deprecated')
ceDisplayMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,344,2,1,2))
ceDisplayMIBCompliance2.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_R)))
if mibBuilder.loadTexts:ceDisplayMIBCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CDisplayType':CDisplayType,'CDisplayColor':CDisplayColor,'CDisplayState':CDisplayState,'ciscoEntityDisplayMIB':ciscoEntityDisplayMIB,'ciscoEntityDisplayMIBObjects':ciscoEntityDisplayMIBObjects,'ceDisplayTable':ceDisplayTable,'ceDisplayEntry':ceDisplayEntry,_F:ceDisplayIndex,_L:ceDisplayType,_M:ceDisplayName,_N:ceDisplayState,_O:ceDisplayColor,_P:ceDisplayText,'ceDisplayBeaconTable':ceDisplayBeaconTable,'ceDisplayBeaconEntry':ceDisplayBeaconEntry,_Q:ceDisplayBeaconEnabled,'ceDisplayMIBConformance':ceDisplayMIBConformance,'ceDisplayMIBCompliances':ceDisplayMIBCompliances,'ceDisplayMIBCompliance':ceDisplayMIBCompliance,'ceDisplayMIBCompliance2':ceDisplayMIBCompliance2,'ceDisplayMIBGroups':ceDisplayMIBGroups,_G:ceDisplayGroup,_H:ceDisplayLEDGroup,_I:ceDisplayAlphaNumericGroup,_R:ceDisplayBeaconGroup})