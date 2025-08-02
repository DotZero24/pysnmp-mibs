_H='dot1dBasePort'
_G='BRIDGE-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_G,_H)
ifIndex,=mibBuilder.importSymbols(_E,_F)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelPort=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,61))
_ZyxelPortSetup_ObjectIdentity=ObjectIdentity
zyxelPortSetup=_ZyxelPortSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,61,1))
_ZyxelPortTable_Object=MibTable
zyxelPortTable=_ZyxelPortTable_Object((1,3,6,1,4,1,890,1,15,3,61,1,1))
if mibBuilder.loadTexts:zyxelPortTable.setStatus(_A)
_ZyxelPortEntry_Object=MibTableRow
zyxelPortEntry=_ZyxelPortEntry_Object((1,3,6,1,4,1,890,1,15,3,61,1,1,1))
zyxelPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zyxelPortEntry.setStatus(_A)
class _ZyPortSpeedDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('auto',0),('speed10Half',1),('speed10Full',2),('speed100Half',3),('speed100Full',4),('speed1000Full',5),('speed10GFull',6),('speed12GFull',7),('speed40GFull',8),('speedAuto1000',9),('speedAuto10G',10),('speed2500Full',11),('speed5GFull',12),('speed10an',13),('speed100an',14)))
_ZyPortSpeedDuplex_Type.__name__=_B
_ZyPortSpeedDuplex_Object=MibTableColumn
zyPortSpeedDuplex=_ZyPortSpeedDuplex_Object((1,3,6,1,4,1,890,1,15,3,61,1,1,1,1),_ZyPortSpeedDuplex_Type())
zyPortSpeedDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPortSpeedDuplex.setStatus(_A)
class _ZyPortFlowControlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tx-rx',1),('disable',2),('tx',3),('rx',4)))
_ZyPortFlowControlState_Type.__name__=_B
_ZyPortFlowControlState_Object=MibTableColumn
zyPortFlowControlState=_ZyPortFlowControlState_Object((1,3,6,1,4,1,890,1,15,3,61,1,1,1,2),_ZyPortFlowControlState_Type())
zyPortFlowControlState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPortFlowControlState.setStatus(_A)
_ZyPortName_Type=DisplayString
_ZyPortName_Object=MibTableColumn
zyPortName=_ZyPortName_Object((1,3,6,1,4,1,890,1,15,3,61,1,1,1,3),_ZyPortName_Type())
zyPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPortName.setStatus(_A)
_ZyPortIntrusionLockState_Type=EnabledStatus
_ZyPortIntrusionLockState_Object=MibTableColumn
zyPortIntrusionLockState=_ZyPortIntrusionLockState_Object((1,3,6,1,4,1,890,1,15,3,61,1,1,1,4),_ZyPortIntrusionLockState_Type())
zyPortIntrusionLockState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPortIntrusionLockState.setStatus(_A)
class _ZyPortCX4CableLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('halfMeters',0),('oneMeters',1),('threeMeters',2),('fiveMeters',3),('tenMeters',4),('fifteenMeters',5)))
_ZyPortCX4CableLength_Type.__name__=_B
_ZyPortCX4CableLength_Object=MibTableColumn
zyPortCX4CableLength=_ZyPortCX4CableLength_Object((1,3,6,1,4,1,890,1,15,3,61,1,1,1,5),_ZyPortCX4CableLength_Type())
zyPortCX4CableLength.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPortCX4CableLength.setStatus(_A)
class _ZyPort10GMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('sfpPlus',0),('dac10g',1)))
_ZyPort10GMediaType_Type.__name__=_B
_ZyPort10GMediaType_Object=MibTableColumn
zyPort10GMediaType=_ZyPort10GMediaType_Object((1,3,6,1,4,1,890,1,15,3,61,1,1,1,6),_ZyPort10GMediaType_Type())
zyPort10GMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPort10GMediaType.setStatus(_A)
_ZyPortExtendRangeState_Type=EnabledStatus
_ZyPortExtendRangeState_Object=MibTableColumn
zyPortExtendRangeState=_ZyPortExtendRangeState_Object((1,3,6,1,4,1,890,1,15,3,61,1,1,1,7),_ZyPortExtendRangeState_Type())
zyPortExtendRangeState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPortExtendRangeState.setStatus(_A)
_ZyxelPortStatus_ObjectIdentity=ObjectIdentity
zyxelPortStatus=_ZyxelPortStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,61,2))
_ZyxelPortInfoTable_Object=MibTable
zyxelPortInfoTable=_ZyxelPortInfoTable_Object((1,3,6,1,4,1,890,1,15,3,61,2,1))
if mibBuilder.loadTexts:zyxelPortInfoTable.setStatus(_A)
_ZyxelPortInfoEntry_Object=MibTableRow
zyxelPortInfoEntry=_ZyxelPortInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,61,2,1,1))
zyxelPortInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:zyxelPortInfoEntry.setStatus(_A)
class _ZyPortModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('fastEthernet',0),('gigabitEthernet',1),('xgEthernet10000',2),('x1Ethernet40000',3)))
_ZyPortModuleType_Type.__name__=_B
_ZyPortModuleType_Object=MibTableColumn
zyPortModuleType=_ZyPortModuleType_Object((1,3,6,1,4,1,890,1,15,3,61,2,1,1,1),_ZyPortModuleType_Type())
zyPortModuleType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyPortModuleType.setStatus(_A)
class _ZyPortLinkUpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('down',0),('copper',1),('fiber',2),('xfp',3),('cx4',4)))
_ZyPortLinkUpType_Type.__name__=_B
_ZyPortLinkUpType_Object=MibTableColumn
zyPortLinkUpType=_ZyPortLinkUpType_Object((1,3,6,1,4,1,890,1,15,3,61,2,1,1,2),_ZyPortLinkUpType_Type())
zyPortLinkUpType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyPortLinkUpType.setStatus(_A)
class _ZyPortTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('underTesting',1),('success',2),('fail',3)))
_ZyPortTestStatus_Type.__name__=_B
_ZyPortTestStatus_Object=MibTableColumn
zyPortTestStatus=_ZyPortTestStatus_Object((1,3,6,1,4,1,890,1,15,3,61,2,1,1,3),_ZyPortTestStatus_Type())
zyPortTestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zyPortTestStatus.setStatus(_A)
_ZyPortCounterReset_Type=EnabledStatus
_ZyPortCounterReset_Object=MibTableColumn
zyPortCounterReset=_ZyPortCounterReset_Object((1,3,6,1,4,1,890,1,15,3,61,2,1,1,4),_ZyPortCounterReset_Type())
zyPortCounterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:zyPortCounterReset.setStatus(_A)
_ZyPortUtilizationRx_Type=Integer32
_ZyPortUtilizationRx_Object=MibTableColumn
zyPortUtilizationRx=_ZyPortUtilizationRx_Object((1,3,6,1,4,1,890,1,15,3,61,2,1,1,5),_ZyPortUtilizationRx_Type())
zyPortUtilizationRx.setMaxAccess(_D)
if mibBuilder.loadTexts:zyPortUtilizationRx.setStatus(_A)
_ZyPortUtilizationTx_Type=Integer32
_ZyPortUtilizationTx_Object=MibTableColumn
zyPortUtilizationTx=_ZyPortUtilizationTx_Object((1,3,6,1,4,1,890,1,15,3,61,2,1,1,6),_ZyPortUtilizationTx_Type())
zyPortUtilizationTx.setMaxAccess(_D)
if mibBuilder.loadTexts:zyPortUtilizationTx.setStatus(_A)
_ZyxelPortNotifications_ObjectIdentity=ObjectIdentity
zyxelPortNotifications=_ZyxelPortNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,61,3))
zyPortAutonegotiationFailed=NotificationType((1,3,6,1,4,1,890,1,15,3,61,3,1))
zyPortAutonegotiationFailed.setObjects((_E,_F))
if mibBuilder.loadTexts:zyPortAutonegotiationFailed.setStatus(_A)
zyPortIntrusionLock=NotificationType((1,3,6,1,4,1,890,1,15,3,61,3,2))
zyPortIntrusionLock.setObjects((_E,_F))
if mibBuilder.loadTexts:zyPortIntrusionLock.setStatus(_A)
zyPortAutonegotiationFailedRecovered=NotificationType((1,3,6,1,4,1,890,1,15,3,61,3,3))
zyPortAutonegotiationFailedRecovered.setObjects((_E,_F))
if mibBuilder.loadTexts:zyPortAutonegotiationFailedRecovered.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-PORT-MIB',**{'zyxelPort':zyxelPort,'zyxelPortSetup':zyxelPortSetup,'zyxelPortTable':zyxelPortTable,'zyxelPortEntry':zyxelPortEntry,'zyPortSpeedDuplex':zyPortSpeedDuplex,'zyPortFlowControlState':zyPortFlowControlState,'zyPortName':zyPortName,'zyPortIntrusionLockState':zyPortIntrusionLockState,'zyPortCX4CableLength':zyPortCX4CableLength,'zyPort10GMediaType':zyPort10GMediaType,'zyPortExtendRangeState':zyPortExtendRangeState,'zyxelPortStatus':zyxelPortStatus,'zyxelPortInfoTable':zyxelPortInfoTable,'zyxelPortInfoEntry':zyxelPortInfoEntry,'zyPortModuleType':zyPortModuleType,'zyPortLinkUpType':zyPortLinkUpType,'zyPortTestStatus':zyPortTestStatus,'zyPortCounterReset':zyPortCounterReset,'zyPortUtilizationRx':zyPortUtilizationRx,'zyPortUtilizationTx':zyPortUtilizationTx,'zyxelPortNotifications':zyxelPortNotifications,'zyPortAutonegotiationFailed':zyPortAutonegotiationFailed,'zyPortIntrusionLock':zyPortIntrusionLock,'zyPortAutonegotiationFailedRecovered':zyPortAutonegotiationFailedRecovered})