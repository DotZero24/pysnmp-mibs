_o='bcsiIfMediaGroup'
_n='bcsiOptMonInfoMonGroup'
_m='bcsiOptMonLaneMonGroup'
_l='bcsiIfMediaSerialNumber'
_k='bcsiIfMediaPartNumber'
_j='bcsiIfMediaVersion'
_i='bcsiIfMediaVendorName'
_h='bcsiIfMediaType'
_g='bcsiOptMonTxBiasCurrent'
_f='bcsiOptMonRxPowerVal'
_e='bcsiOptMonRxPower'
_d='bcsiOptMonRxPowerStatus'
_c='bcsiOptMonTxPowerVal'
_b='bcsiOptMonTxPower'
_a='bcsiOptMonTxPowerStatus'
_Z='bcsiOptMonTemperature'
_Y='bcsiOptMonLaneTxBiasCurrent'
_X='bcsiOptMonLaneRxPowerVal'
_W='bcsiOptMonLaneRxPower'
_V='bcsiOptMonLaneRxPowerStatus'
_U='bcsiOptMonLaneTxPowerVal'
_T='bcsiOptMonLaneTxPower'
_S='bcsiOptMonLaneTxPowerStatus'
_R='bcsiOptMonLaneTemperature'
_Q='bcsiOptMonLaneNum'
_P='microWatt'
_O='lowAlarm'
_N='lowWarn'
_M='normal'
_L='highWarn'
_K='highAlarm'
_J='notApplicable'
_I='notSupported'
_H='ifIndex'
_G='IF-MIB'
_F='Integer32'
_E='SnmpAdminString'
_D='DisplayString'
_C='read-only'
_B='BROCADE-OPTICAL-MONITORING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules')
ifIndex,=mibBuilder.importSymbols(_G,_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
brocadeOpticalMonitoringMIB=ModuleIdentity((1,3,6,1,4,1,1588,3,1,8))
if mibBuilder.loadTexts:brocadeOpticalMonitoringMIB.setRevisions(('2019-09-23 00:00','2018-05-29 12:00','2016-11-23 00:00','2016-09-28 00:00'))
_BcsiOptMonNotifications_ObjectIdentity=ObjectIdentity
bcsiOptMonNotifications=_BcsiOptMonNotifications_ObjectIdentity((1,3,6,1,4,1,1588,3,1,8,0))
_BcsiOptMonObjects_ObjectIdentity=ObjectIdentity
bcsiOptMonObjects=_BcsiOptMonObjects_ObjectIdentity((1,3,6,1,4,1,1588,3,1,8,1))
_BcsiOptMonLaneTable_Object=MibTable
bcsiOptMonLaneTable=_BcsiOptMonLaneTable_Object((1,3,6,1,4,1,1588,3,1,8,1,1))
if mibBuilder.loadTexts:bcsiOptMonLaneTable.setStatus(_A)
_BcsiOptMonLaneEntry_Object=MibTableRow
bcsiOptMonLaneEntry=_BcsiOptMonLaneEntry_Object((1,3,6,1,4,1,1588,3,1,8,1,1,1))
bcsiOptMonLaneEntry.setIndexNames((0,_G,_H),(0,_B,_Q))
if mibBuilder.loadTexts:bcsiOptMonLaneEntry.setStatus(_A)
_BcsiOptMonLaneNum_Type=Unsigned32
_BcsiOptMonLaneNum_Object=MibTableColumn
bcsiOptMonLaneNum=_BcsiOptMonLaneNum_Object((1,3,6,1,4,1,1588,3,1,8,1,1,1,1),_BcsiOptMonLaneNum_Type())
bcsiOptMonLaneNum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bcsiOptMonLaneNum.setStatus(_A)
class _BcsiOptMonLaneTemperature_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BcsiOptMonLaneTemperature_Type.__name__=_E
_BcsiOptMonLaneTemperature_Object=MibTableColumn
bcsiOptMonLaneTemperature=_BcsiOptMonLaneTemperature_Object((1,3,6,1,4,1,1588,3,1,8,1,1,1,2),_BcsiOptMonLaneTemperature_Type())
bcsiOptMonLaneTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonLaneTemperature.setStatus(_A)
class _BcsiOptMonLaneTxPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_BcsiOptMonLaneTxPowerStatus_Type.__name__=_F
_BcsiOptMonLaneTxPowerStatus_Object=MibTableColumn
bcsiOptMonLaneTxPowerStatus=_BcsiOptMonLaneTxPowerStatus_Object((1,3,6,1,4,1,1588,3,1,8,1,1,1,3),_BcsiOptMonLaneTxPowerStatus_Type())
bcsiOptMonLaneTxPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonLaneTxPowerStatus.setStatus(_A)
class _BcsiOptMonLaneTxPower_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BcsiOptMonLaneTxPower_Type.__name__=_E
_BcsiOptMonLaneTxPower_Object=MibTableColumn
bcsiOptMonLaneTxPower=_BcsiOptMonLaneTxPower_Object((1,3,6,1,4,1,1588,3,1,8,1,1,1,4),_BcsiOptMonLaneTxPower_Type())
bcsiOptMonLaneTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonLaneTxPower.setStatus(_A)
_BcsiOptMonLaneTxPowerVal_Type=Unsigned32
_BcsiOptMonLaneTxPowerVal_Object=MibTableColumn
bcsiOptMonLaneTxPowerVal=_BcsiOptMonLaneTxPowerVal_Object((1,3,6,1,4,1,1588,3,1,8,1,1,1,5),_BcsiOptMonLaneTxPowerVal_Type())
bcsiOptMonLaneTxPowerVal.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonLaneTxPowerVal.setStatus(_A)
if mibBuilder.loadTexts:bcsiOptMonLaneTxPowerVal.setUnits(_P)
class _BcsiOptMonLaneRxPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_BcsiOptMonLaneRxPowerStatus_Type.__name__=_F
_BcsiOptMonLaneRxPowerStatus_Object=MibTableColumn
bcsiOptMonLaneRxPowerStatus=_BcsiOptMonLaneRxPowerStatus_Object((1,3,6,1,4,1,1588,3,1,8,1,1,1,6),_BcsiOptMonLaneRxPowerStatus_Type())
bcsiOptMonLaneRxPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonLaneRxPowerStatus.setStatus(_A)
class _BcsiOptMonLaneRxPower_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BcsiOptMonLaneRxPower_Type.__name__=_E
_BcsiOptMonLaneRxPower_Object=MibTableColumn
bcsiOptMonLaneRxPower=_BcsiOptMonLaneRxPower_Object((1,3,6,1,4,1,1588,3,1,8,1,1,1,7),_BcsiOptMonLaneRxPower_Type())
bcsiOptMonLaneRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonLaneRxPower.setStatus(_A)
_BcsiOptMonLaneRxPowerVal_Type=Unsigned32
_BcsiOptMonLaneRxPowerVal_Object=MibTableColumn
bcsiOptMonLaneRxPowerVal=_BcsiOptMonLaneRxPowerVal_Object((1,3,6,1,4,1,1588,3,1,8,1,1,1,8),_BcsiOptMonLaneRxPowerVal_Type())
bcsiOptMonLaneRxPowerVal.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonLaneRxPowerVal.setStatus(_A)
if mibBuilder.loadTexts:bcsiOptMonLaneRxPowerVal.setUnits(_P)
class _BcsiOptMonLaneTxBiasCurrent_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BcsiOptMonLaneTxBiasCurrent_Type.__name__=_E
_BcsiOptMonLaneTxBiasCurrent_Object=MibTableColumn
bcsiOptMonLaneTxBiasCurrent=_BcsiOptMonLaneTxBiasCurrent_Object((1,3,6,1,4,1,1588,3,1,8,1,1,1,9),_BcsiOptMonLaneTxBiasCurrent_Type())
bcsiOptMonLaneTxBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonLaneTxBiasCurrent.setStatus(_A)
_BcsiOptMonInfoTable_Object=MibTable
bcsiOptMonInfoTable=_BcsiOptMonInfoTable_Object((1,3,6,1,4,1,1588,3,1,8,1,2))
if mibBuilder.loadTexts:bcsiOptMonInfoTable.setStatus(_A)
_BcsiOptMonInfoEntry_Object=MibTableRow
bcsiOptMonInfoEntry=_BcsiOptMonInfoEntry_Object((1,3,6,1,4,1,1588,3,1,8,1,2,1))
bcsiOptMonInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:bcsiOptMonInfoEntry.setStatus(_A)
class _BcsiOptMonTemperature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BcsiOptMonTemperature_Type.__name__=_D
_BcsiOptMonTemperature_Object=MibTableColumn
bcsiOptMonTemperature=_BcsiOptMonTemperature_Object((1,3,6,1,4,1,1588,3,1,8,1,2,1,1),_BcsiOptMonTemperature_Type())
bcsiOptMonTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonTemperature.setStatus(_A)
class _BcsiOptMonTxPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_BcsiOptMonTxPowerStatus_Type.__name__=_F
_BcsiOptMonTxPowerStatus_Object=MibTableColumn
bcsiOptMonTxPowerStatus=_BcsiOptMonTxPowerStatus_Object((1,3,6,1,4,1,1588,3,1,8,1,2,1,2),_BcsiOptMonTxPowerStatus_Type())
bcsiOptMonTxPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonTxPowerStatus.setStatus(_A)
class _BcsiOptMonTxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BcsiOptMonTxPower_Type.__name__=_D
_BcsiOptMonTxPower_Object=MibTableColumn
bcsiOptMonTxPower=_BcsiOptMonTxPower_Object((1,3,6,1,4,1,1588,3,1,8,1,2,1,3),_BcsiOptMonTxPower_Type())
bcsiOptMonTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonTxPower.setStatus(_A)
_BcsiOptMonTxPowerVal_Type=Unsigned32
_BcsiOptMonTxPowerVal_Object=MibTableColumn
bcsiOptMonTxPowerVal=_BcsiOptMonTxPowerVal_Object((1,3,6,1,4,1,1588,3,1,8,1,2,1,4),_BcsiOptMonTxPowerVal_Type())
bcsiOptMonTxPowerVal.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonTxPowerVal.setStatus(_A)
if mibBuilder.loadTexts:bcsiOptMonTxPowerVal.setUnits(_P)
class _BcsiOptMonRxPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_BcsiOptMonRxPowerStatus_Type.__name__=_F
_BcsiOptMonRxPowerStatus_Object=MibTableColumn
bcsiOptMonRxPowerStatus=_BcsiOptMonRxPowerStatus_Object((1,3,6,1,4,1,1588,3,1,8,1,2,1,5),_BcsiOptMonRxPowerStatus_Type())
bcsiOptMonRxPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonRxPowerStatus.setStatus(_A)
class _BcsiOptMonRxPower_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BcsiOptMonRxPower_Type.__name__=_D
_BcsiOptMonRxPower_Object=MibTableColumn
bcsiOptMonRxPower=_BcsiOptMonRxPower_Object((1,3,6,1,4,1,1588,3,1,8,1,2,1,6),_BcsiOptMonRxPower_Type())
bcsiOptMonRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonRxPower.setStatus(_A)
_BcsiOptMonRxPowerVal_Type=Unsigned32
_BcsiOptMonRxPowerVal_Object=MibTableColumn
bcsiOptMonRxPowerVal=_BcsiOptMonRxPowerVal_Object((1,3,6,1,4,1,1588,3,1,8,1,2,1,7),_BcsiOptMonRxPowerVal_Type())
bcsiOptMonRxPowerVal.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonRxPowerVal.setStatus(_A)
if mibBuilder.loadTexts:bcsiOptMonRxPowerVal.setUnits(_P)
class _BcsiOptMonTxBiasCurrent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_BcsiOptMonTxBiasCurrent_Type.__name__=_D
_BcsiOptMonTxBiasCurrent_Object=MibTableColumn
bcsiOptMonTxBiasCurrent=_BcsiOptMonTxBiasCurrent_Object((1,3,6,1,4,1,1588,3,1,8,1,2,1,8),_BcsiOptMonTxBiasCurrent_Type())
bcsiOptMonTxBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiOptMonTxBiasCurrent.setStatus(_A)
_BcsiIfMediaInfoTable_Object=MibTable
bcsiIfMediaInfoTable=_BcsiIfMediaInfoTable_Object((1,3,6,1,4,1,1588,3,1,8,1,3))
if mibBuilder.loadTexts:bcsiIfMediaInfoTable.setStatus(_A)
_BcsiIfMediaInfoEntry_Object=MibTableRow
bcsiIfMediaInfoEntry=_BcsiIfMediaInfoEntry_Object((1,3,6,1,4,1,1588,3,1,8,1,3,1))
bcsiIfMediaInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:bcsiIfMediaInfoEntry.setStatus(_A)
class _BcsiIfMediaType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_BcsiIfMediaType_Type.__name__=_D
_BcsiIfMediaType_Object=MibTableColumn
bcsiIfMediaType=_BcsiIfMediaType_Object((1,3,6,1,4,1,1588,3,1,8,1,3,1,1),_BcsiIfMediaType_Type())
bcsiIfMediaType.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfMediaType.setStatus(_A)
class _BcsiIfMediaVendorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_BcsiIfMediaVendorName_Type.__name__=_D
_BcsiIfMediaVendorName_Object=MibTableColumn
bcsiIfMediaVendorName=_BcsiIfMediaVendorName_Object((1,3,6,1,4,1,1588,3,1,8,1,3,1,2),_BcsiIfMediaVendorName_Type())
bcsiIfMediaVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfMediaVendorName.setStatus(_A)
class _BcsiIfMediaVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_BcsiIfMediaVersion_Type.__name__=_D
_BcsiIfMediaVersion_Object=MibTableColumn
bcsiIfMediaVersion=_BcsiIfMediaVersion_Object((1,3,6,1,4,1,1588,3,1,8,1,3,1,3),_BcsiIfMediaVersion_Type())
bcsiIfMediaVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfMediaVersion.setStatus(_A)
class _BcsiIfMediaPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_BcsiIfMediaPartNumber_Type.__name__=_D
_BcsiIfMediaPartNumber_Object=MibTableColumn
bcsiIfMediaPartNumber=_BcsiIfMediaPartNumber_Object((1,3,6,1,4,1,1588,3,1,8,1,3,1,4),_BcsiIfMediaPartNumber_Type())
bcsiIfMediaPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfMediaPartNumber.setStatus(_A)
class _BcsiIfMediaSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_BcsiIfMediaSerialNumber_Type.__name__=_D
_BcsiIfMediaSerialNumber_Object=MibTableColumn
bcsiIfMediaSerialNumber=_BcsiIfMediaSerialNumber_Object((1,3,6,1,4,1,1588,3,1,8,1,3,1,5),_BcsiIfMediaSerialNumber_Type())
bcsiIfMediaSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:bcsiIfMediaSerialNumber.setStatus(_A)
_BcsiOptMonConformance_ObjectIdentity=ObjectIdentity
bcsiOptMonConformance=_BcsiOptMonConformance_ObjectIdentity((1,3,6,1,4,1,1588,3,1,8,2))
_BcsiOptMonCompliances_ObjectIdentity=ObjectIdentity
bcsiOptMonCompliances=_BcsiOptMonCompliances_ObjectIdentity((1,3,6,1,4,1,1588,3,1,8,2,1))
_BcsiOptMonGroups_ObjectIdentity=ObjectIdentity
bcsiOptMonGroups=_BcsiOptMonGroups_ObjectIdentity((1,3,6,1,4,1,1588,3,1,8,2,2))
bcsiOptMonLaneMonGroup=ObjectGroup((1,3,6,1,4,1,1588,3,1,8,2,2,1))
bcsiOptMonLaneMonGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:bcsiOptMonLaneMonGroup.setStatus(_A)
bcsiOptMonInfoMonGroup=ObjectGroup((1,3,6,1,4,1,1588,3,1,8,2,2,2))
bcsiOptMonInfoMonGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:bcsiOptMonInfoMonGroup.setStatus(_A)
bcsiIfMediaGroup=ObjectGroup((1,3,6,1,4,1,1588,3,1,8,2,2,3))
bcsiIfMediaGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:bcsiIfMediaGroup.setStatus(_A)
bcsiOptMonCompliance=ModuleCompliance((1,3,6,1,4,1,1588,3,1,8,2,1,1))
bcsiOptMonCompliance.setObjects(*((_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:bcsiOptMonCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'brocadeOpticalMonitoringMIB':brocadeOpticalMonitoringMIB,'bcsiOptMonNotifications':bcsiOptMonNotifications,'bcsiOptMonObjects':bcsiOptMonObjects,'bcsiOptMonLaneTable':bcsiOptMonLaneTable,'bcsiOptMonLaneEntry':bcsiOptMonLaneEntry,_Q:bcsiOptMonLaneNum,_R:bcsiOptMonLaneTemperature,_S:bcsiOptMonLaneTxPowerStatus,_T:bcsiOptMonLaneTxPower,_U:bcsiOptMonLaneTxPowerVal,_V:bcsiOptMonLaneRxPowerStatus,_W:bcsiOptMonLaneRxPower,_X:bcsiOptMonLaneRxPowerVal,_Y:bcsiOptMonLaneTxBiasCurrent,'bcsiOptMonInfoTable':bcsiOptMonInfoTable,'bcsiOptMonInfoEntry':bcsiOptMonInfoEntry,_Z:bcsiOptMonTemperature,_a:bcsiOptMonTxPowerStatus,_b:bcsiOptMonTxPower,_c:bcsiOptMonTxPowerVal,_d:bcsiOptMonRxPowerStatus,_e:bcsiOptMonRxPower,_f:bcsiOptMonRxPowerVal,_g:bcsiOptMonTxBiasCurrent,'bcsiIfMediaInfoTable':bcsiIfMediaInfoTable,'bcsiIfMediaInfoEntry':bcsiIfMediaInfoEntry,_h:bcsiIfMediaType,_i:bcsiIfMediaVendorName,_j:bcsiIfMediaVersion,_k:bcsiIfMediaPartNumber,_l:bcsiIfMediaSerialNumber,'bcsiOptMonConformance':bcsiOptMonConformance,'bcsiOptMonCompliances':bcsiOptMonCompliances,'bcsiOptMonCompliance':bcsiOptMonCompliance,'bcsiOptMonGroups':bcsiOptMonGroups,_m:bcsiOptMonLaneMonGroup,_n:bcsiOptMonInfoMonGroup,_o:bcsiIfMediaGroup})