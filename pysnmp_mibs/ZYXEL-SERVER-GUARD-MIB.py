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
zyxelDhcpServerGuard=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,122))
_ZyxelDhcpServerGuardSetup_ObjectIdentity=ObjectIdentity
zyxelDhcpServerGuardSetup=_ZyxelDhcpServerGuardSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,122,1))
_ZyDhcpServerGuardState_Type=EnabledStatus
_ZyDhcpServerGuardState_Object=MibScalar
zyDhcpServerGuardState=_ZyDhcpServerGuardState_Object((1,3,6,1,4,1,890,1,15,3,122,1,1),_ZyDhcpServerGuardState_Type())
zyDhcpServerGuardState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyDhcpServerGuardState.setStatus(_A)
_ZyxelDhcpServerGuardPortTable_Object=MibTable
zyxelDhcpServerGuardPortTable=_ZyxelDhcpServerGuardPortTable_Object((1,3,6,1,4,1,890,1,15,3,122,1,2))
if mibBuilder.loadTexts:zyxelDhcpServerGuardPortTable.setStatus(_A)
_ZyxelDhcpServerGuardPortEntry_Object=MibTableRow
zyxelDhcpServerGuardPortEntry=_ZyxelDhcpServerGuardPortEntry_Object((1,3,6,1,4,1,890,1,15,3,122,1,2,1))
zyxelDhcpServerGuardPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelDhcpServerGuardPortEntry.setStatus(_A)
_ZyDhcpServerGuardPortState_Type=EnabledStatus
_ZyDhcpServerGuardPortState_Object=MibTableColumn
zyDhcpServerGuardPortState=_ZyDhcpServerGuardPortState_Object((1,3,6,1,4,1,890,1,15,3,122,1,2,1,1),_ZyDhcpServerGuardPortState_Type())
zyDhcpServerGuardPortState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyDhcpServerGuardPortState.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-SERVER-GUARD-MIB',**{'zyxelDhcpServerGuard':zyxelDhcpServerGuard,'zyxelDhcpServerGuardSetup':zyxelDhcpServerGuardSetup,'zyDhcpServerGuardState':zyDhcpServerGuardState,'zyxelDhcpServerGuardPortTable':zyxelDhcpServerGuardPortTable,'zyxelDhcpServerGuardPortEntry':zyxelDhcpServerGuardPortEntry,'zyDhcpServerGuardPortState':zyDhcpServerGuardPortState})