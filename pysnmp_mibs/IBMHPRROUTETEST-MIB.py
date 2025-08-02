_L='ibmHprRtDetSubTestId'
_K='ibmHprRtDetTestId'
_J='noResponse'
_I='successful'
_H='ibmHprRtGenTestId'
_G='read-write'
_F='IBMHPRROUTETEST-MIB'
_E='OctetString'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmArchitecture_ObjectIdentity=ObjectIdentity
ibmArchitecture=_IbmArchitecture_ObjectIdentity((1,3,6,1,4,1,2,5))
_Hpr_ObjectIdentity=ObjectIdentity
hpr=_Hpr_ObjectIdentity((1,3,6,1,4,1,2,5,10))
_IbmHprRouteTest_ObjectIdentity=ObjectIdentity
ibmHprRouteTest=_IbmHprRouteTest_ObjectIdentity((1,3,6,1,4,1,2,5,10,4))
_IbmHprRtGlobe_ObjectIdentity=ObjectIdentity
ibmHprRtGlobe=_IbmHprRtGlobe_ObjectIdentity((1,3,6,1,4,1,2,5,10,4,1))
class _IbmHprRtGlobeConnTrigger_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(10,17))
_IbmHprRtGlobeConnTrigger_Type.__name__=_E
_IbmHprRtGlobeConnTrigger_Object=MibScalar
ibmHprRtGlobeConnTrigger=_IbmHprRtGlobeConnTrigger_Object((1,3,6,1,4,1,2,5,10,4,1,1),_IbmHprRtGlobeConnTrigger_Type())
ibmHprRtGlobeConnTrigger.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmHprRtGlobeConnTrigger.setStatus(_A)
class _IbmHprRtGlobeNameTrigger_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(5,26))
_IbmHprRtGlobeNameTrigger_Type.__name__=_D
_IbmHprRtGlobeNameTrigger_Object=MibScalar
ibmHprRtGlobeNameTrigger=_IbmHprRtGlobeNameTrigger_Object((1,3,6,1,4,1,2,5,10,4,1,2),_IbmHprRtGlobeNameTrigger_Type())
ibmHprRtGlobeNameTrigger.setMaxAccess(_G)
if mibBuilder.loadTexts:ibmHprRtGlobeNameTrigger.setStatus(_A)
_IbmHprRtGenResults_ObjectIdentity=ObjectIdentity
ibmHprRtGenResults=_IbmHprRtGenResults_ObjectIdentity((1,3,6,1,4,1,2,5,10,4,2))
_IbmHprRtGenTable_Object=MibTable
ibmHprRtGenTable=_IbmHprRtGenTable_Object((1,3,6,1,4,1,2,5,10,4,2,1))
if mibBuilder.loadTexts:ibmHprRtGenTable.setStatus(_A)
_IbmHprRtGenEntry_Object=MibTableRow
ibmHprRtGenEntry=_IbmHprRtGenEntry_Object((1,3,6,1,4,1,2,5,10,4,2,1,1))
ibmHprRtGenEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:ibmHprRtGenEntry.setStatus(_A)
_IbmHprRtGenTestId_Type=Gauge32
_IbmHprRtGenTestId_Object=MibTableColumn
ibmHprRtGenTestId=_IbmHprRtGenTestId_Object((1,3,6,1,4,1,2,5,10,4,2,1,1,1),_IbmHprRtGenTestId_Type())
ibmHprRtGenTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtGenTestId.setStatus(_A)
class _IbmHprRtGenTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connTrigger',1),('nameTrigger',2)))
_IbmHprRtGenTestType_Type.__name__=_C
_IbmHprRtGenTestType_Object=MibTableColumn
ibmHprRtGenTestType=_IbmHprRtGenTestType_Object((1,3,6,1,4,1,2,5,10,4,2,1,1,2),_IbmHprRtGenTestType_Type())
ibmHprRtGenTestType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtGenTestType.setStatus(_A)
class _IbmHprRtGenConnTrigger_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(10,17))
_IbmHprRtGenConnTrigger_Type.__name__=_E
_IbmHprRtGenConnTrigger_Object=MibTableColumn
ibmHprRtGenConnTrigger=_IbmHprRtGenConnTrigger_Object((1,3,6,1,4,1,2,5,10,4,2,1,1,3),_IbmHprRtGenConnTrigger_Type())
ibmHprRtGenConnTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtGenConnTrigger.setStatus(_A)
class _IbmHprRtGenNameTrigger_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(5,26))
_IbmHprRtGenNameTrigger_Type.__name__=_D
_IbmHprRtGenNameTrigger_Object=MibTableColumn
ibmHprRtGenNameTrigger=_IbmHprRtGenNameTrigger_Object((1,3,6,1,4,1,2,5,10,4,2,1,1,4),_IbmHprRtGenNameTrigger_Type())
ibmHprRtGenNameTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtGenNameTrigger.setStatus(_A)
class _IbmHprRtGenResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,1),('inProgess',2),(_J,3),('nceidInvalid',4),('tcidInvalid',5),('luInvalid',6),('modeInvalid',7),('noHprRoute',8)))
_IbmHprRtGenResult_Type.__name__=_C
_IbmHprRtGenResult_Object=MibTableColumn
ibmHprRtGenResult=_IbmHprRtGenResult_Object((1,3,6,1,4,1,2,5,10,4,2,1,1,5),_IbmHprRtGenResult_Type())
ibmHprRtGenResult.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtGenResult.setStatus(_A)
class _IbmHprRtGenSenseCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_IbmHprRtGenSenseCode_Type.__name__=_E
_IbmHprRtGenSenseCode_Object=MibTableColumn
ibmHprRtGenSenseCode=_IbmHprRtGenSenseCode_Object((1,3,6,1,4,1,2,5,10,4,2,1,1,6),_IbmHprRtGenSenseCode_Type())
ibmHprRtGenSenseCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtGenSenseCode.setStatus(_A)
class _IbmHprRtGenCosName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IbmHprRtGenCosName_Type.__name__=_D
_IbmHprRtGenCosName_Object=MibTableColumn
ibmHprRtGenCosName=_IbmHprRtGenCosName_Object((1,3,6,1,4,1,2,5,10,4,2,1,1,7),_IbmHprRtGenCosName_Type())
ibmHprRtGenCosName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtGenCosName.setStatus(_A)
class _IbmHprRtGenRscv_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_IbmHprRtGenRscv_Type.__name__=_E
_IbmHprRtGenRscv_Object=MibTableColumn
ibmHprRtGenRscv=_IbmHprRtGenRscv_Object((1,3,6,1,4,1,2,5,10,4,2,1,1,8),_IbmHprRtGenRscv_Type())
ibmHprRtGenRscv.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtGenRscv.setStatus(_A)
_IbmHprRtDetResults_ObjectIdentity=ObjectIdentity
ibmHprRtDetResults=_IbmHprRtDetResults_ObjectIdentity((1,3,6,1,4,1,2,5,10,4,3))
_IbmHprRtDetTable_Object=MibTable
ibmHprRtDetTable=_IbmHprRtDetTable_Object((1,3,6,1,4,1,2,5,10,4,3,1))
if mibBuilder.loadTexts:ibmHprRtDetTable.setStatus(_A)
_IbmHprRtDetEntry_Object=MibTableRow
ibmHprRtDetEntry=_IbmHprRtDetEntry_Object((1,3,6,1,4,1,2,5,10,4,3,1,1))
ibmHprRtDetEntry.setIndexNames((0,_F,_K),(0,_F,_L))
if mibBuilder.loadTexts:ibmHprRtDetEntry.setStatus(_A)
_IbmHprRtDetTestId_Type=Gauge32
_IbmHprRtDetTestId_Object=MibTableColumn
ibmHprRtDetTestId=_IbmHprRtDetTestId_Object((1,3,6,1,4,1,2,5,10,4,3,1,1,1),_IbmHprRtDetTestId_Type())
ibmHprRtDetTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtDetTestId.setStatus(_A)
class _IbmHprRtDetSubTestId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IbmHprRtDetSubTestId_Type.__name__=_C
_IbmHprRtDetSubTestId_Object=MibTableColumn
ibmHprRtDetSubTestId=_IbmHprRtDetSubTestId_Object((1,3,6,1,4,1,2,5,10,4,3,1,1,2),_IbmHprRtDetSubTestId_Type())
ibmHprRtDetSubTestId.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtDetSubTestId.setStatus(_A)
class _IbmHprRtDetDestNode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_IbmHprRtDetDestNode_Type.__name__=_D
_IbmHprRtDetDestNode_Object=MibTableColumn
ibmHprRtDetDestNode=_IbmHprRtDetDestNode_Object((1,3,6,1,4,1,2,5,10,4,3,1,1,3),_IbmHprRtDetDestNode_Type())
ibmHprRtDetDestNode.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtDetDestNode.setStatus(_A)
class _IbmHprRtDetPriorNode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,17))
_IbmHprRtDetPriorNode_Type.__name__=_D
_IbmHprRtDetPriorNode_Object=MibTableColumn
ibmHprRtDetPriorNode=_IbmHprRtDetPriorNode_Object((1,3,6,1,4,1,2,5,10,4,3,1,1,4),_IbmHprRtDetPriorNode_Type())
ibmHprRtDetPriorNode.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtDetPriorNode.setStatus(_A)
class _IbmHprRtDetLastTgNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmHprRtDetLastTgNumber_Type.__name__=_C
_IbmHprRtDetLastTgNumber_Object=MibTableColumn
ibmHprRtDetLastTgNumber=_IbmHprRtDetLastTgNumber_Object((1,3,6,1,4,1,2,5,10,4,3,1,1,5),_IbmHprRtDetLastTgNumber_Type())
ibmHprRtDetLastTgNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtDetLastTgNumber.setStatus(_A)
_IbmHprRtDetRtripTime_Type=Gauge32
_IbmHprRtDetRtripTime_Object=MibTableColumn
ibmHprRtDetRtripTime=_IbmHprRtDetRtripTime_Object((1,3,6,1,4,1,2,5,10,4,3,1,1,6),_IbmHprRtDetRtripTime_Type())
ibmHprRtDetRtripTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtDetRtripTime.setStatus(_A)
class _IbmHprRtDetResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_IbmHprRtDetResult_Type.__name__=_C
_IbmHprRtDetResult_Object=MibTableColumn
ibmHprRtDetResult=_IbmHprRtDetResult_Object((1,3,6,1,4,1,2,5,10,4,3,1,1,7),_IbmHprRtDetResult_Type())
ibmHprRtDetResult.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmHprRtDetResult.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ibm':ibm,'ibmArchitecture':ibmArchitecture,'hpr':hpr,'ibmHprRouteTest':ibmHprRouteTest,'ibmHprRtGlobe':ibmHprRtGlobe,'ibmHprRtGlobeConnTrigger':ibmHprRtGlobeConnTrigger,'ibmHprRtGlobeNameTrigger':ibmHprRtGlobeNameTrigger,'ibmHprRtGenResults':ibmHprRtGenResults,'ibmHprRtGenTable':ibmHprRtGenTable,'ibmHprRtGenEntry':ibmHprRtGenEntry,_H:ibmHprRtGenTestId,'ibmHprRtGenTestType':ibmHprRtGenTestType,'ibmHprRtGenConnTrigger':ibmHprRtGenConnTrigger,'ibmHprRtGenNameTrigger':ibmHprRtGenNameTrigger,'ibmHprRtGenResult':ibmHprRtGenResult,'ibmHprRtGenSenseCode':ibmHprRtGenSenseCode,'ibmHprRtGenCosName':ibmHprRtGenCosName,'ibmHprRtGenRscv':ibmHprRtGenRscv,'ibmHprRtDetResults':ibmHprRtDetResults,'ibmHprRtDetTable':ibmHprRtDetTable,'ibmHprRtDetEntry':ibmHprRtDetEntry,_K:ibmHprRtDetTestId,_L:ibmHprRtDetSubTestId,'ibmHprRtDetDestNode':ibmHprRtDetDestNode,'ibmHprRtDetPriorNode':ibmHprRtDetPriorNode,'ibmHprRtDetLastTgNumber':ibmHprRtDetLastTgNumber,'ibmHprRtDetRtripTime':ibmHprRtDetRtripTime,'ibmHprRtDetResult':ibmHprRtDetResult})