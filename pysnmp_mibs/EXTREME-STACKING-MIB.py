_U='extremeStackingPortLinkStatus'
_T='extremeStackingPortLinkSpeed'
_S='extremeStackingPortRemoteMac'
_R='extremeStackMemberOperStatus'
_Q='extremeStackingPortIfIndex'
_P='read-write'
_O='sysUpTime'
_N='sysDescr'
_M='ifIndex'
_L='IF-MIB'
_K='extremeCurrentTemperature'
_J='EXTREME-SYSTEM-MIB'
_I='secondary'
_H='primary'
_G='SNMPv2-MIB'
_F='extremeStackMemberSlotId'
_E='DisplayString'
_D='EXTREME-STACKING-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
extremeCurrentTemperature,=mibBuilder.importSymbols(_J,_K)
ifIndex,=mibBuilder.importSymbols(_L,_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysDescr,sysUpTime=mibBuilder.importSymbols(_G,_N,_O)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'MacAddress','PhysAddress','TextualConvention','TruthValue')
extremeStackable=ModuleIdentity((1,3,6,1,4,1,1916,1,33))
if mibBuilder.loadTexts:extremeStackable.setRevisions(('2017-12-06 15:00','2017-10-10 15:15','2014-10-13 10:30','2004-09-27 09:15'))
_ExtremeStackDetection_Type=TruthValue
_ExtremeStackDetection_Object=MibScalar
extremeStackDetection=_ExtremeStackDetection_Object((1,3,6,1,4,1,1916,1,33,1),_ExtremeStackDetection_Type())
extremeStackDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackDetection.setStatus(_A)
_ExtremeStackMemberTable_Object=MibTable
extremeStackMemberTable=_ExtremeStackMemberTable_Object((1,3,6,1,4,1,1916,1,33,2))
if mibBuilder.loadTexts:extremeStackMemberTable.setStatus(_A)
_ExtremeStackMemberEntry_Object=MibTableRow
extremeStackMemberEntry=_ExtremeStackMemberEntry_Object((1,3,6,1,4,1,1916,1,33,2,1))
extremeStackMemberEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:extremeStackMemberEntry.setStatus(_A)
class _ExtremeStackMemberSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ExtremeStackMemberSlotId_Type.__name__=_C
_ExtremeStackMemberSlotId_Object=MibTableColumn
extremeStackMemberSlotId=_ExtremeStackMemberSlotId_Object((1,3,6,1,4,1,1916,1,33,2,1,1),_ExtremeStackMemberSlotId_Type())
extremeStackMemberSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberSlotId.setStatus(_A)
_ExtremeStackMemberType_Type=ObjectIdentifier
_ExtremeStackMemberType_Object=MibTableColumn
extremeStackMemberType=_ExtremeStackMemberType_Object((1,3,6,1,4,1,1916,1,33,2,1,2),_ExtremeStackMemberType_Type())
extremeStackMemberType.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberType.setStatus(_A)
class _ExtremeStackMemberOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('mismatch',3)))
_ExtremeStackMemberOperStatus_Type.__name__=_C
_ExtremeStackMemberOperStatus_Object=MibTableColumn
extremeStackMemberOperStatus=_ExtremeStackMemberOperStatus_Object((1,3,6,1,4,1,1916,1,33,2,1,3),_ExtremeStackMemberOperStatus_Type())
extremeStackMemberOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberOperStatus.setStatus(_A)
class _ExtremeStackMemberRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),('backup',3)))
_ExtremeStackMemberRole_Type.__name__=_C
_ExtremeStackMemberRole_Object=MibTableColumn
extremeStackMemberRole=_ExtremeStackMemberRole_Object((1,3,6,1,4,1,1916,1,33,2,1,4),_ExtremeStackMemberRole_Type())
extremeStackMemberRole.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberRole.setStatus(_A)
_ExtremeStackMemberEntPhysicalIndex_Type=Integer32
_ExtremeStackMemberEntPhysicalIndex_Object=MibTableColumn
extremeStackMemberEntPhysicalIndex=_ExtremeStackMemberEntPhysicalIndex_Object((1,3,6,1,4,1,1916,1,33,2,1,5),_ExtremeStackMemberEntPhysicalIndex_Type())
extremeStackMemberEntPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberEntPhysicalIndex.setStatus(_A)
_ExtremeStackMemberMACAddress_Type=MacAddress
_ExtremeStackMemberMACAddress_Object=MibTableColumn
extremeStackMemberMACAddress=_ExtremeStackMemberMACAddress_Object((1,3,6,1,4,1,1916,1,33,2,1,6),_ExtremeStackMemberMACAddress_Type())
extremeStackMemberMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberMACAddress.setStatus(_A)
class _ExtremeStackMemberCurImageVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ExtremeStackMemberCurImageVersion_Type.__name__=_E
_ExtremeStackMemberCurImageVersion_Object=MibTableColumn
extremeStackMemberCurImageVersion=_ExtremeStackMemberCurImageVersion_Object((1,3,6,1,4,1,1916,1,33,2,1,7),_ExtremeStackMemberCurImageVersion_Type())
extremeStackMemberCurImageVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberCurImageVersion.setStatus(_A)
class _ExtremeStackMemberPriImageVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ExtremeStackMemberPriImageVersion_Type.__name__=_E
_ExtremeStackMemberPriImageVersion_Object=MibTableColumn
extremeStackMemberPriImageVersion=_ExtremeStackMemberPriImageVersion_Object((1,3,6,1,4,1,1916,1,33,2,1,8),_ExtremeStackMemberPriImageVersion_Type())
extremeStackMemberPriImageVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberPriImageVersion.setStatus(_A)
class _ExtremeStackMemberSecImageVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ExtremeStackMemberSecImageVersion_Type.__name__=_E
_ExtremeStackMemberSecImageVersion_Object=MibTableColumn
extremeStackMemberSecImageVersion=_ExtremeStackMemberSecImageVersion_Object((1,3,6,1,4,1,1916,1,33,2,1,9),_ExtremeStackMemberSecImageVersion_Type())
extremeStackMemberSecImageVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberSecImageVersion.setStatus(_A)
class _ExtremeStackMemberBootRomVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ExtremeStackMemberBootRomVersion_Type.__name__=_E
_ExtremeStackMemberBootRomVersion_Object=MibTableColumn
extremeStackMemberBootRomVersion=_ExtremeStackMemberBootRomVersion_Object((1,3,6,1,4,1,1916,1,33,2,1,10),_ExtremeStackMemberBootRomVersion_Type())
extremeStackMemberBootRomVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberBootRomVersion.setStatus(_A)
class _ExtremeStackMemberCurConfig_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ExtremeStackMemberCurConfig_Type.__name__=_E
_ExtremeStackMemberCurConfig_Object=MibTableColumn
extremeStackMemberCurConfig=_ExtremeStackMemberCurConfig_Object((1,3,6,1,4,1,1916,1,33,2,1,11),_ExtremeStackMemberCurConfig_Type())
extremeStackMemberCurConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberCurConfig.setStatus(_A)
class _ExtremeStackMemberConfigSelected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),('other',3)))
_ExtremeStackMemberConfigSelected_Type.__name__=_C
_ExtremeStackMemberConfigSelected_Object=MibTableColumn
extremeStackMemberConfigSelected=_ExtremeStackMemberConfigSelected_Object((1,3,6,1,4,1,1916,1,33,2,1,12),_ExtremeStackMemberConfigSelected_Type())
extremeStackMemberConfigSelected.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberConfigSelected.setStatus(_A)
class _ExtremeStackMemberImageSelected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ExtremeStackMemberImageSelected_Type.__name__=_C
_ExtremeStackMemberImageSelected_Object=MibTableColumn
extremeStackMemberImageSelected=_ExtremeStackMemberImageSelected_Object((1,3,6,1,4,1,1916,1,33,2,1,13),_ExtremeStackMemberImageSelected_Type())
extremeStackMemberImageSelected.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberImageSelected.setStatus(_A)
_ExtremeStackMemberStackPriority_Type=Integer32
_ExtremeStackMemberStackPriority_Object=MibTableColumn
extremeStackMemberStackPriority=_ExtremeStackMemberStackPriority_Object((1,3,6,1,4,1,1916,1,33,2,1,14),_ExtremeStackMemberStackPriority_Type())
extremeStackMemberStackPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberStackPriority.setStatus(_A)
_ExtremeStackMemberMgmtIpAddress_Type=IpAddress
_ExtremeStackMemberMgmtIpAddress_Object=MibTableColumn
extremeStackMemberMgmtIpAddress=_ExtremeStackMemberMgmtIpAddress_Object((1,3,6,1,4,1,1916,1,33,2,1,15),_ExtremeStackMemberMgmtIpAddress_Type())
extremeStackMemberMgmtIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberMgmtIpAddress.setStatus(_A)
class _ExtremeStackMemberSysLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ExtremeStackMemberSysLocation_Type.__name__=_E
_ExtremeStackMemberSysLocation_Object=MibTableColumn
extremeStackMemberSysLocation=_ExtremeStackMemberSysLocation_Object((1,3,6,1,4,1,1916,1,33,2,1,16),_ExtremeStackMemberSysLocation_Type())
extremeStackMemberSysLocation.setMaxAccess(_P)
if mibBuilder.loadTexts:extremeStackMemberSysLocation.setStatus(_A)
_ExtremeStackMemberAutoConfig_Type=TruthValue
_ExtremeStackMemberAutoConfig_Object=MibTableColumn
extremeStackMemberAutoConfig=_ExtremeStackMemberAutoConfig_Object((1,3,6,1,4,1,1916,1,33,2,1,17),_ExtremeStackMemberAutoConfig_Type())
extremeStackMemberAutoConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberAutoConfig.setStatus(_A)
class _ExtremeStackMemberStackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ExtremeStackMemberStackStatus_Type.__name__=_C
_ExtremeStackMemberStackStatus_Object=MibTableColumn
extremeStackMemberStackStatus=_ExtremeStackMemberStackStatus_Object((1,3,6,1,4,1,1916,1,33,2,1,18),_ExtremeStackMemberStackStatus_Type())
extremeStackMemberStackStatus.setMaxAccess(_P)
if mibBuilder.loadTexts:extremeStackMemberStackStatus.setStatus(_A)
class _ExtremeStackMemberImageBooted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ExtremeStackMemberImageBooted_Type.__name__=_C
_ExtremeStackMemberImageBooted_Object=MibTableColumn
extremeStackMemberImageBooted=_ExtremeStackMemberImageBooted_Object((1,3,6,1,4,1,1916,1,33,2,1,19),_ExtremeStackMemberImageBooted_Type())
extremeStackMemberImageBooted.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberImageBooted.setStatus(_A)
_ExtremeStackMemberBootTime_Type=DateAndTime
_ExtremeStackMemberBootTime_Object=MibTableColumn
extremeStackMemberBootTime=_ExtremeStackMemberBootTime_Object((1,3,6,1,4,1,1916,1,33,2,1,20),_ExtremeStackMemberBootTime_Type())
extremeStackMemberBootTime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackMemberBootTime.setStatus(_A)
_ExtremeStackingPortTable_Object=MibTable
extremeStackingPortTable=_ExtremeStackingPortTable_Object((1,3,6,1,4,1,1916,1,33,3))
if mibBuilder.loadTexts:extremeStackingPortTable.setStatus(_A)
_ExtremeStackingPortEntry_Object=MibTableRow
extremeStackingPortEntry=_ExtremeStackingPortEntry_Object((1,3,6,1,4,1,1916,1,33,3,1))
extremeStackingPortEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:extremeStackingPortEntry.setStatus(_A)
class _ExtremeStackingPortIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ExtremeStackingPortIfIndex_Type.__name__=_C
_ExtremeStackingPortIfIndex_Object=MibTableColumn
extremeStackingPortIfIndex=_ExtremeStackingPortIfIndex_Object((1,3,6,1,4,1,1916,1,33,3,1,1),_ExtremeStackingPortIfIndex_Type())
extremeStackingPortIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackingPortIfIndex.setStatus(_A)
_ExtremeStackingPortRemoteMac_Type=MacAddress
_ExtremeStackingPortRemoteMac_Object=MibTableColumn
extremeStackingPortRemoteMac=_ExtremeStackingPortRemoteMac_Object((1,3,6,1,4,1,1916,1,33,3,1,2),_ExtremeStackingPortRemoteMac_Type())
extremeStackingPortRemoteMac.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackingPortRemoteMac.setStatus(_A)
_ExtremeStackingPortLinkSpeed_Type=Unsigned32
_ExtremeStackingPortLinkSpeed_Object=MibTableColumn
extremeStackingPortLinkSpeed=_ExtremeStackingPortLinkSpeed_Object((1,3,6,1,4,1,1916,1,33,3,1,3),_ExtremeStackingPortLinkSpeed_Type())
extremeStackingPortLinkSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackingPortLinkSpeed.setStatus(_A)
class _ExtremeStackingPortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_ExtremeStackingPortLinkStatus_Type.__name__=_C
_ExtremeStackingPortLinkStatus_Object=MibTableColumn
extremeStackingPortLinkStatus=_ExtremeStackingPortLinkStatus_Object((1,3,6,1,4,1,1916,1,33,3,1,4),_ExtremeStackingPortLinkStatus_Type())
extremeStackingPortLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeStackingPortLinkStatus.setStatus(_A)
_ExtremeStackableTraps_ObjectIdentity=ObjectIdentity
extremeStackableTraps=_ExtremeStackableTraps_ObjectIdentity((1,3,6,1,4,1,1916,1,33,4))
_ExtremeStackTrapsPrefix_ObjectIdentity=ObjectIdentity
extremeStackTrapsPrefix=_ExtremeStackTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,33,4,0))
extremeStackMemberOverheat=NotificationType((1,3,6,1,4,1,1916,1,33,4,0,1))
extremeStackMemberOverheat.setObjects(*((_G,_O),(_G,_N),(_J,_K),(_D,_F)))
if mibBuilder.loadTexts:extremeStackMemberOverheat.setStatus(_A)
extremeStackMemberStatusChanged=NotificationType((1,3,6,1,4,1,1916,1,33,4,0,2))
extremeStackMemberStatusChanged.setObjects(*((_D,_F),(_D,_R)))
if mibBuilder.loadTexts:extremeStackMemberStatusChanged.setStatus(_A)
extremeStackingPortStatusChanged=NotificationType((1,3,6,1,4,1,1916,1,33,4,0,3))
extremeStackingPortStatusChanged.setObjects(*((_L,_M),(_D,_S),(_D,_T),(_D,_U)))
if mibBuilder.loadTexts:extremeStackingPortStatusChanged.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'extremeStackable':extremeStackable,'extremeStackDetection':extremeStackDetection,'extremeStackMemberTable':extremeStackMemberTable,'extremeStackMemberEntry':extremeStackMemberEntry,_F:extremeStackMemberSlotId,'extremeStackMemberType':extremeStackMemberType,_R:extremeStackMemberOperStatus,'extremeStackMemberRole':extremeStackMemberRole,'extremeStackMemberEntPhysicalIndex':extremeStackMemberEntPhysicalIndex,'extremeStackMemberMACAddress':extremeStackMemberMACAddress,'extremeStackMemberCurImageVersion':extremeStackMemberCurImageVersion,'extremeStackMemberPriImageVersion':extremeStackMemberPriImageVersion,'extremeStackMemberSecImageVersion':extremeStackMemberSecImageVersion,'extremeStackMemberBootRomVersion':extremeStackMemberBootRomVersion,'extremeStackMemberCurConfig':extremeStackMemberCurConfig,'extremeStackMemberConfigSelected':extremeStackMemberConfigSelected,'extremeStackMemberImageSelected':extremeStackMemberImageSelected,'extremeStackMemberStackPriority':extremeStackMemberStackPriority,'extremeStackMemberMgmtIpAddress':extremeStackMemberMgmtIpAddress,'extremeStackMemberSysLocation':extremeStackMemberSysLocation,'extremeStackMemberAutoConfig':extremeStackMemberAutoConfig,'extremeStackMemberStackStatus':extremeStackMemberStackStatus,'extremeStackMemberImageBooted':extremeStackMemberImageBooted,'extremeStackMemberBootTime':extremeStackMemberBootTime,'extremeStackingPortTable':extremeStackingPortTable,'extremeStackingPortEntry':extremeStackingPortEntry,_Q:extremeStackingPortIfIndex,_S:extremeStackingPortRemoteMac,_T:extremeStackingPortLinkSpeed,_U:extremeStackingPortLinkStatus,'extremeStackableTraps':extremeStackableTraps,'extremeStackTrapsPrefix':extremeStackTrapsPrefix,'extremeStackMemberOverheat':extremeStackMemberOverheat,'extremeStackMemberStatusChanged':extremeStackMemberStatusChanged,'extremeStackingPortStatusChanged':extremeStackingPortStatusChanged})