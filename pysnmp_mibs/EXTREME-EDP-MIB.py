_K='extremeEdpNeighborVlanName'
_J='accessible-for-notify'
_I='DisplayString'
_H='ifIndex'
_G='IF-MIB'
_F='extremeEdpNeighborId'
_E='extremeEdpPortIfIndex'
_D='Integer32'
_C='EXTREME-EDP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ExtremeDeviceId,extremeAgent=mibBuilder.importSymbols('EXTREME-BASE-MIB','ExtremeDeviceId','extremeAgent')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention','TruthValue')
extremeEdp=ModuleIdentity((1,3,6,1,4,1,1916,1,13))
_ExtremeEdpTable_Object=MibTable
extremeEdpTable=_ExtremeEdpTable_Object((1,3,6,1,4,1,1916,1,13,2))
if mibBuilder.loadTexts:extremeEdpTable.setStatus(_A)
_ExtremeEdpEntry_Object=MibTableRow
extremeEdpEntry=_ExtremeEdpEntry_Object((1,3,6,1,4,1,1916,1,13,2,1))
extremeEdpEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:extremeEdpEntry.setStatus(_A)
class _ExtremeEdpPortIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeEdpPortIfIndex_Type.__name__=_D
_ExtremeEdpPortIfIndex_Object=MibTableColumn
extremeEdpPortIfIndex=_ExtremeEdpPortIfIndex_Object((1,3,6,1,4,1,1916,1,13,2,1,1),_ExtremeEdpPortIfIndex_Type())
extremeEdpPortIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeEdpPortIfIndex.setStatus(_A)
_ExtremeEdpNeighborId_Type=ExtremeDeviceId
_ExtremeEdpNeighborId_Object=MibTableColumn
extremeEdpNeighborId=_ExtremeEdpNeighborId_Object((1,3,6,1,4,1,1916,1,13,2,1,2),_ExtremeEdpNeighborId_Type())
extremeEdpNeighborId.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeEdpNeighborId.setStatus(_A)
_ExtremeEdpNeighborName_Type=DisplayString
_ExtremeEdpNeighborName_Object=MibTableColumn
extremeEdpNeighborName=_ExtremeEdpNeighborName_Object((1,3,6,1,4,1,1916,1,13,2,1,3),_ExtremeEdpNeighborName_Type())
extremeEdpNeighborName.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEdpNeighborName.setStatus(_A)
_ExtremeEdpNeighborSoftwareVersion_Type=DisplayString
_ExtremeEdpNeighborSoftwareVersion_Object=MibTableColumn
extremeEdpNeighborSoftwareVersion=_ExtremeEdpNeighborSoftwareVersion_Object((1,3,6,1,4,1,1916,1,13,2,1,4),_ExtremeEdpNeighborSoftwareVersion_Type())
extremeEdpNeighborSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEdpNeighborSoftwareVersion.setStatus(_A)
class _ExtremeEdpNeighborSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeEdpNeighborSlot_Type.__name__=_D
_ExtremeEdpNeighborSlot_Object=MibTableColumn
extremeEdpNeighborSlot=_ExtremeEdpNeighborSlot_Object((1,3,6,1,4,1,1916,1,13,2,1,5),_ExtremeEdpNeighborSlot_Type())
extremeEdpNeighborSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEdpNeighborSlot.setStatus(_A)
class _ExtremeEdpNeighborPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeEdpNeighborPort_Type.__name__=_D
_ExtremeEdpNeighborPort_Object=MibTableColumn
extremeEdpNeighborPort=_ExtremeEdpNeighborPort_Object((1,3,6,1,4,1,1916,1,13,2,1,6),_ExtremeEdpNeighborPort_Type())
extremeEdpNeighborPort.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEdpNeighborPort.setStatus(_A)
_ExtremeEdpEntryAge_Type=Integer32
_ExtremeEdpEntryAge_Object=MibTableColumn
extremeEdpEntryAge=_ExtremeEdpEntryAge_Object((1,3,6,1,4,1,1916,1,13,2,1,7),_ExtremeEdpEntryAge_Type())
extremeEdpEntryAge.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEdpEntryAge.setStatus(_A)
_ExtremeEdpNeighborTable_Object=MibTable
extremeEdpNeighborTable=_ExtremeEdpNeighborTable_Object((1,3,6,1,4,1,1916,1,13,3))
if mibBuilder.loadTexts:extremeEdpNeighborTable.setStatus(_A)
_ExtremeEdpNeighborEntry_Object=MibTableRow
extremeEdpNeighborEntry=_ExtremeEdpNeighborEntry_Object((1,3,6,1,4,1,1916,1,13,3,1))
extremeEdpNeighborEntry.setIndexNames((0,_C,_E),(0,_C,_F),(0,_C,_K))
if mibBuilder.loadTexts:extremeEdpNeighborEntry.setStatus(_A)
class _ExtremeEdpNeighborVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,81))
_ExtremeEdpNeighborVlanName_Type.__name__=_I
_ExtremeEdpNeighborVlanName_Object=MibTableColumn
extremeEdpNeighborVlanName=_ExtremeEdpNeighborVlanName_Object((1,3,6,1,4,1,1916,1,13,3,1,1),_ExtremeEdpNeighborVlanName_Type())
extremeEdpNeighborVlanName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:extremeEdpNeighborVlanName.setStatus(_A)
class _ExtremeEdpNeighborVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ExtremeEdpNeighborVlanId_Type.__name__=_D
_ExtremeEdpNeighborVlanId_Object=MibTableColumn
extremeEdpNeighborVlanId=_ExtremeEdpNeighborVlanId_Object((1,3,6,1,4,1,1916,1,13,3,1,2),_ExtremeEdpNeighborVlanId_Type())
extremeEdpNeighborVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEdpNeighborVlanId.setStatus(_A)
_ExtremeEdpNeighborVlanIpAddress_Type=IpAddress
_ExtremeEdpNeighborVlanIpAddress_Object=MibTableColumn
extremeEdpNeighborVlanIpAddress=_ExtremeEdpNeighborVlanIpAddress_Object((1,3,6,1,4,1,1916,1,13,3,1,3),_ExtremeEdpNeighborVlanIpAddress_Type())
extremeEdpNeighborVlanIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeEdpNeighborVlanIpAddress.setStatus(_A)
_ExtremeEdpPortTable_Object=MibTable
extremeEdpPortTable=_ExtremeEdpPortTable_Object((1,3,6,1,4,1,1916,1,13,4))
if mibBuilder.loadTexts:extremeEdpPortTable.setStatus(_A)
_ExtremeEdpPortEntry_Object=MibTableRow
extremeEdpPortEntry=_ExtremeEdpPortEntry_Object((1,3,6,1,4,1,1916,1,13,4,1))
extremeEdpPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:extremeEdpPortEntry.setStatus(_A)
_ExtremeEdpPortState_Type=TruthValue
_ExtremeEdpPortState_Object=MibTableColumn
extremeEdpPortState=_ExtremeEdpPortState_Object((1,3,6,1,4,1,1916,1,13,4,1,1),_ExtremeEdpPortState_Type())
extremeEdpPortState.setMaxAccess('read-write')
if mibBuilder.loadTexts:extremeEdpPortState.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'extremeEdp':extremeEdp,'extremeEdpTable':extremeEdpTable,'extremeEdpEntry':extremeEdpEntry,_E:extremeEdpPortIfIndex,_F:extremeEdpNeighborId,'extremeEdpNeighborName':extremeEdpNeighborName,'extremeEdpNeighborSoftwareVersion':extremeEdpNeighborSoftwareVersion,'extremeEdpNeighborSlot':extremeEdpNeighborSlot,'extremeEdpNeighborPort':extremeEdpNeighborPort,'extremeEdpEntryAge':extremeEdpEntryAge,'extremeEdpNeighborTable':extremeEdpNeighborTable,'extremeEdpNeighborEntry':extremeEdpNeighborEntry,_K:extremeEdpNeighborVlanName,'extremeEdpNeighborVlanId':extremeEdpNeighborVlanId,'extremeEdpNeighborVlanIpAddress':extremeEdpNeighborVlanIpAddress,'extremeEdpPortTable':extremeEdpPortTable,'extremeEdpPortEntry':extremeEdpPortEntry,'extremeEdpPortState':extremeEdpPortState})