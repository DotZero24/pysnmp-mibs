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
zyxelPortIsolation=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,64))
_ZyxelPortIsolationSetup_ObjectIdentity=ObjectIdentity
zyxelPortIsolationSetup=_ZyxelPortIsolationSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,64,1))
_ZyxelPortIsolationPortTable_Object=MibTable
zyxelPortIsolationPortTable=_ZyxelPortIsolationPortTable_Object((1,3,6,1,4,1,890,1,15,3,64,1,1))
if mibBuilder.loadTexts:zyxelPortIsolationPortTable.setStatus(_A)
_ZyxelPortIsolationPortEntry_Object=MibTableRow
zyxelPortIsolationPortEntry=_ZyxelPortIsolationPortEntry_Object((1,3,6,1,4,1,890,1,15,3,64,1,1,1))
zyxelPortIsolationPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelPortIsolationPortEntry.setStatus(_A)
_ZyPortIsolationPortState_Type=EnabledStatus
_ZyPortIsolationPortState_Object=MibTableColumn
zyPortIsolationPortState=_ZyPortIsolationPortState_Object((1,3,6,1,4,1,890,1,15,3,64,1,1,1,1),_ZyPortIsolationPortState_Type())
zyPortIsolationPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyPortIsolationPortState.setStatus(_A)
_ZyPortIsolationSmartIsolationState_Type=EnabledStatus
_ZyPortIsolationSmartIsolationState_Object=MibScalar
zyPortIsolationSmartIsolationState=_ZyPortIsolationSmartIsolationState_Object((1,3,6,1,4,1,890,1,15,3,64,1,2),_ZyPortIsolationSmartIsolationState_Type())
zyPortIsolationSmartIsolationState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyPortIsolationSmartIsolationState.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-PORT-ISOLATION-MIB',**{'zyxelPortIsolation':zyxelPortIsolation,'zyxelPortIsolationSetup':zyxelPortIsolationSetup,'zyxelPortIsolationPortTable':zyxelPortIsolationPortTable,'zyxelPortIsolationPortEntry':zyxelPortIsolationPortEntry,'zyPortIsolationPortState':zyPortIsolationPortState,'zyPortIsolationSmartIsolationState':zyPortIsolationSmartIsolationState})