_S='os10FanIndex'
_R='os10FanTrayIndex'
_Q='os10PowerSupplyIndex'
_P='os10CardIndex'
_O='degrees Centigrade'
_N='OctetString'
_M='os10ChassisIndex'
_L='Integer32'
_K='accessible-for-notify'
_J='not-accessible'
_I='os10AlmVarPort'
_H='os10AlmVarSlot'
_G='os10AlmVarChassisId'
_F='os10AlmVarString'
_E='os10AlmVarInteger'
_D='DisplayString'
_C='read-only'
_B='DELLEMC-OS10-CHASSIS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
os10,=mibBuilder.importSymbols('DELLEMC-OS10-SMI-MIB','os10')
Os10CardOperStatus,Os10ChassisDefType,Os10CmnOperStatus,Os10DeviceType,Os10SystemCardType=mibBuilder.importSymbols('DELLEMC-OS10-TC-MIB','Os10CardOperStatus','Os10ChassisDefType','Os10CmnOperStatus','Os10DeviceType','Os10SystemCardType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','TextualConvention')
os10ChassisMib=ModuleIdentity((1,3,6,1,4,1,674,11000,5000,100,4))
if mibBuilder.loadTexts:os10ChassisMib.setRevisions(('2017-06-21 12:00','2017-01-25 12:00'))
_Os10SysObject_ObjectIdentity=ObjectIdentity
os10SysObject=_Os10SysObject_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,4,1))
_Os10ChassisObject_ObjectIdentity=ObjectIdentity
os10ChassisObject=_Os10ChassisObject_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,4,1,1))
_Os10NumChassis_Type=Unsigned32
_Os10NumChassis_Object=MibScalar
os10NumChassis=_Os10NumChassis_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,1),_Os10NumChassis_Type())
os10NumChassis.setMaxAccess(_C)
if mibBuilder.loadTexts:os10NumChassis.setStatus(_A)
_Os10MaxNumChassis_Type=Unsigned32
_Os10MaxNumChassis_Object=MibScalar
os10MaxNumChassis=_Os10MaxNumChassis_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,2),_Os10MaxNumChassis_Type())
os10MaxNumChassis.setMaxAccess(_C)
if mibBuilder.loadTexts:os10MaxNumChassis.setStatus(_A)
_Os10ChassisTable_Object=MibTable
os10ChassisTable=_Os10ChassisTable_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3))
if mibBuilder.loadTexts:os10ChassisTable.setStatus(_A)
_Os10ChassisEntry_Object=MibTableRow
os10ChassisEntry=_Os10ChassisEntry_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1))
os10ChassisEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:os10ChassisEntry.setStatus(_A)
_Os10ChassisIndex_Type=Unsigned32
_Os10ChassisIndex_Object=MibTableColumn
os10ChassisIndex=_Os10ChassisIndex_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,1),_Os10ChassisIndex_Type())
os10ChassisIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:os10ChassisIndex.setStatus(_A)
_Os10ChassisType_Type=Os10ChassisDefType
_Os10ChassisType_Object=MibTableColumn
os10ChassisType=_Os10ChassisType_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,2),_Os10ChassisType_Type())
os10ChassisType.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisType.setStatus(_A)
_Os10ChassisMacAddr_Type=MacAddress
_Os10ChassisMacAddr_Object=MibTableColumn
os10ChassisMacAddr=_Os10ChassisMacAddr_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,3),_Os10ChassisMacAddr_Type())
os10ChassisMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisMacAddr.setStatus(_A)
class _Os10ChassisPartNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Os10ChassisPartNum_Type.__name__=_D
_Os10ChassisPartNum_Object=MibTableColumn
os10ChassisPartNum=_Os10ChassisPartNum_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,4),_Os10ChassisPartNum_Type())
os10ChassisPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisPartNum.setStatus(_A)
class _Os10ChassisPPID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_Os10ChassisPPID_Type.__name__=_D
_Os10ChassisPPID_Object=MibTableColumn
os10ChassisPPID=_Os10ChassisPPID_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,5),_Os10ChassisPPID_Type())
os10ChassisPPID.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisPPID.setStatus(_A)
class _Os10ChassisHwRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Os10ChassisHwRev_Type.__name__=_D
_Os10ChassisHwRev_Object=MibTableColumn
os10ChassisHwRev=_Os10ChassisHwRev_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,6),_Os10ChassisHwRev_Type())
os10ChassisHwRev.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisHwRev.setStatus(_A)
class _Os10ChassisServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_Os10ChassisServiceTag_Type.__name__=_D
_Os10ChassisServiceTag_Object=MibTableColumn
os10ChassisServiceTag=_Os10ChassisServiceTag_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,7),_Os10ChassisServiceTag_Type())
os10ChassisServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisServiceTag.setStatus(_A)
class _Os10ChassisExpServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_Os10ChassisExpServiceCode_Type.__name__=_D
_Os10ChassisExpServiceCode_Object=MibTableColumn
os10ChassisExpServiceCode=_Os10ChassisExpServiceCode_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,8),_Os10ChassisExpServiceCode_Type())
os10ChassisExpServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisExpServiceCode.setStatus(_A)
_Os10ChassisNumFanTrays_Type=Unsigned32
_Os10ChassisNumFanTrays_Object=MibTableColumn
os10ChassisNumFanTrays=_Os10ChassisNumFanTrays_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,9),_Os10ChassisNumFanTrays_Type())
os10ChassisNumFanTrays.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisNumFanTrays.setStatus(_A)
_Os10ChassisNumPowerSupplies_Type=Unsigned32
_Os10ChassisNumPowerSupplies_Object=MibTableColumn
os10ChassisNumPowerSupplies=_Os10ChassisNumPowerSupplies_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,10),_Os10ChassisNumPowerSupplies_Type())
os10ChassisNumPowerSupplies.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisNumPowerSupplies.setStatus(_A)
_Os10ChassisTemp_Type=Integer32
_Os10ChassisTemp_Object=MibTableColumn
os10ChassisTemp=_Os10ChassisTemp_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,11),_Os10ChassisTemp_Type())
os10ChassisTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisTemp.setStatus(_A)
if mibBuilder.loadTexts:os10ChassisTemp.setUnits(_O)
class _Os10ChassisProductBase_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Os10ChassisProductBase_Type.__name__=_D
_Os10ChassisProductBase_Object=MibTableColumn
os10ChassisProductBase=_Os10ChassisProductBase_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,12),_Os10ChassisProductBase_Type())
os10ChassisProductBase.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisProductBase.setStatus(_A)
class _Os10ChassisProductSN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Os10ChassisProductSN_Type.__name__=_D
_Os10ChassisProductSN_Object=MibTableColumn
os10ChassisProductSN=_Os10ChassisProductSN_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,13),_Os10ChassisProductSN_Type())
os10ChassisProductSN.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisProductSN.setStatus(_A)
class _Os10ChassisProductPN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Os10ChassisProductPN_Type.__name__=_D
_Os10ChassisProductPN_Object=MibTableColumn
os10ChassisProductPN=_Os10ChassisProductPN_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,3,1,14),_Os10ChassisProductPN_Type())
os10ChassisProductPN.setMaxAccess(_C)
if mibBuilder.loadTexts:os10ChassisProductPN.setStatus(_A)
_Os10CardTable_Object=MibTable
os10CardTable=_Os10CardTable_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4))
if mibBuilder.loadTexts:os10CardTable.setStatus(_A)
_Os10CardEntry_Object=MibTableRow
os10CardEntry=_Os10CardEntry_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4,1))
os10CardEntry.setIndexNames((0,_B,_M),(0,_B,_P))
if mibBuilder.loadTexts:os10CardEntry.setStatus(_A)
_Os10CardIndex_Type=Unsigned32
_Os10CardIndex_Object=MibTableColumn
os10CardIndex=_Os10CardIndex_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4,1,1),_Os10CardIndex_Type())
os10CardIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:os10CardIndex.setStatus(_A)
_Os10CardType_Type=Os10SystemCardType
_Os10CardType_Object=MibTableColumn
os10CardType=_Os10CardType_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4,1,2),_Os10CardType_Type())
os10CardType.setMaxAccess(_C)
if mibBuilder.loadTexts:os10CardType.setStatus(_A)
class _Os10CardDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,120))
_Os10CardDescription_Type.__name__=_D
_Os10CardDescription_Object=MibTableColumn
os10CardDescription=_Os10CardDescription_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4,1,3),_Os10CardDescription_Type())
os10CardDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:os10CardDescription.setStatus(_A)
_Os10CardStatus_Type=Os10CardOperStatus
_Os10CardStatus_Object=MibTableColumn
os10CardStatus=_Os10CardStatus_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4,1,4),_Os10CardStatus_Type())
os10CardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:os10CardStatus.setStatus(_A)
_Os10CardTemp_Type=Integer32
_Os10CardTemp_Object=MibTableColumn
os10CardTemp=_Os10CardTemp_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4,1,5),_Os10CardTemp_Type())
os10CardTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:os10CardTemp.setStatus(_A)
if mibBuilder.loadTexts:os10CardTemp.setUnits(_O)
class _Os10CardPartNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Os10CardPartNum_Type.__name__=_D
_Os10CardPartNum_Object=MibTableColumn
os10CardPartNum=_Os10CardPartNum_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4,1,6),_Os10CardPartNum_Type())
os10CardPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:os10CardPartNum.setStatus(_A)
class _Os10CardPPID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_Os10CardPPID_Type.__name__=_D
_Os10CardPPID_Object=MibTableColumn
os10CardPPID=_Os10CardPPID_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4,1,7),_Os10CardPPID_Type())
os10CardPPID.setMaxAccess(_C)
if mibBuilder.loadTexts:os10CardPPID.setStatus(_A)
class _Os10CardHwRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_Os10CardHwRev_Type.__name__=_D
_Os10CardHwRev_Object=MibTableColumn
os10CardHwRev=_Os10CardHwRev_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4,1,8),_Os10CardHwRev_Type())
os10CardHwRev.setMaxAccess(_C)
if mibBuilder.loadTexts:os10CardHwRev.setStatus(_A)
class _Os10CardServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_Os10CardServiceTag_Type.__name__=_D
_Os10CardServiceTag_Object=MibTableColumn
os10CardServiceTag=_Os10CardServiceTag_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4,1,9),_Os10CardServiceTag_Type())
os10CardServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:os10CardServiceTag.setStatus(_A)
class _Os10CardExpServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_Os10CardExpServiceCode_Type.__name__=_D
_Os10CardExpServiceCode_Object=MibTableColumn
os10CardExpServiceCode=_Os10CardExpServiceCode_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,1,4,1,10),_Os10CardExpServiceCode_Type())
os10CardExpServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:os10CardExpServiceCode.setStatus(_A)
_Os10SystemComponent_ObjectIdentity=ObjectIdentity
os10SystemComponent=_Os10SystemComponent_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,4,1,2))
_Os10PowerSupplyTable_Object=MibTable
os10PowerSupplyTable=_Os10PowerSupplyTable_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,1))
if mibBuilder.loadTexts:os10PowerSupplyTable.setStatus(_A)
_Os10PowerSupplyEntry_Object=MibTableRow
os10PowerSupplyEntry=_Os10PowerSupplyEntry_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,1,1))
os10PowerSupplyEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:os10PowerSupplyEntry.setStatus(_A)
_Os10PowerSupplyIndex_Type=Unsigned32
_Os10PowerSupplyIndex_Object=MibTableColumn
os10PowerSupplyIndex=_Os10PowerSupplyIndex_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,1,1,1),_Os10PowerSupplyIndex_Type())
os10PowerSupplyIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:os10PowerSupplyIndex.setStatus(_A)
_Os10PowerSupplyDevice_Type=Os10DeviceType
_Os10PowerSupplyDevice_Object=MibTableColumn
os10PowerSupplyDevice=_Os10PowerSupplyDevice_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,1,1,2),_Os10PowerSupplyDevice_Type())
os10PowerSupplyDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:os10PowerSupplyDevice.setStatus(_A)
_Os10PowerSupplyDeviceIndex_Type=Unsigned32
_Os10PowerSupplyDeviceIndex_Object=MibTableColumn
os10PowerSupplyDeviceIndex=_Os10PowerSupplyDeviceIndex_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,1,1,3),_Os10PowerSupplyDeviceIndex_Type())
os10PowerSupplyDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:os10PowerSupplyDeviceIndex.setStatus(_A)
_Os10PowerSupplyOperStatus_Type=Os10CmnOperStatus
_Os10PowerSupplyOperStatus_Object=MibTableColumn
os10PowerSupplyOperStatus=_Os10PowerSupplyOperStatus_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,1,1,4),_Os10PowerSupplyOperStatus_Type())
os10PowerSupplyOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:os10PowerSupplyOperStatus.setStatus(_A)
class _Os10PowerSupplyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('ac',2),('dc',3)))
_Os10PowerSupplyType_Type.__name__=_L
_Os10PowerSupplyType_Object=MibTableColumn
os10PowerSupplyType=_Os10PowerSupplyType_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,1,1,5),_Os10PowerSupplyType_Type())
os10PowerSupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:os10PowerSupplyType.setStatus(_A)
class _Os10PowerSupplyPPID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_Os10PowerSupplyPPID_Type.__name__=_D
_Os10PowerSupplyPPID_Object=MibTableColumn
os10PowerSupplyPPID=_Os10PowerSupplyPPID_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,1,1,6),_Os10PowerSupplyPPID_Type())
os10PowerSupplyPPID.setMaxAccess(_C)
if mibBuilder.loadTexts:os10PowerSupplyPPID.setStatus(_A)
class _Os10PowerSupplyServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_Os10PowerSupplyServiceTag_Type.__name__=_D
_Os10PowerSupplyServiceTag_Object=MibTableColumn
os10PowerSupplyServiceTag=_Os10PowerSupplyServiceTag_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,1,1,7),_Os10PowerSupplyServiceTag_Type())
os10PowerSupplyServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:os10PowerSupplyServiceTag.setStatus(_A)
class _Os10PowerSupplyExpServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_Os10PowerSupplyExpServiceCode_Type.__name__=_D
_Os10PowerSupplyExpServiceCode_Object=MibTableColumn
os10PowerSupplyExpServiceCode=_Os10PowerSupplyExpServiceCode_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,1,1,8),_Os10PowerSupplyExpServiceCode_Type())
os10PowerSupplyExpServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:os10PowerSupplyExpServiceCode.setStatus(_A)
_Os10FanTrayTable_Object=MibTable
os10FanTrayTable=_Os10FanTrayTable_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,2))
if mibBuilder.loadTexts:os10FanTrayTable.setStatus(_A)
_Os10FanTrayEntry_Object=MibTableRow
os10FanTrayEntry=_Os10FanTrayEntry_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,2,1))
os10FanTrayEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:os10FanTrayEntry.setStatus(_A)
_Os10FanTrayIndex_Type=Unsigned32
_Os10FanTrayIndex_Object=MibTableColumn
os10FanTrayIndex=_Os10FanTrayIndex_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,2,1,1),_Os10FanTrayIndex_Type())
os10FanTrayIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:os10FanTrayIndex.setStatus(_A)
_Os10FanTrayDevice_Type=Os10DeviceType
_Os10FanTrayDevice_Object=MibTableColumn
os10FanTrayDevice=_Os10FanTrayDevice_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,2,1,2),_Os10FanTrayDevice_Type())
os10FanTrayDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanTrayDevice.setStatus(_A)
_Os10FanTrayDeviceIndex_Type=Unsigned32
_Os10FanTrayDeviceIndex_Object=MibTableColumn
os10FanTrayDeviceIndex=_Os10FanTrayDeviceIndex_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,2,1,3),_Os10FanTrayDeviceIndex_Type())
os10FanTrayDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanTrayDeviceIndex.setStatus(_A)
_Os10FanTrayOperStatus_Type=Os10CmnOperStatus
_Os10FanTrayOperStatus_Object=MibTableColumn
os10FanTrayOperStatus=_Os10FanTrayOperStatus_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,2,1,4),_Os10FanTrayOperStatus_Type())
os10FanTrayOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanTrayOperStatus.setStatus(_A)
class _Os10FanTrayPPID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_Os10FanTrayPPID_Type.__name__=_D
_Os10FanTrayPPID_Object=MibTableColumn
os10FanTrayPPID=_Os10FanTrayPPID_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,2,1,5),_Os10FanTrayPPID_Type())
os10FanTrayPPID.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanTrayPPID.setStatus(_A)
class _Os10FanTrayServiceTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_Os10FanTrayServiceTag_Type.__name__=_D
_Os10FanTrayServiceTag_Object=MibTableColumn
os10FanTrayServiceTag=_Os10FanTrayServiceTag_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,2,1,6),_Os10FanTrayServiceTag_Type())
os10FanTrayServiceTag.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanTrayServiceTag.setStatus(_A)
class _Os10FanTrayExpServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_Os10FanTrayExpServiceCode_Type.__name__=_D
_Os10FanTrayExpServiceCode_Object=MibTableColumn
os10FanTrayExpServiceCode=_Os10FanTrayExpServiceCode_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,2,1,7),_Os10FanTrayExpServiceCode_Type())
os10FanTrayExpServiceCode.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanTrayExpServiceCode.setStatus(_A)
_Os10FanTable_Object=MibTable
os10FanTable=_Os10FanTable_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,3))
if mibBuilder.loadTexts:os10FanTable.setStatus(_A)
_Os10FanEntry_Object=MibTableRow
os10FanEntry=_Os10FanEntry_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,3,1))
os10FanEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:os10FanEntry.setStatus(_A)
_Os10FanIndex_Type=Unsigned32
_Os10FanIndex_Object=MibTableColumn
os10FanIndex=_Os10FanIndex_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,3,1,1),_Os10FanIndex_Type())
os10FanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:os10FanIndex.setStatus(_A)
_Os10FanDevice_Type=Os10DeviceType
_Os10FanDevice_Object=MibTableColumn
os10FanDevice=_Os10FanDevice_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,3,1,2),_Os10FanDevice_Type())
os10FanDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanDevice.setStatus(_A)
_Os10FanDeviceIndex_Type=Unsigned32
_Os10FanDeviceIndex_Object=MibTableColumn
os10FanDeviceIndex=_Os10FanDeviceIndex_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,3,1,3),_Os10FanDeviceIndex_Type())
os10FanDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanDeviceIndex.setStatus(_A)
class _Os10FanEntity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('psu',1),('fanTray',2)))
_Os10FanEntity_Type.__name__=_L
_Os10FanEntity_Object=MibTableColumn
os10FanEntity=_Os10FanEntity_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,3,1,4),_Os10FanEntity_Type())
os10FanEntity.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanEntity.setStatus(_A)
_Os10FanEntitySlot_Type=Unsigned32
_Os10FanEntitySlot_Object=MibTableColumn
os10FanEntitySlot=_Os10FanEntitySlot_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,3,1,5),_Os10FanEntitySlot_Type())
os10FanEntitySlot.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanEntitySlot.setStatus(_A)
_Os10FanId_Type=Unsigned32
_Os10FanId_Object=MibTableColumn
os10FanId=_Os10FanId_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,3,1,6),_Os10FanId_Type())
os10FanId.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanId.setStatus(_A)
_Os10FanOperStatus_Type=Os10CmnOperStatus
_Os10FanOperStatus_Object=MibTableColumn
os10FanOperStatus=_Os10FanOperStatus_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,2,3,1,7),_Os10FanOperStatus_Type())
os10FanOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:os10FanOperStatus.setStatus(_A)
_Os10AlmObjects_ObjectIdentity=ObjectIdentity
os10AlmObjects=_Os10AlmObjects_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,4,1,3))
_Os10AlmMibNotifications_ObjectIdentity=ObjectIdentity
os10AlmMibNotifications=_Os10AlmMibNotifications_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1))
_Os10AlmVariable_ObjectIdentity=ObjectIdentity
os10AlmVariable=_Os10AlmVariable_ObjectIdentity((1,3,6,1,4,1,674,11000,5000,100,4,1,3,2))
_Os10AlmVarInteger_Type=Integer32
_Os10AlmVarInteger_Object=MibScalar
os10AlmVarInteger=_Os10AlmVarInteger_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,3,2,1),_Os10AlmVarInteger_Type())
os10AlmVarInteger.setMaxAccess(_K)
if mibBuilder.loadTexts:os10AlmVarInteger.setStatus(_A)
class _Os10AlmVarString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Os10AlmVarString_Type.__name__=_N
_Os10AlmVarString_Object=MibScalar
os10AlmVarString=_Os10AlmVarString_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,3,2,2),_Os10AlmVarString_Type())
os10AlmVarString.setMaxAccess(_K)
if mibBuilder.loadTexts:os10AlmVarString.setStatus(_A)
_Os10AlmVarChassisId_Type=Integer32
_Os10AlmVarChassisId_Object=MibScalar
os10AlmVarChassisId=_Os10AlmVarChassisId_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,3,2,3),_Os10AlmVarChassisId_Type())
os10AlmVarChassisId.setMaxAccess(_K)
if mibBuilder.loadTexts:os10AlmVarChassisId.setStatus(_A)
_Os10AlmVarSlot_Type=Integer32
_Os10AlmVarSlot_Object=MibScalar
os10AlmVarSlot=_Os10AlmVarSlot_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,3,2,4),_Os10AlmVarSlot_Type())
os10AlmVarSlot.setMaxAccess(_K)
if mibBuilder.loadTexts:os10AlmVarSlot.setStatus(_A)
_Os10AlmVarPort_Type=Integer32
_Os10AlmVarPort_Object=MibScalar
os10AlmVarPort=_Os10AlmVarPort_Object((1,3,6,1,4,1,674,11000,5000,100,4,1,3,2,5),_Os10AlmVarPort_Type())
os10AlmVarPort.setMaxAccess(_K)
if mibBuilder.loadTexts:os10AlmVarPort.setStatus(_A)
os10AlmMinorTempHigh=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,1))
os10AlmMinorTempHigh.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmMinorTempHigh.setStatus(_A)
os10AlmMinorTempClr=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,2))
os10AlmMinorTempClr.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmMinorTempClr.setStatus(_A)
os10AlmMajorTempHigh=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,3))
os10AlmMajorTempHigh.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmMajorTempHigh.setStatus(_A)
os10AlmMajorTempClr=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,4))
os10AlmMajorTempClr.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmMajorTempClr.setStatus(_A)
os10AlmPowerSupplyDown=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,5))
os10AlmPowerSupplyDown.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmPowerSupplyDown.setStatus(_A)
os10AlmPowerSupplyClr=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,6))
os10AlmPowerSupplyClr.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmPowerSupplyClr.setStatus(_A)
os10AlmMajorPowerSupply=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,7))
os10AlmMajorPowerSupply.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmMajorPowerSupply.setStatus(_A)
os10AlmMajorPowerSupplyClr=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,8))
os10AlmMajorPowerSupplyClr.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmMajorPowerSupplyClr.setStatus(_A)
os10AlmMinorPowerSupply=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,9))
os10AlmMinorPowerSupply.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmMinorPowerSupply.setStatus(_A)
os10AlmMinorPowerSupplyClr=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,10))
os10AlmMinorPowerSupplyClr.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmMinorPowerSupplyClr.setStatus(_A)
os10AlmFanTrayDown=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,11))
os10AlmFanTrayDown.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmFanTrayDown.setStatus(_A)
os10AlmFanTrayClr=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,12))
os10AlmFanTrayClr.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmFanTrayClr.setStatus(_A)
os10AlmMinorFanTray=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,13))
os10AlmMinorFanTray.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmMinorFanTray.setStatus(_A)
os10AlmMinorFanTrayClr=NotificationType((1,3,6,1,4,1,674,11000,5000,100,4,1,3,1,14))
os10AlmMinorFanTrayClr.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:os10AlmMinorFanTrayClr.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'os10ChassisMib':os10ChassisMib,'os10SysObject':os10SysObject,'os10ChassisObject':os10ChassisObject,'os10NumChassis':os10NumChassis,'os10MaxNumChassis':os10MaxNumChassis,'os10ChassisTable':os10ChassisTable,'os10ChassisEntry':os10ChassisEntry,_M:os10ChassisIndex,'os10ChassisType':os10ChassisType,'os10ChassisMacAddr':os10ChassisMacAddr,'os10ChassisPartNum':os10ChassisPartNum,'os10ChassisPPID':os10ChassisPPID,'os10ChassisHwRev':os10ChassisHwRev,'os10ChassisServiceTag':os10ChassisServiceTag,'os10ChassisExpServiceCode':os10ChassisExpServiceCode,'os10ChassisNumFanTrays':os10ChassisNumFanTrays,'os10ChassisNumPowerSupplies':os10ChassisNumPowerSupplies,'os10ChassisTemp':os10ChassisTemp,'os10ChassisProductBase':os10ChassisProductBase,'os10ChassisProductSN':os10ChassisProductSN,'os10ChassisProductPN':os10ChassisProductPN,'os10CardTable':os10CardTable,'os10CardEntry':os10CardEntry,_P:os10CardIndex,'os10CardType':os10CardType,'os10CardDescription':os10CardDescription,'os10CardStatus':os10CardStatus,'os10CardTemp':os10CardTemp,'os10CardPartNum':os10CardPartNum,'os10CardPPID':os10CardPPID,'os10CardHwRev':os10CardHwRev,'os10CardServiceTag':os10CardServiceTag,'os10CardExpServiceCode':os10CardExpServiceCode,'os10SystemComponent':os10SystemComponent,'os10PowerSupplyTable':os10PowerSupplyTable,'os10PowerSupplyEntry':os10PowerSupplyEntry,_Q:os10PowerSupplyIndex,'os10PowerSupplyDevice':os10PowerSupplyDevice,'os10PowerSupplyDeviceIndex':os10PowerSupplyDeviceIndex,'os10PowerSupplyOperStatus':os10PowerSupplyOperStatus,'os10PowerSupplyType':os10PowerSupplyType,'os10PowerSupplyPPID':os10PowerSupplyPPID,'os10PowerSupplyServiceTag':os10PowerSupplyServiceTag,'os10PowerSupplyExpServiceCode':os10PowerSupplyExpServiceCode,'os10FanTrayTable':os10FanTrayTable,'os10FanTrayEntry':os10FanTrayEntry,_R:os10FanTrayIndex,'os10FanTrayDevice':os10FanTrayDevice,'os10FanTrayDeviceIndex':os10FanTrayDeviceIndex,'os10FanTrayOperStatus':os10FanTrayOperStatus,'os10FanTrayPPID':os10FanTrayPPID,'os10FanTrayServiceTag':os10FanTrayServiceTag,'os10FanTrayExpServiceCode':os10FanTrayExpServiceCode,'os10FanTable':os10FanTable,'os10FanEntry':os10FanEntry,_S:os10FanIndex,'os10FanDevice':os10FanDevice,'os10FanDeviceIndex':os10FanDeviceIndex,'os10FanEntity':os10FanEntity,'os10FanEntitySlot':os10FanEntitySlot,'os10FanId':os10FanId,'os10FanOperStatus':os10FanOperStatus,'os10AlmObjects':os10AlmObjects,'os10AlmMibNotifications':os10AlmMibNotifications,'os10AlmMinorTempHigh':os10AlmMinorTempHigh,'os10AlmMinorTempClr':os10AlmMinorTempClr,'os10AlmMajorTempHigh':os10AlmMajorTempHigh,'os10AlmMajorTempClr':os10AlmMajorTempClr,'os10AlmPowerSupplyDown':os10AlmPowerSupplyDown,'os10AlmPowerSupplyClr':os10AlmPowerSupplyClr,'os10AlmMajorPowerSupply':os10AlmMajorPowerSupply,'os10AlmMajorPowerSupplyClr':os10AlmMajorPowerSupplyClr,'os10AlmMinorPowerSupply':os10AlmMinorPowerSupply,'os10AlmMinorPowerSupplyClr':os10AlmMinorPowerSupplyClr,'os10AlmFanTrayDown':os10AlmFanTrayDown,'os10AlmFanTrayClr':os10AlmFanTrayClr,'os10AlmMinorFanTray':os10AlmMinorFanTray,'os10AlmMinorFanTrayClr':os10AlmMinorFanTrayClr,'os10AlmVariable':os10AlmVariable,_E:os10AlmVarInteger,_F:os10AlmVarString,_G:os10AlmVarChassisId,_H:os10AlmVarSlot,_I:os10AlmVarPort})