_I='rcLinkAggregationGroupID'
_H='RAISECOM-LINKAGGREGATION-MIB'
_G='read-only'
_F='EnableVar'
_E='dot3adAggPortIndex'
_D='IEEE8023-LAG-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot3adAggPortIndex,=mibBuilder.importSymbols(_D,_E)
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
EnableVar,PortList=mibBuilder.importSymbols('SWITCH-TC',_F,'PortList')
rcLinkAggregation=ModuleIdentity((1,3,6,1,4,1,8886,6,1,6))
if mibBuilder.loadTexts:rcLinkAggregation.setRevisions(('1991-03-31 00:00',))
class _RcLinkAggregationStatus_Type(EnableVar):defaultValue=1
_RcLinkAggregationStatus_Type.__name__=_F
_RcLinkAggregationStatus_Object=MibScalar
rcLinkAggregationStatus=_RcLinkAggregationStatus_Object((1,3,6,1,4,1,8886,6,1,6,1),_RcLinkAggregationStatus_Type())
rcLinkAggregationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLinkAggregationStatus.setStatus(_A)
class _RcLinkAggregationLoadSharingMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('srcMAC',1),('destMAC',2),('srcXORDestMAC',3),('srcIP',4),('destIP',5),('srcXORDestIP',6)))
_RcLinkAggregationLoadSharingMode_Type.__name__=_C
_RcLinkAggregationLoadSharingMode_Object=MibScalar
rcLinkAggregationLoadSharingMode=_RcLinkAggregationLoadSharingMode_Object((1,3,6,1,4,1,8886,6,1,6,2),_RcLinkAggregationLoadSharingMode_Type())
rcLinkAggregationLoadSharingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLinkAggregationLoadSharingMode.setStatus(_A)
class _RcLinkAggregationTicketGenerationAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('direct-map',1),('crc',2)))
_RcLinkAggregationTicketGenerationAlgorithm_Type.__name__=_C
_RcLinkAggregationTicketGenerationAlgorithm_Object=MibScalar
rcLinkAggregationTicketGenerationAlgorithm=_RcLinkAggregationTicketGenerationAlgorithm_Object((1,3,6,1,4,1,8886,6,1,6,3),_RcLinkAggregationTicketGenerationAlgorithm_Type())
rcLinkAggregationTicketGenerationAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLinkAggregationTicketGenerationAlgorithm.setStatus(_A)
class _RcLinkAggregationMaxGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_RcLinkAggregationMaxGroup_Type.__name__=_C
_RcLinkAggregationMaxGroup_Object=MibScalar
rcLinkAggregationMaxGroup=_RcLinkAggregationMaxGroup_Object((1,3,6,1,4,1,8886,6,1,6,4),_RcLinkAggregationMaxGroup_Type())
rcLinkAggregationMaxGroup.setMaxAccess(_G)
if mibBuilder.loadTexts:rcLinkAggregationMaxGroup.setStatus(_A)
_RcLinkAggregationGroupTable_Object=MibTable
rcLinkAggregationGroupTable=_RcLinkAggregationGroupTable_Object((1,3,6,1,4,1,8886,6,1,6,5))
if mibBuilder.loadTexts:rcLinkAggregationGroupTable.setStatus(_A)
_RcLinkAggregationGroupEntry_Object=MibTableRow
rcLinkAggregationGroupEntry=_RcLinkAggregationGroupEntry_Object((1,3,6,1,4,1,8886,6,1,6,5,1))
rcLinkAggregationGroupEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:rcLinkAggregationGroupEntry.setStatus(_A)
class _RcLinkAggregationGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RcLinkAggregationGroupID_Type.__name__=_C
_RcLinkAggregationGroupID_Object=MibTableColumn
rcLinkAggregationGroupID=_RcLinkAggregationGroupID_Object((1,3,6,1,4,1,8886,6,1,6,5,1,1),_RcLinkAggregationGroupID_Type())
rcLinkAggregationGroupID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcLinkAggregationGroupID.setStatus(_A)
_RcLinkAggregationGroupSettingPorts_Type=PortList
_RcLinkAggregationGroupSettingPorts_Object=MibTableColumn
rcLinkAggregationGroupSettingPorts=_RcLinkAggregationGroupSettingPorts_Object((1,3,6,1,4,1,8886,6,1,6,5,1,2),_RcLinkAggregationGroupSettingPorts_Type())
rcLinkAggregationGroupSettingPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLinkAggregationGroupSettingPorts.setStatus(_A)
_RcLinkAggregationGroupCurrentPorts_Type=PortList
_RcLinkAggregationGroupCurrentPorts_Object=MibTableColumn
rcLinkAggregationGroupCurrentPorts=_RcLinkAggregationGroupCurrentPorts_Object((1,3,6,1,4,1,8886,6,1,6,5,1,3),_RcLinkAggregationGroupCurrentPorts_Type())
rcLinkAggregationGroupCurrentPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:rcLinkAggregationGroupCurrentPorts.setStatus(_A)
class _RcLinkAggregationGroupMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('lacp-static',2)))
_RcLinkAggregationGroupMode_Type.__name__=_C
_RcLinkAggregationGroupMode_Object=MibTableColumn
rcLinkAggregationGroupMode=_RcLinkAggregationGroupMode_Object((1,3,6,1,4,1,8886,6,1,6,5,1,4),_RcLinkAggregationGroupMode_Type())
rcLinkAggregationGroupMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLinkAggregationGroupMode.setStatus(_A)
class _RcLinkAggregationGroupMinLinks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_RcLinkAggregationGroupMinLinks_Type.__name__=_C
_RcLinkAggregationGroupMinLinks_Object=MibTableColumn
rcLinkAggregationGroupMinLinks=_RcLinkAggregationGroupMinLinks_Object((1,3,6,1,4,1,8886,6,1,6,5,1,5),_RcLinkAggregationGroupMinLinks_Type())
rcLinkAggregationGroupMinLinks.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLinkAggregationGroupMinLinks.setStatus(_A)
class _RcLinkAggregationGroupMaxLinks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_RcLinkAggregationGroupMaxLinks_Type.__name__=_C
_RcLinkAggregationGroupMaxLinks_Object=MibTableColumn
rcLinkAggregationGroupMaxLinks=_RcLinkAggregationGroupMaxLinks_Object((1,3,6,1,4,1,8886,6,1,6,5,1,6),_RcLinkAggregationGroupMaxLinks_Type())
rcLinkAggregationGroupMaxLinks.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLinkAggregationGroupMaxLinks.setStatus(_A)
_RcLinkAggregationPortStatsClearTable_Object=MibTable
rcLinkAggregationPortStatsClearTable=_RcLinkAggregationPortStatsClearTable_Object((1,3,6,1,4,1,8886,6,1,6,6))
if mibBuilder.loadTexts:rcLinkAggregationPortStatsClearTable.setStatus(_A)
_RcLinkAggregationPortStatsClearEntry_Object=MibTableRow
rcLinkAggregationPortStatsClearEntry=_RcLinkAggregationPortStatsClearEntry_Object((1,3,6,1,4,1,8886,6,1,6,6,1))
rcLinkAggregationPortStatsClearEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rcLinkAggregationPortStatsClearEntry.setStatus(_A)
_RcLinkAggregationPortStatsClear_Type=TruthValue
_RcLinkAggregationPortStatsClear_Object=MibTableColumn
rcLinkAggregationPortStatsClear=_RcLinkAggregationPortStatsClear_Object((1,3,6,1,4,1,8886,6,1,6,6,1,1),_RcLinkAggregationPortStatsClear_Type())
rcLinkAggregationPortStatsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLinkAggregationPortStatsClear.setStatus(_A)
_RcLinkAggregationPortLACPTable_Object=MibTable
rcLinkAggregationPortLACPTable=_RcLinkAggregationPortLACPTable_Object((1,3,6,1,4,1,8886,6,1,6,7))
if mibBuilder.loadTexts:rcLinkAggregationPortLACPTable.setStatus(_A)
_RcLinkAggregationPortLACPEntry_Object=MibTableRow
rcLinkAggregationPortLACPEntry=_RcLinkAggregationPortLACPEntry_Object((1,3,6,1,4,1,8886,6,1,6,7,1))
rcLinkAggregationPortLACPEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rcLinkAggregationPortLACPEntry.setStatus(_A)
class _RcLinkAggregationPortLACPEnable_Type(EnableVar):defaultValue=2
_RcLinkAggregationPortLACPEnable_Type.__name__=_F
_RcLinkAggregationPortLACPEnable_Object=MibTableColumn
rcLinkAggregationPortLACPEnable=_RcLinkAggregationPortLACPEnable_Object((1,3,6,1,4,1,8886,6,1,6,7,1,1),_RcLinkAggregationPortLACPEnable_Type())
rcLinkAggregationPortLACPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcLinkAggregationPortLACPEnable.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'rcLinkAggregation':rcLinkAggregation,'rcLinkAggregationStatus':rcLinkAggregationStatus,'rcLinkAggregationLoadSharingMode':rcLinkAggregationLoadSharingMode,'rcLinkAggregationTicketGenerationAlgorithm':rcLinkAggregationTicketGenerationAlgorithm,'rcLinkAggregationMaxGroup':rcLinkAggregationMaxGroup,'rcLinkAggregationGroupTable':rcLinkAggregationGroupTable,'rcLinkAggregationGroupEntry':rcLinkAggregationGroupEntry,_I:rcLinkAggregationGroupID,'rcLinkAggregationGroupSettingPorts':rcLinkAggregationGroupSettingPorts,'rcLinkAggregationGroupCurrentPorts':rcLinkAggregationGroupCurrentPorts,'rcLinkAggregationGroupMode':rcLinkAggregationGroupMode,'rcLinkAggregationGroupMinLinks':rcLinkAggregationGroupMinLinks,'rcLinkAggregationGroupMaxLinks':rcLinkAggregationGroupMaxLinks,'rcLinkAggregationPortStatsClearTable':rcLinkAggregationPortStatsClearTable,'rcLinkAggregationPortStatsClearEntry':rcLinkAggregationPortStatsClearEntry,'rcLinkAggregationPortStatsClear':rcLinkAggregationPortStatsClear,'rcLinkAggregationPortLACPTable':rcLinkAggregationPortLACPTable,'rcLinkAggregationPortLACPEntry':rcLinkAggregationPortLACPEntry,'rcLinkAggregationPortLACPEnable':rcLinkAggregationPortLACPEnable})