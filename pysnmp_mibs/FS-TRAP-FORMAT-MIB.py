_R='fsTrapFormatMIBGroup'
_Q='fsTrapFormatTrapDateTime'
_P='fsTrapFormatTrapSerialNum'
_O='fsTrapFormatTrapVendorId'
_N='fsTrapFormatTrapSlotInfo'
_M='fsTrapFormatTrapTime'
_L='fsTrapFormatTrapContent'
_K='fsTrapFormatTrapTitle'
_J='fsTrapFormatTrapStatus'
_I='fsTrapFormatTrapReasons'
_H='fsTrapFormatTrapReasonNo'
_G='fsTrapFormatTrapType'
_F='fsTrapFormatTrapLevel'
_E='fsTrapFormatTrapSerialNo'
_D='DisplayString'
_C='read-only'
_B='FS-TRAP-FORMAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
fsTrapFormatMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,97))
if mibBuilder.loadTexts:fsTrapFormatMIB.setRevisions(('2011-05-11 00:00',))
_FsTrapFormatMIBObjects_ObjectIdentity=ObjectIdentity
fsTrapFormatMIBObjects=_FsTrapFormatMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,97,1))
class _FsTrapFormatTrapSerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsTrapFormatTrapSerialNo_Type.__name__=_D
_FsTrapFormatTrapSerialNo_Object=MibScalar
fsTrapFormatTrapSerialNo=_FsTrapFormatTrapSerialNo_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,1),_FsTrapFormatTrapSerialNo_Type())
fsTrapFormatTrapSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapSerialNo.setStatus(_A)
class _FsTrapFormatTrapLevel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsTrapFormatTrapLevel_Type.__name__=_D
_FsTrapFormatTrapLevel_Object=MibScalar
fsTrapFormatTrapLevel=_FsTrapFormatTrapLevel_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,2),_FsTrapFormatTrapLevel_Type())
fsTrapFormatTrapLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapLevel.setStatus(_A)
class _FsTrapFormatTrapType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsTrapFormatTrapType_Type.__name__=_D
_FsTrapFormatTrapType_Object=MibScalar
fsTrapFormatTrapType=_FsTrapFormatTrapType_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,3),_FsTrapFormatTrapType_Type())
fsTrapFormatTrapType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapType.setStatus(_A)
_FsTrapFormatTrapReasonNo_Type=Integer32
_FsTrapFormatTrapReasonNo_Object=MibScalar
fsTrapFormatTrapReasonNo=_FsTrapFormatTrapReasonNo_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,4),_FsTrapFormatTrapReasonNo_Type())
fsTrapFormatTrapReasonNo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapReasonNo.setStatus(_A)
class _FsTrapFormatTrapReasons_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsTrapFormatTrapReasons_Type.__name__=_D
_FsTrapFormatTrapReasons_Object=MibScalar
fsTrapFormatTrapReasons=_FsTrapFormatTrapReasons_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,5),_FsTrapFormatTrapReasons_Type())
fsTrapFormatTrapReasons.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapReasons.setStatus(_A)
_FsTrapFormatTrapStatus_Type=Integer32
_FsTrapFormatTrapStatus_Object=MibScalar
fsTrapFormatTrapStatus=_FsTrapFormatTrapStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,6),_FsTrapFormatTrapStatus_Type())
fsTrapFormatTrapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapStatus.setStatus(_A)
class _FsTrapFormatTrapTitle_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsTrapFormatTrapTitle_Type.__name__=_D
_FsTrapFormatTrapTitle_Object=MibScalar
fsTrapFormatTrapTitle=_FsTrapFormatTrapTitle_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,7),_FsTrapFormatTrapTitle_Type())
fsTrapFormatTrapTitle.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapTitle.setStatus(_A)
class _FsTrapFormatTrapContent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsTrapFormatTrapContent_Type.__name__=_D
_FsTrapFormatTrapContent_Object=MibScalar
fsTrapFormatTrapContent=_FsTrapFormatTrapContent_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,8),_FsTrapFormatTrapContent_Type())
fsTrapFormatTrapContent.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapContent.setStatus(_A)
_FsTrapFormatTrapTime_Type=Counter32
_FsTrapFormatTrapTime_Object=MibScalar
fsTrapFormatTrapTime=_FsTrapFormatTrapTime_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,9),_FsTrapFormatTrapTime_Type())
fsTrapFormatTrapTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapTime.setStatus(_A)
_FsTrapFormatTrapSlotInfo_Type=DisplayString
_FsTrapFormatTrapSlotInfo_Object=MibScalar
fsTrapFormatTrapSlotInfo=_FsTrapFormatTrapSlotInfo_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,10),_FsTrapFormatTrapSlotInfo_Type())
fsTrapFormatTrapSlotInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapSlotInfo.setStatus(_A)
_FsTrapFormatTrapVendorId_Type=Integer32
_FsTrapFormatTrapVendorId_Object=MibScalar
fsTrapFormatTrapVendorId=_FsTrapFormatTrapVendorId_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,11),_FsTrapFormatTrapVendorId_Type())
fsTrapFormatTrapVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapVendorId.setStatus(_A)
class _FsTrapFormatTrapSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsTrapFormatTrapSerialNum_Type.__name__=_D
_FsTrapFormatTrapSerialNum_Object=MibScalar
fsTrapFormatTrapSerialNum=_FsTrapFormatTrapSerialNum_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,12),_FsTrapFormatTrapSerialNum_Type())
fsTrapFormatTrapSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapSerialNum.setStatus(_A)
class _FsTrapFormatTrapDateTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsTrapFormatTrapDateTime_Type.__name__=_D
_FsTrapFormatTrapDateTime_Object=MibScalar
fsTrapFormatTrapDateTime=_FsTrapFormatTrapDateTime_Object((1,3,6,1,4,1,52642,1,1,10,2,97,1,13),_FsTrapFormatTrapDateTime_Type())
fsTrapFormatTrapDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrapFormatTrapDateTime.setStatus(_A)
_FsTrapFormatMIBConformance_ObjectIdentity=ObjectIdentity
fsTrapFormatMIBConformance=_FsTrapFormatMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,97,2))
_FsTrapFormatMIBCompliances_ObjectIdentity=ObjectIdentity
fsTrapFormatMIBCompliances=_FsTrapFormatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,97,2,1))
_FsTrapFormatMIBGroups_ObjectIdentity=ObjectIdentity
fsTrapFormatMIBGroups=_FsTrapFormatMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,97,2,2))
fsTrapFormatMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,97,2,2,1))
fsTrapFormatMIBGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:fsTrapFormatMIBGroup.setStatus(_A)
fsTrapFormatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,97,2,1,1))
fsTrapFormatMIBCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:fsTrapFormatMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsTrapFormatMIB':fsTrapFormatMIB,'fsTrapFormatMIBObjects':fsTrapFormatMIBObjects,_E:fsTrapFormatTrapSerialNo,_F:fsTrapFormatTrapLevel,_G:fsTrapFormatTrapType,_H:fsTrapFormatTrapReasonNo,_I:fsTrapFormatTrapReasons,_J:fsTrapFormatTrapStatus,_K:fsTrapFormatTrapTitle,_L:fsTrapFormatTrapContent,_M:fsTrapFormatTrapTime,_N:fsTrapFormatTrapSlotInfo,_O:fsTrapFormatTrapVendorId,_P:fsTrapFormatTrapSerialNum,_Q:fsTrapFormatTrapDateTime,'fsTrapFormatMIBConformance':fsTrapFormatMIBConformance,'fsTrapFormatMIBCompliances':fsTrapFormatMIBCompliances,'fsTrapFormatMIBCompliance':fsTrapFormatMIBCompliance,'fsTrapFormatMIBGroups':fsTrapFormatMIBGroups,_R:fsTrapFormatMIBGroup})