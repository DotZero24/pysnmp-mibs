_O='qtechTrapFormatMIBGroup'
_N='qtechTrapFormatTrapSlotInfo'
_M='qtechTrapFormatTrapTime'
_L='qtechTrapFormatTrapContent'
_K='qtechTrapFormatTrapTitle'
_J='qtechTrapFormatTrapStatus'
_I='qtechTrapFormatTrapReasons'
_H='qtechTrapFormatTrapReasonNo'
_G='qtechTrapFormatTrapType'
_F='qtechTrapFormatTrapLevel'
_E='qtechTrapFormatTrapSerialNo'
_D='DisplayString'
_C='read-only'
_B='QTECH-TRAP-FORMAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
qtechTrapFormatMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,97))
if mibBuilder.loadTexts:qtechTrapFormatMIB.setRevisions(('2011-05-11 00:00',))
_QtechTrapFormatMIBObjects_ObjectIdentity=ObjectIdentity
qtechTrapFormatMIBObjects=_QtechTrapFormatMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,97,1))
class _QtechTrapFormatTrapSerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechTrapFormatTrapSerialNo_Type.__name__=_D
_QtechTrapFormatTrapSerialNo_Object=MibScalar
qtechTrapFormatTrapSerialNo=_QtechTrapFormatTrapSerialNo_Object((1,3,6,1,4,1,27514,1,1,10,2,97,1,1),_QtechTrapFormatTrapSerialNo_Type())
qtechTrapFormatTrapSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapFormatTrapSerialNo.setStatus(_A)
class _QtechTrapFormatTrapLevel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechTrapFormatTrapLevel_Type.__name__=_D
_QtechTrapFormatTrapLevel_Object=MibScalar
qtechTrapFormatTrapLevel=_QtechTrapFormatTrapLevel_Object((1,3,6,1,4,1,27514,1,1,10,2,97,1,2),_QtechTrapFormatTrapLevel_Type())
qtechTrapFormatTrapLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapFormatTrapLevel.setStatus(_A)
class _QtechTrapFormatTrapType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechTrapFormatTrapType_Type.__name__=_D
_QtechTrapFormatTrapType_Object=MibScalar
qtechTrapFormatTrapType=_QtechTrapFormatTrapType_Object((1,3,6,1,4,1,27514,1,1,10,2,97,1,3),_QtechTrapFormatTrapType_Type())
qtechTrapFormatTrapType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapFormatTrapType.setStatus(_A)
_QtechTrapFormatTrapReasonNo_Type=Integer32
_QtechTrapFormatTrapReasonNo_Object=MibScalar
qtechTrapFormatTrapReasonNo=_QtechTrapFormatTrapReasonNo_Object((1,3,6,1,4,1,27514,1,1,10,2,97,1,4),_QtechTrapFormatTrapReasonNo_Type())
qtechTrapFormatTrapReasonNo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapFormatTrapReasonNo.setStatus(_A)
class _QtechTrapFormatTrapReasons_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechTrapFormatTrapReasons_Type.__name__=_D
_QtechTrapFormatTrapReasons_Object=MibScalar
qtechTrapFormatTrapReasons=_QtechTrapFormatTrapReasons_Object((1,3,6,1,4,1,27514,1,1,10,2,97,1,5),_QtechTrapFormatTrapReasons_Type())
qtechTrapFormatTrapReasons.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapFormatTrapReasons.setStatus(_A)
_QtechTrapFormatTrapStatus_Type=Integer32
_QtechTrapFormatTrapStatus_Object=MibScalar
qtechTrapFormatTrapStatus=_QtechTrapFormatTrapStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,97,1,6),_QtechTrapFormatTrapStatus_Type())
qtechTrapFormatTrapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapFormatTrapStatus.setStatus(_A)
class _QtechTrapFormatTrapTitle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechTrapFormatTrapTitle_Type.__name__=_D
_QtechTrapFormatTrapTitle_Object=MibScalar
qtechTrapFormatTrapTitle=_QtechTrapFormatTrapTitle_Object((1,3,6,1,4,1,27514,1,1,10,2,97,1,7),_QtechTrapFormatTrapTitle_Type())
qtechTrapFormatTrapTitle.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapFormatTrapTitle.setStatus(_A)
class _QtechTrapFormatTrapContent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechTrapFormatTrapContent_Type.__name__=_D
_QtechTrapFormatTrapContent_Object=MibScalar
qtechTrapFormatTrapContent=_QtechTrapFormatTrapContent_Object((1,3,6,1,4,1,27514,1,1,10,2,97,1,8),_QtechTrapFormatTrapContent_Type())
qtechTrapFormatTrapContent.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapFormatTrapContent.setStatus(_A)
_QtechTrapFormatTrapTime_Type=Counter32
_QtechTrapFormatTrapTime_Object=MibScalar
qtechTrapFormatTrapTime=_QtechTrapFormatTrapTime_Object((1,3,6,1,4,1,27514,1,1,10,2,97,1,9),_QtechTrapFormatTrapTime_Type())
qtechTrapFormatTrapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapFormatTrapTime.setStatus(_A)
_QtechTrapFormatTrapSlotInfo_Type=DisplayString
_QtechTrapFormatTrapSlotInfo_Object=MibScalar
qtechTrapFormatTrapSlotInfo=_QtechTrapFormatTrapSlotInfo_Object((1,3,6,1,4,1,27514,1,1,10,2,97,1,10),_QtechTrapFormatTrapSlotInfo_Type())
qtechTrapFormatTrapSlotInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrapFormatTrapSlotInfo.setStatus(_A)
_QtechTrapFormatMIBConformance_ObjectIdentity=ObjectIdentity
qtechTrapFormatMIBConformance=_QtechTrapFormatMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,97,2))
_QtechTrapFormatMIBCompliances_ObjectIdentity=ObjectIdentity
qtechTrapFormatMIBCompliances=_QtechTrapFormatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,97,2,1))
_QtechTrapFormatMIBGroups_ObjectIdentity=ObjectIdentity
qtechTrapFormatMIBGroups=_QtechTrapFormatMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,97,2,2))
qtechTrapFormatMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,97,2,2,1))
qtechTrapFormatMIBGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:qtechTrapFormatMIBGroup.setStatus(_A)
qtechTrapFormatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,97,2,1,1))
qtechTrapFormatMIBCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:qtechTrapFormatMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechTrapFormatMIB':qtechTrapFormatMIB,'qtechTrapFormatMIBObjects':qtechTrapFormatMIBObjects,_E:qtechTrapFormatTrapSerialNo,_F:qtechTrapFormatTrapLevel,_G:qtechTrapFormatTrapType,_H:qtechTrapFormatTrapReasonNo,_I:qtechTrapFormatTrapReasons,_J:qtechTrapFormatTrapStatus,_K:qtechTrapFormatTrapTitle,_L:qtechTrapFormatTrapContent,_M:qtechTrapFormatTrapTime,_N:qtechTrapFormatTrapSlotInfo,'qtechTrapFormatMIBConformance':qtechTrapFormatMIBConformance,'qtechTrapFormatMIBCompliances':qtechTrapFormatMIBCompliances,'qtechTrapFormatMIBCompliance':qtechTrapFormatMIBCompliance,'qtechTrapFormatMIBGroups':qtechTrapFormatMIBGroups,_O:qtechTrapFormatMIBGroup})