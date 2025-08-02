_H='swVLANCounterLevel'
_G='swVLANCounterPktType'
_F='swVLANCounterPort'
_E='swVLANCounterVID'
_D='Integer32'
_C='read-only'
_B='VLAN-COUNTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
swVLANCounterMIB=ModuleIdentity((1,3,6,1,4,1,171,12,65))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwVLANCounterCtrl_ObjectIdentity=ObjectIdentity
swVLANCounterCtrl=_SwVLANCounterCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,65,1))
_SwVLANCounterInfo_ObjectIdentity=ObjectIdentity
swVLANCounterInfo=_SwVLANCounterInfo_ObjectIdentity((1,3,6,1,4,1,171,12,65,2))
_SwVLANCounterMgmt_ObjectIdentity=ObjectIdentity
swVLANCounterMgmt=_SwVLANCounterMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,65,3))
_SwVLANCounterTable_Object=MibTable
swVLANCounterTable=_SwVLANCounterTable_Object((1,3,6,1,4,1,171,12,65,3,1))
if mibBuilder.loadTexts:swVLANCounterTable.setStatus(_A)
_SwVLANCounterEntry_Object=MibTableRow
swVLANCounterEntry=_SwVLANCounterEntry_Object((1,3,6,1,4,1,171,12,65,3,1,1))
swVLANCounterEntry.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:swVLANCounterEntry.setStatus(_A)
_SwVLANCounterVID_Type=Integer32
_SwVLANCounterVID_Object=MibTableColumn
swVLANCounterVID=_SwVLANCounterVID_Object((1,3,6,1,4,1,171,12,65,3,1,1,1),_SwVLANCounterVID_Type())
swVLANCounterVID.setMaxAccess(_C)
if mibBuilder.loadTexts:swVLANCounterVID.setStatus(_A)
class _SwVLANCounterPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwVLANCounterPort_Type.__name__=_D
_SwVLANCounterPort_Object=MibTableColumn
swVLANCounterPort=_SwVLANCounterPort_Object((1,3,6,1,4,1,171,12,65,3,1,1,2),_SwVLANCounterPort_Type())
swVLANCounterPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swVLANCounterPort.setStatus(_A)
class _SwVLANCounterPktType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('broadcast',1),('multicast',2),('unicast',3),('all_frame',4)))
_SwVLANCounterPktType_Type.__name__=_D
_SwVLANCounterPktType_Object=MibTableColumn
swVLANCounterPktType=_SwVLANCounterPktType_Object((1,3,6,1,4,1,171,12,65,3,1,1,3),_SwVLANCounterPktType_Type())
swVLANCounterPktType.setMaxAccess(_C)
if mibBuilder.loadTexts:swVLANCounterPktType.setStatus(_A)
class _SwVLANCounterLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('packet',1),('byte',2)))
_SwVLANCounterLevel_Type.__name__=_D
_SwVLANCounterLevel_Object=MibTableColumn
swVLANCounterLevel=_SwVLANCounterLevel_Object((1,3,6,1,4,1,171,12,65,3,1,1,4),_SwVLANCounterLevel_Type())
swVLANCounterLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:swVLANCounterLevel.setStatus(_A)
_SwVLANCounterTotalStats_Type=Counter64
_SwVLANCounterTotalStats_Object=MibTableColumn
swVLANCounterTotalStats=_SwVLANCounterTotalStats_Object((1,3,6,1,4,1,171,12,65,3,1,1,5),_SwVLANCounterTotalStats_Type())
swVLANCounterTotalStats.setMaxAccess(_C)
if mibBuilder.loadTexts:swVLANCounterTotalStats.setStatus(_A)
_SwVLANCounterRateStats_Type=Counter64
_SwVLANCounterRateStats_Object=MibTableColumn
swVLANCounterRateStats=_SwVLANCounterRateStats_Object((1,3,6,1,4,1,171,12,65,3,1,1,6),_SwVLANCounterRateStats_Type())
swVLANCounterRateStats.setMaxAccess(_C)
if mibBuilder.loadTexts:swVLANCounterRateStats.setStatus(_A)
_SwVLANCounterRowStatus_Type=RowStatus
_SwVLANCounterRowStatus_Object=MibTableColumn
swVLANCounterRowStatus=_SwVLANCounterRowStatus_Object((1,3,6,1,4,1,171,12,65,3,1,1,7),_SwVLANCounterRowStatus_Type())
swVLANCounterRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:swVLANCounterRowStatus.setStatus(_A)
_SwVLANCounterClearTable_Object=MibTable
swVLANCounterClearTable=_SwVLANCounterClearTable_Object((1,3,6,1,4,1,171,12,65,3,2))
if mibBuilder.loadTexts:swVLANCounterClearTable.setStatus(_A)
_SwVLANCounterClearEntry_Object=MibTableRow
swVLANCounterClearEntry=_SwVLANCounterClearEntry_Object((1,3,6,1,4,1,171,12,65,3,2,1))
swVLANCounterClearEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:swVLANCounterClearEntry.setStatus(_A)
class _SwVLANCounterClearAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('start',2)))
_SwVLANCounterClearAction_Type.__name__=_D
_SwVLANCounterClearAction_Object=MibTableColumn
swVLANCounterClearAction=_SwVLANCounterClearAction_Object((1,3,6,1,4,1,171,12,65,3,2,1,1),_SwVLANCounterClearAction_Type())
swVLANCounterClearAction.setMaxAccess('read-write')
if mibBuilder.loadTexts:swVLANCounterClearAction.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PortList':PortList,'swVLANCounterMIB':swVLANCounterMIB,'swVLANCounterCtrl':swVLANCounterCtrl,'swVLANCounterInfo':swVLANCounterInfo,'swVLANCounterMgmt':swVLANCounterMgmt,'swVLANCounterTable':swVLANCounterTable,'swVLANCounterEntry':swVLANCounterEntry,_E:swVLANCounterVID,_F:swVLANCounterPort,_G:swVLANCounterPktType,_H:swVLANCounterLevel,'swVLANCounterTotalStats':swVLANCounterTotalStats,'swVLANCounterRateStats':swVLANCounterRateStats,'swVLANCounterRowStatus':swVLANCounterRowStatus,'swVLANCounterClearTable':swVLANCounterClearTable,'swVLANCounterClearEntry':swVLANCounterClearEntry,'swVLANCounterClearAction':swVLANCounterClearAction})