_J='lineSelectionCustomizationVer1'
_I='lineSelectionDigitMap'
_H='lineSelectionEnable'
_G='read-write'
_F='MxEnableState'
_E='MxDigitMap'
_D='ifIndex'
_C='IF-MIB'
_B='MX-LINE-SELECTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxDigitMap,MxEnableState=mibBuilder.importSymbols('MX-TC',_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lineSelectionMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,90))
if mibBuilder.loadTexts:lineSelectionMIB.setRevisions(('1903-03-19 00:00',))
_LineSelectionMIBObjects_ObjectIdentity=ObjectIdentity
lineSelectionMIBObjects=_LineSelectionMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,90,1))
_LineSelectionIfCustomizationTable_Object=MibTable
lineSelectionIfCustomizationTable=_LineSelectionIfCustomizationTable_Object((1,3,6,1,4,1,4935,15,90,1,10))
if mibBuilder.loadTexts:lineSelectionIfCustomizationTable.setStatus(_A)
_LineSelectionIfCustomizationEntry_Object=MibTableRow
lineSelectionIfCustomizationEntry=_LineSelectionIfCustomizationEntry_Object((1,3,6,1,4,1,4935,15,90,1,10,5))
lineSelectionIfCustomizationEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:lineSelectionIfCustomizationEntry.setStatus(_A)
class _LineSelectionEnable_Type(MxEnableState):defaultValue=0
_LineSelectionEnable_Type.__name__=_F
_LineSelectionEnable_Object=MibTableColumn
lineSelectionEnable=_LineSelectionEnable_Object((1,3,6,1,4,1,4935,15,90,1,10,5,5),_LineSelectionEnable_Type())
lineSelectionEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:lineSelectionEnable.setStatus(_A)
class _LineSelectionDigitMap_Type(MxDigitMap):defaultValue=OctetString('')
_LineSelectionDigitMap_Type.__name__=_E
_LineSelectionDigitMap_Object=MibTableColumn
lineSelectionDigitMap=_LineSelectionDigitMap_Object((1,3,6,1,4,1,4935,15,90,1,10,5,10),_LineSelectionDigitMap_Type())
lineSelectionDigitMap.setMaxAccess(_G)
if mibBuilder.loadTexts:lineSelectionDigitMap.setStatus(_A)
_LineSelectionConformance_ObjectIdentity=ObjectIdentity
lineSelectionConformance=_LineSelectionConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,90,5))
_LineSelectionCompliances_ObjectIdentity=ObjectIdentity
lineSelectionCompliances=_LineSelectionCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,90,5,1))
_LineSelectionGroups_ObjectIdentity=ObjectIdentity
lineSelectionGroups=_LineSelectionGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,90,5,5))
lineSelectionCustomizationVer1=ObjectGroup((1,3,6,1,4,1,4935,15,90,5,5,10))
lineSelectionCustomizationVer1.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:lineSelectionCustomizationVer1.setStatus(_A)
lineSelectionComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,90,5,1,1))
lineSelectionComplVer1.setObjects((_B,_J))
if mibBuilder.loadTexts:lineSelectionComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lineSelectionMIB':lineSelectionMIB,'lineSelectionMIBObjects':lineSelectionMIBObjects,'lineSelectionIfCustomizationTable':lineSelectionIfCustomizationTable,'lineSelectionIfCustomizationEntry':lineSelectionIfCustomizationEntry,_H:lineSelectionEnable,_I:lineSelectionDigitMap,'lineSelectionConformance':lineSelectionConformance,'lineSelectionCompliances':lineSelectionCompliances,'lineSelectionComplVer1':lineSelectionComplVer1,'lineSelectionGroups':lineSelectionGroups,_J:lineSelectionCustomizationVer1})