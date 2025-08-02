_J='zxr10PortNo'
_I='zxr10PosInRack'
_H='NotificationType'
_G='zxr10ShelfNo'
_F='zxr10RackNo'
_E='DisplayString'
_D='ZXR10-T128-MIB'
_C='ZXR10-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
AvailStatus,BoardType,BoolStatus,DisplayString,MasterStatus,NpcType,OperStatus,PidUsedStatus,PortType,PortWorkingType,ShelfAttrib,UnitRunStatus,zxr10,zxr10PosInRack,zxr10RackNo,zxr10rack=mibBuilder.importSymbols(_C,'AvailStatus','BoardType','BoolStatus',_E,'MasterStatus','NpcType','OperStatus','PidUsedStatus','PortType','PortWorkingType','ShelfAttrib','UnitRunStatus','zxr10',_I,_F,'zxr10rack')
class AlarmType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,129,130,131,132,133,134)));namedValues=NamedValues(*(('hardware-environment',1),('hardware-board',2),('hardware-port',3),('softprotocol-ros',65),('softprotocol-database',66),('softprotocol-oam',67),('softprotocol-security',68),('softprotocol-ospf',69),('softprotocol-rip',70),('softprotocol-bgp',71),('softprotocol-drp',72),('softprotocol-tcp-udp',73),('softprotocol-ip',74),('softprotocol-igmp',75),('softprotocol-telnet',76),('softprotocol-udp',77),('softprotocol-arp',78),('softprotocol-isis',79),('softprotocol-icmp',80),('softprotocol-snmp',81),('softprotocol-rmon',82),('statistics-microcode',129),('statistics-ip',130),('statistics-tcp',131),('statistics-udp',132),('statistics-icmp',133),('statistics-bgp',134)))
_Zxr10shelfTable_Object=MibTable
zxr10shelfTable=_Zxr10shelfTable_Object((1,3,6,1,4,1,3902,3,2,2))
if mibBuilder.loadTexts:zxr10shelfTable.setStatus(_A)
_Zxr10shelfEntry_Object=MibTableRow
zxr10shelfEntry=_Zxr10shelfEntry_Object((1,3,6,1,4,1,3902,3,2,2,1))
zxr10shelfEntry.setIndexNames((0,_C,_F),(0,_D,_G))
if mibBuilder.loadTexts:zxr10shelfEntry.setStatus(_A)
_Zxr10ShelfNo_Type=Integer32
_Zxr10ShelfNo_Object=MibTableColumn
zxr10ShelfNo=_Zxr10ShelfNo_Object((1,3,6,1,4,1,3902,3,2,2,1,1),_Zxr10ShelfNo_Type())
zxr10ShelfNo.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ShelfNo.setStatus(_A)
_Zxr10ShelfAttrib_Type=ShelfAttrib
_Zxr10ShelfAttrib_Object=MibTableColumn
zxr10ShelfAttrib=_Zxr10ShelfAttrib_Object((1,3,6,1,4,1,3902,3,2,2,1,2),_Zxr10ShelfAttrib_Type())
zxr10ShelfAttrib.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ShelfAttrib.setStatus(_A)
_Zxr10ShelfAvailStatus_Type=AvailStatus
_Zxr10ShelfAvailStatus_Object=MibTableColumn
zxr10ShelfAvailStatus=_Zxr10ShelfAvailStatus_Object((1,3,6,1,4,1,3902,3,2,2,1,3),_Zxr10ShelfAvailStatus_Type())
zxr10ShelfAvailStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10ShelfAvailStatus.setStatus(_A)
_Zxr10portTable_Object=MibTable
zxr10portTable=_Zxr10portTable_Object((1,3,6,1,4,1,3902,3,2,4))
if mibBuilder.loadTexts:zxr10portTable.setStatus(_A)
_Zxr10portEntry_Object=MibTableRow
zxr10portEntry=_Zxr10portEntry_Object((1,3,6,1,4,1,3902,3,2,4,1))
zxr10portEntry.setIndexNames((0,_C,_F),(0,_D,_G),(0,_C,_I),(0,_D,_J))
if mibBuilder.loadTexts:zxr10portEntry.setStatus(_A)
_Zxr10PortIfIndex_Type=Integer32
_Zxr10PortIfIndex_Object=MibTableColumn
zxr10PortIfIndex=_Zxr10PortIfIndex_Object((1,3,6,1,4,1,3902,3,2,4,1,1),_Zxr10PortIfIndex_Type())
zxr10PortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PortIfIndex.setStatus(_A)
_Zxr10PortNo_Type=Integer32
_Zxr10PortNo_Object=MibTableColumn
zxr10PortNo=_Zxr10PortNo_Object((1,3,6,1,4,1,3902,3,2,4,1,2),_Zxr10PortNo_Type())
zxr10PortNo.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PortNo.setStatus(_A)
_Zxr10PortType_Type=PortType
_Zxr10PortType_Object=MibTableColumn
zxr10PortType=_Zxr10PortType_Object((1,3,6,1,4,1,3902,3,2,4,1,3),_Zxr10PortType_Type())
zxr10PortType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PortType.setStatus(_A)
_Zxr10PortWorkingType_Type=PortWorkingType
_Zxr10PortWorkingType_Object=MibTableColumn
zxr10PortWorkingType=_Zxr10PortWorkingType_Object((1,3,6,1,4,1,3902,3,2,4,1,4),_Zxr10PortWorkingType_Type())
zxr10PortWorkingType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PortWorkingType.setStatus(_A)
_Zxr10PortMTU_Type=Integer32
_Zxr10PortMTU_Object=MibTableColumn
zxr10PortMTU=_Zxr10PortMTU_Object((1,3,6,1,4,1,3902,3,2,4,1,5),_Zxr10PortMTU_Type())
zxr10PortMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PortMTU.setStatus(_A)
class _Zxr10PortSpeed_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Zxr10PortSpeed_Type.__name__=_E
_Zxr10PortSpeed_Object=MibTableColumn
zxr10PortSpeed=_Zxr10PortSpeed_Object((1,3,6,1,4,1,3902,3,2,4,1,6),_Zxr10PortSpeed_Type())
zxr10PortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PortSpeed.setStatus(_A)
_Zxr10PortAvailStatus_Type=AvailStatus
_Zxr10PortAvailStatus_Object=MibTableColumn
zxr10PortAvailStatus=_Zxr10PortAvailStatus_Object((1,3,6,1,4,1,3902,3,2,4,1,7),_Zxr10PortAvailStatus_Type())
zxr10PortAvailStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PortAvailStatus.setStatus(_A)
_Zxr10PortOperStatus_Type=OperStatus
_Zxr10PortOperStatus_Object=MibTableColumn
zxr10PortOperStatus=_Zxr10PortOperStatus_Object((1,3,6,1,4,1,3902,3,2,4,1,8),_Zxr10PortOperStatus_Type())
zxr10PortOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10PortOperStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'AlarmType':AlarmType,'zxr10shelfTable':zxr10shelfTable,'zxr10shelfEntry':zxr10shelfEntry,_G:zxr10ShelfNo,'zxr10ShelfAttrib':zxr10ShelfAttrib,'zxr10ShelfAvailStatus':zxr10ShelfAvailStatus,'zxr10portTable':zxr10portTable,'zxr10portEntry':zxr10portEntry,'zxr10PortIfIndex':zxr10PortIfIndex,_J:zxr10PortNo,'zxr10PortType':zxr10PortType,'zxr10PortWorkingType':zxr10PortWorkingType,'zxr10PortMTU':zxr10PortMTU,'zxr10PortSpeed':zxr10PortSpeed,'zxr10PortAvailStatus':zxr10PortAvailStatus,'zxr10PortOperStatus':zxr10PortOperStatus})