_F='ethernetTrapMessage'
_E='ethIntIndex'
_D='AT-ETH-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB','DisplayStringUnsized','modules')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ethernet=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,23))
if mibBuilder.loadTexts:ethernet.setRevisions(('2006-06-28 12:22','2013-02-07 13:50'))
_EthernetTraps_ObjectIdentity=ObjectIdentity
ethernetTraps=_EthernetTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,23,0))
_EthIntTable_Object=MibTable
ethIntTable=_EthIntTable_Object((1,3,6,1,4,1,207,8,4,4,4,23,1))
if mibBuilder.loadTexts:ethIntTable.setStatus(_A)
_EthIntEntry_Object=MibTableRow
ethIntEntry=_EthIntEntry_Object((1,3,6,1,4,1,207,8,4,4,4,23,1,1))
ethIntEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ethIntEntry.setStatus(_A)
_EthIntIndex_Type=Integer32
_EthIntIndex_Object=MibTableColumn
ethIntIndex=_EthIntIndex_Object((1,3,6,1,4,1,207,8,4,4,4,23,1,1,1),_EthIntIndex_Type())
ethIntIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntIndex.setStatus(_A)
_EthIntBoardIndex_Type=Integer32
_EthIntBoardIndex_Object=MibTableColumn
ethIntBoardIndex=_EthIntBoardIndex_Object((1,3,6,1,4,1,207,8,4,4,4,23,1,1,2),_EthIntBoardIndex_Type())
ethIntBoardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntBoardIndex.setStatus(_A)
_EthIntBoardPosition_Type=Integer32
_EthIntBoardPosition_Object=MibTableColumn
ethIntBoardPosition=_EthIntBoardPosition_Object((1,3,6,1,4,1,207,8,4,4,4,23,1,1,3),_EthIntBoardPosition_Type())
ethIntBoardPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntBoardPosition.setStatus(_A)
class _EthIntDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fullDuplex',1),('halfDuplex',2),('unknown',3)))
_EthIntDuplexMode_Type.__name__=_C
_EthIntDuplexMode_Object=MibTableColumn
ethIntDuplexMode=_EthIntDuplexMode_Object((1,3,6,1,4,1,207,8,4,4,4,23,1,1,4),_EthIntDuplexMode_Type())
ethIntDuplexMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ethIntDuplexMode.setStatus(_A)
class _EthBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_EthBandwidth_Type.__name__=_C
_EthBandwidth_Object=MibTableColumn
ethBandwidth=_EthBandwidth_Object((1,3,6,1,4,1,207,8,4,4,4,23,1,1,5),_EthBandwidth_Type())
ethBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ethBandwidth.setStatus(_A)
if mibBuilder.loadTexts:ethBandwidth.setUnits('kbps')
_EthernetTrapMessage_Type=DisplayString
_EthernetTrapMessage_Object=MibScalar
ethernetTrapMessage=_EthernetTrapMessage_Object((1,3,6,1,4,1,207,8,4,4,4,23,2),_EthernetTrapMessage_Type())
ethernetTrapMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:ethernetTrapMessage.setStatus(_A)
ethernetTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,23,0,1))
ethernetTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:ethernetTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ethernet':ethernet,'ethernetTraps':ethernetTraps,'ethernetTrap':ethernetTrap,'ethIntTable':ethIntTable,'ethIntEntry':ethIntEntry,_E:ethIntIndex,'ethIntBoardIndex':ethIntBoardIndex,'ethIntBoardPosition':ethIntBoardPosition,'ethIntDuplexMode':ethIntDuplexMode,'ethBandwidth':ethBandwidth,_F:ethernetTrapMessage})