_F='Integer32'
_E='dot1dBasePort'
_D='BRIDGE-MIB'
_C='Bits'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_C,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelL2pt=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,39))
_ZyxelL2ptSetup_ObjectIdentity=ObjectIdentity
zyxelL2ptSetup=_ZyxelL2ptSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,39,1))
_ZyL2ptState_Type=EnabledStatus
_ZyL2ptState_Object=MibScalar
zyL2ptState=_ZyL2ptState_Object((1,3,6,1,4,1,890,1,15,3,39,1,1),_ZyL2ptState_Type())
zyL2ptState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyL2ptState.setStatus(_A)
_ZyL2ptMacAddress_Type=MacAddress
_ZyL2ptMacAddress_Object=MibScalar
zyL2ptMacAddress=_ZyL2ptMacAddress_Object((1,3,6,1,4,1,890,1,15,3,39,1,2),_ZyL2ptMacAddress_Type())
zyL2ptMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyL2ptMacAddress.setStatus(_A)
_ZyxelL2ptTable_Object=MibTable
zyxelL2ptTable=_ZyxelL2ptTable_Object((1,3,6,1,4,1,890,1,15,3,39,1,3))
if mibBuilder.loadTexts:zyxelL2ptTable.setStatus(_A)
_ZyxelL2ptEntry_Object=MibTableRow
zyxelL2ptEntry=_ZyxelL2ptEntry_Object((1,3,6,1,4,1,890,1,15,3,39,1,3,1))
zyxelL2ptEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelL2ptEntry.setStatus(_A)
class _ZyL2ptProtocolGroup_Type(Bits):namedValues=NamedValues(*(('cdp',0),('stp',1),('vtp',2),('lldp',3)))
_ZyL2ptProtocolGroup_Type.__name__=_C
_ZyL2ptProtocolGroup_Object=MibTableColumn
zyL2ptProtocolGroup=_ZyL2ptProtocolGroup_Object((1,3,6,1,4,1,890,1,15,3,39,1,3,1,1),_ZyL2ptProtocolGroup_Type())
zyL2ptProtocolGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:zyL2ptProtocolGroup.setStatus(_A)
class _ZyL2ptPointToPointProtocolGroup_Type(Bits):namedValues=NamedValues(*(('pagp',0),('lacp',1),('udld',2)))
_ZyL2ptPointToPointProtocolGroup_Type.__name__=_C
_ZyL2ptPointToPointProtocolGroup_Object=MibTableColumn
zyL2ptPointToPointProtocolGroup=_ZyL2ptPointToPointProtocolGroup_Object((1,3,6,1,4,1,890,1,15,3,39,1,3,1,2),_ZyL2ptPointToPointProtocolGroup_Type())
zyL2ptPointToPointProtocolGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:zyL2ptPointToPointProtocolGroup.setStatus(_A)
class _ZyL2ptMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('access',1),('tunnel',2)))
_ZyL2ptMode_Type.__name__=_F
_ZyL2ptMode_Object=MibTableColumn
zyL2ptMode=_ZyL2ptMode_Object((1,3,6,1,4,1,890,1,15,3,39,1,3,1,3),_ZyL2ptMode_Type())
zyL2ptMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyL2ptMode.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-L2PT-MIB',**{'zyxelL2pt':zyxelL2pt,'zyxelL2ptSetup':zyxelL2ptSetup,'zyL2ptState':zyL2ptState,'zyL2ptMacAddress':zyL2ptMacAddress,'zyxelL2ptTable':zyxelL2ptTable,'zyxelL2ptEntry':zyxelL2ptEntry,'zyL2ptProtocolGroup':zyL2ptProtocolGroup,'zyL2ptPointToPointProtocolGroup':zyL2ptPointToPointProtocolGroup,'zyL2ptMode':zyL2ptMode})