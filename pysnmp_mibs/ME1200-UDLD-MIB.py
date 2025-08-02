_V='me1200UdldStatusInterfaceNeighborTableInfoGroup'
_U='me1200UdldStatusInterfaceTableInfoGroup'
_T='me1200UdldConfigInterfaceParamTableInfoGroup'
_S='me1200UdldStatusInterfaceNeighborLinkDetectionState'
_R='me1200UdldStatusInterfaceNeighborNeighborDeviceName'
_Q='me1200UdldStatusInterfaceNeighborNeighborPortID'
_P='me1200UdldStatusInterfaceNeighborNeighborDeviceID'
_O='me1200UdldStatusInterfaceLinkState'
_N='me1200UdldStatusInterfaceDeviceName'
_M='me1200UdldStatusInterfaceDeviceID'
_L='me1200UdldConfigInterfaceParamProbeMsgInterval'
_K='me1200UdldConfigInterfaceParamUdldMode'
_J='me1200UdldStatusInterfaceNeighborIfIndex'
_I='me1200UdldStatusInterfaceIfIndex'
_H='read-write'
_G='me1200UdldConfigInterfaceParamIfIndex'
_F='Unsigned32'
_E='not-accessible'
_D='ME1200DisplayString'
_C='read-only'
_B='ME1200-UDLD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200DisplayString,ME1200InterfaceIndex=mibBuilder.importSymbols('ME1200-TC',_D,'ME1200InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
me1200UdldMib=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,123))
if mibBuilder.loadTexts:me1200UdldMib.setRevisions(('2014-03-11 00:00',))
class ME1200UdldDetectionState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('inDeterminant',0),('uniDirectional',1),('biDirectional',2),('neighborMismatch',3),('loopback',4),('multipleNeighbor',5)))
class ME1200UdldMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('disable',0),('normal',1),('aggressive',2)))
_Me1200UdldMibObjects_ObjectIdentity=ObjectIdentity
me1200UdldMibObjects=_Me1200UdldMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,123,1))
_Me1200UdldConfig_ObjectIdentity=ObjectIdentity
me1200UdldConfig=_Me1200UdldConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,123,1,2))
_Me1200UdldConfigInterface_ObjectIdentity=ObjectIdentity
me1200UdldConfigInterface=_Me1200UdldConfigInterface_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,123,1,2,1))
_Me1200UdldConfigInterfaceParamTable_Object=MibTable
me1200UdldConfigInterfaceParamTable=_Me1200UdldConfigInterfaceParamTable_Object((1,3,6,1,4,1,9,9,815,1,123,1,2,1,1))
if mibBuilder.loadTexts:me1200UdldConfigInterfaceParamTable.setStatus(_A)
_Me1200UdldConfigInterfaceParamEntry_Object=MibTableRow
me1200UdldConfigInterfaceParamEntry=_Me1200UdldConfigInterfaceParamEntry_Object((1,3,6,1,4,1,9,9,815,1,123,1,2,1,1,1))
me1200UdldConfigInterfaceParamEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:me1200UdldConfigInterfaceParamEntry.setStatus(_A)
_Me1200UdldConfigInterfaceParamIfIndex_Type=ME1200InterfaceIndex
_Me1200UdldConfigInterfaceParamIfIndex_Object=MibTableColumn
me1200UdldConfigInterfaceParamIfIndex=_Me1200UdldConfigInterfaceParamIfIndex_Object((1,3,6,1,4,1,9,9,815,1,123,1,2,1,1,1,1),_Me1200UdldConfigInterfaceParamIfIndex_Type())
me1200UdldConfigInterfaceParamIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200UdldConfigInterfaceParamIfIndex.setStatus(_A)
_Me1200UdldConfigInterfaceParamUdldMode_Type=ME1200UdldMode
_Me1200UdldConfigInterfaceParamUdldMode_Object=MibTableColumn
me1200UdldConfigInterfaceParamUdldMode=_Me1200UdldConfigInterfaceParamUdldMode_Object((1,3,6,1,4,1,9,9,815,1,123,1,2,1,1,1,2),_Me1200UdldConfigInterfaceParamUdldMode_Type())
me1200UdldConfigInterfaceParamUdldMode.setMaxAccess(_H)
if mibBuilder.loadTexts:me1200UdldConfigInterfaceParamUdldMode.setStatus(_A)
class _Me1200UdldConfigInterfaceParamProbeMsgInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,90))
_Me1200UdldConfigInterfaceParamProbeMsgInterval_Type.__name__=_F
_Me1200UdldConfigInterfaceParamProbeMsgInterval_Object=MibTableColumn
me1200UdldConfigInterfaceParamProbeMsgInterval=_Me1200UdldConfigInterfaceParamProbeMsgInterval_Object((1,3,6,1,4,1,9,9,815,1,123,1,2,1,1,1,3),_Me1200UdldConfigInterfaceParamProbeMsgInterval_Type())
me1200UdldConfigInterfaceParamProbeMsgInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:me1200UdldConfigInterfaceParamProbeMsgInterval.setStatus(_A)
_Me1200UdldStatus_ObjectIdentity=ObjectIdentity
me1200UdldStatus=_Me1200UdldStatus_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,123,1,3))
_Me1200UdldStatusInterface_ObjectIdentity=ObjectIdentity
me1200UdldStatusInterface=_Me1200UdldStatusInterface_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,123,1,3,1))
_Me1200UdldStatusInterfaceTable_Object=MibTable
me1200UdldStatusInterfaceTable=_Me1200UdldStatusInterfaceTable_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,1))
if mibBuilder.loadTexts:me1200UdldStatusInterfaceTable.setStatus(_A)
_Me1200UdldStatusInterfaceEntry_Object=MibTableRow
me1200UdldStatusInterfaceEntry=_Me1200UdldStatusInterfaceEntry_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,1,1))
me1200UdldStatusInterfaceEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:me1200UdldStatusInterfaceEntry.setStatus(_A)
_Me1200UdldStatusInterfaceIfIndex_Type=ME1200InterfaceIndex
_Me1200UdldStatusInterfaceIfIndex_Object=MibTableColumn
me1200UdldStatusInterfaceIfIndex=_Me1200UdldStatusInterfaceIfIndex_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,1,1,1),_Me1200UdldStatusInterfaceIfIndex_Type())
me1200UdldStatusInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200UdldStatusInterfaceIfIndex.setStatus(_A)
class _Me1200UdldStatusInterfaceDeviceID_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_Me1200UdldStatusInterfaceDeviceID_Type.__name__=_D
_Me1200UdldStatusInterfaceDeviceID_Object=MibTableColumn
me1200UdldStatusInterfaceDeviceID=_Me1200UdldStatusInterfaceDeviceID_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,1,1,2),_Me1200UdldStatusInterfaceDeviceID_Type())
me1200UdldStatusInterfaceDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UdldStatusInterfaceDeviceID.setStatus(_A)
class _Me1200UdldStatusInterfaceDeviceName_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_Me1200UdldStatusInterfaceDeviceName_Type.__name__=_D
_Me1200UdldStatusInterfaceDeviceName_Object=MibTableColumn
me1200UdldStatusInterfaceDeviceName=_Me1200UdldStatusInterfaceDeviceName_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,1,1,3),_Me1200UdldStatusInterfaceDeviceName_Type())
me1200UdldStatusInterfaceDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UdldStatusInterfaceDeviceName.setStatus(_A)
_Me1200UdldStatusInterfaceLinkState_Type=ME1200UdldDetectionState
_Me1200UdldStatusInterfaceLinkState_Object=MibTableColumn
me1200UdldStatusInterfaceLinkState=_Me1200UdldStatusInterfaceLinkState_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,1,1,4),_Me1200UdldStatusInterfaceLinkState_Type())
me1200UdldStatusInterfaceLinkState.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UdldStatusInterfaceLinkState.setStatus(_A)
_Me1200UdldStatusInterfaceNeighborTable_Object=MibTable
me1200UdldStatusInterfaceNeighborTable=_Me1200UdldStatusInterfaceNeighborTable_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,2))
if mibBuilder.loadTexts:me1200UdldStatusInterfaceNeighborTable.setStatus(_A)
_Me1200UdldStatusInterfaceNeighborEntry_Object=MibTableRow
me1200UdldStatusInterfaceNeighborEntry=_Me1200UdldStatusInterfaceNeighborEntry_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,2,1))
me1200UdldStatusInterfaceNeighborEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:me1200UdldStatusInterfaceNeighborEntry.setStatus(_A)
_Me1200UdldStatusInterfaceNeighborIfIndex_Type=ME1200InterfaceIndex
_Me1200UdldStatusInterfaceNeighborIfIndex_Object=MibTableColumn
me1200UdldStatusInterfaceNeighborIfIndex=_Me1200UdldStatusInterfaceNeighborIfIndex_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,2,1,1),_Me1200UdldStatusInterfaceNeighborIfIndex_Type())
me1200UdldStatusInterfaceNeighborIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200UdldStatusInterfaceNeighborIfIndex.setStatus(_A)
class _Me1200UdldStatusInterfaceNeighborNeighborDeviceID_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_Me1200UdldStatusInterfaceNeighborNeighborDeviceID_Type.__name__=_D
_Me1200UdldStatusInterfaceNeighborNeighborDeviceID_Object=MibTableColumn
me1200UdldStatusInterfaceNeighborNeighborDeviceID=_Me1200UdldStatusInterfaceNeighborNeighborDeviceID_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,2,1,2),_Me1200UdldStatusInterfaceNeighborNeighborDeviceID_Type())
me1200UdldStatusInterfaceNeighborNeighborDeviceID.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UdldStatusInterfaceNeighborNeighborDeviceID.setStatus(_A)
class _Me1200UdldStatusInterfaceNeighborNeighborPortID_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_Me1200UdldStatusInterfaceNeighborNeighborPortID_Type.__name__=_D
_Me1200UdldStatusInterfaceNeighborNeighborPortID_Object=MibTableColumn
me1200UdldStatusInterfaceNeighborNeighborPortID=_Me1200UdldStatusInterfaceNeighborNeighborPortID_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,2,1,3),_Me1200UdldStatusInterfaceNeighborNeighborPortID_Type())
me1200UdldStatusInterfaceNeighborNeighborPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UdldStatusInterfaceNeighborNeighborPortID.setStatus(_A)
class _Me1200UdldStatusInterfaceNeighborNeighborDeviceName_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_Me1200UdldStatusInterfaceNeighborNeighborDeviceName_Type.__name__=_D
_Me1200UdldStatusInterfaceNeighborNeighborDeviceName_Object=MibTableColumn
me1200UdldStatusInterfaceNeighborNeighborDeviceName=_Me1200UdldStatusInterfaceNeighborNeighborDeviceName_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,2,1,4),_Me1200UdldStatusInterfaceNeighborNeighborDeviceName_Type())
me1200UdldStatusInterfaceNeighborNeighborDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UdldStatusInterfaceNeighborNeighborDeviceName.setStatus(_A)
_Me1200UdldStatusInterfaceNeighborLinkDetectionState_Type=ME1200UdldDetectionState
_Me1200UdldStatusInterfaceNeighborLinkDetectionState_Object=MibTableColumn
me1200UdldStatusInterfaceNeighborLinkDetectionState=_Me1200UdldStatusInterfaceNeighborLinkDetectionState_Object((1,3,6,1,4,1,9,9,815,1,123,1,3,1,2,1,5),_Me1200UdldStatusInterfaceNeighborLinkDetectionState_Type())
me1200UdldStatusInterfaceNeighborLinkDetectionState.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200UdldStatusInterfaceNeighborLinkDetectionState.setStatus(_A)
_Me1200UdldMibConformance_ObjectIdentity=ObjectIdentity
me1200UdldMibConformance=_Me1200UdldMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,123,2))
_Me1200UdldMibCompliances_ObjectIdentity=ObjectIdentity
me1200UdldMibCompliances=_Me1200UdldMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,123,2,1))
_Me1200UdldMibGroups_ObjectIdentity=ObjectIdentity
me1200UdldMibGroups=_Me1200UdldMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,123,2,2))
me1200UdldConfigInterfaceParamTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,123,2,2,1))
me1200UdldConfigInterfaceParamTableInfoGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:me1200UdldConfigInterfaceParamTableInfoGroup.setStatus(_A)
me1200UdldStatusInterfaceTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,123,2,2,2))
me1200UdldStatusInterfaceTableInfoGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:me1200UdldStatusInterfaceTableInfoGroup.setStatus(_A)
me1200UdldStatusInterfaceNeighborTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,123,2,2,3))
me1200UdldStatusInterfaceNeighborTableInfoGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:me1200UdldStatusInterfaceNeighborTableInfoGroup.setStatus(_A)
me1200UdldMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,123,2,1,1))
me1200UdldMibCompliance.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:me1200UdldMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ME1200UdldDetectionState':ME1200UdldDetectionState,'ME1200UdldMode':ME1200UdldMode,'me1200UdldMib':me1200UdldMib,'me1200UdldMibObjects':me1200UdldMibObjects,'me1200UdldConfig':me1200UdldConfig,'me1200UdldConfigInterface':me1200UdldConfigInterface,'me1200UdldConfigInterfaceParamTable':me1200UdldConfigInterfaceParamTable,'me1200UdldConfigInterfaceParamEntry':me1200UdldConfigInterfaceParamEntry,_G:me1200UdldConfigInterfaceParamIfIndex,_K:me1200UdldConfigInterfaceParamUdldMode,_L:me1200UdldConfigInterfaceParamProbeMsgInterval,'me1200UdldStatus':me1200UdldStatus,'me1200UdldStatusInterface':me1200UdldStatusInterface,'me1200UdldStatusInterfaceTable':me1200UdldStatusInterfaceTable,'me1200UdldStatusInterfaceEntry':me1200UdldStatusInterfaceEntry,_I:me1200UdldStatusInterfaceIfIndex,_M:me1200UdldStatusInterfaceDeviceID,_N:me1200UdldStatusInterfaceDeviceName,_O:me1200UdldStatusInterfaceLinkState,'me1200UdldStatusInterfaceNeighborTable':me1200UdldStatusInterfaceNeighborTable,'me1200UdldStatusInterfaceNeighborEntry':me1200UdldStatusInterfaceNeighborEntry,_J:me1200UdldStatusInterfaceNeighborIfIndex,_P:me1200UdldStatusInterfaceNeighborNeighborDeviceID,_Q:me1200UdldStatusInterfaceNeighborNeighborPortID,_R:me1200UdldStatusInterfaceNeighborNeighborDeviceName,_S:me1200UdldStatusInterfaceNeighborLinkDetectionState,'me1200UdldMibConformance':me1200UdldMibConformance,'me1200UdldMibCompliances':me1200UdldMibCompliances,'me1200UdldMibCompliance':me1200UdldMibCompliance,'me1200UdldMibGroups':me1200UdldMibGroups,_T:me1200UdldConfigInterfaceParamTableInfoGroup,_U:me1200UdldStatusInterfaceTableInfoGroup,_V:me1200UdldStatusInterfaceNeighborTableInfoGroup})