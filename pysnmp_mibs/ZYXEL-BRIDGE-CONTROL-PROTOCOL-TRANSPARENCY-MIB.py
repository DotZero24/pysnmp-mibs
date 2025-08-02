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
zyxelBridgeControlProtocolTransparency=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,15))
_ZyxelBridgeControlProtocolTransparencySetup_ObjectIdentity=ObjectIdentity
zyxelBridgeControlProtocolTransparencySetup=_ZyxelBridgeControlProtocolTransparencySetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,15,1))
_ZyBridgeControlProtocolTransparencyState_Type=EnabledStatus
_ZyBridgeControlProtocolTransparencyState_Object=MibScalar
zyBridgeControlProtocolTransparencyState=_ZyBridgeControlProtocolTransparencyState_Object((1,3,6,1,4,1,890,1,15,3,15,1,1),_ZyBridgeControlProtocolTransparencyState_Type())
zyBridgeControlProtocolTransparencyState.setMaxAccess(_E)
if mibBuilder.loadTexts:zyBridgeControlProtocolTransparencyState.setStatus(_A)
_ZyxelBridgeControlProtocolTransparencyPortTable_Object=MibTable
zyxelBridgeControlProtocolTransparencyPortTable=_ZyxelBridgeControlProtocolTransparencyPortTable_Object((1,3,6,1,4,1,890,1,15,3,15,1,2))
if mibBuilder.loadTexts:zyxelBridgeControlProtocolTransparencyPortTable.setStatus(_A)
_ZyxelBridgeControlProtocolTransparencyPortEntry_Object=MibTableRow
zyxelBridgeControlProtocolTransparencyPortEntry=_ZyxelBridgeControlProtocolTransparencyPortEntry_Object((1,3,6,1,4,1,890,1,15,3,15,1,2,1))
zyxelBridgeControlProtocolTransparencyPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelBridgeControlProtocolTransparencyPortEntry.setStatus(_A)
class _ZyBridgeControlProtocolTransparencyPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('peer',0),('tunnel',1),('discard',2),('network',3)))
_ZyBridgeControlProtocolTransparencyPortMode_Type.__name__=_D
_ZyBridgeControlProtocolTransparencyPortMode_Object=MibTableColumn
zyBridgeControlProtocolTransparencyPortMode=_ZyBridgeControlProtocolTransparencyPortMode_Object((1,3,6,1,4,1,890,1,15,3,15,1,2,1,1),_ZyBridgeControlProtocolTransparencyPortMode_Type())
zyBridgeControlProtocolTransparencyPortMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zyBridgeControlProtocolTransparencyPortMode.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-BRIDGE-CONTROL-PROTOCOL-TRANSPARENCY-MIB',**{'zyxelBridgeControlProtocolTransparency':zyxelBridgeControlProtocolTransparency,'zyxelBridgeControlProtocolTransparencySetup':zyxelBridgeControlProtocolTransparencySetup,'zyBridgeControlProtocolTransparencyState':zyBridgeControlProtocolTransparencyState,'zyxelBridgeControlProtocolTransparencyPortTable':zyxelBridgeControlProtocolTransparencyPortTable,'zyxelBridgeControlProtocolTransparencyPortEntry':zyxelBridgeControlProtocolTransparencyPortEntry,'zyBridgeControlProtocolTransparencyPortMode':zyBridgeControlProtocolTransparencyPortMode})