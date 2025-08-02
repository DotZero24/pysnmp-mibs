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
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelGreenEthernet=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,93))
_ZyxelGreenEthernetSetup_ObjectIdentity=ObjectIdentity
zyxelGreenEthernetSetup=_ZyxelGreenEthernetSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,93,1))
_ZyGreenEthernetEeeState_Type=EnabledStatus
_ZyGreenEthernetEeeState_Object=MibScalar
zyGreenEthernetEeeState=_ZyGreenEthernetEeeState_Object((1,3,6,1,4,1,890,1,15,3,93,1,1),_ZyGreenEthernetEeeState_Type())
zyGreenEthernetEeeState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyGreenEthernetEeeState.setStatus(_A)
_ZyGreenEthernetAutoPowerDownState_Type=EnabledStatus
_ZyGreenEthernetAutoPowerDownState_Object=MibScalar
zyGreenEthernetAutoPowerDownState=_ZyGreenEthernetAutoPowerDownState_Object((1,3,6,1,4,1,890,1,15,3,93,1,2),_ZyGreenEthernetAutoPowerDownState_Type())
zyGreenEthernetAutoPowerDownState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyGreenEthernetAutoPowerDownState.setStatus(_A)
_ZyGreenEthernetShortReachState_Type=EnabledStatus
_ZyGreenEthernetShortReachState_Object=MibScalar
zyGreenEthernetShortReachState=_ZyGreenEthernetShortReachState_Object((1,3,6,1,4,1,890,1,15,3,93,1,3),_ZyGreenEthernetShortReachState_Type())
zyGreenEthernetShortReachState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyGreenEthernetShortReachState.setStatus(_A)
_ZyxelGreenEthernetPortTable_Object=MibTable
zyxelGreenEthernetPortTable=_ZyxelGreenEthernetPortTable_Object((1,3,6,1,4,1,890,1,15,3,93,1,4))
if mibBuilder.loadTexts:zyxelGreenEthernetPortTable.setStatus(_A)
_ZyxelGreenEthernetPortEntry_Object=MibTableRow
zyxelGreenEthernetPortEntry=_ZyxelGreenEthernetPortEntry_Object((1,3,6,1,4,1,890,1,15,3,93,1,4,1))
zyxelGreenEthernetPortEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelGreenEthernetPortEntry.setStatus(_A)
_ZyGreenEthernetEeePortState_Type=EnabledStatus
_ZyGreenEthernetEeePortState_Object=MibTableColumn
zyGreenEthernetEeePortState=_ZyGreenEthernetEeePortState_Object((1,3,6,1,4,1,890,1,15,3,93,1,4,1,1),_ZyGreenEthernetEeePortState_Type())
zyGreenEthernetEeePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyGreenEthernetEeePortState.setStatus(_A)
_ZyGreenEthernetAutoPowerDownPortState_Type=EnabledStatus
_ZyGreenEthernetAutoPowerDownPortState_Object=MibTableColumn
zyGreenEthernetAutoPowerDownPortState=_ZyGreenEthernetAutoPowerDownPortState_Object((1,3,6,1,4,1,890,1,15,3,93,1,4,1,2),_ZyGreenEthernetAutoPowerDownPortState_Type())
zyGreenEthernetAutoPowerDownPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyGreenEthernetAutoPowerDownPortState.setStatus(_A)
_ZyGreenEthernetShortReachPortState_Type=EnabledStatus
_ZyGreenEthernetShortReachPortState_Object=MibTableColumn
zyGreenEthernetShortReachPortState=_ZyGreenEthernetShortReachPortState_Object((1,3,6,1,4,1,890,1,15,3,93,1,4,1,3),_ZyGreenEthernetShortReachPortState_Type())
zyGreenEthernetShortReachPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyGreenEthernetShortReachPortState.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-GREEN-ETHERNET-MIB',**{'zyxelGreenEthernet':zyxelGreenEthernet,'zyxelGreenEthernetSetup':zyxelGreenEthernetSetup,'zyGreenEthernetEeeState':zyGreenEthernetEeeState,'zyGreenEthernetAutoPowerDownState':zyGreenEthernetAutoPowerDownState,'zyGreenEthernetShortReachState':zyGreenEthernetShortReachState,'zyxelGreenEthernetPortTable':zyxelGreenEthernetPortTable,'zyxelGreenEthernetPortEntry':zyxelGreenEthernetPortEntry,'zyGreenEthernetEeePortState':zyGreenEthernetEeePortState,'zyGreenEthernetAutoPowerDownPortState':zyGreenEthernetAutoPowerDownPortState,'zyGreenEthernetShortReachPortState':zyGreenEthernetShortReachPortState})