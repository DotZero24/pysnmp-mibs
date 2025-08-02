_F='ethIfIndex'
_E='BIANCA-ETH-IF-MIB'
_D='PhysAddress'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_D,'TextualConvention')
class Date(Integer32):0
class HexValue(Integer32):0
class PhysAddress(OctetString):0
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Eth_ObjectIdentity=ObjectIdentity
eth=_Eth_ObjectIdentity((1,3,6,1,4,1,272,4,37))
_EthIfTable_Object=MibTable
ethIfTable=_EthIfTable_Object((1,3,6,1,4,1,272,4,37,1))
if mibBuilder.loadTexts:ethIfTable.setStatus(_A)
_EthIfEntry_Object=MibTableRow
ethIfEntry=_EthIfEntry_Object((1,3,6,1,4,1,272,4,37,1,1))
ethIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ethIfEntry.setStatus(_A)
_EthIfIndex_Type=Integer32
_EthIfIndex_Object=MibTableColumn
ethIfIndex=_EthIfIndex_Object((1,3,6,1,4,1,272,4,37,1,1,1),_EthIfIndex_Type())
ethIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:ethIfIndex.setStatus(_A)
class _EthIfPortGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_EthIfPortGroup_Type.__name__=_B
_EthIfPortGroup_Object=MibTableColumn
ethIfPortGroup=_EthIfPortGroup_Object((1,3,6,1,4,1,272,4,37,1,1,4),_EthIfPortGroup_Type())
ethIfPortGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfPortGroup.setStatus(_A)
class _EthIfMACSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_EthIfMACSlot_Type.__name__=_B
_EthIfMACSlot_Object=MibTableColumn
ethIfMACSlot=_EthIfMACSlot_Object((1,3,6,1,4,1,272,4,37,1,1,5),_EthIfMACSlot_Type())
ethIfMACSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfMACSlot.setStatus(_A)
class _EthIfMACUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_EthIfMACUnit_Type.__name__=_B
_EthIfMACUnit_Object=MibTableColumn
ethIfMACUnit=_EthIfMACUnit_Object((1,3,6,1,4,1,272,4,37,1,1,6),_EthIfMACUnit_Type())
ethIfMACUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfMACUnit.setStatus(_A)
class _EthIfAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_EthIfAdminStatus_Type.__name__=_B
_EthIfAdminStatus_Object=MibTableColumn
ethIfAdminStatus=_EthIfAdminStatus_Object((1,3,6,1,4,1,272,4,37,1,1,7),_EthIfAdminStatus_Type())
ethIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ethIfAdminStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'Date':Date,'HexValue':HexValue,_D:PhysAddress,'bintec':bintec,'bibo':bibo,'eth':eth,'ethIfTable':ethIfTable,'ethIfEntry':ethIfEntry,_F:ethIfIndex,'ethIfPortGroup':ethIfPortGroup,'ethIfMACSlot':ethIfMACSlot,'ethIfMACUnit':ethIfMACUnit,'ethIfAdminStatus':ethIfAdminStatus})