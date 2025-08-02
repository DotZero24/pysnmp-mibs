_V='h3cAccessMedia'
_U='h3cUIMPin'
_T='h3cUIMOldPin'
_S='h3cUIMIndex'
_R='Unsigned32'
_Q='h3c3GImsiBind'
_P='h3c3GCurrentRssiBind'
_O='h3c3GCurrentService'
_N='h3cUIMImsi'
_M='read-write'
_L='accessible-for-notify'
_K='unknown'
_J='h3cWirelessCardSerialNumber'
_I='h3cDevSerialNumber'
_H='h3cDeviceOUI'
_G='h3cWirelessCardIndex'
_F='dBm'
_E='Integer32'
_D='SnmpAdminString'
_C='read-only'
_B='A3COM-HUAWEI-3GMODEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_R,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3c3GModem=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,98))
if mibBuilder.loadTexts:h3c3GModem.setRevisions(('2009-04-30 12:00',))
class H3cUIMStatusType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('absent',1),('initial',2),('fault',3),('unprotected',4),('protected',5),('pinLocked',6),('pukLocked',7),('selfDestruct',8)))
_H3c3GModemObjects_ObjectIdentity=ObjectIdentity
h3c3GModemObjects=_H3c3GModemObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,98,1))
_H3cWirelessCard_ObjectIdentity=ObjectIdentity
h3cWirelessCard=_H3cWirelessCard_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,98,1,1))
_H3cWirelessCardTable_Object=MibTable
h3cWirelessCardTable=_H3cWirelessCardTable_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1))
if mibBuilder.loadTexts:h3cWirelessCardTable.setStatus(_A)
_H3cWirelessCardEntry_Object=MibTableRow
h3cWirelessCardEntry=_H3cWirelessCardEntry_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1))
h3cWirelessCardEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3cWirelessCardEntry.setStatus(_A)
class _H3cWirelessCardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cWirelessCardIndex_Type.__name__=_E
_H3cWirelessCardIndex_Object=MibTableColumn
h3cWirelessCardIndex=_H3cWirelessCardIndex_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,1),_H3cWirelessCardIndex_Type())
h3cWirelessCardIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardIndex.setStatus(_A)
class _H3cWirelessCardModelName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardModelName_Type.__name__=_D
_H3cWirelessCardModelName_Object=MibTableColumn
h3cWirelessCardModelName=_H3cWirelessCardModelName_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,2),_H3cWirelessCardModelName_Type())
h3cWirelessCardModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardModelName.setStatus(_A)
class _H3cWirelessCardMfgName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardMfgName_Type.__name__=_D
_H3cWirelessCardMfgName_Object=MibTableColumn
h3cWirelessCardMfgName=_H3cWirelessCardMfgName_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,3),_H3cWirelessCardMfgName_Type())
h3cWirelessCardMfgName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardMfgName.setStatus(_A)
class _H3cWirelessCardDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardDescription_Type.__name__=_D
_H3cWirelessCardDescription_Object=MibTableColumn
h3cWirelessCardDescription=_H3cWirelessCardDescription_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,4),_H3cWirelessCardDescription_Type())
h3cWirelessCardDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardDescription.setStatus(_A)
class _H3cWirelessCardSerialNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWirelessCardSerialNumber_Type.__name__=_D
_H3cWirelessCardSerialNumber_Object=MibTableColumn
h3cWirelessCardSerialNumber=_H3cWirelessCardSerialNumber_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,5),_H3cWirelessCardSerialNumber_Type())
h3cWirelessCardSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardSerialNumber.setStatus(_A)
class _H3cWirelessCardCMIIID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWirelessCardCMIIID_Type.__name__=_D
_H3cWirelessCardCMIIID_Object=MibTableColumn
h3cWirelessCardCMIIID=_H3cWirelessCardCMIIID_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,6),_H3cWirelessCardCMIIID_Type())
h3cWirelessCardCMIIID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardCMIIID.setStatus(_A)
class _H3cWirelessCardHardwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardHardwareVersion_Type.__name__=_D
_H3cWirelessCardHardwareVersion_Object=MibTableColumn
h3cWirelessCardHardwareVersion=_H3cWirelessCardHardwareVersion_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,7),_H3cWirelessCardHardwareVersion_Type())
h3cWirelessCardHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardHardwareVersion.setStatus(_A)
class _H3cWirelessCardFirmwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardFirmwareVersion_Type.__name__=_D
_H3cWirelessCardFirmwareVersion_Object=MibTableColumn
h3cWirelessCardFirmwareVersion=_H3cWirelessCardFirmwareVersion_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,8),_H3cWirelessCardFirmwareVersion_Type())
h3cWirelessCardFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardFirmwareVersion.setStatus(_A)
class _H3cWirelessCardPRLVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cWirelessCardPRLVersion_Type.__name__=_D
_H3cWirelessCardPRLVersion_Object=MibTableColumn
h3cWirelessCardPRLVersion=_H3cWirelessCardPRLVersion_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,9),_H3cWirelessCardPRLVersion_Type())
h3cWirelessCardPRLVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardPRLVersion.setStatus(_A)
_H3cWirelessCardInterfaceIndex_Type=InterfaceIndex
_H3cWirelessCardInterfaceIndex_Object=MibTableColumn
h3cWirelessCardInterfaceIndex=_H3cWirelessCardInterfaceIndex_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,10),_H3cWirelessCardInterfaceIndex_Type())
h3cWirelessCardInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardInterfaceIndex.setStatus(_A)
class _H3cWirelessCardModemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('onLine',2),('offLine',3)))
_H3cWirelessCardModemStatus_Type.__name__=_E
_H3cWirelessCardModemStatus_Object=MibTableColumn
h3cWirelessCardModemStatus=_H3cWirelessCardModemStatus_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,11),_H3cWirelessCardModemStatus_Type())
h3cWirelessCardModemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardModemStatus.setStatus(_A)
class _H3cWirelessCardCurServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),('available',2),('emergency',3),('lowPower',4),('noService',5)))
_H3cWirelessCardCurServiceStatus_Type.__name__=_E
_H3cWirelessCardCurServiceStatus_Object=MibTableColumn
h3cWirelessCardCurServiceStatus=_H3cWirelessCardCurServiceStatus_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,12),_H3cWirelessCardCurServiceStatus_Type())
h3cWirelessCardCurServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardCurServiceStatus.setStatus(_A)
class _H3cWirelessCardCurRoamingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('roaming',2),('home',3)))
_H3cWirelessCardCurRoamingStatus_Type.__name__=_E
_H3cWirelessCardCurRoamingStatus_Object=MibTableColumn
h3cWirelessCardCurRoamingStatus=_H3cWirelessCardCurRoamingStatus_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,1,1,1,13),_H3cWirelessCardCurRoamingStatus_Type())
h3cWirelessCardCurRoamingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWirelessCardCurRoamingStatus.setStatus(_A)
_H3cUIM_ObjectIdentity=ObjectIdentity
h3cUIM=_H3cUIM_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,98,1,2))
_H3cUIMInfoTable_Object=MibTable
h3cUIMInfoTable=_H3cUIMInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,2,1))
if mibBuilder.loadTexts:h3cUIMInfoTable.setStatus(_A)
_H3cUIMInfoEntry_Object=MibTableRow
h3cUIMInfoEntry=_H3cUIMInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,2,1,1))
h3cUIMInfoEntry.setIndexNames((0,_B,_G),(0,_B,_S))
if mibBuilder.loadTexts:h3cUIMInfoEntry.setStatus(_A)
class _H3cUIMIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cUIMIndex_Type.__name__=_E
_H3cUIMIndex_Object=MibTableColumn
h3cUIMIndex=_H3cUIMIndex_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,2,1,1,1),_H3cUIMIndex_Type())
h3cUIMIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cUIMIndex.setStatus(_A)
_H3cUIMStatus_Type=H3cUIMStatusType
_H3cUIMStatus_Object=MibTableColumn
h3cUIMStatus=_H3cUIMStatus_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,2,1,1,2),_H3cUIMStatus_Type())
h3cUIMStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMStatus.setStatus(_A)
class _H3cUIMImsi_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cUIMImsi_Type.__name__=_D
_H3cUIMImsi_Object=MibTableColumn
h3cUIMImsi=_H3cUIMImsi_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,2,1,1,3),_H3cUIMImsi_Type())
h3cUIMImsi.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMImsi.setStatus(_A)
class _H3cUIMPin_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_H3cUIMPin_Type.__name__=_D
_H3cUIMPin_Object=MibTableColumn
h3cUIMPin=_H3cUIMPin_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,2,1,1,4),_H3cUIMPin_Type())
h3cUIMPin.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMPin.setStatus(_A)
class _H3cUIMVoltage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cUIMVoltage_Type.__name__=_R
_H3cUIMVoltage_Object=MibTableColumn
h3cUIMVoltage=_H3cUIMVoltage_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,2,1,1,5),_H3cUIMVoltage_Type())
h3cUIMVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMVoltage.setStatus(_A)
if mibBuilder.loadTexts:h3cUIMVoltage.setUnits('milli-volt')
class _H3cUIMProvider_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cUIMProvider_Type.__name__=_D
_H3cUIMProvider_Object=MibTableColumn
h3cUIMProvider=_H3cUIMProvider_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,2,1,1,6),_H3cUIMProvider_Type())
h3cUIMProvider.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMProvider.setStatus(_A)
class _H3cUIMSignal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31),ValueRangeConstraint(99,99))
_H3cUIMSignal_Type.__name__=_E
_H3cUIMSignal_Object=MibTableColumn
h3cUIMSignal=_H3cUIMSignal_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,2,1,1,7),_H3cUIMSignal_Type())
h3cUIMSignal.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMSignal.setStatus(_A)
class _H3cUIMTryPinPukTimes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cUIMTryPinPukTimes_Type.__name__=_R
_H3cUIMTryPinPukTimes_Object=MibTableColumn
h3cUIMTryPinPukTimes=_H3cUIMTryPinPukTimes_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,2,1,1,8),_H3cUIMTryPinPukTimes_Type())
h3cUIMTryPinPukTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cUIMTryPinPukTimes.setStatus(_A)
class _H3cUIMOldPin_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,9))
_H3cUIMOldPin_Type.__name__=_D
_H3cUIMOldPin_Object=MibTableColumn
h3cUIMOldPin=_H3cUIMOldPin_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,2,1,1,9),_H3cUIMOldPin_Type())
h3cUIMOldPin.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cUIMOldPin.setStatus(_A)
_H3c3GCdma_ObjectIdentity=ObjectIdentity
h3c3GCdma=_H3c3GCdma_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,98,1,3))
_H3c3GCdma1xRttTable_Object=MibTable
h3c3GCdma1xRttTable=_H3c3GCdma1xRttTable_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,3,1))
if mibBuilder.loadTexts:h3c3GCdma1xRttTable.setStatus(_A)
_H3c3GCdma1xRttEntry_Object=MibTableRow
h3c3GCdma1xRttEntry=_H3c3GCdma1xRttEntry_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,3,1,1))
h3c3GCdma1xRttEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3c3GCdma1xRttEntry.setStatus(_A)
class _H3c3GCdma1xRttCurrentRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GCdma1xRttCurrentRssi_Type.__name__=_E
_H3c3GCdma1xRttCurrentRssi_Object=MibTableColumn
h3c3GCdma1xRttCurrentRssi=_H3c3GCdma1xRttCurrentRssi_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,3,1,1,1),_H3c3GCdma1xRttCurrentRssi_Type())
h3c3GCdma1xRttCurrentRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdma1xRttCurrentRssi.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdma1xRttCurrentRssi.setUnits(_F)
class _H3c3GCdma1xRttRssiMediumThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GCdma1xRttRssiMediumThreshold_Type.__name__=_E
_H3c3GCdma1xRttRssiMediumThreshold_Object=MibTableColumn
h3c3GCdma1xRttRssiMediumThreshold=_H3c3GCdma1xRttRssiMediumThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,3,1,1,2),_H3c3GCdma1xRttRssiMediumThreshold_Type())
h3c3GCdma1xRttRssiMediumThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:h3c3GCdma1xRttRssiMediumThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdma1xRttRssiMediumThreshold.setUnits(_F)
class _H3c3GCdma1xRttRssiWeakThreshold_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GCdma1xRttRssiWeakThreshold_Type.__name__=_E
_H3c3GCdma1xRttRssiWeakThreshold_Object=MibTableColumn
h3c3GCdma1xRttRssiWeakThreshold=_H3c3GCdma1xRttRssiWeakThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,3,1,1,3),_H3c3GCdma1xRttRssiWeakThreshold_Type())
h3c3GCdma1xRttRssiWeakThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:h3c3GCdma1xRttRssiWeakThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdma1xRttRssiWeakThreshold.setUnits(_F)
_H3c3GCdmaEvDoTable_Object=MibTable
h3c3GCdmaEvDoTable=_H3c3GCdmaEvDoTable_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,3,2))
if mibBuilder.loadTexts:h3c3GCdmaEvDoTable.setStatus(_A)
_H3c3GCdmaEvDoEntry_Object=MibTableRow
h3c3GCdmaEvDoEntry=_H3c3GCdmaEvDoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,3,2,1))
h3c3GCdmaEvDoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3c3GCdmaEvDoEntry.setStatus(_A)
class _H3c3GCdmaEvDoCurrentRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GCdmaEvDoCurrentRssi_Type.__name__=_E
_H3c3GCdmaEvDoCurrentRssi_Object=MibTableColumn
h3c3GCdmaEvDoCurrentRssi=_H3c3GCdmaEvDoCurrentRssi_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,3,2,1,1),_H3c3GCdmaEvDoCurrentRssi_Type())
h3c3GCdmaEvDoCurrentRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GCdmaEvDoCurrentRssi.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdmaEvDoCurrentRssi.setUnits(_F)
class _H3c3GCdmaEvDoRssiMediumThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GCdmaEvDoRssiMediumThreshold_Type.__name__=_E
_H3c3GCdmaEvDoRssiMediumThreshold_Object=MibTableColumn
h3c3GCdmaEvDoRssiMediumThreshold=_H3c3GCdmaEvDoRssiMediumThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,3,2,1,2),_H3c3GCdmaEvDoRssiMediumThreshold_Type())
h3c3GCdmaEvDoRssiMediumThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:h3c3GCdmaEvDoRssiMediumThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdmaEvDoRssiMediumThreshold.setUnits(_F)
class _H3c3GCdmaEvDoRssiWeakThreshold_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GCdmaEvDoRssiWeakThreshold_Type.__name__=_E
_H3c3GCdmaEvDoRssiWeakThreshold_Object=MibTableColumn
h3c3GCdmaEvDoRssiWeakThreshold=_H3c3GCdmaEvDoRssiWeakThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,3,2,1,3),_H3c3GCdmaEvDoRssiWeakThreshold_Type())
h3c3GCdmaEvDoRssiWeakThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:h3c3GCdmaEvDoRssiWeakThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCdmaEvDoRssiWeakThreshold.setUnits(_F)
_H3c3GGsm_ObjectIdentity=ObjectIdentity
h3c3GGsm=_H3c3GGsm_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,98,1,4))
_H3c3GGsmInfoTable_Object=MibTable
h3c3GGsmInfoTable=_H3c3GGsmInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1))
if mibBuilder.loadTexts:h3c3GGsmInfoTable.setStatus(_A)
_H3c3GGsmInfoEntry_Object=MibTableRow
h3c3GGsmInfoEntry=_H3c3GGsmInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1))
h3c3GGsmInfoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3c3GGsmInfoEntry.setStatus(_A)
class _H3c3GGsmCurrentRssi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GGsmCurrentRssi_Type.__name__=_E
_H3c3GGsmCurrentRssi_Object=MibTableColumn
h3c3GGsmCurrentRssi=_H3c3GGsmCurrentRssi_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,1),_H3c3GGsmCurrentRssi_Type())
h3c3GGsmCurrentRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmCurrentRssi.setStatus(_A)
if mibBuilder.loadTexts:h3c3GGsmCurrentRssi.setUnits(_F)
class _H3c3GGsmRssiMediumThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GGsmRssiMediumThreshold_Type.__name__=_E
_H3c3GGsmRssiMediumThreshold_Object=MibTableColumn
h3c3GGsmRssiMediumThreshold=_H3c3GGsmRssiMediumThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,2),_H3c3GGsmRssiMediumThreshold_Type())
h3c3GGsmRssiMediumThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:h3c3GGsmRssiMediumThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GGsmRssiMediumThreshold.setUnits(_F)
class _H3c3GGsmRssiWeakThreshold_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GGsmRssiWeakThreshold_Type.__name__=_E
_H3c3GGsmRssiWeakThreshold_Object=MibTableColumn
h3c3GGsmRssiWeakThreshold=_H3c3GGsmRssiWeakThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,3),_H3c3GGsmRssiWeakThreshold_Type())
h3c3GGsmRssiWeakThreshold.setMaxAccess(_M)
if mibBuilder.loadTexts:h3c3GGsmRssiWeakThreshold.setStatus(_A)
if mibBuilder.loadTexts:h3c3GGsmRssiWeakThreshold.setUnits(_F)
class _H3c3GGsmImsi_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmImsi_Type.__name__=_D
_H3c3GGsmImsi_Object=MibTableColumn
h3c3GGsmImsi=_H3c3GGsmImsi_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,4),_H3c3GGsmImsi_Type())
h3c3GGsmImsi.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmImsi.setStatus(_A)
class _H3c3GGsmImei_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmImei_Type.__name__=_D
_H3c3GGsmImei_Object=MibTableColumn
h3c3GGsmImei=_H3c3GGsmImei_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,5),_H3c3GGsmImei_Type())
h3c3GGsmImei.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmImei.setStatus(_A)
class _H3c3GGsmApn_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_H3c3GGsmApn_Type.__name__=_D
_H3c3GGsmApn_Object=MibTableColumn
h3c3GGsmApn=_H3c3GGsmApn_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,6),_H3c3GGsmApn_Type())
h3c3GGsmApn.setMaxAccess(_M)
if mibBuilder.loadTexts:h3c3GGsmApn.setStatus(_A)
class _H3c3GGsmPacketSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('active',2),('inactive',3)))
_H3c3GGsmPacketSessionStatus_Type.__name__=_E
_H3c3GGsmPacketSessionStatus_Object=MibTableColumn
h3c3GGsmPacketSessionStatus=_H3c3GGsmPacketSessionStatus_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,7),_H3c3GGsmPacketSessionStatus_Type())
h3c3GGsmPacketSessionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmPacketSessionStatus.setStatus(_A)
class _H3c3GGsmNetworkSelectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('automatic',2),('manual',3)))
_H3c3GGsmNetworkSelectionMode_Type.__name__=_E
_H3c3GGsmNetworkSelectionMode_Object=MibTableColumn
h3c3GGsmNetworkSelectionMode=_H3c3GGsmNetworkSelectionMode_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,8),_H3c3GGsmNetworkSelectionMode_Type())
h3c3GGsmNetworkSelectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmNetworkSelectionMode.setStatus(_A)
class _H3c3GGsmMobileNetworkName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmMobileNetworkName_Type.__name__=_D
_H3c3GGsmMobileNetworkName_Object=MibTableColumn
h3c3GGsmMobileNetworkName=_H3c3GGsmMobileNetworkName_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,9),_H3c3GGsmMobileNetworkName_Type())
h3c3GGsmMobileNetworkName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmMobileNetworkName.setStatus(_A)
class _H3c3GGsmLac_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmLac_Type.__name__=_D
_H3c3GGsmLac_Object=MibTableColumn
h3c3GGsmLac=_H3c3GGsmLac_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,10),_H3c3GGsmLac_Type())
h3c3GGsmLac.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmLac.setStatus(_A)
class _H3c3GGsmCellId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3c3GGsmCellId_Type.__name__=_D
_H3c3GGsmCellId_Object=MibTableColumn
h3c3GGsmCellId=_H3c3GGsmCellId_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,11),_H3c3GGsmCellId_Type())
h3c3GGsmCellId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmCellId.setStatus(_A)
class _H3c3GGsmSimStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),('ok',2),('notInsert',3),('networkReject',4),('blocked',5)))
_H3c3GGsmSimStatus_Type.__name__=_E
_H3c3GGsmSimStatus_Object=MibTableColumn
h3c3GGsmSimStatus=_H3c3GGsmSimStatus_Object((1,3,6,1,4,1,43,45,1,10,2,98,1,4,1,1,12),_H3c3GGsmSimStatus_Type())
h3c3GGsmSimStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3c3GGsmSimStatus.setStatus(_A)
_H3c3GModemTrap_ObjectIdentity=ObjectIdentity
h3c3GModemTrap=_H3c3GModemTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,98,2))
class _H3cDevSerialNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDevSerialNumber_Type.__name__=_D
_H3cDevSerialNumber_Object=MibScalar
h3cDevSerialNumber=_H3cDevSerialNumber_Object((1,3,6,1,4,1,43,45,1,10,2,98,2,1),_H3cDevSerialNumber_Type())
h3cDevSerialNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDevSerialNumber.setStatus(_A)
class _H3cDeviceOUI_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cDeviceOUI_Type.__name__=_D
_H3cDeviceOUI_Object=MibScalar
h3cDeviceOUI=_H3cDeviceOUI_Object((1,3,6,1,4,1,43,45,1,10,2,98,2,2),_H3cDeviceOUI_Type())
h3cDeviceOUI.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cDeviceOUI.setStatus(_A)
class _H3cAccessMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('air',2),('cable',3)))
_H3cAccessMedia_Type.__name__=_E
_H3cAccessMedia_Object=MibScalar
h3cAccessMedia=_H3cAccessMedia_Object((1,3,6,1,4,1,43,45,1,10,2,98,2,3),_H3cAccessMedia_Type())
h3cAccessMedia.setMaxAccess(_L)
if mibBuilder.loadTexts:h3cAccessMedia.setStatus(_A)
class _H3c3GCurrentService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('oneXRtt',2),('evDo',3),('gsm',4)))
_H3c3GCurrentService_Type.__name__=_E
_H3c3GCurrentService_Object=MibScalar
h3c3GCurrentService=_H3c3GCurrentService_Object((1,3,6,1,4,1,43,45,1,10,2,98,2,4),_H3c3GCurrentService_Type())
h3c3GCurrentService.setMaxAccess(_L)
if mibBuilder.loadTexts:h3c3GCurrentService.setStatus(_A)
class _H3c3GCurrentRssiBind_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-150,0))
_H3c3GCurrentRssiBind_Type.__name__=_E
_H3c3GCurrentRssiBind_Object=MibScalar
h3c3GCurrentRssiBind=_H3c3GCurrentRssiBind_Object((1,3,6,1,4,1,43,45,1,10,2,98,2,5),_H3c3GCurrentRssiBind_Type())
h3c3GCurrentRssiBind.setMaxAccess(_L)
if mibBuilder.loadTexts:h3c3GCurrentRssiBind.setStatus(_A)
if mibBuilder.loadTexts:h3c3GCurrentRssiBind.setUnits(_F)
class _H3c3GImsiBind_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3c3GImsiBind_Type.__name__=_D
_H3c3GImsiBind_Object=MibScalar
h3c3GImsiBind=_H3c3GImsiBind_Object((1,3,6,1,4,1,43,45,1,10,2,98,2,6),_H3c3GImsiBind_Type())
h3c3GImsiBind.setMaxAccess(_L)
if mibBuilder.loadTexts:h3c3GImsiBind.setStatus(_A)
_H3c3GModemTraps_ObjectIdentity=ObjectIdentity
h3c3GModemTraps=_H3c3GModemTraps_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,98,3))
_H3c3GModemTrapPrefix_ObjectIdentity=ObjectIdentity
h3c3GModemTrapPrefix=_H3c3GModemTrapPrefix_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,98,3,0))
h3cWirelessCardInserted=NotificationType((1,3,6,1,4,1,43,45,1,10,2,98,3,0,1))
h3cWirelessCardInserted.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_N)))
if mibBuilder.loadTexts:h3cWirelessCardInserted.setStatus(_A)
h3cWirelessCardPulledOut=NotificationType((1,3,6,1,4,1,43,45,1,10,2,98,3,0,2))
h3cWirelessCardPulledOut.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_N)))
if mibBuilder.loadTexts:h3cWirelessCardPulledOut.setStatus(_A)
h3cUIMPinInvalid=NotificationType((1,3,6,1,4,1,43,45,1,10,2,98,3,0,3))
h3cUIMPinInvalid.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_N)))
if mibBuilder.loadTexts:h3cUIMPinInvalid.setStatus(_A)
h3cUIMPinChanged=NotificationType((1,3,6,1,4,1,43,45,1,10,2,98,3,0,4))
h3cUIMPinChanged.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_N),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:h3cUIMPinChanged.setStatus(_A)
h3cAccessMediaChanged=NotificationType((1,3,6,1,4,1,43,45,1,10,2,98,3,0,5))
h3cAccessMediaChanged.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_N),(_B,_V)))
if mibBuilder.loadTexts:h3cAccessMediaChanged.setStatus(_A)
h3c3GRssiStrongSignalTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,98,3,0,6))
h3c3GRssiStrongSignalTrap.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h3c3GRssiStrongSignalTrap.setStatus(_A)
h3c3GRssiMediumSignalTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,98,3,0,7))
h3c3GRssiMediumSignalTrap.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h3c3GRssiMediumSignalTrap.setStatus(_A)
h3c3GRssiWeakSignalTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,98,3,0,8))
h3c3GRssiWeakSignalTrap.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h3c3GRssiWeakSignalTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'H3cUIMStatusType':H3cUIMStatusType,'h3c3GModem':h3c3GModem,'h3c3GModemObjects':h3c3GModemObjects,'h3cWirelessCard':h3cWirelessCard,'h3cWirelessCardTable':h3cWirelessCardTable,'h3cWirelessCardEntry':h3cWirelessCardEntry,_G:h3cWirelessCardIndex,'h3cWirelessCardModelName':h3cWirelessCardModelName,'h3cWirelessCardMfgName':h3cWirelessCardMfgName,'h3cWirelessCardDescription':h3cWirelessCardDescription,_J:h3cWirelessCardSerialNumber,'h3cWirelessCardCMIIID':h3cWirelessCardCMIIID,'h3cWirelessCardHardwareVersion':h3cWirelessCardHardwareVersion,'h3cWirelessCardFirmwareVersion':h3cWirelessCardFirmwareVersion,'h3cWirelessCardPRLVersion':h3cWirelessCardPRLVersion,'h3cWirelessCardInterfaceIndex':h3cWirelessCardInterfaceIndex,'h3cWirelessCardModemStatus':h3cWirelessCardModemStatus,'h3cWirelessCardCurServiceStatus':h3cWirelessCardCurServiceStatus,'h3cWirelessCardCurRoamingStatus':h3cWirelessCardCurRoamingStatus,'h3cUIM':h3cUIM,'h3cUIMInfoTable':h3cUIMInfoTable,'h3cUIMInfoEntry':h3cUIMInfoEntry,_S:h3cUIMIndex,'h3cUIMStatus':h3cUIMStatus,_N:h3cUIMImsi,_U:h3cUIMPin,'h3cUIMVoltage':h3cUIMVoltage,'h3cUIMProvider':h3cUIMProvider,'h3cUIMSignal':h3cUIMSignal,'h3cUIMTryPinPukTimes':h3cUIMTryPinPukTimes,_T:h3cUIMOldPin,'h3c3GCdma':h3c3GCdma,'h3c3GCdma1xRttTable':h3c3GCdma1xRttTable,'h3c3GCdma1xRttEntry':h3c3GCdma1xRttEntry,'h3c3GCdma1xRttCurrentRssi':h3c3GCdma1xRttCurrentRssi,'h3c3GCdma1xRttRssiMediumThreshold':h3c3GCdma1xRttRssiMediumThreshold,'h3c3GCdma1xRttRssiWeakThreshold':h3c3GCdma1xRttRssiWeakThreshold,'h3c3GCdmaEvDoTable':h3c3GCdmaEvDoTable,'h3c3GCdmaEvDoEntry':h3c3GCdmaEvDoEntry,'h3c3GCdmaEvDoCurrentRssi':h3c3GCdmaEvDoCurrentRssi,'h3c3GCdmaEvDoRssiMediumThreshold':h3c3GCdmaEvDoRssiMediumThreshold,'h3c3GCdmaEvDoRssiWeakThreshold':h3c3GCdmaEvDoRssiWeakThreshold,'h3c3GGsm':h3c3GGsm,'h3c3GGsmInfoTable':h3c3GGsmInfoTable,'h3c3GGsmInfoEntry':h3c3GGsmInfoEntry,'h3c3GGsmCurrentRssi':h3c3GGsmCurrentRssi,'h3c3GGsmRssiMediumThreshold':h3c3GGsmRssiMediumThreshold,'h3c3GGsmRssiWeakThreshold':h3c3GGsmRssiWeakThreshold,'h3c3GGsmImsi':h3c3GGsmImsi,'h3c3GGsmImei':h3c3GGsmImei,'h3c3GGsmApn':h3c3GGsmApn,'h3c3GGsmPacketSessionStatus':h3c3GGsmPacketSessionStatus,'h3c3GGsmNetworkSelectionMode':h3c3GGsmNetworkSelectionMode,'h3c3GGsmMobileNetworkName':h3c3GGsmMobileNetworkName,'h3c3GGsmLac':h3c3GGsmLac,'h3c3GGsmCellId':h3c3GGsmCellId,'h3c3GGsmSimStatus':h3c3GGsmSimStatus,'h3c3GModemTrap':h3c3GModemTrap,_I:h3cDevSerialNumber,_H:h3cDeviceOUI,_V:h3cAccessMedia,_O:h3c3GCurrentService,_P:h3c3GCurrentRssiBind,_Q:h3c3GImsiBind,'h3c3GModemTraps':h3c3GModemTraps,'h3c3GModemTrapPrefix':h3c3GModemTrapPrefix,'h3cWirelessCardInserted':h3cWirelessCardInserted,'h3cWirelessCardPulledOut':h3cWirelessCardPulledOut,'h3cUIMPinInvalid':h3cUIMPinInvalid,'h3cUIMPinChanged':h3cUIMPinChanged,'h3cAccessMediaChanged':h3cAccessMediaChanged,'h3c3GRssiStrongSignalTrap':h3c3GRssiStrongSignalTrap,'h3c3GRssiMediumSignalTrap':h3c3GRssiMediumSignalTrap,'h3c3GRssiWeakSignalTrap':h3c3GRssiWeakSignalTrap})