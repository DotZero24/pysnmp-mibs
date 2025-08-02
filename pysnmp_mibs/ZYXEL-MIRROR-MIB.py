_E='Integer32'
_D='dot1dBasePort'
_C='BRIDGE-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_C,_D)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelMirror=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,65))
_ZyxelMirrorSetup_ObjectIdentity=ObjectIdentity
zyxelMirrorSetup=_ZyxelMirrorSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,65,1))
_ZyMirrorState_Type=EnabledStatus
_ZyMirrorState_Object=MibScalar
zyMirrorState=_ZyMirrorState_Object((1,3,6,1,4,1,890,1,15,3,65,1,1),_ZyMirrorState_Type())
zyMirrorState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMirrorState.setStatus(_A)
_ZyMirrorMonitorPort_Type=Integer32
_ZyMirrorMonitorPort_Object=MibScalar
zyMirrorMonitorPort=_ZyMirrorMonitorPort_Object((1,3,6,1,4,1,890,1,15,3,65,1,2),_ZyMirrorMonitorPort_Type())
zyMirrorMonitorPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMirrorMonitorPort.setStatus(_A)
_ZyxelMirrorTable_Object=MibTable
zyxelMirrorTable=_ZyxelMirrorTable_Object((1,3,6,1,4,1,890,1,15,3,65,1,3))
if mibBuilder.loadTexts:zyxelMirrorTable.setStatus(_A)
_ZyxelMirrorEntry_Object=MibTableRow
zyxelMirrorEntry=_ZyxelMirrorEntry_Object((1,3,6,1,4,1,890,1,15,3,65,1,3,1))
zyxelMirrorEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelMirrorEntry.setStatus(_A)
_ZyMirrorMirroredState_Type=EnabledStatus
_ZyMirrorMirroredState_Object=MibTableColumn
zyMirrorMirroredState=_ZyMirrorMirroredState_Object((1,3,6,1,4,1,890,1,15,3,65,1,3,1,1),_ZyMirrorMirroredState_Type())
zyMirrorMirroredState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMirrorMirroredState.setStatus(_A)
class _ZyMirrorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ingress',0),('egress',1),('both',2)))
_ZyMirrorDirection_Type.__name__=_E
_ZyMirrorDirection_Object=MibTableColumn
zyMirrorDirection=_ZyMirrorDirection_Object((1,3,6,1,4,1,890,1,15,3,65,1,3,1,2),_ZyMirrorDirection_Type())
zyMirrorDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMirrorDirection.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-MIRROR-MIB',**{'zyxelMirror':zyxelMirror,'zyxelMirrorSetup':zyxelMirrorSetup,'zyMirrorState':zyMirrorState,'zyMirrorMonitorPort':zyMirrorMonitorPort,'zyxelMirrorTable':zyxelMirrorTable,'zyxelMirrorEntry':zyxelMirrorEntry,'zyMirrorMirroredState':zyMirrorMirroredState,'zyMirrorDirection':zyMirrorDirection})