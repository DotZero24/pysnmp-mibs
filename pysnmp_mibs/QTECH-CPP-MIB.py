_G='cppIndex'
_F='QTECH-CPP-MIB'
_E='2014-12-19 21:00'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
qtechCPPMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,132))
if mibBuilder.loadTexts:qtechCPPMIB.setRevisions((_E,_E))
_QtechCPPMIBObjects_ObjectIdentity=ObjectIdentity
qtechCPPMIBObjects=_QtechCPPMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,132,1))
_QtechCPPTable_Object=MibTable
qtechCPPTable=_QtechCPPTable_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1))
if mibBuilder.loadTexts:qtechCPPTable.setStatus(_A)
_QtechCPPEntry_Object=MibTableRow
qtechCPPEntry=_QtechCPPEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1))
qtechCPPEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:qtechCPPEntry.setStatus(_A)
class _CppIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppIndex_Type.__name__=_C
_CppIndex_Object=MibTableColumn
cppIndex=_CppIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1,1),_CppIndex_Type())
cppIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cppIndex.setStatus(_A)
class _CppDeviceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppDeviceId_Type.__name__=_C
_CppDeviceId_Object=MibTableColumn
cppDeviceId=_CppDeviceId_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1,2),_CppDeviceId_Type())
cppDeviceId.setMaxAccess(_B)
if mibBuilder.loadTexts:cppDeviceId.setStatus(_A)
class _CppSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppSlotId_Type.__name__=_C
_CppSlotId_Object=MibTableColumn
cppSlotId=_CppSlotId_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1,3),_CppSlotId_Type())
cppSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cppSlotId.setStatus(_A)
class _CppCardIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CppCardIndex_Type.__name__=_D
_CppCardIndex_Object=MibTableColumn
cppCardIndex=_CppCardIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1,4),_CppCardIndex_Type())
cppCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cppCardIndex.setStatus(_A)
class _CppPacketType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CppPacketType_Type.__name__=_D
_CppPacketType_Object=MibTableColumn
cppPacketType=_CppPacketType_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1,5),_CppPacketType_Type())
cppPacketType.setMaxAccess(_B)
if mibBuilder.loadTexts:cppPacketType.setStatus(_A)
class _CppTrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTrafficClass_Type.__name__=_C
_CppTrafficClass_Object=MibTableColumn
cppTrafficClass=_CppTrafficClass_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1,6),_CppTrafficClass_Type())
cppTrafficClass.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTrafficClass.setStatus(_A)
class _CppBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppBandwidth_Type.__name__=_C
_CppBandwidth_Object=MibTableColumn
cppBandwidth=_CppBandwidth_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1,7),_CppBandwidth_Type())
cppBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cppBandwidth.setStatus(_A)
class _CppRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppRate_Type.__name__=_C
_CppRate_Object=MibTableColumn
cppRate=_CppRate_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1,8),_CppRate_Type())
cppRate.setMaxAccess(_B)
if mibBuilder.loadTexts:cppRate.setStatus(_A)
class _CppDrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppDrop_Type.__name__=_C
_CppDrop_Object=MibTableColumn
cppDrop=_CppDrop_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1,9),_CppDrop_Type())
cppDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cppDrop.setStatus(_A)
class _CppTotal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTotal_Type.__name__=_C
_CppTotal_Object=MibTableColumn
cppTotal=_CppTotal_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1,10),_CppTotal_Type())
cppTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTotal.setStatus(_A)
class _CppTotalDrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CppTotalDrop_Type.__name__=_C
_CppTotalDrop_Object=MibTableColumn
cppTotalDrop=_CppTotalDrop_Object((1,3,6,1,4,1,27514,1,1,10,2,132,1,1,1,11),_CppTotalDrop_Type())
cppTotalDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:cppTotalDrop.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'qtechCPPMIB':qtechCPPMIB,'qtechCPPMIBObjects':qtechCPPMIBObjects,'qtechCPPTable':qtechCPPTable,'qtechCPPEntry':qtechCPPEntry,_G:cppIndex,'cppDeviceId':cppDeviceId,'cppSlotId':cppSlotId,'cppCardIndex':cppCardIndex,'cppPacketType':cppPacketType,'cppTrafficClass':cppTrafficClass,'cppBandwidth':cppBandwidth,'cppRate':cppRate,'cppDrop':cppDrop,'cppTotal':cppTotal,'cppTotalDrop':cppTotalDrop})