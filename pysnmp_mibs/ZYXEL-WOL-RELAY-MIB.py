_F='zyWolRelayUdpPort'
_E='ZYXEL-WOL-RELAY-MIB'
_D='Integer32'
_C='read-write'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelWolRelay=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,116))
_ZyxelWolRelaySetup_ObjectIdentity=ObjectIdentity
zyxelWolRelaySetup=_ZyxelWolRelaySetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,116,1))
_ZyMaxNumberOfWolRelayEntry_Type=Integer32
_ZyMaxNumberOfWolRelayEntry_Object=MibScalar
zyMaxNumberOfWolRelayEntry=_ZyMaxNumberOfWolRelayEntry_Object((1,3,6,1,4,1,890,1,15,3,116,1,1),_ZyMaxNumberOfWolRelayEntry_Type())
zyMaxNumberOfWolRelayEntry.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyMaxNumberOfWolRelayEntry.setStatus(_A)
_ZyxelWolRelayTable_Object=MibTable
zyxelWolRelayTable=_ZyxelWolRelayTable_Object((1,3,6,1,4,1,890,1,15,3,116,1,2))
if mibBuilder.loadTexts:zyxelWolRelayTable.setStatus(_A)
_ZyxelWolRelayEntry_Object=MibTableRow
zyxelWolRelayEntry=_ZyxelWolRelayEntry_Object((1,3,6,1,4,1,890,1,15,3,116,1,2,1))
zyxelWolRelayEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zyxelWolRelayEntry.setStatus(_A)
class _ZyWolRelayUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZyWolRelayUdpPort_Type.__name__=_D
_ZyWolRelayUdpPort_Object=MibTableColumn
zyWolRelayUdpPort=_ZyWolRelayUdpPort_Object((1,3,6,1,4,1,890,1,15,3,116,1,2,1,1),_ZyWolRelayUdpPort_Type())
zyWolRelayUdpPort.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyWolRelayUdpPort.setStatus(_A)
class _ZyWolRelaySourceVlanMap1k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyWolRelaySourceVlanMap1k_Type.__name__=_B
_ZyWolRelaySourceVlanMap1k_Object=MibTableColumn
zyWolRelaySourceVlanMap1k=_ZyWolRelaySourceVlanMap1k_Object((1,3,6,1,4,1,890,1,15,3,116,1,2,1,2),_ZyWolRelaySourceVlanMap1k_Type())
zyWolRelaySourceVlanMap1k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyWolRelaySourceVlanMap1k.setStatus(_A)
class _ZyWolRelaySourceVlanMap2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyWolRelaySourceVlanMap2k_Type.__name__=_B
_ZyWolRelaySourceVlanMap2k_Object=MibTableColumn
zyWolRelaySourceVlanMap2k=_ZyWolRelaySourceVlanMap2k_Object((1,3,6,1,4,1,890,1,15,3,116,1,2,1,3),_ZyWolRelaySourceVlanMap2k_Type())
zyWolRelaySourceVlanMap2k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyWolRelaySourceVlanMap2k.setStatus(_A)
class _ZyWolRelaySourceVlanMap3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyWolRelaySourceVlanMap3k_Type.__name__=_B
_ZyWolRelaySourceVlanMap3k_Object=MibTableColumn
zyWolRelaySourceVlanMap3k=_ZyWolRelaySourceVlanMap3k_Object((1,3,6,1,4,1,890,1,15,3,116,1,2,1,4),_ZyWolRelaySourceVlanMap3k_Type())
zyWolRelaySourceVlanMap3k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyWolRelaySourceVlanMap3k.setStatus(_A)
class _ZyWolRelaySourceVlanMap4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyWolRelaySourceVlanMap4k_Type.__name__=_B
_ZyWolRelaySourceVlanMap4k_Object=MibTableColumn
zyWolRelaySourceVlanMap4k=_ZyWolRelaySourceVlanMap4k_Object((1,3,6,1,4,1,890,1,15,3,116,1,2,1,5),_ZyWolRelaySourceVlanMap4k_Type())
zyWolRelaySourceVlanMap4k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyWolRelaySourceVlanMap4k.setStatus(_A)
class _ZyWolRelayDestinationVlanMap1k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyWolRelayDestinationVlanMap1k_Type.__name__=_B
_ZyWolRelayDestinationVlanMap1k_Object=MibTableColumn
zyWolRelayDestinationVlanMap1k=_ZyWolRelayDestinationVlanMap1k_Object((1,3,6,1,4,1,890,1,15,3,116,1,2,1,6),_ZyWolRelayDestinationVlanMap1k_Type())
zyWolRelayDestinationVlanMap1k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyWolRelayDestinationVlanMap1k.setStatus(_A)
class _ZyWolRelayDestinationVlanMap2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyWolRelayDestinationVlanMap2k_Type.__name__=_B
_ZyWolRelayDestinationVlanMap2k_Object=MibTableColumn
zyWolRelayDestinationVlanMap2k=_ZyWolRelayDestinationVlanMap2k_Object((1,3,6,1,4,1,890,1,15,3,116,1,2,1,7),_ZyWolRelayDestinationVlanMap2k_Type())
zyWolRelayDestinationVlanMap2k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyWolRelayDestinationVlanMap2k.setStatus(_A)
class _ZyWolRelayDestinationVlanMap3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyWolRelayDestinationVlanMap3k_Type.__name__=_B
_ZyWolRelayDestinationVlanMap3k_Object=MibTableColumn
zyWolRelayDestinationVlanMap3k=_ZyWolRelayDestinationVlanMap3k_Object((1,3,6,1,4,1,890,1,15,3,116,1,2,1,8),_ZyWolRelayDestinationVlanMap3k_Type())
zyWolRelayDestinationVlanMap3k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyWolRelayDestinationVlanMap3k.setStatus(_A)
class _ZyWolRelayDestinationVlanMap4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyWolRelayDestinationVlanMap4k_Type.__name__=_B
_ZyWolRelayDestinationVlanMap4k_Object=MibTableColumn
zyWolRelayDestinationVlanMap4k=_ZyWolRelayDestinationVlanMap4k_Object((1,3,6,1,4,1,890,1,15,3,116,1,2,1,9),_ZyWolRelayDestinationVlanMap4k_Type())
zyWolRelayDestinationVlanMap4k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyWolRelayDestinationVlanMap4k.setStatus(_A)
_ZyWolRelayRowStatus_Type=RowStatus
_ZyWolRelayRowStatus_Object=MibTableColumn
zyWolRelayRowStatus=_ZyWolRelayRowStatus_Object((1,3,6,1,4,1,890,1,15,3,116,1,2,1,10),_ZyWolRelayRowStatus_Type())
zyWolRelayRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyWolRelayRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zyxelWolRelay':zyxelWolRelay,'zyxelWolRelaySetup':zyxelWolRelaySetup,'zyMaxNumberOfWolRelayEntry':zyMaxNumberOfWolRelayEntry,'zyxelWolRelayTable':zyxelWolRelayTable,'zyxelWolRelayEntry':zyxelWolRelayEntry,_F:zyWolRelayUdpPort,'zyWolRelaySourceVlanMap1k':zyWolRelaySourceVlanMap1k,'zyWolRelaySourceVlanMap2k':zyWolRelaySourceVlanMap2k,'zyWolRelaySourceVlanMap3k':zyWolRelaySourceVlanMap3k,'zyWolRelaySourceVlanMap4k':zyWolRelaySourceVlanMap4k,'zyWolRelayDestinationVlanMap1k':zyWolRelayDestinationVlanMap1k,'zyWolRelayDestinationVlanMap2k':zyWolRelayDestinationVlanMap2k,'zyWolRelayDestinationVlanMap3k':zyWolRelayDestinationVlanMap3k,'zyWolRelayDestinationVlanMap4k':zyWolRelayDestinationVlanMap4k,'zyWolRelayRowStatus':zyWolRelayRowStatus})