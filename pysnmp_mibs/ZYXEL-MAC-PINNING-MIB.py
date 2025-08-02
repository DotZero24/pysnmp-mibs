_D='read-write'
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
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelMacPinning=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,92))
_ZyxelMacPinningSetup_ObjectIdentity=ObjectIdentity
zyxelMacPinningSetup=_ZyxelMacPinningSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,92,1))
_ZyMacPinningState_Type=EnabledStatus
_ZyMacPinningState_Object=MibScalar
zyMacPinningState=_ZyMacPinningState_Object((1,3,6,1,4,1,890,1,15,3,92,1,1),_ZyMacPinningState_Type())
zyMacPinningState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyMacPinningState.setStatus(_A)
_ZyxelMacPinningPortTable_Object=MibTable
zyxelMacPinningPortTable=_ZyxelMacPinningPortTable_Object((1,3,6,1,4,1,890,1,15,3,92,1,2))
if mibBuilder.loadTexts:zyxelMacPinningPortTable.setStatus(_A)
_ZyxelMacPinningPortEntry_Object=MibTableRow
zyxelMacPinningPortEntry=_ZyxelMacPinningPortEntry_Object((1,3,6,1,4,1,890,1,15,3,92,1,2,1))
zyxelMacPinningPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelMacPinningPortEntry.setStatus(_A)
_ZyMacPinningPortState_Type=EnabledStatus
_ZyMacPinningPortState_Object=MibTableColumn
zyMacPinningPortState=_ZyMacPinningPortState_Object((1,3,6,1,4,1,890,1,15,3,92,1,2,1,1),_ZyMacPinningPortState_Type())
zyMacPinningPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyMacPinningPortState.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-MAC-PINNING-MIB',**{'zyxelMacPinning':zyxelMacPinning,'zyxelMacPinningSetup':zyxelMacPinningSetup,'zyMacPinningState':zyMacPinningState,'zyxelMacPinningPortTable':zyxelMacPinningPortTable,'zyxelMacPinningPortEntry':zyxelMacPinningPortEntry,'zyMacPinningPortState':zyMacPinningPortState})