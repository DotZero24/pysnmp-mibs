_R='ds0ConfigGroup'
_Q='dsx0ChanMappedIfIndex'
_P='dsx0Ds0BundleMappedIfIndex'
_O='dsx0TransmitCodesEnable'
_N='dsx0ReceivedCode'
_M='dsx0SeizedCode'
_L='dsx0IdleCode'
_K='dsx0CircuitIdentifier'
_J='dsx0RobbedBitSignalling'
_I='DisplayString'
_H='dsx0Ds0ChannelNumber'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='DS0-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_F,'InterfaceIndex','InterfaceIndexOrZero',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention','TruthValue')
ds0=ModuleIdentity((1,3,6,1,2,1,10,81))
if mibBuilder.loadTexts:ds0.setRevisions(('1998-05-24 20:10',))
_Dsx0ConfigTable_Object=MibTable
dsx0ConfigTable=_Dsx0ConfigTable_Object((1,3,6,1,2,1,10,81,1))
if mibBuilder.loadTexts:dsx0ConfigTable.setStatus(_A)
_Dsx0ConfigEntry_Object=MibTableRow
dsx0ConfigEntry=_Dsx0ConfigEntry_Object((1,3,6,1,2,1,10,81,1,1))
dsx0ConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dsx0ConfigEntry.setStatus(_A)
class _Dsx0Ds0ChannelNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_Dsx0Ds0ChannelNumber_Type.__name__=_C
_Dsx0Ds0ChannelNumber_Object=MibTableColumn
dsx0Ds0ChannelNumber=_Dsx0Ds0ChannelNumber_Object((1,3,6,1,2,1,10,81,1,1,1),_Dsx0Ds0ChannelNumber_Type())
dsx0Ds0ChannelNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx0Ds0ChannelNumber.setStatus(_A)
_Dsx0RobbedBitSignalling_Type=TruthValue
_Dsx0RobbedBitSignalling_Object=MibTableColumn
dsx0RobbedBitSignalling=_Dsx0RobbedBitSignalling_Object((1,3,6,1,2,1,10,81,1,1,2),_Dsx0RobbedBitSignalling_Type())
dsx0RobbedBitSignalling.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx0RobbedBitSignalling.setStatus(_A)
class _Dsx0CircuitIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Dsx0CircuitIdentifier_Type.__name__=_I
_Dsx0CircuitIdentifier_Object=MibTableColumn
dsx0CircuitIdentifier=_Dsx0CircuitIdentifier_Object((1,3,6,1,2,1,10,81,1,1,3),_Dsx0CircuitIdentifier_Type())
dsx0CircuitIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx0CircuitIdentifier.setStatus(_A)
class _Dsx0IdleCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Dsx0IdleCode_Type.__name__=_C
_Dsx0IdleCode_Object=MibTableColumn
dsx0IdleCode=_Dsx0IdleCode_Object((1,3,6,1,2,1,10,81,1,1,4),_Dsx0IdleCode_Type())
dsx0IdleCode.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx0IdleCode.setStatus(_A)
class _Dsx0SeizedCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Dsx0SeizedCode_Type.__name__=_C
_Dsx0SeizedCode_Object=MibTableColumn
dsx0SeizedCode=_Dsx0SeizedCode_Object((1,3,6,1,2,1,10,81,1,1,5),_Dsx0SeizedCode_Type())
dsx0SeizedCode.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx0SeizedCode.setStatus(_A)
class _Dsx0ReceivedCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Dsx0ReceivedCode_Type.__name__=_C
_Dsx0ReceivedCode_Object=MibTableColumn
dsx0ReceivedCode=_Dsx0ReceivedCode_Object((1,3,6,1,2,1,10,81,1,1,6),_Dsx0ReceivedCode_Type())
dsx0ReceivedCode.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx0ReceivedCode.setStatus(_A)
_Dsx0TransmitCodesEnable_Type=TruthValue
_Dsx0TransmitCodesEnable_Object=MibTableColumn
dsx0TransmitCodesEnable=_Dsx0TransmitCodesEnable_Object((1,3,6,1,2,1,10,81,1,1,7),_Dsx0TransmitCodesEnable_Type())
dsx0TransmitCodesEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx0TransmitCodesEnable.setStatus(_A)
_Dsx0Ds0BundleMappedIfIndex_Type=InterfaceIndexOrZero
_Dsx0Ds0BundleMappedIfIndex_Object=MibTableColumn
dsx0Ds0BundleMappedIfIndex=_Dsx0Ds0BundleMappedIfIndex_Object((1,3,6,1,2,1,10,81,1,1,8),_Dsx0Ds0BundleMappedIfIndex_Type())
dsx0Ds0BundleMappedIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx0Ds0BundleMappedIfIndex.setStatus(_A)
_Ds0Conformance_ObjectIdentity=ObjectIdentity
ds0Conformance=_Ds0Conformance_ObjectIdentity((1,3,6,1,2,1,10,81,2))
_Ds0Groups_ObjectIdentity=ObjectIdentity
ds0Groups=_Ds0Groups_ObjectIdentity((1,3,6,1,2,1,10,81,2,1))
_Ds0Compliances_ObjectIdentity=ObjectIdentity
ds0Compliances=_Ds0Compliances_ObjectIdentity((1,3,6,1,2,1,10,81,2,2))
_Dsx0ChanMappingTable_Object=MibTable
dsx0ChanMappingTable=_Dsx0ChanMappingTable_Object((1,3,6,1,2,1,10,81,3))
if mibBuilder.loadTexts:dsx0ChanMappingTable.setStatus(_A)
_Dsx0ChanMappingEntry_Object=MibTableRow
dsx0ChanMappingEntry=_Dsx0ChanMappingEntry_Object((1,3,6,1,2,1,10,81,3,1))
dsx0ChanMappingEntry.setIndexNames((0,_F,_G),(0,_B,_H))
if mibBuilder.loadTexts:dsx0ChanMappingEntry.setStatus(_A)
_Dsx0ChanMappedIfIndex_Type=InterfaceIndex
_Dsx0ChanMappedIfIndex_Object=MibTableColumn
dsx0ChanMappedIfIndex=_Dsx0ChanMappedIfIndex_Object((1,3,6,1,2,1,10,81,3,1,1),_Dsx0ChanMappedIfIndex_Type())
dsx0ChanMappedIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx0ChanMappedIfIndex.setStatus(_A)
ds0ConfigGroup=ObjectGroup((1,3,6,1,2,1,10,81,2,1,1))
ds0ConfigGroup.setObjects(*((_B,_H),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ds0ConfigGroup.setStatus(_A)
ds0Compliance=ModuleCompliance((1,3,6,1,2,1,10,81,2,2,1))
ds0Compliance.setObjects((_B,_R))
if mibBuilder.loadTexts:ds0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ds0':ds0,'dsx0ConfigTable':dsx0ConfigTable,'dsx0ConfigEntry':dsx0ConfigEntry,_H:dsx0Ds0ChannelNumber,_J:dsx0RobbedBitSignalling,_K:dsx0CircuitIdentifier,_L:dsx0IdleCode,_M:dsx0SeizedCode,_N:dsx0ReceivedCode,_O:dsx0TransmitCodesEnable,_P:dsx0Ds0BundleMappedIfIndex,'ds0Conformance':ds0Conformance,'ds0Groups':ds0Groups,_R:ds0ConfigGroup,'ds0Compliances':ds0Compliances,'ds0Compliance':ds0Compliance,'dsx0ChanMappingTable':dsx0ChanMappingTable,'dsx0ChanMappingEntry':dsx0ChanMappingEntry,_Q:dsx0ChanMappedIfIndex})