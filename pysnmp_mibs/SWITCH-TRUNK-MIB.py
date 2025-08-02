_G='rcTrunkGroupID'
_F='SWITCH-TRUNK-MIB'
_E='read-only'
_D='EnableVar'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
EnableVar,PortList=mibBuilder.importSymbols('SWITCH-TC',_D,'PortList')
rcTrunk=ModuleIdentity((1,3,6,1,4,1,8886,6,1,6))
if mibBuilder.loadTexts:rcTrunk.setRevisions(('1991-03-31 00:00',))
class _RcTrunkEnable_Type(EnableVar):defaultValue=2
_RcTrunkEnable_Type.__name__=_D
_RcTrunkEnable_Object=MibScalar
rcTrunkEnable=_RcTrunkEnable_Object((1,3,6,1,4,1,8886,6,1,6,1),_RcTrunkEnable_Type())
rcTrunkEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcTrunkEnable.setStatus(_A)
class _RcTrunkLoadingSharingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('srcMAC',1),('destMAC',2),('srcXORDestMAC',3),('srcIP',4),('destIP',5),('srcXORDestIP',6),('SrcXORDestMACXORSrcPort',7)))
_RcTrunkLoadingSharingMode_Type.__name__=_B
_RcTrunkLoadingSharingMode_Object=MibScalar
rcTrunkLoadingSharingMode=_RcTrunkLoadingSharingMode_Object((1,3,6,1,4,1,8886,6,1,6,2),_RcTrunkLoadingSharingMode_Type())
rcTrunkLoadingSharingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcTrunkLoadingSharingMode.setStatus(_A)
class _RcTrunkMaxGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_RcTrunkMaxGroup_Type.__name__=_B
_RcTrunkMaxGroup_Object=MibScalar
rcTrunkMaxGroup=_RcTrunkMaxGroup_Object((1,3,6,1,4,1,8886,6,1,6,3),_RcTrunkMaxGroup_Type())
rcTrunkMaxGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:rcTrunkMaxGroup.setStatus(_A)
class _RcTrunkTicketGenerationAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('direct-map',1),('crc',2)))
_RcTrunkTicketGenerationAlgorithm_Type.__name__=_B
_RcTrunkTicketGenerationAlgorithm_Object=MibScalar
rcTrunkTicketGenerationAlgorithm=_RcTrunkTicketGenerationAlgorithm_Object((1,3,6,1,4,1,8886,6,1,6,4),_RcTrunkTicketGenerationAlgorithm_Type())
rcTrunkTicketGenerationAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:rcTrunkTicketGenerationAlgorithm.setStatus(_A)
_RcTrunkGroupTable_Object=MibTable
rcTrunkGroupTable=_RcTrunkGroupTable_Object((1,3,6,1,4,1,8886,6,1,6,5))
if mibBuilder.loadTexts:rcTrunkGroupTable.setStatus(_A)
_RcTrunkGroupEntry_Object=MibTableRow
rcTrunkGroupEntry=_RcTrunkGroupEntry_Object((1,3,6,1,4,1,8886,6,1,6,5,1))
rcTrunkGroupEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rcTrunkGroupEntry.setStatus(_A)
class _RcTrunkGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RcTrunkGroupID_Type.__name__=_B
_RcTrunkGroupID_Object=MibTableColumn
rcTrunkGroupID=_RcTrunkGroupID_Object((1,3,6,1,4,1,8886,6,1,6,5,1,1),_RcTrunkGroupID_Type())
rcTrunkGroupID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcTrunkGroupID.setStatus(_A)
_RcTrunkGroupSetPorts_Type=PortList
_RcTrunkGroupSetPorts_Object=MibTableColumn
rcTrunkGroupSetPorts=_RcTrunkGroupSetPorts_Object((1,3,6,1,4,1,8886,6,1,6,5,1,2),_RcTrunkGroupSetPorts_Type())
rcTrunkGroupSetPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rcTrunkGroupSetPorts.setStatus(_A)
_RcTrunkGroupCurrentPortInOperation_Type=PortList
_RcTrunkGroupCurrentPortInOperation_Object=MibTableColumn
rcTrunkGroupCurrentPortInOperation=_RcTrunkGroupCurrentPortInOperation_Object((1,3,6,1,4,1,8886,6,1,6,5,1,3),_RcTrunkGroupCurrentPortInOperation_Type())
rcTrunkGroupCurrentPortInOperation.setMaxAccess(_E)
if mibBuilder.loadTexts:rcTrunkGroupCurrentPortInOperation.setStatus(_A)
class _RcTrunkGroupMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('lacp-static',2)))
_RcTrunkGroupMode_Type.__name__=_B
_RcTrunkGroupMode_Object=MibTableColumn
rcTrunkGroupMode=_RcTrunkGroupMode_Object((1,3,6,1,4,1,8886,6,1,6,5,1,4),_RcTrunkGroupMode_Type())
rcTrunkGroupMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rcTrunkGroupMode.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'rcTrunk':rcTrunk,'rcTrunkEnable':rcTrunkEnable,'rcTrunkLoadingSharingMode':rcTrunkLoadingSharingMode,'rcTrunkMaxGroup':rcTrunkMaxGroup,'rcTrunkTicketGenerationAlgorithm':rcTrunkTicketGenerationAlgorithm,'rcTrunkGroupTable':rcTrunkGroupTable,'rcTrunkGroupEntry':rcTrunkGroupEntry,_G:rcTrunkGroupID,'rcTrunkGroupSetPorts':rcTrunkGroupSetPorts,'rcTrunkGroupCurrentPortInOperation':rcTrunkGroupCurrentPortInOperation,'rcTrunkGroupMode':rcTrunkGroupMode})