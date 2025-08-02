_E='read-write'
_D='Integer32'
_C='dot1dBasePort'
_B='BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_B,_C)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelBpduGuard=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,104))
_ZyxelBpduGuardSetup_ObjectIdentity=ObjectIdentity
zyxelBpduGuardSetup=_ZyxelBpduGuardSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,104,1))
_ZyBpduGuardState_Type=EnabledStatus
_ZyBpduGuardState_Object=MibScalar
zyBpduGuardState=_ZyBpduGuardState_Object((1,3,6,1,4,1,890,1,15,3,104,1,1),_ZyBpduGuardState_Type())
zyBpduGuardState.setMaxAccess(_E)
if mibBuilder.loadTexts:zyBpduGuardState.setStatus(_A)
_ZyxelBpduGuardPortTable_Object=MibTable
zyxelBpduGuardPortTable=_ZyxelBpduGuardPortTable_Object((1,3,6,1,4,1,890,1,15,3,104,1,2))
if mibBuilder.loadTexts:zyxelBpduGuardPortTable.setStatus(_A)
_ZyxelBpduGuardPortEntry_Object=MibTableRow
zyxelBpduGuardPortEntry=_ZyxelBpduGuardPortEntry_Object((1,3,6,1,4,1,890,1,15,3,104,1,2,1))
zyxelBpduGuardPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelBpduGuardPortEntry.setStatus(_A)
_ZyBpduGuardPortState_Type=EnabledStatus
_ZyBpduGuardPortState_Object=MibTableColumn
zyBpduGuardPortState=_ZyBpduGuardPortState_Object((1,3,6,1,4,1,890,1,15,3,104,1,2,1,1),_ZyBpduGuardPortState_Type())
zyBpduGuardPortState.setMaxAccess(_E)
if mibBuilder.loadTexts:zyBpduGuardPortState.setStatus(_A)
_ZyxelBpduGuardStatus_ObjectIdentity=ObjectIdentity
zyxelBpduGuardStatus=_ZyxelBpduGuardStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,104,2))
_ZyxelBpduGuardPortInfoTable_Object=MibTable
zyxelBpduGuardPortInfoTable=_ZyxelBpduGuardPortInfoTable_Object((1,3,6,1,4,1,890,1,15,3,104,2,1))
if mibBuilder.loadTexts:zyxelBpduGuardPortInfoTable.setStatus(_A)
_ZyxelBpduGuardPortInfoEntry_Object=MibTableRow
zyxelBpduGuardPortInfoEntry=_ZyxelBpduGuardPortInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,104,2,1,1))
zyxelBpduGuardPortInfoEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelBpduGuardPortInfoEntry.setStatus(_A)
class _ZyBpduGuardPortInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forwarding',1),('err-disable',2)))
_ZyBpduGuardPortInfoStatus_Type.__name__=_D
_ZyBpduGuardPortInfoStatus_Object=MibTableColumn
zyBpduGuardPortInfoStatus=_ZyBpduGuardPortInfoStatus_Object((1,3,6,1,4,1,890,1,15,3,104,2,1,1,1),_ZyBpduGuardPortInfoStatus_Type())
zyBpduGuardPortInfoStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyBpduGuardPortInfoStatus.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-BPDU-GUARD-MIB',**{'zyxelBpduGuard':zyxelBpduGuard,'zyxelBpduGuardSetup':zyxelBpduGuardSetup,'zyBpduGuardState':zyBpduGuardState,'zyxelBpduGuardPortTable':zyxelBpduGuardPortTable,'zyxelBpduGuardPortEntry':zyxelBpduGuardPortEntry,'zyBpduGuardPortState':zyBpduGuardPortState,'zyxelBpduGuardStatus':zyxelBpduGuardStatus,'zyxelBpduGuardPortInfoTable':zyxelBpduGuardPortInfoTable,'zyxelBpduGuardPortInfoEntry':zyxelBpduGuardPortInfoEntry,'zyBpduGuardPortInfoStatus':zyBpduGuardPortInfoStatus})