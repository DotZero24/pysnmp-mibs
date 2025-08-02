_D='read-write'
_C='dot1dBasePort'
_B='BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_B,_C)
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelDoSPrevention=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,119))
_ZyxelDoSPreventionSetup_ObjectIdentity=ObjectIdentity
zyxelDoSPreventionSetup=_ZyxelDoSPreventionSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,119,1))
_ZyDoSPreventionState_Type=EnabledStatus
_ZyDoSPreventionState_Object=MibScalar
zyDoSPreventionState=_ZyDoSPreventionState_Object((1,3,6,1,4,1,890,1,15,3,119,1,1),_ZyDoSPreventionState_Type())
zyDoSPreventionState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyDoSPreventionState.setStatus(_A)
_ZyxelDoSPreventionPortTable_Object=MibTable
zyxelDoSPreventionPortTable=_ZyxelDoSPreventionPortTable_Object((1,3,6,1,4,1,890,1,15,3,119,1,2))
if mibBuilder.loadTexts:zyxelDoSPreventionPortTable.setStatus(_A)
_ZyxelDoSPreventionPortEntry_Object=MibTableRow
zyxelDoSPreventionPortEntry=_ZyxelDoSPreventionPortEntry_Object((1,3,6,1,4,1,890,1,15,3,119,1,2,1))
zyxelDoSPreventionPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelDoSPreventionPortEntry.setStatus(_A)
_ZyDoSPreventionPortState_Type=EnabledStatus
_ZyDoSPreventionPortState_Object=MibTableColumn
zyDoSPreventionPortState=_ZyDoSPreventionPortState_Object((1,3,6,1,4,1,890,1,15,3,119,1,2,1,1),_ZyDoSPreventionPortState_Type())
zyDoSPreventionPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyDoSPreventionPortState.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-DOS-PREVENTION-MIB',**{'zyxelDoSPrevention':zyxelDoSPrevention,'zyxelDoSPreventionSetup':zyxelDoSPreventionSetup,'zyDoSPreventionState':zyDoSPreventionState,'zyxelDoSPreventionPortTable':zyxelDoSPreventionPortTable,'zyxelDoSPreventionPortEntry':zyxelDoSPreventionPortEntry,'zyDoSPreventionPortState':zyDoSPreventionPortState})