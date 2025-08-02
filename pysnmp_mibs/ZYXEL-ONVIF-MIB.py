_E='zyOnvifVlanVid'
_D='ZYXEL-ONVIF-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelOnvif=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,123))
_ZyxelOnvifSetup_ObjectIdentity=ObjectIdentity
zyxelOnvifSetup=_ZyxelOnvifSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,123,1))
_ZyOnvifState_Type=EnabledStatus
_ZyOnvifState_Object=MibScalar
zyOnvifState=_ZyOnvifState_Object((1,3,6,1,4,1,890,1,15,3,123,1,1),_ZyOnvifState_Type())
zyOnvifState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyOnvifState.setStatus(_A)
_ZyOnvifMaxNumberOfVlans_Type=Integer32
_ZyOnvifMaxNumberOfVlans_Object=MibScalar
zyOnvifMaxNumberOfVlans=_ZyOnvifMaxNumberOfVlans_Object((1,3,6,1,4,1,890,1,15,3,123,1,2),_ZyOnvifMaxNumberOfVlans_Type())
zyOnvifMaxNumberOfVlans.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyOnvifMaxNumberOfVlans.setStatus(_A)
_ZyxelOnvifVlanTable_Object=MibTable
zyxelOnvifVlanTable=_ZyxelOnvifVlanTable_Object((1,3,6,1,4,1,890,1,15,3,123,1,3))
if mibBuilder.loadTexts:zyxelOnvifVlanTable.setStatus(_A)
_ZyxelOnvifVlanEntry_Object=MibTableRow
zyxelOnvifVlanEntry=_ZyxelOnvifVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,123,1,3,1))
zyxelOnvifVlanEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelOnvifVlanEntry.setStatus(_A)
class _ZyOnvifVlanVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyOnvifVlanVid_Type.__name__=_B
_ZyOnvifVlanVid_Object=MibTableColumn
zyOnvifVlanVid=_ZyOnvifVlanVid_Object((1,3,6,1,4,1,890,1,15,3,123,1,3,1,1),_ZyOnvifVlanVid_Type())
zyOnvifVlanVid.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyOnvifVlanVid.setStatus(_A)
_ZyOnvifVlanPorts_Type=PortList
_ZyOnvifVlanPorts_Object=MibTableColumn
zyOnvifVlanPorts=_ZyOnvifVlanPorts_Object((1,3,6,1,4,1,890,1,15,3,123,1,3,1,2),_ZyOnvifVlanPorts_Type())
zyOnvifVlanPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:zyOnvifVlanPorts.setStatus(_A)
_ZyOnvifVlanRowStatus_Type=RowStatus
_ZyOnvifVlanRowStatus_Object=MibTableColumn
zyOnvifVlanRowStatus=_ZyOnvifVlanRowStatus_Object((1,3,6,1,4,1,890,1,15,3,123,1,3,1,3),_ZyOnvifVlanRowStatus_Type())
zyOnvifVlanRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyOnvifVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelOnvif':zyxelOnvif,'zyxelOnvifSetup':zyxelOnvifSetup,'zyOnvifState':zyOnvifState,'zyOnvifMaxNumberOfVlans':zyOnvifMaxNumberOfVlans,'zyxelOnvifVlanTable':zyxelOnvifVlanTable,'zyxelOnvifVlanEntry':zyxelOnvifVlanEntry,_E:zyOnvifVlanVid,'zyOnvifVlanPorts':zyOnvifVlanPorts,'zyOnvifVlanRowStatus':zyOnvifVlanRowStatus})