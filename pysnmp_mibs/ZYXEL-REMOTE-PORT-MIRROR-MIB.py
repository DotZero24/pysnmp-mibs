_E='zyRemotePortMirrorVid'
_D='ZYXEL-REMOTE-PORT-MIRROR-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelRemotePortMirror=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,73))
_ZyxelRemotePortMirrorSetup_ObjectIdentity=ObjectIdentity
zyxelRemotePortMirrorSetup=_ZyxelRemotePortMirrorSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,73,1))
_ZyRemotePortMirrorMaxNumberOfVlans_Type=Integer32
_ZyRemotePortMirrorMaxNumberOfVlans_Object=MibScalar
zyRemotePortMirrorMaxNumberOfVlans=_ZyRemotePortMirrorMaxNumberOfVlans_Object((1,3,6,1,4,1,890,1,15,3,73,1,1),_ZyRemotePortMirrorMaxNumberOfVlans_Type())
zyRemotePortMirrorMaxNumberOfVlans.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyRemotePortMirrorMaxNumberOfVlans.setStatus(_A)
_ZyxelRemotePortMirrorTable_Object=MibTable
zyxelRemotePortMirrorTable=_ZyxelRemotePortMirrorTable_Object((1,3,6,1,4,1,890,1,15,3,73,1,2))
if mibBuilder.loadTexts:zyxelRemotePortMirrorTable.setStatus(_A)
_ZyxelRemotePortMirrorEntry_Object=MibTableRow
zyxelRemotePortMirrorEntry=_ZyxelRemotePortMirrorEntry_Object((1,3,6,1,4,1,890,1,15,3,73,1,2,1))
zyxelRemotePortMirrorEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelRemotePortMirrorEntry.setStatus(_A)
class _ZyRemotePortMirrorVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyRemotePortMirrorVid_Type.__name__=_C
_ZyRemotePortMirrorVid_Object=MibTableColumn
zyRemotePortMirrorVid=_ZyRemotePortMirrorVid_Object((1,3,6,1,4,1,890,1,15,3,73,1,2,1,1),_ZyRemotePortMirrorVid_Type())
zyRemotePortMirrorVid.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyRemotePortMirrorVid.setStatus(_A)
class _ZyRemotePortMirrorSource8021pPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZyRemotePortMirrorSource8021pPriority_Type.__name__=_C
_ZyRemotePortMirrorSource8021pPriority_Object=MibTableColumn
zyRemotePortMirrorSource8021pPriority=_ZyRemotePortMirrorSource8021pPriority_Object((1,3,6,1,4,1,890,1,15,3,73,1,2,1,2),_ZyRemotePortMirrorSource8021pPriority_Type())
zyRemotePortMirrorSource8021pPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRemotePortMirrorSource8021pPriority.setStatus(_A)
_ZyRemotePortMirrorSourceIngressMirrorPorts_Type=PortList
_ZyRemotePortMirrorSourceIngressMirrorPorts_Object=MibTableColumn
zyRemotePortMirrorSourceIngressMirrorPorts=_ZyRemotePortMirrorSourceIngressMirrorPorts_Object((1,3,6,1,4,1,890,1,15,3,73,1,2,1,3),_ZyRemotePortMirrorSourceIngressMirrorPorts_Type())
zyRemotePortMirrorSourceIngressMirrorPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRemotePortMirrorSourceIngressMirrorPorts.setStatus(_A)
_ZyRemotePortMirrorSourceEgressMirrorPorts_Type=PortList
_ZyRemotePortMirrorSourceEgressMirrorPorts_Object=MibTableColumn
zyRemotePortMirrorSourceEgressMirrorPorts=_ZyRemotePortMirrorSourceEgressMirrorPorts_Object((1,3,6,1,4,1,890,1,15,3,73,1,2,1,4),_ZyRemotePortMirrorSourceEgressMirrorPorts_Type())
zyRemotePortMirrorSourceEgressMirrorPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRemotePortMirrorSourceEgressMirrorPorts.setStatus(_A)
_ZyRemotePortMirrorSourceReflectorPortState_Type=EnabledStatus
_ZyRemotePortMirrorSourceReflectorPortState_Object=MibTableColumn
zyRemotePortMirrorSourceReflectorPortState=_ZyRemotePortMirrorSourceReflectorPortState_Object((1,3,6,1,4,1,890,1,15,3,73,1,2,1,5),_ZyRemotePortMirrorSourceReflectorPortState_Type())
zyRemotePortMirrorSourceReflectorPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRemotePortMirrorSourceReflectorPortState.setStatus(_A)
_ZyRemotePortMirrorSourceReflectorPort_Type=Integer32
_ZyRemotePortMirrorSourceReflectorPort_Object=MibTableColumn
zyRemotePortMirrorSourceReflectorPort=_ZyRemotePortMirrorSourceReflectorPort_Object((1,3,6,1,4,1,890,1,15,3,73,1,2,1,6),_ZyRemotePortMirrorSourceReflectorPort_Type())
zyRemotePortMirrorSourceReflectorPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRemotePortMirrorSourceReflectorPort.setStatus(_A)
_ZyRemotePortMirrorDestinationMonitorPort_Type=Integer32
_ZyRemotePortMirrorDestinationMonitorPort_Object=MibTableColumn
zyRemotePortMirrorDestinationMonitorPort=_ZyRemotePortMirrorDestinationMonitorPort_Object((1,3,6,1,4,1,890,1,15,3,73,1,2,1,7),_ZyRemotePortMirrorDestinationMonitorPort_Type())
zyRemotePortMirrorDestinationMonitorPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRemotePortMirrorDestinationMonitorPort.setStatus(_A)
_ZyRemotePortMirrorDestinationMonitorPortTagging_Type=EnabledStatus
_ZyRemotePortMirrorDestinationMonitorPortTagging_Object=MibTableColumn
zyRemotePortMirrorDestinationMonitorPortTagging=_ZyRemotePortMirrorDestinationMonitorPortTagging_Object((1,3,6,1,4,1,890,1,15,3,73,1,2,1,8),_ZyRemotePortMirrorDestinationMonitorPortTagging_Type())
zyRemotePortMirrorDestinationMonitorPortTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRemotePortMirrorDestinationMonitorPortTagging.setStatus(_A)
_ZyRemotePortMirrorConnectedPorts_Type=PortList
_ZyRemotePortMirrorConnectedPorts_Object=MibTableColumn
zyRemotePortMirrorConnectedPorts=_ZyRemotePortMirrorConnectedPorts_Object((1,3,6,1,4,1,890,1,15,3,73,1,2,1,9),_ZyRemotePortMirrorConnectedPorts_Type())
zyRemotePortMirrorConnectedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:zyRemotePortMirrorConnectedPorts.setStatus(_A)
_ZyRemotePortMirrorRowStatus_Type=RowStatus
_ZyRemotePortMirrorRowStatus_Object=MibTableColumn
zyRemotePortMirrorRowStatus=_ZyRemotePortMirrorRowStatus_Object((1,3,6,1,4,1,890,1,15,3,73,1,2,1,10),_ZyRemotePortMirrorRowStatus_Type())
zyRemotePortMirrorRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyRemotePortMirrorRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelRemotePortMirror':zyxelRemotePortMirror,'zyxelRemotePortMirrorSetup':zyxelRemotePortMirrorSetup,'zyRemotePortMirrorMaxNumberOfVlans':zyRemotePortMirrorMaxNumberOfVlans,'zyxelRemotePortMirrorTable':zyxelRemotePortMirrorTable,'zyxelRemotePortMirrorEntry':zyxelRemotePortMirrorEntry,_E:zyRemotePortMirrorVid,'zyRemotePortMirrorSource8021pPriority':zyRemotePortMirrorSource8021pPriority,'zyRemotePortMirrorSourceIngressMirrorPorts':zyRemotePortMirrorSourceIngressMirrorPorts,'zyRemotePortMirrorSourceEgressMirrorPorts':zyRemotePortMirrorSourceEgressMirrorPorts,'zyRemotePortMirrorSourceReflectorPortState':zyRemotePortMirrorSourceReflectorPortState,'zyRemotePortMirrorSourceReflectorPort':zyRemotePortMirrorSourceReflectorPort,'zyRemotePortMirrorDestinationMonitorPort':zyRemotePortMirrorDestinationMonitorPort,'zyRemotePortMirrorDestinationMonitorPortTagging':zyRemotePortMirrorDestinationMonitorPortTagging,'zyRemotePortMirrorConnectedPorts':zyRemotePortMirrorConnectedPorts,'zyRemotePortMirrorRowStatus':zyRemotePortMirrorRowStatus})