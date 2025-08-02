_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelLldp=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,43))
_ZyxelLldpSetup_ObjectIdentity=ObjectIdentity
zyxelLldpSetup=_ZyxelLldpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,43,1))
_ZyLldpState_Type=EnabledStatus
_ZyLldpState_Object=MibScalar
zyLldpState=_ZyLldpState_Object((1,3,6,1,4,1,890,1,15,3,43,1,1),_ZyLldpState_Type())
zyLldpState.setMaxAccess(_A)
if mibBuilder.loadTexts:zyLldpState.setStatus(_B)
_ZyxelLldpStatus_ObjectIdentity=ObjectIdentity
zyxelLldpStatus=_ZyxelLldpStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,43,2))
_ZyLldpRemoteInfoClear_Type=EnabledStatus
_ZyLldpRemoteInfoClear_Object=MibScalar
zyLldpRemoteInfoClear=_ZyLldpRemoteInfoClear_Object((1,3,6,1,4,1,890,1,15,3,43,2,1),_ZyLldpRemoteInfoClear_Type())
zyLldpRemoteInfoClear.setMaxAccess(_A)
if mibBuilder.loadTexts:zyLldpRemoteInfoClear.setStatus(_B)
_ZyLldpRemoteInfoClearPorts_Type=PortList
_ZyLldpRemoteInfoClearPorts_Object=MibScalar
zyLldpRemoteInfoClearPorts=_ZyLldpRemoteInfoClearPorts_Object((1,3,6,1,4,1,890,1,15,3,43,2,2),_ZyLldpRemoteInfoClearPorts_Type())
zyLldpRemoteInfoClearPorts.setMaxAccess(_A)
if mibBuilder.loadTexts:zyLldpRemoteInfoClearPorts.setStatus(_B)
_ZyLldpStatisticsClear_Type=EnabledStatus
_ZyLldpStatisticsClear_Object=MibScalar
zyLldpStatisticsClear=_ZyLldpStatisticsClear_Object((1,3,6,1,4,1,890,1,15,3,43,2,3),_ZyLldpStatisticsClear_Type())
zyLldpStatisticsClear.setMaxAccess(_A)
if mibBuilder.loadTexts:zyLldpStatisticsClear.setStatus(_B)
mibBuilder.exportSymbols('ZYXEL-LLDP-MIB',**{'zyxelLldp':zyxelLldp,'zyxelLldpSetup':zyxelLldpSetup,'zyLldpState':zyLldpState,'zyxelLldpStatus':zyxelLldpStatus,'zyLldpRemoteInfoClear':zyLldpRemoteInfoClear,'zyLldpRemoteInfoClearPorts':zyLldpRemoteInfoClearPorts,'zyLldpStatisticsClear':zyLldpStatisticsClear})