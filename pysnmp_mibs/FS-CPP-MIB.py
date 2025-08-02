_H='cppTcIndex'
_G='cppIndex'
_F='2014-12-19 21:00'
_E='FS-CPP-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
fsCPPMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,132))
if mibBuilder.loadTexts:fsCPPMIB.setRevisions((_F,_F))
_FsCPPMIBObjects_ObjectIdentity=ObjectIdentity
fsCPPMIBObjects=_FsCPPMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,132,1))
_FsCPPTable_Object=MibTable
fsCPPTable=_FsCPPTable_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1))
if mibBuilder.loadTexts:fsCPPTable.setStatus(_A)
_FsCPPEntry_Object=MibTableRow
fsCPPEntry=_FsCPPEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1))
fsCPPEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:fsCPPEntry.setStatus(_A)
class _CppIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppIndex_Type.__name__=_C
_CppIndex_Object=MibTableColumn
cppIndex=_CppIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1,1),_CppIndex_Type())
cppIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cppIndex.setStatus(_A)
class _CppDeviceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppDeviceId_Type.__name__=_C
_CppDeviceId_Object=MibTableColumn
cppDeviceId=_CppDeviceId_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1,2),_CppDeviceId_Type())
cppDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cppDeviceId.setStatus(_A)
class _CppSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppSlotId_Type.__name__=_C
_CppSlotId_Object=MibTableColumn
cppSlotId=_CppSlotId_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1,3),_CppSlotId_Type())
cppSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cppSlotId.setStatus(_A)
class _CppCardIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CppCardIndex_Type.__name__=_D
_CppCardIndex_Object=MibTableColumn
cppCardIndex=_CppCardIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1,4),_CppCardIndex_Type())
cppCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cppCardIndex.setStatus(_A)
class _CppPacketType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CppPacketType_Type.__name__=_D
_CppPacketType_Object=MibTableColumn
cppPacketType=_CppPacketType_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1,5),_CppPacketType_Type())
cppPacketType.setMaxAccess(_B)
if mibBuilder.loadTexts:cppPacketType.setStatus(_A)
class _CppTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTrafficClass_Type.__name__=_C
_CppTrafficClass_Object=MibTableColumn
cppTrafficClass=_CppTrafficClass_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1,6),_CppTrafficClass_Type())
cppTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTrafficClass.setStatus(_A)
class _CppBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppBandwidth_Type.__name__=_C
_CppBandwidth_Object=MibTableColumn
cppBandwidth=_CppBandwidth_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1,7),_CppBandwidth_Type())
cppBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cppBandwidth.setStatus(_A)
class _CppRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppRate_Type.__name__=_C
_CppRate_Object=MibTableColumn
cppRate=_CppRate_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1,8),_CppRate_Type())
cppRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cppRate.setStatus(_A)
class _CppDrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppDrop_Type.__name__=_C
_CppDrop_Object=MibTableColumn
cppDrop=_CppDrop_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1,9),_CppDrop_Type())
cppDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cppDrop.setStatus(_A)
class _CppTotal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTotal_Type.__name__=_C
_CppTotal_Object=MibTableColumn
cppTotal=_CppTotal_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1,10),_CppTotal_Type())
cppTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTotal.setStatus(_A)
class _CppTotalDrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTotalDrop_Type.__name__=_C
_CppTotalDrop_Object=MibTableColumn
cppTotalDrop=_CppTotalDrop_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,1,1,11),_CppTotalDrop_Type())
cppTotalDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTotalDrop.setStatus(_A)
_FsCPPTcTable_Object=MibTable
fsCPPTcTable=_FsCPPTcTable_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,2))
if mibBuilder.loadTexts:fsCPPTcTable.setStatus(_A)
_FsCPPTcEntry_Object=MibTableRow
fsCPPTcEntry=_FsCPPTcEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,2,1))
fsCPPTcEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:fsCPPTcEntry.setStatus(_A)
class _CppTcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTcIndex_Type.__name__=_C
_CppTcIndex_Object=MibTableColumn
cppTcIndex=_CppTcIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,2,1,1),_CppTcIndex_Type())
cppTcIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTcIndex.setStatus(_A)
class _CppTcDeviceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTcDeviceId_Type.__name__=_C
_CppTcDeviceId_Object=MibTableColumn
cppTcDeviceId=_CppTcDeviceId_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,2,1,2),_CppTcDeviceId_Type())
cppTcDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTcDeviceId.setStatus(_A)
class _CppTcSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTcSlotId_Type.__name__=_C
_CppTcSlotId_Object=MibTableColumn
cppTcSlotId=_CppTcSlotId_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,2,1,3),_CppTcSlotId_Type())
cppTcSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTcSlotId.setStatus(_A)
class _CppTcTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTcTrafficClass_Type.__name__=_C
_CppTcTrafficClass_Object=MibTableColumn
cppTcTrafficClass=_CppTcTrafficClass_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,2,1,4),_CppTcTrafficClass_Type())
cppTcTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTcTrafficClass.setStatus(_A)
class _CppTcCardIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CppTcCardIndex_Type.__name__=_D
_CppTcCardIndex_Object=MibTableColumn
cppTcCardIndex=_CppTcCardIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,2,1,5),_CppTcCardIndex_Type())
cppTcCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTcCardIndex.setStatus(_A)
class _CppTcBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTcBandwidth_Type.__name__=_C
_CppTcBandwidth_Object=MibTableColumn
cppTcBandwidth=_CppTcBandwidth_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,2,1,6),_CppTcBandwidth_Type())
cppTcBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTcBandwidth.setStatus(_A)
class _CppTcRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTcRate_Type.__name__=_C
_CppTcRate_Object=MibTableColumn
cppTcRate=_CppTcRate_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,2,1,7),_CppTcRate_Type())
cppTcRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTcRate.setStatus(_A)
class _CppTcDrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTcDrop_Type.__name__=_C
_CppTcDrop_Object=MibTableColumn
cppTcDrop=_CppTcDrop_Object((1,3,6,1,4,1,52642,1,1,10,2,132,1,2,1,8),_CppTcDrop_Type())
cppTcDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTcDrop.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fsCPPMIB':fsCPPMIB,'fsCPPMIBObjects':fsCPPMIBObjects,'fsCPPTable':fsCPPTable,'fsCPPEntry':fsCPPEntry,_G:cppIndex,'cppDeviceId':cppDeviceId,'cppSlotId':cppSlotId,'cppCardIndex':cppCardIndex,'cppPacketType':cppPacketType,'cppTrafficClass':cppTrafficClass,'cppBandwidth':cppBandwidth,'cppRate':cppRate,'cppDrop':cppDrop,'cppTotal':cppTotal,'cppTotalDrop':cppTotalDrop,'fsCPPTcTable':fsCPPTcTable,'fsCPPTcEntry':fsCPPTcEntry,_H:cppTcIndex,'cppTcDeviceId':cppTcDeviceId,'cppTcSlotId':cppTcSlotId,'cppTcTrafficClass':cppTcTrafficClass,'cppTcCardIndex':cppTcCardIndex,'cppTcBandwidth':cppTcBandwidth,'cppTcRate':cppTcRate,'cppTcDrop':cppTcDrop})