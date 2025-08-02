_c='unknown'
_b='termModuleNotInstalled'
_a='iNBbFault'
_Z='iNBaFault'
_Y='psPowerID'
_X='psPowerSlotID'
_W='psPowerSlotStatusID'
_V='boardPowerID'
_U='boardPowerSlotID'
_T='disabled'
_S='enabled'
_R='remotePowerOff'
_Q='temperatureShutdown'
_P='overCurrentShutdown'
_O='boardPowerSlotStatusID'
_N='chPowerLineID'
_M='normal'
_L='reset'
_K='powerOn'
_J='powerOK'
_I='underVoltage'
_H='read-write'
_G='powerOff'
_F='overVoltage'
_E='overCurrent'
_D='CTRON-POWER-SUPPLY-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctps,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctps')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_ChPower_ObjectIdentity=ObjectIdentity
chPower=_ChPower_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,7,1))
class _ChPowerOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('powerAC',1),('powerACRedundant',2),('powerDC',3),('powerDCRedundant',4),('battery',5)))
_ChPowerOperationalStatus_Type.__name__=_C
_ChPowerOperationalStatus_Object=MibScalar
chPowerOperationalStatus=_ChPowerOperationalStatus_Object((1,3,6,1,4,1,52,4,1,1,7,1,1),_ChPowerOperationalStatus_Type())
chPowerOperationalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerOperationalStatus.setStatus(_A)
class _ChPowerMainVoltageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_E,2),(_F,3),(_I,4)))
_ChPowerMainVoltageStatus_Type.__name__=_C
_ChPowerMainVoltageStatus_Object=MibScalar
chPowerMainVoltageStatus=_ChPowerMainVoltageStatus_Object((1,3,6,1,4,1,52,4,1,1,7,1,2),_ChPowerMainVoltageStatus_Type())
chPowerMainVoltageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerMainVoltageStatus.setStatus(_A)
_ChPowerMainVoltage_Type=Integer32
_ChPowerMainVoltage_Object=MibScalar
chPowerMainVoltage=_ChPowerMainVoltage_Object((1,3,6,1,4,1,52,4,1,1,7,1,3),_ChPowerMainVoltage_Type())
chPowerMainVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerMainVoltage.setStatus(_A)
_ChPowerTotalSupply_Type=Integer32
_ChPowerTotalSupply_Object=MibScalar
chPowerTotalSupply=_ChPowerTotalSupply_Object((1,3,6,1,4,1,52,4,1,1,7,1,4),_ChPowerTotalSupply_Type())
chPowerTotalSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerTotalSupply.setStatus(_A)
_ChPowerTotalLoad_Type=Integer32
_ChPowerTotalLoad_Object=MibScalar
chPowerTotalLoad=_ChPowerTotalLoad_Object((1,3,6,1,4,1,52,4,1,1,7,1,5),_ChPowerTotalLoad_Type())
chPowerTotalLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerTotalLoad.setStatus(_A)
_ChPowerMaxSupply_Type=Integer32
_ChPowerMaxSupply_Object=MibScalar
chPowerMaxSupply=_ChPowerMaxSupply_Object((1,3,6,1,4,1,52,4,1,1,7,1,6),_ChPowerMaxSupply_Type())
chPowerMaxSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerMaxSupply.setStatus(_A)
_ChPowerMaxLoad_Type=Integer32
_ChPowerMaxLoad_Object=MibScalar
chPowerMaxLoad=_ChPowerMaxLoad_Object((1,3,6,1,4,1,52,4,1,1,7,1,7),_ChPowerMaxLoad_Type())
chPowerMaxLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerMaxLoad.setStatus(_A)
_ChPowerTable_Object=MibTable
chPowerTable=_ChPowerTable_Object((1,3,6,1,4,1,52,4,1,1,7,1,8))
if mibBuilder.loadTexts:chPowerTable.setStatus(_A)
_ChPowerEntry_Object=MibTableRow
chPowerEntry=_ChPowerEntry_Object((1,3,6,1,4,1,52,4,1,1,7,1,8,1))
chPowerEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:chPowerEntry.setStatus(_A)
_ChPowerLineID_Type=Integer32
_ChPowerLineID_Object=MibTableColumn
chPowerLineID=_ChPowerLineID_Object((1,3,6,1,4,1,52,4,1,1,7,1,8,1,1),_ChPowerLineID_Type())
chPowerLineID.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerLineID.setStatus(_A)
_ChPowerLineType_Type=ObjectIdentifier
_ChPowerLineType_Object=MibTableColumn
chPowerLineType=_ChPowerLineType_Object((1,3,6,1,4,1,52,4,1,1,7,1,8,1,2),_ChPowerLineType_Type())
chPowerLineType.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerLineType.setStatus(_A)
_ChPowerLineTotalSupply_Type=Integer32
_ChPowerLineTotalSupply_Object=MibTableColumn
chPowerLineTotalSupply=_ChPowerLineTotalSupply_Object((1,3,6,1,4,1,52,4,1,1,7,1,8,1,3),_ChPowerLineTotalSupply_Type())
chPowerLineTotalSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerLineTotalSupply.setStatus(_A)
_ChPowerLineTotalLoad_Type=Integer32
_ChPowerLineTotalLoad_Object=MibTableColumn
chPowerLineTotalLoad=_ChPowerLineTotalLoad_Object((1,3,6,1,4,1,52,4,1,1,7,1,8,1,4),_ChPowerLineTotalLoad_Type())
chPowerLineTotalLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerLineTotalLoad.setStatus(_A)
_ChPowerLineMaxSupply_Type=Integer32
_ChPowerLineMaxSupply_Object=MibTableColumn
chPowerLineMaxSupply=_ChPowerLineMaxSupply_Object((1,3,6,1,4,1,52,4,1,1,7,1,8,1,5),_ChPowerLineMaxSupply_Type())
chPowerLineMaxSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerLineMaxSupply.setStatus(_A)
_ChPowerLineMaxLoad_Type=Integer32
_ChPowerLineMaxLoad_Object=MibTableColumn
chPowerLineMaxLoad=_ChPowerLineMaxLoad_Object((1,3,6,1,4,1,52,4,1,1,7,1,8,1,6),_ChPowerLineMaxLoad_Type())
chPowerLineMaxLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerLineMaxLoad.setStatus(_A)
class _ChPowerDiagVoltageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_E,2),(_F,3),(_I,4)))
_ChPowerDiagVoltageStatus_Type.__name__=_C
_ChPowerDiagVoltageStatus_Object=MibScalar
chPowerDiagVoltageStatus=_ChPowerDiagVoltageStatus_Object((1,3,6,1,4,1,52,4,1,1,7,1,9),_ChPowerDiagVoltageStatus_Type())
chPowerDiagVoltageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerDiagVoltageStatus.setStatus(_A)
_ChPowerDiagVoltage_Type=Integer32
_ChPowerDiagVoltage_Object=MibScalar
chPowerDiagVoltage=_ChPowerDiagVoltage_Object((1,3,6,1,4,1,52,4,1,1,7,1,10),_ChPowerDiagVoltage_Type())
chPowerDiagVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:chPowerDiagVoltage.setStatus(_A)
_BoardPower_ObjectIdentity=ObjectIdentity
boardPower=_BoardPower_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,7,2))
_BoardPowerSlotStatusTable_Object=MibTable
boardPowerSlotStatusTable=_BoardPowerSlotStatusTable_Object((1,3,6,1,4,1,52,4,1,1,7,2,1))
if mibBuilder.loadTexts:boardPowerSlotStatusTable.setStatus(_A)
_BoardPowerSlotStatusEntry_Object=MibTableRow
boardPowerSlotStatusEntry=_BoardPowerSlotStatusEntry_Object((1,3,6,1,4,1,52,4,1,1,7,2,1,1))
boardPowerSlotStatusEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:boardPowerSlotStatusEntry.setStatus(_A)
_BoardPowerSlotStatusID_Type=Integer32
_BoardPowerSlotStatusID_Object=MibTableColumn
boardPowerSlotStatusID=_BoardPowerSlotStatusID_Object((1,3,6,1,4,1,52,4,1,1,7,2,1,1,1),_BoardPowerSlotStatusID_Type())
boardPowerSlotStatusID.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerSlotStatusID.setStatus(_A)
class _BoardPowerOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_K,1),(_G,2),(_L,3),(_F,4),(_I,5),(_E,6),(_P,7),(_Q,8),(_R,9),('powerConservationShutdown',10),('frontPanelPowerOff',11)))
_BoardPowerOperationalStatus_Type.__name__=_C
_BoardPowerOperationalStatus_Object=MibTableColumn
boardPowerOperationalStatus=_BoardPowerOperationalStatus_Object((1,3,6,1,4,1,52,4,1,1,7,2,1,1,2),_BoardPowerOperationalStatus_Type())
boardPowerOperationalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerOperationalStatus.setStatus(_A)
class _BoardPowerAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_G,2),(_L,3)))
_BoardPowerAdminStatus_Type.__name__=_C
_BoardPowerAdminStatus_Object=MibTableColumn
boardPowerAdminStatus=_BoardPowerAdminStatus_Object((1,3,6,1,4,1,52,4,1,1,7,2,1,1,3),_BoardPowerAdminStatus_Type())
boardPowerAdminStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:boardPowerAdminStatus.setStatus(_A)
class _BoardPowerLocalAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('localMode',1),('secureMode',2)))
_BoardPowerLocalAdminStatus_Type.__name__=_C
_BoardPowerLocalAdminStatus_Object=MibTableColumn
boardPowerLocalAdminStatus=_BoardPowerLocalAdminStatus_Object((1,3,6,1,4,1,52,4,1,1,7,2,1,1,4),_BoardPowerLocalAdminStatus_Type())
boardPowerLocalAdminStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:boardPowerLocalAdminStatus.setStatus(_A)
class _BoardPowerLocalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('resetRequest',1),('powerDownRequest',2),('powerOnRequest',3),(_M,4)))
_BoardPowerLocalStatus_Type.__name__=_C
_BoardPowerLocalStatus_Object=MibTableColumn
boardPowerLocalStatus=_BoardPowerLocalStatus_Object((1,3,6,1,4,1,52,4,1,1,7,2,1,1,5),_BoardPowerLocalStatus_Type())
boardPowerLocalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerLocalStatus.setStatus(_A)
class _BoardPowerShutdownAdmin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_BoardPowerShutdownAdmin_Type.__name__=_C
_BoardPowerShutdownAdmin_Object=MibTableColumn
boardPowerShutdownAdmin=_BoardPowerShutdownAdmin_Object((1,3,6,1,4,1,52,4,1,1,7,2,1,1,6),_BoardPowerShutdownAdmin_Type())
boardPowerShutdownAdmin.setMaxAccess(_H)
if mibBuilder.loadTexts:boardPowerShutdownAdmin.setStatus(_A)
class _BoardPowerPriority_Type(Integer32):defaultValue=14;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_BoardPowerPriority_Type.__name__=_C
_BoardPowerPriority_Object=MibTableColumn
boardPowerPriority=_BoardPowerPriority_Object((1,3,6,1,4,1,52,4,1,1,7,2,1,1,7),_BoardPowerPriority_Type())
boardPowerPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:boardPowerPriority.setStatus(_A)
_BoardPowerMaxInputPower_Type=Integer32
_BoardPowerMaxInputPower_Object=MibTableColumn
boardPowerMaxInputPower=_BoardPowerMaxInputPower_Object((1,3,6,1,4,1,52,4,1,1,7,2,1,1,8),_BoardPowerMaxInputPower_Type())
boardPowerMaxInputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerMaxInputPower.setStatus(_A)
class _BoardPowerManagement_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,7)));namedValues=NamedValues(*((_T,1),(_S,2),('not-supported',7)))
_BoardPowerManagement_Type.__name__=_C
_BoardPowerManagement_Object=MibTableColumn
boardPowerManagement=_BoardPowerManagement_Object((1,3,6,1,4,1,52,4,1,1,7,2,1,1,9),_BoardPowerManagement_Type())
boardPowerManagement.setMaxAccess(_H)
if mibBuilder.loadTexts:boardPowerManagement.setStatus(_A)
_BoardPowerSlotTable_Object=MibTable
boardPowerSlotTable=_BoardPowerSlotTable_Object((1,3,6,1,4,1,52,4,1,1,7,2,2))
if mibBuilder.loadTexts:boardPowerSlotTable.setStatus(_A)
_BoardPowerSlotEntry_Object=MibTableRow
boardPowerSlotEntry=_BoardPowerSlotEntry_Object((1,3,6,1,4,1,52,4,1,1,7,2,2,1))
boardPowerSlotEntry.setIndexNames((0,_D,_U),(0,_D,_V))
if mibBuilder.loadTexts:boardPowerSlotEntry.setStatus(_A)
_BoardPowerSlotID_Type=Integer32
_BoardPowerSlotID_Object=MibTableColumn
boardPowerSlotID=_BoardPowerSlotID_Object((1,3,6,1,4,1,52,4,1,1,7,2,2,1,1),_BoardPowerSlotID_Type())
boardPowerSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerSlotID.setStatus(_A)
_BoardPowerID_Type=Integer32
_BoardPowerID_Object=MibTableColumn
boardPowerID=_BoardPowerID_Object((1,3,6,1,4,1,52,4,1,1,7,2,2,1,2),_BoardPowerID_Type())
boardPowerID.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerID.setStatus(_A)
_BoardPowerType_Type=ObjectIdentifier
_BoardPowerType_Object=MibTableColumn
boardPowerType=_BoardPowerType_Object((1,3,6,1,4,1,52,4,1,1,7,2,2,1,3),_BoardPowerType_Type())
boardPowerType.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerType.setStatus(_A)
class _BoardPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_G,2),(_E,3),(_F,4),(_I,5)))
_BoardPowerStatus_Type.__name__=_C
_BoardPowerStatus_Object=MibTableColumn
boardPowerStatus=_BoardPowerStatus_Object((1,3,6,1,4,1,52,4,1,1,7,2,2,1,4),_BoardPowerStatus_Type())
boardPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerStatus.setStatus(_A)
_BoardPowerVoltage_Type=Integer32
_BoardPowerVoltage_Object=MibTableColumn
boardPowerVoltage=_BoardPowerVoltage_Object((1,3,6,1,4,1,52,4,1,1,7,2,2,1,5),_BoardPowerVoltage_Type())
boardPowerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerVoltage.setStatus(_A)
_BoardPowerCurrent_Type=Integer32
_BoardPowerCurrent_Object=MibTableColumn
boardPowerCurrent=_BoardPowerCurrent_Object((1,3,6,1,4,1,52,4,1,1,7,2,2,1,6),_BoardPowerCurrent_Type())
boardPowerCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerCurrent.setStatus(_A)
_BoardPowerMaxVoltage_Type=Integer32
_BoardPowerMaxVoltage_Object=MibTableColumn
boardPowerMaxVoltage=_BoardPowerMaxVoltage_Object((1,3,6,1,4,1,52,4,1,1,7,2,2,1,7),_BoardPowerMaxVoltage_Type())
boardPowerMaxVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerMaxVoltage.setStatus(_A)
_BoardPowerMinVoltage_Type=Integer32
_BoardPowerMinVoltage_Object=MibTableColumn
boardPowerMinVoltage=_BoardPowerMinVoltage_Object((1,3,6,1,4,1,52,4,1,1,7,2,2,1,8),_BoardPowerMinVoltage_Type())
boardPowerMinVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerMinVoltage.setStatus(_A)
_BoardPowerMaxPower_Type=Integer32
_BoardPowerMaxPower_Object=MibTableColumn
boardPowerMaxPower=_BoardPowerMaxPower_Object((1,3,6,1,4,1,52,4,1,1,7,2,2,1,9),_BoardPowerMaxPower_Type())
boardPowerMaxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPowerMaxPower.setStatus(_A)
_PsPower_ObjectIdentity=ObjectIdentity
psPower=_PsPower_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,7,3))
_PsPowerSlotStatusTable_Object=MibTable
psPowerSlotStatusTable=_PsPowerSlotStatusTable_Object((1,3,6,1,4,1,52,4,1,1,7,3,1))
if mibBuilder.loadTexts:psPowerSlotStatusTable.setStatus(_A)
_PsPowerSlotStatusEntry_Object=MibTableRow
psPowerSlotStatusEntry=_PsPowerSlotStatusEntry_Object((1,3,6,1,4,1,52,4,1,1,7,3,1,1))
psPowerSlotStatusEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:psPowerSlotStatusEntry.setStatus(_A)
_PsPowerSlotStatusID_Type=Integer32
_PsPowerSlotStatusID_Object=MibTableColumn
psPowerSlotStatusID=_PsPowerSlotStatusID_Object((1,3,6,1,4,1,52,4,1,1,7,3,1,1,1),_PsPowerSlotStatusID_Type())
psPowerSlotStatusID.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerSlotStatusID.setStatus(_A)
class _PsPowerOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_K,1),(_G,2),(_L,3),(_F,4),(_I,5),(_E,6),(_P,7),(_Q,8),(_R,9)))
_PsPowerOperationalStatus_Type.__name__=_C
_PsPowerOperationalStatus_Object=MibTableColumn
psPowerOperationalStatus=_PsPowerOperationalStatus_Object((1,3,6,1,4,1,52,4,1,1,7,3,1,1,2),_PsPowerOperationalStatus_Type())
psPowerOperationalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerOperationalStatus.setStatus(_A)
class _PsPowerAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_G,2)))
_PsPowerAdminStatus_Type.__name__=_C
_PsPowerAdminStatus_Object=MibTableColumn
psPowerAdminStatus=_PsPowerAdminStatus_Object((1,3,6,1,4,1,52,4,1,1,7,3,1,1,3),_PsPowerAdminStatus_Type())
psPowerAdminStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:psPowerAdminStatus.setStatus(_A)
_PsPowerMaxOutputPower_Type=Integer32
_PsPowerMaxOutputPower_Object=MibTableColumn
psPowerMaxOutputPower=_PsPowerMaxOutputPower_Object((1,3,6,1,4,1,52,4,1,1,7,3,1,1,4),_PsPowerMaxOutputPower_Type())
psPowerMaxOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerMaxOutputPower.setStatus(_A)
_PsPowerSlotTable_Object=MibTable
psPowerSlotTable=_PsPowerSlotTable_Object((1,3,6,1,4,1,52,4,1,1,7,3,2))
if mibBuilder.loadTexts:psPowerSlotTable.setStatus(_A)
_PsPowerSlotEntry_Object=MibTableRow
psPowerSlotEntry=_PsPowerSlotEntry_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1))
psPowerSlotEntry.setIndexNames((0,_D,_X),(0,_D,_Y))
if mibBuilder.loadTexts:psPowerSlotEntry.setStatus(_A)
_PsPowerSlotID_Type=Integer32
_PsPowerSlotID_Object=MibTableColumn
psPowerSlotID=_PsPowerSlotID_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1,1),_PsPowerSlotID_Type())
psPowerSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerSlotID.setStatus(_A)
_PsPowerID_Type=Integer32
_PsPowerID_Object=MibTableColumn
psPowerID=_PsPowerID_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1,2),_PsPowerID_Type())
psPowerID.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerID.setStatus(_A)
_PsPowerType_Type=ObjectIdentifier
_PsPowerType_Object=MibTableColumn
psPowerType=_PsPowerType_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1,3),_PsPowerType_Type())
psPowerType.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerType.setStatus(_A)
class _PsPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_G,2),(_E,3),(_F,4),(_I,5)))
_PsPowerStatus_Type.__name__=_C
_PsPowerStatus_Object=MibTableColumn
psPowerStatus=_PsPowerStatus_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1,4),_PsPowerStatus_Type())
psPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerStatus.setStatus(_A)
class _PsPowerAdmin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_G,2)))
_PsPowerAdmin_Type.__name__=_C
_PsPowerAdmin_Object=MibTableColumn
psPowerAdmin=_PsPowerAdmin_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1,5),_PsPowerAdmin_Type())
psPowerAdmin.setMaxAccess(_H)
if mibBuilder.loadTexts:psPowerAdmin.setStatus(_A)
_PsPowerVoltage_Type=Integer32
_PsPowerVoltage_Object=MibTableColumn
psPowerVoltage=_PsPowerVoltage_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1,6),_PsPowerVoltage_Type())
psPowerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerVoltage.setStatus(_A)
_PsPowerCurrent_Type=Integer32
_PsPowerCurrent_Object=MibTableColumn
psPowerCurrent=_PsPowerCurrent_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1,7),_PsPowerCurrent_Type())
psPowerCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerCurrent.setStatus(_A)
_PsPowerLineFrequency_Type=Integer32
_PsPowerLineFrequency_Object=MibTableColumn
psPowerLineFrequency=_PsPowerLineFrequency_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1,8),_PsPowerLineFrequency_Type())
psPowerLineFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerLineFrequency.setStatus(_A)
_PsPowerMaxVoltage_Type=Integer32
_PsPowerMaxVoltage_Object=MibTableColumn
psPowerMaxVoltage=_PsPowerMaxVoltage_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1,9),_PsPowerMaxVoltage_Type())
psPowerMaxVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerMaxVoltage.setStatus(_A)
_PsPowerMinVoltage_Type=Integer32
_PsPowerMinVoltage_Object=MibTableColumn
psPowerMinVoltage=_PsPowerMinVoltage_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1,10),_PsPowerMinVoltage_Type())
psPowerMinVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerMinVoltage.setStatus(_A)
_PsPowerMaxPower_Type=Integer32
_PsPowerMaxPower_Object=MibTableColumn
psPowerMaxPower=_PsPowerMaxPower_Object((1,3,6,1,4,1,52,4,1,1,7,3,2,1,11),_PsPowerMaxPower_Type())
psPowerMaxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:psPowerMaxPower.setStatus(_A)
_BbuPower_ObjectIdentity=ObjectIdentity
bbuPower=_BbuPower_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,7,4))
_TermPower_ObjectIdentity=ObjectIdentity
termPower=_TermPower_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,7,5))
class _TermPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_J,1),(_E,2),(_F,3),('underVolatge',4),('overPower',5)))
_TermPowerStatus_Type.__name__=_C
_TermPowerStatus_Object=MibScalar
termPowerStatus=_TermPowerStatus_Object((1,3,6,1,4,1,52,4,1,1,7,5,1),_TermPowerStatus_Type())
termPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:termPowerStatus.setStatus(_A)
_TermPowerVoltage_Type=Integer32
_TermPowerVoltage_Object=MibScalar
termPowerVoltage=_TermPowerVoltage_Object((1,3,6,1,4,1,52,4,1,1,7,5,2),_TermPowerVoltage_Type())
termPowerVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:termPowerVoltage.setStatus(_A)
_TermPowerCurrent_Type=Integer32
_TermPowerCurrent_Object=MibScalar
termPowerCurrent=_TermPowerCurrent_Object((1,3,6,1,4,1,52,4,1,1,7,5,3),_TermPowerCurrent_Type())
termPowerCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:termPowerCurrent.setStatus(_A)
class _TermPowerModule1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_M,1),(_Z,2),(_a,3),('fault',4),(_b,5),(_c,6)))
_TermPowerModule1Status_Type.__name__=_C
_TermPowerModule1Status_Object=MibScalar
termPowerModule1Status=_TermPowerModule1Status_Object((1,3,6,1,4,1,52,4,1,1,7,5,4),_TermPowerModule1Status_Type())
termPowerModule1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:termPowerModule1Status.setStatus(_A)
class _TermPowerModule2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_M,1),(_Z,2),(_a,3),('fault',4),(_b,5),(_c,6)))
_TermPowerModule2Status_Type.__name__=_C
_TermPowerModule2Status_Object=MibScalar
termPowerModule2Status=_TermPowerModule2Status_Object((1,3,6,1,4,1,52,4,1,1,7,5,5),_TermPowerModule2Status_Type())
termPowerModule2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:termPowerModule2Status.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'chPower':chPower,'chPowerOperationalStatus':chPowerOperationalStatus,'chPowerMainVoltageStatus':chPowerMainVoltageStatus,'chPowerMainVoltage':chPowerMainVoltage,'chPowerTotalSupply':chPowerTotalSupply,'chPowerTotalLoad':chPowerTotalLoad,'chPowerMaxSupply':chPowerMaxSupply,'chPowerMaxLoad':chPowerMaxLoad,'chPowerTable':chPowerTable,'chPowerEntry':chPowerEntry,_N:chPowerLineID,'chPowerLineType':chPowerLineType,'chPowerLineTotalSupply':chPowerLineTotalSupply,'chPowerLineTotalLoad':chPowerLineTotalLoad,'chPowerLineMaxSupply':chPowerLineMaxSupply,'chPowerLineMaxLoad':chPowerLineMaxLoad,'chPowerDiagVoltageStatus':chPowerDiagVoltageStatus,'chPowerDiagVoltage':chPowerDiagVoltage,'boardPower':boardPower,'boardPowerSlotStatusTable':boardPowerSlotStatusTable,'boardPowerSlotStatusEntry':boardPowerSlotStatusEntry,_O:boardPowerSlotStatusID,'boardPowerOperationalStatus':boardPowerOperationalStatus,'boardPowerAdminStatus':boardPowerAdminStatus,'boardPowerLocalAdminStatus':boardPowerLocalAdminStatus,'boardPowerLocalStatus':boardPowerLocalStatus,'boardPowerShutdownAdmin':boardPowerShutdownAdmin,'boardPowerPriority':boardPowerPriority,'boardPowerMaxInputPower':boardPowerMaxInputPower,'boardPowerManagement':boardPowerManagement,'boardPowerSlotTable':boardPowerSlotTable,'boardPowerSlotEntry':boardPowerSlotEntry,_U:boardPowerSlotID,_V:boardPowerID,'boardPowerType':boardPowerType,'boardPowerStatus':boardPowerStatus,'boardPowerVoltage':boardPowerVoltage,'boardPowerCurrent':boardPowerCurrent,'boardPowerMaxVoltage':boardPowerMaxVoltage,'boardPowerMinVoltage':boardPowerMinVoltage,'boardPowerMaxPower':boardPowerMaxPower,'psPower':psPower,'psPowerSlotStatusTable':psPowerSlotStatusTable,'psPowerSlotStatusEntry':psPowerSlotStatusEntry,_W:psPowerSlotStatusID,'psPowerOperationalStatus':psPowerOperationalStatus,'psPowerAdminStatus':psPowerAdminStatus,'psPowerMaxOutputPower':psPowerMaxOutputPower,'psPowerSlotTable':psPowerSlotTable,'psPowerSlotEntry':psPowerSlotEntry,_X:psPowerSlotID,_Y:psPowerID,'psPowerType':psPowerType,'psPowerStatus':psPowerStatus,'psPowerAdmin':psPowerAdmin,'psPowerVoltage':psPowerVoltage,'psPowerCurrent':psPowerCurrent,'psPowerLineFrequency':psPowerLineFrequency,'psPowerMaxVoltage':psPowerMaxVoltage,'psPowerMinVoltage':psPowerMinVoltage,'psPowerMaxPower':psPowerMaxPower,'bbuPower':bbuPower,'termPower':termPower,'termPowerStatus':termPowerStatus,'termPowerVoltage':termPowerVoltage,'termPowerCurrent':termPowerCurrent,'termPowerModule1Status':termPowerModule1Status,'termPowerModule2Status':termPowerModule2Status})