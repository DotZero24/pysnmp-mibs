_c='flSfpNotificationsGroup'
_b='flSfpMonitoringGroup'
_a='flSfpDeviceGroup'
_Z='flSfpAlarmStatusChange'
_Y='flSfpSupplyVoltage'
_X='flSfpBiasCurrent'
_W='flSfpTemperature'
_V='flSfpTxPower'
_U='flSfpRxPower'
_T='flSfpDdmSupport'
_S='flSfpRxWlFraction'
_R='flSfpRxWl'
_Q='flSfpTxWlFraction'
_P='flSfpTxWl'
_O='flSfpRange'
_N='flSfpMaxRate'
_M='flSfpType'
_L='flSfpSerialNumber'
_K='flSfpPartNumber'
_J='flSfpVendor'
_I='micro Watts'
_H='flSfpStatusLastChange'
_G='flSfpAlarmStatus'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='FIBROLAN-SFP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fibrolanGeneric,=mibBuilder.importSymbols('FIBROLAN-COMMON-MIB','fibrolanGeneric')
flDeviceNotifications,=mibBuilder.importSymbols('FIBROLAN-DEVICE-MIB','flDeviceNotifications')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
flSfp=ModuleIdentity((1,3,6,1,4,1,4467,1000,50))
if mibBuilder.loadTexts:flSfp.setRevisions(('2014-04-01 00:00',))
_FlSfpMIBObjects_ObjectIdentity=ObjectIdentity
flSfpMIBObjects=_FlSfpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4467,1000,50,1))
_FlSfpInfoTable_Object=MibTable
flSfpInfoTable=_FlSfpInfoTable_Object((1,3,6,1,4,1,4467,1000,50,1,1))
if mibBuilder.loadTexts:flSfpInfoTable.setStatus(_A)
_FlSfpInfoEntry_Object=MibTableRow
flSfpInfoEntry=_FlSfpInfoEntry_Object((1,3,6,1,4,1,4467,1000,50,1,1,1))
flSfpInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:flSfpInfoEntry.setStatus(_A)
_FlSfpVendor_Type=DisplayString
_FlSfpVendor_Object=MibTableColumn
flSfpVendor=_FlSfpVendor_Object((1,3,6,1,4,1,4467,1000,50,1,1,1,1),_FlSfpVendor_Type())
flSfpVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpVendor.setStatus(_A)
_FlSfpPartNumber_Type=DisplayString
_FlSfpPartNumber_Object=MibTableColumn
flSfpPartNumber=_FlSfpPartNumber_Object((1,3,6,1,4,1,4467,1000,50,1,1,1,2),_FlSfpPartNumber_Type())
flSfpPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpPartNumber.setStatus(_A)
_FlSfpSerialNumber_Type=DisplayString
_FlSfpSerialNumber_Object=MibTableColumn
flSfpSerialNumber=_FlSfpSerialNumber_Object((1,3,6,1,4,1,4467,1000,50,1,1,1,3),_FlSfpSerialNumber_Type())
flSfpSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpSerialNumber.setStatus(_A)
_FlSfpType_Type=DisplayString
_FlSfpType_Object=MibTableColumn
flSfpType=_FlSfpType_Object((1,3,6,1,4,1,4467,1000,50,1,1,1,4),_FlSfpType_Type())
flSfpType.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpType.setStatus(_A)
_FlSfpMaxRate_Type=Integer32
_FlSfpMaxRate_Object=MibTableColumn
flSfpMaxRate=_FlSfpMaxRate_Object((1,3,6,1,4,1,4467,1000,50,1,1,1,5),_FlSfpMaxRate_Type())
flSfpMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpMaxRate.setStatus(_A)
_FlSfpRange_Type=Integer32
_FlSfpRange_Object=MibTableColumn
flSfpRange=_FlSfpRange_Object((1,3,6,1,4,1,4467,1000,50,1,1,1,6),_FlSfpRange_Type())
flSfpRange.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpRange.setStatus(_A)
_FlSfpTxWl_Type=Integer32
_FlSfpTxWl_Object=MibTableColumn
flSfpTxWl=_FlSfpTxWl_Object((1,3,6,1,4,1,4467,1000,50,1,1,1,7),_FlSfpTxWl_Type())
flSfpTxWl.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpTxWl.setStatus(_A)
_FlSfpTxWlFraction_Type=Integer32
_FlSfpTxWlFraction_Object=MibTableColumn
flSfpTxWlFraction=_FlSfpTxWlFraction_Object((1,3,6,1,4,1,4467,1000,50,1,1,1,8),_FlSfpTxWlFraction_Type())
flSfpTxWlFraction.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpTxWlFraction.setStatus(_A)
_FlSfpRxWl_Type=Integer32
_FlSfpRxWl_Object=MibTableColumn
flSfpRxWl=_FlSfpRxWl_Object((1,3,6,1,4,1,4467,1000,50,1,1,1,9),_FlSfpRxWl_Type())
flSfpRxWl.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpRxWl.setStatus(_A)
_FlSfpRxWlFraction_Type=Integer32
_FlSfpRxWlFraction_Object=MibTableColumn
flSfpRxWlFraction=_FlSfpRxWlFraction_Object((1,3,6,1,4,1,4467,1000,50,1,1,1,10),_FlSfpRxWlFraction_Type())
flSfpRxWlFraction.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpRxWlFraction.setStatus(_A)
class _FlSfpDdmSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ddmSupported',1),('ddmNotSupported',2)))
_FlSfpDdmSupport_Type.__name__=_F
_FlSfpDdmSupport_Object=MibTableColumn
flSfpDdmSupport=_FlSfpDdmSupport_Object((1,3,6,1,4,1,4467,1000,50,1,1,1,11),_FlSfpDdmSupport_Type())
flSfpDdmSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpDdmSupport.setStatus(_A)
_FlSfpMonitoringTable_Object=MibTable
flSfpMonitoringTable=_FlSfpMonitoringTable_Object((1,3,6,1,4,1,4467,1000,50,1,2))
if mibBuilder.loadTexts:flSfpMonitoringTable.setStatus(_A)
_FlSfpMonitoringEntry_Object=MibTableRow
flSfpMonitoringEntry=_FlSfpMonitoringEntry_Object((1,3,6,1,4,1,4467,1000,50,1,2,1))
flSfpMonitoringEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:flSfpMonitoringEntry.setStatus(_A)
_FlSfpRxPower_Type=Integer32
_FlSfpRxPower_Object=MibTableColumn
flSfpRxPower=_FlSfpRxPower_Object((1,3,6,1,4,1,4467,1000,50,1,2,1,1),_FlSfpRxPower_Type())
flSfpRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpRxPower.setStatus(_A)
if mibBuilder.loadTexts:flSfpRxPower.setUnits(_I)
_FlSfpTxPower_Type=Integer32
_FlSfpTxPower_Object=MibTableColumn
flSfpTxPower=_FlSfpTxPower_Object((1,3,6,1,4,1,4467,1000,50,1,2,1,2),_FlSfpTxPower_Type())
flSfpTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpTxPower.setStatus(_A)
if mibBuilder.loadTexts:flSfpTxPower.setUnits(_I)
_FlSfpTemperature_Type=Integer32
_FlSfpTemperature_Object=MibTableColumn
flSfpTemperature=_FlSfpTemperature_Object((1,3,6,1,4,1,4467,1000,50,1,2,1,3),_FlSfpTemperature_Type())
flSfpTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpTemperature.setStatus(_A)
if mibBuilder.loadTexts:flSfpTemperature.setUnits('Degrees Celsius (oC)')
_FlSfpBiasCurrent_Type=Integer32
_FlSfpBiasCurrent_Object=MibTableColumn
flSfpBiasCurrent=_FlSfpBiasCurrent_Object((1,3,6,1,4,1,4467,1000,50,1,2,1,4),_FlSfpBiasCurrent_Type())
flSfpBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpBiasCurrent.setStatus(_A)
if mibBuilder.loadTexts:flSfpBiasCurrent.setUnits('milliampere')
_FlSfpSupplyVoltage_Type=Integer32
_FlSfpSupplyVoltage_Object=MibTableColumn
flSfpSupplyVoltage=_FlSfpSupplyVoltage_Object((1,3,6,1,4,1,4467,1000,50,1,2,1,5),_FlSfpSupplyVoltage_Type())
flSfpSupplyVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpSupplyVoltage.setStatus(_A)
if mibBuilder.loadTexts:flSfpSupplyVoltage.setUnits('millivolt')
class _FlSfpAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FlSfpAlarmStatus_Type.__name__=_F
_FlSfpAlarmStatus_Object=MibTableColumn
flSfpAlarmStatus=_FlSfpAlarmStatus_Object((1,3,6,1,4,1,4467,1000,50,1,2,1,6),_FlSfpAlarmStatus_Type())
flSfpAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpAlarmStatus.setStatus(_A)
_FlSfpStatusLastChange_Type=TimeStamp
_FlSfpStatusLastChange_Object=MibTableColumn
flSfpStatusLastChange=_FlSfpStatusLastChange_Object((1,3,6,1,4,1,4467,1000,50,1,2,1,7),_FlSfpStatusLastChange_Type())
flSfpStatusLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:flSfpStatusLastChange.setStatus(_A)
_FlSfpMIBConformance_ObjectIdentity=ObjectIdentity
flSfpMIBConformance=_FlSfpMIBConformance_ObjectIdentity((1,3,6,1,4,1,4467,1000,50,2))
_FlSfpMIBCompliances_ObjectIdentity=ObjectIdentity
flSfpMIBCompliances=_FlSfpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4467,1000,50,2,1))
_FlSfpMIBGroups_ObjectIdentity=ObjectIdentity
flSfpMIBGroups=_FlSfpMIBGroups_ObjectIdentity((1,3,6,1,4,1,4467,1000,50,2,2))
_FlSfpTraps_ObjectIdentity=ObjectIdentity
flSfpTraps=_FlSfpTraps_ObjectIdentity((1,3,6,1,4,1,4467,1000,50,10))
flSfpDeviceGroup=ObjectGroup((1,3,6,1,4,1,4467,1000,50,2,2,1))
flSfpDeviceGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:flSfpDeviceGroup.setStatus(_A)
flSfpMonitoringGroup=ObjectGroup((1,3,6,1,4,1,4467,1000,50,2,2,2))
flSfpMonitoringGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:flSfpMonitoringGroup.setStatus(_A)
flSfpPluggedIn=NotificationType((1,3,6,1,4,1,4467,1000,10,0,17))
if mibBuilder.loadTexts:flSfpPluggedIn.setStatus(_A)
flSfpUnplugged=NotificationType((1,3,6,1,4,1,4467,1000,10,0,18))
if mibBuilder.loadTexts:flSfpUnplugged.setStatus(_A)
flSfpAlarmStatusChange=NotificationType((1,3,6,1,4,1,4467,1000,50,10,1))
flSfpAlarmStatusChange.setObjects(*((_D,_E),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:flSfpAlarmStatusChange.setStatus(_A)
flSfpNotificationsGroup=NotificationGroup((1,3,6,1,4,1,4467,1000,50,2,2,3))
flSfpNotificationsGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:flSfpNotificationsGroup.setStatus(_A)
flSfpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4467,1000,50,2,1,1))
flSfpMIBCompliance.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:flSfpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'flSfpPluggedIn':flSfpPluggedIn,'flSfpUnplugged':flSfpUnplugged,'flSfp':flSfp,'flSfpMIBObjects':flSfpMIBObjects,'flSfpInfoTable':flSfpInfoTable,'flSfpInfoEntry':flSfpInfoEntry,_J:flSfpVendor,_K:flSfpPartNumber,_L:flSfpSerialNumber,_M:flSfpType,_N:flSfpMaxRate,_O:flSfpRange,_P:flSfpTxWl,_Q:flSfpTxWlFraction,_R:flSfpRxWl,_S:flSfpRxWlFraction,_T:flSfpDdmSupport,'flSfpMonitoringTable':flSfpMonitoringTable,'flSfpMonitoringEntry':flSfpMonitoringEntry,_U:flSfpRxPower,_V:flSfpTxPower,_W:flSfpTemperature,_X:flSfpBiasCurrent,_Y:flSfpSupplyVoltage,_G:flSfpAlarmStatus,_H:flSfpStatusLastChange,'flSfpMIBConformance':flSfpMIBConformance,'flSfpMIBCompliances':flSfpMIBCompliances,'flSfpMIBCompliance':flSfpMIBCompliance,'flSfpMIBGroups':flSfpMIBGroups,_a:flSfpDeviceGroup,_b:flSfpMonitoringGroup,_c:flSfpNotificationsGroup,'flSfpTraps':flSfpTraps,_Z:flSfpAlarmStatusChange})