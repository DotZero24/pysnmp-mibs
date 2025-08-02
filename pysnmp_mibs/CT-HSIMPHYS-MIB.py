_I='testing'
_H='localHwDeviceID'
_G='wpimBoardID'
_F='mBusBoardID'
_E='unknown'
_D='CT-HSIMPHYS-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctHSIMPhysMib,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctHSIMPhysMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_HsimInfo_ObjectIdentity=ObjectIdentity
hsimInfo=_HsimInfo_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,17,1))
_HsimBoardRev_Type=DisplayString
_HsimBoardRev_Object=MibScalar
hsimBoardRev=_HsimBoardRev_Object((1,3,6,1,4,1,52,4,1,1,17,1,1),_HsimBoardRev_Type())
hsimBoardRev.setMaxAccess(_B)
if mibBuilder.loadTexts:hsimBoardRev.setStatus(_A)
_HsimBoardId_Type=DisplayString
_HsimBoardId_Object=MibScalar
hsimBoardId=_HsimBoardId_Object((1,3,6,1,4,1,52,4,1,1,17,1,2),_HsimBoardId_Type())
hsimBoardId.setMaxAccess(_B)
if mibBuilder.loadTexts:hsimBoardId.setStatus(_A)
_HsimEpldRev_Type=DisplayString
_HsimEpldRev_Object=MibScalar
hsimEpldRev=_HsimEpldRev_Object((1,3,6,1,4,1,52,4,1,1,17,1,3),_HsimEpldRev_Type())
hsimEpldRev.setMaxAccess(_B)
if mibBuilder.loadTexts:hsimEpldRev.setStatus(_A)
_HsimEpldId_Type=DisplayString
_HsimEpldId_Object=MibScalar
hsimEpldId=_HsimEpldId_Object((1,3,6,1,4,1,52,4,1,1,17,1,4),_HsimEpldId_Type())
hsimEpldId.setMaxAccess(_B)
if mibBuilder.loadTexts:hsimEpldId.setStatus(_A)
_HsimFsbRev_Type=DisplayString
_HsimFsbRev_Object=MibScalar
hsimFsbRev=_HsimFsbRev_Object((1,3,6,1,4,1,52,4,1,1,17,1,5),_HsimFsbRev_Type())
hsimFsbRev.setMaxAccess(_B)
if mibBuilder.loadTexts:hsimFsbRev.setStatus(_A)
_HsimSsbRev_Type=DisplayString
_HsimSsbRev_Object=MibScalar
hsimSsbRev=_HsimSsbRev_Object((1,3,6,1,4,1,52,4,1,1,17,1,6),_HsimSsbRev_Type())
hsimSsbRev.setMaxAccess(_B)
if mibBuilder.loadTexts:hsimSsbRev.setStatus(_A)
_HsimFwRev_Type=DisplayString
_HsimFwRev_Object=MibScalar
hsimFwRev=_HsimFwRev_Object((1,3,6,1,4,1,52,4,1,1,17,1,7),_HsimFwRev_Type())
hsimFwRev.setMaxAccess(_B)
if mibBuilder.loadTexts:hsimFwRev.setStatus(_A)
_HsimPeripheralMBusInfo_ObjectIdentity=ObjectIdentity
hsimPeripheralMBusInfo=_HsimPeripheralMBusInfo_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,17,1,8))
_MBusNumberBoardsInstalled_Type=Integer32
_MBusNumberBoardsInstalled_Object=MibScalar
mBusNumberBoardsInstalled=_MBusNumberBoardsInstalled_Object((1,3,6,1,4,1,52,4,1,1,17,1,8,1),_MBusNumberBoardsInstalled_Type())
mBusNumberBoardsInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:mBusNumberBoardsInstalled.setStatus(_A)
_MBusBoardTable_Object=MibTable
mBusBoardTable=_MBusBoardTable_Object((1,3,6,1,4,1,52,4,1,1,17,1,8,2))
if mibBuilder.loadTexts:mBusBoardTable.setStatus(_A)
_MBusBoardEntry_Object=MibTableRow
mBusBoardEntry=_MBusBoardEntry_Object((1,3,6,1,4,1,52,4,1,1,17,1,8,2,1))
mBusBoardEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:mBusBoardEntry.setStatus(_A)
_MBusBoardID_Type=Integer32
_MBusBoardID_Object=MibTableColumn
mBusBoardID=_MBusBoardID_Object((1,3,6,1,4,1,52,4,1,1,17,1,8,2,1,1),_MBusBoardID_Type())
mBusBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:mBusBoardID.setStatus(_A)
class _MBusBoardEntryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('cmm',2)))
_MBusBoardEntryType_Type.__name__=_C
_MBusBoardEntryType_Object=MibTableColumn
mBusBoardEntryType=_MBusBoardEntryType_Object((1,3,6,1,4,1,52,4,1,1,17,1,8,2,1,2),_MBusBoardEntryType_Type())
mBusBoardEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:mBusBoardEntryType.setStatus(_A)
_MBusBoardOIDPointer_Type=ObjectIdentifier
_MBusBoardOIDPointer_Object=MibTableColumn
mBusBoardOIDPointer=_MBusBoardOIDPointer_Object((1,3,6,1,4,1,52,4,1,1,17,1,8,2,1,3),_MBusBoardOIDPointer_Type())
mBusBoardOIDPointer.setMaxAccess(_B)
if mibBuilder.loadTexts:mBusBoardOIDPointer.setStatus(_A)
_HsimPeripheralWpimInfo_ObjectIdentity=ObjectIdentity
hsimPeripheralWpimInfo=_HsimPeripheralWpimInfo_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,17,1,9))
_WpimNumberBoardsInstalled_Type=Integer32
_WpimNumberBoardsInstalled_Object=MibScalar
wpimNumberBoardsInstalled=_WpimNumberBoardsInstalled_Object((1,3,6,1,4,1,52,4,1,1,17,1,9,1),_WpimNumberBoardsInstalled_Type())
wpimNumberBoardsInstalled.setMaxAccess(_B)
if mibBuilder.loadTexts:wpimNumberBoardsInstalled.setStatus(_A)
_WpimBoardTable_Object=MibTable
wpimBoardTable=_WpimBoardTable_Object((1,3,6,1,4,1,52,4,1,1,17,1,9,2))
if mibBuilder.loadTexts:wpimBoardTable.setStatus(_A)
_WpimBoardEntry_Object=MibTableRow
wpimBoardEntry=_WpimBoardEntry_Object((1,3,6,1,4,1,52,4,1,1,17,1,9,2,1))
wpimBoardEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:wpimBoardEntry.setStatus(_A)
_WpimBoardID_Type=Integer32
_WpimBoardID_Object=MibTableColumn
wpimBoardID=_WpimBoardID_Object((1,3,6,1,4,1,52,4,1,1,17,1,9,2,1,1),_WpimBoardID_Type())
wpimBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:wpimBoardID.setStatus(_A)
_WpimBoardEntryType_Type=ObjectIdentifier
_WpimBoardEntryType_Object=MibTableColumn
wpimBoardEntryType=_WpimBoardEntryType_Object((1,3,6,1,4,1,52,4,1,1,17,1,9,2,1,2),_WpimBoardEntryType_Type())
wpimBoardEntryType.setMaxAccess(_B)
if mibBuilder.loadTexts:wpimBoardEntryType.setStatus(_A)
_WpimBoardOIDPointer_Type=ObjectIdentifier
_WpimBoardOIDPointer_Object=MibTableColumn
wpimBoardOIDPointer=_WpimBoardOIDPointer_Object((1,3,6,1,4,1,52,4,1,1,17,1,9,2,1,3),_WpimBoardOIDPointer_Type())
wpimBoardOIDPointer.setMaxAccess(_B)
if mibBuilder.loadTexts:wpimBoardOIDPointer.setStatus(_A)
_HsimLocalHwDevicesInfo_ObjectIdentity=ObjectIdentity
hsimLocalHwDevicesInfo=_HsimLocalHwDevicesInfo_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,17,1,10))
_LocalHwDevicesTable_Object=MibTable
localHwDevicesTable=_LocalHwDevicesTable_Object((1,3,6,1,4,1,52,4,1,1,17,1,10,1))
if mibBuilder.loadTexts:localHwDevicesTable.setStatus(_A)
_LocalHwDevicesEntry_Object=MibTableRow
localHwDevicesEntry=_LocalHwDevicesEntry_Object((1,3,6,1,4,1,52,4,1,1,17,1,10,1,1))
localHwDevicesEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:localHwDevicesEntry.setStatus(_A)
_LocalHwDeviceID_Type=Integer32
_LocalHwDeviceID_Object=MibTableColumn
localHwDeviceID=_LocalHwDeviceID_Object((1,3,6,1,4,1,52,4,1,1,17,1,10,1,1,1),_LocalHwDeviceID_Type())
localHwDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:localHwDeviceID.setStatus(_A)
class _LocalHwDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('siemensMunich32',2),('mitelMT8985',3)))
_LocalHwDeviceType_Type.__name__=_C
_LocalHwDeviceType_Object=MibTableColumn
localHwDeviceType=_LocalHwDeviceType_Object((1,3,6,1,4,1,52,4,1,1,17,1,10,1,1,2),_LocalHwDeviceType_Type())
localHwDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:localHwDeviceType.setStatus(_A)
class _LocalHwDeviceOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),('down',2),(_I,3),(_E,4),('dormant',5)))
_LocalHwDeviceOperStatus_Type.__name__=_C
_LocalHwDeviceOperStatus_Object=MibTableColumn
localHwDeviceOperStatus=_LocalHwDeviceOperStatus_Object((1,3,6,1,4,1,52,4,1,1,17,1,10,1,1,3),_LocalHwDeviceOperStatus_Type())
localHwDeviceOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:localHwDeviceOperStatus.setStatus(_A)
class _LocalHwDeviceAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_I,3)))
_LocalHwDeviceAdminStatus_Type.__name__=_C
_LocalHwDeviceAdminStatus_Object=MibTableColumn
localHwDeviceAdminStatus=_LocalHwDeviceAdminStatus_Object((1,3,6,1,4,1,52,4,1,1,17,1,10,1,1,4),_LocalHwDeviceAdminStatus_Type())
localHwDeviceAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:localHwDeviceAdminStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hsimInfo':hsimInfo,'hsimBoardRev':hsimBoardRev,'hsimBoardId':hsimBoardId,'hsimEpldRev':hsimEpldRev,'hsimEpldId':hsimEpldId,'hsimFsbRev':hsimFsbRev,'hsimSsbRev':hsimSsbRev,'hsimFwRev':hsimFwRev,'hsimPeripheralMBusInfo':hsimPeripheralMBusInfo,'mBusNumberBoardsInstalled':mBusNumberBoardsInstalled,'mBusBoardTable':mBusBoardTable,'mBusBoardEntry':mBusBoardEntry,_F:mBusBoardID,'mBusBoardEntryType':mBusBoardEntryType,'mBusBoardOIDPointer':mBusBoardOIDPointer,'hsimPeripheralWpimInfo':hsimPeripheralWpimInfo,'wpimNumberBoardsInstalled':wpimNumberBoardsInstalled,'wpimBoardTable':wpimBoardTable,'wpimBoardEntry':wpimBoardEntry,_G:wpimBoardID,'wpimBoardEntryType':wpimBoardEntryType,'wpimBoardOIDPointer':wpimBoardOIDPointer,'hsimLocalHwDevicesInfo':hsimLocalHwDevicesInfo,'localHwDevicesTable':localHwDevicesTable,'localHwDevicesEntry':localHwDevicesEntry,_H:localHwDeviceID,'localHwDeviceType':localHwDeviceType,'localHwDeviceOperStatus':localHwDeviceOperStatus,'localHwDeviceAdminStatus':localHwDeviceAdminStatus})